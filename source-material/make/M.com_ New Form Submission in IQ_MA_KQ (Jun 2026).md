## 📄 **Summary of the Automation**

 This automation is triggered when a new item is created in [🐖 KiwiSaver Questionnaire](https://rsfa-squad.monday.com/boards/5026459551), [❓️Insurance Questionnaire](https://rsfa-squad.monday.com/boards/5025365501/), or [✍ Mortgage App/SOP](https://rsfa-squad.monday.com/boards/5025483251).

 Its purpose is to file the generated PDF into the corresponding client SharePoint folder and notify the team via Slack and email.

 

## 🧭 **High-Level Steps**

1.  **Trigger on New Questionnaire / Mortgage Submission** – Runs when a new item is created in  [🐖 KiwiSaver Questionnaire](https://rsfa-squad.monday.com/boards/5026459551), [❓️Insurance Questionnaire](https://rsfa-squad.monday.com/boards/5025365501/), or [✍ Mortgage App/SOP](https://rsfa-squad.monday.com/boards/5025483251).

   -  **Wait for the Generated PDF** – Waits until the PDF file has been created and attached to the Monday item.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/78654546/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/78654620/image-from-clipboard.png)

2.  **Retrieve the Client SharePoint Folder** – Uses the related contacts and their connection to the Client Profile to retrieve the corresponding SharePoint folder link.

   -  **Identify the Submission Type** – Checks whether the new item belongs to the KiwiSaver, Insurance, or 	Mortgage board and continues through the relevant path.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/78654782/image-from-clipboard.png)

3.  **Download and Upload the PDF to SharePoint** – Downloads the generated PDF from Monday and uploads it to the corresponding client SharePoint folder using the standardized naming structure:

 			** {{lastname}}**_**{{questionnaire_name}}**_**{{month}}{{year}}**

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/78654886/image-from-clipboard.png)

   -  **Wait for the Related Masterboard Item for Mortgage Submissions** – For Mortgage App/SOP submissions, waits until the corresponding item has been created in the Masterboard before continuing.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/78654981/image-from-clipboard.png)

4.  **Send Slack and Email Notifications** – Notifies the team via Slack and email once the PDF has been filed. For Mortgage App/SOP submissions, the notifications also include a link to the related Masterboard item.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/78655048/image-from-clipboard.png)

 

## ✅ **Conclusion**

 This automation ensures that generated PDFs from KiwiSaver, Insurance, and Mortgage submissions are correctly filed into the corresponding client SharePoint folder. 