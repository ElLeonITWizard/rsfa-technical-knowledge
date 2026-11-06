# Proposal — persistent tracking of triaged conversations

**Status:** Proposal only. Nothing described here has been created. Each option requires Leo's explicit approval before implementation.

## Problem

Each Claude Code conversation starts without memory of the previous triage. Reviews by time window therefore repeat conversations already handled, and "mark as resolved for next review" only lasts for the current session.

## Options

| Option | How it works | Pros | Cons / risks |
|---|---|---|---|
| A. Slack reaction convention | Leo (or Claude, after approval) adds a fixed reaction, e.g. ✅ = resolved, 👀 = in progress, on the parent message. Triage reads reactions via `slack_get_reactions`. | No new storage; visible to Rod; Leo already uses ✅ / 📝 informally. | Writing a reaction is an external write (needs approval each time, or a standing authorisation). Rod sees it. Meaning must be agreed. |
| B. Monday `Slack Chain` as the index | Every thread that becomes work gets a task with `Slack Chain` set; triage treats threads linked to a `Done` task as resolved. | Uses the existing board and column; no new structure. | Only covers threads that became tasks; informational/reply-only threads still repeat. |
| C. Local, git-ignored triage log | A file in the scratchpad or a git-ignored path storing `channel_id, ts, state, date`. | Simple; private. | Cloud containers are ephemeral — the file is lost between sessions unless stored elsewhere. Not recommended in this environment. |
| D. Make data store | A small data store keyed by thread `ts` with state and date, read/written through Make MCP tools. | Persistent and queryable across sessions. | New storage in a production platform; needs design, approval and documentation (`CLAUDE.md` §12/§14). |

## Recommendation

Combine **B** (already in place; no change needed) with **A** after Leo and Rod agree on reaction meanings — ideally with a standing authorisation for that single reaction type only. Revisit **D** only if A+B prove insufficient.
