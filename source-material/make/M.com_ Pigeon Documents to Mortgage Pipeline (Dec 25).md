## 📄 **Summary of the Automation**

 This automation is triggered when a **new file is uploaded to any Pigeon question**.

 It finds all items in [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889/views/49646355) linked to the same **Pigeon ID**, identifies **which subitem/question** received the new upload, then retrieves the file location from Pigeon, downloads the file from the **SharePoint folder**, and uploads it into the corresponding subitem in **Mortgage Pipeline JV** under the **Files** column.

## 🧭 **High-Level Steps**

1.  **Trigger on New Pigeon File Upload** - Runs when a new file is uploaded to a Pigeon question.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/56121031/image-from-clipboard.png)

2.  **Look Up Related Items in Mortgage Pipeline JV** - Searches **Mortgage Pipeline JV** for all items associated with the same **Pigeon ID**.

   -  Compares the subitems/questions to determine **which subitem** is the one where the new file was uploaded.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/56121140/image-from-clipboard.png)

3.  **Download the File from SharePoint** - Uses a Pigeon request to retrieve where the file is stored in the **SharePoint folder**, then downloads it from there.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/56121169/image-from-clipboard.png)

4.  **Upload the File to Monday (Subitem Files column)** - Uploads the downloaded file to the matching subitem in [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889/views/49646355), in the **Files** column.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/56124186/image-from-clipboard.png)

## ✅ **Conclusion**

 This [Make.com](https://Make.com) scenario ensures that files uploaded in Pigeon are automatically transferred to the correct subitem in [**Mortgage Pipeline JV**](https://rsfa-squad.monday.com/boards/5025201889/views/49646355), keeping documents centralized in [Monday.com](https://Monday.com) without manual downloading and re-uploading.