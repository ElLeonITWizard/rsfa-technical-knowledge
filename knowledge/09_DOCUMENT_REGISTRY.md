---
id: RSFA-DOCUMENT-REGISTRY
title: RSFA Document Registry
status: active
owner: RSFA
audience:
  - Authorised developers
  - Authorised technical consultants
last_modified: 2026-07-30
last_verified: 2026-07-30
---

# RSFA Document Registry

## 1. Purpose

This document is the master registry of important source documents, exports and system-level documentation referenced elsewhere in this repository. It is one of the four main registry files named in `CLAUDE.md` §12, alongside `02_SYSTEMS_REGISTRY.md`, `03_AUTOMATION_REGISTRY.md` and `04_MONDAY_BOARDS_REGISTRY.md`.

This file was present but empty before 2026-07-30. Its absence of content was noted, not assumed to mean the registry itself did not apply — `CLAUDE.md` §12 and `knowledge/02_SYSTEMS_REGISTRY.md` §8 both already referenced it as an established registry. It is populated here for the first time, starting with the documents created or updated during the 2026-07-30 Power Automate Solution export integration.

## 2. Conventions

Document IDs use the `DOC-` prefix per `knowledge/06_NAMING_AND_ID_CONVENTIONS.md` §3 (e.g. `DOC-PA-EXPORTS-001`). Not every file in the repository needs a registry entry — this registry tracks canonical system/automation documentation, cross-cutting indexes (like a solution inventory), and important source or export documents, not every playbook or template.

## 3. Document registry

| Document ID | File | Type | Status | Last verified |
|---|---|---|---|---|
| `DOC-PA-EXPORTS-001` | `exports/power-automate/README.md` | Export folder guide | Active | 2026-07-30 |
| `DOC-PA-EXPORTS-002` | `exports/power-automate/solution-inventory.md` | Export inventory/index | Active | 2026-07-30 |
| `DOC-PA-EXPORTS-003` | `exports/power-automate/solutions/docusign-to-sharepoint/manifest.md` | Solution export manifest | Active | 2026-07-30 |
| `DOC-PA-EXPORTS-004` | `exports/power-automate/solutions/rsfa-outlook-email-filing/manifest.md` | Solution export manifest | Active | 2026-07-30 |
| `DOC-PA-EXPORTS-005` | `exports/power-automate/solutions/sp-adviser-name-change/manifest.md` | Solution export manifest | Active | 2026-07-30 |
| `DOC-PA-EXPORTS-006` | `exports/power-automate/solutions/sp-client-folder-creation-and-renaming/manifest.md` | Solution export manifest | Active | 2026-07-30 |
| `DOC-PA-SYS-001` | `knowledge/systems/power-automate/README.md` | System documentation | Active | 2026-07-30 |
| `DOC-PA-SYS-002` | `knowledge/systems/power-automate/solutions.md` | System documentation | Active | 2026-07-30 |
| `DOC-PA-SYS-003` | `knowledge/systems/power-automate/environments.md` | System documentation | Active | 2026-07-30 |
| `DOC-PA-SYS-004` | `knowledge/systems/power-automate/connection-references.md` | System documentation | Active | 2026-07-30 |

## 4. Maintenance rule

When creating a new canonical system, automation, board schema or export-evidence document, add it here with a new `DOC-` ID, its file path, its type, and its current status. Update `Last verified` only when the document's content has actually been re-checked against its source, not merely re-read.

## 5. Known gaps

- This registry does not yet cover documents that predate 2026-07-30 (e.g. the individual automation documents under `knowledge/automations/`, the `source-material/power-automate/` walkthroughs, or the system registries themselves). Backfilling those entries is a follow-up task, not performed here since it was out of scope for the Power Automate export integration that created this registry's first entries.
