### <u>Summary of automation </u>

 This workflow automates the retrieval of completed DocuSign envelope details, client information from [Monday.com](https://Monday.com), and file storage in SharePoint. 

 It begins by monitoring completed DocuSign envelopes and retrieving the signer’s email to search for client records within [Monday.com](https://Monday.com). The process continues if the email is found in the Primary Email Column; otherwise, an Alternate Search is conducted in the Secondary Email Column. Once the Unique ID is extracted, the system queries the Client Profile Column for detailed client information. It then searches for the client’s folder in SharePoint, verifying its existence. If the folder exists, documents are uploaded; if not, they are saved in a 'Received Documents to File' folder. The workflow retrieves signed documents from DocuSign, checks for existing files in the client folder to avoid duplicates, and uploads new documents if necessary. Finally, it logs the upload and notifies the support team via Slack, ensuring efficient signed document management.

### **Step 1: Monitor Completed DocuSign Envelopes**

-  The workflow starts automatically when a DocuSign envelope is completed.

-  It listens for the "envelope-completed" status update from DocuSign.

![Image: ](https://content.api.getguru.com/files/view/40ac22e5-7997-4478-8bd6-1bbd6b09fc13)

### **Step 2: Retrieve the Signer’s Email**

-  The automation retrieves the email address of the signer from the completed DocuSign envelope.

-  This email will be used to search for client records in [Monday.com](https://Monday.com).

![Image: ](https://content.api.getguru.com/files/view/64bc9c54-2fee-4547-873f-2616d134e4d6)

### **Step 3: Searching for EMAIL Information in Monday Board’s Primary Column**

-  The system searches the Monday board’s database using the signer’s email.

-  It checks the **Primary Email Column** to locate records associated with the email address.

-  If a match is found, the record’s **ID and Name** are retrieved for further processing.

![Image: ](https://content.api.getguru.com/files/view/61de4e31-7487-4ef9-a682-f9e67b17e431)

![Image: ](https://content.api.getguru.com/files/view/e7c2d3db-d21b-49b0-9c6b-c6b722e6141d)

### **Step 4: Checking if the Email is Found in the Monday Board Column**

-  A condition checks if the email was successfully found in the primary column.

-  If the email exists in the database, the process continues with the matched record.

-  If the email is not found, the workflow triggers an **Alternate Search**.

![Image: ](https://content.api.getguru.com/files/view/fcc5097c-81f5-4b61-aa84-0199274eaf29)

### **Step 5: Performing an Alternate Search in the Monday Board’s Secondary Column**

-  The system performs a second search in the Monday board, this time looking in a **Secondary Email Column**.

-  It attempts to find a match using the same email and retrieves the corresponding **ID and Name**.

![Image: ](https://content.api.getguru.com/files/view/10d2c7e0-cb45-49f1-bfda-2a12d27cf150)

![Image: ](https://content.api.getguru.com/files/view/d12c3623-d46b-4859-8be9-21cc5e1828ed)

### **Step 6: Parsing the Unique ID**

-  Once the email is located (in either the primary or secondary column), the associated **Unique ID** is extracted.

-  This ID links the signer’s email to their client records in [Monday.com](https://Monday.com).

![Image: ](https://content.api.getguru.com/files/view/aee3a5ef-a770-48c2-94b1-408b7305a017)

### **Step 7: Querying the Monday Board for Client Profile Information**

-  Using the extracted Unique ID, the system queries the Monday board’s **Client Profile Column**.

-  It retrieves detailed client information, such as their profile and other linked data, for the next steps in the workflow.

![Image: ](https://content.api.getguru.com/files/view/2c23c950-02cf-4d21-837c-49b90caf8ee3)

![Image: ](https://content.api.getguru.com/files/view/2bfb6da9-e0f0-46ed-8984-91f697c326e3)

### **Step 8: Searching for Client Folder Location in SharePoint**

-  The automation connects to SharePoint and searches for a folder specific to the client.

-  The search is based on the retrieved client details (e.g., name, email, or unique ID).

![Image: ](https://content.api.getguru.com/files/view/7332e601-6bea-41f0-b626-9835ca390ec8)

![Image: ](https://content.api.getguru.com/files/view/fa016552-ce09-4b8b-9a3a-052bea5bd2ec)

### **Step 9: Checking if the Client’s Folder Exists in SharePoint**

-  The system verifies if the client-specific folder is present in SharePoint.

-  If the folder exists, it will be used as the destination for the email and related files.

-  If the folder does not exist, it will be saved in **Received Documents to File folder**.

![Image: ](https://content.api.getguru.com/files/view/9307657f-5448-47c9-8764-124d1bb6aa6d)

![Image: ](https://content.api.getguru.com/files/view/e406a11c-624e-4840-a21d-332c104d9cc3)

### Step 10: If the client folder DOESN'T exists, Retrieve Signed Documents

-  The system retrieves all signed documents and the certificate of completion from DocuSign once an envelope is completed.

![Image: ](https://content.api.getguru.com/files/view/a0b30b94-1add-44d3-ba3e-34e6fa762280)

### Step 11: Save Documents to SharePoint

-  The signed documents are saved in a folder named **"Received Documents to File"** in SharePoint.

![Image: ](https://content.api.getguru.com/files/view/70558168-8b30-4b2a-8dbd-712cbbfe79a1)

![Image: ](https://content.api.getguru.com/files/view/70cb91fa-d979-44df-bdc5-23dd875bbd5f)

### Step 12: Notify the Support Team

-  A Slack message is sent to the **support_team_tasks** channel.

-  The message includes a link to the temporary folder and a note to:

   -  Check [Monday.com](https://Monday.com) to verify why the email address isn’t linked to a client profile.

   -  Rename and move the documents to the correct client folder.

![Image: ](https://content.api.getguru.com/files/view/f9ad313d-554a-43c7-9173-5ae404aa9cf9)

![Image: ](https://content.api.getguru.com/files/view/16194a47-fb8c-4d25-ad91-be67b42e1150)

### Step 13: IF THE CLIENT FOLDER EXISTS, Extract the Client ID

-  Extract the client ID from the Monday board. This ID will act as a unique identifier for the client and is critical for subsequent steps in the workflow.

-  Search the **Client folder** in the SharePoint site.

-  Use the client ID to create a filter query and locate the folder specific to the client.

-  If a matching folder is found, its full path will be returned.

![Image: ](https://content.api.getguru.com/files/view/9ce124af-6ba8-4944-a874-84e88e88ffe5)

### Step 14: Retrieve the Full Folder Path

-  Use the **ClientFullPath** variable to store the complete folder path of the client’s folder retrieved from SharePoint in Step 13. This ensures seamless integration for file uploads and processing.

![Image: ](https://content.api.getguru.com/files/view/88e97c1c-d1db-4815-a2a9-8beeb3cbbee5)

### Step 15: Download Documents from DocuSign

-  Use the **Get documents from envelope 2** action to retrieve signed documents from DocuSign based on the envelope ID.

-  Ensure that the Certificate of Completion is also downloaded to maintain compliance and documentation integrity.

![Image: ](https://content.api.getguru.com/files/view/371709d5-42c0-48a1-b676-aa9c77fdba85)

### Step 16: Check for Existing Files in the Client Folder

-  Use the **CheckFile** action to verify whether the specific signed document already exists in the client’s SharePoint folder. This step prevents duplicate file uploads.

-  Apply a filter query using the document name to streamline the search process.

![Image: ](https://content.api.getguru.com/files/view/099ff2ba-821f-494c-8fce-ce5faa69e82b)

### Step 17: Upload the Signed Document (if not already present)

-  If the document does not already exist in the client’s folder:

   -  Use the **FileDocs** action to upload the signed document to the SharePoint folder.

   -  Ensure the file is named appropriately with the client’s name and document type for easy identification.

![Image: ](https://content.api.getguru.com/files/view/8b1a00b3-1954-486b-915b-96250c7c6a99)

### Step 18: Log the File Upload for Reference

-  Use the **Post message (V2)** action to notify the support team on Slack about the successful file upload.

-  Include the SharePoint link to the uploaded file for easy access by the team.

![Image: ](https://content.api.getguru.com/files/view/5638bb8b-8d78-46ae-a294-627525175887)

### Summary

 This workflow automates the process of managing signed documents received through DocuSign. It includes steps to extract client information, locate or create client folders in SharePoint, and notify the support team for further action.