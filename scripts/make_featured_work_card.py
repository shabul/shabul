"""Render a proof-of-work card for Shabul's public AI projects."""

from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def text(x: int, y: int, value: str, *, color: str, size: int, weight: str = "normal") -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-family="monospace" '
        f'font-size="{size}" font-weight="{weight}">{escape(value)}</text>'
    )


def main() -> None:
    projects = [
        ("01 / MODEL FOUNDRY", "Fine-tuned LLMs", "5 public model releases", "Qwen2.5 · Gemma 2 · Mistral"),
        ("02 / POCKET BRAIN", "LLM on Android", "Gemma 2B served as an API", "Termux · self-hosted"),
        ("03 / CLAUDE LOCAL API", "Tools via Unix socket", "CLI access for local scripts", "Python · local tooling"),
    ]
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="860" height="322" viewBox="0 0 860 322" role="img" aria-labelledby="title desc">',
        '<title id="title">Selected public AI work by Shabul Abdul</title>',
        '<desc id="desc">Model Foundry includes five public fine-tuned language model releases. Pocket Brain serves an LLM from Android. Claude Local API connects local scripts to the Claude Code CLI through a Unix socket.</desc>',
        '<rect width="860" height="322" rx="18" fill="#0d1722"/>',
        '<rect x=".5" y=".5" width="859" height="321" rx="17.5" fill="none" stroke="#274253"/>',
        '<circle cx="23" cy="22" r="4" fill="#f07178"/><circle cx="38" cy="22" r="4" fill="#e7b963"/><circle cx="53" cy="22" r="4" fill="#57c991"/>',
        text(75, 26, "~/work/proof-of-build.ai", color="#91a8b5", size=12),
        '<line x1="0" y1="38" x2="860" y2="38" stroke="#274253"/>',
        text(25, 81, "Models trained. Systems made useful.", color="#e9f3f3", size=27, weight="bold"),
        text(26, 107, "Public projects with code, model artifacts, and reproducible details.", color="#91a8b5", size=12),
    ]
    for index, (eyebrow, heading, detail, tools) in enumerate(projects):
        x = 23 + index * 277
        parts.extend([
            f'<g><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="{0.18 + index * 0.16:.2f}s" fill="freeze"/>',
            f'<rect x="{x}" y="130" width="264" height="147" rx="10" fill="#14252c" stroke="#31514c"/>',
            f'<rect x="{x}" y="130" width="264" height="3" rx="1.5" fill="#4ee0a5"/>',
            text(x + 15, 158, eyebrow, color="#78d6b8", size=10),
            text(x + 15, 191, heading, color="#e9f3f3", size=17, weight="bold"),
            text(x + 15, 218, detail, color="#c9d9d7", size=11),
            f'<line x1="{x + 15}" y1="236" x2="{x + 249}" y2="236" stroke="#31514c"/>',
            text(x + 15, 258, tools, color="#91a8b5", size=10),
            '</g>',
        ])
    parts.extend([
        text(25, 306, "Explore the linked code and model cards below ↓", color="#78d6b8", size=11),
        '</svg>',
    ])
    (ROOT / "featured-work.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("Rendered featured-work.svg")


if __name__ == "__main__":
    main()
