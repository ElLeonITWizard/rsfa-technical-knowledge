---
id: RSFA-AUTOMATION-REGISTRY
title: RSFA Automation Registry
status: active
owner: RSFA
audience:
  - Authorised developers
  - Authorised technical consultants
last_modified: 2026-10-31
last_verified: 2026-09-05
---

# RSFA Automation Registry

## 1. Purpose

This document is the master registry of RSFA automations, workflows, native integrations and reusable automation components.

It helps authorised technical users identify the automation related to a ticket, understand dependencies, distinguish business automations from technical subflows, locate exact platform components and prioritise documentation and maintenance.

This registry is an index. Detailed implementation logic belongs under `knowledge/automations/`.

---

## 2. Registry conventions

### Status

| Status | Meaning |
|---|---|
| `Active` | In production and currently used |
| `Active - Under Improvement` | In production while improvements are implemented |
| `Active - Planned Retirement` | Still active but expected to be removed |
| `Testing` | Under controlled testing |
| `Planned` | Not yet in production |
| `Inactive` | Present but disabled |
| `Deprecated` | Replaced or no longer intended for use |
| `Unknown - Verification Required` | Current state not confirmed |

### Criticality

| Criticality | Meaning |
|---|---|
| `Critical` | Failure can materially disrupt core client or operational processing |
| `High` | Failure significantly affects an important process |
| `Medium` | Failure affects efficiency or a limited workflow |
| `Low` | Utility, experiment or low-impact process |

### Documentation status

| Status | Meaning |
|---|---|
| `Documented` | Current canonical documentation exists and is verified |
| `Partially documented` | Useful documentation exists but is incomplete or not fully current |
| `Outdated documentation` | Existing documentation does not reliably describe current behaviour |
| `Not documented` | No canonical document exists |
| `Unknown` | Documentation status has not been reviewed |

---

## 3. Canonical automation registry

| Automation ID | Canonical automation | Platform | Status | Criticality | Main trigger | Main outcome | Main systems | Documentation | Detailed file |
|---|---|---|---|---|---|---|---|---|---|
| `AUTO-EMAIL-001` | Client Email Filing and Overflow Processing | Power Automate | Active | Critical | Incoming and sent Outlook emails | Files client emails and attachments, updates Client Profiles and routes unmatched emails | Outlook, SharePoint, Monday.com, Slack, Real Savvy Ref | Partially documented | knowledge/automations/power-automate/AUTO-EMAIL-001-client-email-filing.md |
| `AUTO-DOCUSIGN-001` | DocuSign Signed Document Filing | Power Automate | Active - Planned Retirement | High | Completed DocuSign envelope | Files signed documents in SharePoint and sends Slack notifications | DocuSign, Power Automate, SharePoint, Slack | Partially documented | knowledge/automations/power-automate/AUTO-DOCUSIGN-001-docusign-filing.md |
| `AUTO-SP-FOLDER-001` | Client SharePoint Folder Lifecycle | Power Automate | Active | High | Client Profile create, rename, permission or maintenance event | Creates, renames, permissions and maintains Client Profile folders | Monday.com, Power Automate, SharePoint | Partially documented | knowledge/automations/power-automate/AUTO-SP-FOLDER-001-client-folder-lifecycle.md |
| `AUTO-EMAIL-BACKUP-001` | Email Backup and Failed Item Recovery | Power Automate | Active | High | Manual or scheduled backup/recovery trigger | Backs up mailbox content and retries failed email-filing items | Outlook, Power Automate, SharePoint | Partially documented | knowledge/automations/power-automate/AUTO-EMAIL-BACKUP-001-email-backup-recovery.md |
| `AUTO-MONDAY-BACKUP-001` | Monday Activities and Emails Backup | Power Automate | Active | High | Scheduled or manual backup trigger | Backs up large Monday activity and Emails & Activities datasets | Monday.com, Power Automate, SharePoint | Partially documented | knowledge/automations/power-automate/AUTO-MONDAY-BACKUP-001-activity-backup.md |
| `AUTO-AIRCALL-001` | Aircall Call Processing, Transcription and Summary | Make.com + native integration | Active - Under Improvement | High | Aircall call record created in Monday | Matches client, classifies calls, generates transcription and AI summary, files documents and updates Monday | Aircall, Monday.com, Make.com, SharePoint, OpenAI, Word, Slack | Partially documented | knowledge/automations/make/AUTO-AIRCALL-001-aircall-call-processing.md |
| `AUTO-MASTERBOARD-001` | Mortgage Application to Masterboard End Forms | Make.com | Active | Critical | New or changed Mortgage Application / Masterboard event | Copies and synchronises application data into Masterboard End Forms | Monday.com, Make.com, Outlook | Partially documented | knowledge/automations/make/AUTO-MASTERBOARD-001-mortgage-app-to-masterboard.md |
| `AUTO-MACROFORGE-001` | MacroForge End-Forms Integration | Make.com | Active | Critical | Approved Monday data or MacroForge completion webhook | Sends approved payloads to MacroForge and records completion in Monday | Monday.com, Make.com, MacroForge, Google Cloud, OpenAI | Partially documented | knowledge/automations/make/AUTO-MACROFORGE-001-end-forms-integration.md |
| `AUTO-BRANDED-SOP-001` | Branded Mortgage SOP Generation | Make.com | Active | High | Approved SOP generation request | Generates and files an editable branded DOCX | Monday.com, Make.com, Word, SharePoint | Partially documented | knowledge/automations/make/AUTO-BRANDED-SOP-001-branded-sop-generation.md |
| `AUTO-AFFORDX-001` | AffordX Mortgage Application Synchronisation | Make.com | Active | High | Monday application change and scheduled AffordX sync | Creates AffordX applications and synchronises application/client information | Monday.com, Make.com, AffordX, HTTP API | Partially documented | knowledge/automations/make/AUTO-AFFORDX-001-mortgage-application-sync.md |
| `AUTO-PIGEON-001` | Pigeon Integration Suite | Make.com | Active | High | Pigeon request, document, note or verification webhook | Synchronises Pigeon records, documents, notes and verification with Mortgage Pipeline | Pigeon, Monday.com, Make.com, SharePoint, Outlook | Partially documented | knowledge/automations/make/AUTO-PIGEON-001-integration-suite.md |
| `AUTO-FORMS-001` | New Form Submission Filing | Make.com + Superforms / Monday Forms | Active | High | New IQ, MA or KQ submission | Files form documents, updates Monday and sends notifications | Superforms, Monday Forms, Monday.com, Make.com, SharePoint, Outlook, Slack | Partially documented | knowledge/automations/make/AUTO-FORMS-001-new-form-submission.md |
| `AUTO-LEADS-001` | Lead to Contact and Client Profile Creation | Make.com + Monday Workflow | Active | Critical | New lead and pipeline status change | Creates Contacts and Client Profiles and routes records to pipelines | Monday.com, Make.com, Monday Workflows | Partially documented | knowledge/automations/make/AUTO-LEADS-001-lead-client-profile-creation.md |
| `AUTO-MORTGAGE-RENEWAL-001` | Mortgage Fixed Rate Expiry and Renewal | Make.com | Active | High | Fixed Rate Expiry reminder window | Sends reminders and supports renewal movement | Monday.com, Make.com, Outlook, Slack | Partially documented | knowledge/automations/make/AUTO-MORTGAGE-RENEWAL-001-fixed-rate-expiry.md |
| `AUTO-INSURANCE-RENEWAL-001` | Insurance Expiry and Anniversary Processing | Make.com | Active | High | Insurance expiry or anniversary reminder window | Sends reminders and resets reminder state | Monday.com, Make.com, Outlook, Slack | Partially documented | knowledge/automations/make/AUTO-INSURANCE-RENEWAL-001-insurance-expiry.md |
| `AUTO-NAMING-001` | Client, Deal and Policy Naming Synchronisation | Make.com | Active | Medium | Contact, participant, borrower, adviser or policy ownership change | Keeps related names aligned | Monday.com, Make.com | Partially documented | knowledge/automations/make/AUTO-NAMING-001-record-naming-sync.md |
| `AUTO-UNSUBSCRIBE-001` | Client Unsubscribe and Email Preferences | Make.com | Active | Medium | Client unsubscribe webhook | Updates client and insurance email preferences | Monday.com, Make.com, Outlook | Partially documented | knowledge/automations/make/AUTO-UNSUBSCRIBE-001-email-preferences.md |
| `AUTO-MONDAY-WF-001` | Move to Pipeline Workflow (New) | Monday Workflow | Deprecated (superseded 2026-09-05 by Make `9756260`, per RSFA) | Critical | Pipeline Status changes on Leads | Creates Mortgage, Insurance or KiwiSaver pipeline records | Monday.com | Partially documented | knowledge/automations/monday/AUTO-MONDAY-WF-001-move-to-pipeline.md |
| `AUTO-MONDAY-WF-002` | Leads App 2 Creation + CP Name | Monday Workflow | Deprecated (deactivated 2026-09-05, per RSFA, no replacement) | High | Leads Form application contains two applicants | Creates second lead and supports Client Profile naming | Monday.com | Partially documented | knowledge/automations/monday/AUTO-MONDAY-WF-002-second-applicant.md |
| `AUTO-DOCUSEAL-001` | DocuSeal Submission Lifecycle Sync | Make.com | Active | High | DocuSeal webhook event (submission created/sent/viewed/completed/declined/expired) | Creates/updates a Monday tracking item per DocuSeal submission, links Client Profile where possible, sends Slack milestone notifications | DocuSeal, Make.com, Monday.com, Slack | Partially documented | knowledge/automations/make/AUTO-DOCUSEAL-001-docuseal-submission-lifecycle-sync.md |
| `COMP-MAKE-ERROR-001` | Shared Make Failure Email Notification | Make.com shared component | Active | High | Error branch or validation failure | Sends a standard Outlook failure notification | Make.com, Outlook | Partially documented | knowledge/automations/make/components/COMP-MAKE-ERROR-001-failure-email.md |

---

## 4. Make.com inventory summary

**Re-verified live via the Make MCP connector on 2026-09-05** (org RSFA `882256`, team `85772`, zone `eu2.make.com` — confirmed to match the expected org). The Make.com folder `Valid scenarios/working` now contains **43 scenarios**: **40 active** and **3 inactive**, up from the 38 (36 active / 2 inactive) recorded on 2026-07-30. Two additional folders exist outside the working set: `Archive scenarios` (17 scenarios, all historical/pre-2026, unchanged) and a new `Claude Testing` folder (1 experimental POC scenario, `M.com: Claude Scenario Creation POC (Jul 2026)`, id `9597960` — not a production automation, not documented further here).

**Confirmed from live system — changes since 2026-07-30:**

- **5 new scenarios** in `Valid scenarios/working`:
  - `9662353` — M.com: Subflow AffordX to Existing Mortgages Sync (Aug 2026) — see `AUTO-AFFORDX-001` §10a.
  - `9721689` — M.com: AffordX item Need Sync to Existing Mortgages (Aug 2026) — see `AUTO-AFFORDX-001` §10a.
  - `9756260` — M.com: Move to Pipeline (Sep 2026) — see `AUTO-LEADS-001` and `knowledge/automations/monday/AUTO-MONDAY-WF-001-move-to-pipeline.md` (superseded).
  - `9627714` — M.com: Contact Change in Aircall Board (Jul 2026) — see `AUTO-AIRCALL-001`.
  - `9627699` — M.com: New Transcription in Aircall (Jul 2026) — see `AUTO-AIRCALL-001`.
- **1 scenario changed Active → Inactive:** `Aircall Transcript Summary` (`6123035`), last edited 2026-08-08. Not confirmed why it was deactivated, but its timing (edited two days after the two new Aircall scenarios above were created on 2026-08-06) strongly suggests it was superseded by them — not silently assumed, see `AUTO-AIRCALL-001` §18.

The call graph previously resolved 20 of 22 chained scenarios, with two parent scenarios recorded as having unresolved call targets:

- `M.com: New Adviser Assigned in Masterboard (Mar 26)` (`8890068`) — **resolved 2026-09-05**: live blueprint inspection shows its only subscenario calls are the standard error-notification component (`8732008`); it has no other business subscenario target. **New security finding (2026-09-05):** this scenario's `Get Adviser Data` HTTP module contains a hardcoded, literal Monday.com API bearer token in its Authorization header, instead of a Connection Reference. The literal value was not persisted anywhere in this repository. This is a live-credential exposure finding, additional to the ones already recorded for Power Automate in `exports/power-automate/README.md` and §5.1 below — **this credential should be rotated**.
- `M.com: New item in Mortgage App Copy to Masterboard End Forms (Jan 26)` (`8410524`) — attempted re-verification on 2026-09-05 failed twice with a Make API 502 (Bad Gateway) error; still unresolved, retry needed.

`Outlook: Email Notification after Failed Scenario` (`8732008`) is a shared utility used by 19+ resolved scenarios. It is registered as `COMP-MAKE-ERROR-001`, not as an independent business automation.

### Make.com scenario inventory

| Exact Make name | Scenario ID | Status | Trigger | Functional area | Relationship | Main systems | Canonical family | Last modified | Verification notes |
|---|---:|---|---|---|---|---|---|---|---|
| AffordX Subflow Client Creation (Sep 2025) | `7292131` | Active | On-demand (called by parent scenario) | Mortgage Applications | parent (also callable as subscenario) | HTTP / Custom API | AffordX Mortgage Application Sync | 2026-04-14 | — |
| AffordX to M.com Applications Sync (Aug 2025) | `6238398` | Active | Scheduled (daily 08:00) | Mortgage Applications | parent | HTTP / Custom API, Monday.com | AffordX Mortgage Application Sync | 2026-04-22 | Target scenario id 9067654 not found in Valid scenarios/working, confirm its actual location |
| Aircall Transcript Summary | `6123035` | Active | Monday.com instant trigger (watch) | Aircall | standalone | Make AI Tools, Aircall, Monday.com | Aircall Call Processing | 2026-02-23 | — |
| Macroforge to M.com: End Forms Filled (May 2026) | `9254149` | Active | Webhook (custom webhook) | MacroForge | standalone | Webhook Gateway, Monday.com | MacroForge End-Forms Trigger | 2026-07-16 | — |
| M.com: Aircall Upload Transcriptions To SP (Jul 2026) | `9498962` | Active | Monday.com instant trigger (watch) | Aircall | parent | Aircall, Docx Templater, Microsoft SharePoint, Monday.com, OpenAI (GPT), Slack | Aircall Call Processing | 2026-07-29 | — |
| M.com: Banks to send change in Masterboard v2 (Feb 26) | `8666173` | Active | Webhook (custom webhook) | Masterboard / End Forms | parent | Webhook Gateway, Microsoft Outlook/Email, Monday.com | Masterboard / Bank Change Sync | 2026-05-18 | — |
| M.com: Branded SOP Filling and Filing (Jul 2026) | `9555578` | Active | Webhook (custom webhook) | SharePoint and Documents | standalone | Docx Templater, Webhook Gateway, Microsoft SharePoint, Monday.com | SharePoint and Documents | 2026-07-23 | — |
| M.com: Calls > Unknown/Client | `5543887` | Active | Monday.com instant trigger (watch) | Aircall | standalone | Monday.com | Aircall Call Processing | 2026-07-08 | — |
| M.com: Connect Entities to Mortgage Pipeline (Dec25) | `8278547` | Active | Webhook (custom webhook) | Mortgage Applications | parent | Webhook Gateway, Monday.com | Client Profile / Contact Lifecycle | 2026-02-25 | — |
| M.com: CP and Deals Renaming after Contact Renaming | `1054927` | Active | Monday.com instant trigger (watch) | Leads and Client Profiles | parent | HTTP / Custom API, Monday.com | Client Profile / Contact Lifecycle | 2026-02-25 | — |
| M.com: Creating Contact and Client Profile after Lead was Added (Mar 2026) | `8800779` | Active | Webhook (custom webhook) | Leads and Client Profiles | parent | Webhook Gateway, Monday.com | Client Profile / Contact Lifecycle | 2026-04-08 | — |
| M.com: Fixed Rate Expiry Email Alert (May25) | `4840595` | Active | Scheduled (every 900s, restricted window) | Mortgage Applications | parent | Microsoft Outlook/Email, Monday.com, Slack | Mortgage Fixed-Rate Expiry Alerts | 2026-07-07 | — |
| M.com: Insurance Expiry Email (Jul 2025) | `6279522` | Active | Scheduled (every 900s, restricted window) | Insurance | parent | Microsoft Outlook/Email, Monday.com, Slack | Insurance Policy Lifecycle | 2026-07-08 | — |
| M.com: Mortgage renewals board, assign adviser and support | `722853` | Active | Monday.com instant trigger (watch) | Mortgage Applications | standalone | Monday.com | Mortgage Applications | 2024-07-17 | — |
| M.com: New Adviser Assigned in Masterboard (Mar 26) | `8890068` | Active | Webhook (custom webhook) | Masterboard / End Forms | parent | Webhook Gateway, HTTP / Custom API, Monday.com | Masterboard / Bank Change Sync | 2026-05-18 | Resolved 2026-09-05: only subscenario call is the standard error handler (`8732008`); no other unresolved target. Hardcoded live Monday API token found in an HTTP module — see §4 |
| M.com: New Form Submission in IQ/MA/KQ (Jun 2026) | `9447215` | Active | Webhook (custom webhook) | SharePoint and Documents | parent | Webhook Gateway, Microsoft Outlook/Email, Microsoft SharePoint, Monday.com, Slack | Form Submission Filing (IQ/MA/KQ) | 2026-07-13 | — |
| M.com: New item in Contacts (Aircall) -> Delete | `6548539` | Active | Monday.com instant trigger (watch) | Aircall | standalone | Monday.com | Aircall Call Processing | 2026-02-18 | — |
| M.com: New item in Mortgage App Copy to Masterboard End Forms (Jan 26) | `8410524` | Active | Webhook (custom webhook) | Masterboard / End Forms | parent | Webhook Gateway, Microsoft Outlook/Email, Monday.com | Masterboard / Bank Change Sync | 2026-07-07 | Blueprint inspection not completed for this scenario in this follow-up pass, subscenario call targets remain unresolved |
| M.com: Pigeon Board to Mortgage Pipeline (Nov 25) | `7950443` | Active | Webhook (custom webhook) | Pigeon | parent | Webhook Gateway, HTTP / Custom API, Microsoft SharePoint, Monday.com | Pigeon Integration Suite | 2026-03-12 | — |
| M.com: Pigeon Documents to Mortgage Pipeline (Dec 25) | `8367350` | Active | Webhook (custom webhook) | Pigeon | standalone | Webhook Gateway, HTTP / Custom API, Microsoft Outlook/Email, Microsoft SharePoint, Monday.com | Pigeon Integration Suite | 2026-01-21 | — |
| M.com: Pigeon Notes to Mortgage Pipeline (Dec 25) | `8399114` | Active | Webhook (custom webhook) | Pigeon | parent | Webhook Gateway, Monday.com | Pigeon Integration Suite | 2026-02-25 | — |
| M.com: Renaming after Insurance Policy Added or Owner/Provider Change (Feb 2026) | `1215342` | Active | Webhook (custom webhook) | Insurance | parent | Webhook Gateway, Monday.com | Insurance Policy Lifecycle | 2026-02-25 | — |
| M.com Reset Status And Reminder From Exisitng Insurance | `9235525` | Active | Unknown/other (monthly) | Insurance | parent | Monday.com | Insurance Policy Lifecycle | 2026-05-18 | — |
| M.com: Subflow Search Contacts in Monday (Feb 26) | `8518416` | Active | On-demand (called by parent scenario) | Leads and Client Profiles | parent (also callable as subscenario) | Monday.com | Client Profile / Contact Lifecycle (shared search utility) | 2026-03-07 | Resolved 2026-09-05: confirmed callers are `Subflow Application Creation Monday-AffordX (Apr 2026)` (`9067654`) and `M.com: Subflow AffordX to Existing Mortgages Sync (Aug 2026)` (`9662353`), both via live blueprint inspection. Both callers belong to the AffordX family, not Leads — its presence in the "Leads and Client Profiles" functional area in this table is by module content (searches the Contacts board), not by confirmed caller |
| M.com to AffordX Application Creation (Jul 2025) | `6468551` | Active | Monday.com instant trigger (watch) | Mortgage Applications | parent | HTTP / Custom API, Monday.com | AffordX Mortgage Application Sync | 2026-04-14 | — |
| M.com to Macroforge: Trigger Macroforge End Forms Filling Flow (Feb 2026) | `8731317` | Active | Monday.com instant trigger (watch) | MacroForge | parent | code, HTTP / Custom API, Monday.com, OpenAI (GPT) | MacroForge End-Forms Trigger | 2026-07-16 | — |
| M.Com: Unsubscribe Client Level (May 26) | `9229914` | Active | Webhook (custom webhook) | Email Campaigns | parent | Webhook Gateway, Monday.com | Unsubscribe / Email Preference | 2026-05-14 | — |
| M.com: Update Dependents (Dec25) | `8260037` | Active | Webhook (custom webhook) | Leads and Client Profiles | standalone | Webhook Gateway, Monday.com | Leads and Client Profiles | 2026-02-25 | — |
| M.com: Update Existing Mortgages Name from Borrowers (Dec25) | `1228763` | Active | Monday.com instant trigger (watch) | Mortgage Applications | standalone | Monday.com | Mortgage Applications | 2025-12-12 | — |
| M.com: Update Mortgage Pipeline Name from Borrowers (Dec25) | `1232945` | Active | Monday.com instant trigger (watch) | Mortgage Applications | standalone | Monday.com | Mortgage Applications | 2025-12-12 | Added 2026-10-31 (Confirmed from live system). Canonical owner: `AUTO-NAMING-001` |
| RSFA – End Forms: Client Profile link and record name sync | `10037840` | Active | Scheduled, every 900 s | Masterboard / End Forms | standalone | Monday.com | Masterboard / Bank Change Sync | 2026-10-25 | Added 2026-10-31 (Confirmed from live system). Keeps SOP Masterboard `5026186805` CP link and item name in sync; reads the first 500 items only. Not yet documented in a canonical automation file |
| M.com: Lead Rename by ClientProfile (Mar 2026) | `9711585` | Inactive | Webhook (custom webhook, hook `4335040`) | Leads and Client Profiles | standalone | Webhook Gateway | Leads and Client Profiles | 2026-08-25 | Added 2026-10-31 (Confirmed from live system). Unfinished shell: webhook module only; no Monday webhook targets it |
| M.com: Updates profile name when participants added | `1054932` | Active | Monday.com instant trigger (watch) | Leads and Client Profiles | standalone | Monday.com | Leads and Client Profiles | 2025-12-09 | — |
| M.com: Verification in Pigeon to Mortgage Pipeline (Dec 25) | `8356342` | Active | Webhook (custom webhook) | Pigeon | standalone | Webhook Gateway, Microsoft Outlook/Email, Monday.com | Pigeon Integration Suite | 2026-01-21 | — |
| M.com: AffordX item Need Sync to Existing Mortgages (Aug 2026) | `9721689` | Active | Webhook (custom webhook) | Mortgage Applications | parent | Webhook Gateway, Monday.com | AffordX Mortgage Application Sync | 2026-09-04 | New 2026-09-05. Calls `9662353` as a bridge subflow; confirmed live via blueprint inspection — see `AUTO-AFFORDX-001` §10a |
| M.com: Subflow AffordX to Existing Mortgages Sync (Aug 2026) | `9662353` | Active | On-demand (called by parent scenario) | Mortgage Applications | bridge (also callable as subscenario) | Monday.com, Slack | AffordX Mortgage Application Sync | 2026-09-05 | New 2026-09-05. Calls `8518416` (Search Contacts); confirmed live via blueprint inspection — see `AUTO-AFFORDX-001` §10a |
| M.com: Move to Pipeline (Sep 2026) | `9756260` | Active | Webhook (custom webhook) | Leads and Client Profiles | standalone | Webhook Gateway, Monday.com | Leads and Client Profiles | 2026-09-04 | New 2026-09-05, created 2026-09-03. Routes Leads `Pipeline Status` changes to Mortgage/Insurance/KiwiSaver Pipeline; confirmed live via blueprint inspection. Supersedes the native Monday Workflow `AUTO-MONDAY-WF-001` per RSFA — see `knowledge/automations/monday/AUTO-MONDAY-WF-001-move-to-pipeline.md` |
| M.com: Contact Change in Aircall Board (Jul 2026) | `9627714` | Active | Webhook (custom webhook) | Aircall | standalone | Webhook Gateway, Monday.com | Aircall Call Processing | 2026-08-11 | New 2026-09-05, created 2026-08-06. Calls `9498962` when a call's linked Contact changes; confirmed live via blueprint inspection — see `AUTO-AIRCALL-001` |
| M.com: DocuSeal Submission Lifecycle Sync (Sep 2026) | `9803640` | Active | Webhook (custom webhook, instant) | SharePoint and Documents | parent | Webhook Gateway, Monday.com, Slack, DocuSeal (custom/universal connector) | DocuSeal Submission Lifecycle Sync | 2026-09 (exact date not given) | New 2026-09-20, provided directly by RSFA as a blueprint export (not independently queried live). Calls `8518416` (Search Contacts) and `8732008` (error email) — see `AUTO-DOCUSEAL-001` |
| M.com: New Transcription in Aircall (Jul 2026) | `9627699` | Active | Aircall instant trigger (`transcription.created`) | Aircall | standalone | Aircall, Monday.com | Aircall Call Processing | 2026-08-06 | New 2026-09-05, created 2026-08-06. Aircall-native webhook trigger (not Monday-watch); calls `9498962`; confirmed live via blueprint inspection — see `AUTO-AIRCALL-001` |
| Monday Board Columns Generator from JSON | `8440979` | Active | On-demand (called by parent scenario) | General / Shared Utilities | standalone | Monday.com | General / Shared Utilities | 2026-03-09 | — |
| Outlook: Email Notification after Failed Scenario | `8732008` | Active | On-demand (called by parent scenario) | General / Shared Utilities | subscenario | Microsoft Outlook/Email | Shared utility (cross-cutting, not a business family) | 2026-02-23 | — |
| Pigeon to M.com: Request Creation (Nov25) | `7883004` | Active | Webhook (custom webhook) | Pigeon | parent | Webhook Gateway, Monday.com | Pigeon Integration Suite | 2026-02-25 | — |
| Real Savvy Insurance Unsubscribe (11Sep) | `7178534` | Active | Webhook (custom webhook) | Insurance | standalone | Webhook Gateway, Microsoft Outlook/Email, Monday.com | Insurance Policy Lifecycle | 2025-12-09 | — |
| Real Savvy Unsubscribe (12May) | `5195381` | Active | Webhook (custom webhook) | Email Campaigns | standalone | Webhook Gateway, Microsoft Outlook/Email, Monday.com | Unsubscribe / Email Preference | 2025-12-09 | — |
| M.com: CRM Migration - Connect Client Profiles and Pipelines (Dec25) | `8264526` | Inactive | On-demand (called by parent scenario) | Leads and Client Profiles | standalone | Monday.com | Leads and Client Profiles | 2025-12-12 | — |
| M.com: Review Broken SP Links on CP Board (May 2026) | `9277255` | Inactive | On-demand (called by parent scenario) | SharePoint and Documents | standalone | Microsoft SharePoint, Monday.com | SharePoint and Documents | 2026-05-22 | — |
| Aircall Transcript Summary | `6123035` | Inactive | Monday.com instant trigger (watch) | Aircall | standalone | Monday.com | Aircall Call Processing | 2026-08-08 | **Changed Active → Inactive since 2026-07-30** (confirmed 2026-09-05). Not confirmed why; likely superseded by the two new Aircall trigger scenarios (`9627699`, `9627714`) created two days before this scenario's last edit — see `AUTO-AIRCALL-001` §18 |

### Make.com family-to-scenario mapping

| Canonical family | Make scenarios |
|---|---|
| AffordX Mortgage Application Sync | `AffordX Subflow Client Creation (Sep 2025)` (`7292131`)<br>`AffordX to M.com Applications Sync (Aug 2025)` (`6238398`)<br>`M.com to AffordX Application Creation (Jul 2025)` (`6468551`)<br>`Subflow Application Creation Monday-AffordX (Apr 2026)` (`9067654`, found 2026-09-05 — lives outside any folder, see §8)<br>`M.com: AffordX item Need Sync to Existing Mortgages (Aug 2026)` (`9721689`, new)<br>`M.com: Subflow AffordX to Existing Mortgages Sync (Aug 2026)` (`9662353`, new) |
| Aircall Call Processing | `Aircall Transcript Summary` (`6123035`, now Inactive)<br>`M.com: Aircall Upload Transcriptions To SP (Jul 2026)` (`9498962`)<br>`M.com: Calls > Unknown/Client` (`5543887`)<br>`M.com: New item in Contacts (Aircall) -> Delete` (`6548539`)<br>`M.com: Contact Change in Aircall Board (Jul 2026)` (`9627714`, new)<br>`M.com: New Transcription in Aircall (Jul 2026)` (`9627699`, new) |
| Client Profile / Contact Lifecycle | `M.com: Connect Entities to Mortgage Pipeline (Dec25)` (`8278547`)<br>`M.com: CP and Deals Renaming after Contact Renaming` (`1054927`)<br>`M.com: Creating Contact and Client Profile after Lead was Added (Mar 2026)` (`8800779`) |
| Client Profile / Contact Lifecycle (shared search utility) | `M.com: Subflow Search Contacts in Monday (Feb 26)` (`8518416`) — now also called by `M.com: DocuSeal Submission Lifecycle Sync (Sep 2026)` (`9803640`, new 2026-09-20), in addition to its previously confirmed AffordX-family callers |
| DocuSeal Submission Lifecycle Sync | `M.com: DocuSeal Submission Lifecycle Sync (Sep 2026)` (`9803640`, new 2026-09-20) |
| Form Submission Filing (IQ/MA/KQ) | `M.com: New Form Submission in IQ/MA/KQ (Jun 2026)` (`9447215`) |
| General / Shared Utilities | `Monday Board Columns Generator from JSON` (`8440979`) |
| Insurance Policy Lifecycle | `M.com: Insurance Expiry Email (Jul 2025)` (`6279522`)<br>`M.com: Renaming after Insurance Policy Added or Owner/Provider Change (Feb 2026)` (`1215342`)<br>`M.com Reset Status And Reminder From Exisitng Insurance` (`9235525`)<br>`Real Savvy Insurance Unsubscribe (11Sep)` (`7178534`) |
| Leads and Client Profiles | `M.com: Update Dependents (Dec25)` (`8260037`)<br>`M.com: Updates profile name when participants added` (`1054932`)<br>`M.com: CRM Migration - Connect Client Profiles and Pipelines (Dec25)` (`8264526`)<br>`M.com: Move to Pipeline (Sep 2026)` (`9756260`, new — supersedes the native Monday Workflow `AUTO-MONDAY-WF-001` per RSFA) |
| MacroForge End-Forms Trigger | `Macroforge to M.com: End Forms Filled (May 2026)` (`9254149`)<br>`M.com to Macroforge: Trigger Macroforge End Forms Filling Flow (Feb 2026)` (`8731317`) |
| Masterboard / Bank Change Sync | `M.com: Banks to send change in Masterboard v2 (Feb 26)` (`8666173`)<br>`M.com: New Adviser Assigned in Masterboard (Mar 26)` (`8890068`)<br>`M.com: New item in Mortgage App Copy to Masterboard End Forms (Jan 26)` (`8410524`) |
| Mortgage Applications | `M.com: Mortgage renewals board, assign adviser and support` (`722853`)<br>`M.com: Update Existing Mortgages Name from Borrowers (Dec25)` (`1228763`)<br>`M.com: Update Mortgage Pipeline Name from Borrowers (Dec25)` (`1232945`, added 2026-10-31) |
| Mortgage Fixed-Rate Expiry Alerts | `M.com: Fixed Rate Expiry Email Alert (May25)` (`4840595`) |
| Pigeon Integration Suite | `M.com: Pigeon Board to Mortgage Pipeline (Nov 25)` (`7950443`)<br>`M.com: Pigeon Documents to Mortgage Pipeline (Dec 25)` (`8367350`)<br>`M.com: Pigeon Notes to Mortgage Pipeline (Dec 25)` (`8399114`)<br>`M.com: Verification in Pigeon to Mortgage Pipeline (Dec 25)` (`8356342`)<br>`Pigeon to M.com: Request Creation (Nov25)` (`7883004`) |
| SharePoint and Documents | `M.com: Branded SOP Filling and Filing (Jul 2026)` (`9555578`)<br>`M.com: Review Broken SP Links on CP Board (May 2026)` (`9277255`) |
| Shared utility (cross-cutting, not a business family) | `Outlook: Email Notification after Failed Scenario` (`8732008`) |
| Unsubscribe / Email Preference | `M.Com: Unsubscribe Client Level (May 26)` (`9229914`)<br>`Real Savvy Unsubscribe (12May)` (`5195381`) |

---

## 5. Power Automate flow inventory

Power Automate remains the principal platform for Outlook, SharePoint and other Microsoft-centric processes.

| Exact Power Automate flow name | Trigger type | Canonical automation | Current status | Notes |
|---|---|---|---|---|
| DocuSign to SharePoint | Automated | `AUTO-DOCUSIGN-001` | Active - Planned Retirement | Per RSFA (2026-09-20), RSFA plans to migrate to DocuSeal between October and November 2026 — see `AUTO-DOCUSEAL-001` and `knowledge/decisions/ADR-002-docusign-to-docuseal-migration.md`. Still active and relied upon today. |
| Main Outlook Inbox Email Filling | Instant child flow | `AUTO-EMAIL-001` | Active | Central reusable processing flow used by mailbox-specific and overflow flows. |
| Outlook Email Filing - Support v2 | Automated | `AUTO-EMAIL-001` | Active | — |
| Outlook Email Filing - Seth v2 | Automated | `AUTO-EMAIL-001` | Active | — |
| Outlook SENT Email Filling - Seth v2 | Automated | `AUTO-EMAIL-001` | Active | — |
| OLD Outlook SENT Email Filling - Jet v2 | Automated | `AUTO-EMAIL-001` | Active - Planned Retirement | Expected to retire when Jet mailbox and related overflow processes are removed. |
| Outlook Email Filing - Jet v2 | Automated | `AUTO-EMAIL-001` | Active - Planned Retirement | Expected to retire when Jet mailbox and related overflow processes are removed. |
| Outlook Email Filing - Kathleen v2 | Automated | `AUTO-EMAIL-001` | Active | — |
| Outlook SENT Email Filling - Kathleen v2 | Automated | `AUTO-EMAIL-001` | Active | — |
| Outlook SENT Email Filling - Rod v2 | Automated | `AUTO-EMAIL-001` | Active | — |
| Outlook Email Filing - Rod v2 | Automated | `AUTO-EMAIL-001` | Active | — |
| Email Filling Failed Items Processing | Scheduled | `AUTO-EMAIL-BACKUP-001` | Active | — |
| Overflow Emails Contact Matching | Instant | `AUTO-EMAIL-001` | Active | Part of unmatched-email matching, approval and reprocessing. |
| Overflow Emails Suggested Match Approval | Automated | `AUTO-EMAIL-001` | Active | Part of unmatched-email matching, approval and reprocessing. |
| Overflow Emails Related Client Profile Change | Automated | `AUTO-EMAIL-001` | Active | Part of unmatched-email matching, approval and reprocessing. |
| Monday Massive Activities Log Back Up | Scheduled | `AUTO-MONDAY-BACKUP-001` | Active | Bulk maintenance flow; execute only with explicit approval. |
| Monday Massive Emails & Activities Back Up | Instant | `AUTO-MONDAY-BACKUP-001` | Active | Bulk maintenance flow; execute only with explicit approval. |
| SharePoint - Client Folder Creation from Monday.com | Automated | `AUTO-SP-FOLDER-001` | Active | — |
| SharePoint - RSFA Assignees Permissions Creation and Modification | Automated | `AUTO-SP-FOLDER-001` | Active | — |
| Massive Client Folders Renaming | Instant | `AUTO-SP-FOLDER-001` | Active | Bulk maintenance flow; execute only with explicit approval. |
| SharePoint - Rename Client Folder from Monday.com | Automated | `AUTO-SP-FOLDER-001` | Active | — |
| Massive SP Files Renaming | Instant | `AUTO-SP-FOLDER-001` | Active | Bulk maintenance flow; execute only with explicit approval. |
| Email Back Up Generator | Manual | `AUTO-EMAIL-BACKUP-001` | Active | — |
| Moves Client Folder to Recycle Bin | Automated | `AUTO-SP-FOLDER-001` | Active | — |

### Power Automate automation families

#### AUTO-EMAIL-001 — Client Email Filing and Overflow Processing

Includes mailbox-specific received and sent flows, the central `Main Outlook Inbox Email Filling` child flow and Overflow Email matching/reprocessing. It matches Client Profiles, files `.eml` and attachments in SharePoint, updates Monday and Emails & Activities, sends Slack notifications and routes unmatched messages to adviser overflow workflows.

#### AUTO-SP-FOLDER-001 — Client SharePoint Folder Lifecycle

Includes folder creation, standard subfolders, Monday link updates, renaming, RSFA Assignees permission changes, movement to the recycle bin and controlled bulk rename utilities.

#### AUTO-EMAIL-BACKUP-001 — Email Backup and Failed Item Recovery

`Email Back Up Generator` processes mailbox folders in batches, delegates work to child flows and separates Processed and Failed outcomes.

#### AUTO-MONDAY-BACKUP-001 — Monday Activities and Emails Backup

Contains the large-scale backup flows for Monday activity records and Emails & Activities. Retention, destination and recovery procedures still require detailed documentation.

---

## 5.1 Power Automate Solution mapping

Read-only Power Automate Solution export evidence exists for a subset of the flows above under `exports/power-automate/solutions/`. See `exports/power-automate/solution-inventory.md` for the full flow-level mapping, including flows found in an export but not currently listed in §5 above, and vice versa. This table is a summary; the inventory file is authoritative for evidence status.

| Automation ID | Solution Unique Name | Exact flows (export evidence) | Export location | Evidence status |
|---|---|---|---|---|
| `AUTO-DOCUSIGN-001` | `DocuSigntoSharePoint` | `DocuSign to SharePoint ` | `exports/power-automate/solutions/docusign-to-sharepoint/` | Confirmed from export and canonical documentation |
| `AUTO-EMAIL-001` | `RSFAOutlookEmailFilling` | `Main Outlook Inbox Email Filling`, `OLD Outlook SENT Email Filling - Jet v2`, `Outlook SENT Email Filling - Rod v2`, `Outlook SENT Email Filling - Kathleen v2`, `Outlook Email Filing - Support v2`, `Overflow Emails Contact Matching`, `Overflow Emails Related Client Profile Change` | `exports/power-automate/solutions/rsfa-outlook-email-filing/` | Confirmed from export and canonical documentation |
| `AUTO-EMAIL-001` | `RSFAOutlookEmailFilling` | `Outlook Email Filling - Jet v2`, `Outlook Email Filling - Kathleen v2`, `Outlook Email Filling - Rod v2` | `exports/power-automate/solutions/rsfa-outlook-email-filing/` | Likely mapping — registry spells these "Filing", export spells them "Filling"; not silently corrected |
| `AUTO-EMAIL-001` (candidate) | `RSFAOutlookEmailFilling` | `Outlook INBOX items email filing (Rod)`, `Outlook INBOX items email filing (Kathleen)`, `Sent Emails Control`, `Outlook SENT Email Filling - Support v2` | `exports/power-automate/solutions/rsfa-outlook-email-filing/` | Unmapped Power Automate flow — canonical classification required. First two are for mailboxes already covered by other registered flows; last two have no equivalent registry entry at all |
| `AUTO-EMAIL-001` | *(no export in this set)* | `Outlook Email Filing - Seth v2`, `Outlook SENT Email Filling - Seth v2`, `Overflow Emails Suggested Match Approval` | — | Registered in §5 but absent from every current export — inverse gap, not resolved |
| `AUTO-EMAIL-BACKUP-001` | `RSFAOutlookEmailFilling` | `Email Filling Failed Items Processing` | `exports/power-automate/solutions/rsfa-outlook-email-filing/` | Confirmed from export and canonical documentation |
| `AUTO-SP-FOLDER-001` | `SPClientFolderCreationandRenaming` | `SharePoint - Client Folder Creation from Monday.com`, `SharePoint - Rename Client Folder from Monday.com` | `exports/power-automate/solutions/sp-client-folder-creation-and-renaming/` | Confirmed from export and canonical documentation |
| `AUTO-SP-FOLDER-001` | `SPAdviserNameChange` | `SharePoint - RSFA Asignees Permissions Creation and Modification` | `exports/power-automate/solutions/sp-adviser-name-change/` | Likely mapping — registry spells this "Assignees", export spells it "Asignees"; not silently corrected |
| `AUTO-SP-FOLDER-001` (candidate) | `SPAdviserNameChange` | `SharePoint - RSFA Asignees Permissions Modification` | `exports/power-automate/solutions/sp-adviser-name-change/` | Unmapped Power Automate flow — canonical classification required. Draft/not-activated in this export |

**`SPAdviserNameChange` naming note:** despite its display name, this Solution's flows implement RSFA Assignees permission creation/modification, not a client or adviser rename — the actual rename flow (`SharePoint - Rename Client Folder from Monday.com`) lives in the separate `SPClientFolderCreationandRenaming` Solution. See `exports/power-automate/solutions/sp-adviser-name-change/manifest.md` § "Known gaps".

**Security note:** several of the flows above were found, on export inspection, to contain hardcoded Monday.com and OpenAI credentials directly in their action definitions rather than in a Connection Reference. See each Solution manifest's Security Review section — this is a live-credential exposure finding, not just a documentation gap, and both credentials should be rotated.

---

## 6. Monday workflow inventory

RSFA has hundreds of board-level native automation recipes. They are not individually inventoried in this initial registry. The two confirmed active Monday Workflows are:

| Workflow ID | Exact workflow name | Status | Trigger | Outcome | Canonical automation |
|---|---|---|---|---|---|
| `AUTO-MONDAY-WF-001` | Move to Pipeline Workflow (New) | **Superseded 2026-09-05** — per RSFA, replaced by Make scenario `M.com: Move to Pipeline (Sep 2026)` (`9756260`). Board `5025429617` still exists, unchanged since 2025-12-04 (not independently confirmed disabled) | `Pipeline Status` changes on Leads | Creates records in Mortgage, Insurance or KiwiSaver pipelines | `AUTO-LEADS-001` |
| `AUTO-MONDAY-WF-002` | Leads App 2 Creation + CP Name | **Deprecated 2026-09-05** — per RSFA, deactivated outright, no replacement. A two-applicant Leads Form submission now produces a single Lead item. Board `5025430003` confirmed live unchanged since 2025-12-06 | A Leads Form application contains two applicants | Creates the second lead item and supports Client Profile naming | `AUTO-LEADS-001` |

**Both Monday Workflows above are now deprecated as of 2026-09-05** — per RSFA, RSFA no longer builds automation logic as Monday Workflow-builder automations, preferring Make.com, Power Automate, or minor per-board Monday Automations (native recipes, unaffected by this decision) instead. See `knowledge/decisions/ADR-001-deprecate-monday-workflows.md`.

Board-level recipes should initially be documented by business process. Create a separate registry entry only when a recipe starts or completes a critical process, triggers Make or Power Automate, moves records between important boards or requires dedicated testing and rollback.

---

## 7. Native integrations and automation-adjacent components

| Component | Type | Status | Role | Related canonical automation |
|---|---|---|---|---|
| Aircall native Monday integration | Native integration | Active | Creates Monday call records from Aircall events | `AUTO-AIRCALL-001` |
| Superforms to Monday | Native integration | Active - Expanding | Writes submissions directly into connected boards | `AUTO-FORMS-001`, `AUTO-MASTERBOARD-001`, `AUTO-LEADS-001` |
| Monday Forms to Monday | Native integration | Active - Reducing | Writes Leads and Insurance Questionnaire submissions into Monday | `AUTO-FORMS-001`, `AUTO-LEADS-001` |
| Monday Emails & Activities extension | Monday extension | Active | Displays client email and update timelines | `AUTO-EMAIL-001`, `AUTO-MONDAY-BACKUP-001`, `AUTO-AIRCALL-001` |
| Real Savvy Ref Outlook Add-in | Outlook add-in | Active | Retrieves Client Profile references and supports forced email matching | `AUTO-EMAIL-001` |
| Shared Make failure notification | Make subscenario | Active | Sends standard Outlook error notifications | `COMP-MAKE-ERROR-001` |

---

## 8. Reusable components without independent business automation IDs

| Component | Platform ID | Reason | Documentation approach |
|---|---:|---|---|
| Outlook: Email Notification after Failed Scenario | `8732008` | Cross-cutting utility called by 19 resolved scenarios | Document once as `COMP-MAKE-ERROR-001` |
| AffordX Subflow Client Creation (Sep 2025) | `7292131` | Reusable AffordX client-creation subflow | Document inside `AUTO-AFFORDX-001` |
| M.com: Subflow Search Contacts in Monday (Feb 26) | `8518416` | Shared search utility; all callers not yet identified | Document as shared component and verify callers |
| Subflow Application Creation Monday-AffordX (Apr 2026) | `9067654` | **Resolved 2026-09-05:** confirmed live — Active, `islinked: true`, lives outside any Make folder (not deleted, just unfiled), last edited 2026-08-26. Confirmed caller of `8518416` (Search Contacts). Document inside `AUTO-AFFORDX-001` | Document inside `AUTO-AFFORDX-001` |

---

## 9. Inactive, migration and maintenance components

| Platform | Exact name | Status | Recommended treatment |
|---|---|---|---|
| Make.com | M.com: CRM Migration - Connect Client Profiles and Pipelines (Dec25) | Inactive | Retain as historical migration utility until safe to archive |
| Make.com | M.com: Review Broken SP Links on CP Board (May 2026) | Inactive | Retain as maintenance utility and verify future need |
| Power Automate | OLD Outlook SENT Email Filling - Jet v2 | Active - Planned Retirement | Remove after Jet mailbox processes are retired |
| Power Automate | Outlook Email Filing - Jet v2 | Active - Planned Retirement | Remove after Jet mailbox processes are retired |
| Make.com | M.com: Lead Rename by ClientProfile (Mar 2026) (`9711585`) | Inactive (unfinished shell) | Retain; a completed version is proposed in `rsfa-automation-development/projects/client-profile-related-assets-renaming/` (not deployed) |
| Make.com | Aircall Transcript Summary | Inactive (changed since 2026-07-30) | Retain as historical utility; likely superseded by `9627699`/`9627714` — not confirmed, see `AUTO-AIRCALL-001` §18 |

---

## 10. Current verification and documentation gaps

- Exact Power Automate flow IDs, owners and connection references are not yet recorded.
- A new mailbox flow for `it-support@rsfa.co.nz` was reported active as of 2026-08-04 (RSFA report; exact flow name unconfirmed against export or registry — see `AUTO-EMAIL-001` §25). `leo@rsfa.co.nz` remains planned, not active.
- ~~The exact callers of `M.com: Subflow Search Contacts in Monday (Feb 26)` remain unconfirmed.~~ **Resolved 2026-09-05** (live): callers are `9067654` and `9662353`, both in the AffordX family.
- ~~`Subflow Application Creation Monday-AffordX (Apr 2026)` (`9067654`) must be located or confirmed deleted.~~ **Resolved 2026-09-05** (live): found, Active, unfiled (no folder).
- One Make parent call target remains unresolved: `8410524` (`8890068` resolved 2026-09-05 — see §4). Re-verification of `8410524` failed twice with a Make API 502 error on 2026-09-05; retry needed.
- **New 2026-09-05 (live):** a hardcoded, live Monday.com API bearer token was found in scenario `8890068`'s HTTP module — see §4. Not persisted in this repository; recommend rotation.
- The Monday board-level recipe inventory is incomplete.
- Exact destinations and retention rules for Monday backup flows require documentation.
- A long-term log of client-specific processed emails is partially addressed: the `Power Automate Runs` Monday board (`5030408927`) was **confirmed live on 2026-09-05** — see `knowledge/04_MONDAY_BOARDS_REGISTRY.md` §5. Its `Solution` dropdown is designed to cover all Power Automate solutions, but usage volume (13,217 items) is consistent with only the Email Filing flow family actually being connected today; not confirmed to log per-email Client Profile mapping specifically.
- Several Make functional summaries are inferred from names and module structure and require business verification.
- Most Make scenarios do not yet have a verified canonical automation document.
- **New 2026-09-05:** a new Make scenario, `M.com: Move to Pipeline (Sep 2026)` (`9756260`, created 2026-09-03), performs the same Leads → Pipeline routing function as the pre-existing native Monday Workflow `AUTO-MONDAY-WF-001` (board `5025429617`, unchanged since 2025-12-04). Per RSFA, the Make scenario is now the active implementation and the Monday Workflow is superseded/replaced — not independently verified beyond the Make blueprint and the unchanged state of the Workflow's own board; see `knowledge/automations/monday/AUTO-MONDAY-WF-001-move-to-pipeline.md`.
- **New 2026-09-20:** a new Make scenario, `M.com: DocuSeal Submission Lifecycle Sync (Sep 2026)` (`9803640`), was added directly via an RSFA-supplied blueprint export rather than a live Make MCP query — its presence in `Valid scenarios/working` and its exact creation date have not been independently confirmed live. Several notification-logic discrepancies were found reading its blueprint directly — see `AUTO-DOCUSEAL-001` §18. RSFA also reported a planned DocuSign → DocuSeal migration (October–November 2026) — see `knowledge/decisions/ADR-002-docusign-to-docuseal-migration.md`.

- **New 2026-10-31 (live, read-only):** naming conflict — `M.com: CP and Deals Renaming after Contact Renaming` (`1054927`) names Mortgage Pipeline and Existing Mortgages items with the Client Profile name, while `1228763` / `1232945` name them from Borrowers (RSFA: Borrowers is intended). No automation reacts to a Client Profile rename except the Power Automate SharePoint folder rename. See `AUTO-NAMING-001` §10b.

### 10.1 Contradictions and unresolved discrepancies found while drafting detailed automation documents (2026-07-30)

The following were identified while producing the detailed files under `knowledge/automations/`. None have been silently resolved — each is recorded in the affected document's "Known gaps" section and here for registry-level visibility.

- **`AUTO-MASTERBOARD-001`** — `source-material/make/M.com_ New Submission in ROMA Update Masterboard (Mar 26).md` describes a ROMA-to-Masterboard update/create scenario (with subitem creation) that does not appear under this or any obviously-matching name in `exports/make/valid-scenarios-working-inventory.md`. Either the scenario was renamed/retired since the export, or the export is incomplete for this family. Needs a direct Make.com lookup to resolve.
- **`AUTO-MASTERBOARD-001`** — `source-material/make/M.com_ Mortgage Questionnaire find contact in Mortgage Pipeline (Jan 26).md`'s title does not match the registered scenario name `M.com: New item in Mortgage App Copy to Masterboard End Forms (Jan 26)` (`8410524`). The mapping between the two is inferred from matching timeframe and near-identical Masterboard-matching logic, not confirmed by ID.
- **`AUTO-MORTGAGE-RENEWAL-001`** — `source-material/make/Real Savvy Fixed Rate Expiry Email (May25).md`'s title does not exactly match the registered scenario name `M.com: Fixed Rate Expiry Email Alert (May25)` (`4840595`). Treated as the same scenario based on identical "(May25)" dating and identical logic, but not confirmed by ID.
- **`AUTO-UNSUBSCRIBE-001`** — `Real Savvy Insurance Unsubscribe (11Sep)` (`7178534`)'s implementation is inferred by symmetry with the confirmed mortgage-side scenario (`5195381`); no source-material walkthrough exists for the insurance side. `M.Com: Unsubscribe Client Level (May 26)` (`9229914`)'s relationship to the other two unsubscribe scenarios (superseding, parallel, or a different unsubscribe surface entirely) is unconfirmed.
- **`AUTO-MONDAY-BACKUP-001`** — the automation is listed `Active` in this registry, but its destination board `💾 Monday E&A Backup Log` (`5029033494`) is filed under the "Historical Boards" folder and marked `Retained - Historical` in `knowledge/04_MONDAY_BOARDS_REGISTRY.md`. This is an unresolved contradiction between an active automation and a historically-classified destination board — needs direct verification of whether this board is still the live backup target.
- **`AUTO-LEADS-001`** — `M.com: Update Dependents (Dec25)` (`8260037`) and the inactive `M.com: CRM Migration - Connect Client Profiles and Pipelines (Dec25)` (`8264526`) sit in the same "Leads and Client Profiles" functional area but are not confirmed to be part of this automation's execution path; not assigned to any canonical automation ID pending investigation.

These are additive to, not replacements for, the gaps already listed above.

---

## 11. Documentation priorities

1. `AUTO-EMAIL-001` — Client Email Filing and Overflow Processing.
2. `AUTO-MASTERBOARD-001` — Mortgage Application to Masterboard End Forms.
3. `AUTO-MACROFORGE-001` — MacroForge End-Forms Integration.
4. `AUTO-AIRCALL-001` — Aircall Call Processing, Transcription and Summary.
5. `AUTO-BRANDED-SOP-001` — Branded Mortgage SOP Generation.
6. `AUTO-LEADS-001` — Lead to Contact and Client Profile Creation.
7. `AUTO-SP-FOLDER-001` — Client SharePoint Folder Lifecycle.
8. `AUTO-AFFORDX-001` — AffordX Mortgage Application Synchronisation.
9. `AUTO-PIGEON-001` — Pigeon Integration Suite.
10. Mortgage and Insurance renewal automations.

---

## 12. Registry maintenance rules

Update this registry when a scenario or flow is created, removed, renamed, enabled or disabled; when a Make scenario moves into or out of `Valid scenarios/working`; when a Power Automate flow becomes production-relevant; when a Monday Workflow is created or retired; or when a native integration or reusable component changes dependencies.

When adding an automation:

1. Assign a canonical automation ID.
2. Record the exact platform name and platform ID.
3. Identify trigger, systems, outputs and dependencies.
4. Decide whether it is an independent business automation or a reusable component.
5. Create the detailed automation document.
6. Update related system and board documentation.
7. Record testing and rollback requirements.
8. Update `last_modified` and only update `last_verified` after real verification.

---

## 13. Source inventory

This registry was assembled from the read-only Make.com inventory and call graph, current Power Automate environment screenshots, available Power Automate documentation, the Monday workspace structure export, the confirmed two Monday Workflows and current RSFA system context. §5.1 additionally draws on four read-only Power Automate Solution exports inspected on 2026-07-30 — see `exports/power-automate/solution-inventory.md`.