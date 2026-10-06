"""Fetch the public GitHub contribution calendar without an API token."""

from __future__ import annotations

import json
import re
from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
USERNAME = "shabul"
URL = f"https://github.com/users/{USERNAME}/contributions"


class CalendarParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.days: dict[str, dict[str, int | str]] = {}
        self.cell_ids: dict[str, str] = {}
        self.tooltip_for: str | None = None
        self.tooltip_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "td" and attributes.get("data-date"):
            day = attributes["data-date"]
            assert day is not None
            self.days[day] = {
                "date": day,
                "level": int(attributes.get("data-level") or 0),
                "count": 0,
            }
            if attributes.get("id"):
                self.cell_ids[attributes["id"]] = day  # type: ignore[index]
        if tag == "tool-tip" and attributes.get("for"):
            self.tooltip_for = attributes["for"]
            self.tooltip_text = []

    def handle_data(self, data: str) -> None:
        if self.tooltip_for:
            self.tooltip_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "tool-tip" and self.tooltip_for:
            day = self.cell_ids.get(self.tooltip_for)
            if day:
                match = re.search(r"([\d,]+) contributions?", "".join(self.tooltip_text))
                if match:
                    self.days[day]["count"] = int(match.group(1).replace(",", ""))
            self.tooltip_for = None


def main() -> None:
    request = Request(URL, headers={"User-Agent": "shabul-profile-readme/1.0"})
    with urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8")

    parser = CalendarParser()
    parser.feed(html)
    days = sorted(parser.days.values(), key=lambda day: str(day["date"]))
    if not 365 <= len(days) <= 371:
        raise RuntimeError(f"Expected a year of contribution days, got {len(days)}")
    if not any(day["count"] for day in days):
        raise RuntimeError("No contribution counts parsed; GitHub's calendar may have changed")

    dates = [date.fromisoformat(str(day["date"])) for day in days]
    if any(right - left != timedelta(days=1) for left, right in zip(dates, dates[1:])):
        raise RuntimeError("Contribution calendar has missing dates")

    payload = {
        "username": USERNAME,
        "through": str(dates[-1]),
        "total": sum(int(day["count"]) for day in days),
        "active_days": sum(int(day["count"]) > 0 for day in days),
        "days": days,
    }
    summary = re.search(r"([\d,]+)\s+contributions?\s+in the last year", html)
    if summary and payload["total"] != int(summary.group(1).replace(",", "")):
        raise RuntimeError("Parsed day counts do not match GitHub's displayed yearly total")
    destination = ROOT / "data" / "contributions.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {len(days)} days and {payload['total']} contributions")


if __name__ == "__main__":
    main()
