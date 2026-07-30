---
id: SYS-PA-001-ENVIRONMENTS
title: Power Automate — Environments
status: active
owner: RSFA
last_modified: 2026-07-30
last_verified: 2026-07-30
---

# Power Automate — Environments

## 1. Confirmed environments

| Environment | Environment ID | Access URL | Source |
|---|---|---|---|
| Default | `Default-df3cc44d-5e4a-4b7e-a22f-b90a4d6ab53d` | https://make.powerautomate.com/environments/Default-df3cc44d-5e4a-4b7e-a22f-b90a4d6ab53d/home | Confirmed from documentation — `knowledge/02_SYSTEMS_REGISTRY.md` `SYS-PA-001` |

This is the only Power Automate environment currently documented anywhere in this repository. Whether RSFA operates additional environments (e.g. a separate Dev/Test environment) is `Unknown — verify`.

## 2. Environment(s) of origin for exported Solutions

`Unknown — verify` for all four Solutions currently under `exports/power-automate/solutions/`.

None of the four Solution exports (`DocuSigntoSharePoint`, `RSFAOutlookEmailFilling`, `SPAdviserNameChange`, `SPClientFolderCreationandRenaming`) carry embedded environment metadata identifying which environment they were exported from. Per the rule governing this document: **do not infer the source environment of a Solution export solely from the ZIP contents.** Each Solution's manifest records `source_environment: Unknown — verify` accordingly.

Given that only one environment (`Default`) is currently documented for RSFA at all, it is plausible these exports came from it — but plausibility is not confirmation, and this document does not assert it as fact.

## 3. Rules

- Do not invent an environment name, ID or URL not already documented here or in `knowledge/02_SYSTEMS_REGISTRY.md`.
- Do not infer a Solution's environment of origin from its ZIP filename, version number, or export date.
- When a live check confirms a Solution's environment, update the relevant manifest's `source_environment` field and this document together.

## 4. Known gaps

- Whether RSFA operates more than one Power Automate environment is unconfirmed.
- The environment of origin for all four currently-exported Solutions is unconfirmed.
