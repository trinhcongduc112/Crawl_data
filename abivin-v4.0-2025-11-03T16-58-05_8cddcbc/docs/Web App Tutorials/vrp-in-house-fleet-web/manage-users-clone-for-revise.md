---
title: Manage Users (Clone for Revise)
excerpt: ''
deprecated: false
hidden: true
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

* In this model, there are two compulsory User types: **Administrators** and **Drivers**. Apart from these compulsory User types, there are some optional User types: **Salesmen** and **Consumers**

## Administrator Users

* Administrators are the users who will manage the Web app
* Each organization will have its own Administrator User group

## Driver (Deliveryman) Users

* Drivers are the users who will directly operate the delivery vehicles to deliver Orders to the Customers. During the delivery process, they will use the Mobile app to submit the delivery tasks to Web app
* Each Depot/Sun will have its own Driver User group
* To know how the Drivers user the Delivery Mobile app to perform delivery tasks, refer to the following article: [**Drivers (Deliverymen)**](https://dash.readme.io/project/abivin/v3.0/docs/vrp-in-house-fleet-salesman-mobile)
* Below is an illustration of the compulsory User groups hierarchy of this model

<Image title="Untitled Diagram.png" alt={1031} border={true} src="https://files.readme.io/ae6ab4a-Untitled_Diagram.png">
  Illustration Image (English)
</Image>

## Salesman Users

* In many companies, there exists a group that consists of employees who are sales people (Salesmen). These sales people will explore new markets, find and build rapport with new customers. When the business relationships with the customers have been established, the sales people might be required to track the status of orders delivered to their associated customers, or even deliberately create orders for their customers
* Each Depot/Sun will have its own Salesmen User group
* To know how the Salesmen use the Delivery Mobile app to perform delivery tasks, refer to the following article: [**Salesmen**](https://docs.abivin.com/docs/vrp-in-house-fleet-salesmen-web)

## Consumer Users

* Consumers are the end-users, who will ultimately consume the products manufactured by your organizations. When they have demand for certain products, they will actively place orders. After that, the dispatchers of your organization will assign delivery tasks to the Drivers (Deliverymen)
* To know how the Consumers user the Consumer Mobile app to place Sales order, refer to the following article: [**Consumers**](https://docs.abivin.com/docs/vrp-in-house-fleet-consumers)

## Manage User group

## Locate User Group list

* User groups are listed on **Organizations > User Groups** tab

<Image title="org group.png" alt={1894} border={true} src="https://files.readme.io/357d5bb-org_group.png">
  Illustration Image (English)
</Image>

<Image title="AoczRuYRz0.png" alt={1920} border={true} src="https://files.readme.io/753f03b-AoczRuYRz0.png">
  Illustration Image (Vietnamese)
</Image>

## Create User Groups

* You would notice that after an Organization is created, the Administrator User Group of that Organization will also be automatically created. The Administrator User Groups will have their **User Group Code** attribute equal to the **Organization Code** attribute plus the prefix ***AD-***, and the **User Group Name** attribute equal to the **Organization Name** plus the prefix ***Admin\_***
* For example: A Branch has the Organization Name ***Branch Hanoi*** and the Organization Code ***Branch\_Hanoi***. The User Group Administrators of that Branch will have the User Group Name ***Admin\_Branch Hanoi*** and the User Group Code ***AD-Branch\_Hanoi***

<Image title="org group code name.png" alt={1643} border={true} src="https://files.readme.io/f8f95b4-org_group_code_name.png">
  Illustration Image (English)
</Image>

* If you create the Depot using Web form, the Driver User Group would also be created automatically. They will have the User Group Code ***DELIVERER***

<Image title="delv.png" alt={879} border={true} src="https://files.readme.io/a987003-delv.png">
  Illustration Image (English)
</Image>

* Apart from the User Groups that are automatically created, if you wish to create more User Groups, you need to create them manually using Web form. Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single objects using Web form
* The User Groups of optional User Types (Salesmen; Consumer) will not be created automatically. You have to create those User Groups manually

## User Group Information

* Typically, the information of a User Group will be input in two sections:
* 1 - Basic User Group Information Section. This section specifies the most essential information of the User Group such as User Group Code, User Group Name. [Click here for instruction](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#basic-user-group-information-section)
* 2 - Modules Section. This section specifies the modules that the User Group will have access to and the corresponding CRUD rights over the modules that are allocated to that User Group. [Click here for instruction](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#modules-section) 

<Image title="OPK4jerF3w.png" alt={846} border={true} src="https://files.readme.io/b250ceb-OPK4jerF3w.png">
  Illustration Image (English)
</Image>

* Apart from these two sections, there is also the Route Plan Rights Section. This section is intended for the Route Planner User Groups, which specifies the functions the Route Planner Users can perform to the Route Plan. [Click here for instruction](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#route-plan-rights-section)

<Image title="QyuiheFBhN.png" alt={825} border={true} src="https://files.readme.io/c37a2fe-QyuiheFBhN.png">
  Illustration Image (English)
</Image>

### Basic User Group Information Section

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

### Modules Section

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

<Image title="ntKcvO9Dwg.png" alt={609} border={true} src="https://files.readme.io/3eeba0b-ntKcvO9Dwg.png">
  Illustration Image (English)
</Image>

* Below are the essential rights you are recommended to set for each User Group of this model
* Note: The Users who belong to the automatically created Administrator User Group of an Organization will always be able to see all resources of every lower level Organization of that Organization, regardless of whether the **Can see Children Organization** checkbox is ticked or not. For example, a User who belongs to the automatically created Administrator User Group of a **Branch** will always be able to see the resources of all **Depots** under that Branch

#### Manufacturer Administrator User group

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

* Below are the optional permissions which can be enabled depending on your needs:

* If you wish to use the function to retrieve [**Unplanned (Missing) Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-missing-orders) and [**Failed Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-failed-orders) from past dates, you also need to tick the **Integration - Input** checkbox of the **Orders** module

* If your operation involves using [**Discounts and Promotions**](https://docs.abivin.com/docs/vrp-in-house-fleet-discounts-and-promotions), tick the **All** checkbox of the **Promotion** module

* If you wish to use the [**Convert Tool (Built-in)**](https://docs.abivin.com/docs/vrp-in-house-fleet-built-in-convert-tool) to convert your Delivery Order files to Abivin vRoute data format, tick the **All** checkbox of the **Mapping Profile** module

* If you wish to use route plan both in List View and in Map View, please follow these steps

* Step 1: Select a Manufacturer. Click the symbol in the Edit column to edit information for the selected Manufacturer. 

* Step 2: In the form named **Update Group**, select **Other Permissions**. Under the column Route Plan, tick the box **Read**.

* Step 3: Click **Save** for changes to take effects

<Image title="3. Permission (ENG).png" alt={1920} border={true} src="https://files.readme.io/59a7e29-3._Permission_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Permission (VIE).png" alt={1920} border={true} src="https://files.readme.io/1558057-3._Permission_VIE.png">
  Illustration (Vietnamese)
</Image>

#### Depot/Sun Driver User group

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
        Tasks
      </td>

      <td>
        Read\
        Update
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
  </tbody>
</Table>

* If you want to allow the Drivers to actively rearrange the Stop sequence of their assigned Delivery Route right on their Mobile App (Read more here: [**Driver (Delivery Men)**](https://docs.abivin.com/docs/vrp-dc-mobile-app-driver#rearrange-stop-sequence)), then you'll need to navigate to the Other Permissions sub-tab and enable the **Move Order/Stop** permission

<Image title="uILvh0LSdE.png" alt={846} className="border" border={true} src="https://files.readme.io/bc8cf2b-uILvh0LSdE.png" />

#### Route Plan Rights Section

* For the Route Planner (Dispatcher) User Groups (Of the Organization Types **Manufacturer; Distributor; Branch**), there are various functions related to the Route Plan that requires a dedicated setup section apart from the Module section above
* Before going into details, there are some notes: 
* 1 - The automatically created Administrator User Group of the **Manufacturer** will always have full Route Planning permissions regardless of whether the functions in this section are enabled for that User Group or not
* 2 - Some functions in this section will have the same effect as some configurations at some Organization Type (Mostly at the **Branch**). However, the configurations set up at the Organization will always have priority over the functions described in this section. For example, if you don't enable a function in this section but enable the configuration with the same effect at the Organization, then the Users can still use that function
* 3 - Some functions in this section are only available on either [Route Plan (Map View)](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-map-view) or [Route Plan (List View)](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-list-view), not yet available on both modes
* To access the Route Plan Rights setup section, on the **Update Group** form navigate to the sub-tab **Other Permissions**
* To enable a function, simply tick its respective checkbox
* To quickly enable all functions, tick the **Route Plan** checkbox

<Image title="RuLbTbX7qh.png" alt={831} className="border" border={true} src="https://files.readme.io/1733857-RuLbTbX7qh.png" />

* Below is the list of all functions related to the Route Plan:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Route Plan Function
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Create
      </td>

      <td>
        Available for: Map View and List View\
        The ability to generate the Route Plan
      </td>
    </tr>

    <tr>
      <td>
        Read
      </td>

      <td>
        Available for: Map View and List View\
        The ability to view the details of an optimized Route Plan\
        **Important Note**\
        This function is the most fundamental function. If this function is not enabled, no other function can be performed even if they are enabled
      </td>
    </tr>

    <tr>
      <td>
        Delete
      </td>

      <td>
        Available for: Map View and List View\
        The ability to delete/remove a Delivery Shift from the Route Plan\
        Same effect as the following Branch's configuration: [**\
        Enable Unlock And Remove Route**](https://docs.abivin.com/docs/vrp-in-house-fleet-configurations-by-organization-type#enable-unlock-and-remove-route)
      </td>
    </tr>

    <tr>
      <td>
        Export
      </td>

      <td>
        Available for: Map View and List View\
        The ability to export the Route Plan
      </td>
    </tr>

    <tr>
      <td>
        Optimize
      </td>

      <td>
        Available for: Map View and List View\
        The ability to optimize the Route Plan
      </td>
    </tr>

    <tr>
      <td>
        Lock Route
      </td>

      <td>
        Available for: Map View and List View\
        The ability to lock the Delivery Routes within the Route Plan
      </td>
    </tr>

    <tr>
      <td>
        Unlock Route
      </td>

      <td>
        Available for: Map View and List View\
        The ability to unlock the locked Delivery Routes within the Route Plan\
        Same effect as the following Branch's configuration: [**\
        Enable Unlock And Remove Route**](https://docs.abivin.com/docs/vrp-in-house-fleet-configurations-by-organization-type#enable-unlock-and-remove-route)
      </td>
    </tr>

    <tr>
      <td>
        Finalize Route
      </td>

      <td>
        Available for: Map View and List View\
        The ability to finalize the locked Delivery Routes within the Route Plan
      </td>
    </tr>

    <tr>
      <td>
        Integration Output
      </td>

      <td>
        Available for: List View\
        The ability to synchronize the finalized Route Plan to the external Transportation Management Systems
      </td>
    </tr>

    <tr>
      <td>
        Close Trip
      </td>

      <td>
        Available for: List View\
        The ability to 'close' the Delivery Trips within the Route Plan, confirming the Orders within the Delivery Trips have been completed
      </td>
    </tr>

    <tr>
      <td>
        Change Driver
      </td>

      <td>
        Available for: Map View and List View\
        The ability to change driver for the Delivery Shifts within the Route Plan
      </td>
    </tr>

    <tr>
      <td>
        Change Vehicle
      </td>

      <td>
        Available for: Map View and List View\
        The ability to change vehicle for the Delivery Shifts within the Route Plan
      </td>
    </tr>

    <tr>
      <td>
        Move Order/Stop
      </td>

      <td>
        Available for: Map View and List View\
        The ability to move the Orders within a Stop or an entire Stop to another position within the Route Plan; or move Unplanned (Missing) Orders into the Route Plan\
        **Note**\
        Moving Order is currently not available for Map View mode
      </td>
    </tr>

    <tr>
      <td>
        Update Stop Location
      </td>

      <td>
        Available for: Map View\
        The ability to update the coordinate information of a Stop within the Route Plan
      </td>
    </tr>

    <tr>
      <td>
        Remove Order/Stop
      </td>

      <td>
        Available for: Map View and List View\
        The ability to remove the Orders within a Stop or an entire Stop out of the Route Plan\
        **Note**\
        Removing Order is currently not available for Map View mode
      </td>
    </tr>
  </tbody>
</Table>

* After you have completed creating User groups, let's move on to create Users

## Manage Users

## Locate User list

* Users are listed on **Organizations > User List** tab

<Image title="7Ltjn1ypw1.png" alt={1920} className="border" border={true} src="https://files.readme.io/b6e1c5f-7Ltjn1ypw1.png" />

## Create Users

* Users can be created using two methods: Web form and Excel template

### Method 1: Create single user using Web form

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

<Image title="Selection_002.png" alt={1903} className="border" border={true} src="https://files.readme.io/0564f48-Selection_002.png" />

### Method 2: Create multiple users using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template
* You will notice that in the Excel template, there is no **Password** field. This is because upon uploading the Excel template onto the Web app, each user will receive an email enclosed with a password in the email addresses linked with their accounts. They have to use those passwords to login for the first time. After logging in, they can change their passwords to new ones (Note that the new passwords must adhere to the [**Strong Password rules**](https://docs.abivin.com/docs/web-app-account#section-password-rules))

> 📘 How to change password?
>
> * For Web app users, please [click on this link](https://docs.abivin.com/docs/web-app-account#section-change-login-password)
> * For Mobile app users, please [click on this link](https://docs.abivin.com/docs/mobile-app-general-instruction#section-update-strong-password)

### Basic User information

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

### Specific information of Driver

* Apart from the basic information fields above, there will be some additional information fields for users who are **Deliverymen (Drivers)**
* On Web form, these information fields will be visible when you click on **MORE CONFIGURATIONS** :fa-caret-down:

<Image title="Selection_003.png" alt={1898} className="border" border={true} src="https://files.readme.io/ad552bc-Selection_003.png" />

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

## Change Active Status of Driver Users

* Besides the **Organizations > Users** tab, the driver users also have a dedicated tab, **Transportation > Drivers**. On this tab, you can change their Active Status

<Image title="Image 1.png" alt={1908} border={true} src="https://files.readme.io/034a67e-Image_1.png">
  Illustration Image (English)
</Image>

<Image title="TbbLskRJah.png" alt={1920} border={true} src="https://files.readme.io/18eeff8-TbbLskRJah.png">
  Illustration Image (Vietnamese)
</Image>

* By default, after being created, all drivers will have the Active Status ***Active***, represented by the icon :fa-check-square-o: under the column **Active**. This means the drivers can be selected to operate the vehicles during the Route Plan optimization process

<Image title="ALrvcwY47H.png" alt={1309} className="border" border={true} src="https://files.readme.io/3bf144c-ALrvcwY47H.png" />

* To change the active status of a driver, click on that icon. When that icon turns to :fa-square-o:, that means the Active Status of the driver has been switched to ***Inactive***, which means that driver will not appear anymore in the Route Plan optimization process, unless prior to this you have locked a Delivery Shift with that driver

## Beginner's Guide

After creating an organizational chart (you can see the tutorial for beginners [here](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-organizations#beginners-guide)), you can proceed to the next step in the Route Optimization Process: Creating users. In this tutorial, we will determine users as drivers.

### Create a User Group

* Below are the simple steps on how to create a Driver user group using Web form:

* Step 1: Navigate to **Organizations > User Group** tab.

* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Create** (the :fa-pencil: symbol).

![2876](https://files.readme.io/bc1d34a-Screen_Shot_2021-01-22_at_10.56.59.png "Screen Shot 2021-01-22 at 10.56.59.png")

* Step 3: Input information to complete the **Group Information** section. There are 3 required fields:
* **Group Code:** Input the following value: ***SAMPLE-DELIVERER***
* **Organization:** The organization type must be Depot/Sun: ***Sample Depot***
* **Group Name:** Input the name of the Driver user group: ***Sample Deliverers***
* *Example*: 

![2880](https://files.readme.io/27785d5-Screen_Shot_2021-01-22_at_11.07.35.png "Screen Shot 2021-01-22 at 11.07.35.png")

* Step 4: In the **Configurations** section, set up the modules that the  Driver User Group can get access to, and the corresponding level of authority over those modules by ticking the boxes:

![1220](https://files.readme.io/0c484aa-Screen_Shot_2021-01-22_at_13.47.12.png "Screen Shot 2021-01-22 at 13.47.12.png")

* Step 5: Click **SAVE**
* Beside Web form, Excel files can be used to create a Driver user group. Here are the steps to import an Excel file into the system:
* Step 1: Navigate to **Organizations > User Group** tab.
* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Import**.
* Step 3: Choose the Excel you want to import by dropping it to the area or clicking the area.
* **Note:** The chosen file must be in the right format and contain required fields (Group Code, Organization, Group Name). You can also download a sample with a correct format provided by us. To do this, click **DOWNLOAD SAMPLE**. Then you can paste your data onto the sample file.

### Create a User

Next, here are the steps you should follow to create a user (driver)

* Step 1: Navigate to **Organizations > Users** tab.
* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Create** (the :fa-pencil: symbol).

![2880](https://files.readme.io/75f57f3-Screen_Shot_2021-01-22_at_13.49.18.png "Screen Shot 2021-01-22 at 13.49.18.png")

* Step 3: Fill in information to complete the User information section. These are the required fields:
* **Organization Name:** Input the organization in which the user being created belongs: ***Sample Depot***
* **Username:** Input the username the driver will use to login to  the Web app/Mobile app
* **Phone Number:** Input the phone number of the driver being created
* **Full Name:** Input the full name of the driver being created
* **Password/Re-password:** Input the password the driver will use to login to Web app/Mobile app. The password must follow [password rules](https://docs.abivin.com/docs/web-app-account#password-rules)
* **E-mail:** Input the e-mail address of the driver being created. After being created, each new user will receive a email attached with a random password. The user must use that password to log in their account on the first time. After successfully logging in, they can freely change the password as instructed in the following article: [Change login password](https://docs.abivin.com/docs/web-app-account#change-login-password)

![2880](https://files.readme.io/4f7420a-Screen_Shot_2021-01-22_at_13.59.56.png "Screen Shot 2021-01-22 at 13.59.56.png")

* **Vehicle:** Click **MORE CONFIGURATIONS:fa-caret-down:** for the **Vehicle** field to be shown, then click on vehicle assigned to the driver. 

![2880](https://files.readme.io/18513ca-Screen_Shot_2021-01-22_at_14.03.20.png "Screen Shot 2021-01-22 at 14.03.20.png")

* Step 4: Click **SAVE**
