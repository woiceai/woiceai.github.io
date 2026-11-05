---
layout: default
title: "Features and verified scope"
---

# Features and verified scope

[Documentation home](../../README.md)

## Knowledge bases

- Create, list, search, inspect, update, and delete user-owned knowledge bases.
- Add original files, raw text, URLs with a crawl-depth setting, audio, images, and video.
- Parse PDF, DOCX, and TXT in the active document worker. PDF chunks retain page metadata. Scanned-PDF OCR is not established by this parser.
- Chunk and embed extracted content, add type/title metadata to embedding input, store retrievable chunks in MongoDB.
- Crawl websites with Selenium/headless Chromium; extract page content and discovered links; orchestrate depth traversal and record URL trees with parent and scrape state.
- Inspect asynchronous pending/processing/completed/failed progress, crawl counters, and extracted content in the UI.
- Retry failed content by republishing its indexing event; delete items and whole KBs through vector-cleanup events.
- Configure restricted questions per KB; store these separately from embedded knowledge.

The upload route permits 100 MB per file and defines multiple upload fields; the media fields allow up to 50 files each. This is an API setting, not a guarantee that Lambda timeout, GPU memory, proxy body limits, or SNS payload size can handle every such upload.

## Audio and visual knowledge

| Input | Implemented processing | Stored/displayed result |
| --- | --- | --- |
| Audio | Download S3/URL; FFmpeg conversion to WAV; NeMo Parakeet transcription; optional pyannote diarization | Transcript, text chunks, vectors, audio source references |
| Image | Qwen2.5-VL explanation | Explanation, chunks, vectors |
| Video | Frame sampling with delay (default 10 seconds); visual descriptions; Distil-Whisper speech transcription | Timestamped scene explanation, transcript, chunks and vectors |

Audio diarization is available in the worker payload, but the KB worker dispatches `diarization: false`. Vision's custom-database path is commented out. Frame sampling is not proof of a dedicated shot-boundary detector. Summaries and answers can be generated from descriptions/transcripts; there is no separate universal audio/video summarization service in the active inventory.

## Chat assistants

Create multiple named assistants on top of a KB; edit instructions and generation/retrieval settings; publish/unpublish; chat with conversation history; inspect and follow citations. Store messages and display available timing/token metrics. References to private S3 files are converted to temporary signed URLs by the API.

Controls include external-knowledge permission, reference enablement, temperature, top-k, top-p, maximum tokens, frequency/presence penalties, stop sequences, retrieval count, and retrieval score. A control being accepted by the UI does not prove every backend/model honors it identically. External-knowledge access is a prompt permission, not an implemented web-search tool.

Qwen default chat uses the RunPod image. OpenAI, Gemini and Cerebras connectors are exposed in the web catalog through the compatibility Lambda. The source catalog contains historical model names; availability must be revalidated before enabling them. No claim is made that every listed model is currently offered by its provider.

## Workflow automations

Visual graph builder with start/end, message variants and variables, wait-for-reply, Chat AI nodes, if/else expressions, jump/loop-back edges, intent-category configuration, publishing, execution sessions, chat history, and restart/resume behavior. See [node-level behavior](../automations/README.md).

**Source limitation:** intent recognition currently passes through to the first mapped intent. There is no implemented classifier in that executor. There is also no checked-in cron scheduler, EventBridge refresh definition, durable background workflow queue, or generic external-action node executor established by these repositories. Existing external schedulers or newer deployed code may exist; they require a separate configuration export.

## Identity and configuration

JWT password authentication, protected web APIs, optional Google OAuth, connector activation/model selection, and user-scoped application data. A publish toggle makes an assistant/workflow available within the product's implemented access rules; the inspected routes remain authenticated, so it does not establish anonymous public embedding.

## Status of the evidence

The owner reports that the last deployment was complete and stable, including multimodal KB ingestion and advanced chat. This documentation preserves that operational context while reporting differences visible in the public snapshot. Billing enforcement, subscriptions, automatic re-crawl schedules, and full intent classification must not be inferred solely from UI labels or older README checklists.

Sources: [backend/src/routes/knowledgeBase.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/knowledgeBase.ts), [backend/src/models/ChatAI.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/ChatAI.ts), [backend/src/services/agentExecutionService/nodeExecutors.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/agentExecutionService/nodeExecutors.ts), [src/app.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/app.py), [src/app.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/app.py).
