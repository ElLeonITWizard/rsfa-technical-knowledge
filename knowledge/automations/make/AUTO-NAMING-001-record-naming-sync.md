---
id: AUTO-NAMING-001
title: Client, Deal and Policy Naming Synchronisation
platform:
  - Make.com
status: active
criticality: medium
owner: RSFA
technical_account: tech@rsfa.co.nz
business_process: Keep display names on Client Profiles, deals, mortgages and insurance policies aligned whenever the underlying Contact, participant, borrower, adviser or policy-ownership data changes, so records stay recognisable and consistent without manual renaming.
source_systems:
  - Monday.com
related_systems: []
destination_systems:
  - Monday.com
related_boards:
  - name: Client Profiles
    id: "5024661649"
  - name: Contacts
    id: "2074688484"
  - name: "✅️ Existing Mortgages"
    id: "5024672364"
  - name: "✔️ Existing Insurance"
    id: "5024672437"
  - name: "💲Mortgage Pipeline"
    id: "5025201889"
  - name: "➕Insurance Pipeline"
    id: "5025201920"
  - name: "📈 KiwiSaver Pipeline"
    id: "5025201954"
  - name: "Existing KiwiSaver"
    id: "5024672484"
related_scenarios:
  - name: "M.com: CP and Deals Renaming after Contact Renaming"
    id: "1054927"
  - name: "M.com: Renaming after Insurance Policy Added or Owner/Provider Change (Feb 2026)"
    id: "1215342"
  - name: "M.com: Update Existing Mortgages Name from Borrowers (Dec25)"
    id: "1228763"
  - name: "M.com: Updates profile name when participants added"
    id: "1054932"
  - name: "M.com: Update Mortgage Pipeline Name from Borrowers (Dec25)"
    id: "1232945"
related_flows: []
last_modified: 2026-10-31
last_verified: 2026-10-31
documentation_status: partial
---

# AUTO-NAMING-001 — Client, Deal and Policy Naming Synchronisation

## 1. Purpose

Keep the display name of a Client Profile, deal, mortgage or insurance-policy item aligned with its underlying Contact, participant, borrower, adviser or policy-ownership data whenever that data changes — so records remain recognisable and consistent across boards without an adviser manually renaming them after every change.

## 2. Business context

Monday item names are the primary way advisers recognise a record when scanning a board or a linked-item picker. When a Contact is renamed, a participant is added, a mortgage's borrowers change, or an insurance policy's owner/provider changes, every dependent record referencing that entity needs its display name updated to match, or the board becomes confusing and error-prone to work in.

## 3. Scope

### Included

- Renaming Client Profiles and connected deals after a Contact is renamed.
- Renaming an Existing Mortgages item after its Borrowers change.
- Renaming a Client Profile after new participants are added.
- Renaming an Existing Insurance item after a policy is added, or its owner/provider changes.

### Excluded

- The initial creation of Client Profiles/Contacts from a new Lead (`AUTO-LEADS-001`).
- Insurance expiry/anniversary notification logic (`AUTO-INSURANCE-RENEWAL-001`).

## 4. Current status

Active. `Medium` criticality per `knowledge/03_AUTOMATION_REGISTRY.md` §3 — a naming-sync failure affects clarity and efficiency, not correctness of the underlying data.

## 5. Trigger

- `M.com: CP and Deals Renaming after Contact Renaming` (`1054927`): Monday.com instant trigger (watch) — Contact renamed.
- `M.com: Renaming after Insurance Policy Added or Owner/Provider Change (Feb 2026)` (`1215342`): Webhook (custom webhook) — insurance policy added, or owner/provider changed.
- `M.com: Update Existing Mortgages Name from Borrowers (Dec25)` (`1228763`): Monday.com instant trigger (watch) — Borrowers column changed on an Existing Mortgages item.
- `M.com: Updates profile name when participants added` (`1054932`): Monday.com instant trigger (watch) — participant added to a Client Profile.

## 6. Inputs

- Renamed Contact record (name change).
- Existing Mortgages item's `Borrowers` relation.
- Client Profile's linked participants/Contacts.
- Insurance policy's owner and provider fields.

## 7. Outputs

- Updated name on the relevant Client Profile, deal, Existing Mortgages item, or Existing Insurance item.

## 8. Systems involved

Monday.com only (Client Profiles, Contacts, Existing Mortgages, Existing Insurance), via Make.com.

## 9. Related Monday boards

| Board | ID | Role |
|---|---|---|
| Client Profiles | `5024661649` | Renamed on Contact rename or new participant |
| Contacts | `2074688484` | Source of the rename trigger |
| ✅️ Existing Mortgages | `5024672364` | Renamed on Borrowers change |
| ✔️ Existing Insurance | `5024672437` | Renamed on policy add or owner/provider change |

## 10. Platform implementation

### Make.com scenarios

| Scenario ID | Exact Make name | Role | Status | Trigger | Calls | Called by | Source confidence |
|---|---|---|---|---|---|---|---|
| `1054927` | M.com: CP and Deals Renaming after Contact Renaming | Parent | Active | Monday.com instant trigger (watch) | `Outlook: Email Notification after Failed Scenario` (`8732008`) | None confirmed | Current (registry + call graph) only; no dedicated source-material walkthrough |
| `1215342` | M.com: Renaming after Insurance Policy Added or Owner/Provider Change (Feb 2026) | Parent | Active | Webhook (custom webhook) | `Outlook: Email Notification after Failed Scenario` (`8732008`) | None confirmed | Current (registry + call graph) only; no dedicated source-material walkthrough |
| `1228763` | M.com: Update Existing Mortgages Name from Borrowers (Dec25) | Standalone | Active | Monday.com instant trigger (watch) | None confirmed | None confirmed | Current (registry + call graph) only; no dedicated source-material walkthrough |
| `1054932` | M.com: Updates profile name when participants added | Standalone | Active | Monday.com instant trigger (watch) | None confirmed | None confirmed | Current (registry + call graph) only; no dedicated source-material walkthrough |
| `1232945` | M.com: Update Mortgage Pipeline Name from Borrowers (Dec25) | Standalone | Active | Monday.com instant trigger (watch, Borrowers column) | None | None | **Confirmed from live system, 2026-10-31** (blueprint read). Added to this family 2026-10-31 |

Live blueprint inspection on 2026-10-31 (read-only, Make API) confirmed the configuration of all five scenarios — see §10b, §12 and §13. This is a configuration check, not a behaviour test.

No `source-material/make/` file exists for any of these four scenarios — this documentation is built entirely from the registry and call-graph exports.

### Power Automate flows

Not applicable.

### Monday native automations or workflows

Not applicable, per available evidence.

### Native integrations

Not applicable.

### Shared subflows and components

`COMP-MAKE-ERROR-001` — called by `1054927` and `1215342`. `1228763` and `1054932` show no confirmed call to the shared error handler — TODO: verify whether this is a genuine gap.

## 10b. Live configuration verification (2026-10-31)

**Confirmed from live system, 2026-10-31** (Make API blueprint reads; Monday GraphQL reads; nothing executed):

- `1054927` (trigger: Monday "watch item name" on Contacts `2074688484`; last edited 2026-10-25) does, in order:
  1. Writes first/last name columns `text_mkxdmy0m` / `text_mkxdw5rs` on the Contact (first and last word of the name).
  2. Renames the Contact's Client Profile (`board_relation_mkxpzyfq`) to its Contacts (`board_relation38`), with `","` → `" &"`.
  3. Renames every linked **Mortgage Pipeline** (`board_relation_mkyebcmw`), **Existing Mortgage** (`board_relation_mkycc37a`), **KiwiSaver Pipeline** (`board_relation_mkye5k1h`) and **Existing KiwiSaver** (`board_relation_mkyeyfwe`, board `5024672484`) item to that same Client Profile name.
  4. POSTs each of the Contact's Insurance Pipeline (`board_relation_mm0v33yp`) and Existing Insurance (`board_relation_mm0vv3md`) items to `1215342`'s webhook.
- **Discrepancy:** step 3 names mortgage items with the Client Profile name, while `1228763` / `1232945` name them from **Borrowers**. Per RSFA (2026-10-31), Borrowers is the intended rule. The current production behaviour is unchanged; a change is proposed in `rsfa-automation-development/projects/client-profile-related-assets-renaming/`.
- `1054932` renames the Client Profile only when its name has no `&`, or when more than 1 contact is linked. Its error handlers are `Break` retries (no failure email).
- `1228763` / `1232945` have no error handler.
- **No scenario reacts to a Client Profile being renamed.** Only the Power Automate folder rename (`AUTO-SP-FOLDER-001`) does. A Client Profile renamed manually leaves its related items unchanged.
- Naming done outside this family (at creation or by other families), for reference:
  - Leads: CP name, at creation, by `8800779`.
  - Mortgage App: CP name, by `8410524`.
  - Insurance / KiwiSaver Questionnaire: Contact name, by `9447215`.
  - SOP Masterboard `5026186805`: CP name, every 900 s, by `10037840` "RSFA – End Forms: Client Profile link and record name sync" (first 500 items only).
  - Aircall `5026308494`: linked Contact name, by `9869454`; `Unknown` when the caller is not matched.
- `9711585` "M.com: Lead Rename by ClientProfile (Mar 2026)" exists but is **inactive** and holds only a webhook module (hook `4335040`). No Monday webhook points to it: the Leads board has no webhook on `board_relation_mm7c1wcw`.

## 11. End-to-end process

```mermaid
flowchart LR
    A[Contact renamed] --> B[M.com: CP and Deals Renaming after Contact Renaming]
    B --> C[Rename linked Client Profile + connected deals]
    D[Borrowers changed on Existing Mortgages item] --> E[M.com: Update Existing Mortgages Name from Borrowers]
    E --> F[Rename Existing Mortgages item]
    G[Participant added to Client Profile] --> H[M.com: Updates profile name when participants added]
    H --> I[Rename Client Profile]
    J[Insurance policy added or owner/provider changed] --> K[M.com: Renaming after Insurance Policy Added or Owner/Provider Change]
    K --> L[Rename Existing Insurance item]
```

## 12. Data mapping

**Confirmed from live system, 2026-10-31** (blueprint formulas):

| Target | Name formula (Make) | Scenario |
|---|---|---|
| Client Profile `5024661649` | `replace(Contacts.text; ","; " &")` — Contacts `board_relation38` | `1054927`, `1054932` |
| Mortgage Pipeline `5025201889` | `replace(Borrowers.text; ","; " &")` — Borrowers `board_relation_mkyf123a` | `1232945` |
| Existing Mortgages `5024672364` | `replace(Borrowers.text; ","; " &")` — Borrowers `board_relation_mkyjjs0w` | `1228763` |
| Mortgage Pipeline, Existing Mortgages, KiwiSaver Pipeline, Existing KiwiSaver | Client Profile name (as above) | `1054927` (see §10b discrepancy) |
| Insurance Pipeline `5025201920` | Policy Owner names (`board_relation_mkyjddgg`, in link order) joined `" & "` + `" \| " + Provider` (`color_mkxpxs6j`) when not empty | `1215342` |
| Existing Insurance `5024672437` | Policy Owner names (`board_relation_mkyjvgra`) joined `" & "` + `" \| " + Insurance Provider` (`label9`) when not empty | `1215342` |

In the Monday API the board-relation `text` field is `null`; Make builds `.text` itself. API consumers should use `display_value` (same order as the links).

## 13. Decision and routing logic

Confirmed 2026-10-31 (§12): names are joined in link order with `" & "`; no truncation or de-duplication is applied; an empty relation leaves the item unchanged (`1228763`/`1232945` filter on linked IDs existing; `1215342` filters on owners not empty).

## 14. Dependencies

- Depends on the source data (Contact name, Borrowers, participants, policy owner/provider) being accurate at the time of the triggering change.
- Interacts with `AUTO-LEADS-001` (initial creation) and `AUTO-MASTERBOARD-001`/`AUTO-MORTGAGE-RENEWAL-001`/`AUTO-INSURANCE-RENEWAL-001` (which reference these same items by name in generated documents and emails) — a naming inconsistency here could cause a mismatched display name to appear downstream, though the underlying record link itself is unaffected.

## 15. Error handling

`1054927` and `1215342` call `COMP-MAKE-ERROR-001`. `1228763` and `1054932` have no confirmed error-handling call in the current call-graph export.

## 16. Logging and observability

No dedicated log confirmed for this family.

## 17. Manual operations and reprocessing

Not confirmed. TODO: verify whether an item's name can be safely manually corrected without being immediately overwritten on the next trigger, or whether a manual edit would be reverted.

## 18. Known limitations

- No implementation walkthrough exists for any of the four scenarios in this family — naming-format rules, edge cases (e.g. very long names, special characters) and error-handling completeness are all unconfirmed.
- Two of the four scenarios show no confirmed shared-error-handler call, unlike their siblings in other families.

## 19. Security and sensitive data

This automation only manipulates item display names, which are typically client names — treat as client personal data; do not use real client names in test items.

## 20. Testing

### Confirmed tests

None recorded.

### Required regression tests

- Contact renamed → linked Client Profile and connected deals renamed correctly.
- Existing Mortgages `Borrowers` changed → item renamed correctly.
- New participant added to a Client Profile → profile renamed correctly.
- Insurance policy added, or owner/provider changed → Existing Insurance item renamed correctly.
- Manual name edit → confirm whether it survives the next unrelated trigger, or is overwritten.

### Test data restrictions

Use fictional test Contacts, Client Profiles, mortgages and insurance policies only.

## 21. Validation after change

Rename a test Contact and confirm the linked Client Profile and any connected test deals update correctly; change Borrowers on a test mortgage and confirm the item renames correctly; add a participant to a test Client Profile and confirm renaming; add/change a test insurance policy's owner/provider and confirm renaming.

## 22. Rollback

Disable the affected Make.com scenario(s). No automated rollback of already-applied name changes is defined — a name could be manually reverted if needed.

## 23. Troubleshooting guide

1. Confirm the underlying triggering field (Contact name, Borrowers, participants, policy owner/provider) actually changed, not just displayed differently.
2. Check for `COMP-MAKE-ERROR-001` failure emails on `1054927` and `1215342`.
3. For `1228763` and `1054932`, check Make.com scenario run history directly, since no shared error-handler call is currently confirmed.

## 24. Source references

- `exports/make/valid-scenarios-working-inventory.md`, `exports/make/make-scenario-call-graph.md` — Current. Scenario IDs, trigger types, status, error-handler calls.
- `knowledge/03_AUTOMATION_REGISTRY.md` §3, §4 — Current. Canonical ID and family grouping.
- `knowledge/04_MONDAY_BOARDS_REGISTRY.md` — Current. Board IDs and column context.
- No `source-material/make/` file exists for any scenario in this family.

## 25. Known gaps

- ~~Naming-format rules unconfirmed~~ — confirmed from live blueprints 2026-10-31 (§12).
- Mortgage naming conflict between `1054927` (Client Profile name) and `1228763`/`1232945` (Borrowers) — §10b. Unresolved in production.
- No automation cascades a **Client Profile** rename to related items. Proposed in `rsfa-automation-development/projects/client-profile-related-assets-renaming/` (not deployed).
- Missing shared-error-handler call for two of the four scenarios is unexplained.
- Manual-edit survivability is unconfirmed.

## 26. Change history

| Date | Change | Author |
|---|---|---|
| 2026-07-30 | Initial canonical documentation created from registry and call-graph evidence only; no source-material walkthrough available for any scenario in this family. | Claude (documentation task) |
| 2026-10-31 | Live configuration verification (read-only blueprint reads): added `1232945` and the pipeline boards, confirmed naming formulas (§12, §13), documented what `1054927` actually renames, the mortgage-rule discrepancy, the absence of a Client-Profile-rename cascade, and the inactive `9711585` shell (§10b). Behaviour not re-tested. | Claude (Client Profile renaming project) |
