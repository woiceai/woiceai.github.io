---
layout: default
title: "Environment templates"
---

# Environment templates

[Documentation home](../README.md) · [Full variable reference](../docs/configuration/README.md)

| Template | Destination |
| --- | --- |
| [Web backend](web-backend.env.example) | backend/.env locally; secret environment in production |
| [Web frontend](web-frontend.env.example) | frontend/.env before build |
| [KB Lambda](lambda-kb.env.example) | Lambda environment configuration |
| [Scraper Lambda](lambda-scrapper.env.example) | Lambda environment configuration |
| [RunPod chat](runpod-chat.env.example) | Chat endpoint environment |
| [RunPod transcriber](runpod-transcriber.ini.example) | Endpoint variables with RunPod secret bindings |
| [RunPod vision](runpod-vision.ini.example) | Endpoint variables with RunPod secret bindings |

The media INI examples preserve the owner's installation identifiers. Replace them for another account. The RunPod double-brace secret bindings are not plain dotenv substitutions. Do not source these examples as shell scripts. Cost coefficients are historical application inputs, not current pricing. Lambda SNS topic constants still require source edits for another account. Never COPY a filled .env into a publicly distributed image.
