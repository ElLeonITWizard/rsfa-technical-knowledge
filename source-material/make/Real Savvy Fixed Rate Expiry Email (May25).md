### **📄 Summary of the Automation**

 This automation checks the [✅️ Existing Mortgages Monday.com board](https://rsfa-squad.monday.com/boards/5024672364) and sends reminder emails to clients whose fixed-rate mortgage is about to expire. It handles two types of notifications: the first one is sent 90 days before the expiry date, and a second reminder is sent three weeks after the first, if the client hasn't responded yet. Notifications are sent via Outlook and updates are logged in Slack and [Monday.com](https://rsfa-squad.monday.com/boards/5024672364).

 

### **🧭 High-Level Steps**

1.  **List and pre-filter mortgage items** - The flow starts by looking at the **Existing Mortgages** board and only bringing in the items that could actually need action.

   -  Instead of pulling every mortgage and checking them one by one later, the flow now filters directly in the first search. It only brings in mortgages that:

 Have a fixed-rate expiry date within the next 90 days AND Have one of these statuses:

 - Not Contacted

 - Contacted

 This is very important because it avoids processing unnecessary items. It makes the flow lighter, faster, and cheaper to run because it uses fewer steps and fewer operations.


 


![Image: This is the filter setup.](https://rsfa-squad.monday.com/protected_static/18150562/resources/71548262/image-from-clipboard.png)

![Image: These are the statuses used in the ✅️ Existing Mortgages board inMonday.com](https://rsfa-squad.monday.com/protected_static/18150562/resources/71548367/image-from-clipboard.png)

 ⚠️ **Important note about Monday status indexes**

 This first filter depends on the internal position/index of the statuses in Monday:

 1 = Not Contacted

 5 = Contacted

 These indexes must not be changed in the **Renewal Notification Status** column. If the order of the dropdown labels changes in Monday, the indexes may change as well, and the flow may retrieve the wrong items or stop retrieving the correct ones.

 

2.  After this initial pre-filter, the flow still needs a conditional step to decide whether each item actually requires a first contact or a reminder. The initial search only reduces the candidate list; it does not fully determine the final action.

 The status logic is:

-  If the item is currently Not Contacted and the fixed-rate expiry date is between 68 and 90 days away

 => the item should move to Contacted

 

-  If the item is currently Contacted and the reminder date was more than 21 days ago

 => the item should move to Reminder Sent

 

-  If neither condition applies

 => no action is taken

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71550409/image-from-clipboard.png)

 Only items that need a status update continue into the rest of the flow.

 From there, the automation continues into three main parts.

 

3.  **Complete HTML Table**

-  In this part of the flow, we build the table that will later be inserted into the email.

![Image: This is how it looks in the email](https://rsfa-squad.monday.com/protected_static/18150562/resources/71550606/image-from-clipboard.png)

-  The table is created using all mortgage items with the same name in the [✅️ Existing Mortgages board in](https://rsfa-squad.monday.com/boards/5024672364)[ ](https://rsfa-squad.monday.com/boards/5024672364)[Monday.com](https://rsfa-squad.monday.com/boards/5024672364). In other words, if the same client has more than one mortgage item, all relevant items are grouped together in the same email table.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71550680/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71550595/image-from-clipboard.png)

-  For each mortgage item, the table includes:

   -  Lender

   -  Loan Amount

   -  Expiry Date

-  The **Loan Amount** is taken from the **Current Loan ($)** column. If that field is empty, the flow uses the **Original Loan ($)** column instead.

-  The table only includes mortgage items that have not already expired.

 

3.  **Get All Information for the Email:**

-  In this part of the flow, we collect and prepare the main information that will be used in the email.

-  First, the flow searches the [**Contacts**](https://rsfa-squad.monday.com/boards/2074688484)[ ](https://rsfa-squad.monday.com/boards/2074688484)board using the [**Client Profile**](https://rsfa-squad.monday.com/boards/5024661649) linked to the mortgage item that needs to be notified. From those related contacts, the flow extracts the email addresses where the notification should be sent.

-  If a contact does not have a **Primary Email**, the flow sends a Slack notification so the missing email can be added as soon as possible. This allows the contact to be included in future executions of the flow.

-  Using the same contacts, the flow also retrieves the clients’ **Preferred Names**, so the email greeting can be more personal and accurate.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71550888/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71550788/image-from-clipboard.png)

-  Finally, the flow prepares and cleans the main variables needed for the email:

   -  Client Emails

   -  Clients Preferred Names

   -  Client Names

   -  Bank

   -  FX Date

   -  Loan

   -  Adviser

   -  RawEmails

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71550821/image-from-clipboard.png)

 

4.  **Get HTML, Send the Email, and Update the Status**

-  In this final part of the flow, the automation gets the correct HTML template, sends the email, notifies the team in Slack, and updates the mortgage item in the [✅️ Existing Mortgages board in ](https://rsfa-squad.monday.com/boards/5024672364)[M](https://rsfa-squad.monday.com/boards/5024672364)[onday](https://rsfa-squad.monday.com/boards/5024672364).

-  The correct HTML is selected based on the adviser combination in the **Automation** column of the mortgage item.

-  To do this, the flow searches the [✉️ Email Campaigns Templates board](https://rsfa-squad.monday.com/boards/5027616908/views/52349195). It looks for templates where:

   -  Email Campaign = Fixed Rate Expiry AND Related Adviser contains one of the advisers from the mortgage item

   -  After that, the flow checks the exact adviser combination to make sure it uses the correct template.

-  If the flow cannot find the required adviser combination, it stops that route and sends an error notification to: [tech@rsfa.co.nz](mailto:tech@rsfa.co.nz)

   -  This lets the team know that a new adviser combination and HTML template need to be added.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71551477/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71551460/image-from-clipboard.png)

 ⚠️ **Important:** this search also depends on Monday status/index values. The index for **Fixed Rate Expiry** must not be changed in the [✉️ Email Campaigns Templates board](https://rsfa-squad.monday.com/boards/5027616908/views/52349195) column. If the order of the dropdown labels changes, the flow may not find the correct templates and could behave incorrectly.

 

 **Email Design**

-  The HTML file is taken from the **HTML template** column.

-  The same board also has a column called **.eml Examples (Only Visual)**. These files are only examples. They can be downloaded and opened to preview how the email should look when the HTML is sent with the correct data.

   -  This is useful when reviewing or requesting design changes, but these `.eml` files are **not used by the flow**.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71551462/image-from-clipboard.png)

-  Once the correct HTML is found, the flow replaces the variables inside the template. It is very important that these variable names stay exactly the same in every HTML file. If the names are changed, the flow will not replace them correctly.

-  The required HTML variables are:

   -  %URLClientNames%

      -  Used in the unsubscribe link. The link needs the client names to identify who is unsubscribing.

   -  %LoansTable%

      -  Replaced with the table containing the client’s mortgage details.

   -  %ClientNames%

      -  Replaced with the client names used in the email greeting/body.

   -  %BannerByStatus%

      -  Replaced with the correct banner depending on whether the email is the first notification or the second reminder.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71551456/image-from-clipboard.png)

-  **What happens if I want to upload a new HTML design?**

-  If you want to upload a new HTML design, it is very important to follow the variable rules explained above.

   -  The HTML must keep the exact same variable names, including:

      -  %URLClientNames%

      -  %LoansTable%

      -  %ClientNames%

      -  %BannerByStatus%

   -  These names must be written exactly as shown, including uppercase letters, lowercase letters, spaces if applicable, and the `%` symbols at the beginning and end.

   -  If any of these variables are changed, misspelled, or removed, the flow will not be able to replace them correctly and the email may not work as expected.

-  To upload a new HTML design:

   -  1. Open the Email Campaigns Templates board.

   -  2. Find the item that belongs to the adviser combination you want to update.

   -  3. Go to the HTML template column.

   -  4. Delete the current HTML file.

   -  5. Upload the new HTML file.

-  You can either modify the existing HTML and upload the updated version, or upload a completely new HTML file. In both cases, the required variables must be placed in the correct parts of the HTML.

-  If a new HTML design is uploaded, please notify the team so the visual `.eml` example can also be updated manually.

-  The `.eml Examples (Only Visual)` file does **not** update automatically when the HTML template is changed. It is only a visual reference, so if the HTML design changes, the `.eml` example should be recreated and uploaded manually to keep the preview aligned with the real template.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71551775/image-from-clipboard.png)

-  After the email is sent, the flow sends a Slack notification in the channel e_mortgage_all_automations with the relevant information, including:

   -  Status

   -  Client name

   -  Email

   -  Bank

   -  Fixed expiry date

   -  Loan amount

 This is how the notification looks like in slack:

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71551553/image.png)

-  Finally, the flow updates the mortgage item in the **Existing Mortgages** board by:

   -  Updating the Renewal Notification Status to the correct new status

   -  Updating the Reminder Date to today’s date

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71551596/image-from-clipboard.png)

 

 This is how the email looks like:

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/34910324/large-image%20%289%29.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/34910361/large-image%20%2810%29.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/34910390/large-image%20%2811%29.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/34910402/large-image%20%2812%29.png)

 This is the example HTML from the email:

### ✅ **Conclusion**

 This [Make.com](https://Make.com) scenario ensures that mortgage clients are notified in a timely and automated way about upcoming fixed-rate expirations. By combining data from [Monday.com](https://Monday.com), automated emails via Outlook, and Slack updates, it keeps both clients and internal teams informed. To reuse this flow with another board or mailbox, the user would only need to adjust the board ID, status values, and sender email.