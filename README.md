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

The WoiceAI repository organizes the services by directory.

- [web/](https://github.com/asdkazmi/woiceai/tree/main/web)
- [chat-service/](https://github.com/asdkazmi/woiceai/tree/main/chat-service)
- [indexer/](https://github.com/asdkazmi/woiceai/tree/main/indexer)
- [scraper/](https://github.com/asdkazmi/woiceai/tree/main/scraper)
- [audio-transcriber/](https://github.com/asdkazmi/woiceai/tree/main/audio-transcriber)
- [vision-service/](https://github.com/asdkazmi/woiceai/tree/main/vision-service)

Optional third-party connectors still depend on the compatibility Lambda described in the setup guide.

## Evidence labels

**Source verified** means visible in the linked commit. **Owner supplied** means supplied with the documentation request, including architectural and model details. **Recommended procedure** means a proposed deployment or operational practice, not a claim about existing infrastructure. **Unverified** means cloud settings or behavior cannot be established from the available source.

Actual secret values are intentionally absent. All templates use placeholders. No production deployment, AWS mutation, RunPod mutation, or GitHub publication was performed while preparing this documentation.
