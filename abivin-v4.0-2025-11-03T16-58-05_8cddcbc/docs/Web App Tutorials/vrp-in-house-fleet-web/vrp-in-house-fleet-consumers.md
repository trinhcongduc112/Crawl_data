---
title: Consumers
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: link
      title: Consumer Orders Approval Process on Web app
      url: >-
        https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#section-salesmen-consumer-orders
    - type: link
      title: Consumer App - General Instruction
      url: https://docs.abivin.com/docs/consumer-app-general-instruction
---
* Consumers are the end users, who will ultimately consume the products manufactured by your organizations. When they have demand for certain products, they will actively place orders. After that, the dispatchers of your organization will assign delivery tasks to the Drivers (Deliverymen)
* In this article we will find out how to:
* Create Consumers User group
* Allocate Users into Consumers User group

## Create Consumers User group

* Navigate to **Organizations > Group List** tab
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form

## Consumer User group information field

* Below is the list of all information fields of a Consumer User group 

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
        The Organization which manages the Consumers User group being created\
        **2. Input rules:**\
        Click on this field. Input the Organization Name or Organization Code of the appropriate Organization into the search bar, then select from the drop down menu\
        Organization Name and Organization Code can be found under columns of the same name on tab Organizations > Organization List
      </td>
    </tr>

    <tr>
      <td>
        Group Code\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the Consumers User group being created\
        **2. Input rules:**\
        Always input this value: **CONSUMER**
      </td>
    </tr>

    <tr>
      <td>
        Group Name\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The name assigned to the Consumers User group being created\
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
        A short description of the Consumers User group being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

## Assign CRUD rights

## Allocate Users into Consumers User group

> 👍 The consumers can deliberately sign up on their Consumer Mobile app. Upon finishing the sign up process, their user accounts will automatically be added to the Consumer User group of the Manufacturer

## Allocate existing users

* You could allocate existing users of a into the Consumers User group recently created by doing the following steps:
* Navigate to **Organizations > User List** tab
* Click on **Edit** :fa-pencil: icon of the users
* On the **User Information** screen, click on the **Groups** field. Type the text ***CONSUMER*** in the search bar to filter the Consumers User group, then select that group from the drop down menu
* Click **Save** to confirm the change

## Allocate new users

* If you create new consumers users using Web form, follow the steps described above
* If you create new consumers users using Excel template, make sure to input the text ***CONSUMER*** into the **User Group Code** cell
