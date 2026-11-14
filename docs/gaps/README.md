---
layout: default
title: "Recovery questions and remaining evidence gaps"
---

# Recovery questions and remaining evidence gaps

Use the [installation guide](../setup/README.md) to deploy from the consolidated repository. The items below are specific to the deployment environment.

| Missing record | Why it matters | How to recover |
| --- | --- | --- |
| Exact GGUF download/conversion recipe/checksum | Rebuild of deployed chat generator | Original model build folder or preserved container artifact; record provenance |
| Chat image digest and matching source commit | Tag alone does not establish exact code/model build | Container registry and original release notes |
| Runtime source of chat DB_URI | Public handler reads the Atlas URI from the runtime environment | Inspect image/config privately, export only variable names; move to runtime secret |
| Transcriber/vision image tags/digests | Exact working media deployments | Read endpoint image settings |
| GPU type, worker min/max, concurrency, startup/job timeout, disk/volume | Capacity/cold starts and compatibility | Export redacted RunPod endpoint settings |
| KB/scraper function names, image URIs/digests, limits/VPC | Exact AWS deployment | Read-only Lambda/ECR configuration export |
| SNS subscriptions/policies/DLQ/delivery config | Reconstruct routing and callback delivery | Read-only SNS configuration export |
| Actual Atlas index definition and deployed embedding dimension | Avoid retrieval/index mismatch | Export index JSON and probe known model embedding |
| SQL schema/release state | Confirm startup migrations match production | Redacted schema-only export and migration review |
| Web domains/hosting/proxy/runtime process config | Production deployment instructions for original host | Export redacted hosting/service configuration |
| Provider key bridge / compatibility Lambda use | Current web writes SQL but provider worker reads Atlas | Identify missing sync code or document disabled provider paths |
| Semantic intent implementation if present in deployed app | Public executor is a TODO | Identify deployed revision or separate classifier service |
| Scheduled re-crawl/refresh jobs, if any | No scheduler definition in public source | Export schedule target/payload and handler source |

Do not provide actual API keys, passwords, full secret URIs, tokens, or unredacted `.env` files. Resource names, variable names, image digests, model IDs, index definitions and redacted settings are sufficient.

## Review scope

The [source map](../sources/README.md) lists the deployment folders. Configuration templates use installation-specific placeholders.
