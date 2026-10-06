# Profile art maintenance

The README embeds three self-contained SVGs. `featured-work.svg` highlights three public AI projects with verifiable code and model artifacts; `info-card.svg` contains the short professional bio; `search-card.svg` is a designed preview of a linked Google AI Mode answer. The model-release count comes from the five published LLMs listed in `shabul/model-foundry` and linked on Hugging Face. It does not include the in-progress ModernBERT project.

To regenerate the static art locally:

```sh
python3 scripts/make_info_card.py
python3 scripts/make_featured_work_card.py
python3 scripts/make_search_card.py
```

All three cards are static and use only Python's standard library for regeneration. To update the bio, edit `make_info_card.py` and regenerate its SVG. To change the featured projects, edit `make_featured_work_card.py` and regenerate the card.
