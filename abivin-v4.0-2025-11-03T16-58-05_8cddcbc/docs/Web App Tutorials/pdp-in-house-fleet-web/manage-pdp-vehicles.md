---
title: PDP - Manage Vehicles
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
* If your organization has in-house vehicle fleet, you would need to create and manage them.\
  In PDP model, the vehicles can only be managed by organizations of ***Depot*** or ***Transporter*** types
* This article will guide you on how to manage vehicles, including:
* Create vehicles
* Update vehicle information
* Delete vehicles
* Change vehicle active status

## Create Vehicle types

* Navigate to **Transportation > Vehicle Type** tab
* Hover over the yellow :fa-plus-circle: icon, then click on **Create New Type** :fa-pencil: icon
* Input information of the vehicle type in the **Create Vehicle Type** form

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
        The Branch which manages the vehicle type being created\
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
        Palletized Time (minutes)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The time duration (In minutes) for the vehicle type being created to load products with pallet onto its trailer\
        **2. Input rules:**\
        Type only the value, do not type the unit\
        For example: The vehicle type being created takes five minutes to load products with pallet. Type this value into the field: 5
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
        (Required)
      </td>

      <td>
        **1. Description:**\
        The time duration (In minutes) for the vehicle type being created to load products without pallet onto its trailer\
        **2. Input rules:**\
        Type only the value, do not type the unit\
        For example: The vehicle type being created takes five minutes to load products without pallet. Type this value into the field: 5
      </td>
    </tr>
  </tbody>
</Table>

## Locate vehicle list

* Navigate to **Transportation > Vehicle List** tab
* To search for the list of vehicles managed by a specific Depot/Sun/Transporter, click on the **Organization** field, type the ***Organization Name*** of the Depot/Sun/Transporter into the search bar, then select from the drop down menu
* The list of the vehicles under that Depot/Sun/Transporter's management will show up

## Create vehicles

## Create single vehicle using Web form

* Please refer to the [**CRUD**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form

## Create multiple vehicles using Excel template

* Please refer to the [**CRUD**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template

## Vehicle information fields

* Below is the list of all vehicle information fields:

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
        Organization (Web form); Organization Code (Excel template)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The organization (Of Depot; Sun or Transporter type) which manages the vehicle being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field, type the Organization Name/Organization Code of the suitable organization into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the suitable organization which manages the vehicle being created on Web app (Under "Organization Code" column in "Organizations > Organization List" tab), then paste into this cell\
        **Note:**\
        This information can not be changed once the vehicle has been created. Therefore, please pay extra attention
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
        Vehicle Type\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Type of the vehicle being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field then choose the suitable vehicle type from the drop down menu\
        **Excel template:**\
        Copy the Vehicle Type Code of the vehicle being created on Web app (Under "Type Code"\
         column in "Transportation > Vehicle Type" tab), then paste into this cell
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
        License Plate\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        License Plate number of the vehicle being created\
        **2. Input rules:**\
        Format: Free-form\
        Must not contain spaces
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
        Vehicle Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Management code assigned to the vehicle being created\
        **2. Input rules:**\
        Maximum 15 characters\
        Letters and numbers are inputtable. Special characters (Not letters and numbers) will not be inputtable\
        Must not contain spaces
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
        Vehicle Name\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A name assigned to the vehicle being created\
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
        Temperature\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        **This information field is only used for VRP model**\
        The number of temperature levels supported by the vehicle being created\
        Read more about this configuration at this article: [**Optimize routes with Cold Chain**](https://docs.abivin.com/docs/optimize-routes-with-cold-chain)\
        **2. Input rules:**\
        **Web form:**\
        Click on the field, tick on check boxes of the supported temperature levels\
        For example, if the vehicle has two temperature zones for Frozen and Ambient products, tick on the check boxes next to those temperature levels\
        **Excel template:**\
        Type this value into the cell if the vehicle being created supports Frozen products: ***F***\
        Type this value into the cell if the vehicle being created supports Ambient products: ***A***\
        Type this value into the cell if the vehicle being created supports Chilled products: ***C***\
        Type this value into the cell if the vehicle being created supports Frozen and Ambient products: ***FA***\
        Type this value into the cell if the vehicle being created supports Frozen and Chilled products: ***FC***\
        Type this value into the cell if the vehicle being created supports Frozen, Ambient and Chilled products: ***FAC***\
        **Note when using Excel template:**\
        These values are case sensitive. You must write these exact values into the cell
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
        Temp Zone\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        **This information field is only used for VRP model**\
        The number of temperature zones available on the vehicle being created\
        **2. Input rules:**\
        Type only the value into this field, do not type the unit\
        For example, if the vehicle has two temperature zones, type this value into the field/cell: 2
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
        Volume (Web form); Capacity Volume (m3) (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum product capacity (In cubic meter - m3) that the vehicle being created can carry\
        **2. Input rules:**\
        Type only the value into this field, do not type the unit\
        For example, if the vehicle can carry maximum twelve cubic meters, type this value into the field/cell: 12
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
        Weight (Web form); Capacity Weight (kg) (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum product capacity (In kilograms - kg) that the vehicle being created can carry\
        **2. Input rules:**\
        Type only the value into this field, do not type the unit\
        For example: If the vehicle being created can carry maximum three thousand kilograms, type this value into the field/cell: 3000
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
        Gross Weight\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The total of the vehicle curb weight, combined with the product weight and driver weight\
        **2. Input rules:**\
        Type only the value into this field, do not type the unit\
        For example: If the vehicle gross weight is three thousand kilograms, type this value into the field/cell: 3000
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
        Real Weight\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The real weight of the vehicle being created, if that vehicle is of barge type\
        **2. Input rules:**\
        Type only the value into this field, do not type the unit\
        For example: If the vehicle real weight is three thousand kilograms, type this value into the field/cell: 3000
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
        Cost per km\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The total cost for the vehicle being created per one kilometer of operation\
        **2. Input rules:**\
        Type only the value into this field, do not type the unit\
        For example, if the vehicle costs two thousand dollars to operate per one kilometer, type this value into the field/cell only: 2000
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
        Fixed Cost\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The business expenses that are not dependent on the actual operation of the vehicle being created\
        **2. Input rules:**\
        Type only the value into this field, do not type the unit\
        For example, if the Fixed cost of the vehicle is five dollars, type this value into the field/cell: 5
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
        Speed\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Movement speed of the vehicle being created\
        Unit: Kilometer per hour (km/h)\
        **2. Input rules:**\
        Type only the value into this field, do not type the unit\
        For example, if the vehicle runs at thirty kilometers per hour, type this value into the field/cell: 30
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
        Start time; Stop time\
        (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        **This information field is only used for VRP model**\
        The official times of day when the vehicle being created starts and stops working

        **2. Input rules:**\
        Format: hh:mm (24 hour)\
        Type only the value into this field, do not type the unit\
        For example, if the vehicle starts working at 7:30 A.M and stops working at 8:30 P.M, type 07:30 in the "Start time" field and 20:30 in the "Stop time" field
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
        Speed\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Movement speed of the vehicle being created\
        Unit: Kilometer per hour (km/h)\
        **2. Input rules:**\
        Type only the value into this field, do not type the unit\
        For example, if the vehicle runs at thirty kilometers per hour, type this value into the field/cell: 30
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
        Pallete\
        (Web form)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum number of pallets that the vehicle being created can carry\
        **2. Input rules:**\
        Type only the value into this field, do not type the unit\
        For example: The vehicle can carry a maximum of five pallets, type this value into the field: 5
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
        Vehicle Identification Number\
        (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The unique identification code of the vehicle being created\
        **2. Input rules:**\
        Maximum 17 characters\
        Letters and numbers, except for letters I (i), O (o), and Q (q) will be inputtable (These three letters can cause confusion with 1 and 0). Special characters and spaces will also not be inputtable
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
        Vehicle Engine Number\
        (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The number printed on the engine of the vehicle\
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
        Vehicle Internal Code\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A code assigned by the management organization and can be printed out and pasted onto the vehicle being created. This code is similar to the Vehicle code in Abivin vRoute system, but is used by the organization for external management\
        **2. Input rules:**\
        Maximum 15 characters\
        Spaces will not be inputtable\
        All letters, numbers and special characters will be inputtable. Spaces will not be inputtable
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
        Vehicle Description\
        (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Short introduction of the vehicle being created\
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
        MDP\
        (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        **This information field is only used for VRP model**\
        The code assigned to the vehicle being created, to be used for Route optimization with Familiarity constraint\
        **2. Input rules:**\
        **Web form:**\
        Format: Free-form\
        Must not contain spaces\
        For example: "MDP 1" is not acceptable; "MDP\_1" is acceptable\
        Leave the cell blank if there is no MDP code assigned to the vehicle\
        **Excel template:**\
        Same format rules as on Web form\
        Leave the cell blank if there is no MDP code assigned to the vehicle\
        If the vehicle has multiple MDP codes, separate two adjacent MDP codes by a comma and a space\
        For example: MDP\_1, MDP\_2
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
        Default driver\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Choose the default driver for the vehicle being created. The default driver will perform every shipments assigned to the vehicle he has been associated with, unless the dispatcher deliberately change the driver\
        Only the drivers who share the same Vehicle Type with the vehicle being created can be chosen\
        **2. Input rules:**\
        Click on the field, then select the driver from the drop down menu
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
        Active\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The active status of the vehicle being created\
        **2. Input rules:**\
        By default, the status after the vehicle is created is Active, represented by this icon: :fa-check-square:
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
        Reserved\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Specify that the vehicle being created is currently reserved for some other tasks, therefore is inactive and can not perform any order\
        **2. Input rules:**\
        Click on that check box if the vehicle being created is being reserved for other tasks
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
        Sub-contractor\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Specify if the vehicle being created is a rental vehicle, managed by a third party transporter organization\
        **2. Input rules:**\
        If the vehicle being created is a rental vehicle, click on this check box\
        the vehicle being created is not a rental vehicle, do not click on the check box
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
        Sub-contractor Name\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        **This information field only displays after the Sub-contractor box has been checked**\
        Name of the third party transporter organization that manages the vehicle being created\
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
        Rental Cost\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        **On Web app, this information field only displays after the Sub-contractor box has been checked**\
        **On Excel template, this information field is only used for VRP model**\
        The rental cost of the vehicle being created, if it is a rental vehicle\
        **2. Input rules:**\
        Type only the value, do not type the unit\
        For example: The rental cost for the vehicle being created is five hundred dollars. Type this value into the field: 500
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
        Draught\
        (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        **This information field is only used for Freight transport - Barge model**\
        The draught level (In meter - m) of the vehicle being created, if it is of Barge type\
        **2. Input rules:**\
        Leave this cell blank
      </td>
    </tr>
  </tbody>
</Table>

## Update vehicle information

* Please refer to the [**CRUD**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Delete vehicles

* Please refer to the [**CRUD**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

## Change vehicle active status

* By default, all vehicle will be active right after being created, symbolized by a :fa-check-square-o: icon under the **Active** tab
* To change the active status of a vehicle to inactive, there are two options
* Click on the :fa-check-square-o: icon under **Active** column. That icon will change into :fa-square-o:, meaning the vehicle status has changed to **Inactive**

- Click on **Edit** :fa-pencil: icon of the vehicle. On the **Update Vehicle** form, click on **Reserved** check box. Click on the field under the **Reserved Time** text, then select the time period from the drop down calendars

* To turn the vehicle status into ***Active*** again, un-check the **Active** or **Reserved** check box 
