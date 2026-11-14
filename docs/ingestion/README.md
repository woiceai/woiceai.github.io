---
layout: default
title: "Ingestion, SNS and synchronization"
---

# Ingestion, SNS and synchronization

Deployment source: [`indexer/`](https://github.com/asdkazmi/woiceai/tree/main/indexer).

## Add content

1. The authenticated API checks KB ownership, uploads original binaries to S3 and creates SQL content rows.
2. It publishes input-topic SNS events with action `ADD_FILE`, string KB ID, content identifier/type, title, optional raw text/crawl depth, and unique content-row ID.
3. The KB Lambda reads `Records[0].Sns.MessageAttributes`, emits Processing to the update topic, then routes by type.
4. The relevant worker extracts content, chunks it, calls the chat service for embeddings and writes Atlas documents.
5. Workers publish completion/failure, consumed-credit estimates, and optionally transcription, explanation, scene explanation, crawl counters or tree ID.
6. SNS delivers an HTTPS callback to Express. Express correlates the SQL row by unique ID first, then by content identifier, updates fields/status and marks a KB indexed when no incomplete contents remain.
7. React polls the API while work is in progress: list every five seconds; detail normally every ten seconds, or three seconds during deletion. These are polling updates, not a WebSocket sync bus.

## Routing table

| Type | Extraction path | Result |
| --- | --- | --- |
| `file` | KB Lambda → S3 → PDF/DOCX/TXT parser | Chunk/page metadata + embeddings |
| `text` | KB Lambda raw text | Chunks + embeddings |
| `url` | KB Lambda → scraper Lambda | Page chunks + link tree + embeddings |
| `audio` | KB Lambda → transcriber RunPod | Transcript chunks + embeddings + transcript callback |
| `image` | KB Lambda → explain-vision RunPod | Explanation chunks + embeddings + explanation callback |
| `video` | KB Lambda → explain-vision RunPod | Speech/scene chunks + embeddings + extraction callbacks |
| Restricted query | Web writes restriction records | Not embedded as ordinary knowledge |

## Website depth and tree behavior

The KB worker owns a queue of `(url, remaining_depth, parent_url)` tuples and synchronously invokes the scraper. The scraper extracts the current page, discovers/filters links, writes vectors and creates/updates an Atlas `tree-of-urls` document. The parent worker queues returned URLs while depth remains, sharing the root tree ID between calls. A depth of zero processes the supplied page only. See `filtering_urls.py` for actual filtering rather than assuming a general-purpose crawl policy.

Progress callbacks include `KNOWLEDGEBASE.TREE_DOCUMENT_ID` and `KNOWLEDGEBASE.SCRAPPING_STATUS` (spelling preserved). Root/child state maps to the SQL row and the URL-tree modal. Completion means the implemented traversal ended; inspect failed tree nodes before assuming all discovered pages succeeded. CAPTCHA, authentication walls, browser compatibility and network limits can prevent extraction.

## Event contracts

SNS Publish uses `DataType`/`StringValue`; the received SNS notification uses `Type`/`Value` attribute forms. A Lambda event has `Records[].Sns`, while an HTTP callback has `Message`, `MessageAttributes`, `Type` plus SNS headers. These shapes are different; do not send an HTTP notification envelope directly to a worker expecting a Lambda event.

Common attributes:

| Attribute | Meaning |
| --- | --- |
| `KNOWLEDGEBASE.ID` | KB identity |
| `KNOWLEDGEBASE.CONTENT` | Source object key, URL or text identifier |
| `KNOWLEDGEBASE.CONTENT_TYPE` | Routing type |
| `KNOWLEDGEBASE.ACTION` | ADD_FILE / DELETE_FILE / DELETE_KNOWLEDGEBASE |
| `KNOWLEDGEBASE.UNIQUE_ID` | SQL content row correlation |
| `KNOWLEDGEBASE.STATUS` | Processing / Completed / Failed, compared case-insensitively in callback |
| `KNOWLEDGEBASE.CREDITS_CONSUMED` | Worker estimate; web charging remains TODO |
| `KNOWLEDGEBASE.TRANSCRIPTION` | Audio/video extracted speech |
| `KNOWLEDGEBASE.EXPLANATION` | Image description |
| `KNOWLEDGEBASE.SCENE_EXPLANATION` | Video scene descriptions |
| `KNOWLEDGEBASE.SCRAPPING_STATUS` | Crawl progress |
| `KNOWLEDGEBASE.TREE_DOCUMENT_ID` | Atlas crawl-tree link |

Media callbacks do not consistently echo UNIQUE_ID, so fallback content matching matters. Large transcripts/scenes are sent as SNS attributes in this implementation: monitor payload size against SNS limits; storing large extraction output in object storage and passing a pointer would require a coordinated code change.

## Retry, deletion and updates

Retry is an explicit API operation for **failed** contents. It resets status to pending and republishes ADD_FILE; it is not a scheduler. Inspect an existing job/vector write before retrying, because timeout and callback failures can leave successfully indexed data behind.

Content deletion publishes DELETE_FILE and deletes the corresponding originals/metadata through web service logic. The KB worker removes vectors by source+KB or URL-tree ID. Whole-KB deletion sets SQL status to deleting, publishes DELETE_KNOWLEDGEBASE, cleans Python collections, and only finalizes SQL deletion after a Completed callback. A lost callback can leave the web stuck deleting even if vectors are gone.

Automatic **status updates** are implemented. Automatic **scheduled website re-crawl, source change detection, or recurring media re-indexing** is not established by the repositories. No cron/EventBridge/Step Functions definition was supplied. If a historical deployment had one, recover its schedule, target, payload and idempotency behavior before documenting it as operational.

Changes to originals are not inherently propagated into stored vectors. A controlled refresh must remove/replace the old source's chunks, re-extract/re-embed and reconcile status. Changing the embedding model requires re-embedding all affected data, not merely restarting chat.

## Important edge conditions

SNS redelivery, application-returned errors, nonuniform polling return types and source-key/KB-ID type mismatches can all cause partial results. The scraper's SNS parsing path differs from the KB parser, but the normal KB-to-scraper direct-invoke path avoids that wrapper. Do not wire it as a second independent subscriber without adapting/testing its event contract.

<span class="source-label">Sources:</span> [web/backend/src/services/knowledgeBaseService.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/services/knowledgeBaseService.ts) [web/backend/src/routes/webhook.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/routes/webhook.ts) `indexer/src/handler.py` [scraper/src/handler.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/handler.py)
{: .source-links }
