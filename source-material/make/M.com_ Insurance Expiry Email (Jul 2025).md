### **📄 Summary of the Automation**

 This automation checks the [✔️ Existing Insurance board in Monday](https://rsfa-squad.monday.com/boards/5024672437) and sends reminder emails to clients whose Anniversary-rate insurance is about to expire. It handles two types of notifications: the first one is sent 45 days before the expiry date, and a second reminder is sent 15 days after the first, if the client hasn't responded yet. Notifications are sent via Outlook and updates are logged in Slack and [Monday.com](https://Monday.com).

 Throughout the flow, we repeatedly apply the same formula used in the [✔️ Existing Insurance board in Monday](https://rsfa-squad.monday.com/boards/5024672437) board to calculate the current year’s "**Anniversary Date"** based on the "**Commencement Date"**. This is necessary because the "**Anniversary Date"** field in Monday is a formula column and cannot be extracted directly, so we replicate the calculation within the flow to use it when needed.

### **🧭 High-Level Steps**

1.  **List and pre-filter insurance items** - The flow starts by searching the **Existing Insurance** board and only bringing in the items that could actually need action.

-  Instead of pulling every insurance item and checking everything later, the flow now filters directly in the first search. It only brings in items that have one of these statuses:

-  Renewal Notification Status is either:

   -  5 - Not Contacted

   -  0 - Contacted

 This is very important because these are the only statuses that require action in this flow. Filtering at the search level avoids processing unnecessary items, making the automation lighter, faster, and cheaper to run.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71555933/image-from-clipboard.png)

 ⚠️ **Important note about Monday status indexes**

 This first filter depends on the internal position/index of the statuses in Monday.

 The flow currently uses these Monday status indexes:

-  5 = Not Contacted

-  0 = Contacted

 These indexes must not be changed in the **Renewal Notification Status** column of the **Existing Insurance** board. If someone changes the order of the labels in Monday, the indexes may change as well, and the flow may stop finding the correct items or may bring in the wrong ones.

 

-  After this first filter, the flow calculates the correct upcoming **Anniversary Date** for each item.

-  The anniversary date is calculated from the original **Commencement Date**:

   -  If the commencement date converted to the current year has not passed yet => use the anniversary date in the current year

   -  If the commencement date converted to the current year has already passed => use the anniversary date in the next year

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71555984/image-from-clipboard.png)

 Then the flow checks whether the item actually needs to be updated:

-  If the item is currently Not Contacted and the Anniversary Date is between 23 and 45 days away => the item should move to Contacted

-  If the item is currently Contacted and the Reminder Date was more than 15 days ago => the item should move to Reminder Sent

-  If neither condition applies => no action is taken

 Only items with a valid calculated status continue into the rest of the flow.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71556113/image-from-clipboard.png)

 From there, the automation continues into three main parts.

 

3.  **Complete HTML Table**

-  In this part of the flow, we build the table that will later be inserted into the email.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71556170/image-from-clipboard.png)

-  The table is created using all mortgage items with the same name in the [✔️ Existing Insurance board in Monday](https://rsfa-squad.monday.com/boards/5024672437). In other words, if the same client has more than one mortgage item, all relevant items are grouped together in the same email table.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71556620/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71556680/image-from-clipboard.png)

-  For each mortgage item, the table includes:

   -  Insurance Provider

   -  Anniversary Date

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

   -  Insruance Provider

   -  Adviser

   -  RawEmails

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71557189/image-from-clipboard.png)

 

4.  **Get HTML, Send the Email, and Update the Status**

-  In this final part of the flow, the automation gets the correct HTML template, sends the email, notifies the team in Slack, and updates the mortgage item in the [✔️ Existing Insurance board in Monday](https://rsfa-squad.monday.com/boards/5024672437).

-  The correct HTML is selected based on the adviser combination in the **Automation** column of the mortgage item.

-  To do this, the flow searches the [✉️ Email Campaigns Templates board](https://rsfa-squad.monday.com/boards/5027616908/views/52349195). It looks for templates where:

   -  Email Campaign = Insurance Renewal

   -  At least one of the advisers from the insurance item

   -  The correct JV/Referral Source group:

      -  If the item’s JV/Referral Source is TOG => search for TOG

      -  If the item’s JV/Referral Source is Key Mortgages => search for Key Mortgages

      -  If the item’s JV/Referral Source is neither TOG nor Key Mortgages => search for Other

   -  After that, the flow checks the exact adviser combination to make sure it uses the correct template.

-  If the flow cannot find the required adviser combination, it stops that route and sends an error notification to: [tech@rsfa.co.nz](mailto:tech@rsfa.co.nz)

   -  This lets the team know that a new adviser combination and HTML template need to be added.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71557937/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71558019/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71558131/image-from-clipboard.png)

 ⚠️ **Important:** this search also depends on Monday status/index values. The index for **Insurance Renewal and the JV/Referral Source names** must not be changed in the [✉️ Email Campaigns Templates board](https://rsfa-squad.monday.com/boards/5027616908/views/52349195) column. If the order of the dropdown labels changes, the flow may not find the correct templates and could behave incorrectly.

 

 **Email Design**

-  The HTML file is taken from the **HTML template** column.

-  The same board also has a column called **.eml Examples (Only Visual)**. These files are only examples. They can be downloaded and opened to preview how the email should look when the HTML is sent with the correct data.

   -  This is useful when reviewing or requesting design changes, but these `.eml` files are **not used by the flow**.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71558282/image-from-clipboard.png)

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

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71558348/image-from-clipboard.png)

-  **What happens if I want to upload a new HTML design?**

-  If you want to upload a new HTML design, it is very important to follow the variable rules explained above.

   -  The HTML must keep the exact same variable names, including:

      -  %URLClientNames%

      -  %LoansTable%

      -  %ClientNames%

      -  %BannerByStatus%

   -  These names must be written exactly as shown, including uppercase letters, lowercase letters, spaces if applicable, and the `%` symbols at the beginning and end.

   -  If any of these variables are changed, misspelled, or removed, the flow will not be able to replace them correctly and the email may not work as expected.

-  ⚠️ **Important: **Please note that the HTML templates for TOG, Key Mortgages, and Other are different.

   -  For that reason, make sure to use the correct HTML template according to both:

      -  - the JV/Referral Source group: TOG, Key Mortgages, or Other

      -  - the related adviser combination

-  To upload a new HTML design:

   -  1. Open the Email Campaigns Templates board.

   -  2. Find the item that belongs to the **adviser** combination and **JV/Referral Source** you want to update.

   -  3. Go to the HTML template column.

   -  4. Delete the current HTML file.

   -  5. Upload the new HTML file.

-  You can either modify the existing HTML and upload the updated version, or upload a completely new HTML file. In both cases, the required variables must be placed in the correct parts of the HTML.

-  If a new HTML design is uploaded, please notify the team so the visual `.eml` example can also be updated manually.

-  The `.eml Examples (Only Visual)` file does **not** update automatically when the HTML template is changed. It is only a visual reference, so if the HTML design changes, the `.eml` example should be recreated and uploaded manually to keep the preview aligned with the real template.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71551775/image-from-clipboard.png)

-  After the email is sent, the flow sends a Slack notification in the channel e_insurance_all_automations with the relevant information, including:

   -  Status

   -  Client name

   -  Email

   -  Anniversary Date

   -  Insurance Provider

 This is how the notification looks like in slack:

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71551553/image.png)

-  Finally, the flow updates the mortgage item in the [✔️ Existing Insurance board in Monday](https://rsfa-squad.monday.com/boards/5024672437) by:

   -  Updating the Renewal Notification Status to the correct new status

   -  Updating the Reminder Date to today’s date

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/71558992/image-from-clipboard.png)

 

 

 

 This is how the email looks like:

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/36296541/image.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/36296543/image%20%281%29.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/36296553/image%20%282%29.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/36296555/image%20%283%29.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/36296556/image%20%284%29.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/36296558/image%20%285%29.png)

 This is the example for every HTML from the email:

### ✅ **Conclusion**

 This [Make.com](https://Make.com) scenario ensures that insurance clients are notified in a timely and automated way about upcoming fixed-rate expirations. By combining data from [Monday.com](https://Monday.com), automated emails via Outlook, and Slack updates, it keeps both clients and internal teams informed. To reuse this flow with another board or mailbox, the user would only need to adjust the board ID, status values, and sender email.