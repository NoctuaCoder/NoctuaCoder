import importlib.util
import json
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "generate_command_center.py"
SPEC = importlib.util.spec_from_file_location("command_center", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class CommandCenterTests(unittest.TestCase):
    def test_escape_xml_handles_untrusted_text(self):
        self.assertEqual(MODULE.escape_xml('<tag attr="x">'), "&lt;tag attr=&quot;x&quot;&gt;")

    def test_normalize_languages_returns_sorted_percentages(self):
        result = MODULE.normalize_languages({"Rust": 50, "Python": 25, "QML": 25})
        self.assertEqual([item["name"] for item in result], ["Rust", "Python", "QML"])
        self.assertEqual([item["percent"] for item in result], [50.0, 25.0, 25.0])

    def test_normalize_languages_ignores_zero_values(self):
        self.assertEqual(MODULE.normalize_languages({"Rust": 0}), [])

    def test_normalize_contribution_levels_pads_days_and_limits_weeks(self):
        weeks = [
            {
                "contributionDays": [
                    {"contributionLevel": "FOURTH_QUARTILE"},
                    {"contributionLevel": "NONE"},
                ]
            }
        ]
        result = MODULE.normalize_contribution_levels(weeks)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], [4, 0, 0, 0, 0, 0, 0])

    def test_render_svg_contains_real_summary_data_and_accessibility_text(self):
        data = {
            "public_repos": 4,
            "stars": 7,
            "followers": 3,
            "contributions": 129,
            "generated_at": "2026-08-27 12:00 UTC",
            "projects": [
                {"name": "noctua-niri", "area": "LINUX DESKTOP", "stack": "Niri / QML", "stars": 2}
            ],
            "languages": [{"name": "Rust", "percent": 55.0}],
            "contribution_columns": [[1, 0, 2, 0, 3, 0, 4]],
        }
        output = MODULE.render_svg(data)
        self.assertIn('aria-labelledby="title desc"', output)
        self.assertIn("Nocturne Command Center", output)
        self.assertIn("129", output)
        self.assertIn("noctua-niri", output)
        self.assertIn("55.0%", output)

    def test_render_svg_escapes_project_names(self):
        data = {
            "public_repos": 0,
            "stars": 0,
            "followers": 0,
            "contributions": 0,
            "generated_at": "now",
            "projects": [{"name": '<unsafe>', "area": "AREA", "stack": "Rust", "stars": 0}],
            "languages": [],
            "contribution_columns": [],
        }
        output = MODULE.render_svg(data)
        self.assertIn("&lt;unsafe&gt;", output)
        self.assertNotIn("<unsafe>", output)


if __name__ == "__main__":
    unittest.main()
