# Power Automate Exports

This folder stores exported Power Automate Solution packages as read-only technical evidence. It exists so a developer investigating a Power Automate flow can inspect its exact current package contents (flow names, workflow IDs, connection references, trigger definitions) without needing to authenticate against Power Platform.

## What this folder contains

```text
exports/power-automate/
├── README.md                    — this file
├── solution-inventory.md        — master index of every exported Solution and its flows
├── source-zips/                 — original, untouched Solution export ZIPs
└── solutions/
    └── <solution-slug>/
        ├── manifest.md          — per-Solution identity, flow list, mappings, security review
        └── current/
            ├── unmanaged.zip    — copy of the source ZIP for this Solution
            ├── checksums.sha256 — SHA-256 of unmanaged.zip
            └── unpacked/        — extracted package contents, for inspection
```

## `source-zips/`

Holds exactly one copy of each original Solution export ZIP, unmodified and unrenamed. This is the canonical original — never edit, rename or delete a file here. If a Solution is re-exported, add the new ZIP; do not overwrite the previous one unless explicitly instructed to replace it.

## `solutions/<solution>/current/`

`current/` means **the latest snapshot stored in this Git repository**, not a guaranteed reflection of live production state. It contains:

- `unmanaged.zip` — a copy of the matching file in `source-zips/`, checksummed for integrity.
- `checksums.sha256` — the SHA-256 of `unmanaged.zip`, in the format `<hash>  unmanaged.zip`.
- `unpacked/` — the extracted contents (customizations.xml, solution.xml, Workflows/*.json), used for read-only inspection. **Do not hand-edit files under `unpacked/`** — if the package changes, re-export and re-unpack it.

## What `current-export-snapshot` means

Every manifest is tagged `snapshot_status: current-export-snapshot`. This means:

- The Solution package existed with this exact content at the time it was exported.
- It does **not** prove the flows are currently enabled, currently error-free, or currently deployed to any specific environment.
- A flow shown here as "Activated" or "Draft" reflects only what this package said at export time — always re-verify live state before treating it as current production behaviour.

## What this folder is not

This folder is **not tested Power Automate solution content, and it is not a working directory for changes**. Files under `exports/power-automate/solutions/` are production evidence snapshots.

They must not be used as the working directory for proposed changes.

Proposed Power Automate changes belong in:

`../rsfa-automation-development/projects/<project-slug>/power-automate/`

(adjust the relative path if that repository lives elsewhere relative to this one).

## Security note

Some workflow JSON files in this export set were found to contain hardcoded API credentials (a Monday.com bearer token, an OpenAI API key) directly in HTTP action headers rather than in a Connection Reference. Where found, these values have been **redacted** in the `unpacked/` copies (replaced with a `REDACTED-SEE-1PASSWORD-*` placeholder) and flagged in the affected manifest's Security Review section. The corresponding `unmanaged.zip` files (and the originals in `source-zips/`) still contain the same values in plaintext, since those are preserved byte-for-byte for checksum integrity — see each manifest's Security Review section before sharing or distributing a ZIP from this folder. Never add a secret value to a manifest, the inventory, or any canonical documentation file — reference the credential by system/purpose only, per `CLAUDE.md` §13.

## How to add a new export

See "Update procedure" in `solution-inventory.md`.

## How to replace a `current/` snapshot

See "Update procedure" in `solution-inventory.md`.

## How to generate a checksum

```powershell
$hash = (Get-FileHash -Algorithm SHA256 .\unmanaged.zip).Hash.ToLower()
"$hash  unmanaged.zip" | Set-Content .\checksums.sha256 -Encoding UTF8
```

## How to unpack with PAC CLI

```powershell
pac solution unpack `
  --zipfile "<path-to-current-unmanaged.zip>" `
  --folder "<path-to-current-unpacked>"
```

PAC CLI was not available when this export set was first inspected (`pac --version` returned "command not found"). All four current manifests record `inspection_method: standard ZIP extraction` and `PAC CLI unpack validation: not performed`. Installing PAC CLI and re-running an unpack for cross-validation is a recommended, but not yet completed, follow-up.

## How to do a security review

Before adding or refreshing any export, scan every file under `unpacked/` for hardcoded credentials before treating the copy as safe to keep in this repository:

```bash
grep -rniE 'authorization|api[_-]?key|bearer |secret|password|access_token' unpacked/
```

Redact any literal secret value found (do not delete the surrounding structure), note the redaction in the manifest's Security Review section, and flag the credential for rotation. Never reproduce the actual secret value anywhere in this repository.

## How to update manifests and the inventory

After adding, replacing or re-inspecting a Solution:

1. Update the Solution's `manifest.md` (frontmatter `last_inspected`, flow table, connection references, security review, known gaps, change history).
2. Update `solution-inventory.md`'s tables to match.
3. Cross-check flow names against `knowledge/03_AUTOMATION_REGISTRY.md` and update the mapping confidence level accordingly — never silently mark something "Confirmed" without direct name/ID evidence.

## What must never be stored here

- Passwords, API keys, OAuth secrets, access or refresh tokens, or any other credential value — even ones found already hardcoded in an export must be redacted, not preserved, in the `unpacked/` copies kept in this repository.
- Real client financial, insurance, identification or medical data.
- Unredacted client call transcripts or full email contents.
- Anything that would let a reader reconstruct a live credential (partial fragments across multiple files count too).
