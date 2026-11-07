---
id: BOARD-EMAIL-DRAFTS-001
title: Email Drafting Agent — Monday board schemas
status: active (boards created, not yet used by any flow)
owner: RSFA
related_automations:
  - AUTO-EMAIL-DRAFT-001
workspace: Real Savvy_CRM (2308685)
last_modified: 2026-11-07
last_verified: 2026-11-07
---

# BOARD-EMAIL-DRAFTS-001 — Email Drafting Agent boards

**Confirmed from live system (Monday MCP, 2026-11-07):** boards created by Claude through the Monday connector at Leonardo Melman's request (2026-11-04), simplified after review, then extended on 2026-11-07 (Research Depth restored; one Drafts board per adviser). Column lists below were read back from the API. No flow writes to the boards yet (`AUTO-EMAIL-DRAFT-001` is `Planned`).

Column IDs are fixed (`eda_*` on Drafts boards, `eds_*` on Settings). **Do not rename column IDs or status labels** — the flows reference labels by text. Column titles may be changed safely. Monday does not allow re-using the ID of a deleted column, which is why some restored columns have new IDs (e.g. `eda_depth`).

## Boards

| Board | ID | URL | Mailboxes | Kind | Owners |
|---|---|---|---|---|---|
| ✉️ Email Drafting Agent: Drafts - Rod/Kathleen | `5032291843` | https://rsfa-squad.monday.com/boards/5032291843 | `rod@`, `insurance@` (Kathleen), `tech@` (testing) | private | Rod, Kathleen, RSFA IT Desk |
| ✉️ Email Drafting Agent: Drafts - Seth | `5032343560` | https://rsfa-squad.monday.com/boards/5032343560 | `seth@` (`tech@` label kept for testing) | private | Rod, Kathleen, RSFA IT Desk — **Seth to be added at his go-live** (not added yet, to avoid notifying him about an empty board) |
| ⚙️ Email Drafting Agent: Mailbox Settings | `5032291851` | https://rsfa-squad.monday.com/boards/5032291851 | all | private | Rod, Kathleen, RSFA IT Desk |

All in folder Daily Boards/Ops (`6649274`).

**Why one Drafts board per adviser (2026-11-07, Rod via Leonardo Melman):** RSFA does not have Monday Enterprise, so item-level permissions are not available; visibility is controlled per board, mirroring the `📬 Overflow Emails - Rod/Kathleen` / `- Seth` boards. The two Drafts boards are structurally identical (the Seth board was created with `duplicate_board_with_structure`; column IDs, group IDs and the Adviser View are the same), so the flows only need the target board ID, which comes from the mailbox's `Drafts Board ID` in Mailbox Settings.

---

## 1. Drafts boards (`5032291843`, `5032343560`) — identical structure

One item per client email processed by the agent. Item name = email subject (max 120 chars, `No Subject` if empty).

### Views

| Board | View ID | Name |
|---|---|---|
| Rod/Kathleen | `58179384` | Adviser View (pinned) |
| Seth | `58256574` | Adviser View (pinned) |

Adviser View shows: Received At, Draft Status, **Research Depth**, Adviser Action, Draft Text, Instructions for AI, Missing Information, Notes for Adviser, Risk Flag, Status Detail, Client Profile, Sender Email, Original Email Link, Outlook Draft Link. Technical columns are hidden. The Main Table shows everything (RSFA IT / debugging).

### Groups (same IDs on both boards)

| Group ID | Title | Statuses |
|---|---|---|
| `topics` | Needs Review | Ready for review, Needs attention |
| `group_mm8sfnf` | Processing | Processing |
| `group_mm8sta8g` | Done (Sent / Discarded) | Sent from Outlook, Sent from Monday, Discarded |
| `group_mm8s3hhz` | No Draft | No draft |

### Adviser-facing columns

| Column ID | Title | Type | Values / notes | Written by |
|---|---|---|---|---|
| `name` | Name | name | Email subject | Intake |
| `eda_draft_status` | Draft Status | status | `Processing`, `Ready for review`, `Needs attention`, `Sent from Outlook`, `Sent from Monday`, `Discarded`, `No draft` | Flows only |
| `eda_depth` | Research Depth | status | `Basic`, `Medium`, `Deep`. Set by Intake from the mailbox Default Depth; the adviser can change it and choose Regenerate | Intake / Adviser |
| `eda_adviser_action` | Adviser Action | status | `Approve & send`, `Regenerate`, `Discard`. **Webhook trigger column**; reset to empty by the handler | Adviser |
| `eda_draft_text` | Draft Text | long_text | AI draft body without signature; editable — Approve & send sends this text | Generate / Adviser |
| `eda_ai_instructions` | Instructions for AI | long_text | Optional adviser input used by Regenerate | Adviser |
| `eda_missing_info` | Missing Information | long_text | `[[ADVISER: …]]` items | Generate |
| `eda_adviser_notes` | Notes for Adviser | long_text | Never sent; lists CC recipients of the reply | Generate |
| `eda_risk_flag` | Risk Flag | status | `None`, `Review carefully` | Generate |
| `eda_reason` | Status Detail | text | Exact values in the implementation guide §0.5 | Flows |
| `eda_client_profile` | Client Profile | board_relation → `5024661649` | | Intake |
| `eda_sender_email` | Sender Email | email | | Intake |
| `eda_received_at` | Received At | date | | Intake |
| `eda_original_link` | Original Email Link | link | | Intake |
| `eda_draft_link` | Outlook Draft Link | link | | Generate |

### Technical columns (hidden in Adviser View)

| Column ID | Title | Type | Notes |
|---|---|---|---|
| `eda_mailbox` | Mailbox | dropdown | Rod/Kathleen board: `rod@rsfa.co.nz`, `tech@rsfa.co.nz`, `insurance@rsfa.co.nz`. Seth board: `seth@rsfa.co.nz`, `tech@rsfa.co.nz` |
| `eda_confidence` | Confidence | status | `low`, `medium`, `high` |
| `eda_model` | Model / Depth | text | Model and depth actually used, e.g. `gpt-4o-mini · Basic` |
| `eda_input_tokens` / `eda_output_tokens` | Input / Output Tokens | numbers | cumulative |
| `eda_gen_count` | Generation Count | numbers | |
| `eda_draft_created` | Draft Created At | date | |
| `eda_final_status_at` | Final Status At | date | |
| `eda_actioned_by` | Actioned By | people | |
| `eda_message_id` | Outlook Message ID | text | immutable ID |
| `eda_internet_msg_id` | Internet Message ID | text | duplicate key |
| `eda_conversation_id` | Conversation ID | text | |
| `eda_draft_id` | Outlook Draft ID | text | immutable ID |
| `eda_change_key` | Outlook ChangeKey | text | mismatch = edited in Outlook |
| `eda_last_run` | Last Run | link | |
| `eda_pa_run` | Power Automate Run | board_relation → `5030408927` | |

Deleted columns (IDs reserved by Monday, never reference): `eda_research_depth` (replaced by `eda_depth`), `eda_reply_category`, `eda_risk_details`, `eda_edited_outlook`, `eda_edited_on_send`, `eda_adviser`.

### Demo items (fictional — delete before go-live)

13 items prefixed `[DEMO]` on the Rod/Kathleen board (IDs `2899395556`–`2899395568`), fictional data only. **Delete before `rod@` is enabled.** The Seth board has no items.

Webhooks: one per Drafts board, both pointing to `Monday - Email Drafting Agent - Adviser Action Handler` — not yet created. Webhook IDs: TODO.

---

## 2. `⚙️ Email Drafting Agent: Mailbox Settings` (`5032291851`)

One item per mailbox; item name = mailbox address (lookup key). Group `topics` = **Mailboxes**.

| Column ID | Title | Type | Notes |
|---|---|---|---|
| `name` | Name | name | Mailbox address |
| `eds_enabled` | Enabled | status | `Yes`, `No` |
| `eds_drafts_board` | Drafts Board ID | text | Target Drafts board for this mailbox |
| `eds_adviser` | Adviser | people | |
| `eds_approvers` | Allowed Approvers | people | Who may use Approve & send |
| `eds_depth_default` | Default Depth | status | `Basic`, `Medium`, `Deep` — Research Depth of automatic drafts |
| `eds_model_lvl_basic` / `eds_model_lvl_medium` / `eds_model_lvl_deep` | Model Basic / Medium / Deep | text | OpenAI model per Research Depth |
| `eds_daily_cap` | Daily Draft Cap | numbers | |
| `eds_max_chars_basic` / `_medium` / `_deep` | Max Context Chars … | numbers | Context size limit per depth |
| `eds_tone` | Tone | long_text | |
| `eds_style` | Style | long_text | |
| `eds_other_instr` | Other Instructions | long_text | |
| `eds_signoff` | Email Signature (HTML) | long_text | Appended automatically to every draft |
| `eds_change_note` | Last Changed Note | text | |

Deleted columns (IDs reserved): `eds_default_depth` (replaced by `eds_depth_default`), `eds_model_basic`/`_medium`/`_deep` (replaced by `eds_model_lvl_*`), `eds_stale_days`, `eds_reply_mode`.

### Items

| Item ID | Name | Enabled | Drafts board | Notes |
|---|---|---|---|---|
| `2899339258` | rod@rsfa.co.nz | **No** | `5032291843` | Basic default; models `gpt-4o-mini` / `gpt-4o` / `gpt-4o` (initial values — Deep should get the strongest model chosen in testing). Tone/Style/Signature pending Rod |
| `2902028951` | insurance@rsfa.co.nz | **No** | `5032291843` | Kathleen's mailbox (`Case_Kathleen` in `Main` uses `insurance@`). Adviser/approvers/prompt pending |
| `2902028952` | seth@rsfa.co.nz | **No** | `5032343560` | Adviser/approvers/prompt pending; add Seth to his Drafts board at go-live |
| `2899339259` | tech@rsfa.co.nz | Yes | `5032291843` | Test mailbox for Phase 0 only |

People columns were left empty on the new items so nobody was notified.

---

## 3. Change history

| Date | Change | Author |
|---|---|---|
| 2026-11-04 | Initial schemas; boards created; demo items added; board simplified after review (7 statuses + Status Detail, 3 adviser actions, Instructions for AI, Adviser View, automatic signature, Reply all). | Claude (requested by Leonardo Melman) |
| 2026-11-07 | **Research Depth restored** at Rod's request: `eda_depth` on Drafts boards, `eds_depth_default` and `eds_model_lvl_basic/medium/deep` on Settings (new IDs — Monday reserves deleted IDs); demo items and Adviser View updated. **One Drafts board per adviser:** existing board renamed `… - Rod/Kathleen`, new `✉️ Email Drafting Agent: Drafts - Seth` (`5032343560`) duplicated with identical structure; `eds_drafts_board` added to Settings; items `insurance@` and `seth@` created disabled; Mailbox dropdown labels updated. | Claude (requested by Leonardo Melman) |
