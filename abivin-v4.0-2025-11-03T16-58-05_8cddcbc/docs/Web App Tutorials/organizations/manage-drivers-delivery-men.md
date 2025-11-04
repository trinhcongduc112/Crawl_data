---
title: Drivers (Delivery men)
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
* Drivers are the people who operate delivery vehicles for organizations of **Depot/Sun** or **Transporter** types

## Locate driver list

* Apart from the **Organizations > User List** tab where all users, including drivers are listed, there is another dedicated tab to manage drivers: **Transportation > Driver** tab
* To search for the list of drivers managed by a specific Depot/Sun or Transporter, click on the **Organization** field, type the ***Organization Name*** of the Depot/Sun or Transporter into the search field, then select from the drop down menu
* The list of drivers (Or delivery men) will show up

<Image title="2019-10-21 23_32_28-Window.png" alt={1911} className="border" border={true} src="https://files.readme.io/8875b72-2019-10-21_23_32_28-Window.png" />

## Create Driver User group

* Navigate to **Organizations > Group List** tab
* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) to know the general steps about creating single object using web form

## Driver User group information field

* Below is the list of all information fields of a Driver User group 

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
        The Depot/Sun or Transporter which manages the Driver User group being created\
        **2. Input rules:**\
        Click on this field. Type the Organization Name or Organization Code of the Depot/Sun or Transporter into the search bar, then select from the drop down menu
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
        The management code assigned to the Driver User group being created\
        **2. Input rules:**\
        Always input this value: **DELIVERER**
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
        The name assigned to the Driver User group being created\
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
        A short description of the Driver User group being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

## Assign CRUD rights

### Driver User group of VRP model

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
        Orders
      </td>

      <td>
        Read
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2019-10-20 17_41_26-Window.png" alt={810} className="border" border={true} src="https://files.readme.io/c68e10d-2019-10-20_17_41_26-Window.png" />

### Driver User group of PDP model

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
        Longhaul orders
      </td>

      <td>
        Read
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2019-10-20 17_41_38-Window.png" alt={812} className="border" border={true} src="https://files.readme.io/40dc9e8-2019-10-20_17_41_38-Window.png" />

### Driver User group of Freight transport - Road model

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
        Customers
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Freight
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Shipment
      </td>

      <td>
        Read; Update
      </td>
    </tr>

    <tr>
      <td>
        Shipment history
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Charges
      </td>

      <td>
        Create; Read
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2019-10-24 10_14_23-Window.png" alt={604} className="border" border={true} src="https://files.readme.io/eaa7a97-2019-10-24_10_14_23-Window.png" />

### Driver User group of Freight transport - Sea Barge model (Also know as Captains)

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
        Customers
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Freight
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Shipment
      </td>

      <td>
        Read; Update
      </td>
    </tr>

    <tr>
      <td>
        Shipment history
      </td>

      <td>
        Read
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2019-10-24 10_18_01-Window.png" alt={609} className="border" border={true} src="https://files.readme.io/eb555ed-2019-10-24_10_18_01-Window.png" />

## Change active status of drivers

* By default, all drivers after being created will have the status as **Active**, represented by a :fa-check-square-o: icon - meaning they are available to perform deliveries/shipments assigned by the dispatchers
* In case some drivers are temporarily unable to perform shipments, the dispatchers can change their statuses to **Inactive** by clicking on :fa-check-square-o: icon

<Image title="2019-10-20 18_238_31-Window.png" alt={1913} className="border" border={true} src="https://files.readme.io/e853512-2019-10-20_18_238_31-Window.png" />

## Assign vehicle type to drivers

* If you forgot to specify the **Vehicle Type** of a driver during the user creation process, the status of that driver would always be **Inactive** in **Transportation > Driver** tab

<Image title="2019-10-20 18_28_31-Window.png" alt={1913} className="border" border={true} src="https://files.readme.io/28e16db-2019-10-20_18_28_31-Window.png" />

* You must specify the vehicle type of that driver following the steps below
* Click on **Edit** :fa-pencil: icon of the drivers who you need to specify the vehicle type

<Image title="2019-10-28 14_55_53-Window.png" alt={1908} className="border" border={true} src="https://files.readme.io/fd780d6-2019-10-28_14_55_53-Window.png" />

* On the **Update Driver** screen, click on **Vehicle Type** field. Select the appropriate vehicle type from the drop down menu
* Click **Update** to confirm the change

<Image title="2019-10-28 15_00_03-Window.png" alt={792} className="border" border={true} src="https://files.readme.io/7afa8db-2019-10-28_15_00_03-Window.png" />
