## 📄 **Summary of the Automation**

 This automation is triggered when a new **Super Form** is submitted in [**✍️ ROMA: Mortgages**](https://rsfa-squad.monday.com/boards/5026093057/)[.](https://rsfa-squad.monday.com/boards/5026093057/)

 

 Its purpose is to check whether a corresponding item already exists in the [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) board. If it does, the automation updates that existing item with all the information that can be extracted from the new Super Form. If it does not, the automation creates a new item in the [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) board using all the available information from the Super Form.

 

 In addition, the automation also creates the corresponding subitems in the [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) board based on the subitems submitted through ROMA.

 

## 🧭 **High-Level Steps**

1.  **Trigger on New ROMA Super Form Submission** – Runs when a new item is created in [**✍️ ROMA: Mortgages**](https://rsfa-squad.monday.com/boards/5026093057)[.](https://rsfa-squad.monday.com/boards/5026093057)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66343990/image-from-clipboard.png)

2.  **Wait for Contact Retrieval Automation to Finish** – Since another automation is responsible for retrieving the contact first, this automation waits for that process to complete before continuing.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66344093/image-from-clipboard.png)

3.  **Check for an Existing Item in Masterboard: End Forms** – Verifies whether a matching item already exists in the [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) board.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66344173/image-from-clipboard.png)

4.  **Update Existing Item and Add Subitems if Found** – If the item already exists, updates it with all relevant information that can be extracted from the new Super Form and adds the corresponding subitems submitted through ROMA.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66344303/image-from-clipboard.png)

5.  **Create New Item and Add Subitems if Not Found** – If no matching item exists, creates a new item in the [**Masterboard: End Forms**](https://rsfa-squad.monday.com/boards/5026186805) board using all available information from the Super Form and adds the corresponding subitems submitted through ROMA.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66344375/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66392467/image-from-clipboard.png)

## ✅ **Conclusion**

 This automation ensures that new **ROMA Mortgage Super Forms** are properly reflected in the **Masterboard: End Forms** board, whether by updating an existing item or creating a new one. It also brings across the related subitems, helping keep the Masterboard complete, up to date, and aligned with the information submitted through ROMA.