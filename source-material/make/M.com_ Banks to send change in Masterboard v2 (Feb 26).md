## 📄 **Summary of the Automation**

 This automation is triggered when an agent updates the **Banks to Send** column in the [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) board to any bank value.

 Its purpose is to identify which bank was selected and automatically create a new item in the corresponding bank-specific **End Forms** board, carrying over only the relevant mirrored column values for that specific bank.

 Depending on the selected bank, the item is created in one of the following boards:

-  [**ANZ: End Forms**](https://rsfa-squad.monday.com/boards/5025622850)

-  [**ASB: End Forms**](https://rsfa-squad.monday.com/boards/5026525627)

-  [**BNZ: End Forms**](https://rsfa-squad.monday.com/boards/5026525749)

-  [**KB: End Forms**](https://rsfa-squad.monday.com/boards/5026525794)

-  [**WBC: End Forms**](https://rsfa-squad.monday.com/boards/5026525927)

## 🧭 **High-Level Steps**

1.  **Trigger on Banks to Send Update** – Runs when an agent changes the **Banks to Send** column in the **Masterboard: End Forms** board to a bank value.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66343171/image-from-clipboard.png)

2.  **Identify the Selected Bank** – Checks which bank was chosen in the **Banks to Send** column.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66343207/image-from-clipboard.png)

3.  **Check for Existing Duplicates** – Searches the corresponding bank board first to confirm whether an item linked to the same original Masterboard item already exists, preventing duplicate entries from being created.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66343321/image-from-clipboard.png)

4.  **Create and Link the Item** – Creates a new item in the corresponding bank board and links it to the original item where the **Banks to Send** value was updated, so the mirror columns reflect the same connected data.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66343351/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66343366/image-from-clipboard.png)

5.  **Mirror Only Bank-Specific Columns** – Since each bank board only contains the mirror columns related to that specific bank, the new item displays only the relevant bank-specific information.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66343387/image-from-clipboard.png)

## ✅ **Conclusion**

 This automation ensures that when a bank is selected in the **Masterboard: End Forms** board, the relevant data is automatically routed to the correct bank-specific **End Forms** board, allowing the agent to more easily review the information that matters for the specific bank they are working on.