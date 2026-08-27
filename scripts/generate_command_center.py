#!/usr/bin/env python3
"""Generate the Nocturne Command Center from public GitHub activity."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from typing import Any

OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "nocturne-command-center.svg"
GITHUB_API = "https://api.github.com"
GRAPHQL_API = "https://api.github.com/graphql"

PALETTE = {
    "slate_deep": "#3F4B56",
    "slate": "#52616D",
    "slate_gray": "#708090",
    "pearl": "#EAE0C8",
    "lilac": "#C4B9C9",
    "honey": "#FFEBC9",
    "matcha": "#9CA764",
    "milky": "#F1E8C7",
}

PROJECT_META = {
    "noctua-niri": ("LINUX DESKTOP", "Niri / QML"),
    "ArbiterAI": ("LOCAL CODING AGENTS", "Python"),
    "voidkitty-llm": ("LOCAL LLM TOOLING", "Rust"),
    "noctua-material": ("DESKTOP DESIGN", "QML"),
    "termlens": ("OPEN SOURCE CONTRIBUTION", "Rust"),
}

LEVELS = {
    "NONE": 0,
    "FIRST_QUARTILE": 1,
    "SECOND_QUARTILE": 2,
    "THIRD_QUARTILE": 3,
    "FOURTH_QUARTILE": 4,
}


def escape_xml(value: Any) -> str:
    """Escape untrusted GitHub data before putting it into SVG text."""

    return escape(str(value), quote=True)


def format_number(value: int) -> str:
    return f"{int(value):,}"


def normalize_languages(language_counts: dict[str, int], limit: int = 5) -> list[dict[str, Any]]:
    """Return top languages with percentages based on returned byte counts."""

    clean = {name: int(count) for name, count in language_counts.items() if int(count) > 0}
    total = sum(clean.values())
    if not total:
        return []

    top = sorted(clean.items(), key=lambda item: (-item[1], item[0]))[:limit]
    return [
        {
            "name": name,
            "bytes": count,
            "percent": round(count * 100 / total, 1),
        }
        for name, count in top
    ]


def normalize_contribution_levels(weeks: list[dict[str, Any]], limit: int = 52) -> list[list[int]]:
    """Convert GraphQL contribution levels into seven-row display columns."""

    recent = weeks[-limit:]
    columns: list[list[int]] = []
    for week in recent:
        days = week.get("contributionDays", [])
        column = [LEVELS.get(day.get("contributionLevel", "NONE"), 0) for day in days]
        columns.append((column + [0] * 7)[:7])
    return columns


def api_request(url: str, token: str) -> Any:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "nocturne-forge-command-center",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API request failed ({error.code}): {body[:240]}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"GitHub API request failed: {error.reason}") from error


def graphql_request(query: str, variables: dict[str, Any], token: str) -> dict[str, Any]:
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    request = urllib.request.Request(
        GRAPHQL_API,
        data=payload,
        method="POST",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "nocturne-forge-command-center",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.load(response)
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub GraphQL request failed ({error.code}): {body[:240]}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"GitHub GraphQL request failed: {error.reason}") from error

    if result.get("errors"):
        raise RuntimeError(f"GitHub GraphQL returned errors: {result['errors'][0].get('message', 'unknown error')}")
    return result["data"]


def fetch_public_data(login: str, token: str) -> dict[str, Any]:
    user = api_request(f"{GITHUB_API}/users/{urllib.parse.quote(login)}", token)
    repositories = api_request(
        f"{GITHUB_API}/users/{urllib.parse.quote(login)}/repos?type=owner&per_page=100&sort=updated",
        token,
    )
    all_public_repositories = [repo for repo in repositories if not repo.get("private")]
    public_repositories = [repo for repo in all_public_repositories if not repo.get("fork")]

    language_counts: Counter[str] = Counter()
    for repo in public_repositories:
        languages = api_request(repo["languages_url"], token)
        language_counts.update({str(name): int(count) for name, count in languages.items()})

    projects = []
    for repo in all_public_repositories:
        name = repo.get("name", "")
        if name in PROJECT_META:
            area, stack = PROJECT_META[name]
            projects.append(
                {
                    "name": name,
                    "area": area,
                    "stack": stack,
                    "stars": int(repo.get("stargazers_count", 0)),
                }
            )
    projects.sort(key=lambda project: list(PROJECT_META).index(project["name"]))

    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                contributionCount
                contributionLevel
              }
            }
          }
        }
      }
    }
    """
    contribution_data = graphql_request(query, {"login": login}, token)
    calendar = contribution_data["user"]["contributionsCollection"]["contributionCalendar"]

    return {
        "login": login,
        "public_repos": int(user.get("public_repos", len(public_repositories))),
        "stars": sum(int(repo.get("stargazers_count", 0)) for repo in public_repositories),
        "followers": int(user.get("followers", 0)),
        "contributions": int(calendar.get("totalContributions", 0)),
        "projects": projects,
        "languages": normalize_languages(dict(language_counts)),
        "contribution_columns": normalize_contribution_levels(calendar.get("weeks", [])),
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


def text(x: int, y: int, value: Any, *, size: int = 14, fill: str = "milky", weight: int = 400, anchor: str = "start", letter_spacing: int = 0) -> str:
    return (
        f'<text x="{x}" y="{y}" font-family="DejaVu Sans,Arial,sans-serif" '
        f'font-size="{size}px" font-weight="{weight}" fill="{PALETTE[fill]}" text-anchor="{anchor}" '
        f'letter-spacing="{letter_spacing}px">{escape_xml(value)}</text>'
    )


def card(x: int, y: int, width: int, height: int, title: str, value: str, detail: str, accent: str = "matcha") -> str:
    return "".join(
        [
            f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="16" fill="url(#card)" stroke="{PALETTE["lilac"]}" stroke-opacity=".60"/>',
            f'<circle cx="{x + 25}" cy="{y + 25}" r="4" fill="{PALETTE[accent]}" class="pulse"/>',
            text(x + 40, y + 30, title, size=11, fill="lilac", weight=600, letter_spacing=1),
            text(x + 25, y + 72, value, size=28, fill="honey", weight=700),
            text(x + 25, y + 97, detail, size=11, fill="milky"),
        ]
    )


def render_svg(data: dict[str, Any]) -> str:
    width, height = 1200, 860
    output: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Nocturne Command Center</title>',
        '<desc id="desc">A daily dashboard generated from public GitHub activity.</desc>',
        """<defs>
          <linearGradient id="background" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#3F4B56"/>
            <stop offset="52%" stop-color="#52616D"/>
            <stop offset="100%" stop-color="#708090"/>
          </linearGradient>
          <linearGradient id="card" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#52616D" stop-opacity=".95"/>
            <stop offset="100%" stop-color="#3F4B56" stop-opacity=".93"/>
          </linearGradient>
          <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="4" result="blur"/>
            <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
          </filter>
          <style>
            .pulse { animation: pulse 2.8s ease-in-out infinite; }
            .pulse2 { animation: pulse 2.8s .7s ease-in-out infinite; }
            @keyframes pulse { 0%,100% { opacity: .45; } 50% { opacity: 1; } }
          </style>
        </defs>
        <rect width="1200" height="860" rx="24" fill="url(#background)"/>
        <rect x="20" y="20" width="1160" height="820" rx="18" fill="none" stroke="#EAE0C8" stroke-opacity=".35"/>
        <circle cx="1100" cy="78" r="84" fill="#C4B9C9" opacity=".10" filter="url(#glow)"/>
        <circle cx="1100" cy="78" r="3" fill="#FFEBC9" class="pulse"/>
        """,
        text(54, 64, "NOCTURNE COMMAND CENTER", size=26, fill="honey", weight=700, letter_spacing=2),
        text(54, 91, "LOCAL SYSTEMS // OPEN SOURCE // PRACTICAL AI", size=11, fill="lilac", weight=600, letter_spacing=2),
        text(1146, 64, "PROFILE SIGNAL ONLINE", size=10, fill="matcha", weight=600, anchor="end", letter_spacing=1),
        text(1146, 91, data["generated_at"], size=10, fill="milky", anchor="end"),
        '<line x1="54" y1="116" x2="1146" y2="116" stroke="#C4B9C9" stroke-opacity=".40"/>',
        text(54, 145, "IMPACT SIGNAL", size=11, fill="lilac", weight=700, letter_spacing=2),
    ]

    total_width, gap, x0 = 1092, 16, 54
    card_width = (total_width - gap * 3) // 4
    impact = [
        ("PUBLIC REPOS", format_number(data["public_repos"]), "owned repositories", "matcha"),
        ("STARS RECEIVED", format_number(data["stars"]), "public repository stars", "honey"),
        ("FOLLOWERS", format_number(data["followers"]), "people following the work", "lilac"),
        ("CONTRIBUTIONS", format_number(data["contributions"]), "last 12 months", "matcha"),
    ]
    for index, (title_value, value, detail, accent) in enumerate(impact):
        output.append(card(x0 + index * (card_width + gap), 160, card_width, 116, title_value, value, detail, accent))

    output.extend(
        [
            text(54, 320, "SYSTEM MAP", size=11, fill="lilac", weight=700, letter_spacing=2),
            text(1146, 320, "PUBLIC PROJECTS", size=10, fill="milky", anchor="end", letter_spacing=1),
        ]
    )

    project_positions = [(54, 336), (610, 336), (54, 428), (610, 428)]
    for index, (x, y) in enumerate(project_positions):
        if index < len(data["projects"]):
            project = data["projects"][index]
            output.extend(
                [
                    f'<rect x="{x}" y="{y}" width="536" height="76" rx="14" fill="url(#card)" stroke="{PALETTE["lilac"]}" stroke-opacity=".55"/>',
                    f'<circle cx="{x + 23}" cy="{y + 23}" r="4" fill="{PALETTE["matcha"]}" class="pulse2"/>',
                    text(x + 38, y + 27, project["area"], size=10, fill="lilac", weight=600, letter_spacing=1),
                    text(x + 21, y + 57, project["name"], size=17, fill="honey", weight=700),
                    text(x + 500, y + 27, project["stack"], size=10, fill="milky", anchor="end"),
                    text(x + 500, y + 57, f'{format_number(project["stars"])} stars', size=11, fill="milky", anchor="end"),
                ]
            )
        else:
            output.append(f'<rect x="{x}" y="{y}" width="536" height="76" rx="14" fill="url(#card)" stroke="{PALETTE["lilac"]}" stroke-opacity=".30"/>')
            output.append(text(x + 21, y + 44, "PUBLIC PROJECT SLOT", size=11, fill="lilac", weight=600, letter_spacing=1))

    output.extend(
        [
            text(54, 552, "LANGUAGE MIX", size=11, fill="lilac", weight=700, letter_spacing=2),
            text(590, 552, "CONTRIBUTION SIGNAL", size=11, fill="lilac", weight=700, letter_spacing=2),
            '<rect x="54" y="568" width="500" height="220" rx="16" fill="url(#card)" stroke="#C4B9C9" stroke-opacity=".55"/>',
            '<rect x="590" y="568" width="556" height="220" rx="16" fill="url(#card)" stroke="#C4B9C9" stroke-opacity=".55"/>',
        ]
    )

    languages = data.get("languages", [])
    if languages:
        bar_x, bar_y, bar_width = 80, 605, 430
        colors = ["honey", "matcha", "lilac", "pearl", "milky"]
        cursor = bar_x
        for index, language in enumerate(languages):
            segment = max(2, round(bar_width * language["percent"] / 100))
            output.append(f'<rect x="{cursor}" y="{bar_y}" width="{segment}" height="12" fill="{PALETTE[colors[index % len(colors)]]}"/>')
            cursor += segment
        for index, language in enumerate(languages):
            row_y = 650 + index * 24
            output.extend(
                [
                    f'<circle cx="84" cy="{row_y - 4}" r="4" fill="{PALETTE[colors[index % len(colors)]]}"/>',
                    text(98, row_y, language["name"], size=12, fill="milky", weight=600),
                    text(520, row_y, f'{language["percent"]:.1f}%', size=12, fill="honey", weight=700, anchor="end"),
                ]
            )
    else:
        output.append(text(80, 650, "No language data returned", size=12, fill="lilac"))

    columns = data.get("contribution_columns", [])
    grid_x, grid_y, cell, cell_gap = 620, 610, 8, 2
    for column_index in range(52):
        column = columns[column_index] if column_index < len(columns) else [0] * 7
        for row_index in range(7):
            level = column[row_index]
            color = ["slate_gray", "slate", "matcha", "lilac", "honey"][level]
            output.append(
                f'<rect x="{grid_x + column_index * (cell + cell_gap)}" y="{grid_y + row_index * (cell + cell_gap)}" width="{cell}" height="{cell}" rx="2" fill="{PALETTE[color]}" opacity="{0.32 + level * 0.17:.2f}"/>'
            )
    output.extend(
        [
            text(620, 710, "52 WEEKS // PUBLIC CONTRIBUTION ACTIVITY", size=10, fill="milky", letter_spacing=1),
            '<line x1="620" y1="735" x2="1094" y2="735" stroke="#C4B9C9" stroke-opacity=".35"/>',
            text(620, 764, "quiet systems, visible work", size=12, fill="honey", weight=600),
            text(1094, 764, "NOCTURNE FORGE // v0.1", size=10, fill="lilac", weight=600, anchor="end", letter_spacing=1),
            text(54, 816, "generated from public GitHub activity · no private repository data included", size=10, fill="milky"),
            text(1146, 816, "NOCTURNE FORGE", size=10, fill="matcha", weight=700, anchor="end", letter_spacing=2),
            "</svg>",
        ]
    )
    return "".join(output)


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    login = os.environ.get("GITHUB_REPOSITORY_OWNER") or os.environ.get("NOCTURNE_GITHUB_LOGIN")
    if not token:
        print("GITHUB_TOKEN or GH_TOKEN is required", file=sys.stderr)
        return 2
    if not login:
        print("GITHUB_REPOSITORY_OWNER or NOCTURNE_GITHUB_LOGIN is required", file=sys.stderr)
        return 2

    try:
        data = fetch_public_data(login, token)
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(render_svg(data), encoding="utf-8")
        print(f"Generated {OUTPUT} for {login}")
        return 0
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
