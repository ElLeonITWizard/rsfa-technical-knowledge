---
id: RSFA-NAMING-AND-ID-CONVENTIONS
title: RSFA Naming and ID Conventions
status: active
owner: RSFA
audience:
  - Authorised developers
  - Authorised technical consultants
last_modified: 2026-07-30
last_verified: 2026-07-30
---

# RSFA Naming and ID Conventions

## 1. Purpose

This document defines the naming and identification conventions used across RSFA's technical repository, automations, systems, boards, files and documentation.

Its purpose is to:

- Make technical assets easier to identify.
- Reduce ambiguity.
- Preserve exact platform names and IDs.
- Improve searchability.
- Help agents and developers distinguish canonical names from platform-specific names.
- Support consistent documentation across Make.com, Power Automate, Monday.com and the RSFA technical knowledge repository.

These conventions describe the preferred standard.

Existing production assets may not follow them consistently and should not be renamed solely for cosmetic reasons.

---

## 2. General naming principles

Names should be:

- Descriptive.
- Specific.
- Searchable.
- Short enough to scan.
- Clear about the system or process involved.
- Clear about whether the item is a main process, subflow, utility, migration or test.
- Stable over time where possible.

Avoid names that rely on hidden context.

Prefer:

```text
M.com: Aircall Upload Transcriptions To SP (Jul 2026)
```

Avoid:

```text
New Flow
Test 2
Final Final
Working One
Automation Copy
```

Do not rename a live production asset only to improve consistency unless:

- The rename has been assessed for downstream impact.
- Links, references and documentation are updated.
- The change is approved where required.
- The new name is tested.

---

## 3. Canonical repository IDs

Canonical repository IDs are independent from vendor IDs.

They should remain stable even if a Make scenario, Power Automate flow or Monday board is renamed.

| Asset type | Prefix | Example |
|---|---|---|
| System | `SYS-` | `SYS-MAKE-001` |
| Automation | `AUTO-` | `AUTO-AIRCALL-001` |
| Shared automation component | `COMP-` | `COMP-MAKE-ERROR-001` |
| Document | `DOC-` | `DOC-AIRCALL-001` |
| Board schema | `BOARD-` | `BOARD-MONDAY-001` |
| Incident | `INC-` | `INC-2026-001` |
| Decision record | `ADR-` | `ADR-001` |
| Playbook | `PLAYBOOK-` | `PLAYBOOK-TICKET-001` |
| Test record | `TEST-` | `TEST-AIRCALL-001` |

### Rules

- IDs must be unique.
- IDs must not be reused.
- IDs must remain stable after renaming.
- IDs should not contain spaces.
- IDs should not depend on a person's name.
- IDs should describe the canonical business or technical function.

---

## 4. File naming convention

Use lowercase kebab-case after the canonical ID.

### Examples

```text
AUTO-AIRCALL-001-aircall-call-processing.md
AUTO-EMAIL-001-client-email-filing.md
COMP-MAKE-ERROR-001-failure-email.md
INC-2026-001-missing-email-attachment.md
ADR-001-external-execution-logging.md
```

### Rules

- Use lowercase.
- Use hyphens.
- Do not use spaces.
- Do not use underscores unless required by an external platform.
- Preserve the canonical ID at the beginning of the filename.
- Do not include version labels such as `final`, `new`, `latest` or `v2` unless they are part of a platform asset name being documented.

---

## 5. Make.com scenario naming

Make.com currently follows the clearest naming pattern in RSFA.

### Preferred pattern

```text
M.com: [Clear functional description] ([Month/Year or version context])
```

Examples:

```text
M.com: Aircall Upload Transcriptions To SP (Jul 2026)
M.com: Branded SOP Filling and Filing (Jul 2026)
M.com: Insurance Expiry Email (Jul 2025)
M.com: Fixed Rate Expiry Email Alert (May25)
M.com: New item in Mortgage App Copy to Masterboard End Forms (Jan 26)
```

### Integration-direction pattern

Where useful, show system direction explicitly:

```text
[Source] to [Destination]: [Purpose]
```

Examples:

```text
AffordX to M.com Applications Sync (Aug 2025)
Macroforge to M.com: End Forms Filled (May 2026)
M.com to Macroforge: Trigger Macroforge End Forms Filling Flow (Feb 2026)
Pigeon to M.com: Request Creation
```

### Subflow pattern

Reusable subflows should include `Subflow` in the name.

Examples:

```text
AffordX Subflow Client Creation (Sep 2025)
M.com: Subflow Search Contacts in Monday (Feb 26)
```

### Main scenario pattern

Main scenarios may include `Parent` only if the Make interface or operational distinction requires it.

Do not add `Parent` to every main scenario name unnecessarily.

### Date suffix

A date suffix is useful when:

- The scenario was materially rebuilt.
- Multiple versions coexist.
- The scenario is part of a migration.
- The date helps distinguish current from historical versions.

Preferred formats:

```text
(Jul 2026)
(May 2026)
(Jan 26)
(May25)
```

For new work, prefer:

```text
(MMM YYYY)
```

Example:

```text
(Jul 2026)
```

### Avoid

```text
M.com New Flow
M.com Final
M.com V2 Final
Copy of Scenario
Test Scenario
```

### Exact-name rule

Documentation must preserve the exact Make scenario name and scenario ID.

The canonical automation name may be cleaner than the exact Make name.

Example:

- **Canonical automation:** `Aircall Call Processing, Transcription and Summary`
- **Exact Make scenario:** `M.com: Aircall Upload Transcriptions To SP (Jul 2026)`

---

## 6. Make.com scenario roles

Use these role labels in documentation:

- `Parent`
- `Bridge`
- `Standalone`
- `Subscenario`
- `Shared component`
- `Maintenance utility`
- `Migration utility`
- `Historical`

Do not infer the role from the name alone when call-graph metadata exists.

---

## 7. Power Automate flow naming

Power Automate naming is currently less consistent than Make.com naming.

The preferred approach is to use a descriptive name that clearly identifies:

- The source system.
- The destination or action.
- The user or mailbox scope where relevant.
- Whether it is sent, received, manual, scheduled or a child flow.
- Version context only when multiple live versions coexist.

### Existing patterns

Examples:

```text
DocuSign to SharePoint
Main Outlook Inbox Email Filling
Outlook Email Filing - Support v2
Outlook Email Filing - Seth v2
Outlook SENT Email Filling - Kathleen v2
Email Filling Failed Items Processing
Overflow Emails Contact Matching
SharePoint - Client Folder Creation from Monday.com
SharePoint - Rename Client Folder from Monday.com
Monday Massive Activities Log Back Up
```

### Preferred pattern

```text
[Source] - [Action] - [Scope]
```

or:

```text
[Source] to [Destination] - [Purpose]
```

Examples:

```text
Outlook - Email Filing - Rod
Outlook - Sent Email Filing - Kathleen
SharePoint - Client Folder Creation from Monday
DocuSign to SharePoint - Signed Document Filing
Monday - Activities Backup
```

### Child flows

Reusable child flows should clearly indicate their role.

Preferred:

```text
Child - Main Outlook Email Filing
Child - Process Email Attachments
```

Existing names should not be changed without impact review.

### Manual and bulk flows

Manual or potentially high-impact flows should include a clear qualifier:

```text
Manual - Massive Client Folder Renaming
Manual - Massive SharePoint File Renaming
```

### Planned-retirement flows

Do not rename a flow solely to mark retirement.

Use registry and documentation status:

```text
active-planned-retirement
```

Example:

```text
OLD Outlook SENT Email Filling - Jet v2
```

The `OLD` prefix may remain until retirement, but future flows should use documentation status instead of naming alone.

### Version labels

Use `v2`, `v3` or similar only when:

- Multiple versions coexist.
- The version is operationally important.
- The old version has not yet been retired.

Avoid leaving permanent `v2` labels after the previous version is removed, unless renaming would create risk.

---

## 8. Monday board naming

Monday board names are primarily decided by Rod and may vary by process.

The general current style is:

```text
[Emoji] [Descriptive board name]
```

Examples:

```text
💲 Mortgage Pipeline
✅ Existing Mortgages
📋 Pigeon: Finance Checklist
✍ Mortgage App/SOP
✍ ROMA/Stage3: Mortgages
🏧 AffordX: Bank Statements
📞 Aircall: VOIP Call Board
➕ Insurance Deals Pipeline
```

### Preferred board naming principles

- Use one leading emoji when it improves visual scanning.
- Use a clear descriptive name.
- Preserve product or platform names.
- Use `Pipeline` for active opportunity or implementation work.
- Use `Existing` for ongoing or in-force business.
- Use `Questionnaire` for form-intake boards.
- Use `Archive`, `Backup` or `Log` when the board is not operational source data.
- Use `WIP` only for genuinely experimental boards.
- Use `OLD` only for clearly retained historical boards.

### Avoid

- Multiple decorative emojis.
- Names that do not explain item meaning.
- Ambiguous names such as `New Board`.
- Renaming production boards without reviewing integrations.
- Relying on colour or emoji alone to indicate status.

### Exact-name rule

Documentation must preserve the exact board name, board ID and URL.

Canonical documentation may additionally use a simplified display name.

Example:

- **Exact board name:** `💲 Mortgage Pipeline`
- **Simplified reference:** `Mortgage Pipeline`
- **Board ID:** Preserve exact Monday ID.

---

## 9. Monday workflow naming

Monday Workflow names should describe the outcome.

Current examples:

```text
Move to Pipeline Workflow (New)
Leads App 2 Creation + CP Name
```

### Preferred pattern

```text
[Primary action] + [Secondary action or scope]
```

Examples:

```text
Move Lead to Selected Pipeline
Create Second Applicant + Client Profile Name
Move Completed Mortgage to Existing Mortgages
```

### Rules

- Use a verb first where possible.
- Name the source or target when ambiguity exists.
- Avoid `New` as a permanent identifier.
- Use version context only during migration.
- Preserve exact existing names in documentation.

---

## 10. Monday native automation naming

Monday native recipes may be generated from templates and are often too numerous to manage individually.

When a recipe can be named manually, prefer:

```text
[Trigger] → [Action]
```

Examples:

```text
Pipeline Status changes → Create Mortgage Pipeline item
Client Profile assigned → Reprocess Overflow Email
Call ready → Trigger Aircall transcription
Mortgage completed → Create Existing Mortgage
```

Where Monday does not support custom recipe names, document the trigger and action explicitly in the relevant board schema or automation file.

---

## 11. System and integration naming

Use exact vendor names:

```text
Monday.com
Make.com
Power Automate
SharePoint
Microsoft 365
Outlook
Slack
Aircall
Superforms
Monday Forms
Pigeon
MacroForge
AffordX
DocuSign
DocuSeal
Google Cloud
1Password
Claude
ChatGPT
```

Do not replace official names with internal abbreviations in canonical headings.

Abbreviations may be used after the full name has been established.

---

## 12. Common abbreviations

| Abbreviation | Meaning |
|---|---|
| `M.com` | Monday.com |
| `SP` | SharePoint |
| `PA` | Power Automate |
| `CP` | Client Profile |
| `MA` | Mortgage Application |
| `IQ` | Insurance Questionnaire |
| `KQ` | KiwiSaver Questionnaire |
| `E&A` | Emails & Activities |
| `SOP` | Statement of Position |
| `FR Exp` | Fixed Rate Expiry |
| `WIP` | Work in Progress |
| `JV` | Historical or internal naming suffix; exact meaning requires context |
| `AI` | Artificial Intelligence |
| `API` | Application Programming Interface |

### Rules

- Use abbreviations in exact platform names when they already exist.
- In canonical documentation, write the full term on first use.
- Do not introduce new abbreviations without adding them to the glossary.

---

## 13. Date conventions

Use ISO dates in documentation:

```text
YYYY-MM-DD
```

Examples:

```text
2026-07-30
2026-05-19
```

Use human-readable month-year labels only inside exact platform names where they already exist:

```text
(Jul 2026)
(May 2026)
```

---

## 14. Status naming

Use these canonical status values in repository frontmatter.

### Systems

```text
active-core
active
active-expanding
active-reducing
experimental
planned
legacy-migration-required
retired
```

### Automations

```text
active
active-under-improvement
active-planned-retirement
testing
planned
inactive
deprecated
unknown
```

### Documentation

```text
documented
partial
outdated
not-documented
```

Preserve exact platform status labels separately.

---

## 15. Environment and lifecycle labels

Use these labels where relevant:

```text
Production
Testing
Experimental
Migration
Maintenance
Historical
Deprecated
Planned Retirement
```

Do not use `Production` unless actual production use is confirmed.

Do not use `Deprecated` merely because an asset is old.

---

## 16. Account naming

Preserve exact RSFA account addresses.

Examples:

```text
tech@rsfa.co.nz
it-support@rsfa.co.nz
support@rsfa.co.nz
rod@rsfa.co.nz
insurance@rsfa.co.nz
seth@rsfa.co.nz
jet@rsfa.co.nz
slack-ingest@rsfa.co.nz
media@rsfa.co.nz
operations@rsfa.co.nz
```

Do not use display names as substitutes for technical-account references.

Do not include passwords or secret values.

---

## 17. SharePoint folder naming

Client SharePoint folders must include the Monday Client Profile ID.

This supports reliable matching between Monday.com and SharePoint.

Preferred conceptual pattern:

```text
[Client Profile Name] - [Monday Client Profile ID]
```

The exact production pattern must be preserved.

Do not rename client folders without reviewing:

- Power Automate dependencies.
- Real Savvy Ref behaviour.
- Monday SharePoint links.
- Make.com mappings.
- OneDrive synchronisation.
- MacroForge local paths.

General folders should use clear operational names.

Examples:

```text
Emails to Sort
Email Communications
Email Attachments
Overflow
```

---

## 18. Slack channel naming

Preserve exact Slack channel names.

Where automation channels follow a pattern, document the pattern explicitly.

Known conceptual pattern:

```text
[adviser]_ai_emails
```

Example:

```text
rod_ai_emails
seth_ai_emails
```

Exact names must be verified before use.

Do not invent a Slack channel from a pattern.

---

## 19. Email subject reference convention

The Real Savvy Ref Outlook Add-in supports the subject reference:

```text
RSFA Ref %ClientProfileID%
```

This reference is used to force Client Profile matching in Main Outlook Email Filing.

### Rules

- Preserve exact casing and spacing.
- Use the Monday Client Profile ID.
- Do not use Contact ID or another board ID.
- Document any change to this format before implementation.
- Treat the format as a technical dependency.

---

## 20. Platform ID conventions

Always record vendor IDs separately from canonical IDs.

Example:

```text
Canonical automation ID: AUTO-AIRCALL-001
Make scenario ID: 1234567
Monday board ID: 5024672364
Google Cloud project ID: rsfa-backend-fix
```

Do not combine them into one field.

### Common vendor IDs

- Monday board ID.
- Monday column ID.
- Monday item ID.
- Make scenario ID.
- Make webhook ID.
- Power Automate flow ID.
- SharePoint site ID.
- SharePoint drive or library ID.
- Aircall call ID.
- Google Cloud project ID.

---

## 21. Column naming and IDs

Monday column titles may change.

Monday column IDs are the technical identifier used by integrations.

Documentation should record both:

```text
Column title: Client Profile
Column ID: connect_boards123
```

### Rules

- Never infer a column ID from its title.
- Preserve exact casing.
- Record historical title changes when they affect mappings.
- Do not rename a column without reviewing Make, Power Automate, Superforms and Monday native automations.
- Use technical IDs in mappings and schemas.

---

## 22. Canonical name versus platform name

A canonical automation name should describe the business function.

A platform name should preserve the exact live asset name.

Example:

```text
Canonical automation:
Aircall Call Processing, Transcription and Summary

Exact Make scenario:
M.com: Aircall Upload Transcriptions To SP (Jul 2026)
```

Use both in documentation.

Do not force the canonical name back into the live platform unless a rename is separately approved.

---

## 23. Renaming procedure

Before renaming a production asset:

1. Identify all references.
2. Check Make.com.
3. Check Power Automate.
4. Check Monday native automations and workflows.
5. Check Superforms.
6. Check SharePoint.
7. Check Slack notifications.
8. Check repository documentation.
9. Check links in the Automations and Manuals/Documentation boards.
10. Define rollback.
11. Perform the rename.
12. Validate downstream behaviour.
13. Update canonical documentation.

Do not assume a name change is cosmetic.

---

## 24. Prohibited naming patterns

Avoid creating new assets with:

```text
Test
Test 2
Copy
Copy of
Final
Final Final
Latest
New Flow
Untitled
Working
Temp
Fix
Old
New
```

These terms may be used only with additional context and a planned lifecycle.

Better examples:

```text
Migration - Connect Client Profiles and Pipelines - Dec 2025
Maintenance - Review Broken SharePoint Links - May 2026
Testing - DocuSeal Submission Filing
```

---

## 25. Searchability rules

Important names should contain at least one of:

- Main system.
- Main object.
- Main action.
- Main destination.
- Scope.
- Lifecycle qualifier.

Example:

```text
M.com: Pigeon Documents to Mortgage Pipeline
```

This is more searchable than:

```text
Document Automation
```

---

## 26. Maintenance rules

Update this document when:

- A new naming pattern becomes standard.
- A new canonical ID type is introduced.
- Make.com naming changes.
- Power Automate naming is standardised.
- A new board naming approach is adopted.
- A new system abbreviation is introduced.
- A critical technical reference format changes.
- SharePoint folder naming changes.
- Status or lifecycle labels change.

Existing assets should be documented accurately even when they do not comply with the preferred standard.

Do not rewrite history to make old names appear compliant.
