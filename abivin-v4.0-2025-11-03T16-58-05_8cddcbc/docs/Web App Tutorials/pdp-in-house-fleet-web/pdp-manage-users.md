---
title: Manage Users
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
## User and User Group definition

* User is a person that utilizes the Abivin vRoute Web app or Mobile app
* User Group is a group consisting of Users who share the exact same level of permission within Abivin vRoute

## Types of User

* In this model, there are two compulsory types of Users: **Administrators** and **Drivers**. 

### Administrator Users

* Administrators are the users who will manage the Web app
* Each organization will have its own Administrator User group

### Driver (Deliveryman) Users

* Drivers are the users who will directly operate the delivery vehicles to deliver Orders to the Customers. During the delivery process, they will use the Mobile app to submit the delivery tasks to Web app
* Each Depot/Sun will have its own Driver User group
* To know how the Drivers user the Delivery Mobile app to perform delivery tasks, refer to the following article: [**Drivers (Deliverymen)**](https://dash.readme.io/project/abivin/v3.0/docs/vrp-in-house-fleet-salesman-mobile)
* Below is an illustration of the compulsory User groups hierarchy of this model

<Image title="PDP model.png" alt={581} src="https://files.readme.io/8979394-PDP_model.png">
  Illustration (English)
</Image>

## Manage User group

### Locate User Group list

* User groups are listed on **Organizations > User Groups** tab

<Image title="1. List (ENG).png" alt={1920} border={true} src="https://files.readme.io/0e7b3e7-1._List_ENG.png">
  Illustration (English)
</Image>

<Image title="1. List (VIE).png" alt={1920} border={true} src="https://files.readme.io/f385b76-1._List_VIE.png">
  Illustration (Vietnamese)
</Image>

### Create User Groups

* You would notice that after an Organization is created, the Administrator User Group of that Organization will also be automatically created. The Administrator User Groups will have their **User Group Code** attribute equal to the **Organization Code** attribute plus the prefix ***AD-***, and the **User Group Name** attribute equal to the **Organization Name** plus the prefix ***Admin\_***
* For example: A Branch has the Organization Name attribute to be ***Branch New*** and Organization Code attribute to be ***Branch-New***. The Administrator User Group of that Branch will have the User Group Name attribute to be ***Admin\_Branch New*** and the User Group Code attribute to be ***AD-BRANCH-NEW***

<Image title="2. Group (ENG).png" alt={1728} border={true} src="https://files.readme.io/2cb8d34-2._Group_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Group (VIE).png" alt={1708} border={true} src="https://files.readme.io/d3ead99-2._Group_VIE.png">
  Illustration (Vietnamese)
</Image>

* If you create Organizations of **Depot** Organization Type using Web form, the Driver User Group - with the User Group Code ***DELIVERER*** would also be created automatically

<Image title="3. Driver (ENG).png" alt={1726} border={true} src="https://files.readme.io/7ddbcdd-3._Driver_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Driver (VIE).png" alt={1728} border={true} src="https://files.readme.io/c86f131-3._Driver_VIE.png">
  Illustration (Vietnamese)
</Image>

* Apart from the User Groups that are automatically created, if you wish to create more User Groups, you need to create them manually using Web form. Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single objects using Web form
* The User Groups of optional User Types (Salesmen; Consumer) will not be created automatically. You have to create those User Groups manually

### User Group Information

* Typically, the information of a User Group will be input in two sections:
* 1 - **Basic User Group Information Section**. This section specifies the most essential information of the User Group such as User Group Code, User Group Name. [Click here for instruction](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#basic-user-group-information-section)
* 2 - **Modules Section**. This section specifies the modules that the User Group will have access to and the corresponding CRUD rights over the modules that are allocated to that User Group. [Click here for instruction](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#modules-section) 

<Image title="3. Create Groups (ENG).png" alt={949} border={true} src="https://files.readme.io/c72ac89-3._Create_Groups_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Create Groups (VIE).png" alt={947} border={true} src="https://files.readme.io/b467003-3._Create_Groups_VIE.png">
  Illustration (Vietnamese)
</Image>

* Apart from these two sections, there is also the Route Plan Rights Section. This section is intended for the Route Planner User Groups, which specifies the functions the Route Planner Users can perform to the Route Plan. [**Click here for instruction**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#route-plan-rights-section)

#### Basic User Group Information Section

* Below is the list of basic information fields of a User group

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description & Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organization
        (Required)
      </td>

      <td>
        **1. Description:**\
        The organization which manages the User group being created\
        **2. Input rules:**\
        Click on this field. Input the Organization Name/Organization Code of the appropriate management organization into the search bar, then select from the drop down menu\
        **Note:**\
        If the user group being created is Driver/Salesmen user group, the management organization must be of the following types: ***Depot/Sun***\
        If the user group being created is Consumer user group, the management organization must be of the following type: ***Manufacturer***
      </td>
    </tr>

    <tr>
      <td>
        Group Code\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Management code assigned to the user group being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        If the User group being created is Driver User group, input the following value into this field (All letters must be capitalized): DELIVERER\
        If the User group being created is Salesmen User group, input the following value into this field (All letters must be capitalized): SALESMAN\
        If the User group being created is Consumer User group, input the following value into this field (All letters must be capitalized): CONSUMER\
        **Note:**\
        When you create User Group using Web form, all letters of the Group Code will be automatically capitalized
      </td>
    </tr>

    <tr>
      <td>
        Group Name\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Name of the user group being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Description\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Short introduction about the user group being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

#### Modules Section

* This section is where you can set up the modules that the User Group can get access to, and the corresponding level of authority over those modules
* Below is the description for each permission
* Note: There are certain permissions that are not yet available for some modules

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Module Permission
      </th>

      <th>
        Permission Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Create
      </td>

      <td>
        Can create the resources of that module
      </td>
    </tr>

    <tr>
      <td>
        Read
      </td>

      <td>
        Can read the resources of that module
      </td>
    </tr>

    <tr>
      <td>
        Update
      </td>

      <td>
        Can update/edit the resources of that module
      </td>
    </tr>

    <tr>
      <td>
        Delete
      </td>

      <td>
        Can delete the resources of that module
      </td>
    </tr>

    <tr>
      <td>
        View All
      </td>

      <td>
        Can view the resources of that module from other Organizations of the same level
      </td>
    </tr>

    <tr>
      <td>
        Export
      </td>

      <td>
        Can export the resources of that module to Excel spreadsheet
      </td>
    </tr>

    <tr>
      <td>
        All
      </td>

      <td>
        All of the above permissions
      </td>
    </tr>

    <tr>
      <td>
        Integration-Input
      </td>

      <td>
        Can pull the resource of that module from external databases (TMS; ERP etc.) into Abivin vRoute database
      </td>
    </tr>

    <tr>
      <td>
        Integration-Output
      </td>

      <td>
        Can push the resource of that module from Abivin vRoute database to external databases (TMS; ERP etc.)
      </td>
    </tr>
  </tbody>
</Table>

* Furthermore, in order for the User Group of an upper-level Organization to view the resources of all lower-level Organizations below that upper-level Organization, you need to tick the **Can see Children Organization** checkbox

<Image title="4. Children (ENG).png" alt={943} border={true} src="https://files.readme.io/2f491e3-4._Children_ENG.png">
  Illustration (English)
</Image>

<Image title="4. Children (VIE).png" alt={948} border={true} src="https://files.readme.io/eca435c-4._Children_VIE.png">
  Illustration (Vietnamese)
</Image>

* Below are the essential rights you are recommended to set for each User Group of this model
* Note: The Users who belong to the automatically created Administrator User Group of an Organization will always be able to see all resources of every lower level Organizations of that Organization, regardless of whether the **Can see Children Organization** checkbox is ticked or not. For example, a User who belongs to the automatically created Administrator User Group of a **Branch** will always be able to see the resources of all **Depots** under that Branch.

##### Manufacturer Administrator User group

* The table below list the essential modules and permissions you need to enable for the Manufacturer Administrator User Group of this model

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Module
      </th>

      <th>
        Module Permission
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organizations
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Reports
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Roles
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Users
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Customers
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Products
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        PDP orders
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Vehicle
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Tasks
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Task actions
      </td>

      <td>
        All
      </td>
    </tr>
  </tbody>
</Table>

* Below are the optional permissions that can be enabled depending on your needs:
* If you wish to use the function to retrieve [**Unplanned (Missing) Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-missing-orders) and [**Failed Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-failed-orders) from past dates, you also need to tick the **Integration - Input** checkbox of the **Orders** module
* If your operation involves using [**Discounts and Promotions**](https://docs.abivin.com/docs/vrp-in-house-fleet-discounts-and-promotions), tick the **All** checkbox of the **Promotion** module
* If you wish to use the [**Custom Import Tool**](https://docs.abivin.com/docs/vrp-dc-custom-import) to convert your Delivery Order files to Abivin vRoute data format, tick the **All** checkbox of the **Mapping Profile** module

##### Branch Administrator User group

* The table below list the essential modules and permissions you need to enable for the Branch Administrator User Group of this model

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Module
      </th>

      <th>
        Module Permission
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organizations
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Reports
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Roles
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Users
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Customers
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Products
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        PDP orders
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Vehicle
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Tasks
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Task actions
      </td>

      <td>
        View All
      </td>
    </tr>
  </tbody>
</Table>

##### Depot Administrator User Group

* The table below list the essential modules and permissions you need to enable for the Depot Administrator User Group of this model

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Module
      </th>

      <th>
        Module Permission
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organizations
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Reports
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Roles
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Users
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Customers
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Products
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Orders
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Vehicle
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Tasks
      </td>

      <td>
        All
      </td>
    </tr>
  </tbody>
</Table>

##### Driver User group

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Module
      </th>

      <th>
        Module Permission
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organizations
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Customers
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Products
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Orders
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        PDP orders
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Vehicle
      </td>

      <td>
        All
      </td>
    </tr>

    <tr>
      <td>
        Tasks
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Task actions
      </td>

      <td>
        Read\
        Update
      </td>
    </tr>
  </tbody>
</Table>

* After you have completed creating User groups, let's move on to create Users

## Manage Users

### Locate User List

* Users are listed on **Organizations > Users** tab

<Image title="5. User List (ENG).png" alt={1920} border={true} src="https://files.readme.io/7ce38fb-5._User_List_ENG.png">
  Illustration (English)
</Image>

<Image title="5. User List (VIE).png" alt={1920} border={true} src="https://files.readme.io/75e0428-5._User_List_VIE.png">
  Illustration (Vietnamese)
</Image>

### Create Users

* Users can be created using two methods: Web form and Excel template

#### Method 1: Create single user using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single objects using Web form
* When using Web form to create user, the [basic information fields](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#basic-user-information) of a new user must be input in the following sequence to ensure no mistake:
* 1. Organization Name (Note: You can assign one User to multiple Organizations)
* 2. Groups (Note: You can assign one User to multiple User Groups within the Organizations selected above)
* 3. Username (See this article for instruction: [**User Account Setup**](https://docs.abivin.com/docs/web-app-account#username-rules))
* 4. Password, Re-password (See this article for instruction: [**User Account Setup**](https://docs.abivin.com/docs/web-app-account#password-rules))
* 5. Email (You should use real email addresses in order to [reset password when forgetting](https://docs.abivin.com/docs/web-app-account#reset-forgotten-login-password))
* 6. Phone Number
* 7. Full Name
* If the user being created is a Driver, you also have to fill some [specific information fields](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#section-specific-information-of-driver)

<Image title="6. User Info (ENG).png" alt={1707} border={true} src="https://files.readme.io/bc23428-6._User_Info_ENG.png">
  Illustration (English)
</Image>

<Image title="6. User Info (VIE).png" alt={1707} border={true} src="https://files.readme.io/442789c-6._User_Info_VIE.png">
  Illustration (Vietnamese)
</Image>

#### Method 2: Create multiple users using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template
* You will notice that in the Excel template, there is no **Password** field. This is because upon uploading the Excel template onto the Web app, each user will receive an email enclosed with a password in the email addresses linked with their accounts. They have to use those passwords to login for the first time. After logging in, they can change their passwords to new ones (Note that the new passwords must adhere to the [**Strong Password rules**](https://docs.abivin.com/docs/web-app-account#section-password-rules))

> 📘 How to change password?
>
> * For Web app users, please [click on this link](https://docs.abivin.com/docs/web-app-account#section-change-login-password)
> * For Mobile app users, please [click on this link](https://docs.abivin.com/docs/mobile-app-general-instruction#section-update-strong-password)

#### Basic User information

* Below are the basic information fields of a User

> 📘 Apart from the information fields mentioned below, other information fields can be left blank during the creation/update processes

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description & Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organization Name (Web form); Organization Code (Excel template)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The organization in which the user being created belongs\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the appropriate Organization Name into the search bar then choose from the drop down menu\
        **Excel template:**\
        Copy the appropriate Organization code on Web app, then paste into this cell\
        **Note:**\
        The Organization Code can be found under "Organization Code" column in "Organizations > Organization List" tab\
        If the user being created is Driver, the organization must be of Depot/Sun type
      </td>
    </tr>

    <tr>
      <td>
        Groups (Web form); User Group Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        User group in which the user being created belongs\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the appropriate User group name into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the appropriate User group code on Web app, then paste into this cell\
        **Note:**\
        The User group name and User group code can be found under "Group Name" and "Group Code" columns in "Organizations > Group List" tab
      </td>
    </tr>

    <tr>
      <td>
        Username\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Username of the User being created. The User will use this username to login to Web app/Mobile app\
        **2. Input rules:**\
        Maximum 15 characters\
        Letters and numbers are inputtable. Special characters (Not letters and numbers) and spaces will not be inputtable
      </td>
    </tr>

    <tr>
      <td>
        Password; Re-password\
        (Web form)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Password of the user being created. The User will use this password to login to Web app/Mobile app\
        **2. Input rules:**\
        Read the password rules in this article: [**User account setup**](https://docs.abivin.com/docs/web-app-account#section-password-rules)\
        Input the same password value into both Password and Re-password fields
      </td>
    </tr>

    <tr>
      <td>
        Email\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Email address of the user being created\
        After being created, each new user will receive a email attached with a random password. The user must use that password to log in their account on the first time. After successfully logging in, they can freely change the password as instructed in the following article: [**User Account Setup**](https://docs.abivin.com/docs/web-app-account#change-login-password)\
        **2. Input rules:**\
        Input the correct, existing email address into this field/cell\
        **Note when using Excel template:**\
        You MUST remove all hyperlinks from the email addresses before uploading. Read this article for instruction: [**CRUD functions**](https://docs.abivin.com/docs/crud#section-rule-4-remove-hyperlinks-from-email-addresses)
      </td>
    </tr>

    <tr>
      <td>
        Phone Number\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Phone number of the user being created\
        **2. Input rules:**\
        Format: Numbers only. Must not contain spaces\
        For example: "090 181 0800" or "090.181.0800" is not acceptable; "0901810800" is acceptable
      </td>
    </tr>

    <tr>
      <td>
        Full Name\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Full name of the user being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

#### Specific information of Driver

* Apart from the basic information fields above, there will be some additional information fields for users who are **Deliverymen (Drivers)**
* On Web form, these information fields will be visible when you click on **MORE CONFIGURATIONS** :fa-caret-down:

<Image title="7. More Config (ENG).png" alt={1701} border={true} src="https://files.readme.io/cb6a5b4-7._More_Config_ENG.png">
  Illustration (English)
</Image>

<Image title="7. More Config (VIE).png" alt={1701} border={true} src="https://files.readme.io/c239d62-7._More_Config_VIE.png">
  Illustration (Vietnamese)
</Image>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description & Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Vehicle Type (Web form); Type Of Vehicle (Excel template)
        (Required)
      </td>

      <td>
        **1. Description:**\
        Type of vehicle operated by the driver being created\
        One driver can only operate one vehicle type\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Choose the appropriate value from the following three values: truck; bike; semi-truck\
        **Excel template:**\
        **VRP model:**\
        Input only one of the following three values into the cell: ***truck; bike; semi-truck***\
        **Note when using Excel template:**\
        This value is case sensitive. Do not input values such as: ***Truck; BIKE***\
        This value must always be input in English as above
      </td>
    </tr>

    <tr>
      <td>
        Position\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Position of the driver being created in the driver user group\
        **2. Input rules:**\
        **Web form:**\
        Click on this field then choose from the drop down menu\
        **Excel template:**\
        Input the following value into the cell if the driver being created is a Light duty truck driver: LDD\
        Input the following value into the cell if the driver being created is a Heavy duty truck driver: HDD\
        Input the following value into the cell if the driver being created is the leader of the driver group: Driver Leader\
        Input the following value into the cell if the driver being created is a driver who normally operates motorbikes: Delivery Man\
        **Note when using Excel template:**\
        This value is case sensitive. You must input one of the values as shown above into the cell
      </td>
    </tr>

    <tr>
      <td>
        Driver License Number\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Driver license number of the driver being created\
        **2. Input rules:**\
        Format: Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        License Class\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        License class of the driver being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Select the appropriate license class from the drop down menu\
        You can select more than one value, meaning the driver being created has more than one license class\
        **Excel template:**\
        Input license class like on Web form into the cell\
        If the driver being created has more than one license class, separate two adjacent license classes only by commas. Do not add spaces\
        For example: The driver being created has two driver licenses of class A and class B. Input the following values into the cell: A,B
      </td>
    </tr>

    <tr>
      <td>
        Medically Cleared\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Specify whether the driver being created has passed the required medical examination of your organization or not\
        **2. Input rules:**\
        **Web form:**\
        Click on the check box if the user being created has passed required medical exams\
        **Excel template:**\
        Input the following value into the cell if the driver being created has passed required medical examination: TRUE\
        Input the following value into the cell if the driver being created has not passed required medical examination: FALSE\
        **Note when using Excel template:**\
        This field is case sensitive. You must input one of the exact values above into this cell
      </td>
    </tr>

    <tr>
      <td>
        Secret\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Secret of the driver being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        sub scription Code\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Subscription Code of the driver being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        sub scription Expiry\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Subscription Expiry date of the driver being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

## Change Active Status of Drivers

* Besides **Organizations > Users** tab, users who are drivers can also be managed in **Transportation > Drivers** tab

<Image title="8. Trans (ENG).png" alt={1920} border={true} src="https://files.readme.io/0f20c26-8._Trans_ENG.png">
  Illustration (English)
</Image>

<Image title="8. Trans (VIE).png" alt={1920} border={true} src="https://files.readme.io/3119c9f-8._Trans_VIE.png">
  Illustration (Vietnamese)
</Image>

* On this tab, you can change the active status of the drivers - Specify whether the driver is currently active and can be assigned delivery tasks or the driver is currently inactive
* By default, after being created, all drivers will have the active status to be ***Active***, represented by the icon :fa-check-square-o: under the column **Active**. This means the drivers can be assigned delivery tasks during the route optimization process

<Image title="9. Active (ENG) 2.png" alt={1730} border={true} src="https://files.readme.io/1177011-9._Active_ENG_2.png">
  Illustration (English)
</Image>

<Image title="9. Active (VIE) 2.png" alt={1730} border={true} src="https://files.readme.io/d0a53c1-9._Active_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* To change the active status of a driver, click on that icon. When that icon turns to :fa-square-o:, that means the active status of the driver has been converted to ***Inactive***. That driver will not appear anymore in the route optimization process, unless you have locked a Delivery shift with that driver assigned before changing the active status of that driver

<Image title="10. Inactive (ENG).png" alt={1730} border={true} src="https://files.readme.io/2effb52-10._Inactive_ENG.png">
  Illustration (English)
</Image>

<Image title="10. Inactive (VIE).png" alt={1728} border={true} src="https://files.readme.io/ce7969e-10._Inactive_VIE.png">
  Illustration (Vietnamese)
</Image>
