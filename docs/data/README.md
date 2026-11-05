---
layout: default
title: "Databases and vector indexing"
---

# Databases and vector indexing

[Documentation home](../../README.md)

## MongoDB Atlas is required for this project

Use **MongoDB Atlas** with Vector Search. The owner explicitly confirmed Atlas as the intended deployment. A plain local Community MongoDB process is not an adequate replacement for the project's `$vectorSearch` dependency. This guide does not attempt alternate MongoDB deployment products.

Create an Atlas cluster with Vector Search support, a least-privilege database user, and network access for the API, Lambda and RunPod workers. Use TLS and the Atlas connection URI. Configure `MONGODB_URI` in Express and `DB_URI` in every Python worker to the same cluster. Python hardcodes `woice-ai-kb`; keep the web `MONGODB_DATABASE` aligned.

## Storage responsibilities

| Store | Records | Authority |
| --- | --- | --- |
| MySQL | Users, KB ownership/config, content rows/status, connector settings, Chat AIs/messages, agents/executions/messages | Application metadata and session state |
| Atlas `document-kb` | Chunks, vectors, source metadata | Retrieval content |
| Atlas `tree-of-urls` | Root URL, KB ID, parent/child scrape records | Crawl structure/progress |
| Atlas `restricted-queries` | Numeric KB ID/user ID, restricted question arrays | Chat query restrictions |
| Atlas `keys` | Legacy provider API-key IDs and optional custom MongoDB credentials | Optional compatibility lookup |
| Other Python-referenced collections | `schema-based-kb`, `conversation-history` | Compatibility/cleanup references; presence is not proof of an active web writer |
| S3 | Original files/media under generated object keys | Original binary content |

## MySQL tables

The API creates tables in `backend/src/migrations` on startup. Core tables: `users`, `knowledge_bases`, `knowledge_base_contents`, `connectors`, `connector_models`, `connector_user`, `user_connector_models`, `chat_ais`, `chat_ai_messages`, `agents`, `agent_executions`, `agent_chat_messages`. The generated [schema inventory](schema.md) links each migration.

Knowledge-base content rows correlate indexing jobs through their numeric row ID sent as `KNOWLEDGEBASE.UNIQUE_ID`. Content rows include extraction output, scrape status and URL-tree document linkage. Assistant settings and workflow graphs/execution state use structured JSON. Execution states persist current node, prior inputs and context, supporting wait/resume.

## Vector documents

Representative schema; individual writers vary:

```json
{
  "kbId": "123",
  "type": "file",
  "title": "Handbook.pdf",
  "s3_Key": "knowledge-bases/uuid.pdf",
  "metadata": {"pageNo": 1, "chunkNo": 1},
  "content": "Extracted chunk text",
  "bgeVectors": [0.01, 0.02]
}
```

The illustrated array is shortened, not a valid production embedding. Despite the name **bgeVectors**, the active chat embedding endpoint uses Stella. Do not change an index to a BGE dimension merely because of the field name. Some helper paths expose `stellaVectors`; that is not the main stored-field contract.

## Create the Vector Search index

1. Generate one embedding using the deployed chat worker and measure `len(output.output[0])`. The Docker recipe downloads Stella's 1024-dimensional dense head, so **1024 is the expected setup**, but verify the deployed artifact before indexing.
2. In Atlas, create a **Vector Search** index on `woice-ai-kb.document-kb`, named **`bgeVectors`**.
3. Use the following proposed definition when the measured dimension is 1024. It is not an export of the live index:

```json
{
  "fields": [
    {"type": "vector", "path": "bgeVectors", "numDimensions": 1024, "similarity": "cosine"},
    {"type": "filter", "path": "kbId"}
  ]
}
```

4. Wait until the index is queryable. Test a known document and a KB-filtered query. The handler uses `$vectorSearch` with `exact: true`, index/path `bgeVectors`, and a string KB filter.
5. Ensure `kbId` types match actual stored documents. Normal ingestion receives string IDs through SNS; restrictions use numeric IDs, and chat converts its restriction lookup to int. Mixed integer/string vector IDs can silently produce no matches.

See [MongoDB's index documentation](https://www.mongodb.com/docs/vector-search/indexes/vector-search-type/) for current field-definition requirements. Ordinary B-tree indexes do not substitute for a Vector Search index. Add ordinary indexes on frequently queried metadata (`kbId`, source keys, URL/tree IDs, key IDs) after assessing query patterns; they are recommendations rather than exported live definitions.

## Consistency and recovery

There is no distributed transaction across SQL, S3, SNS and Atlas. An uploaded S3 object/SQL row can exist before embeddings do. SNS callbacks update SQL after workers write vectors. UI completion is an application status, not a distributed commit certificate.

Retry or redelivery can insert duplicate chunks: the main writers use `insert_many`, not a universally idempotent upsert. A unique content ID correlates callbacks but does not guarantee deduplication in all vector writers. Before replaying ingestion, inspect existing source chunks and choose a controlled cleanup/reindex strategy.

The web stores provider connector keys in MySQL, while the compatibility Lambda reads Atlas `keys` by `id`. No matching synchronization writer was found in current web connector code. Do not manually populate production keys as a substitute for a designed secret bridge without reviewing access, types and rotation.

For backups, retain SQL, Atlas and S3 together; save index definitions and source-image/model versions. Rebuilding vectors requires the same embedding model or a full re-embedding migration.

Sources: [woice_kb/src/modules/mongo.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/src/modules/mongo.py), [chat-with-all-models/src/modules/vector.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/vector.py), [backend/src/services/restrictedQueryService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/restrictedQueryService.ts), [backend/src/models/AgentExecution.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/AgentExecution.ts).
