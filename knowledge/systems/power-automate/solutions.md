---
id: SYS-PA-001-SOLUTIONS
title: Power Automate — Solutions
status: active
owner: RSFA
last_modified: 2026-07-30
last_verified: 2026-07-30
---

# Power Automate — Solutions

## 1. What a Solution is, in RSFA's context

A Power Automate (Dataverse) Solution is a packaged container for one or more cloud flows, plus their connection references and any other components (custom connectors, environment variables, tables). RSFA uses Solutions as the unit of export/evidence for Power Automate flows — each Solution in the current export set corresponds to a small, related group of flows (usually one business automation, sometimes a component of one).

This document describes Solutions generically. For the current, specific set of exported Solutions, see `exports/power-automate/solution-inventory.md`.

## 2. Summary inventory

As of the 2026-07-30 export set (see `exports/power-automate/solution-inventory.md` for full detail):

| Solution Unique Name | Flows | Primary canonical automation |
|---|---:|---|
| `DocuSigntoSharePoint` | 1 | `AUTO-DOCUSIGN-001` |
| `RSFAOutlookEmailFilling` | 15 | `AUTO-EMAIL-001` (+ `AUTO-EMAIL-BACKUP-001`) |
| `SPAdviserNameChange` | 2 | `AUTO-SP-FOLDER-001` |
| `SPClientFolderCreationandRenaming` | 2 | `AUTO-SP-FOLDER-001` |

This is not necessarily every Solution in the live Power Automate environment — it is only every Solution that has been exported to this repository so far. `TODO: verify` whether other Solutions exist for the remaining Power Automate automations (`AUTO-EMAIL-BACKUP-001`'s `Email Back Up Generator`, `AUTO-MONDAY-BACKUP-001`'s two backup flows) that have not yet been exported.

## 3. Solution → flows → canonical automations

Each Solution maps to canonical automations at the flow level, not necessarily 1:1 at the Solution level — a Solution can contain flows belonging to more than one canonical automation (e.g. `RSFAOutlookEmailFilling` contains flows for both `AUTO-EMAIL-001` and `AUTO-EMAIL-BACKUP-001`), and a canonical automation's flows can be split across more than one Solution (`AUTO-SP-FOLDER-001`'s flows are split across `SPAdviserNameChange` and `SPClientFolderCreationandRenaming`).

Always resolve the mapping at the individual flow level using `exports/power-automate/solution-inventory.md`'s flow-to-solution table — never assume a Solution name implies full coverage of a canonical automation's flows.

## 4. Managed vs. unmanaged

All four Solutions currently exported are **unmanaged** (`Managed: 0` in each `solution.xml`). This is confirmed directly from each export, not inferred. Unmanaged Solutions are typically the "development" form of a Solution in Dataverse/Power Platform; whether these are exported from a dev environment, a single production environment used as the only environment, or something else is `Unknown — verify` for all four (see `environments.md`).

## 5. Export rules

- Export the Solution as **unmanaged** unless a specific reason requires a managed export (not currently the case for any Solution in this repository).
- Read `solution.xml` for the exact `UniqueName`, display name, version and publisher — never derive these from the export filename.
- Read `customizations.xml` for the exact flow names, workflow IDs, states and connection references.
- Treat the export as a point-in-time snapshot of package content — not proof of live deployment state.

## 6. Versioning rules

- Preserve the exact version string from `solution.xml` (e.g. `1.0.0.2`) in the manifest frontmatter.
- Do not renumber or reinterpret the version — if it looks inconsistent with a prior export, flag it as a known gap rather than correcting it.
- When re-exporting, keep the previous `manifest.md` change history intact and append a new entry noting what changed (version bump, new/removed flows, state changes).

## 7. Snapshot rules

- `current/` under each Solution folder means the latest snapshot stored in this Git repository — see `exports/power-automate/README.md`.
- Never treat a Solution export as proof that its flows are currently active in production; cross-check `knowledge/03_AUTOMATION_REGISTRY.md` and, where possible, the live Power Automate environment.

## 8. Current gaps

- Live environment(s) for all four Solutions are unconfirmed (`environments.md`).
- Connection reference owners are unconfirmed for all four Solutions.
- Five flows across two Solutions are unmapped or only loosely mapped against the Automation Registry — see `exports/power-automate/solution-inventory.md` § "Unmapped flows".
- One registered flow (`Overflow Emails Suggested Match Approval`) has no export evidence in this set.
- No Solution export currently exists for `AUTO-EMAIL-BACKUP-001`'s `Email Back Up Generator` flow or for `AUTO-MONDAY-BACKUP-001`'s two backup flows.
