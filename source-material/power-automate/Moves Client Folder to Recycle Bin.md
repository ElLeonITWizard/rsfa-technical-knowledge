### <u>Summary of automation</u>

-  This workflow has two steps: moving a client folder in SharePoint to the recycle bin. 

-  Step 1 involves a manual webhook trigger connected to the Client Profiles Board, which accepts folder path or item ID. 

-  Step 2 sends a POST request to SharePoint to delete the specified folder in 'Client Files', ensuring unnecessary folders are safely moved to the recycle bin for review.

 **Step 1:** **Trigger the Workflow**

-  A manual webhook trigger, connected to the **Client Profiles Board**, is set up to listen for events.

-  It accepts details such as the folder path or item ID, which is required to locate the folder to be deleted.

![Image: ](https://content.api.getguru.com/files/view/5b37027b-3b6d-42ba-ae2b-e2faf6ae3c1d)

 **Step 2:** **Send HTTP Request to SharePoint**

-  A POST request is sent to SharePoint using the item details provided in the trigger.

-  The request targets the specified folder in SharePoint's "Client Files" and moves it to the recycle bin.

![Image: ](https://content.api.getguru.com/files/view/2f59b80c-dd25-429e-bb7d-8706d4a54a56)

 This ensures that folders no longer needed are safely moved to the recycle bin for further processing or review.