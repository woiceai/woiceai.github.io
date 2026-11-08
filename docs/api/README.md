---
layout: default
title: "API and worker contracts"
---

# API and worker contracts

## Express routes

Generated from literal router registrations in the reviewed source. Auth is enforced on application routes; auth login/register/OAuth and SNS callback routes have their own behavior. Review linked handlers for request validation, authorization and response details. This is a route inventory, not a generated OpenAPI specification.

| Method | Path | Handler source |
| --- | --- | --- |
| POST | `/api/auth/register` | [auth](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/auth.ts) |
| POST | `/api/auth/login` | [auth](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/auth.ts) |
| GET | `/api/auth/me` | [auth](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/auth.ts) |
| POST | `/api/auth/logout` | [auth](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/auth.ts) |
| GET | `/api/auth/google` | [auth](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/auth.ts) |
| GET | `/api/auth/google/callback` | [auth](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/auth.ts) |
| GET | `/api/knowledge-base/` | [knowledgeBase](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/knowledgeBase.ts) |
| GET | `/api/knowledge-base/content/:contentId` | [knowledgeBase](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/knowledgeBase.ts) |
| POST | `/api/knowledge-base/content/:contentId/retry` | [knowledgeBase](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/knowledgeBase.ts) |
| GET | `/api/knowledge-base/:id` | [knowledgeBase](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/knowledgeBase.ts) |
| POST | `/api/knowledge-base/` | [knowledgeBase](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/knowledgeBase.ts) |
| PATCH | `/api/knowledge-base/:id` | [knowledgeBase](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/knowledgeBase.ts) |
| DELETE | `/api/knowledge-base/:id` | [knowledgeBase](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/knowledgeBase.ts) |
| GET | `/api/connectors/` | [connector](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/connector.ts) |
| GET | `/api/connectors/my-connections` | [connector](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/connector.ts) |
| GET | `/api/connectors/active-model` | [connector](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/connector.ts) |
| POST | `/api/connectors/connect` | [connector](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/connector.ts) |
| POST | `/api/connectors/switch-model` | [connector](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/connector.ts) |
| PUT | `/api/connectors/:connectorId/update` | [connector](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/connector.ts) |
| DELETE | `/api/connectors/:connectorId/disconnect` | [connector](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/connector.ts) |
| GET | `/api/chat-ai/published` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| GET | `/api/chat-ai/knowledge-base/:knowledgeBaseId` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| GET | `/api/chat-ai/:id` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| POST | `/api/chat-ai/` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| PATCH | `/api/chat-ai/:id` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| DELETE | `/api/chat-ai/:id` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| PATCH | `/api/chat-ai/:id/toggle-publish` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| POST | `/api/chat-ai/:id/chat` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| GET | `/api/chat-ai/:id/messages` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| POST | `/api/chat-ai/:id/messages` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| DELETE | `/api/chat-ai/:id/messages` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| DELETE | `/api/chat-ai/:id/messages/:messageId` | [chatAI](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts) |
| GET | `/api/agents/` | [agents](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts) |
| GET | `/api/agents/:id` | [agents](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts) |
| POST | `/api/agents/` | [agents](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts) |
| PATCH | `/api/agents/:id` | [agents](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts) |
| PATCH | `/api/agents/:id/toggle-publish` | [agents](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts) |
| POST | `/api/agents/:id/execute` | [agents](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts) |
| POST | `/api/agents/:id/resume` | [agents](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts) |
| GET | `/api/agents/:id/messages` | [agents](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts) |
| DELETE | `/api/agents/:id/messages` | [agents](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts) |
| DELETE | `/api/agents/:id` | [agents](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts) |
| DELETE | `/api/agents/:id` | [agents](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts) |
| GET | `/api/url-tree/by-id/:contentId` | [urlTree](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/urlTree.ts) |
| GET | `/api/url-tree/:url` | [urlTree](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/urlTree.ts) |
| GET | `/api/restricted-queries/` | [restrictedQuery](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/restrictedQuery.ts) |
| GET | `/api/restricted-queries/knowledge-base/:kbId` | [restrictedQuery](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/restrictedQuery.ts) |
| POST | `/api/restricted-queries/` | [restrictedQuery](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/restrictedQuery.ts) |
| PUT | `/api/restricted-queries/knowledge-base/:kbId` | [restrictedQuery](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/restrictedQuery.ts) |
| DELETE | `/api/restricted-queries/knowledge-base/:kbId` | [restrictedQuery](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/restrictedQuery.ts) |
| GET | `/knowledgebase/webhook/test` | [webhook](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/webhook.ts) |
| GET | `/api/webhook/webhook/test` | [webhook](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/webhook.ts) |
| POST | `/knowledgebase/webhook` | [webhook](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/webhook.ts) |
| POST | `/api/webhook/webhook` | [webhook](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/webhook.ts) |
| POST | `/knowledgebase/sns` | [webhook](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/webhook.ts) |
| POST | `/api/webhook/sns` | [webhook](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/webhook.ts) |

`GET /api/health` is registered directly in `index.ts` and only reports process liveness. The agents router contains duplicate DELETE registrations for the same path in this snapshot.

## RunPod payload examples

Use your own endpoint/credential and a test KB. Examples do not contain working credentials. Full sample JSON files are in [examples](../../examples/README.md).

| Task | Input | Application output |
| --- | --- | --- |
| Embeddings | `text: [string]`, `task: "embeddings"` | Worker returns `{output: vectors}` inside RunPod outer `output` |
| Chat | `user_query`, `kbId`, optional history/settings/flags | KNOWLEDGEBASE.STATUS, KNOWLEDGEBASE.CONTENT with llama_response/tokens/references |
| Transcriber | `s3_key` or `audio_urls`, kbId/content_type/title, optional diarization | SNS-style attribute dictionary, transcript and status |
| Vision | `s3_key` or url, kbId, content_type image/video, title, optional delay | SNS-style attributes, explanation/transcription/scene explanation |

Example request (RunPod outer input wrapper is already in the file):

```bash
curl -X POST "https://api.runpod.ai/v2/YOUR_ENDPOINT_ID/runsync" \
  -H "Authorization: Bearer $RUNPOD_API_KEY" \
  -H "Content-Type: application/json" \
  --data @examples/embedding.json
```

Use `/run` for asynchronous submission and `/status/JOB_ID` for polling. Inspect both platform status and application status. A successful embedding response is normally shaped like `{"status":"COMPLETED","output":{"output":[[...]]}}`. Chat application status is Completed/Failed; the compatibility provider Lambda uses a different Success contract. Preserve punctuation and key names: the chat handler even emits `KNOWLEDGEBASE.ID ` with a trailing space.

## Native SNS Lambda test event

[examples/sns-add-text.json](../../examples/sns-add-text.json) reproduces the native Lambda envelope expected by the KB worker, rather than the Publish API request structure. A live publish must use SNS MessageAttributes with DataType/StringValue. The update webhook expects SNS headers including `x-amz-sns-message-type`, a notification body and Type/Value attributes. See [synchronization](../ingestion/README.md) before constructing manual events.

## Scraper direct invoke

Example payload: `{"KBID":"123","CONTENT":{"url":"https://example.com","depth":0},"CONTENT_TYPE":"url","UNIQUE_ID":"456"}`. Multi-page orchestration adds parent_url and tree_document_id. `RETURN_CONTENT_ONLY` is a separate scraper-only extraction mode; it is not the complete KB indexing flow.
