---
layout: default
title: "SQL migration inventory"
---

# SQL migration inventory

Deployment source: [`web/`](https://github.com/asdkazmi/woiceai/tree/main/web).

[Database guide](README.md)

Migration SQL is the authoritative column/default/index definition. Initialization order is in backend/src/index.ts.

| Migration | Tables / changes |
| --- | --- |
| [addContentExplanationsToKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/addContentExplanationsToKnowledgeBaseContentsTable.ts) | `knowledge_base_contents` |
| [addDeletingStatusToKnowledgeBasesTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/addDeletingStatusToKnowledgeBasesTable.ts) | `knowledge_bases` |
| [addIsPublishedToChatAisTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/addIsPublishedToChatAisTable.ts) | `chat_ais` |
| [addRestrictedQuerySupport.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/addRestrictedQuerySupport.ts) | `knowledge_base_contents` |
| [addScrappingStatusToKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/addScrappingStatusToKnowledgeBaseContentsTable.ts) | `knowledge_base_contents` |
| [addTreeDocumentIdToKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/addTreeDocumentIdToKnowledgeBaseContentsTable.ts) | `knowledge_base_contents` |
| [createAgentChatMessagesTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createAgentChatMessagesTable.ts) | `agent_chat_messages` |
| [createAgentExecutionsTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createAgentExecutionsTable.ts) | `agent_executions` |
| [createAgentsTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createAgentsTable.ts) | `agents` |
| [createChatAiMessagesTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createChatAiMessagesTable.ts) | `chat_ai_messages` |
| [createChatAisTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createChatAisTable.ts) | `chat_ais` |
| [createConnectorModelsTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createConnectorModelsTable.ts) | `connector_models` |
| [createConnectorUserTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createConnectorUserTable.ts) | `connector_user` |
| [createConnectorsTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createConnectorsTable.ts) | `connectors` |
| [createKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createKnowledgeBaseContentsTable.ts) | `knowledge_base_contents` |
| [createKnowledgeBasesTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createKnowledgeBasesTable.ts) | `knowledge_bases` |
| [createUserConnectorModelsTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createUserConnectorModelsTable.ts) | `user_connector_models` |
| [createUsersTable.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/migrations/createUsersTable.ts) | `users` |
