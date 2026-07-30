### <u>Summary of automation</u>

-  The automation begins by scanning the Sent folder for new emails, followed by a short delay to prevent conflicts. It extracts key email details such as sender, recipients (To, CC, BCC), subject, and timestamps, adjusting time zones for consistency. 

-  Recipient names are organized into lists, and sender names are cleaned for clarity. The automation checks a Monday board for existing email records, performs alternate searches if necessary, and retrieves client profile information using unique IDs. It locates client folders in SharePoint, ensuring no duplicate email files are created. The process checks if emails are internal or external based on the RSFA domain and whether they contain PDF attachments. Email properties are updated accordingly in SharePoint, and if attachments exist, they are saved in a designated folder with updated properties. Notifications for new attachments are sent via Slack. 

-  The automation concludes with all emails and attachments organized and tagged adequately in SharePoint.

### 1. **Starting the Search in Sent Folder**

-  The automation begins by scanning the Sent folder for any new emails that need processing.

![Image: ](https://content.api.getguru.com/files/view/3028a50c-a235-428e-b47a-d628b86f8203)

![Image: ](https://content.api.getguru.com/files/view/b537354a-2067-483c-b45a-3e9865968a61)

### 2. **Adding a Short Delay**

-  To prevent overlap with other processes, a small delay is introduced after the initial search. This ensures that multiple instances of the automation don’t run at the same time, which could cause conflicts and failed process.

![Image: ](https://content.api.getguru.com/files/view/15e1b66e-e190-4d67-9fbb-c19d8ec61157)

### 3. **Extracting Email Details**

-  The automation collects key information from each email, including the sender’s email address, the recipients listed in the "To" field, any addresses included in the "CC" (Carbon Copy) and "BCC" (Blind Carbon Copy) fields, as well as other important details like the email subject and timestamp. This data is then stored for use in the following steps, ensuring all necessary information is readily available for processing and organization.

![Image: ](https://content.api.getguru.com/files/view/d3cc4eed-137e-4438-9469-753ef3fa2d75)

### 4. **Converting and Formatting Time Zones**

-  The automation adjusts the timestamp of each email to the relevant time zone. Once the time zone is updated, the date and time are formatted consistently to ensure a standardized appearance across all emails.

![Image: ](https://content.api.getguru.com/files/view/de46da4d-5b8b-47c7-91e1-b9ca06dc8b73)

### 5. **Getting Recipient Details and Combining Recipients**

-  The automation extracts each recipient’s name from the "To" field of the email. This is a crucial step as it identifies the primary people the email was sent to.

-  After extracting individual recipients from the "To" field, the automation combines them into a single, organized list. This allows for easy access to all main recipients in one place.

![Image: ](https://content.api.getguru.com/files/view/2e11d05b-55fe-48d7-810e-f44ab261b297)

### 6. **Getting CC Recipient Details and Combining CC Recipients**

-  The automation retrieves email addresses from the "CC" field, which contains secondary recipients who were copied on the email for reference or awareness.

-  All "CC" recipients are combined into a unified list. Like the main recipient list, this combined CC list makes it easy to refer to everyone copied on the email.

![Image: ](https://content.api.getguru.com/files/view/ea5f0c7a-3aeb-4e70-930a-187a8a7752a3)

### 7. **Getting BCC Recipient Details and Combining BCC Recipients**

-  The automation extracts addresses from the "BCC" field. BCC recipients receive the email but are hidden from other recipients, so their details are managed separately.

-  All BCC recipients are combined into one list, allowing the automation to handle them as a group without displaying these details to other email recipients.

![Image: ](https://content.api.getguru.com/files/view/f52db091-7112-4904-b711-884a5ac1843e)

### 8. Getting sender name **Cleaning it Up**

-  The automation retrieves the sender name and removes any unnecessary characters or formatting. This makes the sender name clean, consistent, and easy to read.

![Image: ](https://content.api.getguru.com/files/view/e301a722-3e1f-4cc8-a998-60fbadde2e9c)

### 9. **Combining All Emails, Recipients, CC, and BCC into a String**

-  All recipients email are combined into a single string format. This provides a comprehensive view of all recipients involved in the email.

![Image: ](https://content.api.getguru.com/files/view/eea5c6cf-2060-434b-8e4f-716db3db4714)

![Image: ](https://content.api.getguru.com/files/view/f8e87af4-d920-48c4-9a5b-249be3e23035)

### 10. Getting subject line and **Cleaning it Up**

-  The automation retrieves the subject line and removes any unnecessary characters or formatting. This makes the subject line clean, consistent, and easy to read.

![Image: ](https://content.api.getguru.com/files/view/15e4e3a8-7d5a-4292-b08e-6f5341332648)

### 11. **Searching for ID and name Information in Monday Board’s column**

-  The automation checks the Monday board’s primary email database for any matching records. It searches by ID and Name to find if the email is already listed in the database.

![Image: ](https://content.api.getguru.com/files/view/61de4e31-7487-4ef9-a682-f9e67b17e431)

![Image: ](https://content.api.getguru.com/files/view/e7c2d3db-d21b-49b0-9c6b-c6b722e6141d)

### 12. **Checking if the Email is Found in the Monday Board column**

-  A condition is set to check if the email was found in the database. If it was found, the process continues normally; if not, it triggers an alternate search.

![Image: ](https://content.api.getguru.com/files/view/fcc5097c-81f5-4b61-aa84-0199274eaf29)

### 13. **Performing an Alternate Search in the Monday Board’s Secondary Column**

-  If the email wasn’t located in the primary column, an alternate search is performed in a secondary email column on the Monday board. This search also looks for a matching ID and Name.

![Image: ](https://content.api.getguru.com/files/view/10d2c7e0-cb45-49f1-bfda-2a12d27cf150)

![Image: ](https://content.api.getguru.com/files/view/d12c3623-d46b-4859-8be9-21cc5e1828ed)

### 14. **Parsing the Unique ID**

-  Once the email is found in either database, its unique ID is parsed. This ID is crucial for linking the email to other client records and databases.

![Image: ](https://content.api.getguru.com/files/view/aee3a5ef-a770-48c2-94b1-408b7305a017)

### 15. **Querying the Monday Board for Client Profile Information**

-  Using the unique ID, the automation queries the Monday board to retrieve information from the Client Profile column. This step gathers specific client details linked to the email.

![Image: ](https://content.api.getguru.com/files/view/2c23c950-02cf-4d21-837c-49b90caf8ee3)

![Image: ](https://content.api.getguru.com/files/view/2bfb6da9-e0f0-46ed-8984-91f697c326e3)

### 16. **Searching for Client Folder Location in SharePoint**

-  The automation queries SharePoint to locate the client’s specific folder. This folder is where the email and any related files will ultimately be stored.

![Image: ](https://content.api.getguru.com/files/view/7332e601-6bea-41f0-b626-9835ca390ec8)

![Image: ](https://content.api.getguru.com/files/view/fa016552-ce09-4b8b-9a3a-052bea5bd2ec)

### 17. **Locating the Email File in SharePoint**

-  A separate query is made in SharePoint to check if an email file for this particular email already exists. This prevents duplicate file creation.

![Image: ](https://content.api.getguru.com/files/view/46ef9864-eed5-4e36-a075-1c2c23509c51)

![Image: ](https://content.api.getguru.com/files/view/f8f37b35-2403-4593-b955-38a0494513ab)

### 18. **Checking if the Email File Exists**

-  If the email file is found, the automation stops here to avoid duplicating files. If the file does not exist, the automation proceeds to create it.

![Image: ](https://content.api.getguru.com/files/view/69b1ff16-b365-4306-b42e-894b07acf7b6)

### **19. Checking if the Client's Folder Exists in SharePoint**

-  The automation verifies if a client-specific folder is present in SharePoint. This is essential for determining where to place the email file.

![Image: ](https://content.api.getguru.com/files/view/9307657f-5448-47c9-8764-124d1bb6aa6d)

![Image: ](https://content.api.getguru.com/files/view/e406a11c-624e-4840-a21d-332c104d9cc3)

### 20. **Placing the Email File in the Correct Folder**

-  If a specific client folder exists in SharePoint, the email file is saved there; otherwise, it is placed in the general "Emails to sort/Rod_Shay_Kathleen" folder

![Image: ](https://content.api.getguru.com/files/view/f46c2deb-80f3-45ee-92d6-843b2bbf697b)

![Image: ](https://content.api.getguru.com/files/view/b2f9ecfd-fb0f-48d1-a670-c8586c91f65c)

### 21. **Checking if the Sender and Receiver are from the RSFA Domain**

-  A check is performed to see if both the sender and recipient(s) are using the RSFA domain. This helps classify the email as internal or external.

![Image: ](https://content.api.getguru.com/files/view/35fb4747-0385-46d3-b217-c107fe39d9af)

### 22. **Checking for PDF Attachments**

-  The automation checks if the email includes any PDF attachments. This is important for further processing and property updates.

![Image: ](https://content.api.getguru.com/files/view/0304e8d8-729b-4c55-96c6-35f9d842469e)

### 23. **Updating Email File Properties in SharePoint**

-  The email file’s properties, including the date, sender’s name, list of recipients, subject, and more, are updated in SharePoint.

    1.  If the email is internal (both sender and recipient are RSFA) and has no attachments, it’s labeled as “Internal” with an additional “No Attachment” tag.

    2.  If the email is internal and includes an attachment, it’s labeled as “Internal” and tagged with “Yes Attachment.”

    3.  If the email is external (either sender or recipient is outside RSFA) and has no attachment, it’s marked as “External” with a “No Attachment” tag.

    4.  If the email is external and includes an attachment, it’s labeled as “External” and tagged with “Yes Attachment.”

![Image: ](https://content.api.getguru.com/files/view/657daf8f-c761-4d60-8590-22190ba91dbd)

### 24. **Creating the Email File under Client's Folder if It Exists**

-  If a client-specific folder exists, locate the client's folder in SharePoint

![Image: ](https://content.api.getguru.com/files/view/9ce124af-6ba8-4944-a874-84e88e88ffe5)

-  Save the email file under “f. Email Communication” within that folder.

![Image: ](https://content.api.getguru.com/files/view/03ef6b63-c216-44d6-83e4-2cb520c56712)

![Image: ](https://content.api.getguru.com/files/view/55fe749b-ef18-488b-96ce-a8297ed68d1c)

### **25. Checking if the Sender and Receiver are from the RSFA Domain for Client Folders**

-  For emails in client-specific folders, the automation again checks if both the sender and receiver are from the RSFA domain.

![Image: ](https://content.api.getguru.com/files/view/d3b8fc91-d516-4a7a-92c2-2b031b5bdf2b)

### 26. **Verifying if the Email Contains a PDF Attachment in Client-Specific Folders**

-  A check is performed to see if the email includes a PDF attachment for client-specific folder emails.

![Image: ](https://content.api.getguru.com/files/view/c8aa05a5-891b-4fa2-9a7e-24a840963862)

### 27. **Updating Properties for Client-Specific Folders**

-  The email file properties, including date, sender, subject, and other details, are updated for client-specific folders, ensuring consistency.

    1.  If the email is internal and has no attachment, it’s labeled as “Internal” and tagged with “No Attachment.”

    2.  If the email is internal and has an attachment, it’s labeled as “Internal” and tagged with “Yes Attachment.”

    3.  If the email is external and has no attachment, it’s labeled as “External” with a “No Attachment” tag.

    4.  If the email is external and has an attachment, it’s labeled as “External” with a “Yes Attachment” tag.

![Image: ](https://content.api.getguru.com/files/view/31ea6ffd-c685-488f-ae81-c4eeeeaeb18d)

### 28. **Extracting Attachment Details and clean it up**

-  If the email includes an attachment, extract the details of each attachment for further processing and storage. Remove any unnecessary characters or formatting from the subject line to keep it clean, consistent, and easy to read.

![Image: ](https://content.api.getguru.com/files/view/9d079d7d-d4a8-427e-8c44-3ddd5bbadec3)

### **29. Checking for PDF Attachments**

-  The automation checks if the email includes any PDF attachments. This is important for further processing and property updates.

![Image: ](https://content.api.getguru.com/files/view/163e90af-031a-4a51-a3d9-4d6c292a4d3c)

### 30. **Creating the Attachment File under “g. Email Attachments” Folder**

-  If a PDF attachment exists, each attachment is saved as a separate file in the “g. Email Attachments” folder within the client’s directory.

![Image: ](https://content.api.getguru.com/files/view/062c91a1-4dc6-4590-b4b9-4e9fa086f5d7)

![Image: ](https://content.api.getguru.com/files/view/94f3f3ef-bcf8-4bf0-bd94-17113c5cacc4)

### 31. **Updating Attachment File Properties**

-  The properties of each attachment, such as date, sender, and client association, are updated in SharePoint.

![Image: ](https://content.api.getguru.com/files/view/60c14e6b-b0ee-4ff9-8bf4-4b26afa502ef)

### 32. **Sending Slack Notifications for New Attachments**

-  A notification is sent to Slack for each attachment that is added to SharePoint. This informs the team about new documents being available.

![Image: ](https://content.api.getguru.com/files/view/fa009ed8-64d0-49ed-b270-839b45bdfcd8)

![Image: ](https://content.api.getguru.com/files/view/f0a71f8a-6c6a-4241-817a-2b74a82c487f)

### 33. **End of Automation**

-  The process completes once all the steps are fulfilled, ensuring all emails and attachments are organized, filed, and properly tagged in SharePoint, with notifications sent where needed.