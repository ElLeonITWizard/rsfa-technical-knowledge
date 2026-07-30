# RSFA Make.com Scenario Call Graph — Valid scenarios/working

**Scope:** the 22 scenarios in `Valid scenarios/working` with chaining role `parent`, `bridge`, or `child`. Standalone scenarios (chaining role `none`) are excluded, per instruction, since Make's own metadata already confirms they have no subscenario relationship.

**Method:** read-only `scenarios_get` (blueprint) inspection. No scenario was run, enabled, disabled, edited, rescheduled, or otherwise modified.

**Result:** 20 of 22 scenarios resolved. 2 remain unresolved because the follow-up was stopped before their blueprints were read: `M.com: New Adviser Assigned in Masterboard (Mar 26)` (8890068) and `M.com: New item in Mortgage App Copy to Masterboard End Forms (Jan 26)` (8410524).

## Key finding: one shared error-notification utility dominates the graph

`Outlook: Email Notification after Failed Scenario` (8732008) is called by **19 of the 20 resolved scenarios** — confirmed from blueprint, in every case as either an `onerror` handler or an explicit validation-failure branch. It calls nothing itself. This is a cross-cutting shared utility, not a business automation, and should **not** receive its own canonical automation ID — document it once as a shared system component and reference it from every automation that uses it.

## Confirmed business-logic subscenario links (not counting the shared error utility)

Only two genuine business-logic subscenario calls were found across all 20 resolved scenarios:

- `M.com to AffordX Application Creation (Jul 2025)` (6468551) calls `AffordX Subflow Client Creation (Sep 2025)` (7292131) — confirmed from blueprint, main flow.
- `AffordX to M.com Applications Sync (Aug 2025)` (6238398) calls a scenario referenced as `Subflow Application Creation Monday-AffordX (Apr 2026)` (id 9067654) — confirmed from blueprint, main flow, but **this target ID does not exist in `Valid scenarios/working`**. It may live in another folder, have been renamed, or been deleted. Needs manual lookup.

## Probable automation families

### AffordX Mortgage Application Sync

- **AffordX Subflow Client Creation (Sep 2025)** (7292131) (reusable utility, not an independent automation)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: M.com to AffordX Application Creation (Jul 2025) (6468551)
  - Needs verification: Reusable subflow/utility, recommend documenting as a shared component rather than a standalone canonical automation
- **AffordX to M.com Applications Sync (Aug 2025)** (6238398)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008), Subflow Application Creation Monday-AffordX (Apr 2026) (unknown)
  - Called by: none confirmed
- **M.com to AffordX Application Creation (Jul 2025)** (6468551)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008), AffordX Subflow Client Creation (Sep 2025) (7292131)
  - Called by: none confirmed

### Aircall Call Processing

- **Aircall Transcript Summary** (6123035)
  - Calls: none confirmed
  - Called by: none confirmed
- **M.com: Aircall Upload Transcriptions To SP (Jul 2026)** (9498962)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed
- **M.com: Calls > Unknown/Client** (5543887)
  - Calls: none confirmed
  - Called by: none confirmed
- **M.com: New item in Contacts (Aircall) -> Delete** (6548539)
  - Calls: none confirmed
  - Called by: none confirmed

### MacroForge End-Forms Trigger

- **Macroforge to M.com: End Forms Filled (May 2026)** (9254149)
  - Calls: none confirmed
  - Called by: none confirmed
- **M.com to Macroforge: Trigger Macroforge End Forms Filling Flow (Feb 2026)** (8731317)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed

### Masterboard / Bank Change Sync

- **M.com: Banks to send change in Masterboard v2 (Feb 26)** (8666173)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed
- **M.com: New Adviser Assigned in Masterboard (Mar 26)** (8890068)
  - Calls: unknown (unknown)
  - Called by: none confirmed
  - Needs verification: Blueprint inspection not completed for this scenario in this follow-up pass, subscenario call targets remain unresolved
- **M.com: New item in Mortgage App Copy to Masterboard End Forms (Jan 26)** (8410524)
  - Calls: unknown (unknown)
  - Called by: none confirmed
  - Needs verification: Blueprint inspection not completed for this scenario in this follow-up pass, subscenario call targets remain unresolved

### SharePoint and Documents

- **M.com: Branded SOP Filling and Filing (Jul 2026)** (9555578)
  - Calls: none confirmed
  - Called by: none confirmed
- **M.com: Review Broken SP Links on CP Board (May 2026)** (9277255)
  - Calls: none confirmed
  - Called by: none confirmed

### Client Profile / Contact Lifecycle

- **M.com: Connect Entities to Mortgage Pipeline (Dec25)** (8278547)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed
- **M.com: CP and Deals Renaming after Contact Renaming** (1054927)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed
- **M.com: Creating Contact and Client Profile after Lead was Added (Mar 2026)** (8800779)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed

### Mortgage Fixed-Rate Expiry Alerts

- **M.com: Fixed Rate Expiry Email Alert (May25)** (4840595)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed

### Insurance Policy Lifecycle

- **M.com: Insurance Expiry Email (Jul 2025)** (6279522)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed
- **M.com: Renaming after Insurance Policy Added or Owner/Provider Change (Feb 2026)** (1215342)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed
- **M.com Reset Status And Reminder From Exisitng Insurance** (9235525)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed
- **Real Savvy Insurance Unsubscribe (11Sep)** (7178534)
  - Calls: none confirmed
  - Called by: none confirmed

### Mortgage Applications

- **M.com: Mortgage renewals board, assign adviser and support** (722853)
  - Calls: none confirmed
  - Called by: none confirmed
- **M.com: Update Existing Mortgages Name from Borrowers (Dec25)** (1228763)
  - Calls: none confirmed
  - Called by: none confirmed

### Form Submission Filing (IQ/MA/KQ)

- **M.com: New Form Submission in IQ/MA/KQ (Jun 2026)** (9447215)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed

### Pigeon Integration Suite

- **M.com: Pigeon Board to Mortgage Pipeline (Nov 25)** (7950443)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed
- **M.com: Pigeon Documents to Mortgage Pipeline (Dec 25)** (8367350)
  - Calls: none confirmed
  - Called by: none confirmed
- **M.com: Pigeon Notes to Mortgage Pipeline (Dec 25)** (8399114)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed
- **M.com: Verification in Pigeon to Mortgage Pipeline (Dec 25)** (8356342)
  - Calls: none confirmed
  - Called by: none confirmed
- **Pigeon to M.com: Request Creation (Nov25)** (7883004)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed

### Client Profile / Contact Lifecycle (shared search utility)

- **M.com: Subflow Search Contacts in Monday (Feb 26)** (8518416) (reusable utility, not an independent automation)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed
  - Needs verification: No confirmed caller found among the scenarios inspected in this pass, parent may lie outside the fetched set; Reusable subflow/utility, recommend documenting as a shared component rather than a standalone canonical automation

### Unsubscribe / Email Preference

- **M.Com: Unsubscribe Client Level (May 26)** (9229914)
  - Calls: Outlook: Email Notification after Failed Scenario (8732008)
  - Called by: none confirmed
- **Real Savvy Unsubscribe (12May)** (5195381)
  - Calls: none confirmed
  - Called by: none confirmed

### Leads and Client Profiles

- **M.com: Update Dependents (Dec25)** (8260037)
  - Calls: none confirmed
  - Called by: none confirmed
- **M.com: Updates profile name when participants added** (1054932)
  - Calls: none confirmed
  - Called by: none confirmed
- **M.com: CRM Migration - Connect Client Profiles and Pipelines (Dec25)** (8264526)
  - Calls: none confirmed
  - Called by: none confirmed

### General / Shared Utilities

- **Monday Board Columns Generator from JSON** (8440979)
  - Calls: none confirmed
  - Called by: none confirmed

### Shared utility (cross-cutting, not a business family)

- **Outlook: Email Notification after Failed Scenario** (8732008) — called by 19 scenarios, calls nothing.

## Scenarios that should not receive their own canonical automation ID

These are reusable subflows/utilities that other automations depend on, not independent business processes:

- `AffordX Subflow Client Creation (Sep 2025)` (7292131) — 1 confirmed caller(s). Document as a shared component and cross-reference it from each caller's automation doc.
- `M.com: Subflow Search Contacts in Monday (Feb 26)` (8518416) — 0 confirmed caller(s). Document as a shared component and cross-reference it from each caller's automation doc.
- `Outlook: Email Notification after Failed Scenario` (8732008) — 19 confirmed caller(s). Document as a shared component and cross-reference it from each caller's automation doc.

## Unresolved

- `M.com: New Adviser Assigned in Masterboard (Mar 26)` (8890068) — chaining role `parent`, confirmed to call at least one subscenario (per `scenarios_list` module data), but blueprint was not read. Exact target(s) unknown.
- `M.com: New item in Mortgage App Copy to Masterboard End Forms (Jan 26)` (8410524) — chaining role `parent`, confirmed to call at least one subscenario (per `scenarios_list` module data), but blueprint was not read. Exact target(s) unknown.
