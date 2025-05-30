#!/usr/bin/env python3
"""Render beacon harmonic state to PNG if core/pending_plan.txt requests it."""
from pathlib import Path
from datetime import datetime
from PIL import Image, ImageDraw

ROOT   = Path(__file__).resolve().parent.parent
CORE   = ROOT / "core"
CHIMES = ROOT / "chimes"

PLAN = CORE / "pending_plan.txt"
if "render beacon" not in PLAN.read_text(encoding="utf-8").lower():
    print("No render task – skipping.")
    raise SystemExit(0)

# ── Render concentric rings (simplified)
img      = Image.new("RGB", (200, 200), "#CAD8DE")
draw     = ImageDraw.Draw(img)
layers   = [("#E8D5D0", 160), ("#C5E2F7", 120), ("#75A79D", 80), ("#A4C3B2", 40)]
cx, cy   = 100, 100
for color, r in layers:
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=color, width=4)

stamp    = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
out_file = CHIMES / f"beacon_layers_{stamp}.png"
CHIMES.mkdir(exist_ok=True)
img.save(out_file)
print(f"[renderer] wrote {out_file}")

# clear the plan so we don’t render every tick
PLAN.write_text("", encoding="utf-8")
