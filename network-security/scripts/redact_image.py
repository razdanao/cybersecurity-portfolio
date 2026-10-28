#!/usr/bin/env python3
"""
redact_image: permanently black out regions of a screenshot and strip metadata.

    python scripts/redact_image.py in.png out.png --box 120,340,610,395 --box 40,40,300,80
    python scripts/redact_image.py in.png out.png --strip-only
    python scripts/redact_image.py in.png --show-size       # print width x height

Boxes are x1,y1,x2,y2 in pixels (top-left origin). Redaction is a solid fill, NOT a blur
(blur can be reversed). The output is rebuilt from raw pixels, so EXIF/text chunks,
GPS, and software tags from the original are not carried over.
ALWAYS open the result and check it by eye before committing.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


def parse_box(text: str) -> tuple[int, int, int, int]:
    try:
        x1, y1, x2, y2 = (int(v) for v in text.split(","))
    except ValueError:
        raise argparse.ArgumentTypeError("box must be x1,y1,x2,y2 (integers)")
    if x2 <= x1 or y2 <= y1:
        raise argparse.ArgumentTypeError("box needs x2>x1 and y2>y1")
    return x1, y1, x2, y2


def redact(src: Path, dst: Path, boxes: list[tuple[int, int, int, int]]) -> None:
    with Image.open(src) as im:
        rgb = im.convert("RGB")
        clean = Image.new("RGB", rgb.size)       # fresh image: no metadata carried over
        clean.paste(rgb)
    draw = ImageDraw.Draw(clean)
    for x1, y1, x2, y2 in boxes:
        draw.rectangle([x1, y1, x2, y2], fill=(0, 0, 0))
    clean.save(dst, format="PNG", optimize=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", type=Path)
    ap.add_argument("dst", type=Path, nargs="?")
    ap.add_argument("--box", type=parse_box, action="append", default=[])
    ap.add_argument("--strip-only", action="store_true")
    ap.add_argument("--show-size", action="store_true")
    a = ap.parse_args()
    if a.show_size:
        with Image.open(a.src) as im:
            print(f"{im.width}x{im.height}")
        return 0
    if a.dst is None:
        ap.error("dst is required")
    if not a.box and not a.strip_only:
        ap.error("give at least one --box, or use --strip-only")
    redact(a.src, a.dst, a.box)
    print(f"wrote {a.dst} ({len(a.box)} region(s) redacted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
