# Power Automate Solution Inventory

## Purpose

This is the master index of Power Automate Solution exports stored under `exports/power-automate/solutions/`. It exists so an authorised developer can find, at a glance, which Solutions have been exported and inspected, which exact flows they contain, and how those flows map (or fail to map) onto the canonical automations documented under `knowledge/automations/power-automate/`.

This inventory documents **exported package content**, not live production state. Treat every entry as a point-in-time snapshot — see `snapshot_status: current-export-snapshot` in each manifest.

## Source and scope

Covers the four Solution ZIPs added to this repository on 2026-07-30:

| Source ZIP (in `source-zips/`) | Solution folder |
|---|---|
| `DocuSigntoSharePoint_1_0_0_2.zip` | `solutions/docusign-to-sharepoint/` |
| `RSFAOutlookEmailFilling_1_0_0_3.zip` | `solutions/rsfa-outlook-email-filing/` |
| `SPAdviserNameChange_1_0_0_2.zip` | `solutions/sp-adviser-name-change/` |
| `SPClientFolderCreationandRenaming_1_0_0_1.zip` | `solutions/sp-client-folder-creation-and-renaming/` |

No PAC CLI authentication, import, or Power Platform write of any kind was performed to produce this inventory — all four ZIPs were provided as local files and inspected read-only (standard ZIP extraction; PAC CLI was not available in this environment).

## Solution inventory

| Solution Unique Name | Display Name | Version | Source ZIP | Cloud flows | Related canonical automations | Inspection status | Last inspected |
|---|---|---:|---|---:|---|---|---|
| `DocuSigntoSharePoint` | DocuSign to SharePoint | 1.0.0.2 | `DocuSigntoSharePoint_1_0_0_2.zip` | 1 | `AUTO-DOCUSIGN-001` | Inspected (standard ZIP extraction; PAC unpack not performed) | 2026-07-30 |
| `RSFAOutlookEmailFilling` | SP Email Filling | 1.0.0.3 | `RSFAOutlookEmailFilling_1_0_0_3.zip` | 15 | `AUTO-EMAIL-001`, `AUTO-EMAIL-BACKUP-001` | Inspected (standard ZIP extraction; PAC unpack not performed) | 2026-07-30 |
| `SPAdviserNameChange` | SP Adviser Name Change | 1.0.0.2 | `SPAdviserNameChange_1_0_0_2.zip` | 2 | `AUTO-SP-FOLDER-001` | Inspected (standard ZIP extraction; PAC unpack not performed) | 2026-07-30 |
| `SPClientFolderCreationandRenaming` | SP Client Folder Creation and Renaming | 1.0.0.1 | `SPClientFolderCreationandRenaming_1_0_0_1.zip` | 2 | `AUTO-SP-FOLDER-001` | Inspected (standard ZIP extraction; PAC unpack not performed) | 2026-07-30 |

**Total: 4 Solutions, 20 cloud flows.**

## Flow-to-solution mapping

| Exact flow name | Workflow ID | Solution | Canonical automation | Documentation file | Mapping confidence |
|---|---|---|---|---|---|
| DocuSign to SharePoint (trailing space in export) | `911a3139-e5da-ef11-8eea-00224814e0ff` | docusign-to-sharepoint | `AUTO-DOCUSIGN-001` | `AUTO-DOCUSIGN-001-docusign-filing.md` | Confirmed from export and canonical documentation |
| Main Outlook Inbox Email Filling | `f6906da4-c8ed-ef11-9341-6045bd3ce9ae` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` | `AUTO-EMAIL-001-client-email-filing.md` | Confirmed from export and canonical documentation |
| Outlook INBOX items email filing (Rod) | `921a3139-e5da-ef11-8eea-00224814e0ff` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` (candidate) | `AUTO-EMAIL-001-client-email-filing.md` | Unmapped — review required |
| Outlook INBOX items email filing (Kathleen) | `941a3139-e5da-ef11-8eea-00224814e0ff` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` (candidate) | `AUTO-EMAIL-001-client-email-filing.md` | Unmapped — review required |
| Sent Emails Control | `32f10b1d-b79c-f011-bbd2-000d3ae0ae9d` | rsfa-outlook-email-filing | — | — | Unmapped — review required |
| OLD Outlook SENT Email Filling - Jet v2 | `80273d77-b79c-f011-bbd2-000d3ae0ae9d` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` | `AUTO-EMAIL-001-client-email-filing.md` | Confirmed from export and canonical documentation |
| Outlook Email Filling - Jet v2 | `d30599eb-ec37-f011-8c4d-6045bd4096fa` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` | `AUTO-EMAIL-001-client-email-filing.md` | Likely mapping (registry name: "Filing", export: "Filling") |
| Outlook SENT Email Filling - Rod v2 | `d2d40c71-dbf9-ef11-bae2-6045bd4096fa` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` | `AUTO-EMAIL-001-client-email-filing.md` | Confirmed from export and canonical documentation |
| Outlook SENT Email Filling - Kathleen v2 | `5d50f6af-affa-ef11-bae2-6045bd4096fa` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` | `AUTO-EMAIL-001-client-email-filing.md` | Confirmed from export and canonical documentation |
| Outlook Email Filing - Support v2 | `ca963563-abfb-ef11-bae3-6045bd4096fa` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` | `AUTO-EMAIL-001-client-email-filing.md` | Confirmed from export and canonical documentation |
| Outlook Email Filling - Kathleen v2 | `360d1f29-5bf8-ef11-bae2-002248185f06` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` | `AUTO-EMAIL-001-client-email-filing.md` | Likely mapping (registry name: "Filing", export: "Filling") |
| Outlook Email Filling - Rod v2 | `d34b8f51-46f8-ef11-bae2-002248185f06` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` | `AUTO-EMAIL-001-client-email-filing.md` | Likely mapping (registry name: "Filing", export: "Filling") |
| Outlook SENT Email Filling - Support v2 | `816b9f65-6237-f011-8c4d-6045bd4096fa` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` (candidate) | `AUTO-EMAIL-001-client-email-filing.md` | Unmapped — review required |
| Email Filling Failed Items Processing | `04531fc5-dced-ef11-9341-6045bd3ce9ae` | rsfa-outlook-email-filing | `AUTO-EMAIL-BACKUP-001` | `AUTO-EMAIL-BACKUP-001-email-backup-recovery.md` | Confirmed from export and canonical documentation |
| Overflow Emails Contact Matching | `6bf7b40c-b29c-f011-bbd2-000d3ae0ae9d` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` | `AUTO-EMAIL-001-client-email-filing.md` | Confirmed from export and canonical documentation |
| Overflow Emails Related Client Profile Change | `03b8f6d7-66af-f011-bbd3-000d3ae0ae9d` | rsfa-outlook-email-filing | `AUTO-EMAIL-001` | `AUTO-EMAIL-001-client-email-filing.md` | Confirmed from export and canonical documentation |
| SharePoint - RSFA Asignees Permissions Modification | `73103209-0f9e-f011-bbd2-000d3ae0ae9d` | sp-adviser-name-change | `AUTO-SP-FOLDER-001` (candidate) | `AUTO-SP-FOLDER-001-client-folder-lifecycle.md` | Unmapped — review required |
| SharePoint - RSFA Asignees Permissions Creation and Modification | `74103209-0f9e-f011-bbd2-000d3ae0ae9d` | sp-adviser-name-change | `AUTO-SP-FOLDER-001` | `AUTO-SP-FOLDER-001-client-folder-lifecycle.md` | Likely mapping (registry name: "Assignees", export: "Asignees") |
| SharePoint - Rename Client Folder from Monday.com | `8f6285cd-0f9e-f011-bbd2-000d3ae0ae9d` | sp-client-folder-creation-and-renaming | `AUTO-SP-FOLDER-001` | `AUTO-SP-FOLDER-001-client-folder-lifecycle.md` | Confirmed from export and canonical documentation |
| SharePoint - Client Folder Creation from Monday.com | `906285cd-0f9e-f011-bbd2-000d3ae0ae9d` | sp-client-folder-creation-and-renaming | `AUTO-SP-FOLDER-001` | `AUTO-SP-FOLDER-001-client-folder-lifecycle.md` | Confirmed from export and canonical documentation |

## Canonical automation mapping

| Automation ID | Solutions covering it | Flows confirmed | Flows unmapped/likely |
|---|---|---:|---:|
| `AUTO-DOCUSIGN-001` | docusign-to-sharepoint | 1 | 0 |
| `AUTO-EMAIL-001` | rsfa-outlook-email-filing | 9 | 6 (2 unmapped, 3 likely by spelling, 1 unmapped shared-mailbox variant) |
| `AUTO-EMAIL-BACKUP-001` | rsfa-outlook-email-filing | 1 | 0 |
| `AUTO-SP-FOLDER-001` | sp-adviser-name-change, sp-client-folder-creation-and-renaming | 3 | 1 unmapped, 1 likely by spelling |

## Unmapped flows

The following flows exist in an export but have **no current canonical automation registry entry** under their exact exported name:

1. `Outlook INBOX items email filing (Rod)` — `921a3139-e5da-ef11-8eea-00224814e0ff` (Draft/not activated in export)
2. `Outlook INBOX items email filing (Kathleen)` — `941a3139-e5da-ef11-8eea-00224814e0ff` (Draft/not activated in export)
3. `Sent Emails Control` — `32f10b1d-b79c-f011-bbd2-000d3ae0ae9d` (Draft/not activated in export)
4. `Outlook SENT Email Filling - Support v2` — `816b9f65-6237-f011-8c4d-6045bd4096fa` (Draft/not activated in export)
5. `SharePoint - RSFA Asignees Permissions Modification` — `73103209-0f9e-f011-bbd2-000d3ae0ae9d` (Draft/not activated in export)

Additionally, `Overflow Emails Suggested Match Approval` — registered in `knowledge/03_AUTOMATION_REGISTRY.md` §5 as part of `AUTO-EMAIL-001` — is **absent from every export in this set**. This is the inverse gap: a registry entry with no corresponding export evidence yet.

None of the above have been guessed into a mapping. They require either a live Power Automate lookup or a conversation with whoever built them.

## Validation status

- PAC CLI available: **No** (`pac --version` returned "command not found" in this environment).
- PAC CLI unpack performed: **No** — all four Solutions were unpacked with standard ZIP extraction only.
- Checksums generated for all four `unmanaged.zip` copies and verified identical to their `source-zips/` originals: **Yes**.
- All four original ZIPs retained, unmodified, in `source-zips/`: **Yes**.
- Sensitive-value review performed: **Yes** — see "Security-relevant cross-solution finding" below.
- No Power Platform authentication or write operation was performed at any point.

## Security-relevant cross-solution finding

All four Solutions hardcode the **same Monday.com API bearer token** directly into HTTP action headers (across 10 of the 20 flows), instead of using a Connection Reference or Environment Variable. Three flows in two Solutions (`docusign-to-sharepoint`, `rsfa-outlook-email-filing`) additionally hardcode the **same OpenAI API key**. Both literal values have been redacted in every unpacked copy stored in this repository; the `current/unmanaged.zip` files and the `source-zips/` originals still contain them in plaintext because those are preserved byte-for-byte for checksum integrity. **Both credentials appear to be live and should be rotated as soon as possible** — see the Security Review section of each affected manifest for the exact per-flow occurrence counts. Restrict distribution of the zip files until rotation is confirmed.

## Known gaps

- Five flows are unmapped against the current Automation Registry (listed above) and one registered flow (`Overflow Emails Suggested Match Approval`) has no corresponding export — both directions of this discrepancy need live-system verification, not silent reconciliation.
- Three flow-name spelling mismatches ("Filing" vs "Filling"; "Assignees" vs "Asignees") between the registry and the live Power Automate environment are documented as-is in each manifest, per the naming-convention rule against silently correcting production asset names.
- An `Outlook_Insurance_RSFA` connection reference in `rsfa-outlook-email-filing` suggests an undocumented Insurance-mailbox email-filing capability not currently described in `AUTO-EMAIL-001`.
- The `SPAdviserNameChange` Solution's display name does not match the actual function of the flows it contains (assignee permissions, not adviser renaming) — flagged in its manifest.
- `source_environment` and `exported_at` are `Unknown — verify` for all four Solutions; none of these exports carry embedded environment or export-timestamp metadata.
- Connection reference **owners** are not recorded in any of the four unmanaged exports.

## Update procedure

To add a new Solution export:

1. Place the new `.zip` in `source-zips/`, keeping its original filename.
2. Read `solution.xml` and `customizations.xml` from the zip to get the exact `UniqueName`, display name, version, publisher and flow list — do not derive these from the filename.
3. Create (or update) `solutions/<kebab-case-slug>/` with `manifest.md` and a `current/` folder containing `unmanaged.zip`, `checksums.sha256`, and `unpacked/`.
4. Scan every unpacked workflow JSON for hardcoded secrets before treating the unpacked copy as safe to keep in this repository; redact any found and flag them.
5. Update this file's tables and the relevant manifest(s).
6. Cross-check flow names against `knowledge/03_AUTOMATION_REGISTRY.md` §5 and update mappings, marking anything uncertain as `Likely mapping`, `Unmapped`, or `Conflict — verification required` rather than guessing.

To replace an existing Solution's `current/` snapshot:

1. Follow steps 1–4 above for the new zip, overwriting the existing `current/unmanaged.zip`, `checksums.sha256` and `unpacked/`.
2. Update `last_inspected` in the manifest frontmatter and update the manifest body to reflect what changed (new/removed/renamed flows, state changes, new connection references).
3. Do not delete the manifest's change history — append a new row.

## Change history

| Date | Change | Author |
|---|---|---|
| 2026-07-30 | Initial inventory created covering the first four Power Automate Solution exports added to this repository. | Claude (documentation task) |
