"""Render a clearly labeled preview of Shabul's shared Google AI Mode answer."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="860" height="258" viewBox="0 0 860 258" role="img" aria-labelledby="title desc">',
        '<title id="title">AI Mode search result preview for Shabul Hussain</title>',
        '<desc id="desc">Designed preview of a shared AI-generated answer. It identifies Shabul Hussain Abdul as an AI and data science professional with experience at JPMorgan Chase and Amazon. The image links to the original conversation.</desc>',
        '<rect width="860" height="258" rx="18" fill="#f8fafc"/>',
        '<rect x=".5" y=".5" width="859" height="257" rx="17.5" fill="none" stroke="#d6dfe9"/>',
        '<circle cx="27" cy="25" r="5" fill="#4285f4"/><circle cx="42" cy="25" r="5" fill="#ea4335"/><circle cx="57" cy="25" r="5" fill="#fbbc05"/><circle cx="72" cy="25" r="5" fill="#34a853"/>',
        '<text x="91" y="30" fill="#334155" font-family="Arial, sans-serif" font-size="14" font-weight="bold">Google AI Mode</text>',
        '<text x="830" y="29" text-anchor="end" fill="#64748b" font-family="Arial, sans-serif" font-size="11">DESIGNED PREVIEW</text>',
        '<line x1="0" y1="46" x2="860" y2="46" stroke="#e1e7ef"/>',
        '<rect x="25" y="63" width="268" height="35" rx="17.5" fill="#e9eef5"/>',
        '<text x="42" y="85" fill="#334155" font-family="Arial, sans-serif" font-size="14">Who is Shabul Hussain?</text>',
        '<text x="27" y="136" fill="#18283c" font-family="Arial, sans-serif" font-size="25" font-weight="bold">Shabul Hussain Abdul</text>',
        '<text x="27" y="164" fill="#334155" font-family="Arial, sans-serif" font-size="15">The shared AI Mode answer describes Shabul as an AI and data science</text>',
        '<text x="27" y="185" fill="#334155" font-family="Arial, sans-serif" font-size="15">professional with experience at JPMorgan Chase and Amazon.</text>',
        '<line x1="26" y1="205" x2="834" y2="205" stroke="#e1e7ef"/>',
        '<text x="27" y="231" fill="#1967d2" font-family="Arial, sans-serif" font-size="13" font-weight="bold">Open the shared AI Mode answer ↗</text>',
        '<text x="832" y="231" text-anchor="end" fill="#64748b" font-family="Arial, sans-serif" font-size="11">AI-GENERATED SUMMARY</text>',
        '</svg>',
    ]
    (ROOT / "search-card.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("Rendered search-card.svg")


if __name__ == "__main__":
    main()
