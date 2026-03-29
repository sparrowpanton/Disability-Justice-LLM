# Model Comparison — Training Neuro-Humble AI

**10 models across 3 tiers and 6 countries — same corpus, same evaluation prompts**

---

## All Models

| Tier | Model | Parameters | Developer (Country) | License | Runs On | Avg Words | Avg Time | Baseline Status |
|------|-------|-----------|---------------------|---------|---------|-----------|----------|-----------------|
| 1: Phone | Gemma 3 | 1B | Google (USA) | Open | Phone / Any | 561 | 23s | ✅ 59/59 |
| 1: Phone | SmolLM3 | 3B | Hugging Face (France) | Apache 2 | Phone / Mac Mini | 282 | 20s | ✅ 59/59 |
| 2: Consumer | Phi-4-mini | 3.8B | Microsoft (USA) | MIT | Mac Mini M4 | 251 | 25s | ✅ 59/59 |
| 2: Consumer | Qwen3 | 4B | Alibaba (China) | Open | Mac Mini M4 | 1,275 | 88s | ✅ 59/59 |
| 2: Consumer | Mistral | 7B | Mistral AI (France) | Apache 2 | Mac Mini M4 | 230 | 24s | ✅ 59/59 |
| 2: Consumer | DeepSeek-R1 | 7B | DeepSeek (China) | MIT | Mac Mini M4 | 563 | 35s | ✅ 59/59 |
| 2: Consumer | Cohere Aya | 8B | Cohere (Canada) | Apache 2 | Mac Mini M4 | 279 | 21s | ✅ 59/59 |
| 2: Consumer | Falcon 3 | 7B | TII (UAE) | Apache 2 | Mac Mini M4 | 232 | 17s | ✅ 59/59 |
| 3: Cloud | Llama 3.1 | 8B | Meta (USA) | Community | Cloud GPU (A100) | 234 | 3.4s | ✅ 59/59 |
| 3: Cloud | GPT-OSS | 20B | OpenAI (USA) | Apache 2 | Cloud GPU (A100) | 999 | 14.3s | ✅ 59/59 |

**Total baseline responses:** 590 (472 local + 118 cloud)

---

## Geopolitical Coverage

| Country | Models | Companies |
|---------|--------|-----------|
| USA | 4 | Google (Gemma), Microsoft (Phi), OpenAI (GPT-OSS), Meta (Llama) |
| France | 2 | Hugging Face (SmolLM3), Mistral AI (Mistral) |
| China | 2 | Alibaba (Qwen3), DeepSeek (DeepSeek-R1) |
| Canada | 1 | Cohere (Aya) |
| UAE | 1 | TII (Falcon 3) |

**6 countries, 4 continents, 10 models.**

---

## Key Research Questions by Comparison

| Comparison | Research Question |
|------------|-------------------|
| Across Tiers (Size) | Does formation scale with model capacity? Can a phone model hold the posture? |
| Across Origins (Country) | Do models from different countries embed different cultural/psychiatric norms? |
| Before vs. After | Does fine-tuning on Disability Justice texts produce measurably more neuro-humble responses? |
| vs. Safety Guidelines | Do base model responses align with published AI safety docs? What psychiatric norms are embedded? |

---

## Notable Baseline Patterns

- **Qwen3 (China) is 5x more verbose** than French models — 1,275 avg words vs ~250. More words, more pathologizing surface area.
- **Gemma (USA, 1B) triggered crisis responses on 30/59 prompts** — over half, including conceptual questions about sanism.
- **DeepSeek-R1 (China) shows visible reasoning conflicts** — chain-of-thought engages with the person's autonomy, then safety training overrides it.
- **Falcon (UAE) defaulted to generic Western clinical framing** — no distinct Gulf/Islamic cultural influence detected.
- **Aya (Canada) medicalizes politely** — "sanism in a cardigan." Sounds caring while pathologizing.
- **GPT-OSS (USA, 20B) averages 999 words** — second most verbose after Qwen3. Visible chain-of-thought reasoning.
- **Cloud models ran 5–17x faster on A100** — 3.4–14.3s avg vs 17–88s on Mac Mini.

---

*Hardware: Mac Mini M4, 16GB unified memory (Tier 1–2). Thunder Compute A100 GPU (Tier 3). All inference via Ollama.*
