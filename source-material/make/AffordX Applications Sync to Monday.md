# **📄 Summary of the Automation**

 This [Make.com](https://Make.com) scenario keeps the **AffordX Submissions** board in [Monday.com](https://Monday.com) in sync with applications stored in **AffordX**. It runs **daily**, fetches all applications from AffordX, and **creates or updates** a parent item per application. For each application, the flow also pulls **active loans** from **Accounts → Loans** in AffordX and represents them as **subitems** under the parent item in [Monday.com](https://Monday.com).

 

 Data on the **parent item** comes from **Application Summary** (e.g., Application Date, Applicants/Account Holders, Application Status). Data on **subitems** comes from the **Loan** records (e.g., Account/Loan No., Account Holders, Product Name, Repayment Next Amount, Repayment Next Date).

 

> Planned enhancement:
>  Applicants will later be linked to the existing 
> Contacts
>  board in Monday CRM so the related person appears in the 
> Contacts
>  column in 
> AffordX Submissions
> .

 

 

# **🧭 High-Level Steps**

1.  **Authenticate to AffordX API: **Securely obtain an access token and set request headers for subsequent calls.

2.  **List Applications (AffordX): **Retrieve the set of applications to process. (The scenario is scheduled daily; pagination is handled where applicable.)

3.  **Upsert Parent Items (**[**Monday.com**](https://Monday.com)**)**

   -  **De-duplication key:** the **AffordX Application ID**.

   -  If an application **doesn’t exist** in Monday, **create** the parent item.

   -  If it **exists**, **update** the mapped fields when values changed (e.g., Status, Application Date, Applicants).

1.  **Fetch Application Details (AffordX): **For each application being processed, request **Application Summary** details used to fill or refresh the parent item in Monday.

2.  **Create/Update Parent Item (**[**Monday.com**](https://Monday.com)**): **Map fields from **Application Summary** into columns on the parent item (see “Data Mapping” below).

3.  **Fetch Active Loans (AffordX → Accounts → Loans): **Retrieve all **active** loans associated with the application.

4.  **Upsert Subitems per Loan (**[**Monday.com**](https://Monday.com)**)**

   -  **De-duplication key:** the **Loan/Account ID**.

-  For each loan:

      -  If the subitem **doesn’t exist**, **create** it under the application’s parent item.

   -  If it **exists**, **update** the mapped loan fields (e.g., Product Name, Repayment Next Amount/Date).

# **🗂️ Data Model in **[**Monday.com**](https://Monday.com)

## Parent item (one per application)

 **Source:** AffordX → _Application Summary_

  **Typical columns (examples):**

 

-  **Application ID** (Text) – from AffordX (used for de-duplication)

-  **Application Date** (Date)

-  **Applicants / Account Holders** (Text for now; will link to **Contacts** in a later iteration)

-  **Application Status** (Status/Text)

-  **AffordX Link** (Link) – optional, quick access back to AffordX

-  **Last Synced At** (Date/Time) – optional audit trail

## 

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/39474082/Application%20Summarty.png)

 

## Subitems (one per active loan)

 **Source:** AffordX → _Accounts → Loans_

  Each **active loan** inside an application is represented as a **subitem** in [Monday.com](https://Monday.com).

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/39474060/Example_Item_01.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/39474061/Example_Item_02.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/39474063/Example_Item_03.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/39474065/Example_Item_04.png)

### 
Columns:

-  **Loan / Account No.** (Text) – e.g., `88705507-1003`

-  **Account Holders** (Text) – e.g., _MRS DELEN FRANCISCA CRISP_

-  **Product Name** (Text) – e.g., _Home Loan_

-  **Repayment Frequency** (Dropdown / Status) – e.g., _Monthly_

-  **Repayment Next Amount** (Number / Currency) – e.g., `$1,550.14`

-  **Repayment Next Date** (Date) – e.g., `29 Mar`

-  **Interest Type & Rate** (Text) – e.g., _FIXED 5.75_

-  **Interest Expiry Date** (Date) – e.g., `29 Nov` / `27 Feb, 2026`

-  **Is Interest Only** (Dropdown Yes/No) – e.g., _No_

-  **Interest Only Expiry Date** (Date) – e.g., `29 Nov, 2021`

-  **Original Drawdown Date** (Date) – e.g., `27 Aug, 2022`

-  **Initial Principal** (Number / Currency) – e.g., `$254,167.06`

-  **Total Year Term** (Text / Number) – e.g., `27 years`

-  **Remaining Time** (Text) – e.g., `23 years 8 months`

-  **Maturity Date** (Date) – e.g., `29 Nov, 2048`

> These columns mirror the screenshoted structure: parent application at the top; 
> multiple active loans as subitems
>  with repayment details underneath.

 

 

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/39474075/AffordX%20Accounts%20Loan.png)

 

# **🔁 Run Cadence & Idempotency**

-  **Schedule:** Daily at 8AM (time configurable in Make).

-  **Idempotency:**

   -  Parent items keyed by **Application ID**.

   -  Subitems keyed by **Loan/Account ID**.

   -  Existing records are **updated**, not duplicated.

# ⚙️ **Configuration**

-  [**Make.com**](https://Make.com)** Connections:**

   -  **HTTP / AffordX API** (base URL + auth)

   -  [**Monday.com**](https://Monday.com) (Board ID: _AffordX Submissions_)

-  **Secrets:** AffordX credentials and Monday API token stored in Make’s connection vault.

-  **Board/Column IDs:** Stored as scenario variables; adjust if the board is cloned or field names change.

# **🔮 Next Steps (Roadmap)**

1.  **Contacts linkage:** Link records in the Contacts board with the linked Application's clients from AffordX.

2.  **Closed loans handling:** Optionally archive or flag subitems when a loan becomes inactive in AffordX.

3.  **Notifications:** (Optional) Post a Slack message when **new applications** arrive or when key statuses change.

# **✅ Conclusion**

 This scenario provides a reliable, daily synchronization from **AffordX** into [**Monday.com**](https://Monday.com), organizing each **application** as a parent item and each **active loan** as a **subitem** with repayment details. It ensures RSFA has an up-to-date operational view without manual re-entry. To reuse or extend the flow, update the board/column IDs and (optionally) enable the planned **Contacts** linkage and change-only processing.