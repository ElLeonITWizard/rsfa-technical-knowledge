### **📄 Summary of the Automation**

 This automation is triggered when the **“Banks to Send”** field is updated for one or more banks in the [**Pigeon Board JV**](https://rsfa-squad.monday.com/boards/5025365499) board.


 Its purpose is to detect the updated bank entry, check whether it has already been registered in the **Await Docs** table within the [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889/views/49646355) board, and if not, create and populate a new record. It also retrieves the related client information from [**Client Profiles JV :: Private**](https://rsfa-squad.monday.com/boards/5024661649/views/49255949) so the new item is correctly linked to the client profile. Finally, it requests the set of questions (subitems) from Pigeon and creates them as subitems under the newly created item.

 

### **🧭 High-Level Steps**

1.  **Trigger on “Banks to Send” Update** - Runs when the **Banks to Send** field is modified in the **Pigeon Board JV** board.

   -  The scenario detects the item that was updated and identifies which bank(s) were added/changed.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55717328/image-from-clipboard.png)

 

2.  **Look Up the Item in “Await Docs” (Mortgage Pipeline JV)** - Searches the **Await Docs** table in [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889/views/49646355) to check if the bank is already registered for that item/client.

   -   If a matching record already exists for the same bank, the flow **does not create a new entry**.

   -   o If no matching record exists, the flow proceeds to create and populate a new item.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55717435/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55717498/image-from-clipboard.png)

3.  **Retrieve Client Profile Data (Client Profiles JV :: Private)** - Pulls the client’s details from **Client Profiles JV :: Private** to correctly link the new item to the client profile.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55717592/image-from-clipboard.png)

4.  **Create and Populate the New “Await Docs” Item** - Creates a new item in **Await Docs** and fills the 					 required fields.

   -  The **bank** that was added is stored on the new item.

   -  The item is linked back to the original record using the **Pigeon Board JV item ID** (reference/linking ID).

   -  The new item is associated to the correct **Client Profile**.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55717692/image-from-clipboard.png)

 

5.  **Fetch Pigeon Questions and Create Subitems** - Requests the list of questions from Pigeon and creates them as subitems under the newly created item.

   -  Each question in Pigeon is created as a **subitem**, and filed with the data in pigeon.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55717779/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55717856/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55717889/image-from-clipboard.png)

### ✅ **Conclusion**

 This [Make.com](https://Make.com) scenario ensures that any update to **“Banks to Send”** in [**Pigeon Board JV**](https://rsfa-squad.monday.com/boards/5025365499) is automatically reflected in the **Await Docs** process within [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889). By validating whether the bank entry already exists, linking the new record to the correct [**Client Profile**](https://rsfa-squad.monday.com/boards/5024661649/views/49255949), and generating the required **Pigeon questions as subitems**.