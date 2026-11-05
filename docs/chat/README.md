---
layout: default
title: "Chat, RAG and model maintenance"
---

# Chat, RAG and model maintenance

[Documentation home](../../README.md)

## Query pipeline

1. Express loads the user-owned Chat AI, connector and saved settings. It transforms history from role/content to `is_human`/`prompt`.
2. Default `qwen` dispatch calls RunPod `/runsync` with the KB ID, query/history, instructions, citation/external-knowledge flags and generation/retrieval settings.
3. The public RunPod handler uses Stella to embed/retrieve. When history or restricted questions exist, it rewrites the query using the GGUF model, with possible restriction validation messages.
4. Atlas `$vectorSearch` retrieves `document-kb` chunks filtered by string KB ID and projects source metadata.
5. The custom GPTQ Llama GemFilter code selects/compresses relevant context. The GGUF llama.cpp model generates the final response from instructions, filtered knowledge and history.
6. If references are enabled, the handler extracts numbered Markdown citations, removes uncited results and renumbers references.
7. Express adds signed document URLs for S3 references and returns the response plus available token/timing information to the browser.

The handler has a separate `responseOnly` branch that uses the GGUF model without normal RAG, and separate `embeddings`/`retrieval` tasks. Chat and ingestion therefore share model capacity and scaling limits.

## Runtime model inventory

| Role | Source/artifact | Where configured |
| --- | --- | --- |
| Document/query embeddings | `dunzhang/stella_en_400M_v5`, local `stella_en_400M_v5` | Chat Dockerfile; `modules/stella.py` |
| Context selection | Local `Meta-Llama-3.1-8B-Instruct-gptq` directory | Chat handler + custom `llama_gemfilter/load_model.py` |
| GPTQ download identified by owner | [hugging-quants/Meta-Llama-3.1-8B-Instruct-GPTQ-INT4](https://huggingface.co/hugging-quants/Meta-Llama-3.1-8B-Instruct-GPTQ-INT4) | Download to directory expected by Dockerfile; validate custom loader compatibility |
| GGUF generation/query rewrite | `merged-q4_k_m-model.gguf` | Chat handler; llama-cpp-python |
| Audio ASR | `nvidia/parakeet-rnnt-0.6b` | Transcriber `src/models.py`, Dockerfile |
| Speaker diarization | pyannote speaker-diarization-3.1; segmentation-3.0; wespeaker-voxceleb-resnet34-LM | Transcriber model config/downloads |
| Image/video description | `Qwen/Qwen2.5-VL-7B-Instruct` | Vision `src/modules/models.py` |
| Video ASR | `distil-whisper/distil-large-v3` | Vision `src/modules/transcribing_video.py` |

The UI label `Qwen-14b-Instruct` is a connector catalog label; it does not prove the actual GGUF architecture or weight provenance. The owner says the merged artifact was compiled locally and was their GemFiltered Llama variant. The public source separately loads a GGUF generator and GPTQ context selector. Preserve both facts: no exact conversion recipe, original GGUF base model, checksum or exact deployed-image-to-source build manifest was supplied.

## Get and use GemFilter

The upstream implementation is [SalesforceAIResearch/GemFilter](https://github.com/SalesforceAIResearch/GemFilter). To obtain it for study:

```bash
git clone https://github.com/SalesforceAIResearch/GemFilter.git
```

WoiceAI already vendors its adapted implementation under `chat-with-all-models/src/modules/llama_gemfilter/`. Preserve this adaptation and the project's pinned inference dependencies when reproducing the worker. Upstream installation is a separate research environment, not a drop-in replacement for these adapted files.

In WoiceAI, `handler.py` selects `modified='llama_gemfilter'`, `topk=1024`, `select_layer_idx=13`, enables selection and reduces layers. `applygemfilter.py` invokes `my_greedy_generate_selection` and extracts the selected `<book>` content. This is runtime context filtering; it does not itself provide a GGUF conversion/export command. Recreating the owner's merged artifact still requires the original model/conversion details or a deliberately validated replacement.

The project pins torch 2.4.1, transformers 4.43.3, flash-attn 2.6.3, auto-gptq 0.7.1 and llama-cpp-python 0.2.90 in its build/requirements. Test version changes together; custom attention/generation patches are sensitive to Transformers internals.

## Settings and defaults in the public RunPod handler

| Setting | Default |
| --- | --- |
| `temperature` | 0.2 |
| `top_k` / `top_p` | 40 / 0.95 |
| `max_tokens` | 2048 |
| frequency / presence penalty | 0.0 / 0.0 |
| retrieval limit / score | 10 / 0.5 |
| external knowledge | true |
| references | false |
| GGUF context / threads / GPU layers | 8000 / 8 / -1 |

`external_knowledge_access` affects the generated prompt; it does not browse the internet. The score loop appends a result before checking whether it falls below threshold, so the source does not enforce a strict exclude-every-below-threshold rule. Check actual retrieval quality with known examples.

## Replace or update a model

- **Prompts/behavior:** edit `generate_prompt.py`, `rewrite_query.py` and `response.py`; retain reference formatting and restriction tests.
- **GGUF:** update artifact path/COPY and generation configuration; record base model, tokenizer/chat template, quantization method and checksum. Verify output schema and history/restriction behavior.
- **GemFilter:** update compatible GPTQ weights/loader and attention hooks, layer selection and tokenizer together. Validate that selected text preserves usable citation metadata and that long prompts fit VRAM.
- **Embeddings:** update Stella downloads/loading and measure vector dimension. Re-embed the entire affected KB corpus and rebuild/swap its Atlas index. Never mix incompatible embeddings in the same field/index.
- **ASR/vision:** update model IDs/downloads/loaders in the relevant repository, rebuild image, test long/short/no-speech inputs, transcript quality and SNS callbacks.
- **Provider catalog:** update `connectorService.ts` and the compatibility provider mapping/pricing. Existing connector rows are skipped by startup seeding, so changing defaults alone does not migrate existing database catalogs.

## Provider paths and restrictions

OpenAI/Gemini/Cerebras in the web snapshot invoke the compatibility Lambda; the active RunPod handler does not read a provider API key or choose from `llm_name`. Keep this distinction visible when migrating all providers into RunPod.

Restrictions live in Atlas `restricted-queries` with numeric KB IDs. They are model-mediated query validation, not a hard authorization boundary for data isolation. KB ownership/filtering must remain enforced independently. Citations indicate source linkage produced by the model; they are not a guarantee that each statement is entailed by a source.

Sources: [chat-with-all-models/src/handler.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/handler.py), [chat-with-all-models/src/modules/response.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/response.py), [chat-with-all-models/src/modules/applygemfilter.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/applygemfilter.py), [backend/src/services/chatAIService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/chatAIService.ts).
