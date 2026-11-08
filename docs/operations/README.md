---
layout: default
title: "Operations, acceptance tests and troubleshooting"
---

# Operations, acceptance tests and troubleshooting

These are manual acceptance procedures for an isolated test KB. Cloud inference and uploads may incur costs. They were documented, not executed against production during this review.

## Release acceptance

| Test | Pass condition |
| --- | --- |
| API startup | SQL migrations/seeding complete; actual authenticated DB read works |
| Atlas | Connection succeeds; vector index queryable; known KB filter returns only its documents |
| Embeddings | One request returns numeric vectors with expected dimension |
| Text and PDF | Completed callback; SQL indexed; chunks in Atlas; PDF citation resolves correct source/page |
| DOCX/TXT | Content extracted and queryable |
| URL depth 0 | Only supplied page processed |
| URL depth >0 | Parent/child tree recorded, progress updates, failed nodes visible |
| Audio | Short sample transcript saved; question answered from audio; diarization tested separately if used |
| Image | Explanation saved and answer grounded in image description |
| Video | Spoken transcript and timestamped scene explanation saved and retrievable |
| References | Citation numbering matches returned list; private S3 access uses expiring URLs |
| Restrictions | Known restricted question yields intended validation; unrelated query still works |
| Isolation | Different users/KBs cannot retrieve each other's data through application paths |
| History | Follow-up question rewrites/answers correctly |
| Workflow | Wait/resume with same executionId, both condition branches, loop termination, persisted messages |
| Delete | Item vectors disappear; whole KB exits deleting after completion callback |
| Cold starts | Web sync and worker polling paths handle queued/in-progress responses |
| Provider connector (optional) | Key validation and chat use intended provider; keys resolve across stores |

Intent classification is an expected gap in this source, not an acceptance pass. Verify the deployed source/build if the historical installation behaved differently.

## Failure diagnosis

| Symptom | Check |
| --- | --- |
| UI stays pending/processing | Input SNS subscription and Lambda invoke permission; worker logs; update-topic ARN; HTTPS subscription confirmation; webhook correlation |
| Vectors exist but UI pending | Update publish failed, callback rejected, wrong topic/subscription or UNIQUE_ID/content mismatch |
| UI indexed but empty chat | Atlas vector index/dimension; string KB ID filter; database/collection; actual vector writes; application-level job status |
| Chat fails immediately | RUNPOD_API_KEY/base; endpoint worker logs; model artifact paths; Atlas DB_URI |
| Rebuild cannot start | Missing GGUF/GPTQ artifacts; flash-attn/CUDA mismatch; offline Stella files; actual GPU VRAM |
| Embedding unpack/type errors under load | Sync versus polling fallback return shapes in embeddings.py |
| Website fails | Chromium/driver binary compatibility; outbound network; CAPTCHA/auth; page filtering; Lambda timeout |
| Audio fails | S3 access/key; FFmpeg; Parakeet artifact; local pyannote config/gated model files; nested embeddings |
| Video speech succeeds but no scenes | Qwen-VL load/VRAM/frame extraction; frame delay; missing scene processing output |
| Provider says missing API key | SQL connector ID vs Atlas keys ID mismatch; missing compatibility Lambda; provider availability |
| Deletion stuck | Lambda cleanup result and update-topic callback; current SQL deleting state |
| Duplicate answers/chunks | SNS replay, timed-out job still writing, non-idempotent insert_many |
| CORS/Google login failure | CORS_ORIGINS versus FRONTEND_URL; callback URL; sessions/cookies; build-time frontend API URL |

## Observability

Correlate SQL KB/content IDs, SNS MessageId, Lambda request ID and RunPod job ID. Capture each worker's source SHA and image digest. Monitor Lambda errors/duration/throttles, SNS delivery failures, RunPod queue/startup/execution failures, Atlas connectivity/index state and API error logs. Separate liveness from dependency readiness.

Logs in the provided code include full payloads and some credential-bearing data. Restrict log access and redact before sharing. Keep transcripts/customer content out of public deployment records.

## Backup and disaster recovery

Back up MySQL, Atlas and S3 with a consistent record of content/source identifiers. Preserve vector index JSON, IAM policies/subscriptions, redacted environment names, model checksums/licenses and container digests. A source checkout alone cannot restore the locally compiled GGUF model or undocumented cloud configuration.

Restore databases/object storage and index definitions, then deploy pinned images, reconnect callbacks and validate a known KB before allowing new ingestion. If switching embedding models, create a migration plan and regenerate vectors; do not reuse old vectors with a new model just because dimensions match.

## Rollback

Record previous API/static build versions, Lambda image digests and RunPod image/config snapshots before a release. Roll back worker images and web artifacts together when their payload contracts change. Database schema changes need an explicit compatibility/restore plan; image rollback does not undo migrations. Retain old model artifacts until the new release passes known-KB and citation tests.

## Cost accounting

Treat historical per-second coefficients as estimates only. Chat source uses a placeholder time-based cost, and web SNS charging remains TODO. Actual costs include GPU idle/minimum workers/cold starts, storage, traffic, Lambda duration and external provider usage. Reconcile billing from service usage before exposing credits as money-backed accounting.
