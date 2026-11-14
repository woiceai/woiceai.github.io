---
layout: default
title: "Code map and extension points"
---

# Code map and extension points

## Where to change behavior

| Capability | Main files |
| --- | --- | --- |
| Web bootstrap/routes/migrations | [backend/src/index.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/index.ts) |
| Upload, indexing dispatch, retry and deletion | [backend/src/services/knowledgeBaseService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/knowledgeBaseService.ts) |
| SNS contract / callback | `backend/src/services/aws/snsService.ts`, [backend/src/routes/webhook.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/routes/webhook.ts) |
| Web chat settings and provider routing | [backend/src/services/chatAIService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/chatAIService.ts), [backend/src/services/connectorService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/connectorService.ts) |
| Visual builder and node configuration | [frontend/src/components/AgentBuilder.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/AgentBuilder.tsx), [frontend/src/components/agent-nodes/NodeConfigPanel.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/agent-nodes/NodeConfigPanel.tsx) |
| Workflow traversal / node implementations | [backend/src/services/agentExecutionService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/agentExecutionService.ts), [backend/src/services/agentExecutionService/nodeExecutors.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/agentExecutionService/nodeExecutors.ts) |
| File parsing and media dispatch | `indexer/src/handler.py`, [indexer/src/modules/reading.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/src/modules/reading.py), [indexer/src/modules/embeddings.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/src/modules/embeddings.py) |
| Crawl extraction/filtering | [scraper/src/modules/seleniumCode.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/modules/seleniumCode.py), [scraper/src/modules/filtering_urls.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/modules/filtering_urls.py) |
| Chat models and payload dispatch | [chat-service/src/handler.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/handler.py) |
| Retrieval / embeddings | [chat-service/src/modules/vector.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/vector.py), [chat-service/src/modules/stella.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/stella.py) |
| Prompt and citation behavior | [chat-service/src/modules/generate_prompt.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/generate_prompt.py), [chat-service/src/modules/response.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/response.py) |
| GemFilter | [chat-service/src/modules/applygemfilter.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/applygemfilter.py) and llama_gemfilter subtree |
| Audio ASR/diarization | [src/models.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/models.py), [src/transcriber.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/transcriber.py) |
| Vision and video speech | [src/modules/models.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/models.py), [src/modules/transcribing_video.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/transcribing_video.py) |

## Linked implementation inventory

Only service-specific branch directories are included; stale siblings in AI branches are excluded. Deprecated/archive files are excluded from this active map.

### web

- [backend/src/config/database.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/config/database.ts)
- `backend/src/config/env.example.txt`
- [backend/src/config/googleAuth.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/config/googleAuth.ts)
- [backend/src/index.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/index.ts)
- [backend/src/middleware/auth.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/middleware/auth.ts)
- [backend/src/migrations/addContentExplanationsToKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/addContentExplanationsToKnowledgeBaseContentsTable.ts)
- [backend/src/migrations/addDeletingStatusToKnowledgeBasesTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/addDeletingStatusToKnowledgeBasesTable.ts)
- [backend/src/migrations/addIsPublishedToChatAisTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/addIsPublishedToChatAisTable.ts)
- [backend/src/migrations/addRestrictedQuerySupport.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/addRestrictedQuerySupport.ts)
- [backend/src/migrations/addScrappingStatusToKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/addScrappingStatusToKnowledgeBaseContentsTable.ts)
- [backend/src/migrations/addTreeDocumentIdToKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/addTreeDocumentIdToKnowledgeBaseContentsTable.ts)
- [backend/src/migrations/createAgentChatMessagesTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createAgentChatMessagesTable.ts)
- [backend/src/migrations/createAgentExecutionsTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createAgentExecutionsTable.ts)
- [backend/src/migrations/createAgentsTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createAgentsTable.ts)
- [backend/src/migrations/createChatAiMessagesTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createChatAiMessagesTable.ts)
- [backend/src/migrations/createChatAisTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createChatAisTable.ts)
- [backend/src/migrations/createConnectorModelsTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createConnectorModelsTable.ts)
- [backend/src/migrations/createConnectorUserTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createConnectorUserTable.ts)
- [backend/src/migrations/createConnectorsTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createConnectorsTable.ts)
- [backend/src/migrations/createKnowledgeBaseContentsTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createKnowledgeBaseContentsTable.ts)
- [backend/src/migrations/createKnowledgeBasesTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createKnowledgeBasesTable.ts)
- [backend/src/migrations/createUserConnectorModelsTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createUserConnectorModelsTable.ts)
- [backend/src/migrations/createUsersTable.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/migrations/createUsersTable.ts)
- [backend/src/models/Agent.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/Agent.ts)
- [backend/src/models/AgentChatMessage.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/AgentChatMessage.ts)
- [backend/src/models/AgentExecution.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/AgentExecution.ts)
- [backend/src/models/ChatAI.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/ChatAI.ts)
- [backend/src/models/ChatAIMessage.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/ChatAIMessage.ts)
- [backend/src/models/Connector.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/Connector.ts)
- [backend/src/models/ConnectorModel.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/ConnectorModel.ts)
- [backend/src/models/ConnectorUser.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/ConnectorUser.ts)
- [backend/src/models/KnowledgeBase.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/KnowledgeBase.ts)
- [backend/src/models/User.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/User.ts)
- [backend/src/models/UserConnectorModel.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/models/UserConnectorModel.ts)
- [backend/src/routes/agents.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/routes/agents.ts)
- [backend/src/routes/auth.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/routes/auth.ts)
- [backend/src/routes/chatAI.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/routes/chatAI.ts)
- [backend/src/routes/connector.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/routes/connector.ts)
- [backend/src/routes/knowledgeBase.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/routes/knowledgeBase.ts)
- [backend/src/routes/restrictedQuery.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/routes/restrictedQuery.ts)
- [backend/src/routes/urlTree.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/routes/urlTree.ts)
- [backend/src/routes/webhook.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/routes/webhook.ts)
- [backend/src/scripts/createTestUser.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/scripts/createTestUser.ts)
- [backend/src/scripts/seedConnectors.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/scripts/seedConnectors.ts)
- [backend/src/scripts/testLogin.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/scripts/testLogin.ts)
- [backend/src/services/agentExecutionService/nodeExecutors.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/agentExecutionService/nodeExecutors.ts)
- [backend/src/services/agentExecutionService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/agentExecutionService.ts)
- [backend/src/services/agentService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/agentService.ts)
- `backend/src/services/aws/lambdaService.ts`
- `backend/src/services/aws/lambdaValidationService.ts`
- [backend/src/services/aws/s3Service.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/aws/s3Service.ts)
- `backend/src/services/aws/snsService.ts`
- [backend/src/services/chatAIService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/chatAIService.ts)
- [backend/src/services/connectorService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/connectorService.ts)
- [backend/src/services/knowledgeBaseContentHelper.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/knowledgeBaseContentHelper.ts)
- [backend/src/services/knowledgeBaseService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/knowledgeBaseService.ts)
- [backend/src/services/mongodbService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/mongodbService.ts)
- [backend/src/services/restrictedQueryService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/backend/src/services/restrictedQueryService.ts)
- `backend/src/services/runpodService.ts`
- [frontend/src/App.test.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/App.test.tsx)
- [frontend/src/App.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/App.tsx)
- [frontend/src/components/AddContentModal.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/AddContentModal.tsx)
- [frontend/src/components/AgentBuilder.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/AgentBuilder.tsx)
- [frontend/src/components/AgentBuilderChat.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/AgentBuilderChat.tsx)
- [frontend/src/components/AgentChat.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/AgentChat.tsx)
- [frontend/src/components/AgentsList.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/AgentsList.tsx)
- [frontend/src/components/AudioContentModal.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/AudioContentModal.tsx)
- [frontend/src/components/AuthCallback.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/AuthCallback.tsx)
- [frontend/src/components/ChatAIInterface.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ChatAIInterface.tsx)
- [frontend/src/components/ChatAIModal.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ChatAIModal.tsx)
- [frontend/src/components/ChatAIPage.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ChatAIPage.tsx)
- [frontend/src/components/ConnectorsList.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ConnectorsList.tsx)
- [frontend/src/components/CreateChatAINameModal.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/CreateChatAINameModal.tsx)
- [frontend/src/components/CreateKnowledgeBaseModal.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/CreateKnowledgeBaseModal.tsx)
- [frontend/src/components/Dashboard.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/Dashboard.tsx)
- [frontend/src/components/DashboardPage.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/DashboardPage.tsx)
- [frontend/src/components/ErrorBoundary.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ErrorBoundary.tsx)
- [frontend/src/components/ImageContentModal.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ImageContentModal.tsx)
- [frontend/src/components/KnowledgeBaseDetail.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/KnowledgeBaseDetail.tsx)
- [frontend/src/components/KnowledgeBaseList.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/KnowledgeBaseList.tsx)
- [frontend/src/components/Layout.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/Layout.tsx)
- [frontend/src/components/Login.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/Login.tsx)
- [frontend/src/components/ReferenceModal.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ReferenceModal.tsx)
- [frontend/src/components/UrlTreeModal.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/UrlTreeModal.tsx)
- [frontend/src/components/VideoContentModal.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/VideoContentModal.tsx)
- [frontend/src/components/agent-nodes/ChatAINode.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/agent-nodes/ChatAINode.tsx)
- [frontend/src/components/agent-nodes/EndNode.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/agent-nodes/EndNode.tsx)
- [frontend/src/components/agent-nodes/IfElseNode.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/agent-nodes/IfElseNode.tsx)
- [frontend/src/components/agent-nodes/IntentRecognitionNode.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/agent-nodes/IntentRecognitionNode.tsx)
- [frontend/src/components/agent-nodes/LoopBackNode.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/agent-nodes/LoopBackNode.tsx)
- [frontend/src/components/agent-nodes/NodeConfigPanel.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/agent-nodes/NodeConfigPanel.tsx)
- [frontend/src/components/agent-nodes/PlaceholderNode.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/agent-nodes/PlaceholderNode.tsx)
- [frontend/src/components/agent-nodes/SendMessageNode.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/agent-nodes/SendMessageNode.tsx)
- [frontend/src/components/agent-nodes/StartNode.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/agent-nodes/StartNode.tsx)
- [frontend/src/components/agent-nodes/WaitForReplyNode.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/agent-nodes/WaitForReplyNode.tsx)
- [frontend/src/components/edges/AddNodeEdge.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/edges/AddNodeEdge.tsx)
- [frontend/src/components/edges/LoopBackEdge.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/edges/LoopBackEdge.tsx)
- [frontend/src/components/ui/Badge.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ui/Badge.tsx)
- [frontend/src/components/ui/Button.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ui/Button.tsx)
- [frontend/src/components/ui/CircularProgress.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ui/CircularProgress.tsx)
- [frontend/src/components/ui/ConfirmModal.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ui/ConfirmModal.tsx)
- [frontend/src/components/ui/IconButton.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ui/IconButton.tsx)
- [frontend/src/components/ui/Input.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ui/Input.tsx)
- [frontend/src/components/ui/Pagination.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ui/Pagination.tsx)
- [frontend/src/components/ui/PieChart.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ui/PieChart.tsx)
- [frontend/src/components/ui/ProgressBar.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ui/ProgressBar.tsx)
- [frontend/src/components/ui/Spinner.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/components/ui/Spinner.tsx)
- [frontend/src/index.tsx](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/index.tsx)
- [frontend/src/react-app-env.d.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/react-app-env.d.ts)
- [frontend/src/reportWebVitals.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/reportWebVitals.ts)
- [frontend/src/services/agentService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/services/agentService.ts)
- [frontend/src/services/api.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/services/api.ts)
- [frontend/src/services/authService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/services/authService.ts)
- [frontend/src/services/chatAIService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/services/chatAIService.ts)
- [frontend/src/services/connectorService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/services/connectorService.ts)
- [frontend/src/services/knowledgeBaseService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/services/knowledgeBaseService.ts)
- [frontend/src/services/urlTreeService.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/services/urlTreeService.ts)
- [frontend/src/setupTests.ts](https://github.com/asdkazmi/woiceai/blob/8c3dbaf/web/frontend/src/setupTests.ts)

### chat

- [chat-service/Dockerfile](https://github.com/asdkazmi/woiceai/blob/main/chat-service/Dockerfile)
- [chat-service/requirements.txt](https://github.com/asdkazmi/woiceai/blob/main/chat-service/requirements.txt)
- [chat-service/src/handler.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/handler.py)
- [chat-service/src/modules/applygemfilter.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/applygemfilter.py)
- [chat-service/src/modules/bge.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/bge.py)
- [chat-service/src/modules/fetch_custom_db.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/fetch_custom_db.py)
- [chat-service/src/modules/generate_prompt.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/generate_prompt.py)
- [chat-service/src/modules/llama.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/llama.py)
- [chat-service/src/modules/llama_gemfilter/gem_filter_utils.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/llama_gemfilter/gem_filter_utils.py)
- [chat-service/src/modules/llama_gemfilter/llama_select_attention.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/llama_gemfilter/llama_select_attention.py)
- [chat-service/src/modules/llama_gemfilter/load_model.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/llama_gemfilter/load_model.py)
- [chat-service/src/modules/llama_gemfilter/my_generation.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/llama_gemfilter/my_generation.py)
- [chat-service/src/modules/response.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/response.py)
- [chat-service/src/modules/rewrite_query.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/rewrite_query.py)
- [chat-service/src/modules/stella.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/stella.py)
- [chat-service/src/modules/vector.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/modules/vector.py)

### kb

- [indexer/Dockerfile](https://github.com/asdkazmi/woiceai/blob/main/indexer/Dockerfile)
- [indexer/app.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/app.py)
- [indexer/requirements.txt](https://github.com/asdkazmi/woiceai/blob/main/indexer/requirements.txt)
- `indexer/src/handler.py`
- [indexer/src/modules/chunks.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/src/modules/chunks.py)
- [indexer/src/modules/credits.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/src/modules/credits.py)
- [indexer/src/modules/custom_mongodb_pipeline.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/src/modules/custom_mongodb_pipeline.py)
- [indexer/src/modules/embeddings.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/src/modules/embeddings.py)
- [indexer/src/modules/mongo.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/src/modules/mongo.py)
- [indexer/src/modules/reading.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/src/modules/reading.py)
- [indexer/src/modules/s3download.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/src/modules/s3download.py)
- `indexer/src/modules/sns.py`

### scrapper

- [scraper/Dockerfile](https://github.com/asdkazmi/woiceai/blob/main/scraper/Dockerfile)
- [scraper/app.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/app.py)
- [scraper/requirements.txt](https://github.com/asdkazmi/woiceai/blob/main/scraper/requirements.txt)
- [scraper/src/handler.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/handler.py)
- [scraper/src/modules/chunks.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/modules/chunks.py)
- [scraper/src/modules/credits.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/modules/credits.py)
- [scraper/src/modules/custom_mongodb_handling.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/modules/custom_mongodb_handling.py)
- [scraper/src/modules/detectCaptcha.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/modules/detectCaptcha.py)
- [scraper/src/modules/embeddings.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/modules/embeddings.py)
- [scraper/src/modules/filtering_urls.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/modules/filtering_urls.py)
- [scraper/src/modules/mongo.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/modules/mongo.py)
- [scraper/src/modules/seleniumCode.py](https://github.com/asdkazmi/woiceai/blob/main/scraper/src/modules/seleniumCode.py)
- `scraper/src/modules/sns.py`

### transcriber

- [Dockerfile](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/Dockerfile)
- [requirements.txt](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/requirements.txt)
- [src/app.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/app.py)
- [src/flask_app.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/flask_app.py)
- [src/models.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/models.py)
- [src/modules/chunks.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/modules/chunks.py)
- [src/modules/converting_to_wav.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/modules/converting_to_wav.py)
- [src/modules/credits.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/modules/credits.py)
- [src/modules/custom_mongodb_handling.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/modules/custom_mongodb_handling.py)
- [src/modules/embeddings.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/modules/embeddings.py)
- [src/modules/mongo.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/modules/mongo.py)
- [src/modules/s3download.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/modules/s3download.py)
- [src/modules/sns.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/modules/sns.py)
- [src/transcriber.py](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/src/transcriber.py)

### vision

- [Dockerfile](https://github.com/asdkazmi/woiceai/blob/main/vision-service/Dockerfile)
- [requirements.txt](https://github.com/asdkazmi/woiceai/blob/main/vision-service/requirements.txt)
- [src/app.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/app.py)
- [src/modules/chunks.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/chunks.py)
- [src/modules/credits.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/credits.py)
- [src/modules/custom_mongodb_handling.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/custom_mongodb_handling.py)
- [src/modules/embeddings.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/embeddings.py)
- [src/modules/llama.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/llama.py)
- [src/modules/models.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/models.py)
- [src/modules/mongo.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/mongo.py)
- [src/modules/process_image.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/process_image.py)
- [src/modules/process_video.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/process_video.py)
- [src/modules/s3download.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/s3download.py)
- [src/modules/sns.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/sns.py)
- [src/modules/transcribing_video.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/transcribing_video.py)
- [src/modules/video_to_image_frames.py](https://github.com/asdkazmi/woiceai/blob/main/vision-service/src/modules/video_to_image_frames.py)

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
