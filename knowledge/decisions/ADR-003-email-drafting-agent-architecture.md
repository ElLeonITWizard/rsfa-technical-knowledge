---
id: ADR-003
title: Build the Email Drafting Agent on Email Filing (Power Automate + OpenAI) with a Monday control board
status: proposed
owner: RSFA
date: 2026-11-04
audience:
  - Authorised developers
  - Authorised technical consultants
last_modified: 2026-11-04
last_verified: "TODO: verify — pending Rod Schubert approval"
---

# ADR-003 — Email Drafting Agent architecture

## Context

Rod Schubert wants AI-prepared replies to client emails, reviewed before sending, starting with `rod@rsfa.co.nz`, with control over token spend and research depth (Basic / Medium / Deep) and configurable Tone / Style / Other instructions (Slack thread, shared in chat 2026-11-04 — historical information). Options discussed in that thread: a Microsoft Copilot assistant inside Outlook, the Make template scenario `9789700`, or extending the existing Email Filing process (`AUTO-EMAIL-001`).

Evidence:

- `AUTO-EMAIL-001` already identifies the client for every incoming email in Rod's Inbox (`Main Outlook Inbox Email Filling`, confirmed from the 2026-07-30 export), and already calls OpenAI for attachment renaming.
- Make scenario `9789700` is an inactive, unconfigured template that **sends** replies automatically (confirmed live via Make MCP, 2026-11-04).
- Copilot in Outlook drafts on demand when the adviser asks; it does not produce drafts automatically per client email, does not provide a Monday tracking board, and its access to Monday data is not established (`SYS-COPILOT-001` is an experimental POC).

## Decision (proposed)

1. Generate drafts in Power Automate, triggered from `Outlook Email Filling - Rod v2` only after the filing child confirms a client-folder match on a received email (additive response fields on `Main Outlook Inbox Email Filling`; drafting runs in an isolated scope that can never fail filing).
2. Use the OpenAI Responses API with a structured JSON output and a fixed safety system prompt; adviser tone/style rules live on a Monday settings board.
3. Output is always an Outlook **draft** (`createReply`) in the adviser's mailbox. Sending requires an explicit adviser action in Outlook or Monday (`Approve & send`).
4. A private Monday board `✉️ Email Drafting Agent: Drafts` (`5032291843`, created 2026-11-04) is part of v1 (not optional, per the 2026-11-04 request), with two-way status sync.
5. Drafting flows live in a new Solution (`RSFAEmailDraftingAgent`) separate from `RSFAOutlookEmailFilling`.
6. Make scenario `9789700` is not used.

## Consequences

- Production change to two `AUTO-EMAIL-001` flows (small, additive) — requires a fresh export and regression testing (AUTO-EMAIL-DRAFT-001 T-02).
- New processing of client email content by OpenAI — needs Rod's explicit approval (AUTO-EMAIL-DRAFT-001 D2).
- AI draft text is stored in Monday to allow editing from Monday (D1).
- New secrets must be handled through a secret store, not hardcoded as in the existing filing flows.
- Added cost (OpenAI tokens, Power Automate runs) — controlled by per-mailbox daily cap and depth.
- Rollout to other advisers becomes a configuration change (new settings item + mailbox flow scope), not a redesign.

## Alternatives considered

| Alternative | Why not chosen for v1 |
|---|---|
| Copilot assistant in Outlook | On-demand only; no automatic per-client draft, no Monday tracking/status, no controlled access to Monday context. Remains a valid complement for ad-hoc drafting |
| Make scenario `9789700` | Auto-sends; would duplicate mailbox monitoring and client matching already done by Email Filing |
| Make.com for the drafting logic, called from Power Automate | Possible, but splits one process across two platforms and still needs Outlook draft/sent tracking in Microsoft; reconsider only if Power Automate limits are hit |
| Drafts in Outlook only (concept document POC) | Simpler, but Rod asked for Monday control and depth selection in v1 |

## Related documents

- `knowledge/automations/power-automate/AUTO-EMAIL-DRAFT-001-email-drafting-agent.md`
- `knowledge/schemas/monday/BOARD-EMAIL-DRAFTS-001-email-drafting-agent-boards.md`
- `knowledge/automations/power-automate/AUTO-EMAIL-001-client-email-filing.md`
- `knowledge/decisions/ADR-001-deprecate-monday-workflows.md`

## Change history

| Date | Change | Author |
|---|---|---|
| 2026-11-04 | Proposed. | Claude (design task, requested by Leonardo Melman) |
