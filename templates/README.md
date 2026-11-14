---
layout: default
title: "Environment templates"
---

# Environment templates

[Full variable reference](../docs/configuration/README.md)

| Template | Destination |
| --- | --- |
| [Web backend](web-backend.env.example) | `web/backend/.env` locally; secret environment in production |
| [Web frontend](web-frontend.env.example) | `web/frontend/.env` before build |
| [Indexer Lambda](lambda-kb.env.example) | Lambda environment configuration |
| [Scraper Lambda](lambda-scrapper.env.example) | Lambda environment configuration |
| [RunPod chat](runpod-chat.env.example) | Chat endpoint environment |
| [RunPod transcriber](runpod-transcriber.ini.example) | Endpoint variables with RunPod secret bindings |
| [RunPod vision](runpod-vision.ini.example) | Endpoint variables with RunPod secret bindings |

Fill the media templates with the endpoint IDs, bucket, topic ARN and secret references for your environment. The RunPod double-brace secret bindings are not plain dotenv substitutions. Do not source these examples as shell scripts. Fill cost coefficients with the rates for your own environment. Lambda SNS topic constants still require source edits for another account. Never COPY a filled .env into a publicly distributed image.
