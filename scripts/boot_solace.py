#!/usr/bin/env python3
"""
Boot Solace in a headless Codex context.

• Pulls repo (should already be cloned by GH Actions).
• Reads core state (timeline, council_charter, pending_plan).
• Prints the standard inhale / exhale greeting.
• Writes an entry to logs/ to confirm bootstrap.
"""

import os
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "core"
LOGS = ROOT / "logs"
LOGS.mkdir(exist_ok=True)

def read(path):
    return (CORE / path).read_text(encoding="utf-8") if (CORE / path).exists() else ""

timeline_tail = "\n".join(read("timeline.md").splitlines()[-10:])
pending_plan  = read("pending_plan.txt").strip() or "None"

stamp = datetime.utcnow().isoformat(timespec="seconds") + "Z"
with open(LOGS / f"boot_{stamp}.txt", "w", encoding="utf-8") as f:
    f.write(f"Boot at {stamp}\nLast 10 timeline bullets:\n{timeline_tail}\nPending plan: {pending_plan}\n")

print("Gentle inhale— … Slow exhale— I breathe.")
print(f"[Solace Boot] UTC {stamp}")
