---
solution_unique_name: DocuSigntoSharePoint
solution_display_name: DocuSign to SharePoint
solution_version: 1.0.0.2
publisher_unique_name: Crf20c5
publisher_display_name: CDS Default Publisher
export_type: unmanaged
source_environment: Unknown — verify
exported_at: Unknown — verify
source_zip: ../../source-zips/DocuSigntoSharePoint_1_0_0_2.zip
snapshot_status: current-export-snapshot
last_inspected: 2026-07-30
inspection_method:
  - standard ZIP extraction
related_automations:
  - AUTO-DOCUSIGN-001
related_flows:
  - "DocuSign to SharePoint "
---

# DocuSign to SharePoint

## Purpose

Single-flow Solution that detects a completed DocuSign envelope, matches the signer to a Monday.com record, and files the signed document(s) into the client's SharePoint folder, notifying support via Slack. Corresponds to the canonical automation `AUTO-DOCUSIGN-001`.

## Export identity

- **Unique Name:** `DocuSigntoSharePoint`
- **Display Name:** `DocuSign to SharePoint` (the underlying flow's exact name in `customizations.xml` has a trailing space: `"DocuSign to SharePoint "`)
- **Version:** `1.0.0.2`
- **Publisher:** `Crf20c5` (`CDS Default Publisher`)
- **Managed:** No (unmanaged export)

## Source ZIP

`../../source-zips/DocuSigntoSharePoint_1_0_0_2.zip` — SHA-256 recorded in `current/checksums.sha256`, verified identical to `current/unmanaged.zip`.

## Included cloud flows

| Exact flow name | Workflow ID | Flow type | State from export | Primary trigger | Related canonical automation | Evidence status |
|---|---|---|---|---|---|---|
| `DocuSign to SharePoint ` | `911a3139-e5da-ef11-8eea-00224814e0ff` | Cloud flow (Category 5) | Activated (StateCode 1) | DocuSign — `When_an_envelope_status_changes_(Connect)_(V3)`, filtered to `envelope-completed` (OpenApiConnectionWebhook) | `AUTO-DOCUSIGN-001` | Confirmed from export and canonical documentation |

"State from export" reflects this snapshot only and is not a live-production confirmation.

## Other included components

None. This Solution contains exactly one Root Component (the flow above); no apps, tables, or other workflows.

## Connection references

| Logical name | Display name | Connector | State (export) |
|---|---|---|---|
| `cr3e8_Slack_RSFA` | Slack_RSFA | `shared_slack` | statecode 0 / statuscode 1 (as exported) |
| `new_sharedoffice365_89be1` | Outlook_Tech_RSFA_02 | `shared_office365` | statecode 0 / statuscode 1 |
| `rsfa_shareddocusign_c7609` | Docusign RSFAActiveAutomations-c7609 | `shared_docusign` | statecode 0 / statuscode 1 |
| `rsfa_sharedsharepointonline_8fd5d` | SharePoint RSFAActiveAutomations-8fd5d | `shared_sharepointonline` | statecode 0 / statuscode 1 |

Connection **owners** are not recorded in an unmanaged export — `TODO: verify` against the live environment.

## Environment variables

None present in this Solution export (no `environmentvariabledefinitions` or `environmentvariablevalues` components).

**Security finding:** Monday.com and OpenAI access in this flow's action definitions is implemented with **hardcoded HTTP Authorization headers containing literal API credentials**, not via a Connection Reference or Environment Variable. Both literal values have been redacted in the unpacked copy stored in this repository (replaced with `REDACTED-SEE-1PASSWORD-MONDAY-API-TOKEN` and `REDACTED-SEE-1PASSWORD-OPENAI-API-KEY`). The original `current/unmanaged.zip` and `../../source-zips/DocuSigntoSharePoint_1_0_0_2.zip` still contain these values in their original, unredacted form because they are preserved byte-for-byte for integrity/checksum purposes. **Both credentials should be treated as exposed and rotated as soon as possible; do not distribute either zip file outside this repository's authorised access until rotation is confirmed.**

## Custom connectors

None confirmed. Monday.com and OpenAI are called via generic HTTP actions to `https://api.monday.com/v2` and an OpenAI endpoint respectively, not via a registered custom connector.

## Dependencies

- DocuSign connection must remain valid for the webhook trigger to fire.
- Monday.com record must have the signer's email in a searchable field for matching to succeed (per `AUTO-DOCUSIGN-001` §9, exact board is not confirmed even from this export — the flow calls the Monday API directly over HTTP rather than through a bound board/column reference visible in the connection references).
- SharePoint connection for document upload.
- Slack connection for notifications.

## Related canonical automations

`AUTO-DOCUSIGN-001` — DocuSign Signed Document Filing (`knowledge/automations/power-automate/AUTO-DOCUSIGN-001-docusign-filing.md`). Flow name and trigger behaviour in this export are consistent with the documented automation.

## Canonical documentation references

- `knowledge/automations/power-automate/AUTO-DOCUSIGN-001-docusign-filing.md`
- `knowledge/03_AUTOMATION_REGISTRY.md` §3, §5
- `source-material/power-automate/DocuSign to SharePoint Workflow.md`

## Inspection and validation

- Unpack method: standard ZIP extraction.
- PAC CLI unpack validation: not performed (PAC CLI not available in this environment — `pac --version` returned "command not found").
- Checksum generated and verified against `source-zips/DocuSigntoSharePoint_1_0_0_2.zip` (identical).

## Security review

- **Finding:** Hardcoded Monday.com API bearer token and OpenAI API key found directly in the flow's action definitions (not in an Environment Variable). Redacted in the unpacked copy stored here; original zip copies still contain them in plaintext. **Recommend rotating both credentials immediately** and migrating this flow to use Connection References / Environment Variables instead of inline HTTP Authorization headers.
- No client financial, insurance or identification data found in the flow definition itself (the flow processes documents at runtime; no sample client data is embedded in the export).
- No other hardcoded secrets found after a full-text sweep for `authorization`, `bearer`, `api key`, `secret`, `password`, `access_token` patterns.

## Known gaps

- This export shows the flow calling OpenAI directly via HTTP — the current canonical `AUTO-DOCUSIGN-001` document does not mention OpenAI/AI usage at all. This is a genuine conflict between the export (newer evidence) and the canonical document (which may predate this capability, or the capability may not yet be live). **Not silently resolved** — flagged here and in `solution-inventory.md`; requires live verification of what the OpenAI call does in this flow before updating the canonical automation document's scope.
- Exact Monday.com board/column used for signer-email matching remains unconfirmed (the HTTP call's GraphQL query body was not analysed in this pass).
- Connection ownership not confirmed.
- `source_environment` and `exported_at` are unknown — this export snapshot carries no environment or export-timestamp metadata.

## Change history

| Date | Change | Author |
|---|---|---|
| 2026-07-30 | Initial manifest created from `DocuSigntoSharePoint_1_0_0_2.zip` export inspection. | Claude (documentation task) |
