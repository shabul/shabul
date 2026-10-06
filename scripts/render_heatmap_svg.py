"""Render the contribution calendar as a self-contained, animated SVG."""

from __future__ import annotations

import json
from datetime import date
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PALETTE = ["#202b36", "#125045", "#167a5d", "#20a67a", "#4ee0a5"]
STEP = 14
LEFT = 58
TOP = 52


def main() -> None:
    payload = json.loads((ROOT / "data" / "contributions.json").read_text())
    stats = json.loads((ROOT / "data" / "profile_stats.json").read_text())
    if payload["through"] != stats["through"]:
        raise RuntimeError("Contribution calendar and profile stats have different dates")
    days = payload["days"]
    first = date.fromisoformat(days[0]["date"])
    first_sunday = first.toordinal() - (first.weekday() + 1) % 7
    last_week = max((date.fromisoformat(day["date"]).toordinal() - first_sunday) // 7 for day in days)

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="860" height="224" viewBox="0 0 860 224" role="img" aria-labelledby="title desc">',
        '<title id="title">Shabul\'s public GitHub contributions</title>',
        f'<desc id="desc">Animated public contribution calendar through {escape(payload["through"])}. {stats["public_repos_updated_this_year"]} public repositories updated in {stats["year"]}; {stats["public_repos"]} public repositories and {stats["years_on_github"]} years on GitHub.</desc>',
        '<rect width="860" height="224" rx="18" fill="#0d1722"/>',
        '<rect x=".5" y=".5" width="859" height="223" rx="17.5" fill="none" stroke="#274253"/>',
        '<circle cx="23" cy="22" r="4" fill="#f07178"/><circle cx="38" cy="22" r="4" fill="#e7b963"/><circle cx="53" cy="22" r="4" fill="#57c991"/>',
        '<text x="75" y="26" fill="#91a8b5" font-family="monospace" font-size="12">~/activity/contributions.log</text>',
        '<line x1="0" y1="38" x2="860" y2="38" stroke="#274253"/>',
    ]

    month_positions: list[tuple[str, int]] = []
    for day in days:
        current = date.fromisoformat(day["date"])
        week = (current.toordinal() - first_sunday) // 7
        if current.day == 1 or current == first:
            month_positions.append((current.strftime("%b"), week))
    for month, week in month_positions:
        x = LEFT + week * STEP
        if x < 800:
            parts.append(f'<text x="{x}" y="49" fill="#91a8b5" font-family="monospace" font-size="10">{month}</text>')

    for label, row in (("Mon", 1), ("Wed", 3), ("Fri", 5)):
        parts.append(f'<text x="17" y="{TOP + row * STEP + 9}" fill="#718a9a" font-family="monospace" font-size="10">{label}</text>')

    for day in days:
        current = date.fromisoformat(day["date"])
        week = (current.toordinal() - first_sunday) // 7
        row = (current.weekday() + 1) % 7
        x = LEFT + week * STEP
        y = TOP + row * STEP
        level = min(max(int(day["level"]), 0), 4)
        delay = 0.05 + (week / max(last_week, 1) * 1.3) + (row * 0.035)
        parts.append(
            f'<rect x="{x}" y="{y}" width="10" height="10" rx="2" fill="{PALETTE[level]}">'
            f'<animate attributeName="opacity" from="0" to="1" dur="0.45s" begin="{delay:.2f}s" fill="freeze"/>'
            '</rect>'
        )

    parts.extend([
        '<line x1="19" y1="165" x2="841" y2="165" stroke="#274253"/>',
        '<line x1="303" y1="176" x2="303" y2="213" stroke="#274253"/>',
        '<line x1="553" y1="176" x2="553" y2="213" stroke="#274253"/>',
        f'<text x="23" y="201" fill="#e9f3f3" font-family="monospace" font-size="25" font-weight="bold">{stats["public_repos_updated_this_year"]}</text>',
        f'<text x="65" y="190" fill="#d9e8e8" font-family="monospace" font-size="12">public repos updated</text>',
        f'<text x="65" y="208" fill="#91a8b5" font-family="monospace" font-size="11">in {stats["year"]}</text>',
        f'<text x="323" y="201" fill="#e9f3f3" font-family="monospace" font-size="25" font-weight="bold">{stats["public_repos"]}</text>',
        '<text x="365" y="196" fill="#d9e8e8" font-family="monospace" font-size="12">public repositories</text>',
        f'<text x="573" y="201" fill="#e9f3f3" font-family="monospace" font-size="25" font-weight="bold">{stats["years_on_github"]}</text>',
        '<text x="601" y="196" fill="#d9e8e8" font-family="monospace" font-size="12">years on GitHub</text>',
    ])
    parts.append('</svg>')
    (ROOT / "activity-card.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("Rendered activity-card.svg")


if __name__ == "__main__":
    main()
