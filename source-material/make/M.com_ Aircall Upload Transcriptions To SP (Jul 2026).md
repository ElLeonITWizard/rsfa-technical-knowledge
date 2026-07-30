## 📄 **Summary of the Automation**

 This automation is triggered when a new Aircall call is registered in the [📞 Aircall: VOIP Call Board.](https://rsfa-squad.monday.com/boards/5026308494?term=un&termColumns=XQAAAALvAAAAAAAAAABAqoKjAbHZ0tDTJiUrX6p5Ixoplh2rFjFd-h0peKGiqVsTgyoWTCxk_Yi056PMyHdkObBKdsM0F8HAoddctTsAwCGcLgnsn2MwssrrtCgumZK1EhsfX5GxE5Ld_haHNtupJXDK6NhRD4GjA04Gs_6bwXrUfZjbrkQGcGpYIzmK7k_abJQ9JWBtOPetMUgmqT99TeR4vbLgbFutCefjAUVibb0l__6-cAA)

 Its purpose is to retrieve the call recording and transcription, generate both a full transcript and a concise AI-generated summary in Word format, file the documents into the corresponding client SharePoint folder and files column, and add the call summary to the client timeline.

## 🧭 **High-Level Steps**

1.  Trigger on New Aircall Call – Runs when a new call is registered in the [📞 Aircall: VOIP Call Board.](https://rsfa-squad.monday.com/boards/5026308494?term=un&termColumns=XQAAAALvAAAAAAAAAABAqoKjAbHZ0tDTJiUrX6p5Ixoplh2rFjFd-h0peKGiqVsTgyoWTCxk_Yi056PMyHdkObBKdsM0F8HAoddctTsAwCGcLgnsn2MwssrrtCgumZK1EhsfX5GxE5Ld_haHNtupJXDK6NhRD4GjA04Gs_6bwXrUfZjbrkQGcGpYIzmK7k_abJQ9JWBtOPetMUgmqT99TeR4vbLgbFutCefjAUVibb0l__6-cAA)

   -  Wait for the Client Contact to Be Linked – Waits a few seconds for the related client contact to be connected to the call item, then retrieves the item again with the updated contact information.	

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821576/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821628/image-from-clipboard.png)

2.  Retrieve the Client SharePoint Folder – Uses the linked contact and its connection to the Client Profile to retrieve the corresponding client SharePoint folder.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821590/image-from-clipboard.png)

3.  Retrieve the Aircall Call and Transcription – Uses the Call ID stored in Monday to retrieve the corresponding call details and transcription from Aircall.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821605/image-from-clipboard.png)

4.  Combine the Transcription Utterances – Collects and combines all individual transcription utterances into a single, complete conversation.

   -  Retrieve the Word Templates from SharePoint – Downloads the required Word template files from SharePoint before generating the documents.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821715/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821719/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821726/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821736/image-from-clipboard.png)

5.  Generate the Full Call Transcript – Populates the Word template located in the [Aircall Templates SP Folder](https://rodschubertfinancialadvice.sharepoint.com/sites/RSFATeam/Shared%20Documents/Forms/AllItems.aspx?id=/sites/RSFATeam/Shared+Documents/Aircall+Transcription+Template+(LEO)&newTargetListUrl=/sites/RSFATeam/Shared+Documents&viewid=65a65248-641c-4d10-87ea-87aa5953a02f&viewpath=/sites/RSFATeam/Shared+Documents/Forms/AllItems.aspx). This has all the call information and the complete, literal transcription of the conversation.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821757/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821769/image-from-clipboard.png)

6.  Generate the Call Summary – Uses GPT to create a concise summary of the conversation and populates a separate Word document with the generated content.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821800/image-from-clipboard.png)

7.  Upload the Documents to SharePoint – Uploads the completed transcript and call summary documents to the corresponding client SharePoint folder.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821847/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821927/image-from-clipboard.png)

8.  Upload the Documents to the Client's Files column on the Client Profiles board – Uploads the completed transcript and call summary documents to the corresponding client files column.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80962481/image-from-clipboard.png)

9.  Add the Call to the Client Timeline – Creates a new timeline item containing the call summary and marks it with the Aircall Call tag.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80822013/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/80821823/image-from-clipboard.png)

## ✅ **Conclusion**

 This automation ensures that Aircall conversations are accurately documented, summarized, filed in the corresponding client SharePoint folder and files column, and recorded in the client timeline for future reference.