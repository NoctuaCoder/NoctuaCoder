# Noctua profile automations

The profile presentation includes two generated contribution visuals. Both are maintained as scheduled GitHub Actions and can also be started manually from the Actions tab.

## Contribution Snake

The workflow in `.github/workflows/snake.yml` reads the public contribution calendar for the repository owner and publishes two SVG files to the `output` branch:

- `github-contribution-grid-snake.svg` for the light presentation.
- `github-contribution-grid-snake-dark.svg` for the dark presentation.

The outputs use the Noctua Editorial palette. The five dot colors progress from Pearl through Lilac Dust, Matcha Cream, Slate Gray, and a deeper Slate Gray. The snake itself uses Slate Gray in the light presentation and Honey Haze in the dark presentation.

## 3D contribution calendar

The workflow in `.github/workflows/profile-3d.yml` uses `conf/github-profile-3d-contrib.json` to generate light and night variants. The generated files are published to the `output-3d-contrib` branch:

- `day.svg` for the light presentation.
- `night.svg` for the dark presentation.

The README uses the HTML `picture` element so GitHub can select the matching image for the viewer's color scheme.

## Schedule and manual runs

Both workflows run once per day and support `workflow_dispatch`. A manual run is useful after changing the color configuration or when the profile should refresh immediately. The generated branches are intentionally separate from `main`, keeping the source files and the profile presentation easy to review.

## Safe maintenance checklist

When changing a generated visual, update the source workflow or configuration first, run the workflow manually, and verify the resulting raw SVG URL before changing the README path. Keep `contents: write` limited to the workflow that publishes generated assets. Avoid adding personal access tokens when the default workflow token is sufficient.

## Related files

- `README.md` — English profile presentation.
- `README.pt-BR.md` — Portuguese profile presentation.
- `docs/PROFILE_PALETTE.md` — color system and usage rules.
- `.github/workflows/snake.yml` — animated Snake generation.
- `.github/workflows/profile-3d.yml` — 3D calendar generation.
- `conf/github-profile-3d-contrib.json` — 3D color configuration.
