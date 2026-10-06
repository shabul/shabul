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
        '<desc id="desc">Shabul Abdul, Senior Applied AI and ML Scientist at JPMorgan Chase. Focused on agent systems, model evaluation, model efficiency, and retrieval.</desc>',
        '<rect width="860" height="320" rx="18" fill="#0d1722"/>',
        '<rect x=".5" y=".5" width="859" height="319" rx="17.5" fill="none" stroke="#274253"/>',
        '<circle cx="23" cy="22" r="4" fill="#f07178"/><circle cx="38" cy="22" r="4" fill="#e7b963"/><circle cx="53" cy="22" r="4" fill="#57c991"/>',
        '<text x="75" y="26" fill="#91a8b5" font-family="monospace" font-size="12">shabul@github:~$ whoami</text>',
        '<line x1="0" y1="38" x2="860" y2="38" stroke="#274253"/>',
        '<line x1="322" y1="58" x2="322" y2="296" stroke="#274253"/>',
    ]
    parts.append(animated('<text x="28" y="137" fill="#eaf6f3" font-family="monospace" font-size="51" font-weight="bold" letter-spacing="3">SHABUL</text>', 0.1))
    parts.append(animated('<text x="31" y="162" fill="#56dcb0" font-family="monospace" font-size="13" letter-spacing="3">ABDUL</text>', 0.22))
    parts.append('<line x1="31" y1="184" x2="283" y2="184" stroke="#3b7d76"/>')
    parts.append(animated('<text x="31" y="212" fill="#d9e8e8" font-family="monospace" font-size="13">Applied AI / ML Scientist</text>', 0.34))
    parts.append(animated('<text x="31" y="237" fill="#91a8b5" font-family="monospace" font-size="12">Bengaluru, India</text>', 0.44))
    parts.append(animated('<text x="31" y="289" fill="#56dcb0" font-family="monospace" font-size="12">shabul.github.io ↗</text>', 1.3))
    parts.append(animated('<text x="351" y="77" fill="#6e99a9" font-family="monospace" font-size="11">CURRENT ROLE</text>', 0.26))
    parts.append(animated('<text x="351" y="106" fill="#eaf6f3" font-family="monospace" font-size="18" font-weight="bold">Sr. Applied AI/ML Scientist</text>', 0.36))
    parts.append(animated('<text x="351" y="130" fill="#56dcb0" font-family="monospace" font-size="12">JPMorgan Chase</text>', 0.44))
    parts.append('<line x1="351" y1="150" x2="830" y2="150" stroke="#274253"/>')
    parts.append(animated('<text x="351" y="174" fill="#6e99a9" font-family="monospace" font-size="11">WHAT I WORK ON</text>', 0.52))
    rows = [
        ("Agent systems", "Multi-agent workflows · MCP"),
        ("Model quality", "LLM evals · guardrails · prompt opt."),
        ("Model efficiency", "LoRA · quantization · distillation"),
        ("Retrieval", "RAG · vector & graph search"),
    ]
    for index, (label, value) in enumerate(rows):
        y = 199 + index * 22
        parts.append(animated(
            f'<text x="351" y="{y}" fill="#7cd5bf" font-family="monospace" font-size="11">{escape(label)}</text>'
            f'<text x="492" y="{y}" fill="#d9e8e8" font-family="monospace" font-size="12">{escape(value)}</text>',
            0.62 + index * 0.1,
        ))
    parts.append('<line x1="351" y1="278" x2="830" y2="278" stroke="#274253"/>')
    parts.append(animated('<text x="351" y="300" fill="#91a8b5" font-family="monospace" font-size="11">Previously: Amazon · TCS  |  7+ years in ML</text>', 1.1))
    parts.append('</svg>')
    (ROOT / "info-card.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("Rendered info-card.svg")


if __name__ == "__main__":
    main()
