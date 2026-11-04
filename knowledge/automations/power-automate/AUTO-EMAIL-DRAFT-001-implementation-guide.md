---
id: DOC-EMAIL-DRAFT-002
title: Email Drafting Agent — Power Automate implementation guide (v1)
status: planned
owner: RSFA
related_automations:
  - AUTO-EMAIL-DRAFT-001
  - AUTO-EMAIL-001
last_modified: 2026-11-04
last_verified: "TODO: verify — not yet built"
---

# Email Drafting Agent — implementation guide (v1)

Companion to `AUTO-EMAIL-DRAFT-001-email-drafting-agent.md` (design, guardrails, test plan). This file is the **build checklist**: exactly what to change in the existing flows, which flows to create, and which actions each one contains.

> **Evidence base.** Flow JSON exports of `Main Outlook Inbox Email Filling`, `Outlook Email Filling - Rod v2` and `Outlook SENT Email Filling - Rod v2` supplied by Leonardo Melman in chat on 2026-11-04 (current-export-snapshot, not live-verified). They are **newer than** the `RSFAOutlookEmailFilling` 1.0.0.3 snapshot under `exports/` (they include Power Automate Runs logging, `text_3`–`text_5` inputs, `ResolvedMessageID`, `contactmatchingdetails`, and the `it-support` mailbox). They were not stored in this repository (they contain a plaintext Monday token — see §0.1). Action names below are taken from those 2026-11-04 exports.

> **Nothing here has been built or tested.** Status of every step: `Planned`.

---

## 0. Prerequisites (do these first)

### 0.1 Security — before anything else

- The 2026-11-04 exports still contain the **same literal Monday API token** in `Create_item_in_PA_Executions_Board` / `Update_Log_Column_Values*` (all three flows). The rotation recommended on 2026-07-30 has therefore not happened yet, or the old token is still valid. Rotate it and treat any copy of those JSON files as sensitive.
- The new flows must **not** contain any literal secret. Choose one:
  - **Option A (preferred):** Azure Key Vault + Environment Variables of type *Secret* (`rsfa_EDA_OpenAIKey`, `rsfa_EDA_MondayToken`). Needs an Azure subscription — TODO: verify.
  - **Option B (no Azure):** two custom connectors in the environment — `RSFA OpenAI` (host `api.openai.com`, API-key auth, header `Authorization`) and `RSFA Monday API` (host `api.monday.com`, API-key auth, header `Authorization`). The key lives in the connection, not in the flow definition.
- In every HTTP/Graph action that carries email content or client data: **Settings → Secure inputs + Secure outputs = On**.

### 0.2 Backup

1. Export the `SP Email Filling` Solution (`RSFAOutlookEmailFilling`) as **unmanaged** and keep the zip (rollback point). Also `Save As` copies are **not** recommended (they create duplicate triggers).
2. Record the current version number of the Solution.

### 0.3 Monday (done 2026-11-04 — see §6)

Boards `✉️ Email Drafting Agent: Drafts` (`5032291843`) and `⚙️ Email Drafting Agent: Mailbox Settings` (`5032291851`) exist with fixed column IDs. Still to do manually:

- On `⚡ Power Automate Runs` (`5030408927`), add the dropdown label **`Email Drafting Agent`** to the `Solution` column (`dropdown_mm5xp991`).
- After building flow 4, create the Monday webhook (§5).

### 0.4 New Solution

- Create Solution: Display name **`Email Drafting Agent`**, Name **`RSFAEmailDraftingAgent`**, publisher = the publisher that owns the `rsfa_` prefix (the prefix used by `rsfa_sharedoffice365_91c50`) — TODO: verify publisher name in Solutions → Publishers.
- Connection references (new, inside this Solution):

| Display name | Logical name (auto from publisher) | Connector | Connection to use |
|---|---|---|---|
| `EDA_Outlook_Rod_RSFA` | `rsfa_EDA_Outlook_Rod_RSFA` | Office 365 Outlook | The same connection as `Outlook_Rod_RSFA` (`rsfa_sharedoffice365_91c50`). Export evidence: `Get_Email_Body_Rod` calls `GET /me/messages/{id}` on Rod's Inbox message through this connection, so `/me` resolves to Rod's mailbox |
| `EDA_Outlook_Tech_RSFA` | `rsfa_EDA_Outlook_Tech_RSFA` | Office 365 Outlook | Same connection as `Outlook_Tech_RSFA` (`cr3e8_sharedoffice365_591c0`) — test mailbox |
| `EDA_SharePoint_RSFA` | `rsfa_EDA_SharePoint_RSFA` | SharePoint | Same connection as `rsfa_sharedsharepointonline_8fd5d` |
| `EDA_KeyVault_RSFA` or the 2 custom connectors | — | per §0.1 | — |

- Environment variables (Text unless stated):

| Schema name | Value |
|---|---|
| `rsfa_EDA_DraftsBoardId` | `5032291843` |
| `rsfa_EDA_SettingsBoardId` | `5032291851` |
| `rsfa_EDA_RunsBoardId` | `5030408927` |
| `rsfa_EDA_RunsGroupId` | `group_mm5xsbsv` |
| `rsfa_EDA_ExtPropId` | `String {90e70716-23a1-4f23-84e2-f97649d4df7d} Name RSFAEmailDraftItemId` |
| `rsfa_EDA_OpenAIModel` | `gpt-4o` (initial; confirm in T-20). Not adviser-editable since 2026-11-04 |
| `rsfa_EDA_OpenAIKey` / `rsfa_EDA_MondayToken` | Secret (Option A only) |

The GUID above is fixed for this project — never change it, or sent drafts can no longer be matched.

### 0.5 Child-flow rules (apply to every `Child - …` flow)

- Trigger: **Manually trigger a flow** (instant) with typed text inputs.
- Details → *Run only users* → each connection set to **Use this connection (…)**, never *Provided by run-only user*. Otherwise the parent's `Run a Child Flow` fails.
- Must end every path with **Respond to a PowerApp or flow** (same output schema on all of them).
- If `Child - Email Drafting Agent - Intake` does not appear in the `Run a Child Flow` picker inside `Outlook Email Filling - Rod v2`, add it to the `SP Email Filling` Solution too (*Add existing → Automation → Cloud flow*). A flow can belong to both unmanaged Solutions.

---

## 1. Change A — `Main Outlook Inbox Email Filling` (`f6906da4-c8ed-ef11-9341-6045bd3ce9ae`)

**Goal:** let the caller know whether the email was filed into a client folder, which Client Profile, and the direction. Additive only — `status`, `slackbackupchannels`, `contactmatchingdetails` are unchanged.

Power Automate requires all *Respond to a PowerApp or flow* actions in a flow to share one output schema, so add the **same four Text outputs to all seven Response actions**:

| Output name (exact, lowercase) | Description |
|---|---|
| `matchstatus` | `ClientFolder` / `NoMatch` / `OldSite` / `Error` / `Unknown` |
| `clientprofileid` | Client Profile item ID when `matchstatus = ClientFolder` |
| `direction` | `Received` / `Sent` / `Internal` (empty if not computed) |
| `resolvedmessageid` | Graph message ID actually used by the flow |

Values per action:

| Response action (exact name) | Where it is | `matchstatus` | `clientprofileid` | `direction` | `resolvedmessageid` |
|---|---|---|---|---|---|
| `Respond_to_a_Parent_Flow_Success_02` | `Try_Upload_Email_to_SP` → `ID_Not_Found` (else) → `Were_File_Properties_Updated` (true) | `ClientFolder` | `@{outputs('Get_ClientID')}` | `@{variables('StatusVariable')}` | `@{variables('ResolvedMessageID')}` |
| `Respond_to_a_Parent_Flow_Success_03` | `ID_Not_Found` (true) → `No_Duplicate_Found_in_Common_Folder` | `NoMatch` | *(empty)* | `@{variables('StatusVariable')}` | `@{variables('ResolvedMessageID')}` |
| `Respond_to_a_Parent_Flow_Success_RSFA_Team_Old_Site` | `Were_File_Properties_Updated` (false) → `Client_Folder_not_in_Real_Savvy_Clients_Site` | `OldSite` | *(empty)* | `@{variables('StatusVariable')}` | `@{variables('ResolvedMessageID')}` |
| `Respond_to_a_Parent_Flow_Success` | top level, `Child_did_not_Respond` | `Unknown` | *(empty)* | `@{variables('StatusVariable')}` | `@{variables('ResolvedMessageID')}` |
| `Respond_to_a_Parent_Flow_Upload_Email_Error` | `Catch_Upload_Email_to_SP_Error` | `Error` | *(empty)* | `@{variables('StatusVariable')}` | `@{variables('ResolvedMessageID')}` |
| `Respond_to_a_Parent_Flow_Monday.com_Search_Error` | `Catch_Monday.com_Search_Error` | `Error` | *(empty)* | *(empty)* | `@{variables('ResolvedMessageID')}` |
| `Respond_to_a_Parent_Flow_Switch_Error` | `Catch_Switch_Error` | `Error` | *(empty)* | *(empty)* | *(empty)* |

Notes:

- `Get_ClientID` is the Client Profile **item ID** (used as `item_id` in `Add_Email_to_Timeline_Monday`), so no extra lookup is needed.
- `StatusVariable` is set inside `Try_Upload_Email_to_SP` → `Is_Internal_Email`. `Received` requires the sender to be non-RSFA **and** the mailbox address to be in **To** (`Recipient_Address`). An external email where Rod is only in **CC** is classified `Sent` today → no draft for it in v1 (documented limitation, do not change the filing logic for this).
- Do not change anything else in `Main`. Save → test with T-02 (regression) before Change B.

---

## 2. Change B — `Outlook Email Filling - Rod v2` (`d34b8f51-46f8-ef11-bae2-002248185f06`)

Current top-level order (2026-11-04 export): `Initialize_*` → `Compose_Processing_Details_JSON_Column` → `Compose_PA_Run_Column_Values` → `Create_item_in_PA_Executions_Board` → `Try_Run_Main_Filling_Flow` → `Catch_Send_Fail_Email` → `Flow_Has_Failed`.

**Do not put the drafting call inside `Try_Run_Main_Filling_Flow`.** A failure there runs `Catch_Send_Fail_Email`, which forwards the email to `tech@` + `fails_ai_emails` as `Failed Item Email Filling` → it would be re-filed.

Add at the **end** (after `Flow_Has_Failed`):

```
Try_Run_Email_Drafting_Agent            [Scope]
  runAfter: Flow_Has_Failed = Succeeded, Failed, Skipped, TimedOut
  └─ Is_Client_Email_for_Drafting       [Condition]
       AND:
         @variables('FailedFlag')                                          is equal to  @false
         @body('Run_a_Main_Email_Filling_Flow')?['matchstatus']            is equal to  ClientFolder
         @body('Run_a_Main_Email_Filling_Flow')?['direction']              is equal to  Received
       True:
         └─ Run_Email_Drafting_Agent_Intake   [Run a Child Flow → Child - Email Drafting Agent - Intake]
              mailbox          = @{variables('MailConnection')}
              messageid        = @{body('Run_a_Main_Email_Filling_Flow')?['resolvedmessageid']}
              internetmessageid= @{triggerOutputs()?['body/internetMessageId']}
              clientprofileid  = @{body('Run_a_Main_Email_Filling_Flow')?['clientprofileid']}
              parentlogid      = @{body('Create_item_in_PA_Executions_Board')?['data']?['create_item']?['id']}
              advisername      = Rod
       False: (empty)

Catch_Email_Drafting_Agent              [Scope]
  runAfter: Try_Run_Email_Drafting_Agent = Failed, TimedOut
  └─ Compose_Email_Drafting_Agent_Error [Compose]  @{result('Try_Run_Email_Drafting_Agent')}
```

Rules for `Catch_Email_Drafting_Agent`: **no** `Set_Failed_Flag_*`, **no** `Forward_Failed_Email_*`, **no** deletes. (Intake logs its own failures — §3.1.) Optionally add an `Update_Log_Column_Values` call writing `Developer Notes` on the parent run item.

Settings of `Run_Email_Drafting_Agent_Intake`: Timeout `PT2M`. Intake responds within seconds (§3.1), so the Rod flow is delayed only by that response.

`Outlook SENT Email Filling - Rod v2` is **not modified**. Sent detection is a separate flow (§3.5).

---

## 3. New flows (all in Solution `RSFAEmailDraftingAgent`)

| # | Flow name (exact) | Trigger |
|---|---|---|
| 3.0 | `Child - Email Drafting Agent - Outlook Graph Request` | Manual (child) |
| 3.1 | `Child - Email Drafting Agent - Intake` | Manual (child) |
| 3.2 | `Child - Email Drafting Agent - Generate Draft` | Manual (child) |
| 3.3 | `Monday - Email Drafting Agent - Adviser Action Handler` | When an HTTP request is received |
| 3.4 | `Scheduled - Email Drafting Agent - Draft Reconciliation` | Recurrence |
| 3.5 | `Outlook - Email Drafting Agent - Sent Items Sync - Rod` | When a new email arrives (V3), Rod, Sent Items |
| 3.6 | `Manual - Email Drafting Agent - Test Harness` | Manual (testing only; turn off after go-live) |

Naming follows `knowledge/06_NAMING_AND_ID_CONVENTIONS.md` §7 (`[Source] - [Action] - [Scope]`, `Child -` / `Manual -` qualifiers). Action names follow the existing flows' style (`Try_…`, `Catch_…`, `Compose_…`, `Create_item_in_PA_Executions_Board`, `Update_Log_Column_Values`).

### Common blocks used in every flow

**Run logging (copy of the existing pattern, Solution label changed):**

- `Compose_PA_Run_Column_Values` → same structure as in `Outlook Email Filling - Rod v2`, but `dropdown_mm5xp991.labels = ["Email Drafting Agent"]` and `board_relation_mm5x7zse.item_ids = [parentlogid]` when a parent log ID is passed.
- `Create_item_in_PA_Executions_Board` → board `@{parameters('rsfa_EDA_RunsBoardId')}`, group `@{parameters('rsfa_EDA_RunsGroupId')}`, name `@{advisername} - Email Drafting Agent <step> - dd-MM-yyyy hh:mm:ss`.
- `Update_Log_Column_Values` → `color_mm5xna8e` = `Succeeded` / `Failed`, `date_mm5xge5j` = now NZT.
- Monday auth: Option A header `Authorization: @{parameters('rsfa_EDA_MondayToken')}` or Option B custom connector action. **Never a literal.**

**Monday "update Drafts item" pattern** (used everywhere): `change_multiple_column_values(board_id: rsfa_EDA_DraftsBoardId, item_id: X, column_values: JSON, create_labels_if_missing: false)`. Move between groups with `move_item_to_group`.

Drafts board group IDs: `topics` = **Needs Review**, `group_mm8sfnf` = **Processing**, `group_mm8sta8g` = **Done (Sent / Discarded)**, `group_mm8s3hhz` = **No Draft**.

**Status model (simplified 2026-11-04 at Leonardo Melman's request — authoritative).** `eda_draft_status` has seven adviser-facing labels; the reason goes in `eda_reason` (**Status Detail**, text). Flows must use these exact strings:

| `eda_draft_status` | Group | `eda_reason` (Status Detail) values written by flows |
|---|---|---|
| `Processing` | `group_mm8sfnf` | *(empty)* |
| `Ready for review` | `topics` | empty · `Regenerated with adviser instructions` · `Regenerated` |
| `Needs attention` | `topics` | `Edited in Outlook - finish there, or Discard / Regenerate` · `AI unavailable - use Regenerate` · `Invalid AI output - use Regenerate` · `Intake error` · `Generate error` · `Not an allowed approver` |
| `Sent from Outlook` | `group_mm8sta8g` | `No edits` · `Edited before sending` |
| `Sent from Monday` | `group_mm8sta8g` | *(empty)* — Monday sends exactly the current `Draft Text` |
| `Discarded` | `group_mm8sta8g` | `Deleted in Outlook` · `Discarded from Monday` · `Replaced by newer email in same thread` · `Replaced by newer email - old draft kept (edited in Outlook)` |
| `No draft` | `group_mm8s3hhz` | `No reply needed` · `Automatic message` · `Sender not verified as client contact` · `Protected message` · `Daily cap reached - use Regenerate` |

- There is no "Stale" status: old drafts are found with a board view filtered on `Draft Created At`.
- The flows decide on **status + Status Detail + `eda_change_key`**. An Outlook edit is detected live by a changeKey mismatch (→ `Needs attention`). An edit of `Draft Text` in Monday needs no detection: **Approve & send always rebuilds the Outlook draft from the Monday text before sending** (§3.3).
- **Adviser actions (reduced 2026-11-04): `Approve & send`, `Regenerate`, `Discard`.** There is no "Update Outlook draft" action any more.
- **Regenerate** = new draft at **Medium** depth (adds linked business + client timeline) using the adviser's **Instructions for AI** (`eda_ai_instructions`) when filled. Without instructions it only adds context, so the board help text tells the adviser to write instructions first. Depth used is written in `eda_model` (**Model / Depth**). Automatic drafts are always **Basic**. `Deep` is not used in v1 (kept in the design for later).
- **Signature:** the flow appends `eds_signoff` (**Email Signature (HTML)**) to every draft automatically (§3.2). `Draft Text` in Monday never contains the signature, so it is never duplicated when Monday text is pushed.
- **Recipients:** drafts are always created with `createReplyAll` (Reply mode column removed). CC recipients are listed in `Notes for Adviser` so they are visible in Monday before Approve & send.

---

### 3.0 `Child - Email Drafting Agent - Outlook Graph Request`

Single place that knows which Outlook connection serves which mailbox (same idea as `Switch_Email_Connection` in `Main`). Adding a mailbox later = one new case here.

Inputs: `mailbox`, `method`, `uri` (relative, e.g. `/me/messages/{id}`), `body` (text, may be empty), `bodytextonly` (`true`/`false`).

```
Compose_Prefer_Header   = @{if(equals(triggerBody()?['bodytextonly'],'true'),
                               'outlook.body-content-type="text", IdType="ImmutableId"',
                               'IdType="ImmutableId"')}
Switch_Mailbox_Connection  on @toLower(triggerBody()?['mailbox'])
  Case_Rod   rod@rsfa.co.nz  → Send_an_HTTP_request_Rod   (Office 365 Outlook › Send an HTTP request, conn EDA_Outlook_Rod_RSFA)
  Case_Tech  tech@rsfa.co.nz → Send_an_HTTP_request_Tech  (conn EDA_Outlook_Tech_RSFA)
  Default                    → Respond_Unsupported_Mailbox (statuscode 400)
     Each HTTP action: URI = https://graph.microsoft.com/v1.0@{triggerBody()?['uri']}
                       Method = @{triggerBody()?['method']}
                       Body = @{triggerBody()?['body']}   Content-Type = application/json
                       CustomHeader1 = Prefer: @{outputs('Compose_Prefer_Header')}
                       Settings: Secure inputs/outputs ON; Retry policy exponential, 3
     Each case ends with Respond_Graph_Result_<Case> (runAfter Succeeded AND Failed):
        statuscode = @{outputs('Send_an_HTTP_request_Rod')?['statusCode']}
        responsebody = @{string(body('Send_an_HTTP_request_Rod'))}
```

Callers parse `responsebody` with `json()`. A 404 is a valid answer (deleted draft), so callers must check `statuscode` rather than relying on action failure.

---

### 3.1 `Child - Email Drafting Agent - Intake`

Inputs: `mailbox`, `messageid`, `internetmessageid`, `clientprofileid`, `parentlogid`, `advisername`.

```
Respond_to_Parent_Accepted                [Response] status=Accepted  (FIRST ACTION — parent continues immediately)
Initialize_variable_SkipReason            [string] ''
Initialize_variable_DraftItemId           [string] ''
Compose_PA_Run_Column_Values / Create_item_in_PA_Executions_Board   (log, parent = parentlogid)

Try_Intake [Scope]
  Get_Mailbox_Settings          [HTTP Monday]
      query { items_page_by_column_values(board_id: <SettingsBoardId>, limit: 1,
              columns: [{column_id: "name", column_values: ["<mailbox>"]}]) {
              items { id column_values(ids:["eds_enabled","eds_daily_cap"]) { id text } } } }
  Compose_Settings              → object {enabled, dailycap} from column_values text
  Mailbox_Enabled               [Condition] enabled == 'Yes'
     False → Update_Log (Succeeded, Developer Notes "mailbox disabled") → Terminate Succeeded
  Check_Duplicate_Message       [HTTP Monday] items_page_by_column_values on eda_internet_msg_id = internetmessageid
     If found → Terminate Succeeded (no new item)
  Get_Incoming_Email            [Run Child: Graph Request]
      GET /me/messages/<messageid>?$select=id,subject,from,toRecipients,ccRecipients,receivedDateTime,
          conversationId,internetMessageId,internetMessageHeaders,webLink,sensitivity,uniqueBody   (bodytextonly=true)
  Parse_Incoming_Email          [Parse JSON] json(responsebody)
  Get_Client_Contacts_Emails    [HTTP Monday]
      query { items(ids:[<clientprofileid>]) { name column_values(ids:["board_relation38"]) {
              ... on BoardRelationValue { linked_items { column_values(ids:["contact_email","email_mkxd41p7","email_mkxdantz"]) { text } } } } } }
  Compose_Client_Emails_Text    → toLower(string(body)) (used with contains())
  Create_Drafts_Item            [HTTP Monday] create_item(board_id: DraftsBoardId, group_id: "group_mm8sfnf", item_name: <subject, max 120, 'No Subject'>,
        column_values: eda_draft_status=Processing, eda_client_profile={item_ids:[clientprofileid]},
        eda_mailbox={labels:[mailbox]}, eda_sender_email, eda_received_at (NZT), eda_original_link={url: webLink, text:"Open email"},
        eda_message_id=<immutable id>, eda_internet_msg_id, eda_conversation_id, eda_pa_run={item_ids:[run log id]})
  Set_DraftItemId

  Eligibility checks — first failure sets SkipReason (exact texts):
   1 Sender_Not_RSFA_and_Is_Client_Contact
        not(contains(toLower(from), 'rsfa.co.nz')) AND contains(Compose_Client_Emails_Text, toLower(from))
        else 'Sender not verified as client contact'
   2 Is_Automatic_Message   any of:
        internetMessageHeaders has Auto-Submitted ≠ 'no' | X-Auto-Response-Suppress | Precedence in (bulk,list,junk)
        from startsWith/contains 'noreply','no-reply','mailer-daemon','postmaster'
        subject startsWith 'Automatic reply','Out of Office','Undeliverable','Delivery Status Notification'
        → 'Automatic message'
        (headers: Filter array on internetMessageHeaders where toLower(item()?['name']) equals 'auto-submitted', etc.)
   3 Is_Protected_Message   sensitivity in ('private','confidential') → 'Protected message'   (TODO verify IRM detection in testing)
   4 Daily_Cap_Reached      [HTTP Monday] items_page(limit:500, query_params:{rules:[
          {column_id:"eda_mailbox", compare_value:[<dropdown label id>], operator:any_of},
          {column_id:"eda_draft_created", compare_value:["TODAY"], operator:any_of}]})
        length(items) >= dailycap → 'Daily cap reached - use Regenerate'
  Has_Skip_Reason [Condition] SkipReason not empty
     True  → Update Drafts item: eda_draft_status='No draft', eda_reason=SkipReason; move_item_to_group group_mm8s3hhz
     False → Supersede_Previous_Drafts (below) → Run_Generate_Draft [Run Child: Generate Draft]
                 draftitemid, mailbox, depth=Basic, parentlogid=<this run log id>, advisername

  Supersede_Previous_Drafts:
     Get_Open_Drafts_Same_Conversation [HTTP Monday] items_page rules eda_conversation_id = conversationId
          AND eda_draft_status any_of [Ready for review, Needs attention]  (exclude current item)
     Apply_to_each_Open_Draft:
        Get_Previous_Draft [Graph] GET /me/messages/<eda_draft_id>?$select=id,changeKey
        Draft_Unchanged [Condition] statuscode == 200 AND changeKey == eda_change_key
          True  → Delete_Previous_Draft [Graph] DELETE /me/messages/<id>; status='Discarded', eda_reason='Replaced by newer email in same thread'; group Done
          False → status='Discarded', eda_reason='Replaced by newer email - old draft kept (edited in Outlook)' (do NOT delete)
Catch_Intake [Scope] runAfter Try_Intake Failed/TimedOut
  If DraftItemId not empty → status='Needs attention', eda_reason='Intake error', eda_last_run=<run url>
  Update_Log_Column_Values → Failed
  Send_Failure_Notification → To tech@rsfa.co.nz, Subject 'Email Drafting Agent Failure', body: run URL + Drafts item link ONLY (no email content)
```

Concurrency: trigger concurrency limit 5.

Note: the Intake has already responded, so a failure here never returns `Failed` to the Rod flow.

---

### 3.2 `Child - Email Drafting Agent - Generate Draft`

Inputs: `draftitemid`, `mailbox`, `depth` (`Basic`/`Medium`/`Deep`), `parentlogid`, `advisername`, `mode` (`New` / `Regenerate` / `MondayText`). `Regenerate` is always called with depth `Medium` and reads `eda_ai_instructions`.

Unlike Intake, this flow responds **at the end** (`Respond_Result` with `result` = `DraftReady` / `NoReplyNeeded` / `EditedInOutlook` / `Failed`, plus `draftid`), because the Action Handler must wait for the rebuilt draft before sending it. The caller of a child flow waits for roughly 2 minutes at most (TODO: confirm the limit in testing — T-21). Therefore: OpenAI action timeout `PT90S` with 1 retry; and callers that do not need the result (Intake, Regenerate) must have their `Run a Child Flow` action followed by a step that runs after `Succeeded, Failed, TimedOut`. A caller timeout does **not** cancel the child, which keeps updating Monday itself. `mode=MondayText` makes no OpenAI call and returns in seconds.

```
Log create (as above)
Try_Generate [Scope]
  Set_Status_Processing          eda_draft_status=Processing
  Get_Drafts_Item                [HTTP Monday] items(ids:[draftitemid]) { column_values(ids:[eda_message_id, eda_conversation_id,
                                   eda_client_profile, eda_sender_email, eda_draft_text, eda_draft_id, eda_change_key, eda_input_tokens,
                                   eda_output_tokens, eda_gen_count]) { id text value } }
  Get_Mailbox_Settings           (eds_tone, eds_style, eds_other_instr, eds_signoff, max chars for <depth>); model = parameters('rsfa_EDA_OpenAIModel')

  Mode_is_MondayText [Condition]  — used by Approve & send: skip AI, ReplyHtml = Monday text with
        replace(eda_draft_text, decodeUriComponent('%0A'), '<br>')  → jump to Create_Outlook_Draft

  Build context (Compose_* actions, each truncated with substring(x, 0, min(length(x), N))):
   Compose_Context_Email      Get_Incoming_Email (Graph, bodytextonly) → subject, from, receivedDateTime, uniqueBody.content
   Get_Thread                 GET /me/messages?$filter=conversationId eq '<encodeUriComponent(cid)>'
                                  &$select=from,receivedDateTime,sentDateTime,uniqueBody&$top=<5 | Deep:15>
                              (do NOT add $orderby — Graph rejects conversationId filter + orderby; sort in flow:
                               reverse(sort(body?['value'], 'receivedDateTime')) )
   Get_Style_Examples         GET /me/mailFolders/sentitems/messages?$search="recipients:<sender>"&$top=3&$select=sentDateTime,uniqueBody
   Get_Client_Profile         Monday items(ids:[cp]) { name column_values(ids:["lookup_mkypams8","color_mm08t3w8","multiple_person_mm5ky9nz"]) { id text } }
   Depth_Medium_or_Deep [Condition]
     Get_Linked_Business      Monday items(ids:[cp]) { column_values(ids:["board_relation_mkycc37a","board_relation_mkyebcmw",
                                "board_relation_mkyep8n0","board_relation_mkye6rvb","board_relation_mkyeyfwe","board_relation_mkye5k1h",
                                "board_relation_mm6fn506"]) { ... on BoardRelationValue { linked_items { name board { name } group { title } } } } } }
     Get_Timeline             last 10 timeline items of the Client Profile — TODO: confirm GraphQL shape in the Monday API playground
                              (title + summary only, never full content)
   Depth_Deep [Condition]
     Get_Client_Folder        SharePoint Get files (properties only) — same dataset/table as Main's Get_Client_Folder
                              (site RealSavvyClients, library 021a912a-571a-43ab-8575-5f9326ae8bfb, filter substringof(<cp>, FileLeafRef))
     List_Recent_Files        Get files (properties only), Limit to folder = client folder path, Include nested = Yes,
                              Order by 'Modified desc', Top 20 → Select FileLeafRef, Modified  (names/dates only)
   Compose_User_Context       '<client_profile>…</client_profile><linked_business>…</linked_business><timeline>…</timeline>
                               <sharepoint_files>…</sharepoint_files><thread>…</thread><style_examples>…</style_examples>
                               <incoming_email>…</incoming_email>'   then truncate to max chars for depth (oldest thread content cut first)

  Call_OpenAI_Responses          [HTTP] POST https://api.openai.com/v1/responses   (Secure in/out ON, timeout PT90S, retry fixed 1)
     body:
     {
       "model": "@{parameters('rsfa_EDA_OpenAIModel')}",
       "max_output_tokens": 1500,
       "input": [
         {"role":"system","content":[{"type":"input_text","text":"<FIXED SAFETY PROMPT — AUTO-EMAIL-DRAFT-001 §14.2 item 1>"}]},
         {"role":"developer","content":[{"type":"input_text","text":"Tone: …\nStyle: …\nOther instructions: …\nDo NOT write a sign-off, name or signature — it is added automatically.\n<adviser_instructions_for_this_email>…eda_ai_instructions (Regenerate only)…</adviser_instructions_for_this_email>"}]},
         {"role":"user","content":[{"type":"input_text","text":"<Compose_User_Context>"}]}
       ],
       "text": {"format": {"type":"json_schema","name":"eda_reply","strict":true,"schema": <schema below>}}
     }
  Filter_Output_Message          Filter array body('Call_OpenAI_Responses')?['output'] where item()?['type'] == 'message'
  Compose_AI_Text                first(body('Filter_Output_Message'))?['content']?[0]?['text']
                                 (do not use output[0] as the TXT/PDF renaming actions do — reasoning models put a 'reasoning' item first)
  Parse_AI_JSON                  [Parse JSON] with the schema below → on failure → Catch (Failed – invalid AI output)
  Validate_AI_Output [Condition]  needs_reply=true requires length(reply_html) > 0 and no '<script', '<iframe', '<img' (toLower contains)
  Needs_Reply [Condition]
     False → status 'No draft', eda_reason 'No reply needed', group group_mm8s3hhz, tokens/model/category written → Respond
     True  → Create_Outlook_Draft

  Create_Outlook_Draft:
     Create_Reply             [Graph] POST /me/messages/<eda_message_id>/createReplyAll, body {}   (always Reply all)
     Compose_Draft_Body_Html  concat(<reply_html>, '<br>', <eds_signoff>, '<br>', body('Create_Reply')?['body']?['content'])   (signature always appended; keeps the quoted thread)
     Patch_Draft              [Graph] PATCH /me/messages/<new draft id>
          {"body":{"contentType":"HTML","content":"<Compose_Draft_Body_Html>"},
           "categories":["AI Draft"]  (or ["AI Draft – Review carefully"] when risk_flags not empty),
           "singleValueExtendedProperties":[{"id":"<rsfa_EDA_ExtPropId>","value":"<draftitemid>"}]}
     Previous_Draft_Exists [Condition] eda_draft_id not empty (Regenerate / MondayText):
          Get previous draft changeKey → if unchanged → DELETE previous draft; if changed → do not delete, set status 'Needs attention' + reason 'Edited in Outlook - finish there, or Discard / Regenerate' and stop
          (check BEFORE Create_Reply so no orphan draft is produced)
     Update_Drafts_Item       eda_draft_status='Ready for review', eda_reason ('' / 'Regenerated with adviser instructions' / 'Regenerated'), group 'topics', eda_draft_link={url: webLink, text:'Open draft'},
                              eda_draft_text=<html-to-text of reply_html (Content Conversion › Html to text)>, eda_missing_info, eda_adviser_notes,
                              eda_risk_flag (None | Review carefully), eda_confidence, eda_model = '<model> · <depth>',
                              eda_input_tokens += usage.input_tokens, eda_output_tokens += usage.output_tokens, eda_gen_count += 1,
                              eda_draft_created=now NZT, eda_draft_id=<patched id>, eda_change_key=<patched changeKey>
Catch_Generate [Scope]
  If a new draft id was created but Update_Drafts_Item failed → DELETE that draft id (compensation, only the id this run created)
  status='Needs attention', eda_reason ('AI unavailable - use Regenerate' if OpenAI status 429/5xx or timeout, 'Invalid AI output - use Regenerate', else 'Generate error')
  Log Failed + 'Email Drafting Agent Failure' email (run URL + item link only)
```

AI output JSON schema (strict mode requires every property in `required` and `additionalProperties:false`):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["needs_reply","risk_flags","reply_html","missing_information","notes_for_adviser","confidence"],
  "properties": {
    "needs_reply": {"type":"boolean"},
    "risk_flags": {"type":"array","items":{"type":"string","enum":["complaint","hardship","claim","cancellation","legal","vulnerable_client","advice_request"]}},
    "reply_html": {"type":"string"},
    "missing_information": {"type":"array","items":{"type":"string"}},
    "notes_for_adviser": {"type":"string"},
    "confidence": {"type":"string","enum":["low","medium","high"]}
  }
}
```

The `confidence` enum values are identical to the status labels on the Drafts board, so they can be written as `{"label": "<value>"}` directly. `notes_for_adviser` must also list CC recipients when present (instruction in the system prompt). `reply_category` was removed on 2026-11-04 together with its board column.

---

### 3.3 `Monday - Email Drafting Agent - Adviser Action Handler`

Trigger: **When an HTTP request is received** (method POST). Settings → Concurrency control **On, degree 1** (serialises actions; prevents double sends).

```
Is_Monday_Challenge [Condition] contains(string(triggerBody()), 'challenge')
   True → Response 200 body {"challenge": "@{triggerBody()?['challenge']}"} → Terminate Succeeded
Compose_Event       triggerBody()?['event']   → boardId, pulseId, columnId, userId, value.label.text
Is_Expected_Event   boardId == rsfa_EDA_DraftsBoardId AND columnId == 'eda_adviser_action' AND label not empty
   False → Response 200 → Terminate
Response_200        (answer Monday quickly, then continue)
Get_Drafts_Item     (re-read from Monday — never trust payload values)
Get_Mailbox_Settings (allowed approvers)
Is_Busy             eda_draft_status == 'Processing' → reset action, Terminate
Switch_Adviser_Action on label:
  'Approve & send':
     Is_Allowed_Approver   userId ∈ eds_approvers person ids            else → reset action + eda_reason 'Not an allowed approver'
     Status_Allows_Send    status == 'Ready for review'
     Get_Draft             [Graph] GET /me/messages/<eda_draft_id>?$select=id,changeKey,isDraft,parentFolderId
     Draft_Unchanged       statuscode 200 AND isDraft AND changeKey == eda_change_key   else → status 'Needs attention' + reason 'Edited in Outlook - finish there, or Discard / Regenerate'
     Rebuild_From_Monday   Run Child Generate Draft (mode=MondayText) — ALWAYS, so what is sent is exactly the
                           current Monday `Draft Text` (safe because the changeKey check proved there are no Outlook edits);
                           then re-read the item (new eda_draft_id / eda_change_key)
     Send_Draft            [Graph] POST /me/messages/<new draft id>/send   (expects 202)
     Update                status 'Sent from Monday', eda_reason '', eda_final_status_at, eda_actioned_by=userId, group Done
  'Regenerate':
     status ∉ {Sent from Outlook, Sent from Monday, Discarded} → Run Child Generate Draft (mode=Regenerate, depth=Medium; uses eda_ai_instructions)
     (also allowed on 'No draft', e.g. daily cap reached or a 'No reply needed' the adviser disagrees with)
  'Discard':
     status not Sent → [Graph] DELETE /me/messages/<eda_draft_id> (404 = already gone, treat as success)
     status 'Discarded', eda_reason 'Discarded from Monday', eda_final_status_at, eda_actioned_by, group Done
Finally (runAfter all): Reset_Adviser_Action  change_multiple_column_values eda_adviser_action = null ("{\"eda_adviser_action\":null}"),
                         eda_last_run=<run url>
```

Monday user ID → people column value: `{"personsAndTeams":[{"id":<userId>,"kind":"person"}]}`.

---

### 3.4 `Scheduled - Email Drafting Agent - Draft Reconciliation`

Trigger: Recurrence, every 30 minutes, time zone `New Zealand Standard Time`, hours 7–20.

```
Get_Open_Draft_Items  Monday items_page rules eda_draft_status any_of [Ready for review, Needs attention] (limit 200)
Get_Deleted_Items_Folder_Id per mailbox  [Graph] GET /me/mailFolders/deleteditems?$select=id
Apply_to_each (concurrency 1):
  Get_Draft  [Graph] GET /me/messages/<eda_draft_id>?$select=id,changeKey,isDraft,parentFolderId,createdDateTime
  404 OR parentFolderId == DeletedItems id  → (Sent Items Sync may have already handled it) re-read status; if still open →
        status 'Discarded', eda_reason 'Deleted in Outlook', eda_final_status_at, group Done
  200 AND changeKey ≠ eda_change_key       → write nothing. Do NOT overwrite eda_change_key:
                                              it is the last version written by the agent, and Monday actions use the
                                              mismatch to return Needs attention instead of overwriting the adviser's Outlook edits.
```

`isDraft = false` on a message that still resolves means it was sent between runs — leave it for Sent Items Sync.

---

### 3.5 `Outlook - Email Drafting Agent - Sent Items Sync - Rod`

Trigger: **When a new email arrives (V3)**, connection `EDA_Outlook_Rod_RSFA`, Folder **Sent Items**, Include attachments **No**.
(Same folder as `Outlook SENT Email Filling - Rod v2`; two independent triggers on one folder are fine.)

```
Has_AI_Draft_Category  [Condition] contains(string(triggerOutputs()?['body/categories']), 'AI Draft')
   False → Terminate Succeeded   (keeps run volume low; TODO verify in T-12 that categories survive on the Sent copy,
                                  otherwise remove this filter and rely on the extended property only)
Get_Sent_Message  [Graph] GET /me/messages/<id>?$select=id,conversationId,sentDateTime,uniqueBody
                    &$expand=singleValueExtendedProperties($filter=id eq '<rsfa_EDA_ExtPropId>')   (bodytextonly=true)
Compose_Draft_Item_Id   first(body?['singleValueExtendedProperties'])?['value']
Fallback (empty id): Monday items_page eda_conversation_id = conversationId AND status ∈ open → newest item
Get_Drafts_Item → Already_Sent [Condition] status ∈ {Sent from Outlook, Sent from Monday} → Terminate (idempotent with Monday send)
Compare_Text  normalised(uniqueBody.content minus Html-to-text(eds_signoff)) vs normalised(eda_draft_text)
   normalise = toLower + replace CR, LF, tab, non-breaking space and spaces with ''
Update  status 'Sent from Outlook', eda_reason 'No edits' / 'Edited before sending', eda_final_status_at, group Done
```

Additional mailbox later = duplicate this flow with that mailbox's connection (`… - Sent Items Sync - Kathleen`).

### 3.6 `Manual - Email Drafting Agent - Test Harness`

Manual trigger with inputs `mailbox` (default `tech@rsfa.co.nz`), `messageid`, `clientprofileid` → `Run a Child Flow` Intake (`advisername` = `Test`). Used for Phase 0 with a fictional Client Profile so `Main` and the Rod flow are not involved. Turn **off** after go-live.

---

## 4. Order of work

1. §0 prerequisites (secrets, backup, Solution, connection references, env vars, Runs dropdown label).
2. Build 3.0 → 3.1 → 3.2 → 3.6. Test T-01, T-05…T-10, T-17…T-20, T-22…T-24 on `tech@` via the harness.
3. Build 3.3 + webhook (§5) → T-14…T-16. Build 3.5 for tech (temporary `… - Sent Items Sync - Tech`) + 3.4 → T-11…T-13.
4. Change A in `Main` → T-02 regression on live traffic for 1 working day (drafting not yet connected).
5. Change B in `Rod v2` with Rod's settings item still `Enabled = No` → confirm `Try_Run_Email_Drafting_Agent` runs and Intake exits "mailbox disabled".
6. Rod approval of D1–D5, fill Tone/Style/Other Instructions and paste Rod's **Email Signature (HTML)** → set `Enabled = Yes` (Phase 1, Basic, cap 20).

## 5. Monday webhook (after 3.3 is saved)

1. Copy the HTTP POST URL of flow 3.3 and store it in 1Password (item name TODO — e.g. `PA - Email Drafting Agent - Monday webhook URL`).
2. Create the webhook, either in Monday (*Integrate → Webhooks → "When a column changes, send a webhook"*, column **Adviser Action**) or via API:
   `mutation { create_webhook(board_id: 5032291843, url: "<URL>", event: change_specific_column_value, config: "{\"columnId\":\"eda_adviser_action\"}") { id } }`
3. Monday sends a `challenge` first — flow 3.3 echoes it (§3.3). Record the webhook ID in `BOARD-EMAIL-DRAFTS-001`.

## 6. Monday boards created (2026-11-04, via Monday MCP)

See `knowledge/schemas/monday/BOARD-EMAIL-DRAFTS-001-email-drafting-agent-boards.md` for full column lists with IDs.

| Board | ID | Folder | Kind |
|---|---|---|---|
| ✉️ Email Drafting Agent: Drafts | `5032291843` | Daily Boards/Ops (`6649274`), workspace Real Savvy_CRM | private |
| ⚙️ Email Drafting Agent: Mailbox Settings | `5032291851` | Daily Boards/Ops (`6649274`), workspace Real Savvy_CRM | private |

Settings items: `rod@rsfa.co.nz` (`2899339258`, **Enabled = No**), `tech@rsfa.co.nz` (`2899339259`, Enabled = Yes, test only).

## 7. Change history

| Date | Change | Author |
|---|---|---|
| 2026-11-04 | Initial build guide based on the 2026-11-04 flow exports supplied in chat. | Claude (requested by Leonardo Melman) |
| 2026-11-04 | Simplified the status model: 6 Draft Status labels + Status Detail text; Research Depth column deleted (depth in Model / Depth); depth selected via `Regenerate - more context` / `Regenerate - deep research`; Stale status removed. | Claude (requested by Leonardo Melman) |
| 2026-11-04 | Second simplification: statuses `Sent from Outlook` / `Sent from Monday` restored; actions reduced to Approve & send / Regenerate / Discard; Regenerate = Medium + `Instructions for AI`; signature appended automatically from `Email Signature (HTML)`; always Reply all; model moved to env var `rsfa_EDA_OpenAIModel`; removed reply_category, edited flags, reply mode, stale. | Claude (requested by Leonardo Melman) |
| 2026-11-04 | `eds_default_depth` (Default Depth) removed from Mailbox Settings by Leonardo Melman: automatic drafts are always **Basic**, Regenerate is always **Medium**; Deep is not used in v1. | Claude (requested by Leonardo Melman) |
