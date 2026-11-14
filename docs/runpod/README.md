---
layout: default
title: "RunPod serverless services"
---

# RunPod serverless services

## Worker endpoints

| Service | Worker entrypoint | Build context |
| --- | --- | --- |
| Chat, retrieval and embeddings | `python3 -u /handler.py` | `chat-service/` |
| Audio transcription/indexing | `python3 -u /app.py` | `audio-transcriber/` |
| Explain vision/indexing | `python3 -u /app.py` | `vision-service/` |

Use `https://api.runpod.ai/v2/YOUR_ENDPOINT_ID` as the base URL for each endpoint you create. Send the API key in the `Authorization: Bearer RUNPOD_API_KEY` header and wrap the job payload in `{"input": ...}`.

## Deploy an existing image

1. Open/create the matching serverless endpoint. Select the worker container image and registry credentials if private.
2. Select the image you built and tagged for that worker. See the build instructions below.
3. Choose a CUDA-capable GPU with enough measured VRAM for the loaded models. Chat loads Stella, a GGUF generator and a GPTQ filter model together; vision loads a 7B visual model plus ASR. No exact GPU size is verified by the repository.
4. Inject variables using RunPod secrets and the [templates](../../templates/README.md). Point every media worker's `RUNPOD_BASE_URL` at chat, not at itself.
5. Configure model download/cache persistence under `/runpod-volume` where appropriate; these Docker environment paths do not prove a network volume is attached.
6. Allow startup/download time; inspect logs until all models load. Test on an idle endpoint to measure cold-start behavior and select minimum workers/scaling accordingly.
7. Submit the acceptance payloads, inspect job status and application output, then test the complete web/SNS flow.

Inject the chat worker’s MongoDB Atlas connection string through the `DB_URI` runtime secret.

## Rebuild chat

Restore these build-context artifacts before `docker build`:

- `merged-q4_k_m-model.gguf` — Qwen GGUF for answer generation and query rewriting. Download a compatible variant and rename it to the expected filename, or update both the Dockerfile COPY and the handler path. [Qwen3-14B GGUF](https://huggingface.co/unsloth/Qwen3-14B-GGUF)
- `Meta-Llama-3.1-8B-Instruct-gptq/` — Local model directory for GemFilter context selection. [Llama 3.1 GPTQ](https://huggingface.co/shuyuej/Meta-Llama-3.1-8B-Instruct-GPTQ)
- Stella model files are downloaded by the Dockerfile; verify all tokenizer/config/dense-projection files and weight files are present. `HF_HUB_OFFLINE=1` prevents a missing artifact being fetched at runtime.

Use `chat-service/Dockerfile`. See [Chat and models](../chat/README.md) for GemFilter. Create an empty `.env` to satisfy the historical COPY instruction, then inject real configuration at runtime.

```bash
# From chat-service, AFTER restoring the model artifacts:
touch .env
docker buildx build --platform linux/amd64 --load -t YOUR_REGISTRY/woiceai-chat:YOUR_RELEASE .
docker push YOUR_REGISTRY/woiceai-chat:YOUR_RELEASE
```

## Rebuild transcriber

The Dockerfile installs FFmpeg/libsndfile, NeMo 1.23.0, downloads Parakeet ASR plus pyannote gated assets, and also downloads FastPitch/HiFi-GAN assets that are not active ASR requirements in `models.py`. Its build argument is `HUGGINGFACE_TOKEN`; the supplied runtime template's `HF_TOKEN` is not a replacement for that build argument. Obtain model access before building.

The historical Dockerfile places an HF token in authenticated Git clone URLs through a build ARG. For a publishable new image, change this to a BuildKit secret mount or pre-download model files in a controlled build step, copy only model artifacts, and remove Git remotes/credential-bearing metadata. Do not build/push with a real token using the historical pattern.

Build from `audio-transcriber/` with an empty runtime credential environment. After securing the download step, build/tag/push a release image and deploy it to the transcription endpoint. Validate diarization separately from normal ASR.

## Rebuild explain vision

Build from `vision-service/`. It downloads `Qwen/Qwen2.5-VL-7B-Instruct` and `distil-whisper/distil-large-v3`; loads flash-attention with bfloat16 visual inference; and needs FFmpeg/libsndfile. Create an empty `.env` for the historical COPY line, build/tag/push, inject runtime variables and deploy.

All GPU Dockerfiles contain two FROM statements; the final image starts from `python:3.11-slim`, then manually installs an Ubuntu CUDA repository. The initial NVIDIA FROM is not the final inherited runtime. This mixed-distribution recipe may need repair for a new build. Preserve known working image digests; test CUDA, torch, flash-attn and model loading together before release.

## Job handling

`/run` returns an asynchronous job ID; inspect `/status/JOB_ID` until complete. `/runsync` can return a queued/in-progress state. Python helper modules poll every two seconds and can cancel after their threshold. Their sync path and polling fallback do not consistently return the same tuple shape; test cold starts explicitly before treating a rebuild as compatible. The web RunPod client uses `/runsync` but has no general status-polling fallback in that client.

A RunPod job status COMPLETED only means the handler returned; inspect its application-level `KNOWLEDGEBASE.STATUS` too. Media handlers can return a Failed payload. Avoid duplicate retries while a previous job is still indexing.

<span class="source-label">Sources:</span> [chat-service/Dockerfile](https://github.com/asdkazmi/woiceai/blob/main/chat-service/Dockerfile) [chat-service/src/handler.py](https://github.com/asdkazmi/woiceai/blob/main/chat-service/src/handler.py) [audio-transcriber/Dockerfile](https://github.com/asdkazmi/woiceai/blob/main/audio-transcriber/Dockerfile) [vision-service/Dockerfile](https://github.com/asdkazmi/woiceai/blob/main/vision-service/Dockerfile) [indexer/src/modules/embeddings.py](https://github.com/asdkazmi/woiceai/blob/main/indexer/src/modules/embeddings.py)
{: .source-links }

## Build and publish a media image

After applying the transcriber secret-download change described above (or supplying already downloaded model artifacts through a reviewed Dockerfile), use the same release procedure for each media service directory:

```bash
# Run from `audio-transcriber/` using its reviewed Dockerfile:
docker buildx build --platform linux/amd64 --load -t YOUR_REGISTRY/audio-transcriber:YOUR_RELEASE .
docker push YOUR_REGISTRY/audio-transcriber:YOUR_RELEASE
# Run separately from `vision-service/`:
touch .env
docker buildx build --platform linux/amd64 --load -t YOUR_REGISTRY/vision-service:YOUR_RELEASE .
docker push YOUR_REGISTRY/vision-service:YOUR_RELEASE
```

The transcriber command assumes you removed the historical token ARG clone steps or replaced them with a secret-mount flow; it is not a claim that the unmodified Dockerfile builds without gated-model credentials. On each endpoint, change the image to the new release, keep the appropriate handler CMD, bind variables and wait for a healthy worker before sending production work.

Current API request conventions: [RunPod documentation](https://docs.runpod.io/serverless/endpoints/send-requests). Lambda container deployment requirements: [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html).
