---
solution_unique_name: RSFAOutlookEmailFilling
solution_display_name: SP Email Filling
solution_version: 1.0.0.3
publisher_unique_name: Crf20c5
publisher_display_name: CDS Default Publisher
export_type: unmanaged
source_environment: Unknown — verify
exported_at: Unknown — verify
source_zip: ../../source-zips/RSFAOutlookEmailFilling_1_0_0_3.zip
snapshot_status: current-export-snapshot
last_inspected: 2026-07-30
inspection_method:
  - standard ZIP extraction
related_automations:
  - AUTO-EMAIL-001
  - AUTO-EMAIL-BACKUP-001
related_flows:
  - Main Outlook Inbox Email Filling
  - Outlook INBOX items email filing (Rod)
  - Outlook INBOX items email filing (Kathleen)
  - Sent Emails Control
  - OLD Outlook SENT Email Filling - Jet v2
  - Outlook Email Filling - Jet v2
  - Outlook SENT Email Filling - Rod v2
  - Outlook SENT Email Filling - Kathleen v2
  - Outlook Email Filing - Support v2
  - Outlook Email Filling - Kathleen v2
  - Outlook Email Filling - Rod v2
  - Outlook SENT Email Filling - Support v2
  - Email Filling Failed Items Processing
  - Overflow Emails Contact Matching
  - Overflow Emails Related Client Profile Change
---

# SP Email Filling

## Purpose

Largest Solution in this export set: the full mailbox-specific and shared Outlook email-filing family, including the central `Main Outlook Inbox Email Filling` child flow, per-adviser INBOX/SENT flows, overflow matching/reprocessing flows, and the scheduled failed-item recovery flow. Corresponds primarily to `AUTO-EMAIL-001`, with one flow (`Email Filling Failed Items Processing`) belonging to `AUTO-EMAIL-BACKUP-001`.

## Export identity

- **Unique Name:** `RSFAOutlookEmailFilling`
- **Display Name:** `SP Email Filling` (note: the Solution's own display name does not match the "Outlook Email Filing" naming used by the flows or registry — a labeling inconsistency at the Solution-container level only, not a flow-naming issue)
- **Version:** `1.0.0.3`
- **Publisher:** `Crf20c5` (`CDS Default Publisher`)
- **Managed:** No (unmanaged export)

## Source ZIP

`../../source-zips/RSFAOutlookEmailFilling_1_0_0_3.zip` — SHA-256 recorded in `current/checksums.sha256`, verified identical to `current/unmanaged.zip`.

## Included cloud flows

| Exact flow name | Workflow ID | Flow type | State from export | Primary trigger | Related canonical automation | Evidence status |
|---|---|---|---|---|---|---|
| Main Outlook Inbox Email Filling | `f6906da4-c8ed-ef11-9341-6045bd3ce9ae` | Cloud flow | Activated | `manual` — HTTP Request (child-flow invocation) | `AUTO-EMAIL-001` | Confirmed from export and canonical documentation — exact name match |
| Outlook INBOX items email filing (Rod) | `921a3139-e5da-ef11-8eea-00224814e0ff` | Cloud flow | **Draft (not activated)** | `When_a_new_email_arrives_(V3)` (Office 365 Outlook, OpenApiConnectionNotification) | `AUTO-EMAIL-001` (candidate) | Unmapped — review required. Not listed under this exact name in `knowledge/03_AUTOMATION_REGISTRY.md` §5; distinct from the registered `Outlook Email Filling - Rod v2` |
| Outlook INBOX items email filing (Kathleen) | `941a3139-e5da-ef11-8eea-00224814e0ff` | Cloud flow | **Draft (not activated)** | `When_a_new_email_arrives_(V3)` | `AUTO-EMAIL-001` (candidate) | Unmapped — review required. Same as above, for Kathleen |
| Sent Emails Control | `32f10b1d-b79c-f011-bbd2-000d3ae0ae9d` | Cloud flow | **Draft (not activated)** | `manual` — HTTP Request | — | Unmapped — review required. Not present in the current registry under any name |
| OLD Outlook SENT Email Filling - Jet v2 | `80273d77-b79c-f011-bbd2-000d3ae0ae9d` | Cloud flow | Activated | `When_a_new_email_arrives_(V3)` | `AUTO-EMAIL-001` | Confirmed from export and canonical documentation — exact name match; registry flags this flow `Active - Planned Retirement` |
| Outlook Email Filling - Jet v2 | `d30599eb-ec37-f011-8c4d-6045bd4096fa` | Cloud flow | Activated | `When_a_new_email_arrives_(V3)` | `AUTO-EMAIL-001` | Likely mapping — registry lists this flow as `Outlook Email Filing - Jet v2` ("Filing"); export spells it `Filling`. Same spelling conflict as the Kathleen/Rod flows below |
| Outlook SENT Email Filling - Rod v2 | `d2d40c71-dbf9-ef11-bae2-6045bd4096fa` | Cloud flow | Activated | `When_a_new_email_arrives_(V3)` | `AUTO-EMAIL-001` | Confirmed from export and canonical documentation — exact name match |
| Outlook SENT Email Filling - Kathleen v2 | `5d50f6af-affa-ef11-bae2-6045bd4096fa` | Cloud flow | Activated | `When_a_new_email_arrives_(V3)` | `AUTO-EMAIL-001` | Confirmed from export and canonical documentation — exact name match |
| Outlook Email Filing - Support v2 | `ca963563-abfb-ef11-bae3-6045bd4096fa` | Cloud flow | Activated | `When_a_new_email_arrives_(V3)` | `AUTO-EMAIL-001` | Confirmed from export and canonical documentation — exact name match |
| Outlook Email Filling - Kathleen v2 | `360d1f29-5bf8-ef11-bae2-002248185f06` | Cloud flow | Activated | `When_a_new_email_arrives_(V3)` | `AUTO-EMAIL-001` | Likely mapping — registry lists `Outlook Email Filing - Kathleen v2` ("Filing"); export spells it `Filling`. Conflict — verification required to confirm this is the same flow and not a duplicate/parallel one |
| Outlook Email Filling - Rod v2 | `d34b8f51-46f8-ef11-bae2-002248185f06` | Cloud flow | Activated | `When_a_new_email_arrives_(V3)` | `AUTO-EMAIL-001` | Likely mapping — same "Filing" vs "Filling" conflict as above |
| Outlook SENT Email Filling - Support v2 | `816b9f65-6237-f011-8c4d-6045bd4096fa` | Cloud flow | **Draft (not activated)** | `When_a_new_email_arrives_in_a_shared_mailbox_(V2)` (OpenApiConnection — a different trigger operation than the `(V3)` used elsewhere) | `AUTO-EMAIL-001` (candidate) | Unmapped — review required. Registry does not list a SENT-side flow for Support |
| Email Filling Failed Items Processing | `04531fc5-dced-ef11-9341-6045bd3ce9ae` | Cloud flow | Activated | `Recurrence` (scheduled) | `AUTO-EMAIL-BACKUP-001` | Confirmed from export and canonical documentation — exact name match |
| Overflow Emails Contact Matching | `6bf7b40c-b29c-f011-bbd2-000d3ae0ae9d` | Cloud flow | Activated | `manual` — HTTP Request | `AUTO-EMAIL-001` | Confirmed from export and canonical documentation — exact name match |
| Overflow Emails Related Client Profile Change | `03b8f6d7-66af-f011-bbd3-000d3ae0ae9d` | Cloud flow | Activated | `manual` — HTTP Request | `AUTO-EMAIL-001` | Confirmed from export and canonical documentation — exact name match |

"State from export" reflects this snapshot only; a flow shown here as Draft/off may since have been activated (or vice versa) in the live environment — `TODO: verify from live system`.

**Flow present in the registry but absent from this export:** `Overflow Emails Suggested Match Approval` (listed in `knowledge/03_AUTOMATION_REGISTRY.md` §5 as part of `AUTO-EMAIL-001`) does not appear anywhere in this Solution. Either it lives in a different Solution not covered by this export set, the export is incomplete, or the flow has since been removed/renamed. **Conflict — verification required.**

## Other included components

None beyond the 15 cloud flows listed above (no apps, tables, or non-flow workflows).

## Connection references

| Logical name | Display name | Connector |
|---|---|---|
| `cr3e8_Outlook_Jet_RSFA` | Outlook_Jet_RSFA | `shared_office365` |
| `cr3e8_Outlook_Jet_RSFA_02` | Outlook_Jet_RSFA_02 | `shared_office365` |
| `cr3e8_Outlook_Seth_RSFA` | Outlook_Seth_RSFA | `shared_office365` |
| `cr3e8_sharedoffice365_591c0` | Outlook_Tech_RSFA | `shared_office365` |
| `cr3e8_sharedsharepointonline_23323` | SP Tech RSFA 02 | `shared_sharepointonline` |
| `cr3e8_Slack_RSFA` | Slack_RSFA | `shared_slack` |
| `new_sharedoffice365_4ebbe` | Outlook_Support_RSFA | `shared_office365` |
| `new_sharedoffice365_89be1` | Outlook_Tech_RSFA_02 | `shared_office365` |
| `new_sharedwordonlinebusiness_5aa2e` | Word Online (Business) | `shared_wordonlinebusiness` |
| `rsfa_sharedoffice365_326a9` | **Outlook_Insurance_RSFA** | `shared_office365` |
| `rsfa_sharedoffice365_91c50` | Outlook_Rod_RSFA | `shared_office365` |
| `rsfa_sharedsharepointonline_8fd5d` | SharePoint RSFAActiveAutomations-8fd5d | `shared_sharepointonline` |
| `rsfa_sharedslack_c50e1` | Slack RSFAActiveAutomations-c50e1 | `shared_slack` |
| `rsfa_SharePointConnection` | SharePoint Connection | `shared_sharepointonline` |

Connection **owners** are not recorded in an unmanaged export — `TODO: verify` against the live environment. Which specific workflow calls which specific connection reference was not individually traced for every flow in this pass (14 connection references across 15 flows) — `TODO: verify` per-flow connector usage if needed for a specific investigation.

**Notable finding — `Outlook_Insurance_RSFA` connection reference:** this Solution references an Outlook connection for an "Insurance" mailbox. `knowledge/automations/power-automate/AUTO-EMAIL-001-client-email-filing.md` §4 currently lists only Rod, Kathleen, Seth, Jet and Support as monitored mailboxes — **Insurance is not currently listed**. `knowledge/06_NAMING_AND_ID_CONVENTIONS.md` §16 does list `insurance@rsfa.co.nz` as a known RSFA account, which corroborates that this mailbox exists, but no automation document currently describes it as part of the email-filing family. **Conflict/gap — flagged here and in `solution-inventory.md`; not silently resolved.** Requires live verification of whether an Insurance-mailbox email-filing flow is active and, if so, updating `AUTO-EMAIL-001`.

**Notable finding — `Word Online (Business)` connection reference:** present in this Solution but its usage was not traced to a specific action in this pass. `AUTO-EMAIL-001` does not currently document any Word-document generation step. `TODO: verify` what this connector is used for.

## Environment variables

None present in this Solution export.

**Security finding:** the following flows contain **hardcoded HTTP Authorization headers with literal API credentials** (a Monday.com API bearer token, and — in three flows — an OpenAI API key) instead of a Connection Reference or Environment Variable:

| Flow | Hardcoded Monday token occurrences | Hardcoded OpenAI key occurrences |
|---|---:|---:|
| Main Outlook Inbox Email Filling | 9 | 3 |
| Outlook INBOX items email filing (Rod) | 4 | 0 |
| Outlook INBOX items email filing (Kathleen) | 4 | 0 |
| Overflow Emails Contact Matching | 4 | 1 |
| Overflow Emails Related Client Profile Change | 1 | 0 |

Both literal values have been redacted in the unpacked copies stored in this repository (replaced with `REDACTED-SEE-1PASSWORD-MONDAY-API-TOKEN` / `REDACTED-SEE-1PASSWORD-OPENAI-API-KEY`). The original `current/unmanaged.zip` and `../../source-zips/RSFAOutlookEmailFilling_1_0_0_3.zip` still contain these values in plaintext because they are preserved byte-for-byte for integrity/checksum purposes. **Both credentials should be treated as exposed and rotated as soon as possible; do not distribute either zip file outside this repository's authorised access until rotation is confirmed.** This is the same Monday.com token and the same OpenAI key found in the other three Solutions in this export set — i.e. one shared, reused credential pair hardcoded across multiple flows and Solutions, which increases the blast radius of a single rotation.

## Custom connectors

None confirmed. Monday.com is called via generic HTTP actions to `https://api.monday.com/v2` (and `/v2/file`), not via a registered custom connector.

## Dependencies

- Contacts and Client Profiles boards (Monday.com) must have accurate Primary/Secondary email values for matching to succeed.
- SharePoint client folder must already exist (`AUTO-SP-FOLDER-001`) for direct filing to succeed.
- Overflow Emails boards (Rod/Kathleen, Seth, Jet, OLD) as reprocessing/notification targets.
- Real Savvy Ref Outlook Add-in for the forced-match subject convention (not verifiable from this export; referenced only in canonical documentation).

## Related canonical automations

- `AUTO-EMAIL-001` — Client Email Filing and Overflow Processing (primary; 13 of 15 flows in this Solution)
- `AUTO-EMAIL-BACKUP-001` — Email Backup and Failed Item Recovery (`Email Filling Failed Items Processing` only)

## Canonical documentation references

- `knowledge/automations/power-automate/AUTO-EMAIL-001-client-email-filing.md`
- `knowledge/automations/power-automate/AUTO-EMAIL-BACKUP-001-email-backup-recovery.md`
- `knowledge/03_AUTOMATION_REGISTRY.md` §3, §5
- `source-material/power-automate/Outlook Email Filing to SharePoint.md`

## Inspection and validation

- Unpack method: standard ZIP extraction.
- PAC CLI unpack validation: not performed (PAC CLI not available in this environment).
- Checksum generated and verified against `source-zips/RSFAOutlookEmailFilling_1_0_0_3.zip` (identical).

## Security review

- **Finding:** hardcoded Monday.com API bearer token and OpenAI API key found across 5 of 15 flows (see table above). Redacted in the unpacked copy stored here; original zip copies still contain them in plaintext. **Recommend rotating both credentials immediately** and migrating these flows to Connection References / Environment Variables.
- No client financial, insurance or identification content found embedded in the flow definitions themselves.
- No other hardcoded secrets found after a full-text sweep for `authorization`, `bearer`, `api key`, `secret`, `password`, `access_token` patterns.

## Known gaps

- Five flows in this export (`Outlook INBOX items email filing (Rod)`, `Outlook INBOX items email filing (Kathleen)`, `Sent Emails Control`, `Outlook SENT Email Filling - Support v2`, and by spelling, three "Filling" vs "Filing" flows) are either entirely absent from the current Automation Registry or present only under a differently-spelled name. None of this has been silently resolved — see per-flow notes in the table above.
- `Overflow Emails Suggested Match Approval` is registered as part of `AUTO-EMAIL-001` but is absent from this export entirely.
- `Outlook_Insurance_RSFA` connection reference suggests an undocumented Insurance mailbox in the email-filing family — not reflected in `AUTO-EMAIL-001`.
- `Word Online (Business)` connector usage is unconfirmed.
- Four flows are shown as Draft/not-activated in this snapshot; live state must be confirmed separately, especially for `Outlook INBOX items email filing (Rod)`/`(Kathleen)`, which — if these turn out to be work-in-progress replacements for the existing `v2` flows — would be materially relevant to understanding the current email-filing architecture.
- Per-flow connection-reference usage (which of the 14 references each of the 15 flows actually calls) was not individually traced.
- `source_environment` and `exported_at` are unknown.

## Change history

| Date | Change | Author |
|---|---|---|
| 2026-07-30 | Initial manifest created from `RSFAOutlookEmailFilling_1_0_0_3.zip` export inspection. | Claude (documentation task) |
