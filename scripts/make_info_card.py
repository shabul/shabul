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
        '<svg xmlns="http://www.w3.org/2000/svg" width="860" height="320" viewBox="0 0 860 320" role="img" aria-labelledby="title desc">',
        '<title id="title">About Shabul Hussain Abdul</title>',
        '<desc id="desc">Senior Data Scientist at JPMorgan Chase. Building machine learning platforms, LLM products, and agentic AI systems in India.</desc>',
        '<rect width="860" height="320" rx="18" fill="#0d1722"/>',
        '<rect x=".5" y=".5" width="859" height="319" rx="17.5" fill="none" stroke="#274253"/>',
        '<circle cx="23" cy="22" r="4" fill="#f07178"/><circle cx="38" cy="22" r="4" fill="#e7b963"/><circle cx="53" cy="22" r="4" fill="#57c991"/>',
        '<text x="75" y="26" fill="#91a8b5" font-family="monospace" font-size="12">shabul@github:~$ whoami</text>',
        '<line x1="0" y1="38" x2="860" y2="38" stroke="#274253"/>',
        '<line x1="322" y1="58" x2="322" y2="296" stroke="#274253"/>',
    ]
    parts.append(animated('<text x="28" y="137" fill="#eaf6f3" font-family="monospace" font-size="51" font-weight="bold" letter-spacing="3">SHABUL</text>', 0.1))
    parts.append(animated('<text x="31" y="162" fill="#56dcb0" font-family="monospace" font-size="13" letter-spacing="3">HUSSAIN ABDUL</text>', 0.22))
    parts.append('<line x1="31" y1="184" x2="283" y2="184" stroke="#3b7d76"/>')
    parts.append(animated('<text x="31" y="212" fill="#d9e8e8" font-family="monospace" font-size="13">Senior Data Scientist</text>', 0.34))
    parts.append(animated('<text x="31" y="237" fill="#91a8b5" font-family="monospace" font-size="12">Hyderabad / Bengaluru, India</text>', 0.44))
    parts.append(animated('<text x="31" y="289" fill="#56dcb0" font-family="monospace" font-size="12">shabul.github.io ↗</text>', 1.3))
    parts.append(animated('<text x="351" y="77" fill="#6e99a9" font-family="monospace" font-size="11">PROFILE</text>', 0.26))
    parts.append(animated('<text x="351" y="106" fill="#eaf6f3" font-family="monospace" font-size="18" font-weight="bold">Building AI that works in production.</text>', 0.36))
    rows = [
        ("NOW", "JPMorgan Chase · Data Science"),
        ("BEFORE", "Amazon · TCS"),
        ("EXPERIENCE", "7+ years in ML & data science"),
        ("AWARD", "Amazon 2024 Innovista winner"),
    ]
    for index, (label, value) in enumerate(rows):
        y = 134 + index * 22
        parts.append(animated(
            f'<text x="351" y="{y}" fill="#7cd5bf" font-family="monospace" font-size="11">{escape(label)}</text>'
            f'<text x="454" y="{y}" fill="#d9e8e8" font-family="monospace" font-size="12">{escape(value)}</text>',
            0.48 + index * 0.09,
        ))
    parts.append('<line x1="351" y1="216" x2="830" y2="216" stroke="#274253"/>')
    parts.append(animated('<text x="351" y="238" fill="#6e99a9" font-family="monospace" font-size="11">CURRENT FOCUS</text>', 0.89))
    focus = [
        "LLM products & agentic workflows",
        "Retrieval, GenAI & trusted automation",
        "ML platforms at enterprise scale",
    ]
    for index, line in enumerate(focus):
        y = 260 + index * 21
        parts.append(animated(
            f'<text x="351" y="{y}" fill="#d9e8e8" font-family="monospace" font-size="12"><tspan fill="#56dcb0">&gt;</tspan> {escape(line)}</text>',
            0.98 + index * 0.1,
        ))
    parts.append('</svg>')
    (ROOT / "info-card.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("Rendered info-card.svg")


if __name__ == "__main__":
    main()
