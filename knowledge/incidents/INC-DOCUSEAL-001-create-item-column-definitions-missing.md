---
id: INC-DOCUSEAL-001
title: DocuSeal-created submissions not reaching Monday (create-item column definitions missing)
status: resolved
severity: medium
related_automations:
  - AUTO-DOCUSEAL-001
related_scenarios:
  - name: "M.com: DocuSeal Submission Lifecycle Sync (Sep 2026)"
    id: "9803640"
related_boards:
  - name: 🖊️ DocuSeal Submissions
    id: "5029524384"
detected: 2026-11-02
resolved: 2026-11-02
last_modified: 2026-11-02
last_verified: 2026-11-02
---

# INC-DOCUSEAL-001 — DocuSeal-created submissions not reaching Monday

## Summary

From 2026-10-27 to 2026-11-02, every submission created **directly in DocuSeal** failed to get its Monday item in `🖊️ DocuSeal Submissions`. Each webhook for such a submission sent a technical email:

```text
Step: Monday createItem2V2 (create path). Event: form.completed. Submission ID: <id>.
Error: Function 'removeNullsAndEmptyArrays' finished with error! Function 'encodeItemColumnValues'
finished with error! Board column definitions are missing. Please open the module settings and
reselect the board to reload columns.
```

Submissions sent from Monday (`AUTO-DOCUSEAL-002`, Send Now) were **not** affected: they never use the create-item path.

## Impact (Confirmed from live system — Make, Monday, DocuSeal, 2026-11-02)

- 3 production submissions had no Monday item: `12911238` (created 2026-10-30), `12988461` and `12992472` (2026-11-01/02). 7 executions failed in total (several webhooks per submission).
- No Sync Index record was written for them, so later events kept failing (repeated emails).
- None of the 3 was completed yet (client still `sent`), so no signed document was left unfiled and no filing lock was set.
- No item, file or record was lost or overwritten.

## Root cause (Confirmed)

- `monday:createItem2V2` encodes column values using the board's column definitions stored in the module's editor metadata (`metadata.expect` → `columnValues.spec`, with `mondayType` per column).
- On 2026-10-27 the `AUTO-DOCUSEAL-002` dependency change was applied by sending the full blueprint through the Make MCP connector **without** the editor metadata (`expect`, `parameters`, `interface`). Every later API update carried that forward. Confirmed by comparing exports `786bf36` (2026-10-26, metadata present) and `89f44f2` (metadata absent).
- All other modules kept working without that metadata. The two create-item modules (70 contact found, 9081 no contact) cannot.
- The change was not caught by testing because every end-to-end test after 2026-10-27 used Send Now, which skips the create-item path.

## Resolution

1. **Fix (2026-11-02 03:33 UTC):** restored `metadata.parameters` and `metadata.expect` on modules 70 and 9081 from the 2026-10-26 export, adding the definitions for the two columns added on 2026-10-27 (`email_mm8hpzzs` email, `board_relation_mm8hgw4t` board relation → `5032131811`), in the same shape as the existing columns.
   - Tested first in a temporary scenario with the same module and metadata: test item created with all 8 columns, including both relations, then deleted (scenario deleted too).
   - Applied with backup; re-read: 95 modules, only 70 and 9081 differ, identical to the target; scenario stayed active.
2. **Recovery:** the 7 failed executions were replayed one at a time, oldest first. Each finished successfully; 3 items were created (`2896925425`, `2896953960`, `2896927775`), linked to the correct Client Profiles, named with the naming convention.
3. **Status correction:** two recovered items showed `Viewed` because the adviser signed his own part directly in DocuSeal (see Follow-ups). DocuSeal showed the clients still at `sent`, so both were set to `Sent` manually.

## Follow-ups

- **Process rule:** when updating a Make blueprint through the API, keep every module's existing `metadata` (including `expect`/`parameters`/`interface`) and re-test any create-item path, not only the path being changed. Recorded in `AUTO-DOCUSEAL-001` §22.
- **Other modules still lack editor metadata** (they run correctly). Opening and saving them in the Make editor restores it; low priority.
- **Viewed from adviser signing:** module 21 treated `form.viewed`/`form.started`/`form.completed` from an adviser (`@rsfa.co.nz`) as Viewed. **Fixed 2026-11-02** (RSFA-approved): those events from an adviser now map to Sent (`AUTO-DOCUSEAL-001` §13).
- **Naming when the template starts with the client name:** e.g. template `Jane_Example_Medical_Information` gives `Example_Jane_Jane_Example_Medical_Information_02Nov26`, because only `_First_Last` (with a leading underscore) is stripped. Proposed fix: also strip a leading `First_Last_` — not applied, awaiting RSFA approval.

## Change history

| Date | Change | Author |
|---|---|---|
| 2026-11-02 | Adviser-viewed follow-up fixed in module 21. | Claude (incident task) |
| 2026-11-02 | Incident recorded after fix, recovery and verification. | Claude (incident task) |
