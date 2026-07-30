---
solution_unique_name: SPClientFolderCreationandRenaming
solution_display_name: SP Client Folder Creation and Renaming
solution_version: 1.0.0.1
publisher_unique_name: Crf20c5
publisher_display_name: CDS Default Publisher
export_type: unmanaged
source_environment: Unknown — verify
exported_at: Unknown — verify
source_zip: ../../source-zips/SPClientFolderCreationandRenaming_1_0_0_1.zip
snapshot_status: current-export-snapshot
last_inspected: 2026-07-30
inspection_method:
  - standard ZIP extraction
related_automations:
  - AUTO-SP-FOLDER-001
related_flows:
  - SharePoint - Rename Client Folder from Monday.com
  - SharePoint - Client Folder Creation from Monday.com
---

# SP Client Folder Creation and Renaming

## Purpose

Two-flow Solution implementing client SharePoint folder creation and renaming, driven by Client Profiles board changes in Monday.com. This is the cleanest mapping in this export set — both flows match the Automation Registry exactly by name.

## Export identity

- **Unique Name:** `SPClientFolderCreationandRenaming`
- **Display Name:** `SP Client Folder Creation and Renaming`
- **Version:** `1.0.0.1`
- **Publisher:** `Crf20c5` (`CDS Default Publisher`)
- **Managed:** No (unmanaged export)

## Source ZIP

`../../source-zips/SPClientFolderCreationandRenaming_1_0_0_1.zip` — SHA-256 recorded in `current/checksums.sha256`, verified identical to `current/unmanaged.zip`.

## Included cloud flows

| Exact flow name | Workflow ID | Flow type | State from export | Primary trigger | Related canonical automation | Evidence status |
|---|---|---|---|---|---|---|
| SharePoint - Rename Client Folder from Monday.com | `8f6285cd-0f9e-f011-bbd2-000d3ae0ae9d` | Cloud flow | Activated | `manual` — HTTP Request | `AUTO-SP-FOLDER-001` | Confirmed from export and canonical documentation — exact name match |
| SharePoint - Client Folder Creation from Monday.com | `906285cd-0f9e-f011-bbd2-000d3ae0ae9d` | Cloud flow | Activated | `manual` — HTTP Request | `AUTO-SP-FOLDER-001` | Confirmed from export and canonical documentation — exact name match |

"State from export" reflects this snapshot only.

## Other included components

None beyond the 2 cloud flows above.

## Connection references

| Logical name | Display name | Connector |
|---|---|---|
| `cr3e8_sharedoffice365_49c3f` | Office 365 Outlook SPClientFolderCreationandRenaming-49c3f | `shared_office365` |
| `cr3e8_sharedsharepointonline_10f77` | SharePoint SPClientFolderCreationandRenaming-10f77 | `shared_sharepointonline` |

Connection owners are not recorded in an unmanaged export — `TODO: verify`.

## Environment variables

None present in this Solution export.

**Security finding:** both flows contain a **hardcoded HTTP Authorization header with a literal Monday.com API bearer token** instead of a Connection Reference or Environment Variable (`SharePoint - Client Folder Creation from Monday.com`: 2 occurrences; `SharePoint - Rename Client Folder from Monday.com`: 1 occurrence). This is the same token found hardcoded across the other three Solutions in this export set. The literal value has been redacted in the unpacked copy stored in this repository (replaced with `REDACTED-SEE-1PASSWORD-MONDAY-API-TOKEN`). The original `current/unmanaged.zip` and `../../source-zips/SPClientFolderCreationandRenaming_1_0_0_1.zip` still contain it in plaintext because they are preserved byte-for-byte for integrity/checksum purposes. **This credential should be treated as exposed and rotated as soon as possible.**

## Custom connectors

None confirmed. Monday.com is called via a generic HTTP action to `https://api.monday.com/v2` and `https://api.monday.com/v2/`.

## Dependencies

- Client Profiles board (`pulseID`, name) as the trigger data source.
- SharePoint client-files library as the destination.
- `AUTO-EMAIL-001`, `AUTO-DOCUSIGN-001` and other filing automations depend on this Solution having already created a valid, correctly-permissioned folder.

## Related canonical automations

`AUTO-SP-FOLDER-001` — Client SharePoint Folder Lifecycle (`knowledge/automations/power-automate/AUTO-SP-FOLDER-001-client-folder-lifecycle.md`).

## Canonical documentation references

- `knowledge/automations/power-automate/AUTO-SP-FOLDER-001-client-folder-lifecycle.md`
- `knowledge/03_AUTOMATION_REGISTRY.md` §3, §5
- `source-material/power-automate/SharePoint Client File Creation from M.com.md`
- `source-material/power-automate/Rename Client SP Folder per m.com change.md`

## Inspection and validation

- Unpack method: standard ZIP extraction.
- PAC CLI unpack validation: not performed (PAC CLI not available in this environment).
- Checksum generated and verified against `source-zips/SPClientFolderCreationandRenaming_1_0_0_1.zip` (identical).

## Security review

- **Finding:** hardcoded Monday.com API bearer token found in both flows. Redacted in the unpacked copy stored here; original zip copies still contain it in plaintext. **Recommend rotating this credential immediately** and migrating both flows to a Connection Reference or Environment Variable.
- No client financial, insurance or identification data found embedded in the flow definitions.
- No other hardcoded secrets found after a full-text sweep.

## Known gaps

- Exact standard subfolder list created by `SharePoint - Client Folder Creation from Monday.com` was not re-verified from this export in this pass (see `AUTO-SP-FOLDER-001` §25 for prior gap).
- Connection ownership not confirmed.
- `source_environment` and `exported_at` are unknown.

## Change history

| Date | Change | Author |
|---|---|---|
| 2026-07-30 | Initial manifest created from `SPClientFolderCreationandRenaming_1_0_0_1.zip` export inspection. | Claude (documentation task) |
