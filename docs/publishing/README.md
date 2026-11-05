---
layout: default
title: "Publish on GitHub and GitHub Pages"
---

# Publish on GitHub and GitHub Pages

[Documentation home](../../README.md)

## Put these files on a new main branch

Copy the **contents** of `woiceai-documentation/` into the repository you intend to publish. They are independent of the inspected application repositories. Preserve the relative folder layout. Review the source pins/recovery gaps, add your license if appropriate, then commit and push using your usual Git workflow. No remote branch was created or changed during documentation preparation.

GitHub renders the root README and each directory README directly. The optional `_config.yml` and `index.md` also prepare the same content for GitHub Pages using Jekyll and relative-link rewriting; there is no separate JavaScript docs app to maintain.

## Optional GitHub Pages

1. For the exact URL `https://woiceai.github.io/`, the GitHub account/organization must be **woiceai**, and the repository must be **woiceai.github.io**. A repository under asdkazmi cannot claim another account's Pages hostname. Under that account, `asdkazmi.github.io` is its user-site name; other repositories normally use a project path.
2. Copy this documentation set to the chosen repository's main branch.
3. In repository Settings → Pages choose **Deploy from a branch**, branch main, folder `/ (root)`.
4. In `_config.yml`, set `url` to your actual site origin. Keep `baseurl: ""` for a user/organization site; set `/YOUR_REPOSITORY_NAME` for a project site.
5. Wait for the Pages build, then verify the home page, every guide link and downloadable examples. GitHub access and account ownership remain prerequisites; no site has been published by this task.

The `jekyll-relative-links` plugin rewrites Markdown links for the Pages build while preserving Markdown-first navigation on GitHub. Mermaid blocks render natively on GitHub; the supplied Pages layout loads Mermaid for diagrams. The Pages layout uses GitHub's Cayman theme. If your hosting policy disallows a public CDN, vendor the Mermaid asset or omit diagram enhancement.

A local Jekyll build can be performed in a GitHub Pages-compatible Ruby environment using the supplied Gemfile:

```bash
bundle install
bundle exec jekyll build
bundle exec jekyll serve
```

Review and commit a dependency lock after validating the selected Pages dependency versions. The documentation preparation checks links and payloads but does not claim a local Ruby/Jekyll build was executed.
