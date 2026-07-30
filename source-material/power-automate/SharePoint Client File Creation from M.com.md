### <u>Summary of automation</u>

-  This workflow automates folder creation in SharePoint and updates [Monday.com](https://Monday.com) with links to those folders, enhancing organisation and accessibility. 

-  It begins with an HTTP Trigger to initiate the flow. Then, incoming data is parsed and formatted. Subfolder names are initialized, and new folders are created in SharePoint. The folder path is stored and formatted for URL use. 

-  Finally, an HTTP POST request updates [Monday.com](https://Monday.com) with the SharePoint folder link, improving efficiency and saving time.

### Step 1: Trigger the Workflow

 Start the workflow with an **HTTP Trigger**.

-  Allow external systems to initiate the flow using a URL.

-  Ensure incoming data is properly structured using a JSON schema.

![Image: ](https://content.api.getguru.com/files/view/fdafa2f3-9a2d-445c-9b39-e1a0e397d2c8)

### Step 2: Read Incoming Data

 Use **Parse JSON** to extract key information from the HTTP request.

![Image: ](https://content.api.getguru.com/files/view/ba67ecba-9e2d-4a06-b52b-ff1efa395cbb)

### Step 3: Format Data

 Use **Compose** to combine and clean data like folder names or IDs for easier processing.

![Image: ](https://content.api.getguru.com/files/view/80eefe09-e94f-4f2d-a0c4-15e09d45620e)

### Step 4: Set Up Folder Names

 Create a list of subfolder names using an **Initialize Variable** action (e.g., "Mortgages," "Risk Insurance").

![Image: ](https://content.api.getguru.com/files/view/74a37e38-9953-4a69-9db4-c392e07a11f4)

### Step 5: Create a New Folder

 Use **Create new folder** to add a folder in the SharePoint library based on the provided data.

![Image: ](https://content.api.getguru.com/files/view/a281f203-c46b-4d22-a073-afdda71854af)

### Step 6: Save Folder Path

 Store the folder’s path using a **Compose** action for later use.

![Image: ](https://content.api.getguru.com/files/view/62b600e5-9293-4089-80c8-d78c027f8d07)

### Step 7: Create Subfolders

 Use **Create new folder** again to create subfolders under the main folder dynamically.

![Image: ](https://content.api.getguru.com/files/view/6e6b59e9-fe4b-4af9-83ff-159cc8fd46d4)

### Step 8: Prepare Folder Path for Links

 Format the folder path for use in URLs by replacing spaces and special characters with a **Compose** action.

![Image: ](https://content.api.getguru.com/files/view/d3a4343a-6af4-4ae6-bcec-b3f95daf8791)

### Step 9: Update [Monday.com](https://Monday.com) with Folder Link

 Send an HTTP POST request to [Monday.com](https://Monday.com) to add the SharePoint folder link to a specific column in a board.

![Image: ](https://content.api.getguru.com/files/view/7fc39092-1395-4db4-a5ec-3ecf69c407d8)

### Conclusion

 This workflow keeps files organized in SharePoint and ensures links are accessible within [Monday.com](https://Monday.com), saving time and improving efficiency.