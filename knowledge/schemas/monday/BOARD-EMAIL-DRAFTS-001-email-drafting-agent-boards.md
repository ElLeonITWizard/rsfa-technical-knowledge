---
id: BOARD-EMAIL-DRAFTS-001
title: Email Drafting Agent — proposed Monday board schemas
status: planned
owner: RSFA
related_automations:
  - AUTO-EMAIL-DRAFT-001
workspace: Real Savvy_CRM (2308685) — proposed, TODO: confirm
last_modified: 2026-11-04
last_verified: "TODO: verify — boards not yet created"
---

# BOARD-EMAIL-DRAFTS-001 — Email Drafting Agent boards (proposed)

> **Status: Planned.** Neither board exists yet. A Monday search on 2026-11-04 (board names containing "Email Draft") returned only the existing Overflow Emails boards. Column IDs will be assigned by Monday on creation and must be recorded here afterwards — until then every column ID is `TODO: assign on creation`. Do not reference these columns from a flow until real IDs are recorded.

Both boards should be **private** (Rod Schubert + `tech@rsfa.co.nz` / RSFA IT Desk in v1) because the Drafts board holds AI draft text written to clients.

---

## 1. `✉️ Email Drafts` (one item per processed client email)

Item name: email subject (truncated to 120 characters; `No Subject` if empty — same convention as `Add_Email_to_Timeline_Monday`).

Groups: `Needs review` (Draft ready, Edited in Monday, Conflict, Failed), `Done` (Sent…, Discarded…, No reply needed, Superseded, Stale), `Skipped`. Group moves are done by the flows.

| Column | Type | Values / purpose | Written by |
|---|---|---|---|
| Name | name | Email subject | Intake |
| Draft Status | status | `Queued`, `Processing`, `Draft ready`, `Edited in Monday`, `Conflict`, `Sent from Outlook`, `Sent from Monday`, `Discarded in Outlook`, `Discarded in Monday`, `No reply needed`, `Superseded`, `Superseded – kept (edited)`, `Stale`, `Skipped`, `Failed` | Flows only |
| Adviser Action | status | empty, `Approve & send`, `Update Outlook draft`, `Regenerate`, `Discard`. **Webhook trigger column.** Reset to empty by the handler | Adviser |
| Research Depth | status | `Basic`, `Medium`, `Deep` — used by the next Generate/Regenerate | Intake (default) / Adviser |
| Client Profile | board_relation → `Client Profiles` (`5024661649`) | Matched client | Intake |
| Mailbox | dropdown | `rod@rsfa.co.nz` (later others) | Intake |
| Adviser | people | Mailbox owner (Rod) — notifications/filters | Intake |
| Sender Email | email | Verified client sender | Intake |
| Received At | date (with time) | Email `receivedDateTime` | Intake |
| Original Email Link | link | Outlook `webLink` of the incoming email | Intake |
| Outlook Draft Link | link | Outlook `webLink` of the current AI draft | Generate / Handler |
| Draft Text | long_text | AI draft body as plain text, editable by the adviser (Decision D1). Placeholders `[[ADVISER: …]]` kept as-is | Generate / Adviser |
| Missing Information | long_text | From AI `missing_information` | Generate |
| Notes for Adviser | long_text | From AI `notes_for_adviser` (never sent) | Generate |
| Reply Category | status | `information_request`, `document_sent`, `scheduling`, `thanks_ack`, `advice_request`, `complaint`, `other` | Generate |
| Risk Flag | status | `None`, `Review carefully` | Generate |
| Risk Details | text | Comma list of `risk_flags` | Generate |
| Confidence | status | `low`, `medium`, `high` | Generate |
| Edited in Outlook | status | `No`, `Yes` | Reconciliation |
| Edited Before Send | status | `No`, `Yes`, `Unknown` | Sent Items Sync |
| Skip / Error Reason | text | e.g. `Skipped – automatic message`, `Failed – AI unavailable` | Flows |
| Model | text | Model used for the current draft | Generate |
| Input Tokens | numbers | OpenAI `usage.input_tokens` (cumulative across regenerations) | Generate |
| Output Tokens | numbers | OpenAI `usage.output_tokens` (cumulative) | Generate |
| Generation Count | numbers | Number of generations for this email | Generate |
| Draft Created At | date (with time) | Current draft creation | Generate |
| Final Status At | date (with time) | Sent / discarded time | Flows |
| Actioned By | people | Monday user who triggered the last action | Handler |
| Outlook Message ID | text | Incoming message immutable ID | Intake |
| Internet Message ID | text | Duplicate check key | Intake |
| Conversation ID | text | Supersede and sent-match key | Intake |
| Outlook Draft ID | text | Current draft immutable ID | Generate / Handler |
| Outlook ChangeKey | text | Draft `changeKey` at last sync — conflict detection | Generate / Handler / Reconciliation |
| Last Run | link | Power Automate run URL of the last flow touching the item | Flows |
| Power Automate Run | board_relation → `⚡ Power Automate Runs` (`5030408927`) | Run log link (existing convention) | Flows |

Webhook (Monday integration "When a column changes → send a webhook"): column `Adviser Action` → HTTP trigger URL of `Email Drafting Agent - Monday Action Handler`. The URL is a secret — store in 1Password (item name TODO), never in this repository.

Views (proposed): `Needs review` (filter status ∈ Draft ready / Edited in Monday / Conflict / Failed, sorted by Received At), `Today`, `Quality` (Sent unchanged vs edited vs discarded — for Rod's testing), `Costs` (tokens per day).

---

## 2. `⚙️ Email Drafting Agent Settings` (one item per mailbox)

Item name: mailbox address (e.g. `rod@rsfa.co.nz`, `tech@rsfa.co.nz` for testing).

| Column | Type | Purpose |
|---|---|---|
| Name | name | Mailbox address (lookup key) |
| Enabled | status | `Yes` / `No` — master switch, checked on every Intake run |
| Adviser | people | Mailbox owner |
| Allowed Approvers | people | Who may use `Approve & send` for this mailbox |
| Default Depth | status | `Basic` / `Medium` / `Deep` |
| Daily Draft Cap | numbers | Max automatic generations per NZ day |
| Model Basic / Model Medium / Model Deep | text (3 columns) | OpenAI model per depth — TODO: decide in testing |
| Max Context Characters Basic / Medium / Deep | numbers (3 columns) | Truncation limits (§12 of AUTO-EMAIL-DRAFT-001) |
| Reply Mode | status | `Reply` / `Reply all` (Decision D3) |
| Tone | long_text | Rod's "Tone" prompt input |
| Style | long_text | Rod's "Style" prompt input |
| Other Instructions | long_text | Rod's "Other instructions" prompt input |
| Sign-off | long_text | Closing/signature text, if not added by Outlook automatically — TODO: check whether Rod's Outlook signature is applied to drafts created via Graph (it normally is **not**) |
| Stale After (days) | numbers | Reconciliation threshold |
| Last Changed Note | text | Who changed the prompt and why (manual) |

The fixed safety rules (AUTO-EMAIL-DRAFT-001 §14.2 item 1) are **not** stored here, so they cannot be removed by editing the board.

---

## 3. Change history

| Date | Change | Author |
|---|---|---|
| 2026-11-04 | Initial proposed schemas for both boards. Not created in Monday. | Claude (design task, requested by Leonardo Melman) |
