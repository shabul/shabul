# Profile art maintenance

The README embeds two self-contained SVGs. `info-card.svg` contains the short professional bio; `contrib-heatmap.svg` uses GitHub's public contribution calendar. Its total may differ from the signed-in GitHub profile, which can also show private activity.

To regenerate the static art locally:

```sh
python3 scripts/make_info_card.py
```

To refresh the calendar manually:

```sh
python3 scripts/fetch_contributions.py
python3 scripts/render_heatmap_svg.py
```

The scheduled GitHub Action runs the last two commands daily using only Python's standard library. It commits changes when the calendar data or SVG has changed. To update the bio, edit `make_info_card.py` and regenerate its SVG.
