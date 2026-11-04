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

**Confirmed from live system (Monday MCP, 2026-11-04):** both boards were created on 2026-11-04 by Claude through the Monday connector, at Leonardo Melman's request, and the column set below was read back from the API after creation. No flow writes to them yet (`AUTO-EMAIL-DRAFT-001` is `Planned`).

Column IDs were set explicitly (`eda_*` on Drafts, `eds_*` on Settings) so the flows are readable. **Do not rename column IDs or status labels** — the flows reference labels by text. Column titles may be changed safely.

| Board | ID | URL | Folder | Kind | Owners |
|---|---|---|---|---|---|
| ✉️ Email Drafting Agent: Drafts | `5032291843` | https://rsfa-squad.monday.com/boards/5032291843 | Daily Boards/Ops (`6649274`) | private | Rod Schubert (`46751134`), RSFA IT Desk (`46759817`) — owners requested on creation; TODO: verify in board permissions |
| ⚙️ Email Drafting Agent: Mailbox Settings | `5032291851` | https://rsfa-squad.monday.com/boards/5032291851 | Daily Boards/Ops (`6649274`) | private | same |

---

## 1. `✉️ Email Drafting Agent: Drafts` (`5032291843`)

One item per client email processed by the agent. Item name = email subject (max 120 chars, `No Subject` if empty).

### Groups

| Group ID | Title | Used for |
|---|---|---|
| `topics` | Needs Review | Ready for review, Needs attention |
| `group_mm8sfnf` | Processing | Processing |
| `group_mm8sta8g` | Done (Sent / Discarded) | Sent, Discarded |
| `group_mm8s3hhz` | No Draft | No draft |

### Columns

| Column ID | Title | Type | Labels / notes | Written by |
|---|---|---|---|---|
| `name` | Name | name | Email subject | Intake |
| `eda_draft_status` | Draft Status | status | `Processing`, `Ready for review`, `Needs attention`, `Sent`, `Discarded`, `No draft` (simplified 2026-11-04; cause in Status Detail) | Flows only |
| `eda_adviser_action` | Adviser Action | status | `Approve & send`, `Update Outlook draft`, `Regenerate - more context` (Medium), `Regenerate - deep research` (Deep), `Discard`. **Webhook trigger column**; reset to empty by the handler | Adviser |
| `eda_client_profile` | Client Profile | board_relation → `5024661649` | | Intake |
| `eda_mailbox` | Mailbox | dropdown | `rod@rsfa.co.nz` (id 1), `tech@rsfa.co.nz` (id 2) | Intake |
| `eda_adviser` | Adviser | people | | Intake |
| `eda_sender_email` | Sender Email | email | | Intake |
| `eda_received_at` | Received At | date | NZT | Intake |
| `eda_original_link` | Original Email Link | link | Outlook webLink | Intake |
| `eda_draft_link` | Outlook Draft Link | link | Outlook webLink of the current draft | Generate |
| `eda_draft_text` | Draft Text | long_text | Editable by the adviser (Decision D1) | Generate / Adviser |
| `eda_missing_info` | Missing Information | long_text | | Generate |
| `eda_adviser_notes` | Notes for Adviser | long_text | Never sent | Generate |
| `eda_reply_category` | Reply Category | status | `information_request`, `document_sent`, `complaint`, `scheduling`, `thanks_ack`, `other`, `advice_request` (same values as the AI JSON enum) | Generate |
| `eda_risk_flag` | Risk Flag | status | `None`, `Review carefully` | Generate |
| `eda_risk_details` | Risk Details | text | | Generate |
| `eda_confidence` | Confidence | status | `low`, `medium`, `high` | Generate |
| `eda_edited_outlook` | Edited in Outlook | status | `No`, `Yes` | Reconciliation |
| `eda_edited_on_send` | Edited Before Send | status | `No`, `Yes`, `Unknown` | Sent Items Sync |
| `eda_reason` | Status Detail | text | Why the item has its status — exact values in the implementation guide §3 "Status model" | Flows |
| `eda_model` | Model / Depth | text | `<model> · <Basic|Medium|Deep>`, e.g. `gpt-4o · Basic` | Generate |
| `eda_input_tokens` | Input Tokens | numbers | cumulative | Generate |
| `eda_output_tokens` | Output Tokens | numbers | cumulative | Generate |
| `eda_gen_count` | Generation Count | numbers | | Generate |
| `eda_draft_created` | Draft Created At | date | | Generate |
| `eda_final_status_at` | Final Status At | date | | Flows |
| `eda_actioned_by` | Actioned By | people | | Action Handler |
| `eda_message_id` | Outlook Message ID | text | immutable ID | Intake |
| `eda_internet_msg_id` | Internet Message ID | text | duplicate key | Intake |
| `eda_conversation_id` | Conversation ID | text | | Intake |
| `eda_draft_id` | Outlook Draft ID | text | immutable ID | Generate |
| `eda_change_key` | Outlook ChangeKey | text | last version written by the agent | Generate |
| `eda_last_run` | Last Run | link | | Flows |
| `eda_pa_run` | Power Automate Run | board_relation → `5030408927` | | Flows |

### Demo items (fictional — delete before go-live)

13 items prefixed `[DEMO]` were created on 2026-11-04 (IDs `2899395556`–`2899395568`) to show Rod the board. All data is fictional (`@example.com` senders, invented names, no Client Profile links, no people assigned so nobody was notified). After the 2026-11-04 simplification they cover all six statuses: Ready for review (incl. two `Review carefully` cases — advice request and complaint — and one `Edited in Monday` detail), Needs attention (edited in Outlook; AI unavailable), Sent (from Outlook; from Monday), Discarded (replaced by newer email; deleted in Outlook) and No draft (no reply needed; automatic message; sender not a client contact). **Delete all `[DEMO]` items before `rod@rsfa.co.nz` is enabled**, so they do not count towards the daily cap or appear in metrics.

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
| `eds_default_depth` | Default Depth | status | `Basic`, `Medium`, `Deep` |
| `eds_daily_cap` | Daily Draft Cap | numbers | |
| `eds_model_basic` / `eds_model_medium` / `eds_model_deep` | Model Basic / Medium / Deep | text | |
| `eds_max_chars_basic` / `eds_max_chars_medium` / `eds_max_chars_deep` | Max Context Chars … | numbers | |
| `eds_reply_mode` | Reply Mode | status | `Reply`, `Reply all` |
| `eds_tone` | Tone | long_text | Rod's prompt input |
| `eds_style` | Style | long_text | Rod's prompt input |
| `eds_other_instr` | Other Instructions | long_text | Rod's prompt input |
| `eds_signoff` | Sign-off | long_text | Outlook signature is not added to drafts created via Graph — TODO: verify T-01 |
| `eds_stale_days` | Stale After (days) | numbers | Not used since the 2026-11-04 status simplification (no Stale status) — candidate for deletion |
| `eds_change_note` | Last Changed Note | text | |

### Items created 2026-11-04

| Item ID | Name | Enabled | Notes |
|---|---|---|---|
| `2899339258` | rod@rsfa.co.nz | **No** | Basic, cap 20, models `gpt-4o` (initial value, to confirm in T-20), 12k/24k/40k chars, Reply, stale 14. Tone/Style/Other/Sign-off empty — pending Rod (D5) |
| `2899339259` | tech@rsfa.co.nz | Yes | Test mailbox for Phase 0 only. Cap 50, placeholder tone/style |

The fixed RSFA safety rules are in the Generate Draft flow, not on this board, so they cannot be removed by editing it.

---

## 3. Change history

| Date | Change | Author |
|---|---|---|
| 2026-11-04 | Initial proposed schemas. | Claude (design task, requested by Leonardo Melman) |
| 2026-11-04 | Both boards created in Monday (private, Real Savvy_CRM › Daily Boards/Ops) with fixed column IDs, groups and two settings items; schema read back from the API. Board names made explicit (`Email Drafting Agent: …`) at Leonardo Melman's request. | Claude (requested by Leonardo Melman) |
| 2026-11-04 | Added 13 fictional `[DEMO]` items to the Drafts board for the Rod demo (to be deleted before go-live). | Claude (requested by Leonardo Melman) |
| 2026-11-04 | Simplified Draft Status to 6 labels; renamed `eda_reason` → Status Detail and `eda_model` → Model / Depth; Adviser Action now has `Regenerate - more context` / `Regenerate - deep research`; **deleted column `eda_research_depth` (Research Depth)** at Leonardo Melman's request; groups renamed `Done (Sent / Discarded)` and `No Draft`; demo items migrated. | Claude (requested by Leonardo Melman) |
