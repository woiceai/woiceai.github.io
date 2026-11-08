---
layout: default
title: "Documentation validation"
---

# Documentation validation

Reviewed November 5, 2026.

- 202 unique pinned source-file targets were checked against the downloaded repository snapshots.
- Relative Markdown links were checked for existing targets.
- Six JSON payload examples were parsed.
- Markdown code fences were checked for balance.
- A basic scan found no AWS access-key, Hugging Face token, GitHub token or private-key patterns.
- The source review used all four repositories and the relevant AI branches; no application code was modified.

Re-run portable checks with `python3 scripts/validate_docs.py` from this folder. Pattern scanning cannot prove that every possible credential is absent; all supplied values were reviewed as placeholders or non-secret installation identifiers.

No live cloud deployment, endpoint inference, application build, or local Ruby/Jekyll build was performed. GitHub Pages publishing assets are supplied for the destination repository to build. Outstanding live-configuration and model-artifact records are listed in docs/gaps/README.md.
