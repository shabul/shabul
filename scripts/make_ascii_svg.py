"""Create a self-typing ASCII portrait from Shabul's GitHub avatar.

Requires Pillow locally: python3 -m pip install Pillow
"""

from __future__ import annotations

from html import escape
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
PHOTO_URL = "https://avatars.githubusercontent.com/u/38516249?v=4&s=800"
RAMP = " .`:-=+*cs#%@"
COLS = 68
ROWS = 45


def main() -> None:
    request = Request(PHOTO_URL, headers={"User-Agent": "shabul-profile-readme/1.0"})
    with urlopen(request, timeout=30) as response:
        photo = Image.open(BytesIO(response.read())).convert("RGB")

    # The avatar already has a clean white background, which maps to spaces.
    gray = ImageOps.autocontrast(ImageOps.grayscale(photo), cutoff=1)
    pixels = gray.resize((COLS, ROWS), Image.Resampling.LANCZOS)

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="345" height="436" viewBox="0 0 345 436" role="img" aria-labelledby="title desc">',
        '<title id="title">ASCII portrait of Shabul Hussain Abdul</title>',
        '<desc id="desc">A monochrome portrait that types itself line by line.</desc>',
        '<rect width="345" height="436" rx="18" fill="#0d1722"/>',
        '<rect x=".5" y=".5" width="344" height="435" rx="17.5" fill="none" stroke="#274253"/>',
        '<circle cx="23" cy="22" r="4" fill="#f07178"/><circle cx="38" cy="22" r="4" fill="#e7b963"/><circle cx="53" cy="22" r="4" fill="#57c991"/>',
        '<text x="75" y="26" fill="#91a8b5" font-family="monospace" font-size="12">~/portraits/shabul.txt</text>',
        '<line x1="0" y1="38" x2="345" y2="38" stroke="#274253"/>',
        '<defs>',
    ]
    for row in range(ROWS):
        parts.append(
            f'<clipPath id="row-{row}"><rect x="15" y="{52 + row * 8}" width="315" height="9">'
            f'<animate attributeName="width" from="0" to="315" dur="0.52s" begin="{row * 0.028:.2f}s" fill="freeze"/>'
            '</rect></clipPath>'
        )
    parts.append('</defs>')
    for row in range(ROWS):
        glyphs = "".join(RAMP[round((255 - pixels.getpixel((col, row))) / 255 * (len(RAMP) - 1))] for col in range(COLS))
        parts.append(
            f'<text x="17" y="{59 + row * 8}" clip-path="url(#row-{row})" xml:space="preserve" '
            f'fill="#c8e7df" font-family="monospace" font-size="8" textLength="311" lengthAdjust="spacing">{escape(glyphs)}</text>'
        )
    parts.append('</svg>')
    (ROOT / "shabul-ascii.svg").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("Rendered shabul-ascii.svg")


if __name__ == "__main__":
    main()
