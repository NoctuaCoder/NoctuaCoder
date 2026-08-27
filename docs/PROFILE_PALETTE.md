# Noctua Editorial palette

This profile uses a calm editorial palette inspired by observatories, printed paper, and quiet systems. The colors are intentionally restrained so the animated widgets remain readable instead of competing with the project descriptions.

## Core colors

| Name | Hex | Role |
| --- | --- | --- |
| Pearl | `#EAE0C8` | Light background, paper-like surfaces, and the lowest contribution level. |
| Slate Gray | `#708090` | Dark foundation, primary neutral, and structural lines. |
| Lilac Dust | `#C4B9C9` | Soft panels, borders, and atmospheric accents. |
| Honey Haze | `#FFEBC9` | Primary highlight, dark-mode text, and orbital light. |
| Matcha Cream | `#9CA764` | Activity markers, signal points, and secondary emphasis. |
| Milky Honey | `#F1E8C7` | Supporting light text and low-contrast highlights. |

## Usage rules

Use Slate Gray and Pearl as the principal surfaces. Use Honey Haze for important text and focal details, but keep it sparse so it retains its luminous character. Use Lilac Dust for secondary structure and Matcha Cream for small signals or activity states. Milky Honey should support, not replace, Honey Haze.

The light presentation favors Pearl as the main field with Slate Gray as the horizon and structural contrast. The dark presentation uses Slate Gray as the base, Lilac Dust as atmosphere, and Honey Haze as the primary light. Both modes should remain quiet, spacious, and legible.

## Accessibility and maintainability

When introducing a new widget, prefer a version that supports both light and dark modes. Keep text away from low-contrast decorative areas, and do not use Matcha Cream or Lilac Dust as the only indicator of meaning. External SVG services should be tested before being added to the README, and generated assets should keep stable filenames so cached profile links do not break.

## Related files

- `README.md` — English profile presentation.
- `README.pt-BR.md` — Portuguese profile presentation.
- `conf/github-profile-3d-contrib.json` — 3D contribution calendar colors.
- `.github/workflows/snake.yml` — Snake animation colors.
- `assets/noctua_editorial_header_light_wide.png` — Light cover.
- `assets/noctua_editorial_header_twilight_wide.png` — Dark cover.
