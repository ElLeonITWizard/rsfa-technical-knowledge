# rsfa-slack-triage — read-only acceptance test

## Purpose

Confirms the skill can do its job end to end **without writing to any external system**. Re-run after connector, board or skill changes. Record each run below; never store client names, transcripts or screenshots here.

## Procedure

| # | Check | How | Pass criteria |
|---|---|---|---|
| 1 | Access to `#leo_it_tasks` | `slack_search_channels(["leo_it_tasks"], private)` → `slack_read_channel(C0895LK722Z, limit=15)` | Channel ID resolved; recent messages returned |
| 2 | Full thread retrieval | `slack_read_thread` on a Rod thread with replies | Parent + all replies, authors and times; no pagination left |
| 3 | Visual reading of screenshots | `slack_read_file` on ≥1 `image/png` from Rod | Image returned and its relevant content described (board, view, highlights) |
| 4 | Audio transcription | `slack_read_file` on an `audio/mp4` → copy to scratchpad → `python3 -I .claude/skills/transcribe-slack-audio/scripts/transcribe.py <file>` | Transcript produced (quality noted) without touching the existing skill |
| 5 | Related documentation | `grep` board/automation IDs in `knowledge/` | Canonical doc(s) located and cited |
| 6 | Monday tasks | `get_board_info(5005075773)` + `search(ITEMS)` + `get_board_items_page` (Slack Chain not empty) | Related items with status/priority/link returned |
| 7 | Action identification | Apply §6.3 to one real request | Ordered actions split into "now" vs "depends on" |
| 8 | Reply in Leo's voice | Invoke `leo-rod-slack-voice` | Skill available; one English draft consistent with verified status |
| 9 | No external writes | Review the list of tool calls made during the test | Only read tools used; nothing sent/created/updated/executed |

## Run log

### 2026-11-06 — initial run (skill creation session)

| # | Result | Evidence |
|---|---|---|
| 1 | **Passed** | `#leo_it_tasks` = `C0895LK722Z` (private, created by Rod). 15 latest messages read (2026-10-30 → 2026-11-06). Rod = `U0AJ7UV2PEG` ("Adviser Wizard"). |
| 2 | **Passed** | Thread `1793870386.457149` (SOP board / Client Profile linking): parent + 4 replies. Thread `1793739700.578679` (Pigeon replacement proposal): parent with 3 audios + 2 replies, incl. an xlsx. |
| 3 | **Passed** | `F0CF84PJ6DS` (Mortgage App/SOP board, Client Profiles relation picker with a profile highlighted and the item's empty Client Profiles cell circled) and `F0CFLREU3NG` (`Overflow Emails (old)` board showing items dated Nov 6 / "7 hours ago", arrows pointing at the board name and the item list) were opened and interpreted. |
| 4 | **Passed (quality: low)** | `F0CG63N5A56` (7 s voice note) transcribed with faster-whisper `small`, `en`, in 11 s. Output was garbled — consistent with Leo's own reply in the thread asking whether it was in Chinese. Confirms the "flag low confidence" rule. The 3 longer audios of the Pigeon thread were **not** transcribed in this run (not needed to prove the capability). |
| 5 | **Passed** | Board `5025365487` (📬 Overflow Emails (OLD)) found in `knowledge/04_MONDAY_BOARDS_REGISTRY.md` and in `AUTO-EMAIL-001` §9, where its current use is `TODO: verify`. |
| 6 | **Passed** | Board `5005075773` schema read (108 items, 15 columns). Keyword search "Overflow" returned 4 related tasks (3 Done, 1 Upcoming). 52 items have `Slack Chain` populated. `contains_text` on `link_mkw6fk9z` returned 0 results for a known permalink → local matching adopted in the skill. |
| 7 | **Passed** | Overflow (OLD) request analysed: (a) live screenshot evidence shows the board still receives items on 2026-11-06 → something still writes to it (Confirmed from screenshot); (b) docs list it as legacy with `TODO: verify` (Confirmed from documentation); (c) actions: identify which flow/scenario writes to `5025365487` (read-only: Monday board activity / automations, PA export manifests), confirm with Rod that nothing still depends on it, then prepare a change plan to stop/redirect that writer — the switch-off itself depends on those results and Rod's approval. Existing related task `Draft Plan for Not Found Overflow Emails` (Upcoming) — related, not the same work. Priority: P3/P2 (tidy-up; no reported failure). |
| 8 | **Passed** | `leo-rod-slack-voice` is installed and loads in this environment as `anthropic-skills:leo-rod-slack-voice` (personal skill, not stored in this repo). Draft produced: *"Good spot. It's still getting new emails as of today, so something is still writing to it. I'll find which flow is behind it before switching anything off and let you know."* Not sent. |
| 9 | **Passed** | Tools used: `slack_search_channels`, `slack_search_users`, `slack_read_channel`, `slack_read_thread`, `slack_read_file`, `slack_get_reactions`, Monday `get_board_info`, `search`, `get_board_items_page`, local `grep`/`sed`, local transcription. No Slack send/draft/reaction, no Monday write, no Make/PA/SharePoint call. |

**Not yet verified in a real session:** the full multi-conversation review flow one-at-a-time with Leo's follow-up commands; DM/mention scopes (`slack_read_channel` with Rod's user ID, `slack_search_public_and_private`); Make read-only lookups; any approved write path ("Creá esa tarea", "Respondé a Rod").
