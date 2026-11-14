---
layout: default
title: "Deploy React and Express"
---

# Deploy React and Express

The React frontend and Express API live under `web/`. Follow [web/README.md](https://github.com/asdkazmi/woiceai/blob/main/web/README.md) for service-specific commands.

## What to deploy

| Directory | Artifact | Runtime |
| --- | --- | --- |
| `frontend` | `npm run build` → `build/` | Static HTTPS host with SPA fallback to index.html |
| `backend` | `npm run build` → `dist/` plus production dependencies | Node.js persistent process, entrypoint `dist/index.js` |

The repository README requests Node 20.15.1+ and MySQL 8+. React in the actual package manifest is 19.2.3, not the older React 18 description. Select a supported Node release compatible with these dependencies and verify both builds. Package locks are not present in these snapshots; `npm install` can resolve newer compatible dependency versions. Commit a tested lockfile for reproducible releases.

## Local setup

```bash
cd web/backend
npm install
# Copy templates/web-backend.env.example from this documentation to backend/.env.
# Fill the values locally using your secret store.
npm run dev
```

In another terminal:

```bash
cd web/frontend
npm install
# Create .env with REACT_APP_API_URL=http://localhost:5000/api
npm start
```

Default URLs: frontend `http://localhost:3000`; API `http://localhost:5000/api`; liveness `http://localhost:5000/api/health`. MongoDB Atlas is required for the full project even though API startup treats its connection as optional.

The backend calls database creation, table-creation/alter migrations and connector seeding on startup. Grant the initialization account the required DDL permissions. Review these migrations and back up existing data before starting a new version. There is no standalone `npm run migrate` in the checked-in package. Do not substitute Laravel migration commands.

## Production hosting (recommended procedure)

1. Provision an API host/container platform supporting persistent Node processes and public HTTPS callbacks. No production web host or domain is established by the repository.
2. Install/build the backend, inject backend variables at process startup, then run `npm start` from `backend`. Put a service manager/container orchestrator in charge of restarts and logs. Do not use `nodemon` as a production process manager.
3. Set `NODE_ENV=production`, `PORT`, unique `JWT_SECRET` and `SESSION_SECRET`, database credentials, AWS/RunPod configuration, and `CORS_ORIGINS` to the exact frontend origin(s).
4. Set `FRONTEND_URL` for OAuth redirects and `BACKEND_URL`/`GOOGLE_CALLBACK_URL` for the API origin. `FRONTEND_URL` does not control actual CORS in `index.ts`; `CORS_ORIGINS` does.
5. Build the frontend with `REACT_APP_API_URL=https://YOUR_API_HOST/api`. This value is embedded at build time; changing the runtime environment of an already built static site does not change it.
6. Deploy `frontend/build/` to static hosting. Enable SPA history fallback. Serve API and SNS callback paths through the API host, not the static fallback.
7. Match proxy upload/time limits to the API's 100 MB upload setting and model latency. `/runsync` can incur cold-start delay; size timeouts using measured behavior rather than assuming ordinary short web requests.
8. Verify table initialization, login, real DB queries, RunPod access, S3 upload and SNS callback completion before switching traffic.

The API serves JSON; it does not contain a checked-in production static-file server for the React build. It stores OAuth sessions using the default express-session store. For multi-instance/production social login, plan a shared production session store and appropriate secure cookie/proxy settings; these are deployment/code additions, not provided services.

## Authentication

Password registration/login issue JWTs. Protected API routes expect `Authorization: Bearer <token>`. Google login is optional: create a Google OAuth web application, set the callback to `https://YOUR_API_HOST/api/auth/google/callback`, configure authorized origins/redirects, then set `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`. The code conditionally registers the strategy when credentials are available.

No provider/AWS/RunPod credential belongs in `REACT_APP_*`; those values are public browser assets. The backend must use real secrets rather than its fallback defaults. Provider connector keys are stored in SQL by the inspected model; no encryption layer is demonstrated there.

## Existing helper scripts

`start.sh` and `start-ngrok.sh` are development helpers. Ngrok is useful for receiving SNS callbacks locally; after restarting a temporary tunnel, update the SNS subscription URL and confirm it again. It is not the documented production host.

<span class="source-label">Sources:</span> [web/backend/package.json](https://github.com/asdkazmi/woiceai/blob/main/web/backend/package.json) [web/frontend/package.json](https://github.com/asdkazmi/woiceai/blob/main/web/frontend/package.json) [web/backend/src/index.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/index.ts) [web/backend/src/config/googleAuth.ts](https://github.com/asdkazmi/woiceai/blob/main/web/backend/src/config/googleAuth.ts)
{: .source-links }
