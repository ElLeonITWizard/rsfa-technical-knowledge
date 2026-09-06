---
id: ADR-001
title: Deprecate Monday Workflow-builder automations in favour of Make.com, Power Automate and minor Monday Automations
status: accepted
owner: RSFA
date: 2026-09-05
audience:
  - Authorised developers
  - Authorised technical consultants
last_modified: 2026-09-05
last_verified: 2026-09-05
---

# ADR-001 — Deprecate Monday Workflow-builder automations

## Context

RSFA had two native Monday **Workflows** (the multi-step Workflow-builder feature, distinct from simple per-board Automations/recipes) in production:

- `AUTO-MONDAY-WF-001` — Move to Pipeline Workflow (New), board `5025429617`.
- `AUTO-MONDAY-WF-002` — Leads App 2 Creation + CP Name, board `5025430003`.

Both were confirmed live on 2026-09-05 to still exist as boards, unchanged since late 2025, while their functions have moved elsewhere:

- `AUTO-MONDAY-WF-001`'s Pipeline-routing function was replaced by the new Make scenario `M.com: Move to Pipeline (Sep 2026)` (`9756260`), part of the 2026-09-04 Leads Board Revamp — see `knowledge/automations/make/AUTO-LEADS-001-lead-client-profile-creation.md` §10a.
- `AUTO-MONDAY-WF-002`'s second-Lead-creation function was **deactivated outright, per RSFA (2026-09-05)** — a two-applicant Leads Form submission now produces a single Lead item instead of two.

## Decision

Per RSFA (2026-09-05, Confirmed from provided evidence — not independently verified against Monday's Workflow builder directly, which does not expose enabled/disabled state via the board-schema API used in this repository's verification): **RSFA no longer builds or relies on Monday Workflow-builder automations.** Going forward, automation logic should be implemented using one of:

- Make.com scenarios.
- Power Automate flows.
- Minor, per-board Monday Automations (native recipes) — the simple "when X, do Y" board-level automations, which are explicitly **not** affected by this decision and remain in active use.

This is a statement of current direction, not a claim that every existing Monday Workflow has been individually audited and removed — see `knowledge/03_AUTOMATION_REGISTRY.md` §6 for the two known instances.

## Consequences

- `AUTO-MONDAY-WF-001` and `AUTO-MONDAY-WF-002` are marked `deprecated` in `knowledge/03_AUTOMATION_REGISTRY.md` and their own automation documents, retained for historical reference (per `CLAUDE.md` §11), not deleted.
- New automation proposals should default to Make.com, Power Automate, or a minor Monday Automation — a Monday Workflow-builder automation should not be proposed without first confirming with RSFA that this direction has changed.
- The Leads board's two-applicant handling is simplified: one Lead item now represents both applicants, rather than two linked Lead items. Any downstream logic that assumed two Lead items per joint enquiry (e.g. `AUTO-LEADS-001`'s per-applicant processing) needs to be checked against this — see `knowledge/automations/make/AUTO-LEADS-001-lead-client-profile-creation.md` §10a and §18.
- Both deprecated Workflow boards (`5025429617`, `5025430003`) still exist in Monday and were confirmed live to be unchanged since late 2025 — this is consistent with, but does not independently prove, deactivation. TODO: verify directly in Monday's Workflow builder if this needs confirming beyond RSFA's own report.

## Alternatives considered

Not documented — this decision was reported by RSFA as already made and in effect, not proposed for evaluation in this session.

## Related documents

- `knowledge/automations/monday/AUTO-MONDAY-WF-001-move-to-pipeline.md`
- `knowledge/automations/monday/AUTO-MONDAY-WF-002-second-applicant.md`
- `knowledge/automations/make/AUTO-LEADS-001-lead-client-profile-creation.md` §10a
- `knowledge/03_AUTOMATION_REGISTRY.md` §6
- `knowledge/02_SYSTEMS_REGISTRY.md` SYS-MONDAY-AUTO-001

## Change history

| Date | Change | Author |
|---|---|---|
| 2026-09-05 | Initial decision record created from RSFA's direct report. | Claude (documentation task) |
