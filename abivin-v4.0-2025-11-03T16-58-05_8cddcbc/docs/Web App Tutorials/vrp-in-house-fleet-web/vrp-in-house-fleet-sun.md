---
title: Sun Warehouse
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
* The Sun warehouse is considered the second-level warehouse, directly below the Depot. Products from the main Depotare transported to Sun, and from the Sun warehouse they will be distributed to the Sun warehouse's Customer base

<Image title="Untitled Diagram (3).png" alt={121} className="border" border={true} src="https://files.readme.io/22b8876-Untitled_Diagram_3.png" />

## Create Sun

* Navigate to **Organizations > Organization List** tab
* The Sun organization can be created similarly to other organizations
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-create-objects) article to know the general steps about creating objects in Abivin vRoute
* Below are the required information fields when creating Sun using web form and Excel template

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
        Parent Organization (Web form); Parent Organization Code (Excel template)
      </td>

      <td>
        **1. Description:**\
        The main Depot, from which products will be transported to the Sun being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the Organization Name/Organization Code of the main Depot into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization code of the main Depot on Web app, then paste into this cell\
        **Note:**\
        The Organization Name and Organization Code can be found under "Organization Name" and "Organization Code" columns in "Organizations > Organization List" tab
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
        Organization Code\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        Organization code of the Sun being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Sun 01" is not acceptable; "Sun\_01" is acceptable
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
        Organization Name\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        Organization name of the Sun being created\
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
        Phone Number\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        Phone Number of the Sun being created\
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
        Address\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        Address of the Sun being created\
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
        Open Time; Close Time\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        The regular time of day at which the Sun being created officially starts working and closes\
        **2. Input rules:**\
        Format: hh:mm (24 hour format)\
        For example: The Sun regularly starts working at 8:30 A.M and closes at 5:30 P.M every day. Input the following values into "Open Time" field and "Close Time" field correspondingly: **08:30; 17:30**
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
        Latitude; Longitude\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        Coordinate information of the Sun being created\
        **2. Input rules:**\
        Format: Decimal degrees\
        For example: 41.40338 and 2.17403\
        Please refer to this article to get instruction: [**Get coordinates of places**](https://docs.abivin.com/docs/how-to-get-coordinates-of-places)
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
        Min time; Max time\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        The minimum and maximum time period (in minute) that the Sun being created requires every delivery vehicle when loading products at that Sun\
        **2. Input rules:**\
        Input only the value in numbers. Do not input the unit\
        For example: The Sun requires all vehicles to load products no less than five minutes and no longer than ten minutes. Input the following values into "Min time" field and "Max time" field correspondingly: **5; 10**
      </td>
    </tr>
  </tbody>
</Table>

## Route Plan Optimization For Sun Warehouse

## Object management allocation

* In order to successfully create and optimize orders of Sun, you must have the following four objects correctly configured: **Vehicles; Drivers; Products; Customers**. The configurations are as follows:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Object
      </th>

      <th>
        Direct management organization
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Vehicles
      </td>

      <td>
        Sun
      </td>
    </tr>

    <tr>
      <td>
        Drivers
      </td>

      <td>
        Sun
      </td>
    </tr>

    <tr>
      <td>
        Products
      </td>

      <td>
        Sun
      </td>
    </tr>

    <tr>
      <td>
        Customers
      </td>

      <td>
        Sun
      </td>
    </tr>
  </tbody>
</Table>

## Create routes involving Sun

* After the above objects have been correctly configured, you can now create orders and optimizes routes normally
* On the Optimization map, the Sun icon is a green location mark :fa-map-marker:
* Similar to Depot, the delivery vehicles will load products at Sun, deliver to customer, then travel back to the Sun and end their delivery routes

<Image title="Sun-route.png" alt={1362} className="border" border={true} src="https://files.readme.io/a80d6a5-Sun-route.png" />
