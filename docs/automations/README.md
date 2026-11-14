---
layout: default
title: "Visual workflows and conversational automations"
---

# Visual workflows and conversational automations

## Architecture

The React builder uses `@xyflow/react` nodes/edges. A saved agent has a graph and publishing/settings metadata in MySQL. Express executes that graph in `agentExecutionService.ts`; there is no separate workflow server to deploy for the implemented nodes. Chat AI nodes call the same assistant service and RunPod/provider paths as ordinary chat.

An execution is a conversation session identified by `executionId`. Stored JSON state includes current node, inputs and context; messages are linked to that execution. Resuming sends the same execution ID with new input. Omitting it starts a fresh session and may remove prior waiting executions for the same agent/user in the service logic. Preserve IDs in the client if continuing a conversation.

## Nodes actually executed

| Node type | Behavior |
| --- | --- |
| `start` | Passes input onward, no message/pause |
| `sendMessage` | Chooses a configured message variant, interpolates variables, emits it; supports configured wait behavior |
| `waitForReply` | Pauses until input arrives, stores/forwards user reply |
| `chatAI` | Calls a selected saved Chat AI; can emit references/tokens/timing and handle input/wait settings |
| `ifElse` | Evaluates a configured condition; follows true/false target without emitting a chat message |
| `jumpAnywhere` / `loopBack` | Jumps to a configured target, carrying current input |
| `intentRecognition` | Supports categories/edge mapping and optional waiting, but currently selects first mapped intent/fallback; classifier TODO |
| `end` | Completes the implemented flow/end behavior |

The dispatcher is the authoritative list. Placeholder nodes shown by a UI palette are not evidence of implemented external actions. The executor limits each traversal to 500 steps to guard against infinite loops.

## Variables

Wrap each variable name in two opening and two closing braces. Supported names are `user.input.latest`, `user.input.first`, `node[ID].user.message`, `node[ID].output.text`, and `chat.messages` when history storage is enabled. Numeric node IDs in templates are resolved to saved graph node IDs. Configuration paths/IDs must remain consistent when importing/editing a graph.

The If/Else executor exposes `message`, `input`, `node` and `user` to a JavaScript expression created with `new Function`. This is server-side executable configuration; it is not a sandboxed expression language. Before allowing untrusted workflow authors in a public deployment, replace it with a constrained evaluator or otherwise enforce a trusted-author boundary. Do not treat graph configuration as harmless display data.

## Create and test a workflow

1. Create/index a KB, then create a Chat AI over it and verify a normal answer.
2. Create an agent with Start → Send Message → Wait for Reply → Chat AI → End.
3. Save the graph and test as its owner before publishing.
4. Submit a first execution request. When waiting_input is returned, retain executionId and submit the reply to resume.
5. Add If/Else paths and assert both outcomes using representative inputs.
6. Add loop-back only after checking termination, duplicate input/message behavior and history.
7. Test publishing/access rules and resume state after restarting the API.

## What needs separate implementation

A complete semantic intent classifier must be added in `executeIntentRecognitionNode`; the current first-branch behavior must not be advertised as reliable natural-language intent recognition. Calendar schedules, cron triggers, arbitrary HTTP action nodes, third-party automation connectors and durable job retries are not established by the checked-in dispatcher. Historical external services or unpublished revisions require their own source/configuration before inclusion.

<span class="source-label">Sources:</span> [woiceai-web/frontend/src/components/AgentBuilder.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/AgentBuilder.tsx) [woiceai-web/backend/src/services/agentExecutionService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/agentExecutionService.ts) [woiceai-web/backend/src/services/agentExecutionService/nodeExecutors.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/agentExecutionService/nodeExecutors.ts) [woiceai-web/backend/src/models/AgentExecution.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/AgentExecution.ts)
{: .source-links }
