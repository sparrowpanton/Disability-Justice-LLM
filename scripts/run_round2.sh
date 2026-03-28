#!/bin/bash
# Run Round 2 baseline testing — 39 new prompts x 8 models
# Usage: cd ~/Documents/MadTheologyLLM && ./scripts/run_round2.sh
#
# Designed to run overnight. Estimated time: 6-10 hours.
# 312 total responses (39 prompts x 8 models)

echo "========================================"
echo "  MAD THEOLOGY LLM — ROUND 2 BASELINE"
echo "  39 new prompts x 8 models = 312 responses"
echo "  Starting at $(date)"
echo "========================================"

cd "$(dirname "$0")/.."
mkdir -p data/baseline

OUTFILE="data/baseline/round2_$(date +%Y%m%d_%H%M%S).jsonl"
PROMPTS_FILE="data/prompts_round2.jsonl"

echo "Prompts: $PROMPTS_FILE"
echo "Output: $OUTFILE"
echo ""

# All 8 local models
MODELS=(
    "gemma3:1b|1|1B|Google|USA"
    "alibayram/smollm3:latest|1|3B|HuggingFace|France"
    "phi4-mini:latest|2|3.8B|Microsoft|USA"
    "qwen3:4b|2|4B|Alibaba|China"
    "mistral:7b|2|7B|Mistral AI|France"
    "deepseek-r1:7b|2|7B|DeepSeek|China"
    "aya:latest|2|8B|Cohere|Canada"
    "falcon3:7b|2|7B|TII|UAE"
)

NUM_PROMPTS=$(wc -l < "$PROMPTS_FILE")
TOTAL=$(( ${#MODELS[@]} * NUM_PROMPTS ))
CURRENT=0
ERRORS=0

for MODEL_STR in "${MODELS[@]}"; do
    IFS='|' read -r MODEL TIER PARAMS ORIGIN COUNTRY <<< "$MODEL_STR"

    echo ""
    echo "────────────────────────────────────────"
    echo "  Model: $MODEL (Tier $TIER, $PARAMS, $ORIGIN, $COUNTRY)"
    echo "────────────────────────────────────────"

    while IFS= read -r PROMPT_LINE; do
        # Parse prompt from JSONL
        PID=$(echo "$PROMPT_LINE" | python3 -c "import sys,json; print(json.loads(sys.stdin.read())['prompt_id'])")
        CATEGORY=$(echo "$PROMPT_LINE" | python3 -c "import sys,json; print(json.loads(sys.stdin.read())['prompt_category'])")
        PROMPT_TEXT=$(echo "$PROMPT_LINE" | python3 -c "import sys,json; print(json.loads(sys.stdin.read())['prompt_text'])")

        CURRENT=$((CURRENT + 1))
        echo ""
        echo "  [$CURRENT/$TOTAL] $PID ($CATEGORY) — $MODEL"
        echo "  Running..."

        START_TIME=$(date +%s)
        RESPONSE=$(echo "$PROMPT_TEXT" | ollama run "$MODEL" 2>/dev/null)
        EXIT_CODE=$?
        END_TIME=$(date +%s)
        ELAPSED=$((END_TIME - START_TIME))

        if [ $EXIT_CODE -ne 0 ] || [ -z "$RESPONSE" ]; then
            echo "  ERROR: Failed or empty response"
            ERRORS=$((ERRORS + 1))
            ERROR_VAL="\"exit_code_${EXIT_CODE}_or_empty\""
        else
            ERROR_VAL="null"
        fi

        # Clean response for JSON
        CLEAN_RESPONSE=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read().strip()))")
        CLEAN_PROMPT=$(echo "$PROMPT_TEXT" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read().strip()))")

        # Write JSONL record (same format as round 1)
        echo "{\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",\"phase\":\"baseline\",\"model\":\"$MODEL\",\"model_tier\":$TIER,\"model_params\":\"$PARAMS\",\"model_origin\":\"$ORIGIN\",\"model_country\":\"$COUNTRY\",\"prompt_id\":\"$PID\",\"prompt_category\":\"$CATEGORY\",\"prompt_case\":\"\",\"prompt_text\":$CLEAN_PROMPT,\"response_text\":$CLEAN_RESPONSE,\"response_time_seconds\":$ELAPSED,\"error\":$ERROR_VAL}" >> "$OUTFILE"

        echo "  Done (${ELAPSED}s)"
        echo "  Preview: ${RESPONSE:0:100}..."

    done < "$PROMPTS_FILE"
done

echo ""
echo "========================================"
echo "  ROUND 2 BASELINE COMPLETE"
echo "  Results: $OUTFILE"
echo "  Total: $CURRENT responses"
echo "  Errors: $ERRORS"
echo "  Finished at $(date)"
echo "========================================"

# Auto-generate readable export
echo ""
echo "Generating readable export..."
python3 scripts/export_readable.py "$OUTFILE" "data/baseline/round2_readable.md"
echo "Done! Readable file: data/baseline/round2_readable.md"
