---
layout: default
title: "WoiceAI 2.0 documentation"
---

# WoiceAI 2.0 documentation

WoiceAI turns documents, websites, text, audio, images, and video into searchable knowledge bases; exposes configurable chat assistants over that knowledge; and composes assistants into visual conversational workflows.

This is a standalone, GitHub-ready documentation repository. Reviewed **November 5, 2026** against the public source snapshots in [Sources](docs/sources/README.md). The owner's last working deployment is the intended baseline. Source inspection establishes implemented behavior; it does not establish the current health or configuration of a running cloud service.

## Read the documentation

| Guide | Contents |
| --- | --- |
| [Features](docs/features/README.md) | Product capabilities, limitations, supported inputs |
| [Architecture and service inventory](docs/architecture/README.md) | Every required component, dependencies, active versus legacy paths |
| [Installation order](docs/setup/README.md) | Bring up the entire stack in dependency order |
| [Web deployment](docs/web/README.md) | React, Express, MySQL, authentication, hosting |
| [AWS deployment](docs/aws/README.md) | ECR, Lambda, S3, SNS, IAM, callback subscriptions |
| [RunPod deployment](docs/runpod/README.md) | Chat, embeddings, transcriber, explain vision, image builds |
| [Configuration and secrets](docs/configuration/README.md) | Variable matrix, credentials, templates, hardcoded resources |
| [Databases and vector indexing](docs/data/README.md) | MySQL, MongoDB, Atlas Vector Search, consistency |
| [Ingestion and synchronization](docs/ingestion/README.md) | Events, crawl depth, status callbacks, retry, deletion, updates |
| [Chat and models](docs/chat/README.md) | RAG, citations, restrictions, model replacement |
| [Workflow automations](docs/automations/README.md) | Builder, node behavior, sessions, branching, implementation gaps |
| [API reference](docs/api/README.md) | Route inventory and worker payload contracts |
| [Operations and troubleshooting](docs/operations/README.md) | Acceptance tests, failure diagnosis, rollback and backups |
| [Code map](docs/code-map/README.md) | Where to change each capability; linked source inventory |
| [Recovery questions](docs/gaps/README.md) | Missing live infrastructure and reproducibility information |

## Deployment baseline

- Web: `asdkazmi/woiceai-web`, branch `main` (React + Express).
- AWS knowledge-base worker: `asdkazmi/woiceai-ai`, branch `dev-woiceai-kb`, folder `woice_kb`.
- AWS scraper: same repository, branch `dev-scrapper`, folder `scrapper`.
- RunPod chat **and embeddings**: same repository, branch `chat-all-models`, folder `chat-with-all-models`.
- RunPod transcription: `asdkazmi/woiceai-transcriber`, branch `main`.
- RunPod explain vision: `asdkazmi/woiceai-vision`, branch `master`.

Do not deploy the AI repository's `main` tree as though it contained the latest complete system. The `dev-woiceai-chat` branch is not the owner's active major chat backend. The current web source nevertheless still invokes the compatibility chat Lambda for third-party providers and API-key validation; those optional paths need that compatibility service or a code migration.

## Evidence labels

**Source verified** means visible in the linked commit. **Owner supplied** means supplied with the documentation request, including architectural and model details. **Recommended procedure** means a proposed deployment or operational practice, not a claim about existing infrastructure. **Unverified** means cloud settings or behavior cannot be established from the available source.

Actual secret values are intentionally absent. All templates use placeholders. No production deployment, AWS mutation, RunPod mutation, or GitHub publication was performed while preparing this documentation.
