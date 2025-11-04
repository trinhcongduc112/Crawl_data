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
## User Type

* In this model, essentially there seven User types:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        User Type
      </th>

      <th style={{ textAlign: "left" }}>
        Management Organization
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Top Administrators
      </td>

      <td style={{ textAlign: "left" }}>
        Manufacturer
      </td>

      <td style={{ textAlign: "left" }}>
        Users who will manage all resources
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Order Creator Users
      </td>

      <td style={{ textAlign: "left" }}>
        Branch
      </td>

      <td style={{ textAlign: "left" }}>
        Users who will create Orders on behalf of the Depots
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Order Inspector Users
      </td>

      <td style={{ textAlign: "left" }}>
        Branch
      </td>

      <td style={{ textAlign: "left" }}>
        Users who will inspect and approve/decline the Orders that have been created and submitted by the Order Creators
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Route Planner Users
      </td>

      <td style={{ textAlign: "left" }}>
        Branch
      </td>

      <td style={{ textAlign: "left" }}>
        Users who will perform Route Plan Optimization process for the Orders that have been approved by and submitted from the Order Inspectors
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Transporter Administrators
      </td>

      <td style={{ textAlign: "left" }}>
        Transporter
      </td>

      <td style={{ textAlign: "left" }}>
        Users who will accept/decline the optimized Delivery Routes that have been optimized by and forwarded from the Route Planners
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Warehousemen
      </td>

      <td style={{ textAlign: "left" }}>
        Depot
      </td>

      <td style={{ textAlign: "left" }}>
        Users who will hand over products to the Transporter's drivers (If they belong to the Origin Depot) or receive products from the Transporter's drivers (If they belong to the Destination Depot)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Drivers
      </td>

      <td style={{ textAlign: "left" }}>
        Transporter
      </td>

      <td style={{ textAlign: "left" }}>
        Users who will operate the vehicles, travel to the Origin Depot, receive products and deliver to the Destination Depot
      </td>
    </tr>
  </tbody>
</Table>

* These User types will be allocated into User Groups. Each User Group is assigned different permissions

## Create User group

### Locate User group list

* Navigate to **Organizations > Group List** tab
* This tab lists all the User groups in your organization
* You would notice that the **Administrator User groups** were automatically created for every available organization after those organizations have been created

<Image title="2019-10-21 23_07_55-Window.png" alt={1891} className="border" border={true} src="https://files.readme.io/0cb6b59-2019-10-21_23_07_55-Window.png" />

* The Warehousemen User groups will also be created automatically for every available organizations of **Depot** type, with the User Group Code ***WAREHOUSEMEN***
* The Driver User groups will also be created automatically for every available organizations of **Transporter** type, with the User Group Code ***DELIVERER***

### Create User group

* The User group can only be created manually using Web form
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single objects using Web form

#### Basic User group information

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
        Click on this field. Input the Organization Name or Organization Code into the search bar, then choose from the drop down menu\
        **Note:**\
        If the user being created is a Driver, the organization must be of "Transporter" type\
        If the user being created is a Warehouseman,  the organization must be of "Depot" type
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
        **Special notes:**\
        If the User group being created is Driver User group, input the following value into this field (Note: All letters must be uppercase): DELIVERER\
        If the User group being created is Warehousemen User group, input the following value into this field (Note: All letters must be uppercase): WAREHOUSEMEN\
        There are no requirements when inputting group codes of Order Issuer; Order Inspector; Route Planners user groups
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

#### Assign CRUD rights to User group

* On the **Group Information** screen, apart from the basic information fields, you will also see a **Module table**. This table is where you could enable/disable various modules and corresponding CRUD rights for each User group

<Image title="GtVkM9k64v.png" alt={1920} className="border" border={true} src="https://files.readme.io/3b1f329-GtVkM9k64v.png" />

* To immediately navigate to the CRUD rights of a specific User group, click on the corresponding link in the below table:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        User group
      </th>

      <th>
        CRUD rights
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Top Administrators
      </td>

      <td>
        [Click on this link](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-users#section-top-administrator-user-group)
      </td>
    </tr>

    <tr>
      <td>
        Order Creators
      </td>

      <td>
        [Click on this link](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-users#section-order-creator-user-group)
      </td>
    </tr>

    <tr>
      <td>
        Order Inspectors
      </td>

      <td>
        [Click on this link](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-users#section-order-inspector-user-group)
      </td>
    </tr>

    <tr>
      <td>
        Route Planners
      </td>

      <td>
        [Click on this link](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-users#section-route-planners-user-group)
      </td>
    </tr>

    <tr>
      <td>
        Transporter Administrators
      </td>

      <td>
        [Click on this link](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-users#section-transporter-administrator-user-group)
      </td>
    </tr>

    <tr>
      <td>
        Warehousemen
      </td>

      <td>
        [Click on this link](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-users#section-warehousemen-user-group)
      </td>
    </tr>

    <tr>
      <td>
        Drivers
      </td>

      <td>
        [Click on this link](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-users#section-transporter-driver-user-group)
      </td>
    </tr>
  </tbody>
</Table>

#### **Top Administrator User group**

* Below are the essential CRUD rights you have to assign to this User group

#### **Order Creator User group**

* Before assigning CRUD rights to this User group, you have to make sure this User group can see all Depots under their Branch's management by clicking on **Can see Children Organization** check box

<Image title="can see children.png" alt={293} className="border" border={true} src="https://files.readme.io/29045de-can_see_children.png" />

* Next, click on **Order Issuer** radio box under **Order Approval Role** field
* The field  **Authorized Depot** will appear below. This is where you need to select the Depots which you want to grant this Order Issuer User group the authorization to create Orders on behalf of

<Image title="order issuer selected.png" alt={403} className="border" border={true} src="https://files.readme.io/8ff2ccd-order_issuer_selected.png" />

* To select the Depots, click on the field below the **Depot** text. Input the Organization Code/Organization Name of the appropriate Depots into the search bar, then select from the drop down menu

<Image title="select depot.png" alt={227} className="border" border={true} src="https://files.readme.io/c2cc74b-select_depot.png" />

* You can also select all Depots under the Branch by clicking on **Access All** check box

<Image title="access all.png" alt={1693} className="border" border={true} src="https://files.readme.io/926a4a8-access_all.png" />

* The selected Depots are hereby called ***Authorized Depots***, and the remaining unselected Depots are called ***Not Authorized Depots***
* Combining with the Depot types that have been mentioned at the article [**Manage Organizations**](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-organizations#special-notes-when-creating-depots), we have a total of six Depot groups based on the authorization: ***Authorized Internal Depot; Not Authorized Internal Depot; Authorized Customer Depot; Not Authorized Customer Depot; Authorized Supplier Depot; Not Authorized Supplier Depot***
* After selecting the Depots, assign the CRUD rights to this User group as below:

<Image title="order issuer.png" alt={817} className="border" border={true} src="https://files.readme.io/30f8732-order_issuer.png" />

##### **Order Creating permission**

* You also need to specify the Order Creating permission for this User group. To do this, perform the following steps:
* Navigate to **Organizations > Organization List** tab
* Click the icon **Edit** :fa-pencil: of the **Branch** which manages this Order Creator User group
* On the form **Edit Organization**, navigate to the sub-tab **More Configuration > Order Creation**
* Here you can configure the Depot group pairs that the Order Creator User Group can create Orders on behalf of
* Sequentially click on the fields below the text **Permission Order's Origin** and **Permission Order's Destination**, select the Depot group pair which you want to grant the Order creating permission to the Order Creator User group
* For example: If the value selected from the field **Permission Order's Origin** is ***Authorized Internal*** and the corresponding value selected from the field **Permission Order's Destination** is ***Authorized Supplier***, that means the Order Creator User group is granted the permission to create Orders from an Authorized Internal Depot to an Authorized Supplier Depot

<Image title="C991gQ1AKd.png" alt={730} className="border" border={true} src="https://files.readme.io/24bc609-C991gQ1AKd.png" />

* To add more Depot group pairs, click on the button **Add Permission** to add additional rows

![723](https://files.readme.io/af3075d-ba16163-wkRhfL7Zvs.png "ba16163-wkRhfL7Zvs.png")

* To remove a Depot group pair, click on the corresponding recycle bin icon :fa-trash: of that pair

<Image title="35ab43e-LWyReia1Cp.png" alt={678} className="border" border={true} src="https://files.readme.io/095ec14-35ab43e-LWyReia1Cp.png" />

* If you accidentally add duplicate pairs, then as you click on the button **Save**, there will be an error message

<Image title="a73b638-p42QMuV5aC.png" alt={587} className="border" border={true} src="https://files.readme.io/3c6e8c4-a73b638-p42QMuV5aC.png" />

#### *Order Inspector User group*

* Before assigning CRUD rights to this User group, you have to make sure this User group can see all Depots under their Branch's management by clicking on **Can see Children Organization** check box

<Image title="order inspector 1.png" alt={363} className="border" border={true} src="https://files.readme.io/851d634-order_inspector_1.png" />

* Next, click on **Order Inspector** radio box under **Order Approval Role** field
* The **Depot** field will appear below. This is where you need to select the Depots of which you want to grant this Order Inspector User group the right to inspect orders

<Image title="Selection_003.png" alt={508} className="border" border={true} src="https://files.readme.io/aaec9d9-Selection_003.png" />

* To select the Depots, click on the field below the **Depot** text. Input the Organization Code/Organization Name of the appropriate Depots into the search bar, then select from the drop down menu

<Image title="c2cc74b-select_depot.png" alt={227} className="border" border={true} src="https://files.readme.io/c82b6db-c2cc74b-select_depot.png" />

* You can also select all Depots under the Branch by clicking on **Access All** check box

<Image title="926a4a8-access_all.png" alt={1693} className="border" border={true} src="https://files.readme.io/a3bae13-926a4a8-access_all.png" />

* After selecting the Depots, assign the CRUD rights to this User group as below:

<Image title="order inspector rights.png" alt={818} className="border" border={true} src="https://files.readme.io/2818323-order_inspector_rights.png" />

##### **Order Approving permission**

* You also need to specify the Order Approving permission for this User group. To do this, perform the following steps:
* Navigate to **Organizations > Organization List** tab
* Click the icon **Edit** :fa-pencil: of the **Branch** which manages this Order Inspector User group
* On the form **Edit Organization**, navigate to the sub-tab **More Configuration > Order Creation**
* Here, with each Depot group pair that have been created earlier for the Order Creator User Group above, you need to specify for which Depot (Between the Origin and Destination Depot) that this Order Inspector User Group can approve Orders 
* For example: If the value selected from the field **Permission Order's Origin** is ***Authorized Internal***, the corresponding value selected from the field **Permission Order's Destination** is ***Authorized Supplier***, the value selected from the field **Approval Permission** is ***Destination***, that means the Order Inspector User group can approve every Order that originates from an Authorized Internal Depot and will be delivered to an Authorized Supplier Depot as long as the Authorized Supplier Depot belongs to the list of authorized Depot configured above for this User Group

<Image title="C991gQ1AKds.png" alt={730} className="border" border={true} src="https://files.readme.io/71b78ca-C991gQ1AKds.png" />

#### *Route Planners User group*

* Before assigning CRUD rights to this User group, you have to make sure this User group can see all Depots under their Branch's management by clicking on **Can see Children Organization** check box

<Image title="29045de-can_see_children.png" alt={293} className="border" border={true} src="https://files.readme.io/49320e5-29045de-can_see_children.png" />

* Next, click on **Route Planner** radio box under **Order Approval Role** field

<Image title="Selection_002.png" alt={510} className="border" border={true} src="https://files.readme.io/7a5d9c2-Selection_002.png" />

* Then, assign the CRUD rights to this User group as below:

<Image title="Selection_003.png" alt={816} className="border" border={true} src="https://files.readme.io/aa6b01a-Selection_003.png" />

#### *Transporter Administrator User group*

<Image title="Selection_005.png" alt={817} className="border" border={true} src="https://files.readme.io/a54cd37-Selection_005.png" />

#### *Transporter Driver User group*

<Image title="Selection_014.png" alt={829} className="border" border={true} src="https://files.readme.io/0c9a421-Selection_014.png" />

#### *Warehousemen User group*

<Image title="Selection_006.png" alt={822} className="border" border={true} src="https://files.readme.io/af1d69e-Selection_006.png" />

## Create Users

* Navigate to **Organizations > User List** tab
* This tab lists the users in your organization

<Image title="7Ltjn1ypw1.png" alt={1920} className="border" border={true} src="https://files.readme.io/b6e1c5f-7Ltjn1ypw1.png" />

* You have two options to create Users: Using Web form or using Excel template

## Option 1: Create single user using web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single objects using Web form
* When using Web form, the information fields of a new user must be input in the following sequence to ensure no mistakes:

1. Organization Name
2. Groups
3. Username
4. Password; Re-password
5. Email
6. Phone Number
7. Full Name

## Option 2: Create multiple users using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template

## Basic User information

* Below are the basic information fields of a User

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
        The Organization Code can be found under "Organization Code" column in "Organizations > Organization List" tab
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
        (Web form + Excel template)\
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
        **2. Input rules:**\
        Input the correct, existing email address into this field/cell\
        **Note when using Excel template:**\
        You MUST remove all hyperlinks from the email addresses before uploading. Read this article for instruction: [**CRUD functions**](https://docs.abivin.com/docs/crud#section-remove-hyperlinks-from-email-addresses-before-upload)
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

## Extensive Driver user information

* Apart from the basic information fields above, there will be some additional information fields for users who are **Delivery men (or drivers)**
* On Web form, these information fields will be visible when you click on **MORE CONFIGURATIONS** :fa-caret-down:

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
        Click on this field. Choose the appropriate vehicle type from the drop down menu\
        **Excel template:**\
        Copy the code of the appropriate vehicle type on Web app, then paste into this cell\
        The code of the vehicle type can be found under "Type Code" column in "Transportation > Vehicle Type" tab
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
        Input this value into the cell if the driver being created is a Light duty truck driver: LDD\
        Input this value into the cell if the driver being created is a Heavy duty truck driver: HDD\
        Input this value into the cell if the driver being created is the leader of the driver group: Driver Leader\
        Input this value into the cell if the driver being created is a driver who normally operates motorbikes: Delivery Man\
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

> ❗️ For this model, every Depot, including Supplier's Depots, needs to have one Warehouseman user, else you will not be able to perform Route Optimization process\
> Similarly, every vehicles of the Transporter needs to be assigned a default driver

## Change active status of Drivers

* By default, after being created, the drivers are ***Active*** - meaning that they can be assigned delivery routes
* In the scenario a driver is temporarily inable to perform delivery routes, you can change the status of that driver to ***Inactive*** by following the steps below
* Navigate to **Transportation > Driver** tab
* Click on the check box icon :fa-check-square-o: of the driver which you want to change the active status to inactive. When that icon changes to :fa-square-o:, that means the driver has been inactive
