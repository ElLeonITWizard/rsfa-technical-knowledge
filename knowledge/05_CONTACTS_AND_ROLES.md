---
id: RSFA-CONTACTS-AND-ROLES
title: RSFA Contacts and Roles
status: active
owner: RSFA
audience:
  - Authorised developers
  - Authorised technical consultants
last_modified: 2026-07-30
last_verified: 2026-07-30
---

# RSFA Contacts and Roles

## 1. Purpose

This document identifies the people, shared accounts and external contacts relevant to RSFA's systems, automations, technical maintenance and operational support.

Its purpose is to help authorised technical users determine:

- Who owns a business process.
- Who can approve a change.
- Who administers a system.
- Who should be contacted for a platform-specific issue.
- Which shared accounts are used for technical or operational purposes.
- Which users are affected by a change.
- Which contacts are current, transitional or historical.

This document is not a general staff directory.

It should only contain information relevant to systems, automation, permissions, incident handling and technical communication.

---

## 2. Role classification

| Role classification | Meaning |
|---|---|
| `Business Owner` | Can approve business decisions, commercial commitments and high-impact organisational changes |
| `Process Owner` | Defines requirements and priorities for a specific operational area |
| `Technical Administrator` | Controls administrative access, tenant settings, platform ownership or privileged configuration |
| `Technical Maintainer` | Investigates, develops, documents and maintains systems and automations |
| `Operational User` | Uses the system and may report issues or request improvements |
| `External Vendor` | Provides or maintains a third-party platform or specialist service |
| `Historical Contact` | Holds historical implementation knowledge but has no confirmed current responsibility |

A person may have more than one classification.

---

## 3. Internal stakeholders

## 3.1 Rod Schubert

- **Email:** `rod@rsfa.co.nz`
- **Organisation:** RSFA
- **Current status:** Active
- **Primary role:** Owner and Financial Adviser
- **Role classification:**
  - Business Owner
  - Technical Administrator
  - Operational User
- **Main responsibilities:**
  - Overall ownership of RSFA.
  - Final approval for commercial commitments and billing.
  - Administrative control of important systems.
  - Main stakeholder for IT and automation work.
  - Business decisions affecting multiple operational areas.
- **Systems with important administrative control:**
  - Aircall.
  - Microsoft 365 Admin Centre.
  - Rod's Outlook account.
  - Workspace ownership or primary-owner actions where applicable.
  - Tool subscriptions and billing.
- **Typical technical interactions:**
  - Reports tickets and requests through Slack.
  - Defines priorities.
  - Provides business clarification.
  - Approves new tools, material cost changes and major process changes.
- **Approval guidance:**
  - Not every IT change requires Rod's explicit approval.
  - Routine maintenance, documentation work and clearly authorised technical fixes may proceed without separate approval.
  - Rod's approval is required when the change affects:
    - Billing.
    - New subscriptions.
    - Administrative ownership.
    - High-impact permissions.
    - Major cross-business processes.
    - Aircall administration.
    - Microsoft tenant administration.
    - His own mailbox or account configuration.
- **Communication style:**
  - Clear.
  - Concise.
  - Evidence-based.
  - Direct about limitations.
  - Focused on functionality and next steps.
- **Important note:** Do not describe an issue as resolved until the expected outcome has been validated.

---

## 3.2 Kathleen Schubert

- **Email:** `insurance@rsfa.co.nz`
- **Organisation:** RSFA
- **Current status:** Active
- **Primary role:** Insurance Adviser
- **Role classification:**
  - Process Owner
  - Operational User
- **Main responsibilities:**
  - Insurance advice operations.
  - Insurance process requirements.
  - Insurance-related client servicing.
  - Emerging Group Health Insurance Schemes work.
- **Primary systems and boards:**
  - `Insurance Deals Pipeline`.
  - `Existing Insurance`.
  - `Insurance Questionnaire`.
  - Insurance-related email and renewal processes.
  - Insurance-related Slack notifications.
- **Approval guidance:**
  - Kathleen defines and validates insurance process requirements.
  - She does not provide final approval for broad production or infrastructure changes.
  - Material technical changes should still follow the applicable technical and business approval path.
- **Operational authority:**
  - Can clarify insurance workflow behaviour.
  - Can validate whether an insurance-related automation supports the intended process.
  - Can report issues and request improvements.
- **Communication style:**
  - Use English.
  - Focus on the insurance process and practical outcome.
  - Avoid unnecessary technical detail unless requested.

---

## 3.3 Seth Rackham

- **Email:** `seth@rsfa.co.nz`
- **Organisation:** RSFA
- **Current status:** Active
- **Primary role:** Financial Adviser and contractor
- **Role classification:**
  - Operational User
- **Likely area:** Mortgages
- **Verification status:** Specialisation requires confirmation
- **Relevant systems and processes:**
  - Outlook Email Filing.
  - Seth-specific sent and received mailbox flows.
  - Seth Overflow Emails board.
  - Mortgage-related boards and processes.
- **Approval guidance:**
  - Seth may report issues and request improvements.
  - Material changes require Rod's approval.
  - Do not treat a request from Seth as approval for a broad production change unless Rod has authorised it.
- **Known technical dependencies:**
  - `Outlook Email Filing - Seth v2`.
  - `Outlook SENT Email Filling - Seth v2`.
  - `Overflow Emails - Seth`.
  - Seth-related Slack overflow channel.
- **Known gap:**
  - TODO: verify Seth's exact advice specialisation and process ownership.

---

## 3.4 Jet Douglas

- **Email:** `jet@rsfa.co.nz`
- **Organisation:** RSFA
- **Current status:** Active - Transitioning Out
- **Expected departure:** Approximately two weeks from 2026-07-30
- **Primary role:** Financial Adviser
- **Role classification:**
  - Operational User
- **Relevant systems and processes:**
  - Outlook Email Filing.
  - Jet-specific sent and received mailbox flows.
  - Jet Overflow Emails board.
  - Jet-related Slack overflow routing.
  - Historical client and pipeline records.
- **Approval guidance:**
  - Jet may still report issues while active.
  - Material changes require Rod's approval.
- **Retirement considerations:**
  - Remove or disable Jet-specific mailbox flows only after mailbox handling is formally transitioned.
  - Review the Jet Overflow Emails board before retirement.
  - Preserve historical records.
  - Review Slack routing and permissions.
  - Review adviser assignments in Monday.
  - Review Microsoft 365 access.
  - Review Aircall and other platform access.
- **Known technical flows:**
  - `Outlook Email Filing - Jet v2`.
  - `OLD Outlook SENT Email Filling - Jet v2`.
- **Important note:** Do not retire Jet-related automation solely because departure is expected. Confirm the transition plan first.

---

## 3.5 Leonardo Melman

- **Email:** `leo@rsfa.co.nz`
- **Organisation:** RSFA technical support
- **Current status:** Active
- **Primary role:** Authorised Technical Consultant and Automation Developer
- **Role classification:**
  - Technical Maintainer
  - Technical Administrator
- **Main responsibilities:**
  - Automation development and maintenance.
  - Technical investigations.
  - Documentation.
  - Make.com maintenance.
  - Power Automate maintenance.
  - Monday.com configuration.
  - SharePoint and Microsoft integration work.
  - Google Cloud maintenance.
  - Claude and ChatGPT technical setup.
  - Real Savvy Ref maintenance.
- **Important account rule:**
  - `leo@rsfa.co.nz` is not the default technical account for platform logins.
  - Most technical ownership and platform access should use `tech@rsfa.co.nz`.
- **Mailbox relationship:**
  - `it-support@rsfa.co.nz` is a shared mailbox under `leo@rsfa.co.nz`.
- **Approval guidance:**
  - Routine maintenance and explicitly requested technical fixes may be completed without separate approval from Rod.
  - Commercial, billing, major permission and high-impact business changes require the relevant approval.
- **Communication responsibility:**
  - Investigate issues.
  - Separate confirmed facts from assumptions.
  - Prepare concise stakeholder updates.
  - Update canonical documentation after verified changes.

---

## 4. Shared and technical accounts

## 4.1 `tech@rsfa.co.nz`

- **Account type:** Primary technical and automation account
- **Current status:** Active
- **Controlled by:** Rod Schubert and Leonardo Melman
- **Primary day-to-day controller:** Leonardo Melman
- **Role classification:**
  - Technical Administrator
  - Technical Maintainer
- **Primary purposes:**
  - Automation Hub.
  - Make.com ownership.
  - Power Automate ownership.
  - Google Cloud access.
  - Technical subscriptions.
  - Developer tools.
  - Integration connections.
  - Claude and ChatGPT technical accounts.
  - 1Password technical access.
- **Usage rule:**
  - Use this account as the default technical owner unless a system explicitly requires another account.
- **Security rule:**
  - Credentials must remain in the approved password manager.
  - Do not store passwords or tokens in this repository.

---

## 4.2 `it-support@rsfa.co.nz`

- **Account type:** Shared mailbox
- **Current status:** Active
- **Hosted under:** `leo@rsfa.co.nz`
- **Primary purpose:**
  - Technical communications.
  - External and internal support conversations.
  - IT-related correspondence.
- **Planned automation use:**
  - Intended to be added to Main Outlook Email Filing.
- **Role classification:**
  - Technical communication account
- **Important note:** This is not the default platform-login account.

---

## 4.3 `support@rsfa.co.nz`

- **Account type:** Shared operational account
- **Current status:** Active
- **Primary purpose:**
  - Operational support.
  - Shared platform access.
  - DocuSign account.
  - Some automation error notifications.
- **Known systems:**
  - DocuSign.
  - Pigeon.
  - Outlook-related operational processes.
- **Usage note:**
  - Some error notifications currently use `support@rsfa.co.nz`.
  - Other error notifications use `tech@rsfa.co.nz`.
  - TODO: standardise error-notification sender and recipient conventions.

---

## 4.4 `slack-ingest@rsfa.co.nz`

- **Account type:** Shared ingestion mailbox
- **Current status:** Active
- **Primary purpose:**
  - Receives overflow emails intended for Slack.
  - Provides a backup or intermediary path for Slack overflow notifications.
- **Related systems:**
  - Outlook.
  - Power Automate.
  - Slack.
  - Overflow Emails boards.
- **Role classification:**
  - Automation service account
- **Known gap:**
  - TODO: document the exact routing rules and mailbox ownership.

---

## 4.5 `media@rsfa.co.nz`

- **Account type:** Shared operational mailbox
- **Current status:** Active
- **Primary purpose:** Marketing
- **Role classification:**
  - Operational service account
- **Related systems:**
  - Marketing tools.
  - Email campaign processes.
  - Social-media or media workflows where applicable.
- **Known gap:**
  - TODO: document current integrations and ownership.

---

## 4.6 `operations@rsfa.co.nz`

- **Account type:** Shared operational mailbox
- **Current status:** Active
- **Primary purpose:** Operations
- **Role classification:**
  - Operational service account
- **Known gap:**
  - TODO: document current users, permissions and automation dependencies.

---

## 5. External vendors and specialist contacts

## 5.1 Kevin — MacroForge

- **Full name:** TODO: verify surname
- **Organisation:** MacroForge
- **Current status:** Active external contact
- **Primary role:** Creator and specialist maintainer of MacroForge
- **Role classification:**
  - External Vendor
- **Contact method:**
  - Email.
  - Microsoft Teams meetings when required.
- **Escalate to Kevin for:**
  - MacroForge desktop application issues.
  - MacroForge-specific behaviour.
  - End-form completion defects originating inside MacroForge.
  - MacroForge product limitations.
  - MacroForge updates or implementation questions.
- **RSFA responsibilities before escalation:**
  - Verify the Monday source data.
  - Verify the Make payload.
  - Verify the Masterboard mapping.
  - Reproduce the issue where possible.
  - Separate integration defects from MacroForge application defects.

---

## 5.2 Yuan Gao — AffordX

- **Organisation:** AffordX
- **Current status:** Active external contact
- **Primary role:** Creator of AffordX
- **Role classification:**
  - External Vendor
- **Contact method:** TODO: verify
- **Escalate for:**
  - AffordX platform defects.
  - API behaviour.
  - Application synchronisation issues caused by AffordX.
  - Bank-statement analysis issues.
  - Meeting summary or transcription module issues.
- **RSFA responsibilities before escalation:**
  - Verify the Make scenario.
  - Verify the API request and response.
  - Verify Monday source values.
  - Confirm whether the issue is reproducible.

---

## 5.3 Silvie — Aircall

- **Full name:** TODO: verify
- **Organisation:** Aircall or Aircall-related support
- **Current status:** Active external contact
- **Role classification:**
  - External Vendor
- **Contact method:** Email
- **Known area:** Aircall support
- **Escalate for:**
  - Aircall account or platform questions.
  - Recording or transcription availability.
  - Native Monday integration behaviour.
  - Aircall API or account limitations.
- **Known gap:** TODO: verify Silvie's exact role and area of responsibility.

---

## 5.4 Ben — Aircall

- **Full name:** TODO: verify
- **Organisation:** Aircall or Aircall-related support
- **Current status:** Active external contact
- **Role classification:**
  - External Vendor
- **Contact method:** Email
- **Known area:** Aircall support
- **Known gap:** TODO: verify Ben's exact role and when to contact him instead of Silvie.

---

## 5.5 Stephanie — Slack

- **Full name:** TODO: verify
- **Organisation:** Slack or Slack-related support
- **Current status:** Active external contact
- **Role classification:**
  - External Vendor
- **Contact method:** Email
- **Known area:** Slack support or implementation
- **Escalate for:**
  - Workspace-level Slack questions.
  - Slack integration limitations.
  - Slack administration or implementation support.
- **Known gap:** TODO: verify Stephanie's exact company, role and support scope.

---

## 5.6 Mischa Slang

- **Name verification:** Surname believed to be Slang; TODO: verify
- **Current status:** Historical developer
- **Role classification:**
  - Historical Contact
  - External Developer
- **Known contribution:**
  - Original developer of the Real Savvy Ref Outlook Add-in.
- **Related systems:**
  - Outlook add-in.
  - Monday.com.
  - SharePoint.
  - Google Cloud project `rsfa-backend-fix`.
- **Current maintenance owner:** `tech@rsfa.co.nz`
- **Relationship status:** No confirmed negative end to the relationship
- **Availability:** TODO: verify
- **Contact guidance:**
  - Contact only when historical implementation knowledge is required and current documentation or code is insufficient.
  - Do not treat Mischa as the current maintainer.

---

## 6. Authority and approval matrix

| Change type | Rod | Kathleen | Seth | Jet | Technical Maintainer |
|---|---|---|---|---|---|
| Routine documentation update | Not required | Not required | Not applicable | Not applicable | May proceed |
| Routine technical maintenance | Not always required | May provide process context | May report issue | May report issue | May proceed within authorised scope |
| Insurance process requirement | Informed when material | Defines requirement | Not applicable | Not applicable | Implements after clarification |
| Broad production change | Approves | Provides area input | Requires Rod approval | Requires Rod approval | Plans and implements after approval |
| New paid tool or billing change | Approves | Does not approve | Does not approve | Does not approve | Recommends only |
| Microsoft tenant administration | Controls or approves | No general authority | No authority | No authority | Acts within delegated access |
| Aircall administration | Controls or approves | Operational input only | No authority | No authority | Maintains within authorised scope |
| Make or Power Automate fix | Approval not always required | Process input where relevant | May report | May report | May investigate and fix when authorised |
| Destructive or irreversible action | Explicit approval required | Cannot approve broadly | Cannot approve | Cannot approve | Must not proceed without approval |
| External vendor escalation | May be informed | May participate for insurance | May provide evidence | May provide evidence | Coordinates escalation |

---

## 7. Communication and escalation rules

### Technical issue reported by Rod

1. Confirm the request.
2. Review relevant documentation.
3. Retrieve live evidence when needed.
4. Investigate within the authorised technical scope.
5. Escalate only when a business, billing, permission or vendor decision is required.
6. Report confirmed findings and limitations.

### Technical issue reported by Kathleen

1. Confirm whether the issue is insurance-related.
2. Use Kathleen as the process expert.
3. Investigate and propose the technical resolution.
4. Obtain Rod's approval only when the change is broad, commercial, high-risk or cross-business.

### Technical issue reported by Seth or Jet

1. Treat the message as a valid issue report.
2. Investigate the issue.
3. Do not treat the request as approval for a broad production change.
4. Escalate material changes to Rod.

### Platform-specific defect

Escalate to the relevant external vendor only after confirming:

- The RSFA source data.
- The RSFA automation logic.
- The API request or platform input.
- The failure evidence.
- The expected behaviour.
- The impact.
- The reproduction steps.

---

## 8. Account usage principles

- Use `tech@rsfa.co.nz` for technical platform ownership and automation access.
- Use `it-support@rsfa.co.nz` for technical correspondence.
- Use `support@rsfa.co.nz` for operational systems where it is already the configured account.
- Do not use `leo@rsfa.co.nz` as the default technical login.
- Do not change account ownership casually.
- Do not create personal dependencies when a shared technical account is available.
- Record platform-specific exceptions in the relevant system documentation.
- Keep credentials in the approved password manager.

---

## 9. Known gaps

- Confirm Seth Rackham's exact advice specialisation.
- Confirm Jet Douglas's exact departure date.
- Confirm Kevin's surname.
- Confirm Silvie's full name and exact Aircall role.
- Confirm Ben's full name and exact Aircall role.
- Confirm Stephanie's full name, organisation and Slack support scope.
- Confirm Mischa Slang's surname and current availability.
- Document ownership and routing for `slack-ingest@rsfa.co.nz`.
- Document current ownership and integrations for `media@rsfa.co.nz`.
- Document current ownership and integrations for `operations@rsfa.co.nz`.
- Standardise whether automation error emails use `support@rsfa.co.nz` or `tech@rsfa.co.nz`.
- Confirm the contact method for Yuan Gao.

---

## 10. Maintenance rules

Update this document when:

- A staff member joins or leaves.
- A shared mailbox is created or retired.
- Administrative ownership changes.
- A new external vendor becomes relevant.
- A process owner changes.
- A platform account changes.
- A technical-maintenance responsibility changes.
- An adviser-specific flow or board is retired.
- Approval rules change.

Do not add personal phone numbers, home addresses or unrelated personal information.

Preserve exact corporate email addresses and system responsibilities.
