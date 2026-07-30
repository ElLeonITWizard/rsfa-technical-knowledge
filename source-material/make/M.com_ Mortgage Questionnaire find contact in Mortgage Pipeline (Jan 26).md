## 📄 **Summary of the Automation**

 This automation is triggered when a **Super Form** is completed in [**✍ Mortgage App**](https://rsfa-squad.monday.com/boards/5025483251)[.](https://rsfa-squad.monday.com/boards/5025483251)

 Its purpose is to identify whether each applicant already has a related contact or existing record in the system, and then either update the existing information or create a new item in [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) with as much information as possible from the Super Form.

 The automation first checks for a related contact in the [**Contacts**](https://rsfa-squad.monday.com/boards/2074688484) board. If a match is found, it updates that contact with all available information. Then searches  [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805)  using the applicant’s email addresses in a fallback sequence. If no match is found after all relevant checks, it creates a new item in  [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) , sends a notification email to **support@rsfa.co.nz**, and performs an additional step to add and then remove default values required by [Monday.com](https://Monday.com) for this creation flow.

## 🧭 **High-Level Steps**

1.  **Trigger on Mortgage App Super Form Completion** – Runs when a **Super Form** is completed in [**✍ Mortgage App**](https://rsfa-squad.monday.com/boards/5025483251)[.](https://rsfa-squad.monday.com/boards/5025483251)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66349333/image-from-clipboard.png)

2.  **Check for an Existing Related Contact** – For each applicant, checks whether there is already a related contact in the **Contacts** board.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66349429/image-from-clipboard.png)

3.  **Update Contact if Found** – If a related contact is found, updates it with as much information as possible from the Super Form.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66349493/image-from-clipboard.png)

4.  **Search **[**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805)** by Primary Email if No Contact Is Found** – Searches  [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) using the applicant’s **Primary Email**.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66349641/image-from-clipboard.png)

6.  **Update Existing **[**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805)** Item if Found by Primary Email** – If a matching item is found in [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) using the **Primary Email**, updates it with as much information as possible from the Super Form. And then send a report to [support@rsfa.co.nz.](mailto:support@rsfa.co.nz.)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66349720/image-from-clipboard.png)

7.  **Create New **[**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805)** Item if No Email Match Is Found and No Alternative Email Exists** – If no match is found by **Primary Email** and the applicant does not have an alternative email, creates a new item in [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) with all available information.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66349844/image-from-clipboard.png)

8.  **Send Support Notification for New Item Creation** – When a new item is created in [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805), sends an email notification to **support@rsfa.co.nz** to advise that a new item has been added.

-  **Add and Remove Default Values Required by **[**Monday.com**](https://Monday.com) – For newly created items, temporarily 		adds and then removes default values required by [Monday.com](https://Monday.com) for this creation process to work correctly.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66349940/image-from-clipboard.png)

9.  **Search **[**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805)** by Alternative Email if Primary Email Is Not Matched** – If no match is found by **Primary Email** and the applicant has an **Alternative Email**, searches [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) using that email.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66350114/image-from-clipboard.png)

10.  **Update Existing **[**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805)** Item if Found by Alternative Email** – If a matching item is found using the **Alternative Email**, updates it with as much information as possible from the Super Form.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66350304/image-from-clipboard.png)

11.  **Search  **[**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805)** by Second Alternative Email if Needed** – If no match is found by **Alternative Email**, searches ** **[**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) using the **Second Alternative Email**, if available.

-  **Update Existing  **[**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805)** Item if Found by Second Alternative Email** – If a matching item is found using the **Second Alternative Email**, updates it with as much information as possible from the Super Form.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66350470/image-from-clipboard.png)

12.  **Create New **[**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805)** Item if No Match Is Found After All Email Checks** – If no matching item is found after checking the available email fields, creates a new item in** **[**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) with all available information from the Super Form.

-  **Clear Default Values After Creation** – After creating the new item, removes the temporary default values that were added as part of the [Monday.com](https://Monday.com) creation logic.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66350584/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66392546/image-from-clipboard.png)

## ✅ **Conclusion**

 This automation ensures that completed **Mortgage App Super Forms** are properly matched against existing records whenever possible, whether through related contacts or applicant email addresses. If no match is found, a new item is created in** **[**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805), support is notified, and the required [Monday.com](https://Monday.com) default value handling is completed automatically. This helps keep applicant records updated, reduces duplicates, and ensures new submissions are captured correctly.