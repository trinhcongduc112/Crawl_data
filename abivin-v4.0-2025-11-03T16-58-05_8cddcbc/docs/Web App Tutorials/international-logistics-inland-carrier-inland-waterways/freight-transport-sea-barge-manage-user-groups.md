---
title: Manage User groups
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
* Within each organization, you can create multiple **User groups**. User groups are separate groups of personnel that are assigned different rights according to their roles in the organization

## Locate User groups list

* Navigate to **Organizations > Group List** tab
* This tab lists the User groups in which the you belong, or have the rights to view. If you are the top administrator user, you will be able to view all the user groups you are managing

<Image title="2019-10-21 23_07_55-Window.png" alt={1891} className="border" border={true} src="https://files.readme.io/0cb6b59-2019-10-21_23_07_55-Window.png" />

## Create User group

## User group basic information fields

* A User group will have these basic information fields:

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
        Organizations
        (Required)
      </td>

      <td>
        **1. Description:**\
        The organization which manages the user group being created\
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
        If the User group being created is Barge captain User group, input the following value into this field (Note: All letters must be uppercase): DELIVERER
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

<Image title="2019-10-21 23_10_28-Window.png" alt={1890} className="border" border={true} src="https://files.readme.io/b3fea57-2019-10-21_23_10_28-Window.png" />

* For this model, essentially you need to have two User groups: ***Administrator User group*** and ***Barge captain User group***
* You would notice that the **Administrator User groups** have been automatically created for each of the available organization
* If you created the **Transporter** organization using Web form, the **Barge captain User group**, with the User group code ***DELIVERER*** would also have been created automatically

- If you created the **Transporter** organization using Excel template, the Barge captain User group would not have been created automatically. You  have to create that User group using Web form
- Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form

## Assign rights to User groups

* Below the basic information fields is the CRUD table, where you can assign roles and rights for a User group

## Administrator User group

* Below are the rights you should assign to the Administrator User group

<Image title="barge admin.png" alt={827} className="border" border={true} src="https://files.readme.io/4b2fde6-barge_admin.png" />

## Barge captain User group

* Below are the rights you should assign to the Barge captain User group

<Image title="barge captain.png" alt={815} className="border" border={true} src="https://files.readme.io/90ae3fe-barge_captain.png" />
