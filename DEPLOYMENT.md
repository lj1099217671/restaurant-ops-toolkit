# GitHub deployment

This document records the safe publication process. GitHub credentials are
never embedded in this workspace.

## 1. Create the repository

On GitHub, create a public repository named:

```text
restaurant-ops-toolkit
```

Do not initialize it with a README, license, or `.gitignore`; those files already exist locally.

Recommended description:

```text
Vendor-neutral metrics, validation, and data contracts for multi-store restaurant operations.
```

Recommended topics:

```text
restaurant-analytics
restaurant-operations
pos
retail-analytics
china
python
```

## 2. Configure local Git identity

Use your own public maintainer identity:

```powershell
git config --global user.name "YOUR_NAME"
git config --global user.email "YOUR_PUBLIC_OR_NOREPLY_EMAIL"
```

## 3. Initialize and push

From this directory:

```powershell
git init -b main
git add .
git status
git commit -m "Initial public release: restaurant operations metric kernel"
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/restaurant-ops-toolkit.git
git push -u origin main
```

If GitHub CLI is installed and authenticated, repository creation can instead be done with:

```powershell
gh repo create restaurant-ops-toolkit --public --source . --remote origin --push
```

## 4. GitHub settings

After the first push:

1. Enable Issues and Discussions.
2. Add the repository description and topics.
3. Protect `main` after the project has more than one contributor.
4. Require the CI workflow before merge.
5. Add a private security contact.
6. Publish a `v0.1.0` release after CI passes.

## 5. First public evidence

Before applying to maintainer programs, create visible maintenance evidence:

- 5–10 well-scoped issues;
- at least 3 releases over time;
- a public roadmap;
- accepted feedback from real restaurant operators or analysts;
- anonymized impact evidence such as hours saved or error rates reduced;
- regular issue triage and pull-request review.

Do not manufacture stars, downloads, users, or contribution activity.
