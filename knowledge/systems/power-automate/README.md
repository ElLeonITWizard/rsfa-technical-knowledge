---
id: SYS-PA-001-DOC
title: Power Automate — System Documentation
status: active
owner: RSFA
last_modified: 2026-07-30
last_verified: 2026-07-30
---

# Power Automate — System Documentation

## 1. Role in RSFA

Power Automate is RSFA's Microsoft-centric automation platform, retained primarily for Outlook email filing, SharePoint client-folder lifecycle management, and DocuSign document filing. See `knowledge/02_SYSTEMS_REGISTRY.md` `SYS-PA-001` for the canonical status/criticality entry, and `knowledge/01_RSFA_SYSTEM_MAP.md` §4.2 for its place in the broader automation architecture (Power Automate is `Active - Reducing` — Make.com is preferred for new non-Microsoft work).

## 2. Where to look for what

| Question | Where to look |
|---|---|
| Is this automation active, and what's its business purpose? | `knowledge/automations/power-automate/` — the canonical automation document |
| Which Solution package contains this flow, and what does the package actually contain? | `exports/power-automate/solution-inventory.md`, then the Solution's `manifest.md` |
| What are the exact flow names, workflow IDs, connection references and states last seen in an export? | `exports/power-automate/solutions/<solution>/manifest.md` |
| What Power Automate flows exist across all RSFA automations, and what's their current registry status? | `knowledge/03_AUTOMATION_REGISTRY.md` §5 |
| What environments exist? | `environments.md` (this folder) |
| What connectors/connection references are in use, and where? | `connection-references.md` (this folder) |
| What does a Solution mean for RSFA, and what are the export/versioning rules? | `solutions.md` (this folder) |

## 3. Relationship to other documentation

- `knowledge/02_SYSTEMS_REGISTRY.md` — `SYS-PA-001` entry: platform-level status, criticality, ownership.
- `knowledge/03_AUTOMATION_REGISTRY.md` §5 and the "Power Automate Solution mapping" section — the canonical flow inventory and its mapping to Solution exports.
- `knowledge/automations/power-automate/*.md` — one canonical document per business automation (`AUTO-EMAIL-001`, `AUTO-DOCUSIGN-001`, `AUTO-SP-FOLDER-001`, `AUTO-EMAIL-BACKUP-001`, `AUTO-MONDAY-BACKUP-001`).
- `exports/power-automate/` — point-in-time Solution export evidence: manifests, checksums, unpacked package contents.
- `source-material/power-automate/` — earlier walkthrough notes for individual flows, treated as historical/partial evidence per each automation document's source references.

## 4. Evidence hierarchy for Power Automate questions

```text
Current live-system evidence (Power Automate portal, run history)
→ latest inspected Solution export (exports/power-automate/solutions/<solution>/manifest.md)
→ canonical automation documentation (knowledge/automations/power-automate/)
→ historical/source-material documentation (source-material/power-automate/)
→ inference
```

If an export contradicts the canonical documentation (a different flow name, a different state, a flow present in one but not the other), do not silently resolve it — record the conflict, state which source appears more current, and specify what live verification is required. See `CLAUDE.md` § "Power Automate Solution exports" for the full rule.

## 5. Known gaps

- No PAC CLI environment was available when the current export set was inspected — package inspection used standard ZIP extraction only.
- Exact live environment(s) these Solutions are deployed to are not confirmed from the exports themselves (see `environments.md`).
- Connection reference **owners** are not recorded in any current export (unmanaged exports do not carry this).
- Several flows in the current export set are unmapped against the Automation Registry, or mapped only by close-but-inexact name — see `exports/power-automate/solution-inventory.md` for the full list.
