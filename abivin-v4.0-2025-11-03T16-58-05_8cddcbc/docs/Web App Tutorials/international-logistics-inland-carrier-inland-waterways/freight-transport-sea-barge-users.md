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
## Locate user list

* Navigate to **Organizations > User List** tab
* This tab lists all the users under an organization's management
* The top organization administrator accounts can view all users of every organization under their management

<Image title="2019-10-20 17_54_57-Window.png" alt={1899} className="border" border={true} src="https://files.readme.io/c13cacb-2019-10-20_17_54_57-Window.png" />

## Create users

## User information fields

> 🚧 Except for the information fields mentioned below, all other information fields can be left blank

### Basic information fields

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organization Name (Web form); Organization Code (Excel template)
      </td>

      <td>
        **1. Description:**\
        The organization which manages the user being created\
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

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Groups (Web form); User Group Code (Excel template)
      </td>

      <td>
        **1. Description:**\
        User group in which the user being created belongs\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the appropriate User group name into the search bar, then select from the drop down menu\
        For users who are barge captain, always input the following value into this cell: DELIVERER\
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

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Username\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        Username of the user being created. The user will use this username to login to  both Web app and Mobile app\
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

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Password; Re-password\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        Password of the user being created. The user will use this password to login to both Web app and Mobile app\
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

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Email\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        Email address of the user being created\
        **2. Input rules:**\
        Input the correct, existing email address of the user being created into this field/cell\
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

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Phone Number\
        (Web form + Excel template)
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

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Full Name\
        (Web form + Excel template)
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

### Additional information fields for barge captain users

* On Web form, if the user being created is a Barge captain, you need to input additional information field by clicking on **More Configurations** :fa-caret-down:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Vehicle Type (Web form); Type Of Vehicle (Excel template)
      </td>

      <td>
        **1. Description:**\
        Type of vehicle operated by the driver being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field. Choose the following value from the drop down menu: barge\
        **Excel template:**\
        Input the following value into the cell: barge
      </td>
    </tr>
  </tbody>
</Table>

<Image title="R7fR3FyPsA.png" alt={1920} className="border" border={true} src="https://files.readme.io/5be092a-R7fR3FyPsA.png" />

## Create single user using Web form

* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) to know the general steps about creating single objects using Web form
* When using Web form, the information fields of a new user must be input in the following sequence to ensure no mistakes:

1. Organization Name
2. Groups
3. Username
4. Password; Re-password
5. Email
6. Phone Number
7. Full Name
8. Vehicle Type (If the user being created is a Barge captain)

<Image title="feb7696-2019-10-22_09_28_47-Window.png" alt={1674} className="border" border={true} src="https://files.readme.io/d433282-feb7696-2019-10-22_09_28_47-Window.png" />

## Create multiple users using Excel template

* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) to know the general steps about creating multiple objects using Excel template

## Update user information

* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-update-objects) to know the general steps about updating objects in Abivin vRoute

<Image title="2019-10-20 19_15_25-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/f2ab665-2019-10-20_19_15_25-Window.png" />

## Delete users

* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-delete-objects) to know the general steps about deleting objects in Abivin vRoute

<Image title="2019-10-20 19_16_00-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/154191e-2019-10-20_19_16_00-Window.png" />

## Reset user password

* If you login with the top administrator account of your organization, you can reset passwords of other users to a random password, in case those users forgot their passwords
* On the row of the users who wish to reset password, click on **Reset Password** :fa-rotate-right: symbol
* Click **OK** on the pop out message

<Image title="2019-10-20 19_14_35-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/ada3683-2019-10-20_19_14_35-Window.png" />

* The users will receive an email enclosed with the random passwords. They can use the random passwords to login to their accounts. They can decide to change the password to a new one or not
