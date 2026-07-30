## 📄 **Summary of the Automation**

 This automation is triggered when a new **Leads Form** or item is created in the [**Leads**](https://rsfa-squad.monday.com/boards/2074688480) board. The Leads Forms exist as far as the website, and an External Form view within the Leads board:

-  External link that can be sent to clients:[ https://rsfa-squad.monday.com/boards/2074688480/views/48177980](https://rsfa-squad.monday.com/boards/2074688480/views/48177980)/ see below[](https://rsfa-squad.monday.com/boards/2074688480/views/48177980)

-  Directing to the Contact Us page of our website, towards the bottom of the page: [https://rsfa.co.nz/contact/](https://rsfa.co.nz/contact/)[Contact Real Savvy Financial Advice | Papamoa, New Zealand](https://rsfa.co.nz/contact/)

 

 The automation checks whether a [**Client Profile**](https://rsfa-squad.monday.com/boards/5024661649) and a [**Contact**](https://rsfa-squad.monday.com/boards/2074688484) already exist for each applicant. If they do not, the automation creates all the necessary records and then updates the [**Client Profile**](https://rsfa-squad.monday.com/boards/5024661649) so that either way, everything is correctly linked, new client, or existing. 

 

 The automation first waits to determine whether the new item was fully populated by a **Leads Form** submission or whether it was created manually and still needs to be completed by an agent. It then processes each applicant individually, checking for an existing [**Client Profile**](https://rsfa-squad.monday.com/boards/5024661649) and [**Contact**](https://rsfa-squad.monday.com/boards/2074688484), creating them if needed, storing their IDs, and finally using those IDs to update the [**Client Profile**](https://rsfa-squad.monday.com/boards/5024661649) with the correct linked contacts.

 

## 🧭 **High-Level Steps**

1.  **Triggers on New Lead Creation** – Runs when a new **Leads Form** or **item is created (manually)** in the [**Leads**](https://rsfa-squad.monday.com/boards/2074688480) board.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66390950/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66391044/image-from-clipboard.png)

### <u>***Warning***</u>

2.  **Wait for the Item to Be Fully Populated** – Waits to determine whether the item was created through a **Leads Form** and is already populated, or whether it was created manually and still needs to be completed by the agent.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66391191/image-from-clipboard.png)

3.  **It checks for an Existing Client Profile for Each Applicant** – For each applicant, it checks whether a related **Client Profile** already exists.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66391350/image-from-clipboard.png)

4.  **It creates a Client Profile if no existing profile is located **– If no related **Client Profile** exists for an applicant, it creates one and stores its ID for later use.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66391416/image-from-clipboard.png)

5.  **It also checks for an Existing Contact by Email** – For each applicant, searches for an existing **Contact** linked to their email address.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66391477/image-from-clipboard.png)

6.  **It also create a Contact if Not Found** – If no related **Contact** is found, creates one and stores its ID.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66391578/image-from-clipboard.png)

7.  **It stores an Existing Contact ID if Found** – If the **Contact** already exists, it stores its ID so it can be used in the next step.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66391645/image-from-clipboard.png)

8.  **It moves on then to update the Client Profile with Linked Contacts** – After processing the/both applicants, it updates the **Client Profile**, whether newly created or already existing, using the stored IDs so the correct contacts are properly linked.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66391729/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66392098/image-from-clipboard.png)

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/66392022/image-from-clipboard.png)

## ✅ **Conclusion**

 This automation ensures that every new item created in the **Leads** board has the necessary **Client Profiles** and **Contacts** in place for each applicant. By creating missing records and then updating the **Client Profile** with the correct linked contacts, the automation helps keep relationships between records accurate, complete, and properly connected.