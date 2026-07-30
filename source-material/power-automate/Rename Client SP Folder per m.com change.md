### <u>Summary of automation:</u>

-  This workflow automates renaming a client folder in SharePoint based on updates from the Client Profile Board within [Monday.com](https://Monday.com). 

-  It begins with a webhook trigger from a manual HTTP request. The workflow then parses JSON to extract details like pulseID and the new folder name. Using the pulseID, it reformats the folder name, retrieves existing folder details from SharePoint, and sends a POST request to rename the folder. 

-  It generates an updated SharePoint link and synchronises it to [Monday.com](https://Monday.com), ensuring seamless updates with minimal manual intervention.

### Step 1: **Webhook Trigger**

 The workflow starts when a manual HTTP request is sent, triggered by an update on the Client Profile Board.

![Image: ](https://content.api.getguru.com/files/view/6ada027c-4432-4bbc-b3f1-a5dbc0524984)

### Step 2: **Parse JSON**

 Parses the JSON content from the webhook to extract relevant details, such as `pulseID` and the new folder name.

![Image: ](https://content.api.getguru.com/files/view/56147cf1-55f5-4952-b8b4-67adb1f7bd08)

### Step 3: **Extract Pulse ID**

 Fetches the `pulseID` from the webhook data for identifying the related item in [Monday.com](https://Monday.com).

![Image: ](https://content.api.getguru.com/files/view/706955a2-ca64-4ce7-aee8-b898050488a0)

### Step 4: **Generate Client Folder Name**

 Reformats the new folder name received from the webhook, replacing spaces with `%20` and adding "and" for formatting consistency.

![Image: ](https://content.api.getguru.com/files/view/a0eb570a-8f62-4614-a055-c72c247a5b96)

### Step 5: **Get Existing Folder Details**

 Queries SharePoint to locate the existing folder in the "Client Files" directory using the extracted `pulseID`.

![Image: ](https://content.api.getguru.com/files/view/b17edd4b-61ad-4f49-9733-bfa89bbfca11)

### Step 6: **Send Update Request to SharePoint**

 Sends a POST request to SharePoint to rename the located folder using the new folder name.

![Image: ](https://content.api.getguru.com/files/view/51d38e9c-6e7f-4ca6-832e-f60ba4870b39)

### Step 7: **Generate Updated Link**

 Creates the updated SharePoint folder link using the new folder name and formats it for synchronization with [Monday.com](https://Monday.com).

![Image: ](https://content.api.getguru.com/files/view/e40c1067-996d-4a5e-a0d1-6de9345e2a79)

### Step 8: **Update **[**Monday.com**](https://Monday.com)

 Sends the updated folder link back to the Client Profile Board on [Monday.com](https://Monday.com) using the `pulseID` to ensure synchronization.

![Image: ](https://content.api.getguru.com/files/view/21de0622-1edc-4733-984c-d6b1404686ec)

 This workflow ensures seamless folder name updates across SharePoint and [Monday.com](https://Monday.com) with minimal manual intervention.