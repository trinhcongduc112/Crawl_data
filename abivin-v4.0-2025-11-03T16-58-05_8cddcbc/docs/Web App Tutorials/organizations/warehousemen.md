---
title: Warehouse Men
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
## Create Warehousemen User group

## Warehousemen User group information field

* Below is the list of all information fields of a Warehousemen User group 

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
        The Depot which manages the Warehousemen User group being created\
        **2. Input rules:**\
        Click on this field. Type the Organization Name or Organization Code of the Depot into the search bar, then select from the drop down menu
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
        Group Code\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the Warehousemen User group being created\
        **2. Input rules:**\
        Always input this value: **WAREHOUSEMEN**
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
        Group Name\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The name assigned to the Warehousemen User group being created\
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
        A short description of the Warehousemen User group being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

## Create Warehousemen User group automatically

* Navigate to **Organizations > Organization List** tab
* Click on **Edit** :fa-pencil: icon of the ***Manufacturer***

<Image title="2019-10-23 14_54_48-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/aba0776-2019-10-23_14_54_48-Window.png" />

* On the **Organization Information** screen, click on **Transport Service By** field, choose ***Transporter*** from the drop down menu

<Image title="2019-10-23 14_55_39-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/8f0e427-2019-10-23_14_55_39-Window.png" />

* Click **Save** to confirm the change
* From now on, the Warehousemen User group will automatically be created for every organizations of ***Depot*** type after those Depots have been created using Excel template

<Image title="2019-10-23 14_56_14-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/2cdb2b5-2019-10-23_14_56_14-Window.png" />

## Create Warehousemen User group manually

* Navigate to **Organizations > Group List** tab
* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) to know the general steps about creating single object using web form

<Image title="2019-10-23 15_22_08-Window.png" alt={1663} className="border" border={true} src="https://files.readme.io/a8af932-2019-10-23_15_22_08-Window.png" />

## Assign CRUD rights

* A Warehousemen User group will have the below CRUD rights

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Module
      </th>

      <th>
        Rights assigned
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
        Read; Update
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
        Longhaul Orders
      </td>

      <td>
        Read
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2019-10-23 15_20_19-Window.png" alt={694} className="border" border={true} src="https://files.readme.io/0663c6e-2019-10-23_15_20_19-Window.png" />

## Allocate Users into Warehousemen User group

## Allocate existing users

* You could allocate existing users of a ***Depot*** into the Warehousemen User group recently created by doing the following steps:
* Navigate to **Organizations > User List** tab
* Filter out the users of the Depot which you want to allocate, then click on **Edit** :fa-pencil: icon of those users
* On the **User Information** screen, click on the **Groups** field. Type the text ***Warehouse*** in the search bar to filter the Warehousemen User group, then select that group from the drop down menu
* Click **Save** to confirm the change

<Image title="2019-10-20 20_10_34-Window.png" alt={1915} className="border" border={true} src="https://files.readme.io/6807bb2-2019-10-20_20_10_34-Window.png" />

## Allocate new users

* If you create new warehousemen users using Web form, follow the steps described above
* If you create new warehousemen users using Excel template, you need to pay attention to the following things:
* Make sure the value in the **Organization Code** cell is the Organization Code of the ***Depot*** in which the warehousemen being created belong
* Input the text ***WAREHOUSEMEN*** into the **User Group Code** cell
* Repeat these steps for other warehousemen users

<Image title="2019-10-23 15_29_13-Window.png" alt={1498} className="border" border={true} src="https://files.readme.io/1231ecd-2019-10-23_15_29_13-Window.png" />

## Stop generating tasks for depots of suppliers

* If a Depot belongs to your supplier, not your organization, you could enable a configuration to stop generating tasks for warehousemen users of that Depot
* Navigate to **Organizations > Organization List** tab
* Click on **Edit** :fa-pencil: icon of the ***Depots*** which you want to stop generating tasks for the warehousemen users

<Image title="2019-10-29 16_25_36-Window.png" alt={1907} className="border" border={true} src="https://files.readme.io/dd7c89d-2019-10-29_16_25_36-Window.png" />

* On the **Organization Information** screen, click on **Supplier's Depot** check box
* Click **Save** to confirm the change

<Image title="2019-10-29 16_27_07-Window.png" alt={1907} className="border" border={true} src="https://files.readme.io/2563421-2019-10-29_16_27_07-Window.png" />

* From now on,  tasks for the warehousemen users of these depots will not be generated on Mobile app
