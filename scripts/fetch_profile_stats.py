"""Fetch public repository statistics for the profile activity card."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
USERNAME = "shabul"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "shabul-profile-readme/1.0",
}


def fetch_json(url: str) -> object:
    with urlopen(Request(url, headers=HEADERS), timeout=30) as response:
        return json.load(response)


def main() -> None:
    profile = fetch_json(f"https://api.github.com/users/{USERNAME}")
    if not isinstance(profile, dict):
        raise RuntimeError("GitHub user response was not an object")

    repos: list[dict[str, object]] = []
    page = 1
    while True:
        batch = fetch_json(
            f"https://api.github.com/users/{USERNAME}/repos?type=owner&per_page=100&page={page}"
        )
        if not isinstance(batch, list) or not all(isinstance(repo, dict) for repo in batch):
            raise RuntimeError("GitHub repositories response was not a list of objects")
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    public_count = profile.get("public_repos")
    if not isinstance(public_count, int) or public_count != len(repos):
        raise RuntimeError("Public repository count did not match the repository list")
    if not isinstance(profile.get("created_at"), str):
        raise RuntimeError("GitHub account creation date was missing")

    today = date.fromisoformat(json.loads((ROOT / "data" / "contributions.json").read_text())["through"])
    created = date.fromisoformat(profile["created_at"][:10])
    years = today.year - created.year - ((today.month, today.day) < (created.month, created.day))
    updated_this_year = sum(
        isinstance(repo.get("pushed_at"), str)
        and str(repo["pushed_at"])[:4] == str(today.year)
        for repo in repos
    )

    payload = {
        "username": USERNAME,
        "through": today.isoformat(),
        "year": today.year,
        "public_repos": public_count,
        "public_repos_updated_this_year": updated_this_year,
        "years_on_github": years,
    }
    destination = ROOT / "data" / "profile_stats.json"
    destination.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Saved public profile stats: {updated_this_year}/{public_count} repos updated in {today.year}")


if __name__ == "__main__":
    main()
