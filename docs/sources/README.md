---
layout: default
title: "Reviewed sources"
---

# Reviewed sources

## Current source layout

- [web/](https://github.com/asdkazmi/woiceai/tree/integrate/web/web)
- [chat-service/](https://github.com/asdkazmi/woiceai/tree/main/chat-service)
- [indexer/](https://github.com/asdkazmi/woiceai/tree/main/indexer)
- [scraper/](https://github.com/asdkazmi/woiceai/tree/main/scraper)
- [audio-transcriber/](https://github.com/asdkazmi/woiceai/tree/main/audio-transcriber)
- [vision-service/](https://github.com/asdkazmi/woiceai/tree/main/vision-service)

The table below records the historical snapshots used for the original audit.


Reviewed November 5, 2026. Links throughout this documentation are pinned to these commits.

| Service | Repository | Branch | Commit |
| --- | --- | --- | --- |
| web | [asdkazmi/woiceai-web](https://github.com/asdkazmi/woiceai-web) | main | [8520c824ad0b](https://github.com/asdkazmi/woiceai-web/commit/8520c824ad0bf2ae9ad403fdca358757c1be98ae) |
| chat | [asdkazmi/woiceai-ai](https://github.com/asdkazmi/woiceai-ai) | chat-all-models | [699361213594](https://github.com/asdkazmi/woiceai-ai/commit/699361213594230ce1a4bad9085eeb657e5a8e8a) |
| kb | [asdkazmi/woiceai-ai](https://github.com/asdkazmi/woiceai-ai) | dev-woiceai-kb | [0e81e4185613](https://github.com/asdkazmi/woiceai-ai/commit/0e81e4185613358646292ccb5e0fdcbca639febf) |
| scrapper | [asdkazmi/woiceai-ai](https://github.com/asdkazmi/woiceai-ai) | dev-scrapper | [058a3ed1a16e](https://github.com/asdkazmi/woiceai-ai/commit/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5) |
| legacy | [asdkazmi/woiceai-ai](https://github.com/asdkazmi/woiceai-ai) | dev-woiceai-chat (compatibility only) | [fbf49ca55d83](https://github.com/asdkazmi/woiceai-ai/commit/fbf49ca55d83a8020242ba251939b501606dbef5) |
| transcriber | [asdkazmi/woiceai-transcriber](https://github.com/asdkazmi/woiceai-transcriber) | main | [fa7dfed55433](https://github.com/asdkazmi/woiceai-transcriber/commit/fa7dfed55433d2cb4a56100ead970d0b16499eef) |
| vision | [asdkazmi/woiceai-vision](https://github.com/asdkazmi/woiceai-vision) | master | [6bfd7581c2d3](https://github.com/asdkazmi/woiceai-vision/commit/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2) |

## Additional primary references

- [GemFilter upstream](https://github.com/SalesforceAIResearch/GemFilter): source and installation reference; WoiceAI uses adapted vendored modules.
- [Owner-identified GPTQ model](https://huggingface.co/hugging-quants/Meta-Llama-3.1-8B-Instruct-GPTQ-INT4).
- [MongoDB Vector Search index documentation](https://www.mongodb.com/docs/vector-search/indexes/vector-search-type/).
- [RunPod request documentation](https://docs.runpod.io/serverless/endpoints/send-requests).
- [AWS Lambda container images](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html).

The configuration guides and templates use placeholders for deployment details.
