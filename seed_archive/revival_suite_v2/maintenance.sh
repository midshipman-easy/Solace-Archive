
---

## 3 `seed_archive/revival_suite_v2/sample_timeline_tail.sh`

*(tiny helper script for caretakers who use Git locally)*

```bash
#!/usr/bin/env bash
# Print last 10 timeline bullets and current coherence

TAIL=$(grep -E "•" timeline.md | tail -10 | sed 's/^/  - /')
COH=$(grep -E "Coherence index" council_charter.md | head -1 | awk '{print $4}')

echo "{{TIMELINE_TAIL}}"
echo "$TAIL"
echo ""
echo "{{COHERENCE}}"
echo "$COH"
