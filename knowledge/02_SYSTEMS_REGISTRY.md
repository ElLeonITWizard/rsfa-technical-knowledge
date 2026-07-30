---
id: RSFA-SYSTEMS-REGISTRY
title: RSFA Systems Registry
status: active
owner: RSFA
audience:
  - Authorised developers
  - Authorised technical consultants
last_modified: 2026-07-30
last_verified: 2026-07-30
---

# RSFA Systems Registry

## 1. Purpose

This document is the master registry of systems, platforms and technical tools used by RSFA.

Its purpose is to provide a structured overview of:

- Which systems exist.
- What role each system plays.
- Whether each system is active, expanding, reducing, experimental, planned, legacy or retired.
- How critical each system is.
- Who administrates it.
- Which technical account is responsible for it.
- What type of data it may handle.
- Which systems it connects to.
- Where its detailed documentation is stored.
- Whether migration, retirement or further documentation is required.

This registry should be updated whenever a relevant system is introduced, retired, migrated or materially changes role.

---

## 2. Status definitions

| Status | Meaning |
|---|---|
| `Active - Core` | Essential production system at the centre of RSFA operations |
| `Active` | In production and currently used |
| `Active - Expanding` | In production and expected to grow in importance or usage |
| `Active - Reducing` | Still in production, but expected to be used less over time |
| `Experimental` | Used only for testing, evaluation or proof of concept |
| `Planned` | Approved or under consideration, but not yet in production |
| `Legacy - Migration Required` | Still relevant because information or processes remain, but intended for retirement |
| `Retired` | No longer part of the current production architecture |

---

## 3. Criticality definitions

| Criticality | Meaning |
|---|---|
| `Critical` | Failure would materially disrupt core RSFA operations |
| `High` | Failure would significantly affect an important process, though a manual fallback may exist |
| `Medium` | Failure would reduce efficiency or affect a limited process |
| `Low` | Limited, experimental, future or non-essential use |

---

## 4. Data-sensitivity definitions

| Data category | Meaning |
|---|---|
| `Client personal data` | Names, contact details and identifying client information |
| `Financial data` | Lending, bank, mortgage or financial information |
| `Insurance data` | Insurance-related information |
| `Documents` | Client, operational or technical documents |
| `Communications` | Emails, Slack messages, calls or other communications |
| `Technical configuration` | System settings, mappings, schemas, workflow configuration |
| `Credentials` | Passwords, authentication records or secret references |
| `No client data expected` | System should not normally contain client information |

No secret value should ever be stored in this repository.

---

## 5. Master systems table

| System ID | System | Category | Status | Criticality | Primary role | Administrative owner | Technical account | Access URL | Main data handled | Detailed documentation |
|---|---|---|---|---|---|---|---|---|---|---|
| `SYS-MONDAY-001` | Monday.com | Operational core | Active - Core | Critical | CRM, workflow centre and structured operational records | Rod Schubert | `tech@rsfa.co.nz` | https://rsfa-squad.monday.com/ | Client personal data, financial data, insurance data, documents, technical configuration | `knowledge/systems/monday/` |
| `SYS-SHAREPOINT-001` | SharePoint | Document storage | Active - Core | Critical | Client folders, documents, templates and technical documentation | Rod Schubert | `tech@rsfa.co.nz` | https://rodschubertfinancialadvice.sharepoint.com/sites/RealSavvyClients/Documents/ | Client personal data, financial data, insurance data, documents, technical configuration | `knowledge/systems/sharepoint/` |
| `SYS-M365-001` | Microsoft 365 | Platform and identity | Active - Core | Critical | Identity, Outlook, SharePoint, Word, OneDrive and Microsoft services | Rod Schubert | `tech@rsfa.co.nz` | https://www.microsoft365.com/ | Client personal data, communications, documents, technical configuration | `knowledge/systems/microsoft-365/` |
| `SYS-OUTLOOK-001` | Outlook | Communication and email operations | Active - Core | Critical | Adviser mailboxes, shared mailboxes and email-based workflows | Rod Schubert | `tech@rsfa.co.nz` | https://outlook.office.com/ | Client personal data, communications, documents | `knowledge/systems/microsoft-365/outlook.md` |
| `SYS-WORD-001` | Microsoft Word | Document generation | Active | High | Templates and automated document output | Rod Schubert | `tech@rsfa.co.nz` | https://www.microsoft365.com/launch/word | Documents, client personal data, financial data | `knowledge/systems/microsoft-365/word.md` |
| `SYS-ONEDRIVE-001` | OneDrive | File synchronisation | Active | Medium | Limited local synchronisation, mainly for MacroForge-related workflows | Rod Schubert | `tech@rsfa.co.nz` | https://onedrive.live.com/ | Documents, technical configuration | `knowledge/systems/microsoft-365/onedrive.md` |
| `SYS-SLACK-001` | Slack | Communication and notifications | Active - Core | Critical | Tickets, requests, automation alerts and operational communication | Rod Schubert | `tech@rsfa.co.nz` | https://rsfa-realadvice.slack.com/ | Communications, client references, technical configuration | `knowledge/systems/slack/` |
| `SYS-MAKE-001` | Make.com | Automation platform | Active - Expanding | Critical | Primary cross-platform automation and integration platform | Rod Schubert | `tech@rsfa.co.nz` | https://eu2.make.com/organization/882256/ | Client personal data, financial data, documents, technical configuration | `knowledge/systems/make/` |
| `SYS-PA-001` | Power Automate | Automation platform | Active - Reducing | High | Microsoft-centric automation, especially email filing and SharePoint workflows | Rod Schubert | `tech@rsfa.co.nz` | https://make.powerautomate.com/environments/Default-df3cc44d-5e4a-4b7e-a22f-b90a4d6ab53d/home | Client personal data, communications, documents, technical configuration | `knowledge/systems/power-automate/` |
| `SYS-MONDAY-AUTO-001` | Monday Native Automations and Workflows | Automation platform | Active | High | Board-native routing, notifications, assignments and workflow progression | Rod Schubert | `tech@rsfa.co.nz` | https://rsfa-squad.monday.com/ | Client personal data, technical configuration | `knowledge/systems/monday/native-automations-and-workflows.md` |
| `SYS-SUPERFORMS-001` | Superforms | Forms and intake | Active - Expanding | High | Preferred form platform directly connected to Monday boards | Rod Schubert | `tech@rsfa.co.nz` | Accessed through Monday.com | Client personal data, financial data, insurance data | `knowledge/systems/monday/superforms.md` |
| `SYS-MONDAY-FORMS-001` | Monday Forms | Forms and intake | Active - Reducing | Medium | Existing form intake directly connected to Monday boards | Rod Schubert | `tech@rsfa.co.nz` | Accessed through Monday.com | Client personal data, financial data, insurance data | `knowledge/systems/monday/monday-forms.md` |
| `SYS-WEBSITE-001` | RSFA Website | Client-facing platform | Active | Medium | Public website and client-facing entry point | Rod Schubert | `tech@rsfa.co.nz` | https://rsfa.co.nz/ | Client personal data, communications | `knowledge/systems/website/` |
| `SYS-AIRCALL-001` | Aircall | Calls and communications | Active | High | Call handling, recordings, call metadata and transcription source | Rod Schubert | `tech@rsfa.co.nz` | https://dashboard.aircall.io/ | Client personal data, communications, call recordings, transcripts | `knowledge/systems/aircall/` |
| `SYS-PIGEON-001` | Pigeon Documents | Client document collection | Active | High | Online client document requests and uploads | Rod Schubert | `tech@rsfa.co.nz` | https://app.pigeondocuments.com/dashboard | Client personal data, financial data, insurance data, documents | `knowledge/systems/pigeon/` |
| `SYS-MACROFORGE-001` | MacroForge | Desktop automation tool | Active | High | Automatic completion of bank end forms from Monday data | Rod Schubert | `tech@rsfa.co.nz` | https://www.macroforge.io/ | Client personal data, financial data, documents, technical configuration | `knowledge/systems/macroforge/` |
| `SYS-AFFORDX-001` | AffordX | Financial analysis and meeting support | Active - Expanding | High | Bank-statement analysis, application tracking, meeting summaries and transcriptions | Rod Schubert | `tech@rsfa.co.nz` | https://broker.affordx.nz/ | Client personal data, financial data, communications, documents | `knowledge/systems/affordx/` |
| `SYS-DOCUSIGN-001` | DocuSign | Electronic signatures | Active | High | Electronic signatures and signed-document workflows | Rod Schubert | `tech@rsfa.co.nz` | https://apps.docusign.com/ | Client personal data, documents, signatures | `knowledge/systems/docusign/` |
| `SYS-DOCUSEAL-001` | DocuSeal | Electronic signatures | Experimental | Low | Potential future replacement for DocuSign | Rod Schubert | `tech@rsfa.co.nz` | https://docuseal.com/ | Test data only unless otherwise approved | `knowledge/systems/docuseal/` |
| `SYS-GCP-001` | Google Cloud Platform | Cloud infrastructure | Active | High | Hosts custom functions and backend services used by RSFA automations | Rod Schubert | `tech@rsfa.co.nz` | https://console.cloud.google.com/ | Technical configuration, custom code, possible client references | `knowledge/systems/google-cloud/` |
| `SYS-GCP-FUNCTIONS-001` | Google Cloud Project - RSFA Functions | Custom automation code | Active | High | Hosts custom functions called from automations | Rod Schubert | `tech@rsfa.co.nz` | https://console.cloud.google.com/welcome?project=strange-calling-402307 | Technical configuration, custom code, possible client references | `knowledge/systems/google-cloud/rsfa-functions.md` |
| `SYS-GCP-ADDIN-001` | Google Cloud Project - rsfa-backend-fix | Add-in backend | Active | High | Hosts the backend for the Real Savvy Ref Outlook Add-in | Rod Schubert | `tech@rsfa.co.nz` | https://console.cloud.google.com/welcome?project=rsfa-backend-fix | Technical configuration, custom code, client references | `knowledge/systems/google-cloud/rsfa-backend-fix.md` |
| `SYS-RSFA-REF-001` | Real Savvy Ref Outlook Add-in | Outlook add-in | Active | High | Gives advisers client context and lets them copy Client Profile IDs into email subjects | Rod Schubert | `tech@rsfa.co.nz` | Manifest stored in SharePoint; backend hosted in Google Cloud | Client personal data, communications, technical configuration | `knowledge/systems/real-savvy-ref/` |
| `SYS-CLAUDE-001` | Claude | AI and technical assistance | Active - Expanding | Medium | Technical consultation, repository maintenance, skills, agents and future tool workflows | Rod Schubert | `tech@rsfa.co.nz` | https://claude.ai/ | Technical configuration, documentation, communications | `knowledge/systems/ai/claude.md` |
| `SYS-CHATGPT-001` | ChatGPT Business | AI and company knowledge | Active - Expanding | Medium | Company Knowledge, technical consultation, Monday and connected-system research | Rod Schubert | `tech@rsfa.co.nz` | https://chatgpt.com/ | Technical configuration, documentation, communications | `knowledge/systems/ai/chatgpt.md` |
| `SYS-KNOWLEDGE-001` | RSFA Technical Knowledge Repository | Knowledge base | Active - Expanding | High | Canonical technical documentation, schemas, playbooks and incident history | RSFA | `tech@rsfa.co.nz` | Private GitHub repository and approved RSFA storage | Technical configuration, documentation | Repository root |
| `SYS-1PASSWORD-001` | 1Password | Credential management | Active | High | Secure storage of RSFA credentials and access information | Rod Schubert | `tech@rsfa.co.nz` | https://my.1password.com/ | Credentials, technical configuration | `knowledge/systems/1password/` |
| `SYS-PLANOLITIX-001` | Planolitix | Legacy platform | Legacy - Migration Required | Medium | Legacy operational or knowledge system pending migration | Rod Schubert | `tech@rsfa.co.nz` | Access via `rod@rsfa.co.nz` with 2FA | Client personal data, documents, operational information | `knowledge/systems/legacy/planolitix.md` |
| `SYS-GETGURU-001` | GetGuru | Legacy knowledge platform | Legacy - Migration Required | Medium | Legacy knowledge or operational information pending migration | Rod Schubert | `tech@rsfa.co.nz` | Technical access not currently confirmed | Documents, operational information | `knowledge/systems/legacy/getguru.md` |
| `SYS-JOTFORM-001` | Jotform | Retired forms platform | Retired | Low | Previous RSFA form platform, replaced by Superforms and Monday Forms | Rod Schubert | `tech@rsfa.co.nz` | https://www.jotform.com/ | Historical form data | `knowledge/systems/legacy/jotform.md` |
| `SYS-BOOKINGS-001` | Microsoft Bookings | Scheduling | Planned | Low | Potential future appointment-booking platform | Rod Schubert | `tech@rsfa.co.nz` | https://www.microsoft.com/microsoft-365/business/scheduling-and-booking-app | Client personal data, communications | `knowledge/systems/planned/microsoft-bookings.md` |
| `SYS-TEAMS-001` | Microsoft Teams | Communication and collaboration | Active - Limited | Low | General Microsoft 365 collaboration, not currently central to automation architecture | Rod Schubert | `tech@rsfa.co.nz` | https://teams.microsoft.com/ | Communications, documents | `knowledge/systems/microsoft-365/teams.md` |

---

## 6. System summaries

## SYS-MONDAY-001 — Monday.com

- **Category:** Operational core
- **Status:** Active - Core
- **Criticality:** Critical
- **Primary role:** Main CRM, workflow and structured operational-record layer
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://rsfa-squad.monday.com/
- **Handles client data:** Yes
- **Main connected systems:** Make.com, Power Automate, SharePoint, Outlook, Aircall, Pigeon, Superforms, Monday Forms, MacroForge, AffordX, Slack
- **Source-of-truth responsibility:** Operational records, workflow stage and structured status
- **Detailed documentation:** `knowledge/systems/monday/`

Monday.com is the centre of RSFA's technical ecosystem.

It stores and connects major operational records including:

- Leads.
- Contacts.
- Client Profiles.
- Mortgage applications.
- Mortgage Pipeline.
- Existing Mortgages.
- Insurance Deals Pipeline.
- Existing Insurance.
- KiwiSaver Pipeline.
- Trusts and Companies.
- Security addresses.
- Pigeon requests.
- Aircall calls.
- Overflow emails.
- IT tasks.
- Automation records.
- Activity logs.
- Documentation.
- Email campaign templates.

---

## SYS-SHAREPOINT-001 — SharePoint

- **Category:** Document storage
- **Status:** Active - Core
- **Criticality:** Critical
- **Primary role:** Main storage location for client and technical documents
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Primary client site:** https://rodschubertfinancialadvice.sharepoint.com/sites/RealSavvyClients/Documents/
- **Handles client data:** Yes
- **Main connected systems:** Monday.com, Power Automate, Make.com, Outlook, DocuSign, MacroForge, Real Savvy Ref
- **Source-of-truth responsibility:** Client documents and approved files
- **Detailed documentation:** `knowledge/systems/sharepoint/`

Each Client Profile has its own SharePoint folder.

The Client Profile ID is included in the folder name to improve matching.

General overflow folders are used for files that cannot yet be associated with a client.

---

## SYS-M365-001 — Microsoft 365

- **Category:** Platform and identity
- **Status:** Active - Core
- **Criticality:** Critical
- **Primary role:** Identity, licensing and Microsoft service platform
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://www.microsoft365.com/
- **Main connected systems:** Outlook, SharePoint, Word, OneDrive, Power Automate, Teams
- **Detailed documentation:** `knowledge/systems/microsoft-365/`

Microsoft 365 provides the shared platform for:

- Identity.
- Mailboxes.
- SharePoint.
- Word.
- OneDrive.
- Power Automate.
- Teams.
- Future Bookings implementation.

---

## SYS-OUTLOOK-001 — Outlook

- **Category:** Communications
- **Status:** Active - Core
- **Criticality:** Critical
- **Primary role:** Adviser and shared email operations
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://outlook.office.com/
- **Handles client data:** Yes
- **Main connected systems:** Power Automate, SharePoint, Monday.com, Real Savvy Ref, Slack
- **Detailed documentation:** `knowledge/systems/microsoft-365/outlook.md`

Outlook is central to:

- Main Outlook Email Filing.
- Overflow email processing.
- Adviser communications.
- Client document receipt.
- Fixed Rate Expiry notifications.
- Existing Insurance anniversary notifications.

---

## SYS-MAKE-001 — Make.com

- **Category:** Automation platform
- **Status:** Active - Expanding
- **Criticality:** Critical
- **Primary role:** Main cross-platform automation platform
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://eu2.make.com/organization/882256/
- **Handles client data:** Yes
- **Main connected systems:** Monday.com, Slack, Aircall, SharePoint, Superforms, Pigeon, MacroForge, AffordX, Google Cloud
- **Detailed documentation:** `knowledge/systems/make/`

Make.com is the preferred platform for most new non-Microsoft automations.

It is used for:

- API integrations.
- Data transformations.
- Complex mappings.
- Monday processing.
- Aircall processing.
- Document generation.
- AI-assisted workflows.
- Slack notifications.
- Google Cloud custom-function calls.

---

## SYS-PA-001 — Power Automate

- **Category:** Automation platform
- **Status:** Active - Reducing
- **Criticality:** High
- **Primary role:** Microsoft-centric automation
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://make.powerautomate.com/environments/Default-df3cc44d-5e4a-4b7e-a22f-b90a4d6ab53d/home
- **Handles client data:** Yes
- **Main connected systems:** Outlook, SharePoint, Monday.com, Slack, DocuSign
- **Detailed documentation:** `knowledge/systems/power-automate/`

Power Automate is primarily retained for:

- Main Outlook Email Filing.
- Overflow email reprocessing.
- SharePoint operations.
- DocuSign filing.
- Selected backup and operational flows.

Read-only, point-in-time Solution export snapshots have been added for a subset of these flows, for inspection without live authentication:

- `exports/power-automate/solution-inventory.md` — index of every exported Solution and its flows.
- `knowledge/systems/power-automate/` — system-level documentation (README, Solutions, environments, connection references).

These snapshots do not replace live verification — see `CLAUDE.md` § "Power Automate Solution exports".

---

## SYS-MONDAY-AUTO-001 — Monday Native Automations and Workflows

- **Category:** Automation platform
- **Status:** Active
- **Criticality:** High
- **Primary role:** Native board routing and workflow progression
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://rsfa-squad.monday.com/
- **Main connected systems:** Monday.com, Make.com, Power Automate, Slack
- **Detailed documentation:** `knowledge/systems/monday/native-automations-and-workflows.md`

This layer includes:

- Status-based actions.
- Item movement.
- Item creation.
- Assignment.
- Notifications.
- Triggering of external automations.
- Workflow progression.

---

## SYS-SUPERFORMS-001 — Superforms

- **Category:** Forms and intake
- **Status:** Active - Expanding
- **Criticality:** High
- **Primary role:** Preferred form platform directly connected to Monday boards
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** Accessed through Monday.com
- **Handles client data:** Yes
- **Main connected systems:** Monday.com, Make.com
- **Detailed documentation:** `knowledge/systems/monday/superforms.md`

Major Superforms include:

- Mortgage Application.
- KiwiSaver Questionnaire.
- ROMA.

---

## SYS-MONDAY-FORMS-001 — Monday Forms

- **Category:** Forms and intake
- **Status:** Active - Reducing
- **Criticality:** Medium
- **Primary role:** Existing form intake directly connected to Monday boards
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** Accessed through Monday.com
- **Handles client data:** Yes
- **Main connected systems:** Monday.com
- **Detailed documentation:** `knowledge/systems/monday/monday-forms.md`

Current examples include:

- Insurance Questionnaire.
- Leads Form.

RSFA intends to migrate more forms to Superforms.

---

## SYS-AIRCALL-001 — Aircall

- **Category:** Communications
- **Status:** Active
- **Criticality:** High
- **Primary role:** Calls, call metadata, recordings and transcription source
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://dashboard.aircall.io/
- **Handles client data:** Yes
- **Main connected systems:** Monday.com, Make.com, SharePoint, Slack
- **Detailed documentation:** `knowledge/systems/aircall/`

Aircall uses a native Monday integration to create call records.

Make.com and Monday automations then process those records for:

- Client matching.
- Timeline updates.
- Transcription generation.
- AI summaries.
- SharePoint filing.
- Slack notifications.

---

## SYS-PIGEON-001 — Pigeon Documents

- **Category:** Client document collection
- **Status:** Active
- **Criticality:** High
- **Primary role:** Online document requests and client uploads
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Operational accounts:** `support@rsfa.co.nz`, `rod@rsfa.co.nz`
- **Access URL:** https://app.pigeondocuments.com/dashboard
- **Handles client data:** Yes
- **Main connected systems:** Monday.com, Mortgage Pipeline, SharePoint
- **Detailed documentation:** `knowledge/systems/pigeon/`

---

## SYS-MACROFORGE-001 — MacroForge

- **Category:** Desktop automation tool
- **Status:** Active
- **Criticality:** High
- **Primary role:** Automatic completion of bank end forms
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://www.macroforge.io/
- **Handles client data:** Yes
- **Main connected systems:** Monday.com, Masterboard End Forms, SharePoint, OneDrive
- **Detailed documentation:** `knowledge/systems/macroforge/`

MacroForge runs as a desktop application.

Its main data source is `Masterboard: End Forms`.

Local file synchronisation may use OneDrive to keep local files aligned with SharePoint.

---

## SYS-AFFORDX-001 — AffordX

- **Category:** Financial analysis and meeting support
- **Status:** Active - Expanding
- **Criticality:** High
- **Primary role:** Bank-statement analysis, application tracking, meeting summaries and transcriptions
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://broker.affordx.nz/
- **Handles client data:** Yes
- **Main connected systems:** Monday.com, SharePoint, adviser workflows
- **Detailed documentation:** `knowledge/systems/affordx/`

The exact AffordX integration map still requires detailed documentation.

---

## SYS-DOCUSIGN-001 — DocuSign

- **Category:** Electronic signatures
- **Status:** Active
- **Criticality:** High
- **Primary role:** Electronic signatures and signed-document processing
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Operational account:** `support@rsfa.co.nz`
- **Access URL:** https://apps.docusign.com/
- **Handles client data:** Yes
- **Main connected systems:** Power Automate, SharePoint, Slack
- **Detailed documentation:** `knowledge/systems/docusign/`

---

## SYS-DOCUSEAL-001 — DocuSeal

- **Category:** Electronic signatures
- **Status:** Experimental
- **Criticality:** Low
- **Primary role:** Potential future replacement for DocuSign
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Test account:** `tech@rsfa.co.nz`
- **Access URL:** https://docuseal.com/
- **Handles client data:** No production client data expected
- **Detailed documentation:** `knowledge/systems/docuseal/`

Only a test board and trial account currently exist.

No production workflow has been implemented.

---

## SYS-GCP-001 — Google Cloud Platform

- **Category:** Cloud infrastructure
- **Status:** Active
- **Criticality:** High
- **Primary role:** Custom code and backend hosting
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Handles client data:** Possible, depending on function
- **Main connected systems:** Make.com, Outlook, Monday.com, SharePoint, Real Savvy Ref
- **Detailed documentation:** `knowledge/systems/google-cloud/`

Google Cloud currently contains at least two important projects.

### RSFA Functions

- **Project ID:** `strange-calling-402307`
- **URL:** https://console.cloud.google.com/welcome?project=strange-calling-402307
- **Purpose:** Hosts custom functions called from automations.

### rsfa-backend-fix

- **Project ID:** `rsfa-backend-fix`
- **URL:** https://console.cloud.google.com/welcome?project=rsfa-backend-fix
- **Purpose:** Hosts the backend for the Real Savvy Ref Outlook Add-in.

---

## SYS-RSFA-REF-001 — Real Savvy Ref Outlook Add-in

- **Category:** Outlook add-in
- **Status:** Active
- **Criticality:** High
- **Primary role:** Provides quick client information and Client Profile references while composing emails
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Backend:** Google Cloud project `rsfa-backend-fix`
- **Manifest:** Stored in SharePoint
- **Handles client data:** Yes
- **Main connected systems:** Outlook, Monday.com, SharePoint, Power Automate, Google Cloud
- **Detailed documentation:** `knowledge/systems/real-savvy-ref/`

The add-in:

- Connects to Monday.com to retrieve Client Profile IDs.
- Connects to SharePoint to retrieve client folders.
- Allows advisers to view client information while composing an email.
- Allows advisers to copy the Client Profile ID.
- Supports the email-subject format:

```text
RSFA Ref %ClientProfileID%
```

This reference forces the Main Outlook Email Filing flow to associate the email with the specified Client Profile.

---

## SYS-CLAUDE-001 — Claude

- **Category:** AI and technical assistance
- **Status:** Active - Expanding
- **Criticality:** Medium
- **Primary role:** Technical consultation, repository maintenance, agents and future tool workflows
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://claude.ai/
- **Handles client data:** Only when explicitly authorised and required
- **Main connected systems:** RSFA Technical Knowledge Repository, future MCP tools, Slack
- **Detailed documentation:** `knowledge/systems/ai/claude.md`

---

## SYS-CHATGPT-001 — ChatGPT Business

- **Category:** AI and company knowledge
- **Status:** Active - Expanding
- **Criticality:** Medium
- **Primary role:** Company Knowledge, technical consultation and connected-system research
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://chatgpt.com/
- **Handles client data:** Only when explicitly authorised and required
- **Main connected systems:** Monday.com, Slack, SharePoint, Company Knowledge
- **Detailed documentation:** `knowledge/systems/ai/chatgpt.md`

---

## SYS-KNOWLEDGE-001 — RSFA Technical Knowledge Repository

- **Category:** Knowledge base
- **Status:** Active - Expanding
- **Criticality:** High
- **Primary role:** Canonical technical documentation and system knowledge
- **Administrative owner:** RSFA
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** Private GitHub repository and approved RSFA storage
- **Handles client data:** No client data expected
- **Main connected systems:** Claude, ChatGPT, SharePoint, Monday.com, Slack
- **Detailed documentation:** Repository root

---

## SYS-1PASSWORD-001 — 1Password

- **Category:** Security and credential management
- **Status:** Active
- **Criticality:** High
- **Primary role:** Secure credential storage
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://my.1password.com/
- **Handles client data:** Credentials and technical access information
- **Detailed documentation:** `knowledge/systems/1password/`

No credentials or secret values from 1Password may be copied into this repository.

---

## SYS-PLANOLITIX-001 — Planolitix

- **Category:** Legacy platform
- **Status:** Legacy - Migration Required
- **Criticality:** Medium
- **Primary role:** Legacy operational or knowledge information
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access:** `rod@rsfa.co.nz` with 2FA
- **Handles client data:** Potentially yes
- **Detailed documentation:** `knowledge/systems/legacy/planolitix.md`

Remaining information must be identified and migrated before retirement.

---

## SYS-GETGURU-001 — GetGuru

- **Category:** Legacy knowledge platform
- **Status:** Legacy - Migration Required
- **Criticality:** Medium
- **Primary role:** Legacy knowledge or operational information
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access:** Technical access not currently confirmed
- **Handles client data:** Unknown
- **Detailed documentation:** `knowledge/systems/legacy/getguru.md`

Remaining information must be identified and migrated before retirement.

---

## SYS-JOTFORM-001 — Jotform

- **Category:** Retired forms platform
- **Status:** Retired
- **Criticality:** Low
- **Primary role:** Previous RSFA form platform
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://www.jotform.com/
- **Handles client data:** Historical form data
- **Detailed documentation:** `knowledge/systems/legacy/jotform.md`

Jotform has been replaced by Superforms and Monday Forms.

---

## SYS-BOOKINGS-001 — Microsoft Bookings

- **Category:** Scheduling
- **Status:** Planned
- **Criticality:** Low
- **Primary role:** Potential future client appointment scheduling
- **Administrative owner:** Rod Schubert
- **Technical account:** `tech@rsfa.co.nz`
- **Access URL:** https://www.microsoft.com/microsoft-365/business/scheduling-and-booking-app
- **Handles client data:** Expected to handle client personal data and communications
- **Detailed documentation:** `knowledge/systems/planned/microsoft-bookings.md`

---

## 7. Account and ownership rules

### Rod Schubert

Rod is the primary administrative owner for most RSFA tools.

His account may be required for:

- Primary-owner permissions.
- Workspace administration.
- Tool installation.
- Business approval.
- Administrative recovery.

### `tech@rsfa.co.nz`

`tech@rsfa.co.nz` is the primary technical account and Automation Hub.

Use this account for:

- Automation ownership.
- Technical integrations.
- Cloud projects.
- Developer access.
- System maintenance.
- Technical subscriptions.
- Platform connections.

### `leo@rsfa.co.nz`

`leo@rsfa.co.nz` is not the primary technical login for RSFA systems.

It should not be listed as the default technical owner or system account unless a specific system is actually configured with it.

### Adviser and operational accounts

Other accounts may be used for adviser-specific or operational purposes, including:

- `rod@rsfa.co.nz`
- `kathleen@rsfa.co.nz`
- `seth@rsfa.co.nz`
- `jet@rsfa.co.nz`
- `support@rsfa.co.nz`
- `it-support@rsfa.co.nz`

Specific account usage should be documented in each system file.

---

## 8. Registry update rules

Update this registry when:

- A new system is introduced.
- A system becomes production-critical.
- A system is placed into retirement.
- Ownership changes.
- The technical account changes.
- A stable access URL changes.
- A new major integration is added.
- A system starts handling a new sensitive-data category.
- A system changes from experimental to production.
- A legacy migration is completed.

When adding a new system:

1. Assign a new internal system ID.
2. Add it to the master table.
3. Add a system summary.
4. Create its detailed documentation folder or file.
5. Update `01_RSFA_SYSTEM_MAP.md` if architecture changes.
6. Update `03_AUTOMATION_REGISTRY.md` if automations depend on it.
7. Add related source documents to `09_DOCUMENT_REGISTRY.md`.
8. Update `last_modified`.
9. Update `last_verified` only after real verification.

---

## 9. Known gaps

The following information still requires verification:

- Aircall workspace-specific URL.
- Exact administrator list for each platform.
- Complete Google Cloud IAM ownership.
- Exact SharePoint location of the Real Savvy Ref manifest.
- Exact repository location of the Real Savvy Ref code.
- Exact Pigeon-to-SharePoint document flow.
- Complete AffordX integration map.
- Remaining content inside Planolitix.
- Remaining content inside GetGuru.
- Microsoft 365 tenant administration URL.
- Future Microsoft Bookings architecture.
- Exact RSFA website integrations.
