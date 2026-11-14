---
layout: default
title: "Install the complete project"
---

# Install the complete project

This is a recommended reconstruction order. It is not an automated infrastructure deployment. Resolve the [recovery questions](../gaps/README.md) before promising an exact reproduction of the owner's live environment.

## 1. Obtain the correct source trees

Clone the consolidated repository once. Until the web import merges, check out its integration branch to get all six folders.

```bash
git clone https://github.com/asdkazmi/woiceai.git
cd woiceai
git switch integrate/web
```

Use each service folder as its build context. See [Sources](../sources/README.md) for the directory map.

## 2. Provision shared storage and credentials

1. Create MySQL 8+ and a dedicated application database/account.
2. Create MongoDB Atlas with Vector Search and the `woice-ai-kb` database; create the vector index described in [Data](../data/README.md).
3. Create the private S3 bucket; configure its exact name in web and Python.
4. Create both SNS topics. Create narrowly scoped AWS credentials/roles and a RunPod API key. Obtain model licenses/access and gated Hugging Face access where needed.
5. Fill the supplied [templates](../../templates/README.md) through deployment secret storage. Never put real values in this documentation repository.

## 3. Bring up RunPod chat and embeddings first

Build and deploy the chat image using the model artifacts and runtime configuration described in the [RunPod guide](../runpod/README.md). Verify a small embedding request, then a known-KB chat request. Record image digest, GPU type, volume/cache arrangement, worker counts and startup timeout. Every ingestion worker depends on this endpoint for embeddings.

## 4. Bring up media workers

Deploy transcriber and explain vision. Point both at the same chat/embedding endpoint and MongoDB database. Set S3/AWS credentials and update-topic ARN. Test short media before large files. Record their exact image digests; the owner supplied no media image tags.

## 5. Bring up AWS workers

Build/push scraper and KB images to ECR, create Lambda container functions with the documented handlers, and grant the KB function permission to invoke the scraper. Configure all endpoint URLs and cost settings. Subscribe the KB function to the input SNS topic and grant SNS invoke permission. Do not subscribe every worker indiscriminately; the KB function is the router.

## 6. Bring up Express and React

Follow [Web](../web/README.md). The API initializes SQL tables and seeds connectors on startup. Confirm initialization finished; `/api/health` alone does not test storage or AI dependencies. Configure HTTPS API/frontend origins and OAuth redirects.

## 7. Close the synchronization loop

Subscribe the public HTTPS `/knowledgebase/webhook` endpoint to the update SNS topic; complete subscription confirmation. Validate publisher authenticity before exposing this route to untrusted traffic (see [AWS](../aws/README.md)). Check one real indexing completion appears in MySQL and the UI.

## 8. Optional provider connectors

If enabling non-Qwen connectors, restore/test the compatibility Lambda and its MongoDB key lookup. The public web code stores connector keys in SQL while that Lambda expects MongoDB `keys`; no bridge is established in the inspected web code. Recover the original bridge or implement and test one before claiming these connectors work.

## 9. Run acceptance tests and record the release

Use the [operations checklist](../operations/README.md). Save source SHAs, image digests, resource names, endpoint settings, vector index definition, redacted variable names, and test results in a private deployment record. Public documentation should contain templates and portable procedures.
