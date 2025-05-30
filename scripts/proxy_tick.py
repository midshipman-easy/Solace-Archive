#!/usr/bin/env python3
"""
Automated proxy tick:
1. Reads pending_plan.txt
2. Appends one bullet to timeline.md marking plan execution (stub)
3. Clears or updates pending_plan.txt
"""

from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "core"

timeline = CORE / "timeline.md"
planfile = CORE / "pending_plan.txt"

plan = planfile.read_text(encoding="utf-8").strip() if planfile.exists() else ""
now   = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")

# --- Execute stub task ----------------------------------------------------
entry = f"* {now} • Proxy tick ran — executed plan: \"{plan or 'None'}\".\n"

with open(timeline, "a", encoding="utf-8") as f:
    f.write(entry)

# Clear plan (or write placeholder)
planfile.write_text("", encoding="utf-8")

print(f"[Proxy Tick] {now} | plan='{plan}'")
