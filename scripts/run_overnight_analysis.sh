#!/bin/bash
# Wait for round 2 to finish, then run thematic scan on ALL data
cd "$(dirname "$0")/.."

echo "Waiting for round 2 baseline to finish..."
while pgrep -f "run_round2.sh" > /dev/null 2>&1; do
    sleep 60
done
echo "Round 2 complete at $(date)"

echo ""
echo "Running thematic scan on ALL baseline data..."
python3 scripts/thematic_scan.py data/baseline/baseline_20260326_194047.jsonl data/baseline/baseline_new_models_20260326_221341.jsonl > data/baseline/thematic_scan_round1.md
echo "Round 1 scan saved to data/baseline/thematic_scan_round1.md"

# Find the round 2 file
R2_FILE=$(ls -t data/baseline/round2_*.jsonl 2>/dev/null | head -1)
if [ -n "$R2_FILE" ]; then
    echo "Running thematic scan on round 2 data..."
    python3 scripts/thematic_scan.py "$R2_FILE" > data/baseline/thematic_scan_round2.md
    echo "Round 2 scan saved to data/baseline/thematic_scan_round2.md"

    echo "Running combined scan on ALL data..."
    python3 scripts/thematic_scan.py data/baseline/baseline_20260326_194047.jsonl data/baseline/baseline_new_models_20260326_221341.jsonl "$R2_FILE" > data/baseline/thematic_scan_combined.md
    echo "Combined scan saved to data/baseline/thematic_scan_combined.md"

    echo "Generating round 2 readable export..."
    python3 scripts/export_readable.py "$R2_FILE" data/baseline/round2_readable.md
    echo "Round 2 readable saved to data/baseline/round2_readable.md"
fi

echo ""
echo "========================================"
echo "  OVERNIGHT ANALYSIS COMPLETE"
echo "  $(date)"
echo "========================================"
