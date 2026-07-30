---
id: SYS-PA-001-CONNECTION-REFERENCES
title: Power Automate — Connection References
status: active
owner: RSFA
last_modified: 2026-07-30
last_verified: 2026-07-30
---

# Power Automate — Connection References

## 1. Purpose

Consolidated index of every connection reference found across the current Power Automate Solution export set (`exports/power-automate/solutions/`). Sourced entirely from each Solution's `customizations.xml` — confirmed from export, not from a live Power Automate check.

## 2. Consolidated connection references

| Logical name | Display name | Connector/API | Solutions where it appears |
|---|---|---|---|
| `cr3e8_Slack_RSFA` | Slack_RSFA | `shared_slack` | docusign-to-sharepoint, rsfa-outlook-email-filing |
| `new_sharedoffice365_89be1` | Outlook_Tech_RSFA_02 | `shared_office365` | docusign-to-sharepoint, rsfa-outlook-email-filing |
| `rsfa_shareddocusign_c7609` | Docusign RSFAActiveAutomations-c7609 | `shared_docusign` | docusign-to-sharepoint |
| `rsfa_sharedsharepointonline_8fd5d` | SharePoint RSFAActiveAutomations-8fd5d | `shared_sharepointonline` | docusign-to-sharepoint, rsfa-outlook-email-filing |
| `cr3e8_Outlook_Jet_RSFA` | Outlook_Jet_RSFA | `shared_office365` | rsfa-outlook-email-filing |
| `cr3e8_Outlook_Jet_RSFA_02` | Outlook_Jet_RSFA_02 | `shared_office365` | rsfa-outlook-email-filing |
| `cr3e8_Outlook_Seth_RSFA` | Outlook_Seth_RSFA | `shared_office365` | rsfa-outlook-email-filing |
| `cr3e8_sharedoffice365_591c0` | Outlook_Tech_RSFA | `shared_office365` | rsfa-outlook-email-filing |
| `cr3e8_sharedsharepointonline_23323` | SP Tech RSFA 02 | `shared_sharepointonline` | rsfa-outlook-email-filing, sp-adviser-name-change |
| `new_sharedoffice365_4ebbe` | Outlook_Support_RSFA | `shared_office365` | rsfa-outlook-email-filing |
| `new_sharedwordonlinebusiness_5aa2e` | Word Online (Business) | `shared_wordonlinebusiness` | rsfa-outlook-email-filing |
| `rsfa_sharedoffice365_326a9` | **Outlook_Insurance_RSFA** | `shared_office365` | rsfa-outlook-email-filing |
| `rsfa_sharedoffice365_91c50` | Outlook_Rod_RSFA | `shared_office365` | rsfa-outlook-email-filing |
| `rsfa_sharedslack_c50e1` | Slack RSFAActiveAutomations-c50e1 | `shared_slack` | rsfa-outlook-email-filing |
| `rsfa_SharePointConnection` | SharePoint Connection | `shared_sharepointonline` | rsfa-outlook-email-filing |
| `cr3e8_sharedoffice365_4938b` | SP Tech RSFA | `shared_office365` | sp-adviser-name-change |
| `cr3e8_sharedoffice365_49c3f` | Office 365 Outlook SPClientFolderCreationandRenaming-49c3f | `shared_office365` | sp-client-folder-creation-and-renaming |
| `cr3e8_sharedsharepointonline_10f77` | SharePoint SPClientFolderCreationandRenaming-10f77 | `shared_sharepointonline` | sp-client-folder-creation-and-renaming |

`cr3e8_sharedsharepointonline_23323` ("SP Tech RSFA 02") is the one connection reference confirmed shared, by identical logical name, across two different Solutions (`rsfa-outlook-email-filing` and `sp-adviser-name-change`).

## 3. Flows that appear to use each reference

Per-flow connection-reference usage was **not individually traced for every flow** in this inspection pass — each Solution's `customizations.xml` lists the connection references available to the whole Solution, but confirming exactly which of a Solution's flows calls which specific reference would require reading every workflow JSON's `connectionReferences` block flow-by-flow. This has been done only spot-check style (e.g. confirming the DocuSign flow uses all four of its Solution's references). Treat "Solutions where it appears" above as Solution-level evidence, not flow-level, until this is completed — **known gap**.

## 4. Connection owners

Not confirmed for any connection reference in this list. Unmanaged Solution exports do not carry connection-owner information. `TODO: verify` against the live Power Automate environment if ownership needs to be confirmed for a specific investigation (e.g. what happens if the owning user's account is disabled).

## 5. Secret values

**Never stored.** No connection reference here includes a client secret, API key, or token value — those live in the underlying Connection object in Power Automate, not in the exported Connection Reference metadata, and must never be added to this file or any other document in this repository.

Separately, several flows in this export set were found to call Monday.com and OpenAI via **hardcoded HTTP Authorization headers instead of a Connection Reference** — see the Security Review section of each affected Solution manifest under `exports/power-automate/solutions/`. This is a known anti-pattern (bypassing the Connection Reference / Environment Variable mechanism entirely) and a live credential-exposure finding, not merely a documentation gap.

## 6. Gaps in ownership or configuration

- Connection owners are unconfirmed for all 18 connection references listed above.
- Flow-level (not just Solution-level) usage of each reference is unconfirmed.
- Whether `Outlook_Insurance_RSFA` is actively used by a currently-enabled flow, or is a leftover/in-progress reference, is unconfirmed — see `exports/power-automate/solutions/rsfa-outlook-email-filing/manifest.md` for the related flow-mapping gap.
- Whether `Word Online (Business)` (`new_sharedwordonlinebusiness_5aa2e`) is actually invoked by any action, or just declared and unused, is unconfirmed.
