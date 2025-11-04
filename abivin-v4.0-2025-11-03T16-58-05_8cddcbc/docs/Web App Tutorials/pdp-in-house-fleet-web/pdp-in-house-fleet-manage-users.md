---
title: Manage Users
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
* In this model, essentially there are the following types of Users:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Type of user
      </th>

      <th style={{ textAlign: "left" }}>
        Management organization
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
        Users who will manage all resources of this model
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Drivers
      </td>

      <td style={{ textAlign: "left" }}>
        Depot
      </td>

      <td style={{ textAlign: "left" }}>
        Users who will perform tasks of Depots on Mobile app
      </td>
    </tr>
  </tbody>
</Table>

* These types of users will be allocated into User groups. Each User group is assigned with different rights and roles

## Create User group

## Locate User group list

* Navigate to **Organizations > Group List** tab
* This tab lists all the User groups in your organization
* You would notice that the **Administrator User groups** were automatically created for every available organization after those organizations have been created

<Image title="2019-10-21 23_07_55-Window.png" alt={1891} className="border" border={true} src="https://files.readme.io/0cb6b59-2019-10-21_23_07_55-Window.png" />

* If you created the **Depot** organization using Web form, the Driver User group - with the User group code ***DELIVERER*** would also have been created automatically

## Create User group

* The User group can only be created manually using Web form
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single objects using Web form

### Basic User group information

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
        Click on this field. Input the Organization Name or Organization Code into the search bar, then choose from the drop down menu
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

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
        If the User group being created is Driver User group, input the following value into this field (Note: All letters must be uppercase): DELIVERER
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

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

      </td>

      <td>

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

### Assign CRUD rights to User group

* On the **Group Information** screen, apart from the basic information fields, you will also see a **Module table**. This table is where you could enable/disable various modules and corresponding CRUD rights for each User group

<Image title="GtVkM9k64v.png" alt={1920} className="border" border={true} src="https://files.readme.io/3b1f329-GtVkM9k64v.png" />

#### Top Administrator User group

* Below are the essential CRUD rights you have to assign to this User group

<Image title="pdp in house crud admin.png" alt={827} className="border" border={true} src="https://files.readme.io/774c6c9-pdp_in_house_crud_admin.png" />

#### Depot Driver User group

<Image title="pdpdriver.png" alt={818} className="border" border={true} src="https://files.readme.io/6a44457-pdpdriver.png" />

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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
