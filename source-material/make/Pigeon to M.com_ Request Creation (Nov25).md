### **📄 Summary of the Automation**

 This automation is triggered when a **new request is created in Pigeon**.

 It creates a new item in the [Monday.com](https://Monday.com) board [**Pigeon Board JV**](https://rsfa-squad.monday.com/boards/5025365499), storing the request details. The scenario first tries to find an existing client using the request email by searching [**Contacts JV :: Public**](https://rsfa-squad.monday.com/boards/5024661649/views/49255949) (first by **primary email**, and if not found, by **AlternativeEmail**). If a match is found, the item is created and the client is assigned in **Client Profiles**; otherwise, the item is created with **Client Profiles left empty**. In both cases, the item is populated with the request name, creation date, and **Banks to Send** (left empty). Finally, since some requests include a **due date** and others don’t, the flow branches into two paths: one updates the due date column and the other skips it.


### **🧭 High-Level Steps**

1.  **Trigger on New Pigeon Request** - Runs when a new request is created in Pigeon.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55895360/image-from-clipboard.png)

2.  **Look Up Client in “**[**Contacts JV :: Public**](https://rsfa-squad.monday.com/boards/5024661649/views/49255949)**”** - Searches the[ ](https://rsfa-squad.monday.com/boards/5024661649/views/49255949)[**Contacts JV :: Public**](https://rsfa-squad.monday.com/boards/5024661649/views/49255949) table to find a client linked to the email used for the Pigeon request.

   -  If no match is found using the **primary email**, the flow retries using **AlternativeEmail**.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55895403/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55895442/image-from-clipboard.png)

3.  **Create Item in “**[**Pigeon Board JV**](https://rsfa-squad.monday.com/boards/5025365499)**”** - Creates a new item in [**Pigeon Board JV**](https://rsfa-squad.monday.com/boards/5025365499) and stores the request details.

   -  If a client was found, it assigns them in the **Client Profiles** column.

   -  If no client was found, the item is created with **Client Profiles** left empty.

   -  In both cases, the flow fills the request **name**, **creation date**, and **Banks to Send** is left empty, since this column is used to manually assign the bank(s) associated with the request. Once it is filled in, it triggers the automation **“**[**M.com: Pigeon Board to Mortgage Pipeline (Nov 25)**](https://eu2.make.com/85772/scenarios/7950443/edit)**”**.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55895793/image-from-clipboard.png)

4.  **Handle Due Date (Conditional Path)** - Splits into two branches depending on whether the Pigeon request includes a due date.

   -  If a due date exists, it is written to the **Due Date** column.

   -  If no due date exists, this step is skipped.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55895921/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55895945/image-from-clipboard.png)

 

## ✅ Conclusion

 This [Make.com](https://Make.com) scenario ensures every new Pigeon request is automatically captured in [Monday.com](https://Monday.com) under [**Pigeon Board JV**](https://rsfa-squad.monday.com/boards/5025365499), with client matching handled via [**Contacts JV :: Public**](https://rsfa-squad.monday.com/boards/5024661649/views/49255949) when possible. By standardizing how request data is stored (and conditionally applying the due date when available).