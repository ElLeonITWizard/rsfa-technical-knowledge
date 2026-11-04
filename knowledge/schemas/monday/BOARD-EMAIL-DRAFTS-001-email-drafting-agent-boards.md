---
id: BOARD-EMAIL-DRAFTS-001
title: Email Drafting Agent — Monday board schemas
status: active (boards created, not yet used by any flow)
owner: RSFA
related_automations:
  - AUTO-EMAIL-DRAFT-001
workspace: Real Savvy_CRM (2308685)
last_modified: 2026-11-04
last_verified: 2026-11-04
---

# BOARD-EMAIL-DRAFTS-001 — Email Drafting Agent boards

**Confirmed from live system (Monday MCP, 2026-11-04):** both boards were created on 2026-11-04 by Claude through the Monday connector at Leonardo Melman's request, then simplified the same day after review (see change history). The column lists below were read back from the API after the last change. No flow writes to the boards yet (`AUTO-EMAIL-DRAFT-001` is `Planned`).

Column IDs are fixed (`eda_*` on Drafts, `eds_*` on Settings). **Do not rename column IDs or status labels** — the flows reference labels by text. Column titles may be changed safely.

| Board | ID | URL | Folder | Kind |
|---|---|---|---|---|
| ✉️ Email Drafting Agent: Drafts | `5032291843` | https://rsfa-squad.monday.com/boards/5032291843 | Daily Boards/Ops (`6649274`) | private |
| ⚙️ Email Drafting Agent: Mailbox Settings | `5032291851` | https://rsfa-squad.monday.com/boards/5032291851 | Daily Boards/Ops (`6649274`) | private |

Owners shown by the API: Rod Schubert, RSFA IT Desk, Kathleen Schubert (Kathleen appears as a workspace owner). TODO: confirm board membership is limited to the intended people before go-live.

---

## 1. `✉️ Email Drafting Agent: Drafts` (`5032291843`)

One item per client email processed by the agent. Item name = email subject (max 120 chars, `No Subject` if empty).

### Views

| View ID | Name | Purpose |
|---|---|---|
| `58179384` | Adviser View (pinned) | What the adviser uses: status, action, draft text, instructions, missing info, notes, risk flag, status detail, client, sender, received, links. Sorted by Received At desc. Technical columns hidden |
| *(Main Table)* | Main Table | Shows every column — for RSFA IT / debugging |

### Groups

| Group ID | Title | Statuses |
|---|---|---|
| `topics` | Needs Review | Ready for review, Needs attention |
| `group_mm8sfnf` | Processing | Processing |
| `group_mm8sta8g` | Done (Sent / Discarded) | Sent from Outlook, Sent from Monday, Discarded |
| `group_mm8s3hhz` | No Draft | No draft |

### Adviser-facing columns (visible in Adviser View)

| Column ID | Title | Type | Values / notes | Written by |
|---|---|---|---|---|
| `name` | Name | name | Email subject | Intake |
| `eda_draft_status` | Draft Status | status | `Processing`, `Ready for review`, `Needs attention`, `Sent from Outlook`, `Sent from Monday`, `Discarded`, `No draft` | Flows only |
| `eda_adviser_action` | Adviser Action | status | `Approve & send`, `Regenerate`, `Discard` (reduced by Leonardo Melman 2026-11-04). **Webhook trigger column**; reset to empty by the handler | Adviser |
| `eda_draft_text` | Draft Text | long_text | AI draft body without signature; editable — Approve & send sends this text | Generate / Adviser |
| `eda_ai_instructions` | Instructions for AI | long_text | Optional adviser input used by **Regenerate** | Adviser |
| `eda_missing_info` | Missing Information | long_text | `[[ADVISER: …]]` items | Generate |
| `eda_adviser_notes` | Notes for Adviser | long_text | Never sent. Also lists CC recipients that the reply will include | Generate |
| `eda_risk_flag` | Risk Flag | status | `None`, `Review carefully` | Generate |
| `eda_reason` | Status Detail | text | Why the item has its status — exact values in the implementation guide §3 "Status model" | Flows |
| `eda_client_profile` | Client Profile | board_relation → `5024661649` | | Intake |
| `eda_sender_email` | Sender Email | email | | Intake |
| `eda_received_at` | Received At | date | | Intake |
| `eda_original_link` | Original Email Link | link | Outlook webLink | Intake |
| `eda_draft_link` | Outlook Draft Link | link | webLink of the current draft | Generate |

### Technical columns (hidden in Adviser View)

| Column ID | Title | Type | Notes |
|---|---|---|---|
| `eda_mailbox` | Mailbox | dropdown | `rod@rsfa.co.nz` (id 1), `tech@rsfa.co.nz` (id 2) |
| `eda_confidence` | Confidence | status | `low`, `medium`, `high` |
| `eda_model` | Model / Depth | text | `<model> · <Basic|Medium|Deep>` |
| `eda_input_tokens` / `eda_output_tokens` | Input / Output Tokens | numbers | cumulative |
| `eda_gen_count` | Generation Count | numbers | |
| `eda_draft_created` | Draft Created At | date | |
| `eda_final_status_at` | Final Status At | date | |
| `eda_actioned_by` | Actioned By | people | Monday user of the last action |
| `eda_message_id` | Outlook Message ID | text | immutable ID |
| `eda_internet_msg_id` | Internet Message ID | text | duplicate key |
| `eda_conversation_id` | Conversation ID | text | |
| `eda_draft_id` | Outlook Draft ID | text | immutable ID |
| `eda_change_key` | Outlook ChangeKey | text | last version written by the agent; mismatch = edited in Outlook |
| `eda_last_run` | Last Run | link | Power Automate run URL |
| `eda_pa_run` | Power Automate Run | board_relation → `5030408927` | |

Removed on 2026-11-04 (do not reference in flows): `eda_research_depth`, `eda_reply_category`, `eda_risk_details`, `eda_edited_outlook`, `eda_edited_on_send`, `eda_adviser` (not present on re-read; assumed removed manually). Their information is either in **Status Detail** (`No edits` / `Edited before sending`) or in `Model / Depth`.

### Demo items (fictional — delete before go-live)

13 items prefixed `[DEMO]` (IDs `2899395556`–`2899395568`) created 2026-11-04 for the Rod demo. All fictional (`@example.com`, invented names, no Client Profile links, no people assigned). **Delete all `[DEMO]` items before `rod@rsfa.co.nz` is enabled.**

Webhook: not yet created (needs the HTTP URL of `Monday - Email Drafting Agent - Adviser Action Handler`). Webhook ID: TODO.

---

## 2. `⚙️ Email Drafting Agent: Mailbox Settings` (`5032291851`)

One item per mailbox; item name = mailbox address (lookup key). Group `topics` = **Mailboxes**.

| Column ID | Title | Type | Notes |
|---|---|---|---|
| `name` | Name | name | Mailbox address |
| `eds_enabled` | Enabled | status | `Yes`, `No` |
| `eds_adviser` | Adviser | people | |
| `eds_approvers` | Allowed Approvers | people | Who may use Approve & send |
| `eds_daily_cap` | Daily Draft Cap | numbers | |
| `eds_max_chars_basic` / `_medium` / `_deep` | Max Context Chars … | numbers | Technical; candidates to move to environment variables (`_deep` unused while Deep is not used) |
| `eds_tone` | Tone | long_text | Rod's prompt input |
| `eds_style` | Style | long_text | Rod's prompt input |
| `eds_other_instr` | Other Instructions | long_text | Rod's prompt input |
| `eds_signoff` | Email Signature (HTML) | long_text | Appended automatically to every draft (AUTO-EMAIL-DRAFT-001 §14.4) |
| `eds_change_note` | Last Changed Note | text | |

Removed on 2026-11-04: `eds_default_depth` (by Leonardo Melman — automatic drafts always Basic), `eds_stale_days`, `eds_model_basic`, `eds_model_medium`, `eds_model_deep`, `eds_reply_mode`. The OpenAI model is now the environment variable `rsfa_EDA_OpenAIModel`; drafts are always created as **Reply all** (`createReplyAll`).

### Items

| Item ID | Name | Enabled | Notes |
|---|---|---|---|
| `2899339258` | rod@rsfa.co.nz | **No** | Cap 20. Tone/Style/Other/Signature pending Rod (D5) |
| `2899339259` | tech@rsfa.co.nz | Yes | Test mailbox for Phase 0 only |

The fixed RSFA safety rules are in the Generate Draft flow, not on this board.

---

## 3. Change history

| Date | Change | Author |
|---|---|---|
| 2026-11-04 | Initial proposed schemas. | Claude (requested by Leonardo Melman) |
| 2026-11-04 | Both boards created in Monday with fixed column IDs, groups and two settings items. | Claude (requested by Leonardo Melman) |
| 2026-11-04 | 13 fictional `[DEMO]` items added for the Rod demo. | Claude (requested by Leonardo Melman) |
| 2026-11-04 | Simplification after review: Draft Status = 7 labels (incl. `Sent from Outlook` / `Sent from Monday`) + Status Detail; Adviser Action reduced to Approve & send / Regenerate / Discard (by Leonardo Melman); new `Instructions for AI`; deleted `eda_research_depth`, `eda_reply_category`, `eda_risk_details`, `eda_edited_outlook`, `eda_edited_on_send`; `eda_model` → Model / Depth; `eda_reason` → Status Detail; pinned **Adviser View** (`58179384`) hiding technical columns. Settings: deleted `eds_stale_days`, the three model columns and `eds_reply_mode`; `eds_signoff` → Email Signature (HTML). | Claude (requested by Leonardo Melman) |
| 2026-11-04 | `eds_default_depth` (Default Depth) removed from Mailbox Settings by Leonardo Melman: automatic drafts are always **Basic**, Regenerate is always **Medium**; Deep is not used in v1. | Claude (requested by Leonardo Melman) |
