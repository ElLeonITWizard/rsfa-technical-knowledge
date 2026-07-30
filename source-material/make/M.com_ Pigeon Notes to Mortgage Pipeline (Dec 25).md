## **📄 Summary of the Automation**

 This automation is triggered whenever a **note is added or updated** on an item in **Pigeon**.

 It is **dependent** on the scenario **“**[**M.com: Pigeon Board to Mortgage Pipeline (Nov 25)**](https://eu2.make.com/85772/scenarios/7950443/edit)**”** , because the Pigeon item must already have an associated bank and an existing record created in [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889)** → Await Docs**.

 Once triggered, the scenario finds **all Await Docs items** in [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889) that are linked to the same Pigeon item (regardless of the bank) and posts the updated note into each item’s **Updates** section.

 

 

## **🧭 High-Level Steps**

1.  **Trigger on Pigeon Note Update** - Runs when a **note is created or modified** on a Pigeon item.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55718126/image-from-clipboard.png)

2.  **Search Matching Items in Mortgage Pipeline JV (Await Docs)** - Retrieves all items in **Mortgage Pipeline JV → Await Docs** that are associated with the same Pigeon item.

   -   This search includes all related items, regardless of which bank they belong to.	

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55719036/image-from-clipboard.png)

3.  **Post the Note as an Update** - For each matching item, the scenario posts the new note in the **Updates** section.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/55719149/image-from-clipboard.png)

## ✅ **Conclusion**

 This [Make.com](https://Make.com) scenario ensures that any note added or updated in Pigeon is automatically replicated as an Update across all linked **Await Docs** items in [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889/views/49646355), keeping all related records aligned without manual effort.