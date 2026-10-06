"""Render Shabul's neofetch-inspired profile card as an animated SVG."""

from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def animated(content: str, delay: float) -> str:
    return (
        f'<g>{content}<animate attributeName="opacity" from="0" to="1" '
        f'dur="0.4s" begin="{delay:.2f}s" fill="freeze"/></g>'
    )


def main() -> None:
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="505" height="436" viewBox="0 0 505 436" role="img" aria-labelledby="title desc">',
        '<title id="title">About Shabul Hussain Abdul</title>',
        '<desc id="desc">Senior Data Scientist at JPMorgan Chase. Building machine learning platforms, LLM products, and agentic AI systems in India.</desc>',
        '<rect width="505" height="436" rx="18" fill="#0d1722"/>',
        '<rect x=".5" y=".5" width="504" height="435" rx="17.5" fill="none" stroke="#274253"/>',
        '<circle cx="23" cy="22" r="4" fill="#f07178"/><circle cx="38" cy="22" r="4" fill="#e7b963"/><circle cx="53" cy="22" r="4" fill="#57c991"/>',
        '<text x="75" y="26" fill="#91a8b5" font-family="monospace" font-size="12">shabul@github:~$ whoami</text>',
        '<line x1="0" y1="38" x2="505" y2="38" stroke="#274253"/>',
    ]
    parts.append(animated('<text x="24" y="79" fill="#eaf6f3" font-family="monospace" font-size="22" font-weight="bold">Shabul Hussain Abdul</text>', 0.1))
    parts.append(animated('<text x="24" y="103" fill="#56dcb0" font-family="monospace" font-size="12">Senior Data Scientist · JPMorgan Chase</text>', 0.2))
    parts.append('<line x1="24" y1="122" x2="481" y2="122" stroke="#274253"/>')
    parts.append(animated('<text x="24" y="148" fill="#6e99a9" font-family="monospace" font-size="11">PROFILE</text>', 0.3))
    rows = [
        ("Location", "Hyderabad / Bengaluru, India"),
        ("Previously", "Amazon · TCS"),
        ("Experience", "7+ years in ML & data science"),
        ("Recognition", "Amazon 2024 Innovista winner"),
    ]
    for index, (label, value) in enumerate(rows):
        y = 174 + index * 23
        parts.append(animated(
            f'<text x="24" y="{y}" fill="#7cd5bf" font-family="monospace" font-size="12">{escape(label)}</text>'
            f'<text x="132" y="{y}" fill="#d9e8e8" font-family="monospace" font-size="12">{escape(value)}</text>',
            0.38 + index * 0.1,
        ))
    parts.append('<line x1="24" y1="257" x2="481" y2="257" stroke="#274253"/>')
    parts.append(animated('<text x="24" y="283" fill="#6e99a9" font-family="monospace" font-size="11">CURRENT FOCUS</text>', 0.84))
    focus = [
        "LLM products & agentic workflows",
        "Retrieval, GenAI & trusted automation",
        "Reliable ML platforms at enterprise scale",
    ]
    for index, line in enumerate(focus):
        y = 309 + index * 24
        parts.append(animated(
            f'<text x="24" y="{y}" fill="#d9e8e8" font-family="monospace" font-size="13"><tspan fill="#56dcb0">&gt;</tspan> {escape(line)}</text>',
            0.94 + index * 0.1,
        ))
    parts.extend([
        '<line x1="24" y1="372" x2="481" y2="372" stroke="#274253"/>',
        animated('<text x="24" y="400" fill="#a3b9c2" font-family="monospace" font-size="12">Building AI that earns its place in production.</text>', 1.28),
        animated('<text x="24" y="422" fill="#56dcb0" font-family="monospace" font-size="11">shabul.github.io  ↗</text>', 1.38),
        '</svg>',
    ])
    (ROOT / "info-card.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("Rendered info-card.svg")


if __name__ == "__main__":
    main()
