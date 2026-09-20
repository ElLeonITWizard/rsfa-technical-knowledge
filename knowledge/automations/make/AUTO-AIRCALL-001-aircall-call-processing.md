---
id: AUTO-AIRCALL-001
title: Aircall Call Processing, Transcription and Summary
platform:
  - Make.com
  - Native integration
status: active-under-improvement
criticality: high
owner: RSFA
technical_account: tech@rsfa.co.nz
business_process: Turn every Aircall phone call into a client-matched, transcribed and AI-summarised record filed against the correct Client Profile, so advisers have a searchable written record of every call without manual note-taking.
source_systems:
  - Aircall
related_systems:
  - Monday.com
  - OpenAI
destination_systems:
  - SharePoint
  - Monday.com
related_boards:
  - name: 📞 Aircall: VOIP Call Board
    id: "5026308494"
  - name: Contacts
    id: "2074688484"
  - name: Client Profiles
    id: "5024661649"
related_scenarios:
  - name: Aircall Transcript Summary
    id: "6123035"
  - name: M.com: Aircall Upload Transcriptions To SP (Jul 2026)
    id: "9498962"
  - name: "M.com: Calls > Unknown/Client"
    id: "5543887"
  - name: M.com: New item in Contacts (Aircall) -> Delete
    id: "6548539"
  - name: M.com: New Transcription in Aircall (Jul 2026)
    id: "9627699"
  - name: M.com: Contact Change in Aircall Board (Jul 2026)
    id: "9627714"
related_flows: []
last_modified: 2026-09-06
last_verified: 2026-09-06
documentation_status: partial
---

# AUTO-AIRCALL-001 — Aircall Call Processing, Transcription and Summary

## 1. Purpose

Automatically match Aircall calls to the correct client, generate a full written transcript and a concise AI-generated summary of the conversation in Word format, file both documents in the client's SharePoint folder and Monday Files column, and add the call to the client's activity timeline — so every advice-relevant phone call becomes a durable, reviewable written record.

## 2. Business context

Aircall's native Monday integration creates a call record in the `📞 Aircall: VOIP Call Board` for every call. `knowledge/01_RSFA_SYSTEM_MAP.md` §11 describes the full flow: native integration → call board → Monday native automation + Make.com processing → client matching, transcription, AI summary, SharePoint filing, Slack notification. Short calls may not produce a transcription; this is treated as an expected case, not a failure.

## 3. Scope

### Included

- Matching an incoming call's phone number/contact to a Client Profile.
- Handling calls that cannot be matched to a known contact ("Unknown/Client" routing).
- Retrieving the call recording and transcription from Aircall by Call ID.
- Combining transcription utterances into a single conversation.
- Generating a full transcript Word document and a separate GPT-generated summary Word document from SharePoint-stored templates.
- Uploading both documents to the client's SharePoint folder and to the Client Profiles Files column.
- Adding the call to the Client Profile's activity timeline, tagged as an Aircall Call.
- Cleanup of stray Contacts records created by the Aircall native integration.

### Excluded

- Call routing/answering within Aircall itself.
- Slack notification for new calls (described in the system map as "currently being developed" — not yet confirmed live).

## 4. Current status

Active - Under Improvement. Registry criticality: High. **Per RSFA, the transcription/summary automation has been stabilised** (2026-09-05 update). Confirmed from live system (2026-09-05): the trigger architecture changed materially since 2026-07-30 —

- `Aircall Transcript Summary` (`6123035`), the original standalone scenario, is now **Inactive** (last edited 2026-08-08).
- Two new scenarios, both created 2026-08-06, now provide the trigger path into the core processing scenario `9498962`: `M.com: New Transcription in Aircall (Jul 2026)` (`9627699`, triggered directly by Aircall's own `transcription.created` webhook — not a Monday-watch trigger) and `M.com: Contact Change in Aircall Board (Jul 2026)` (`9627714`, triggered by a Monday webhook when a call's linked Contact changes, gated by "already processed" checks to avoid duplicate runs).

This is a materially different, more event-accurate trigger design than the original Monday-watch-only approach, consistent with RSFA's description of stabilisation work — but the causal relationship between the two changes (new scenarios created → old scenario deactivated two days later) is inferred from timing, not confirmed by a change-log entry. The `Transcription Available (Bot)` flag on the Aircall VOIP Call Board (`5026308494`) still exists per the 2026-07-30 export; not re-verified live in this pass. Recent-error counts from the 2026-07-30 export (6 recent errors on `9498962`) were not re-checked live in this pass — TODO: verify current error status.

## 5. Trigger

- `Aircall Transcript Summary` (6123035): Monday.com instant trigger (watch) on the Aircall VOIP Call Board. **Inactive as of 2026-09-05** — retained here for history, not a current trigger path.
- `M.com: Aircall Upload Transcriptions To SP (Jul 2026)` (9498962): **Corrected 2026-09-06** — this scenario has no Monday.com watch trigger of its own. Confirmed from live system (2026-09-06, Make MCP `scenarios_get`): `hookId` is null, `chainingRole` is `bridge`, scheduling type is `on-demand`. It runs only on-demand as a subscenario. Confirmed caller: `9627714` (`M.com: Contact Change in Aircall Board (Jul 2026)`). Per `03_AUTOMATION_REGISTRY.md`, likely also called by `9627699` (`M.com: New Transcription in Aircall (Jul 2026)`) — not yet independently confirmed from that scenario's own blueprint. The prior description here — "Monday.com instant trigger (watch)" — is outdated/incorrect as of this verification; retained in the change history (§26) rather than silently deleted.
- `M.com: Calls > Unknown/Client` (5543887): Monday.com instant trigger (watch).
- `M.com: New item in Contacts (Aircall) -> Delete` (6548539): Monday.com instant trigger (watch), for cleanup of Aircall-generated Contacts.
- `M.com: New Transcription in Aircall (Jul 2026)` (9627699) — **new, confirmed live 2026-09-05:** Aircall-native webhook trigger on the `transcription.created` conversation-intelligence event; calls `9498962` directly with the Call ID.
- `M.com: Contact Change in Aircall Board (Jul 2026)` (9627714) — **new, confirmed live 2026-09-05:** Monday webhook trigger, fires on a Contact-link change to a call item; calls `9498962` after "already processed" checks.

## 6. Inputs

- New item in `📞 Aircall: VOIP Call Board` (Call ID, linked contact).
- Aircall call and transcription data, retrieved via the stored Call ID.
- Word template files stored in the Aircall Templates SharePoint folder (transcript template and summary template).
- GPT (OpenAI) for summary generation.

## 7. Outputs

- Full call transcript Word document, filed in the client's SharePoint folder.
- AI-generated call summary Word document, filed in the client's SharePoint folder.
- Both documents also uploaded to the Client Profiles board Files column.
- New Client Profile timeline entry tagged "Aircall Call".

## 8. Systems involved

Aircall (native integration + API), Monday.com (call board, Contacts, Client Profiles), Make.com (execution), OpenAI/GPT (summary generation), Docx Templater (document population), Microsoft SharePoint (template source and document destination), Slack (planned, not yet confirmed live).

## 9. Related Monday boards

| Board | ID | Role |
|---|---|---|
| 📞 Aircall: VOIP Call Board | `5026308494` | Trigger source; stores Call ID, linked Contact, transcription-availability flag |
| Contacts | `2074688484` | Client matching by phone; also the target of the cleanup scenario |
| Client Profiles | `5024661649` | Destination for Files column upload and activity timeline entry |

## 10. Platform implementation

### Make.com scenarios

| Scenario ID | Exact Make name | Role | Status | Trigger | Calls | Called by | Source confidence |
|---|---|---|---|---|---|---|---|
| `6123035` | Aircall Transcript Summary | Standalone | **Inactive (was Active)** | Monday.com instant trigger (watch) | None confirmed | None confirmed | Confirmed live 2026-09-05: status change since 2026-07-30 |
| `9498962` | M.com: Aircall Upload Transcriptions To SP (Jul 2026) | Parent (also confirmed callable as subscenario) | Active | **Corrected 2026-09-06:** On-demand / bridge (subscenario only) — `hookId` null, `chainingRole` `bridge`, confirmed live via `scenarios_get`; no independent Monday watch trigger. Previously documented as "Monday.com instant trigger (watch)" — that was incorrect. | `Outlook: Email Notification after Failed Scenario` (`8732008`) | `9627699`, `9627714` (confirmed live 2026-09-05) | Current (registry + call graph); matches source-material walkthrough in detail |
| `5543887` | M.com: Calls > Unknown/Client | Standalone | Active | Monday.com instant trigger (watch) | None confirmed | None confirmed | Current (registry + call graph) |
| `6548539` | M.com: New item in Contacts (Aircall) -> Delete | Standalone | Active | Monday.com instant trigger (watch) | None confirmed | None confirmed | Current (registry + call graph) |
| `9627699` | M.com: New Transcription in Aircall (Jul 2026) | Parent | Active | Aircall instant trigger (`transcription.created`) | `9498962` | None confirmed | New, confirmed live 2026-09-05 via blueprint inspection |
| `9627714` | M.com: Contact Change in Aircall Board (Jul 2026) | Parent | Active | Monday webhook (Contact-link change) | `9498962` | None confirmed | New, confirmed live 2026-09-05 via blueprint inspection |

`Outlook: Email Notification after Failed Scenario` (`8732008`, `COMP-MAKE-ERROR-001`) is called by `9498962` as a shared error-handling component, not part of this automation's own logic.

### Power Automate flows

Not applicable.

### Monday native automations or workflows

Monday native automations participate in the call board's routing per `knowledge/01_RSFA_SYSTEM_MAP.md` §11 (`MondayAutomation` node in the flow diagram) — exact recipe not documented. TODO: verify.

### Native integrations

Aircall native Monday integration creates the initial call record in the Aircall VOIP Call Board (`knowledge/02_SYSTEMS_REGISTRY.md` SYS-AIRCALL-001).

### Shared subflows and components

`COMP-MAKE-ERROR-001` (Shared Make Failure Email Notification) — used by scenario `9498962`.

## 11. End-to-end process

```mermaid
flowchart TD
    A[Aircall call] --> B[Aircall native Monday integration]
    B --> C[New item in Aircall VOIP Call Board]
    C --> D{Contact matched?}
    D -->|Yes| E[Wait for contact link to populate]
    D -->|No| F[M.com: Calls > Unknown/Client]
    E --> G[Retrieve client SharePoint folder via Contact -> Client Profile]
    G --> H[Retrieve call + transcription from Aircall by Call ID]
    H --> I{Transcription available?}
    I -->|No, e.g. short call| J[Expected case, no document generated]
    I -->|Yes| K[Combine transcription utterances]
    K --> L[Generate full transcript Word doc from SP template]
    K --> M[Generate GPT AI summary Word doc from SP template]
    L --> N[Upload transcript + summary to client SharePoint folder]
    N --> O[Upload transcript + summary to Client Profiles Files column]
    O --> P[Add Aircall Call entry to Client Profile timeline]
    C --> Q[M.com: New item in Contacts Aircall -> Delete]
    Q --> R[Clean up stray Aircall-generated Contacts record]
```

## 12. Data mapping

| Source field | Destination | Notes |
|---|---|---|
| Aircall Call ID (Monday) | Aircall API call/transcription lookup | Key used to retrieve call detail |
| Linked Contact -> Client Profile -> SP folder | Upload destination | Resolved via the Contact's Client Profile relation |
| Combined transcription utterances | Full transcript Word template | Populated via Docx Templater |
| GPT-generated summary text | Summary Word template | Populated via Docx Templater |

TODO: complete mapping from current production configuration for exact template placeholder names and Monday Files-column field IDs.

## 13. Decision and routing logic

- If the call cannot be matched to a known contact, `M.com: Calls > Unknown/Client` handles routing instead of the main transcription path.
- If no transcription is available (typically short calls), no transcript/summary document is generated — this is expected behaviour, not an error.
- The Aircall native integration occasionally creates a stray Contacts record; `M.com: New item in Contacts (Aircall) -> Delete` removes it.
- Voicemail items are excluded from the Aircall retrieval/document-generation branch: the `Get Contacts To Get Client Profiles` filter ("Recording and Call ID exist") was extended with an additional AND condition — `{{4.mappable_column_values.link_mm01c4ba.url}}` does NOT contain `/voicemail`. This routes voicemail records to skip the branch entirely, treated as an expected no-op, the same way short calls with no transcription are already handled. — *Confirmed from live system (2026-09-06 blueprint inspection + live fix applied by RSFA IT)*

## 14. Dependencies

- Client's SharePoint folder must already exist (`AUTO-SP-FOLDER-001`).
- Aircall Templates SharePoint folder must contain the current transcript and summary Word templates.
- OpenAI/GPT availability for summary generation.

## 15. Error handling

`M.com: Aircall Upload Transcriptions To SP (Jul 2026)` calls the shared `COMP-MAKE-ERROR-001` Outlook failure-notification component on error.

## 16. Logging and observability

Recent-errors counts are visible in the Make inventory export (`exports/make/valid-scenarios-working-inventory.md`) but are not otherwise summarised in a Monday board. TODO: verify whether a dedicated error/health board (e.g. System Health Monitor, board `5030207135`) currently tracks this automation.

## 17. Manual operations and reprocessing

Not confirmed. TODO: verify whether a failed transcription/summary generation can be manually re-triggered, or requires a Make.com scenario re-run from the error point.

## 18. Known limitations

- Short calls may not produce a transcription — expected, not a defect.
- Slack notification for new Aircall processing is described in the system map as "currently being developed" and should not be assumed live.
- Recent-error counts from the 2026-07-30 export were not re-checked live in this pass — needs follow-up before being treated as fully stable.
- The reason `6123035` was deactivated is not confirmed — inferred from timing relative to the two new trigger scenarios, not from a direct statement or change log.
- The `Transcription Available (Bot)` field on the Aircall VOIP Call Board was not re-verified live in this pass (last confirmed in the 2026-07-30 export).
- **Voicemail 404 failures — resolved 2026-09-06.** Voicemail records previously failed with a 404: `Get Item Call` (`aircall:getCall`) derives the Aircall call ID by stripping `https://assets.aircall.io/calls/` and `/recording` from the Recording/VM URL, but voicemail URLs end in `/voicemail`, so the suffix was never stripped (e.g. producing `4117209783/voicemail`). Fixed by extending the filter in `Get Contacts To Get Client Profiles` to skip `/voicemail` URLs (§13). **Residual risk:** if Aircall changes the Recording/VM URL format for voicemails, this string-match detection would silently stop working with no alert — recommend a periodic spot-check of a sample voicemail item's URL format.

## 19. Security and sensitive data

Call recordings, transcriptions and summaries may contain sensitive client financial/personal information. Never use real call recordings or transcripts as test data; use synthetic test calls only, and never commit real transcript content to this repository.

## 20. Testing

### Confirmed tests

None recorded.

### Required regression tests

- Call with a matched contact and available transcription → transcript + summary generated and filed correctly.
- Call with a matched contact but no transcription (short call) → no document generated, no error raised.
- Call with no matched contact → routed via `M.com: Calls > Unknown/Client`.
- Stray Aircall Contacts record → correctly deleted by the cleanup scenario.

### Test data restrictions

Use synthetic/test Aircall calls only; never process real client call recordings as test data.

## 21. Validation after change

Place a test call through Aircall with a known test contact, confirm the call item appears on the Aircall VOIP Call Board, confirm the transcript and summary documents are generated (where transcription is available) and filed to both SharePoint and the Client Profiles Files column, and confirm the activity timeline entry appears.

## 22. Rollback

Disable the affected Make.com scenario(s). No automated rollback of already-generated documents is defined.

## 23. Troubleshooting guide

1. Confirm the call appears in the Aircall VOIP Call Board with a Call ID.
2. Confirm the linked Contact and its Client Profile relation are populated (the flow explicitly waits for this).
3. If no transcript/summary was generated, check whether the call was short enough that Aircall itself produced no transcription (expected) versus a genuine processing failure.
4. Check for `COMP-MAKE-ERROR-001` failure emails.
5. Check the Make inventory export for recent-error counts on the relevant scenario.

## 24. Source references

- `source-material/make/M.com_ Aircall Upload Transcriptions To SP (Jul 2026).md` — Current. Detailed step-by-step walkthrough matching scenario `9498962`.
- `exports/make/valid-scenarios-working-inventory.md` — Current. Scenario IDs, trigger types, recent-error counts.
- `exports/make/make-scenario-call-graph.md` — Current. Confirmed call to `COMP-MAKE-ERROR-001`.
- `knowledge/03_AUTOMATION_REGISTRY.md` §3, §4 — Current. Family grouping and canonical ID.
- `knowledge/01_RSFA_SYSTEM_MAP.md` §11 — Current. Business-process flow and expected-short-call behaviour.
- `knowledge/04_MONDAY_BOARDS_REGISTRY.md` — Current. Aircall VOIP Call Board description.
- RSFA direct report, 2026-09-05 — reported the transcription/summary automation as stabilised.
- Live Make MCP scenario list and blueprint inspection, 2026-09-05 — confirmed `6123035` inactive, `9627699`/`9627714` new and active, and both calling `9498962` as a subscenario.

## 25. Known gaps

- Exact Monday native automation recipe used in the call-routing path is not documented.
- Slack notification status (built vs. planned) is unconfirmed.
- Root cause of recent errors on scenarios `9498962` and `9254149`-adjacent flows: **partially investigated 2026-09-06.** One cause — voicemail records producing a 404 in `Get Item Call` because the Recording/VM URL ends in `/voicemail` instead of `/recording` — is confirmed diagnosed and fixed (§13, §18). This is **not confirmed** to be the cause of all 6 recent errors recorded in `exports/make/valid-scenarios-working-inventory.md`; only the voicemail-404 pattern itself is confirmed. The remaining error count/causes are still open — TODO: verify.
- Manual reprocessing procedure for a failed transcription/summary generation is not confirmed.
- The reason `6123035` was deactivated is not confirmed (inferred from timing only).

## 26. Change history

| Date | Change | Author |
|---|---|---|
| 2026-07-30 | Initial canonical documentation created from registry, call-graph and source-material evidence. | Claude (documentation task) |
| 2026-09-05 | Documented the stabilised trigger architecture per RSFA and live Make MCP re-verification: `6123035` confirmed Inactive; two new scenarios (`9627699` Aircall-native transcription webhook, `9627714` Monday Contact-change webhook) confirmed live, both calling `9498962` as a subscenario. Recorded that the causal link between the two changes is inferred from timing, not confirmed. | Claude (documentation task) |
| 2026-09-06 | Fixed voicemail-404 root cause in scenario `9498962` (module "Get Contacts To Get Client Profiles" filter extended to skip items whose Recording/VM URL contains "/voicemail"). Also corrected documented trigger type for `9498962` from "Monday.com instant trigger (watch)" to "on-demand / bridge (subscenario only)" based on live blueprint inspection. | TODO: confirm author |
