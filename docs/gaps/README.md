---
layout: default
title: "Recovery questions and remaining evidence gaps"
---

# Recovery questions and remaining evidence gaps

[Documentation home](../../README.md)

The owner confirmed React + Express as the only web baseline, MongoDB Atlas for vector search, and the GPTQ Llama model source. Those questions are resolved. The documentation can be published now, but an exact production rebuild still requires the following non-secret records.

| Missing record | Why it matters | How to recover |
| --- | --- | --- |
| Exact GGUF download/conversion recipe/checksum | Rebuild of deployed chat generator | Original model build folder or preserved container artifact; record provenance |
| Chat image digest and matching source commit | Tag alone does not establish exact code/model build | Container registry and original release notes |
| Runtime source of chat DB_URI | Public handler reads Atlas URI, endpoint reportedly has no visible vars | Inspect image/config privately, export only variable names; move to runtime secret |
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

All four public repositories and relevant AI service branches were inspected locally. Owner-provided endpoint templates and image information were incorporated. Source-level route/schema/environment inventories were generated. No AWS account inventory, signed-in RunPod configuration audit, live endpoint job, full application build or production end-to-end test was performed. Thus this is complete documentation of the available source and owner-specified topology, with explicit reconstruction gaps, rather than a certification that the current cloud installation is running.
