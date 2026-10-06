# Profile art maintenance

The README embeds three self-contained SVGs. `info-card.svg` contains the short professional bio; `contrib-heatmap.svg` uses GitHub's public contribution calendar and public repository statistics; `search-card.svg` is a designed preview of a linked Google AI Mode answer. The graph uses public data only; the signed-in GitHub profile may also show private activity.

To regenerate the static art locally:

```sh
python3 scripts/make_info_card.py
python3 scripts/make_search_card.py
```

To refresh the calendar manually:

```sh
python3 scripts/fetch_contributions.py
python3 scripts/fetch_profile_stats.py
python3 scripts/render_heatmap_svg.py
```

The scheduled GitHub Action runs the last three commands daily using only Python's standard library. It commits changes when the public data or SVG has changed. The displayed repository counts come from the public GitHub API; "updated" means the repository's latest push was in the displayed calendar year. To update the bio, edit `make_info_card.py` and regenerate its SVG.
