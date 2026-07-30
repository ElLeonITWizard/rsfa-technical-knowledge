# **📄 Summary of the Automation**

 The automation ensures that advisers assigned to a client in [Monday.com](https://Monday.com) receive the correct editing permissions for that client’s folder in SharePoint.

 

 It consists of **two functionalities**:

-  **RSFA Asignees Permissions Creation**: triggered when a new item is created in the _Client Profiles_ board.

-  **RSFA Asignees Permissions Modification**: triggered when the _RSFA Asignees_ column of an existing item is updated.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/52469753/image-from-clipboard.png)

# 

# **🧭 High-Level Steps**

 1. Detect creation of a new client profile or modification of the _RSFA Asignees_ column.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/42423442/image-from-clipboard.png)

 2. Retrieve the client’s details and the advisers’ emails from the Monday item.

 3. Locate the client’s folder in SharePoint.

 4. Grant editing permissions to all advisers listed in _RSFA Asignees_.

![Image: ](https://rsfa-squad.monday.com/protected_static/18150562/resources/42423496/image-from-clipboard.png)

 5. In the modification flow, revoke access for advisers removed from the column (except when they belong to predefined SharePoint groups that already have access).

 

# **🔁 Run Cadence**

 Triggers **when a new item is created on the **_**Client Profiles**_** Board** or **when the **_**RSFA Asignees**_** column is modified**.

 

# ⚙️ **Configuration**

-  [**Monday.com**](https://Monday.com)** connection**: Used to detect triggers (new item or column update) and fetch adviser user details (emails).

-  **SharePoint connection**: Used to identify the client folder and adjust permissions accordingly.

-  **¡IMPORTANT! Permissions logic**:

   -  Advisers already part of SharePoint groups with access will not appear individually under _People_ but still retain access.

   -  When advisers are removed, their individual access is revoked, provided they are not members of the predefined groups.

# 

# **✅ Conclusion**

 This automation eliminates the manual effort of managing folder permissions for client advisers, ensuring that access is always aligned with the _RSFA Asignees_ column in Monday. It improves both security and efficiency by automatically granting or revoking access in near real-time.