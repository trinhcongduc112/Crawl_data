---
title: Manage Vehicle Types
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
* In this model, you would have to create vehicle types before being able to create orders

## Locate Vehicle Type tab

* Navigate to **Transportation > Vehicle Type** tab
* This tab lists all the vehicle types managed by the **Branch** of your organization

<Image title="2019-10-21 15_28_57-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/9dbe24c-2019-10-21_15_28_57-Window.png" />

## Create Vehicle type

* Hover over the yellow :fa-plus-circle: icon, then click on **Create New Type** :fa-pencil: icon
* Input information of the vehicle type in the **Create Vehicle Type** form
* Click on **Create** to finish creating the Vehicle Type

<Image title="e268195-create_vehicle_type.gif" alt={1668} className="border" border={true} src="https://files.readme.io/05820e8-e268195-create_vehicle_type.gif" />

* Below is the list of all information fields of a Vehicle Type

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
        Organization Name of the Branch which you want to create vehicle types\
        **2. Input rules:**\
        Click on the field then choose the branch from the drop down menu
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
        Type Code\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the vehicle type being created\
        **2. Input rules:**\
        Format: Free-form\
        Must not contain spaces\
        For example: "Vehicle Type 01" is not acceptable; "Vehicle\_Type-01" is acceptable
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
        Type Name\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The name assigned to the vehicle type being created\
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
        Palletized Time (minute)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The time duration (In minutes) for the vehicle type being created to load products with pallet onto its trailer\
        **2. Input rules:**\
        Type only the value, do not type the unit\
        For example: The vehicle type being created takes five minutes to load products with pallet. Type this value into the field: 5\
        If this information is unknown, type this value into the field: 0
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
        Non-Palletized Time (minutes)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The time duration (In minutes) for the vehicle type being created to load products without pallet onto its trailer\
        **2. Input rules:**\
        Type only the value, do not type the unit\
        For example: The vehicle type being created takes five minutes to load products without pallet. Type this value into the field: 5\
        If this information is unknown, type this value into the field: 0
      </td>
    </tr>
  </tbody>
</Table>

## Map Vehicles with Vehicle types

## Map existing vehicles

* Navigate to **Transportation > Vehicle List** tab
* Filter the vehicles of the **Depots/xDocks/Sun** or **Transporter** under the Branch recently configured above
* Click on **Edit** :fa-pencil: icon of the vehicle which you want to map with the vehicle types recently created
* On the **Update Vehicle** form, click on **Vehicle Type** field, then choose the suitable vehicle type from the drop down menu
* Click **Update** to confirm the change

<Image title="992a629-assign_vehicle_type.gif" alt={1668} className="border" border={true} src="https://files.readme.io/0a00a43-992a629-assign_vehicle_type.gif" />

## Map new vehicles

* If you create new vehicles using Web app, follow the steps described above
* If you create new vehicles using Excel template, copy the code of the appropriate vehicle type on Web app, then paste into **Vehicle Type** cell
* The code of the Vehicle Type can be found under **Type Code** column in **Transportation > Vehicle Type** tab
