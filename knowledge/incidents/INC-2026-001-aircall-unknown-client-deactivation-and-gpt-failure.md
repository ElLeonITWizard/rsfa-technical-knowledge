---
id: INC-2026-001
title: Aircall — "Calls > Unknown/Client" scenario deactivated and one GPT summary failure
status: resolved-monitoring
severity: medium
incident_date: 2026-11-04
detected_by: Make.com deactivation email + COMP-MAKE-ERROR-001 failure email (RSFA Automation Hub mailbox)
related_automations:
  - AUTO-AIRCALL-001
related_scenarios:
  - name: "M.com: Calls > Unknown/Client"
    id: "5543887"
  - name: M.com: Aircall Upload Transcriptions To SP (Jul 2026)
    id: "9498962"
related_boards:
  - name: 📞 Aircall: VOIP Call Board
    id: "5026308494"
last_modified: 2026-11-06
last_verified: 2026-11-06
---

# INC-2026-001 — Aircall: "Calls > Unknown/Client" deactivated + GPT summary failure

All times are UTC. The notification emails showed local times of 19:07 and 21:04 on 2026-11-04 (UTC-3 mailbox view).

Two **independent** faults happened on the same day. Only the first one deactivated a scenario.

## 1. Summary

| # | Scenario | Symptom | Business impact | Status |
|---|---|---|---|---|
| A | `M.com: Calls > Unknown/Client` (`5543887`) | Deactivated by Make after one `BundleValidationError` (2026-11-04 22:07:10) | 23 new Aircall VOIP Call Board items kept the placeholder name "Aircall new contact" and were not renamed to the contact name or "Unknown" | Fixed and reactivated 2026-11-06 20:00. Backlog processed automatically. |
| B | `M.com: Aircall Upload Transcriptions To SP (Jul 2026)` (`9498962`) | OpenAI module 14 "Summarise Transcription" errored once (execution `e49c0eac487044fda59a8bcf802ac81c`, 2026-11-05 00:04:16) | One answered call had no AI summary Word document, no SharePoint/Files upload, no timeline entry and no Slack notice. The execution showed SUCCESS because the error handler ended with `Ignore`. | Call reprocessed 2026-11-06 20:04. Automatic retry added to module 14. |

## 2. Fault A — `5543887` deactivation

### Evidence

- **Confirmed from live system (Make):** execution `512e6398a1b94226a984a7faf161cec6` failed with `BundleValidationError: Validation failed for 1 parameter(s).` It used 4 operations and transferred 880 bytes, against roughly 7 KB on normal runs. All earlier runs from 2026-10-29 onward were successful.
- **Confirmed from live system (Make):** scenario settings were `dlq: false` (incomplete executions not stored). With that setting, Make deactivates an instant scenario on a non-retryable error. After the failure the scenario was also flagged `isinvalid: true`.
- **Confirmed from live system (Monday activity log):** the triggering item was created at 22:07:08. Its Contact link was populated at 22:07:58, after the scenario's 15-second sleep had already elapsed.
- **Inference (execution-level module data was not available from the API):** `Get an Item` (module 9) returned an almost empty bundle. The rename modules (10 and 11) mapped `itemId` from `{{9.id}}`, which was therefore empty, and failed the required-parameter validation.

### Fix applied (2026-11-06, approved by RSFA IT in the ticket conversation)

1. Changed `itemId` in modules 10 (rename to contact) and 11 (rename to "Unknown") from `{{9.id}}` to `{{7.pulseId}}`. The trigger always provides the item ID, so a sparse `Get an Item` response can no longer break validation.
2. Enabled "Allow storing of incomplete executions" (`dlq: true`). A future single error now creates an incomplete execution for review instead of switching the scenario off.
3. Reactivated the scenario. `isinvalid` is now `false`.

### Validation

- **Passed:** after reactivation, Make processed the webhook events queued while the scenario was off. All of them ended SUCCESS.
- **Passed:** a board check showed all 23 items created between 2026-11-04 22:07 and 2026-11-06 03:52 are now named either with the linked contact or "Unknown". Item `2899576711`, the one that triggered the failure, is named correctly.
- **Not testable:** a deliberate reproduction of the empty `Get an Item` response was not possible.

### Rollback

The pre-change blueprint was saved outside the repository: in the session scratchpad and in Make's own scenario version history (edit of 2026-11-06 20:00:22). To roll back, restore the previous version in Make, then reactivate.

## 3. Fault B — `9498962` GPT failure

### Evidence

- **Confirmed from live system (blueprint):** the email text "The GPT Fails" exists only in module 14's error handler: `CallSubscenario` to `COMP-MAKE-ERROR-001` (`8732008`), then `builtin:Ignore`.
- **Inference (operation count):** the execution used 11 operations. A full run uses 21, and 11 equals "everything before module 14, plus the handler". Nothing after module 14 ran.
- **Unknown:** the actual OpenAI error (rate limit, timeout, server error, etc.). The Make API returned no module-level detail.
- **Confirmed from live system:** this was the only GPT failure between 2026-10-28 and 2026-11-06. All later runs succeeded. A screenshot later re-sent as "another error" was the same 2026-11-05 00:04 email, not a new failure.

### Fix applied (2026-11-06)

Module 14's error handler was changed from "email → Ignore" to an automatic retry:

1. `Sleep` 90 s (module 171).
2. `Summarise Transcription (Retry)` (module 174): an identical OpenAI `createModelResponse` call with the same model, prompt and connection.
3. `Resume` (module 175) with `result = {{174.result}}`. The normal flow continues with the retry's output: KeyPoints and ActionItems parsing, Word document, SharePoint, Files column, timeline, Slack and central Activities.
4. If the retry also fails, module 174's own handler sends the `COMP-MAKE-ERROR-001` email, which now includes the CallID and states that the retry also failed, then `Ignore`.

A self-calling retry (scenario re-invoking itself) was attempted first. Make rejected it as an infinite-loop chain, so it was not saved.

### Reprocessing of the missed call

- Ran `9498962` on demand with the affected CallID (Aircall VOIP Call Board item `2899709866`). Execution `ad060e17c60f41c69315fcd8a36f57a1` ended SUCCESS with 21 operations, the full happy path.
- **Partially verified:** completion was confirmed from Make execution status and operation count. The presence of the Word document in SharePoint was not opened and checked.

### Validation status

- **Passed:** the scenario saved with `isinvalid: false` and remained active. The reprocessing run on the edited blueprint completed the full path.
- **Not testable:** the retry branch itself (modules 171, 174 and 175) cannot be exercised safely without forcing an OpenAI failure. It should be confirmed the next time a "GPT Fails" condition occurs (look for a run with about 23 operations).

### Rollback

Restore the Make version saved before the 2026-11-06 20:02:54 edit.

## 4. Follow-ups

- TODO: verify the retry branch on the next real OpenAI failure.
- TODO: review incomplete executions on `5543887` periodically now that `dlq` is enabled.
- Consider setting `max_output_tokens` on modules 14 and 174 (currently unset).

## 5. Change history

| Date | Change | Author |
|---|---|---|
| 2026-11-06 | Incident recorded; fixes applied and validated as described. | Claude (ticket investigation, on RSFA IT request) |
