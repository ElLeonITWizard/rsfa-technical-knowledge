---
solution_unique_name: SPAdviserNameChange
solution_display_name: SP Adviser Name Change
solution_version: 1.0.0.2
publisher_unique_name: Crf20c5
publisher_display_name: CDS Default Publisher
export_type: unmanaged
source_environment: Unknown — verify
exported_at: Unknown — verify
source_zip: ../../source-zips/SPAdviserNameChange_1_0_0_2.zip
snapshot_status: current-export-snapshot
last_inspected: 2026-07-30
inspection_method:
  - standard ZIP extraction
related_automations:
  - AUTO-SP-FOLDER-001
related_flows:
  - SharePoint - RSFA Asignees Permissions Modification
  - SharePoint - RSFA Asignees Permissions Creation and Modification
---

# SP Adviser Name Change

## Purpose

Two-flow Solution implementing SharePoint adviser (RSFA Assignees) permission creation and modification, keyed off changes to the `RSFA Assignees` column on Client Profiles. Despite the Solution's display name ("SP Adviser Name Change"), its flows implement **assignee permission management**, not a client/adviser name-rename operation — see "Known gaps" below.

## Export identity

- **Unique Name:** `SPAdviserNameChange`
- **Display Name:** `SP Adviser Name Change`
- **Version:** `1.0.0.2`
- **Publisher:** `Crf20c5` (`CDS Default Publisher`)
- **Managed:** No (unmanaged export)

## Source ZIP

`../../source-zips/SPAdviserNameChange_1_0_0_2.zip` — SHA-256 recorded in `current/checksums.sha256`, verified identical to `current/unmanaged.zip`.

## Included cloud flows

| Exact flow name | Workflow ID | Flow type | State from export | Primary trigger | Related canonical automation | Evidence status |
|---|---|---|---|---|---|---|
| SharePoint - RSFA Asignees Permissions Modification | `73103209-0f9e-f011-bbd2-000d3ae0ae9d` | Cloud flow | **Draft (not activated)** | `manual` — HTTP Request | `AUTO-SP-FOLDER-001` (candidate) | Unmapped — review required. Not listed as a separate flow in `knowledge/03_AUTOMATION_REGISTRY.md` §5 |
| SharePoint - RSFA Asignees Permissions Creation and Modification | `74103209-0f9e-f011-bbd2-000d3ae0ae9d` | Cloud flow | Activated | `manual` — HTTP Request | `AUTO-SP-FOLDER-001` | Likely mapping — registry lists `SharePoint - RSFA Assignees Permissions Creation and Modification` ("Assignees"); export spells it `Asignees` (missing one "s"). Same flow, spelling conflict only — not silently corrected |

"State from export" reflects this snapshot only.

## Other included components

None beyond the 2 cloud flows above.

## Connection references

| Logical name | Display name | Connector |
|---|---|---|
| `cr3e8_sharedoffice365_4938b` | SP Tech RSFA | `shared_office365` |
| `cr3e8_sharedsharepointonline_23323` | SP Tech RSFA 02 | `shared_sharepointonline` |

Connection owners are not recorded in an unmanaged export — `TODO: verify`.

## Environment variables

None present in this Solution export.

**Security finding:** both flows contain a **hardcoded HTTP Authorization header with a literal Monday.com API bearer token** instead of a Connection Reference or Environment Variable (`SharePoint - RSFA Asignees Permissions Modification`: 2 occurrences; `SharePoint - RSFA Asignees Permissions Creation and Modification`: 3 occurrences). This is the same token found hardcoded across the other three Solutions in this export set. The literal value has been redacted in the unpacked copy stored in this repository (replaced with `REDACTED-SEE-1PASSWORD-MONDAY-API-TOKEN`). The original `current/unmanaged.zip` and `../../source-zips/SPAdviserNameChange_1_0_0_2.zip` still contain it in plaintext because they are preserved byte-for-byte for integrity/checksum purposes. **This credential should be treated as exposed and rotated as soon as possible.**

## Custom connectors

None confirmed. Monday.com is called via a generic HTTP action to `https://api.monday.com/v2`.

## Dependencies

- Client Profiles board `RSFA Assignees` column as the trigger data source.
- SharePoint client folder must already exist for permission changes to apply.

## Related canonical automations

`AUTO-SP-FOLDER-001` — Client SharePoint Folder Lifecycle (`knowledge/automations/power-automate/AUTO-SP-FOLDER-001-client-folder-lifecycle.md`).

## Canonical documentation references

- `knowledge/automations/power-automate/AUTO-SP-FOLDER-001-client-folder-lifecycle.md`
- `knowledge/03_AUTOMATION_REGISTRY.md` §3, §5
- `source-material/power-automate/RSFA Asignees Permissions Creation_Modification.md`

## Inspection and validation

- Unpack method: standard ZIP extraction.
- PAC CLI unpack validation: not performed (PAC CLI not available in this environment).
- Checksum generated and verified against `source-zips/SPAdviserNameChange_1_0_0_2.zip` (identical).

## Security review

- **Finding:** hardcoded Monday.com API bearer token found in both flows. Redacted in the unpacked copy stored here; original zip copies still contain it in plaintext. **Recommend rotating this credential immediately** and migrating both flows to a Connection Reference or Environment Variable.
- No client financial, insurance or identification data found embedded in the flow definitions.
- No other hardcoded secrets found after a full-text sweep.

## Known gaps

- **Solution-name vs. flow-scope mismatch:** the Solution's display name, "SP Adviser Name Change," implies a rename/name-change operation, but both flows it contains implement RSFA Assignees **permission** creation/modification, not a rename. The actual Client Profile / SharePoint-folder rename flow lives in the separate `sp-client-folder-creation-and-renaming` Solution (`SharePoint - Rename Client Folder from Monday.com`). This mismatch has not been silently resolved — flagged here for whoever manages the Power Automate solution containers, since the naming may cause future confusion about where rename logic actually lives.
- `SharePoint - RSFA Asignees Permissions Modification` (Draft/not activated in this export) is not currently listed in `knowledge/03_AUTOMATION_REGISTRY.md` §5 at all — only the "Creation and Modification" flow is registered. Requires live verification of whether this second flow is a work-in-progress split of the registered flow, a superseded predecessor, or something else.
- "Assignees" vs "Asignees" spelling difference between registry and export is a naming inconsistency in the live Power Automate environment itself (not a documentation error) — per `knowledge/06_NAMING_AND_ID_CONVENTIONS.md` §23, do not rename the live asset without an approved, tested renaming procedure; this manifest preserves the exact export spelling.
- Connection ownership not confirmed.
- `source_environment` and `exported_at` are unknown.

## Change history

| Date | Change | Author |
|---|---|---|
| 2026-07-30 | Initial manifest created from `SPAdviserNameChange_1_0_0_2.zip` export inspection. | Claude (documentation task) |
