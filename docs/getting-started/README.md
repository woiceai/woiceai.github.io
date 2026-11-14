---
layout: default
title: Getting started
---

# Getting started

Deployment source: [WoiceAI on `main`](https://github.com/asdkazmi/woiceai/tree/main).

WoiceAI lets you build AI assistants and conversational workflows from your own sources. A knowledge base organizes the material, an assistant retrieves it to answer questions, and an agent combines assistants with messages and branching logic.

## Choose where to begin

| What you want to do | Start here |
| --- | --- |
| Understand how the services fit together | [Architecture](../architecture/README.md) |
| Run WoiceAI on your own infrastructure | [Installation order](../setup/README.md) |
| Explore the platform’s capabilities | [Feature overview](../features/README.md) |
| Connect another application to WoiceAI | [API reference](../api/README.md) |

## Try your first assistant

1. Sign in and create a knowledge base from the dashboard.
2. Add a short document or text sample and wait for it to finish indexing.
3. Create a Chat AI for that knowledge base. Enable references if you want to inspect the source behind an answer.
4. Ask a question that the sample can answer. Open the cited source to confirm the answer.
5. To include the assistant in a conversation flow, add a Chat AI node in the agent builder.

The [ingestion guide](../ingestion/README.md) explains indexing and status updates. The [chat guide](../chat/README.md) covers model settings, retrieval and citations, and the [workflow guide](../automations/README.md) explains how to build and test an agent.
