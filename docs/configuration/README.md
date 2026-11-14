---
layout: default
title: "Configuration, credentials and secrets"
---

# Configuration, credentials and secrets

[Copyable templates](../../templates/README.md)

## Web backend variables

| Variable | Required/use |
| --- | --- |
| `PORT`, `NODE_ENV` | API port and development/production behavior |
| `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` | MySQL metadata; default database `woice_ai` |
| `JWT_SECRET`, `JWT_EXPIRE` | JWT signing; expiry defaults to `7d` |
| `SESSION_SECRET` | Express OAuth session signing |
| `CORS_ORIGINS` | Comma-separated frontend origins; real CORS control |
| `FRONTEND_URL` | OAuth redirects |
| `BACKEND_URL`, `GOOGLE_CALLBACK_URL` | Optional OAuth API callback base/override |
| `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` | Optional Google login |
| `AWS_REGION` | Defaults to `us-east-1` |
| `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | Web AWS credentials in static-key mode |
| `AWS_SSO_PROFILE` | Switches client creation to default SDK credential chain; configure `AWS_PROFILE`/AWS SDK environment appropriately, since this variable is not passed as a profile name |
| `AWS_S3_BUCKET_NAME` | Upload/reference bucket |
| `MONGODB_URI`, `MONGODB_DATABASE` | Atlas; database should match Python `woice-ai-kb` |
| `RUNPOD_API_KEY`, `RUNPOD_API_ENDPOINT` | Direct default chat; endpoint base without `/run` or `/runsync` |

Frontend: **only** `REACT_APP_API_URL` is needed for API routing. It is public and embedded during the build.

## Python worker variables

| Variable | KB | Scraper | Transcriber | Vision | Chat |
| --- | --- | --- | --- | --- | --- |
| `DB_URI` | Yes | Yes | Yes | Yes | Yes |
| `ACCESS_KEY`, `SECRET_KEY` | S3/SNS/invoke | SNS | S3/SNS | S3/SNS | No AWS use |
| `BUCKET_NAME` | Yes | Not in active scraper reads | Yes | Yes | No |
| `RUNPOD_API_KEY` | Yes | Yes | Yes | Yes | Not needed for incoming RunPod SDK jobs |
| `RUNPOD_BASE_URL` | Chat embeddings | Chat embeddings | Chat embeddings | Chat embeddings | Not read by active handler |
| `TRANSCRIBER_RUNPOD_URL` | Audio dispatch | Helper has optional audio path | No | No | No |
| `EXPLAIN_VISION_RUNPOD_URL` | Image/video dispatch | No | No | No | No |
| `SCRAPPER_LAMBDA_ARN` | URL dispatch | No | No | No | No |
| `RUNPOD_API_COST_PER_SECOND` | Yes | Yes | Yes | Yes | Handler uses placeholder cost |
| `RUNPOD_TRANSCRIBER_COST_PER_SECOND` | Yes | No | Yes | No | No |
| `COST_PER_3GB_MILLISECOND` | Yes | Yes | No | Yes | No |
| `TOPIC_ARN` | Hardcoded instead | Hardcoded instead | Yes | Yes | No |
| `HF_TOKEN` | No | No | Owner-supplied runtime value; gated model artifacts must already be available | Not shown required by active code | Artifacts/access as needed |

`ACCESS_KEY`/`SECRET_KEY` are Python names; they are not interchangeable with the web's `AWS_ACCESS_KEY_ID`/`AWS_SECRET_ACCESS_KEY`. AWS session-token handling is not wired in these custom static-key arguments. Prefer role/default-chain support when adapting deployment code, and test each client.

Set cost variables to the rates for your own infrastructure. Verify the required units in the worker before using these settings for billing.

## RunPod secret references

Replace the example references with the names from your own RunPod secret manager.

| Reference | Supplies |
| --- | --- |
| `YOUR_HF_TOKEN_SECRET` | Hugging Face token |
| `YOUR_AWS_ACCESS_KEY_SECRET` | AWS access key ID |
| `YOUR_AWS_SECRET_KEY_SECRET` | AWS secret access key |
| `YOUR_ATLAS_URI_SECRET` | Atlas connection URI |
| `YOUR_RUNPOD_API_KEY_SECRET` | RunPod API key used by nested embedding requests |

The double-brace values in the supplied INI templates are platform references, not actual credentials and not ordinary dotenv interpolation. Create the secrets first, then bind them in endpoint configuration. For a plain local `.env`, replace the references with local values through your secret tooling.

## Hardcoded values that must change for another installation

- Input topic: `web/backend/src/services/aws/snsService.ts`.
- Provider chat and validation ARN: `lambdaService.ts`, `lambdaValidationService.ts`.
- Update topic in both Lambda workers: `indexer/src/modules/sns.py`, `scraper/src/modules/sns.py`; changing `TOPIC_ARN` alone does not change these.
- Python MongoDB database name: worker `mongo.py`, scraper handler, chat handler.
- Vector collection/path/index name: chat `modules/vector.py`, ingest writers' `bgeVectors` fields.
- Models/artifact paths: chat handler/Dockerfile, transcriber models/Dockerfile, vision models/transcribing_video/Dockerfile.

## Obtain, store and rotate

Create dedicated database users; keep the Atlas URI on server/worker environments. Obtain AWS IAM credentials for only the bucket/topic/function operations required. Create RunPod API credentials in the account managing these endpoints. Obtain Hugging Face access and accept relevant gated-model licenses. Google OAuth credentials belong in the backend only. Provider API keys enter through connector settings only when that compatibility path is operational.

Use deployment secret storage, omit real `.env` files from Git, and avoid Docker COPY of secrets. Rotate a shared key in every producer/consumer, redeploy/restart affected processes, test, then revoke the previous key. Inspect image history/files for baked secrets before publishing a rebuilt image. Avoid copying unredacted logs: these sources log payloads and the legacy Lambda even logs a fetched provider key.

<span class="source-label">Sources:</span> `web/backend/src/config/env.example.txt` `web/backend/src/services/runpodService.ts` [indexer/src/modules/embeddings.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/src/modules/embeddings.py) [chat-service/src/handler.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/handler.py)
{: .source-links }
