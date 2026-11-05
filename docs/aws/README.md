---
layout: default
title: "AWS: Lambda, ECR, S3 and SNS"
---

# AWS: Lambda, ECR, S3 and SNS

[Documentation home](../../README.md)

## Deployment units

| Unit | Branch / build context | Container command | Trigger |
| --- | --- | --- | --- |
| KB router/indexer | `dev-woiceai-kb` / `woice_kb/` | `handler.lambda_handler` | SNS input topic |
| Website scraper | `dev-scrapper` / `scrapper/` | `handler.scrapper` | Synchronous invoke from KB Lambda |
| Optional provider chat | `dev-woiceai-chat` / `woice_chat/` | `handler.lambda_handler` | Direct API invoke, including key validation |

The actual KB and scraper Lambda function names and ECR repositories/tags were not supplied. `SCRAPPER_LAMBDA_ARN` binds them. The web hardcodes the compatibility chat ARN ending in `function:devWoiceChat`. Do not invent an ECR tag from a Lambda name.

The KB Dockerfile uses Lambda Python 3.9; the scraper uses an old Python 3.6 Lambda base and old Chromium/Chromedriver downloads. These are historical recipes, not a verified modern rebuild. Preserve a known working image digest if available. A rebuild may require a supported Lambda runtime, matching Chromium/driver, updated binary libraries and regression tests. Changing only the base version is insufficient.

## ECR build/push procedure

Recommended shell outline; run from one service's build context, with AWS CLI authenticated and the target account selected. Names below are chosen for a new installation, not verified live names.

```bash
export AWS_REGION=us-east-1
export AWS_ACCOUNT_ID=YOUR_ACCOUNT_ID
export ECR_REPOSITORY=woiceai-kb
export IMAGE_TAG=YOUR_RELEASE_TAG
export ECR_REGISTRY="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"
aws ecr create-repository --repository-name "$ECR_REPOSITORY" --region "$AWS_REGION"
aws ecr get-login-password --region "$AWS_REGION" | docker login --username AWS --password-stdin "$ECR_REGISTRY"
# Dockerfiles currently COPY .env. Supply an EMPTY .env, never a real credential file.
touch .env
docker buildx build --platform linux/amd64 --provenance=false --load -t "$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG" .
docker push "$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG"
```

Skip repository creation if it already exists. Build separate images for KB and scraper. Deploy x86_64 functions for these historical x86 browser binaries. Validate architecture rather than building an Apple Silicon default image. ECR and the Lambda function must be in the appropriate deployment region. Select the image URI/digest when creating a container-image Lambda, attach the execution role, then inject [Python variables](../configuration/README.md).

A Lambda function does not automatically redeploy when an existing ECR tag is pushed again. Update function code to the new image and wait for the update to complete. Prefer immutable release tags/digests:

```bash
aws lambda update-function-code --function-name YOUR_FUNCTION --image-uri YOUR_IMAGE_URI
aws lambda wait function-updated --function-name YOUR_FUNCTION
```

Record timeout, memory, ephemeral storage, architecture, concurrency, VPC/subnets, security groups, image digest and environment variable names. None are established by source alone. Choose limits from representative file/media and crawl tests. Lambda's finite execution window constrains deep synchronous crawls and polling for cold GPU workers.

## IAM and networking

Recommended permission boundaries:

| Principal | Needed access |
| --- | --- |
| Web API | S3 Put/Get/Delete on its bucket prefix; SNS Publish to input topic; optional InvokeFunction on provider chat |
| KB Lambda | S3 Get on originals; Publish update topic; InvokeFunction on scraper; CloudWatch logging |
| Scraper Lambda | Publish update topic; logging; outbound HTTPS to crawled pages, RunPod, MongoDB Atlas |
| RunPod media workers | S3 Get on originals and Publish update topic using dedicated AWS credentials; Atlas and RunPod access |
| SNS input topic | Permission to invoke only KB Lambda |
| Deployment identity | ECR push and controlled Lambda configuration/image updates |

Atlas must allow the workers' network access. Lambda VPC placement without internet/NAT can break RunPod, websites, Atlas DNS, or S3/public endpoints. Configure these dependencies deliberately. The existing AWS SDK clients may explicitly pass static keys; attaching a role alone does not guarantee that every code path uses it. See configuration caveats.

## Input SNS topic

Create `woice-ai-knowledgebase` (or replace the hardcoded web topic ARN). Subscribe **KB Lambda** with protocol Lambda, and add its resource-based permission allowing `sns.amazonaws.com` with SourceArn restricted to that topic. The scraper is invoked by the KB function; it does not need a separate input-topic subscription for the main flow.

Input attributes are the routing contract: `KNOWLEDGEBASE.ID`, `.CONTENT`, `.CONTENT_TYPE`, `.ACTION`, optional `.TEXT`, `.TITLE`, `.URL_DEPTH`, `.UNIQUE_ID`, and worker-side optional `.MONGODB_SRV_ID`. Use native SNS delivery with its `Records[0].Sns.MessageAttributes` envelope. These handlers process only the first record in the inspected implementation.

## Update SNS topic and HTTPS callback

Create `lambda-indexing-update-events`. Configure worker publishers and subscribe `https://YOUR_API_HOST/knowledgebase/webhook` using HTTPS. The API also exposes `/api/webhook/webhook`, `/api/webhook/sns` and `/knowledgebase/sns` through its two router mounts. Use the first canonical path consistently.

The callback handles `SubscriptionConfirmation` by fetching SubscribeURL and handles `Notification` by reading MessageAttributes. Allow SNS's `text/plain` JSON envelope through the proxy. Use standard SNS delivery, not raw message delivery, since the handler needs envelope attributes. Confirm that the subscription is no longer pending before testing indexing.

**Required hardening for an untrusted public deployment:** the inspected webhook accepts SNS-shaped traffic without verifying its signature/topic and fetches a submitted confirmation URL. Add SNS signature/certificate validation, expected-topic checks and safe AWS confirmation-URL validation before relying on this route publicly. This is a concrete property of the supplied handler, not an extra existing service.

Recommended operations: configure SNS delivery monitoring and a failure destination/DLQ where supported by the chosen subscription/Lambda setup. Capture both Lambda invocation errors and application-level Failed attributes: returning a Failed dictionary may still count as a successful Lambda invocation.

## Optional provider Lambda

If the web offers non-Qwen models, build the compatibility service from its own branch, supply its `DB_URI`, RunPod embedding/rewrite configuration, and MongoDB `keys` records. It expects provider keys by `api_key_id`. Recover/test the SQL-to-Mongo key bridge before enabling this path. This does not replace the active chat-all-models RunPod deployment.

Sources: [woice_kb/Dockerfile](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/Dockerfile), [scrapper/Dockerfile](https://github.com/asdkazmi/woiceai-ai/blob/058a3ed1a16ec39d12ea7c6ddba43951049cf1c5/scrapper/Dockerfile), [woice_kb/src/handler.py](https://github.com/asdkazmi/woiceai-ai/blob/0e81e4185613358646292ccb5e0fdcbca639febf/woice_kb/src/handler.py), [backend/src/routes/webhook.ts](https://github.com/asdkazmi/woiceai-web/blob/8520c824ad0bf2ae9ad403fdca358757c1be98ae/backend/src/routes/webhook.ts), [woice_chat/src/handler.py](https://github.com/asdkazmi/woiceai-ai/blob/fbf49ca55d83a8020242ba251939b501606dbef5/woice_chat/src/handler.py).
