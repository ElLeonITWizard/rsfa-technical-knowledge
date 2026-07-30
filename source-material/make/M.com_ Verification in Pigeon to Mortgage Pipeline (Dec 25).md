### **📄 Summary of the Automation**

 This automation is triggered when the **Verify** column on Pigeon questions is updated from **“Verify”** to **“Verified”**.

 It is **dependent** on the scenario **“**[**M.com: Pigeon Board to Mortgage Pipeline (Nov 25)**](https://eu2.make.com/85772/scenarios/7950443/edit)**”** , because the Pigeon item must already have an associated bank and an existing record created in [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889)** → Await Docs**.

 Once triggered, the scenario finds **all Await Docs items** in [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889) that are linked to the same Pigeon item (regardless of the bank) and posts the updated note into each item’s **Updates** section.

 

### **🧭 High-Level Steps**

1.  **Trigger on Verify → Verified** - Runs when a Pigeon question’s **Verify** column changes from **“Verify”** to **“Verified”**.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55719762/image-from-clipboard.png)

2.  **Search Matching Items in Mortgage Pipeline JV (Await Docs)** - Retrieves all items in **Mortgage Pipeline JV → Await Docs** that are associated with the same Pigeon item.

   -   This search includes all related items, regardless of which bank they belong to.	

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55719931/image-from-clipboard.png)

3.  **Update Subitem Status** - For each matching item, the scenario updates the corresponding subitem by setting its **Status** column to **“Met/Verified”**.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55719888/image-from-clipboard.png)

## ✅ **Conclusion**

 This [Make.com](https://Make.com) scenario ensures that when a Pigeon question is marked as **Verified**, the corresponding subitem **Status** is automatically updated to **Met/Verified** across all linked **Await Docs** items in [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889/views/49646355), regardless of the bank.