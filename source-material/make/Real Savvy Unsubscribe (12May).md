### **📄 Summary of the Automation**

  In the email sent by the flow "Real Savvy Fixed Rate Expiry Email (May25)," there's a button at the bottom that allows the user to unsubscribe. When this button is clicked, the user should no longer receive reminder emails.

 We need to update their** "Renewal Notification Status" in the "Existing Mortgages**" board on [Monday.com](https://Monday.com) to "**Unsubscribed**", so they are excluded from the logic of the reminder flow.

 

### **🧭 High-Level Steps**

1.  **Triggered via webhook**

   -  This webhook is called when the user clicks the unsubscribe button in the email, which redirects them to a page that activates the flow.

   -  The webhook receives the username as a parameter. This is then used to search for the corresponding user in the Existing Mortgages board.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/34988101/large-image%20%2815%29.png)

 

1.  **U****pdate**** Renewal Notification Status column**

   -  With the name we search in the board for the corresponding user in the "**Existing Mortgages**" board, and their Renewal Notification Status column is updated to "**Unsubscribed**".

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/34988127/large-image%20%2813%29.png)

 

1.  **Redirect the user**

   -  After the update, the user is redirected to the following confirmation page: [https://firbotpages.github.io/unsubscribe/](https://firbotpages.github.io/unsubscribe/)

   -  This ensures the user is visually notified that they have successfully unsubscribed, and their status is updated accordingly in the system.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/34988107/large-image%20%2814%29.png)