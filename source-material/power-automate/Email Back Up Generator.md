### 📄 **Summary of the Automation**

 This Power Automate flow generates a backup of all emails (and their attachments) from a specific Outlook mailbox into SharePoint. It loops through mailbox folders, filters those that should be processed, retrieves emails in batches of 25, and stores the relevant data into the corresponding SharePoint folders. It also moves each email to a “Processed” or “Failed” folder depending on the outcome.

 

### 🧭 **High-Level Steps**

1.  **Trigger the Flow Manually: **The flow starts with a manual trigger for controlled execution.

2.  **Get Mail Folders from SharePoint: **Retrieves a SharePoint list containing the folders to process.

3.  **Initialize and Parse Folder Data: **Sets an email counter to 0 and parses the JSON with folder details.

4.  **Loop Through Each Folder**

   -  Counts items per folder.

   -  Composes folder name for use.

   -  Skips folders marked as “non-processable”.

1.  **Get Emails in Batches (Top 25): **For each processable folder, retrieves the latest 25 emails using the Outlook connector.

2.  **Loop Through Each Email**

   -  Increments a counter to determine parity (even or odd).

   -  Calls one of two child flows depending on the counter (to allow parallel/distributed processing).

1.  **Run Until All Emails Are Processed: **A `Do until` loop ensures all emails in the folder are processed batch by batch.

### ✅ **Conclusion**

 This automation provides a scalable and structured way to back up emails from a mailbox to SharePoint, handling attachments and processing status automatically. To adapt it to a new mailbox, one simply needs to update the Outlook connection and ensure the “Processed” and “Failed” folders exist in the target mailbox.