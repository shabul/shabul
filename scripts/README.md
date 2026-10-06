# Profile art maintenance

The README embeds three self-contained SVGs. `shabul-ascii.svg` uses the public GitHub avatar; `info-card.svg` contains the short professional bio; `contrib-heatmap.svg` uses GitHub's public contribution calendar.

To regenerate the static art locally:

```sh
python3 -m pip install Pillow
python3 scripts/make_ascii_svg.py
python3 scripts/make_info_card.py
```

To refresh the calendar manually:

```sh
python3 scripts/fetch_contributions.py
python3 scripts/render_heatmap_svg.py
```

The scheduled GitHub Action runs the last two commands daily using only Python's standard library. It commits changes when the calendar data or SVG has changed. To update the bio, edit `make_info_card.py` and regenerate its SVG.
