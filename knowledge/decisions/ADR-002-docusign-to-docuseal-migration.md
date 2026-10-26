---
id: ADR-002
title: Migrate electronic signatures from DocuSign to DocuSeal
status: accepted
owner: RSFA
date: 2026-09-20
audience:
  - Authorised developers
  - Authorised technical consultants
last_modified: 2026-10-26
last_verified: 2026-10-26
---

# ADR-002 — Migrate electronic signatures from DocuSign to DocuSeal

## Context

DocuSign is RSFA's current electronic-signature platform, integrated via the Power Automate flow `DocuSign to SharePoint` (`AUTO-DOCUSIGN-001`), which files completed envelopes into client SharePoint folders and notifies Slack (`knowledge/automations/power-automate/AUTO-DOCUSIGN-001-docusign-filing.md`).

DocuSeal was previously listed as `Experimental` / `Low` criticality (`knowledge/02_SYSTEMS_REGISTRY.md` SYS-DOCUSEAL-001), with only a test board and trial account, "being considered as a possible future replacement for DocuSign."

Per RSFA (reported directly in chat, 2026-09-20 — Confirmed from provided evidence, not independently verified live): RSFA now has a first production Make.com automation live for DocuSeal, `M.com: DocuSeal Submission Lifecycle Sync (Sep 2026)` (`9803640`, see `AUTO-DOCUSEAL-001`), syncing DocuSeal submissions to a Monday board. RSFA intends to migrate document sending/signing from DocuSign to DocuSeal entirely, expected between October and November 2026.

## Decision

Per RSFA (2026-09-20, Confirmed from provided evidence — not independently verified against a signed migration plan or cutover date): **RSFA intends to replace DocuSign with DocuSeal** as its electronic-signature platform, with the transition expected in October–November 2026. This is a statement of current direction and an in-progress build, not a confirmed completed migration — as of this record, DocuSign remains the live signing platform and `AUTO-DOCUSIGN-001` remains active.

## Consequences

- `AUTO-DOCUSIGN-001` is marked `Active - Planned Retirement` in `knowledge/03_AUTOMATION_REGISTRY.md` (status value already defined in `knowledge/06_NAMING_AND_ID_CONVENTIONS.md` §14, used elsewhere for the Jet mailbox flows) — still active and relied upon today, but new work should not extend it further without checking this decision first.
- `SYS-DOCUSIGN-001` status changes from `Active` to `Active - Reducing` in `knowledge/02_SYSTEMS_REGISTRY.md`; `SYS-DOCUSEAL-001` status changes from `Experimental` to `Active - Expanding`, criticality from `Low` to `Medium`, reflecting a real production automation now depending on it.
- New automation proposals involving document signing should default to DocuSeal, not DocuSign, unless RSFA says otherwise.
- Once the migration completes, `AUTO-DOCUSIGN-001` should be marked `deprecated` (not deleted) per CLAUDE.md §11, linked to `AUTO-DOCUSEAL-001` as its replacement, with migration/compatibility considerations documented at that time — not yet done, since the migration has not happened.
- ~~`AUTO-DOCUSEAL-001` does not currently include a SharePoint-filing step for signed documents~~ — **resolved (2026-10-26):** `AUTO-DOCUSEAL-001` now files each completed submission's signed PDF(s) into the client's SharePoint folder under `h. FileInvite and Docusign` (the same subfolder `AUTO-DOCUSIGN-001` uses), with a Slack "Manual SharePoint Filing Required" fallback when no single Client Profile or valid `SP folder` link exists. Confirmed from the 2026-10-26 blueprint and a live SharePoint check (see `AUTO-DOCUSEAL-001` §4, §13).

## Status update — 2026-10-26

Status changed from `proposed` to `accepted`. Evidence:

- **Per RSFA (2026-10-26):** SharePoint filing has been implemented, multiple tests were completed, and DocuSeal is now used in production.
- **Confirmed from live system (2026-10-26):** the DocuSeal Monday board holds real client submissions, and signed PDFs are being filed to SharePoint (`AUTO-DOCUSEAL-001` §4).

Not yet confirmed:

- whether DocuSign has been retired or still runs in parallel. `AUTO-DOCUSIGN-001` therefore stays `Active - Planned Retirement` and is **not** marked deprecated. Do that per CLAUDE.md §11 once RSFA confirms the cutover.
- the open reliability findings in `AUTO-DOCUSEAL-001` §18 — the 2026-10-21 → 23 stoppage and duplicate items under concurrent webhooks. These should be reviewed before DocuSign is switched off.

## Alternatives considered

Not documented — this decision was reported by RSFA as already in progress, not proposed for evaluation in this session.

## Related documents

- `knowledge/automations/make/AUTO-DOCUSEAL-001-docuseal-submission-lifecycle-sync.md`
- `knowledge/automations/power-automate/AUTO-DOCUSIGN-001-docusign-filing.md`
- `knowledge/02_SYSTEMS_REGISTRY.md` SYS-DOCUSIGN-001, SYS-DOCUSEAL-001
- `knowledge/03_AUTOMATION_REGISTRY.md` §3, §5
- `knowledge/01_RSFA_SYSTEM_MAP.md` §13, §18

## Change history

| Date | Change | Author |
|---|---|---|
| 2026-09-20 | Initial decision record created from RSFA's direct report alongside the first DocuSeal automation's documentation. | Claude (documentation task) |
| 2026-10-26 | Status `proposed` → `accepted`: DocuSeal confirmed in production, SharePoint-filing gap resolved; DocuSign retirement still unconfirmed. | Claude (documentation task) |
