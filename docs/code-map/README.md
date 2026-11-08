---
layout: default
title: "Code map and extension points"
---

# Code map and extension points

## Where to change behavior

| Capability | Main files |
| --- | --- | --- |
| Web bootstrap/routes/migrations | [backend/src/index.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/index.ts) |
| Upload, indexing dispatch, retry and deletion | [backend/src/services/knowledgeBaseService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/knowledgeBaseService.ts) |
| SNS contract / callback | `backend/src/services/aws/snsService.ts`, [backend/src/routes/webhook.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/webhook.ts) |
| Web chat settings and provider routing | [backend/src/services/chatAIService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/chatAIService.ts), [backend/src/services/connectorService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/connectorService.ts) |
| Visual builder and node configuration | [frontend/src/components/AgentBuilder.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/AgentBuilder.tsx), [frontend/src/components/agent-nodes/NodeConfigPanel.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/agent-nodes/NodeConfigPanel.tsx) |
| Workflow traversal / node implementations | [backend/src/services/agentExecutionService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/agentExecutionService.ts), [backend/src/services/agentExecutionService/nodeExecutors.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/agentExecutionService/nodeExecutors.ts) |
| File parsing and media dispatch | `woice_kb/src/handler.py`, [woice_kb/src/modules/reading.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/src/modules/reading.py), [woice_kb/src/modules/embeddings.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/src/modules/embeddings.py) |
| Crawl extraction/filtering | [scrapper/src/modules/seleniumCode.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/src/modules/seleniumCode.py), [scrapper/src/modules/filtering_urls.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/src/modules/filtering_urls.py) |
| Chat models and payload dispatch | [chat-with-all-models/src/handler.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/handler.py) |
| Retrieval / embeddings | [chat-with-all-models/src/modules/vector.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/vector.py), [chat-with-all-models/src/modules/stella.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/stella.py) |
| Prompt and citation behavior | [chat-with-all-models/src/modules/generate_prompt.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/generate_prompt.py), [chat-with-all-models/src/modules/response.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/response.py) |
| GemFilter | [chat-with-all-models/src/modules/applygemfilter.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/applygemfilter.py) and llama_gemfilter subtree |
| Audio ASR/diarization | [src/models.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/models.py), [src/transcriber.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/transcriber.py) |
| Vision and video speech | [src/modules/models.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/models.py), [src/modules/transcribing_video.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/transcribing_video.py) |

## Linked implementation inventory

Only service-specific branch directories are included; stale siblings in AI branches are excluded. Deprecated/archive files are excluded from this active map.

### web

- [backend/src/config/database.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/config/database.ts)
- `backend/src/config/env.example.txt`
- [backend/src/config/googleAuth.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/config/googleAuth.ts)
- [backend/src/index.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/index.ts)
- [backend/src/middleware/auth.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/middleware/auth.ts)
- [backend/src/migrations/addContentExplanationsToKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/addContentExplanationsToKnowledgeBaseContentsTable.ts)
- [backend/src/migrations/addDeletingStatusToKnowledgeBasesTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/addDeletingStatusToKnowledgeBasesTable.ts)
- [backend/src/migrations/addIsPublishedToChatAisTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/addIsPublishedToChatAisTable.ts)
- [backend/src/migrations/addRestrictedQuerySupport.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/addRestrictedQuerySupport.ts)
- [backend/src/migrations/addScrappingStatusToKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/addScrappingStatusToKnowledgeBaseContentsTable.ts)
- [backend/src/migrations/addTreeDocumentIdToKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/addTreeDocumentIdToKnowledgeBaseContentsTable.ts)
- [backend/src/migrations/createAgentChatMessagesTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createAgentChatMessagesTable.ts)
- [backend/src/migrations/createAgentExecutionsTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createAgentExecutionsTable.ts)
- [backend/src/migrations/createAgentsTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createAgentsTable.ts)
- [backend/src/migrations/createChatAiMessagesTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createChatAiMessagesTable.ts)
- [backend/src/migrations/createChatAisTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createChatAisTable.ts)
- [backend/src/migrations/createConnectorModelsTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createConnectorModelsTable.ts)
- [backend/src/migrations/createConnectorUserTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createConnectorUserTable.ts)
- [backend/src/migrations/createConnectorsTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createConnectorsTable.ts)
- [backend/src/migrations/createKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createKnowledgeBaseContentsTable.ts)
- [backend/src/migrations/createKnowledgeBasesTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createKnowledgeBasesTable.ts)
- [backend/src/migrations/createUserConnectorModelsTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createUserConnectorModelsTable.ts)
- [backend/src/migrations/createUsersTable.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/migrations/createUsersTable.ts)
- [backend/src/models/Agent.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/Agent.ts)
- [backend/src/models/AgentChatMessage.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/AgentChatMessage.ts)
- [backend/src/models/AgentExecution.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/AgentExecution.ts)
- [backend/src/models/ChatAI.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/ChatAI.ts)
- [backend/src/models/ChatAIMessage.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/ChatAIMessage.ts)
- [backend/src/models/Connector.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/Connector.ts)
- [backend/src/models/ConnectorModel.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/ConnectorModel.ts)
- [backend/src/models/ConnectorUser.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/ConnectorUser.ts)
- [backend/src/models/KnowledgeBase.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/KnowledgeBase.ts)
- [backend/src/models/User.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/User.ts)
- [backend/src/models/UserConnectorModel.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/models/UserConnectorModel.ts)
- [backend/src/routes/agents.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/agents.ts)
- [backend/src/routes/auth.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/auth.ts)
- [backend/src/routes/chatAI.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/chatAI.ts)
- [backend/src/routes/connector.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/connector.ts)
- [backend/src/routes/knowledgeBase.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/knowledgeBase.ts)
- [backend/src/routes/restrictedQuery.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/restrictedQuery.ts)
- [backend/src/routes/urlTree.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/urlTree.ts)
- [backend/src/routes/webhook.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/webhook.ts)
- [backend/src/scripts/createTestUser.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/scripts/createTestUser.ts)
- [backend/src/scripts/seedConnectors.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/scripts/seedConnectors.ts)
- [backend/src/scripts/testLogin.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/scripts/testLogin.ts)
- [backend/src/services/agentExecutionService/nodeExecutors.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/agentExecutionService/nodeExecutors.ts)
- [backend/src/services/agentExecutionService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/agentExecutionService.ts)
- [backend/src/services/agentService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/agentService.ts)
- `backend/src/services/aws/lambdaService.ts`
- `backend/src/services/aws/lambdaValidationService.ts`
- [backend/src/services/aws/s3Service.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/aws/s3Service.ts)
- `backend/src/services/aws/snsService.ts`
- [backend/src/services/chatAIService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/chatAIService.ts)
- [backend/src/services/connectorService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/connectorService.ts)
- [backend/src/services/knowledgeBaseContentHelper.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/knowledgeBaseContentHelper.ts)
- [backend/src/services/knowledgeBaseService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/knowledgeBaseService.ts)
- [backend/src/services/mongodbService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/mongodbService.ts)
- [backend/src/services/restrictedQueryService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/services/restrictedQueryService.ts)
- `backend/src/services/runpodService.ts`
- [frontend/src/App.test.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/App.test.tsx)
- [frontend/src/App.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/App.tsx)
- [frontend/src/components/AddContentModal.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/AddContentModal.tsx)
- [frontend/src/components/AgentBuilder.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/AgentBuilder.tsx)
- [frontend/src/components/AgentBuilderChat.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/AgentBuilderChat.tsx)
- [frontend/src/components/AgentChat.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/AgentChat.tsx)
- [frontend/src/components/AgentsList.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/AgentsList.tsx)
- [frontend/src/components/AudioContentModal.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/AudioContentModal.tsx)
- [frontend/src/components/AuthCallback.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/AuthCallback.tsx)
- [frontend/src/components/ChatAIInterface.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ChatAIInterface.tsx)
- [frontend/src/components/ChatAIModal.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ChatAIModal.tsx)
- [frontend/src/components/ChatAIPage.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ChatAIPage.tsx)
- [frontend/src/components/ConnectorsList.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ConnectorsList.tsx)
- [frontend/src/components/CreateChatAINameModal.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/CreateChatAINameModal.tsx)
- [frontend/src/components/CreateKnowledgeBaseModal.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/CreateKnowledgeBaseModal.tsx)
- [frontend/src/components/Dashboard.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/Dashboard.tsx)
- [frontend/src/components/DashboardPage.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/DashboardPage.tsx)
- [frontend/src/components/ErrorBoundary.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ErrorBoundary.tsx)
- [frontend/src/components/ImageContentModal.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ImageContentModal.tsx)
- [frontend/src/components/KnowledgeBaseDetail.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/KnowledgeBaseDetail.tsx)
- [frontend/src/components/KnowledgeBaseList.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/KnowledgeBaseList.tsx)
- [frontend/src/components/Layout.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/Layout.tsx)
- [frontend/src/components/Login.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/Login.tsx)
- [frontend/src/components/ReferenceModal.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ReferenceModal.tsx)
- [frontend/src/components/UrlTreeModal.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/UrlTreeModal.tsx)
- [frontend/src/components/VideoContentModal.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/VideoContentModal.tsx)
- [frontend/src/components/agent-nodes/ChatAINode.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/agent-nodes/ChatAINode.tsx)
- [frontend/src/components/agent-nodes/EndNode.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/agent-nodes/EndNode.tsx)
- [frontend/src/components/agent-nodes/IfElseNode.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/agent-nodes/IfElseNode.tsx)
- [frontend/src/components/agent-nodes/IntentRecognitionNode.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/agent-nodes/IntentRecognitionNode.tsx)
- [frontend/src/components/agent-nodes/LoopBackNode.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/agent-nodes/LoopBackNode.tsx)
- [frontend/src/components/agent-nodes/NodeConfigPanel.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/agent-nodes/NodeConfigPanel.tsx)
- [frontend/src/components/agent-nodes/PlaceholderNode.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/agent-nodes/PlaceholderNode.tsx)
- [frontend/src/components/agent-nodes/SendMessageNode.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/agent-nodes/SendMessageNode.tsx)
- [frontend/src/components/agent-nodes/StartNode.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/agent-nodes/StartNode.tsx)
- [frontend/src/components/agent-nodes/WaitForReplyNode.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/agent-nodes/WaitForReplyNode.tsx)
- [frontend/src/components/edges/AddNodeEdge.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/edges/AddNodeEdge.tsx)
- [frontend/src/components/edges/LoopBackEdge.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/edges/LoopBackEdge.tsx)
- [frontend/src/components/ui/Badge.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ui/Badge.tsx)
- [frontend/src/components/ui/Button.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ui/Button.tsx)
- [frontend/src/components/ui/CircularProgress.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ui/CircularProgress.tsx)
- [frontend/src/components/ui/ConfirmModal.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ui/ConfirmModal.tsx)
- [frontend/src/components/ui/IconButton.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ui/IconButton.tsx)
- [frontend/src/components/ui/Input.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ui/Input.tsx)
- [frontend/src/components/ui/Pagination.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ui/Pagination.tsx)
- [frontend/src/components/ui/PieChart.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ui/PieChart.tsx)
- [frontend/src/components/ui/ProgressBar.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ui/ProgressBar.tsx)
- [frontend/src/components/ui/Spinner.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/components/ui/Spinner.tsx)
- [frontend/src/index.tsx](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/index.tsx)
- [frontend/src/react-app-env.d.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/react-app-env.d.ts)
- [frontend/src/reportWebVitals.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/reportWebVitals.ts)
- [frontend/src/services/agentService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/services/agentService.ts)
- [frontend/src/services/api.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/services/api.ts)
- [frontend/src/services/authService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/services/authService.ts)
- [frontend/src/services/chatAIService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/services/chatAIService.ts)
- [frontend/src/services/connectorService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/services/connectorService.ts)
- [frontend/src/services/knowledgeBaseService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/services/knowledgeBaseService.ts)
- [frontend/src/services/urlTreeService.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/services/urlTreeService.ts)
- [frontend/src/setupTests.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/frontend/src/setupTests.ts)

### chat

- [chat-with-all-models/Dockerfile](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/Dockerfile)
- [chat-with-all-models/requirements.txt](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/requirements.txt)
- [chat-with-all-models/src/handler.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/handler.py)
- [chat-with-all-models/src/modules/applygemfilter.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/applygemfilter.py)
- [chat-with-all-models/src/modules/bge.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/bge.py)
- [chat-with-all-models/src/modules/fetch_custom_db.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/fetch_custom_db.py)
- [chat-with-all-models/src/modules/generate_prompt.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/generate_prompt.py)
- [chat-with-all-models/src/modules/llama.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/llama.py)
- [chat-with-all-models/src/modules/llama_gemfilter/gem_filter_utils.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/llama_gemfilter/gem_filter_utils.py)
- [chat-with-all-models/src/modules/llama_gemfilter/llama_select_attention.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/llama_gemfilter/llama_select_attention.py)
- [chat-with-all-models/src/modules/llama_gemfilter/load_model.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/llama_gemfilter/load_model.py)
- [chat-with-all-models/src/modules/llama_gemfilter/my_generation.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/llama_gemfilter/my_generation.py)
- [chat-with-all-models/src/modules/response.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/response.py)
- [chat-with-all-models/src/modules/rewrite_query.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/rewrite_query.py)
- [chat-with-all-models/src/modules/stella.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/stella.py)
- [chat-with-all-models/src/modules/vector.py](https://github.com/asdkazmi/woiceai-ai/blob/699361213594230ce1a4bad9085eeb657e5a8e8a/chat-with-all-models/src/modules/vector.py)

### kb

- [woice_kb/Dockerfile](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/Dockerfile)
- [woice_kb/app.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/app.py)
- [woice_kb/requirements.txt](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/requirements.txt)
- `woice_kb/src/handler.py`
- [woice_kb/src/modules/chunks.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/src/modules/chunks.py)
- [woice_kb/src/modules/credits.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/src/modules/credits.py)
- [woice_kb/src/modules/custom_mongodb_pipeline.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/src/modules/custom_mongodb_pipeline.py)
- [woice_kb/src/modules/embeddings.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/src/modules/embeddings.py)
- [woice_kb/src/modules/mongo.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/src/modules/mongo.py)
- [woice_kb/src/modules/reading.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/src/modules/reading.py)
- [woice_kb/src/modules/s3download.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/src/modules/s3download.py)
- `woice_kb/src/modules/sns.py`

### scrapper

- [scrapper/Dockerfile](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/Dockerfile)
- [scrapper/app.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/app.py)
- [scrapper/requirements.txt](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/requirements.txt)
- [scrapper/src/handler.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/src/handler.py)
- [scrapper/src/modules/chunks.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/src/modules/chunks.py)
- [scrapper/src/modules/credits.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/src/modules/credits.py)
- [scrapper/src/modules/custom_mongodb_handling.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/src/modules/custom_mongodb_handling.py)
- [scrapper/src/modules/detectCaptcha.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/src/modules/detectCaptcha.py)
- [scrapper/src/modules/embeddings.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/src/modules/embeddings.py)
- [scrapper/src/modules/filtering_urls.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/src/modules/filtering_urls.py)
- [scrapper/src/modules/mongo.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/src/modules/mongo.py)
- [scrapper/src/modules/seleniumCode.py](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/src/modules/seleniumCode.py)
- `scrapper/src/modules/sns.py`

### transcriber

- [Dockerfile](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/Dockerfile)
- [requirements.txt](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/requirements.txt)
- [src/app.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/app.py)
- [src/flask_app.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/flask_app.py)
- [src/models.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/models.py)
- [src/modules/chunks.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/modules/chunks.py)
- [src/modules/converting_to_wav.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/modules/converting_to_wav.py)
- [src/modules/credits.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/modules/credits.py)
- [src/modules/custom_mongodb_handling.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/modules/custom_mongodb_handling.py)
- [src/modules/embeddings.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/modules/embeddings.py)
- [src/modules/mongo.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/modules/mongo.py)
- [src/modules/s3download.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/modules/s3download.py)
- [src/modules/sns.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/modules/sns.py)
- [src/transcriber.py](https://github.com/asdkazmi/woiceai-transcriber/blob/fa7dfed55433d2cb4a56100ead970d0b16499eef/src/transcriber.py)

### vision

- [Dockerfile](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/Dockerfile)
- [requirements.txt](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/requirements.txt)
- [src/app.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/app.py)
- [src/modules/chunks.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/chunks.py)
- [src/modules/credits.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/credits.py)
- [src/modules/custom_mongodb_handling.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/custom_mongodb_handling.py)
- [src/modules/embeddings.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/embeddings.py)
- [src/modules/llama.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/llama.py)
- [src/modules/models.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/models.py)
- [src/modules/mongo.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/mongo.py)
- [src/modules/process_image.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/process_image.py)
- [src/modules/process_video.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/process_video.py)
- [src/modules/s3download.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/s3download.py)
- [src/modules/sns.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/sns.py)
- [src/modules/transcribing_video.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/transcribing_video.py)
- [src/modules/video_to_image_frames.py](https://github.com/asdkazmi/woiceai-vision/blob/6bfd7581c2d3ee7ea7f79100a2eb624076ae01e2/src/modules/video_to_image_frames.py)

### legacy

- [woice_chat/Dockerfile](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/Dockerfile)
- [woice_chat/src/handler.py](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/src/handler.py)
- [woice_chat/src/modules/credits.py](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/src/modules/credits.py)
- [woice_chat/src/modules/fetch_custom_mongodb.py](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/src/modules/fetch_custom_mongodb.py)
- [woice_chat/src/modules/query_rewrite.py](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/src/modules/query_rewrite.py)
- [woice_chat/src/modules/response.py](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/src/modules/response.py)
- [woice_chat/src/modules/runpod.py](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/src/modules/runpod.py)
- [woice_chat/src/modules/stella.py](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/src/modules/stella.py)
- [woice_chat/src/modules/third_party_llms.py](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/src/modules/third_party_llms.py)
- [woice_chat/src/modules/validate_api_key.py](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/src/modules/validate_api_key.py)
- [woice_chat/src/modules/vector.py](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/src/modules/vector.py)
