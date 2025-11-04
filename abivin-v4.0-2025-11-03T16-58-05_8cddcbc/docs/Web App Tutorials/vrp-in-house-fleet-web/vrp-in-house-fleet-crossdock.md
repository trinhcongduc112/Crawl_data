---
title: Crossdock
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
* Crossdock  (We can call **Xdock** for short) is a form of freight movement whereby products from a supplier or manufacturer are distributed directly to the user, with minimal or no storage time. The Xdock is like a Hub, receiving products through an inbound transportation and then transferring them across the Xdock to the outbound destination. The products usually spend less than 24 hours at the Xdock, sometimes even less than an hour
* In Abivin vRoute, the Xdock procedure consists of two phases:
* In-bound phase: A truck will carry products from the main Depot to the Xdock, then drives back to the main Depot
* Out-bound phase: Trucks or bikes will load products at the Xdock, then delivers to customers. At the end of their routes, they will come back to the Xdock

<Image title="Untitled-2.png" alt={1717} className="border" border={true} src="https://files.readme.io/cb0e0fa-Untitled-2.png" />

## Create Xdock

* Navigate to **Organizations > Organization List** tab
* The Xdock can be created similarly to other organizations
* Please refer to the **[CRUD](https://docs.abivin.com/docs/crud#section-create-objects)** article to know the general steps about creating objects in Abivin vRoute
* Below are the information fields required when creating Xdock using web form and Excel template

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
        The main Depot, from where products will be transported to the Xdock being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the Organization Name/Organization Code of the main Depot into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the main Depot on Web app, then paste into this cell\
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
        Organization code of the Xdock being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Xdock 01" is not acceptable; "Xdock\_01" is acceptable
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
        Organization name of the Xdock being created\
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
        Phone Number of the Xdock being created\
        **2. Input rules:**\
        Format: Numbers only\
        Must not contain spaces\
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
        Address of the Xdock being created\
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
        The regular time of day at which the Xdock being created officially starts working and closes\
        **2. Input rules:**\
        Format: hh:mm (24 hour format)\
        For example: The Xdock regularly starts working at 8:30 A.M and closes at 5:30 P.M every day. Input the following values into "Open Time" field and "Close Time" field correspondingly: **08:30; 17:30**
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
        Coordinate information of the Xdock being created\
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
        The minimum and maximum time period (in minute) that the Xdock being created requires every delivery vehicle when loading products at that Xdock\
        **2. Input rules:**\
        Input only the value in numbers. Do not input the unit\
        For example: The Xdock requires all vehicles to load products no less than five minutes and no longer than ten minutes. Input the following values into "Min time" field and "Max time" field correspondingly: **5; 10**
      </td>
    </tr>
  </tbody>
</Table>

## Optimize routes involving Xdock

## Object management allocation

* In order to successfully create and optimize orders of Xdock, you must have the following four objects correctly configured: **Vehicles; Drivers; Products; Customers**. The configurations are as follows:

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
        Main Depot
      </td>
    </tr>

    <tr>
      <td>
        Drivers
      </td>

      <td>
        Main Depot
      </td>
    </tr>

    <tr>
      <td>
        Products
      </td>

      <td>
        Xdock
      </td>
    </tr>

    <tr>
      <td>
        Customers
      </td>

      <td>
        Xdock
      </td>
    </tr>
  </tbody>
</Table>

## Optimize routes involving Xdock

* After the above objects have been correctly configured, you can now create orders and optimizes routes normally
* In the route plan, products in the orders will first be transported from the main Depot to the Xdock by a truck. Then, from the Xdock, the orders will be automatically assigned to the delivery vehicles to deliver to the customers

<Image title="xdock.gif" alt={1672} className="border" border={true} src="https://files.readme.io/8bc1298-xdock.gif" />

* On the Timeline panel, the Xdock is symbolized with the below icon:

<Image title="xdock.png" alt={66} className="border" border={true} src="https://files.readme.io/428ef05-xdock.png" />
