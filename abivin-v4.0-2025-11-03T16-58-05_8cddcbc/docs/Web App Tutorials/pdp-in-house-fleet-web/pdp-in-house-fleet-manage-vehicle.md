---
title: Manage Vehicles
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
* In this model, the **Depots** are actually the **Parking Garage** where the Vehicles park. Each Depot will have its own Vehicle fleet.

## Locate Vehicle List

* The Vehicles are listed on the **Transportation > Vehicles** tab

<Image title="1. List (ENG).png" alt={1920} border={true} src="https://files.readme.io/0bc6122-1._List_ENG.png">
  Illustration (English)
</Image>

<Image title="1. List (VIE).png" alt={1920} border={true} src="https://files.readme.io/3437d3c-1._List_VIE.png">
  Illustration (Vietnamese)
</Image>

* To search for the List of Vehicles managed by a specific Depot, click on the **Organization** field, input the ***Organization Name*** of the appropriate Depot into the search bar, then select from the drop-down menu
* The List of the Vehicles under that Depot's management will show up

<Image title="2. Search (ENG).png" alt={1731} border={true} src="https://files.readme.io/edce05b-2._Search_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Search (VIE).png" alt={1727} border={true} src="https://files.readme.io/2382b8f-2._Search_VIE.png">
  Illustration (Vietnamese)
</Image>

## Create Vehicles

* You have two methods to create the Vehicles: Webform and Excel import file

### Vehicle Information Fields

* Below is the list of all information fields of a Vehicle

> 📘 You don't necessarily need to input into all the information fields
>
> Apart from the information fields mentioned below, other information fields can be left blank during the creation process

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Description & Input Rules
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organization (Webform); Organization Code (Excel import file)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Depot which directly manages the Vehicle being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the Organization Name/Organization Code of the desired Depot into the search bar then select it from the drop-down menu\
        **Excel import file:**\
        Copy the Organization Code of the desired Depot on the Web app then paste it into this cell\
        **Note:**\
        The Organization Name and Organization Code can be found under the "Organization Name" and "Organization Code" columns in the "Organizations > Organization List" tab\
        This information cannot be changed once the Vehicle has been created, therefore, please pay extra attention
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Type\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Vehicle type of the vehicle being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field then choose the suitable vehicle type from the drop down menu\
        **Excel template:**\
        Copy the code of the appropriate vehicle type on Web app, then paste into this cell\
        **Note when using Excel template:**\
        The vehicle type code can be found under "Type Code" column in "Transportation > Vehicle Type" tab
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Name\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A name assigned to the vehicle being created for easier management\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        License Plate\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        License Plate number of the vehicle being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "License Plate 01" is not acceptable; "License\_Plate\_01" is acceptable
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Code\
        (Webform + Excel import file)\
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
        Temperature\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **Note: This information field is only effective in VRP - In-house Fleet Model**\
        **1. Description:**\
        The number of product temperature levels supported by the vehicle being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field, tick on check boxes of all three temperature levels: Ambient, Chilled, Frozen\
        **Excel template:**\
        Input the following value into this cell: ***FAC***
      </td>
    </tr>

    <tr>
      <td>
        Temp Zone\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **Note: This information field is only effective in VRP - In-house Fleet Model**\
        **1. Description:**\
        The number of temperature zones available on the vehicle being created\
        **2. Input rules:**\
        Input the following value into this field/cell: ***3***
      </td>
    </tr>

    <tr>
      <td>
        Volume (Web form); Capacity Volume (m3) (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum product capacity in cubic meter (m3) that the vehicle being created can carry\
        **2. Input rules:**\
        Input only the value in numbers. Do not input the unit\
        For example: The vehicle being created can carry maximum twelve cubic meters. Input the following value into this field/cell: ***12***
      </td>
    </tr>

    <tr>
      <td>
        Weight (Web form); Capacity Weight (kg) (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum product capacity in kilograms (kg) that the vehicle being created can carry\
        **2. Input rules:**\
        Input only the value in numbers. Do not input the unit\
        For example: The vehicle being created can carry maximum three thousand kilograms. Input the following value into this field/cell: ***3000***
      </td>
    </tr>

    <tr>
      <td>
        Start time; Stop time\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **Note: This information field is only effective in VRP model**\
        **1. Description:**\
        The official times of day when the vehicle being created starts and stops working\
        **2. Input rules:**\
        Format: hh:mm (24 hour)\
        Input only the value in numbers. Do not input the unit\
        For example: The vehicle starts working at 7:30 A.M and stops working at 8:30 P.M. Input the following values into the "Start time" and "Stop time" fields/cells correspondingly: ***07:30; 20:30***
      </td>
    </tr>

    <tr>
      <td>
        Lunch start time; Lunch stop time\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **Note: This information field is only effective in VRP model**\
        **1. Description:**\
        The official times of day when the driver of the vehicle being created starts and stops the lunch break\
        **2. Input rules:**\
        Format: hh:mm (24 hour)\
        Input only the value in numbers. Do not input the unit\
        For example: The lunch break starts at 12:30 A.M and stops at 1:30 P.M. Input the following values into the "Lunch start time" and "Lunch stop time" fields/cells correspondingly: ***12:30; 13:30***
      </td>
    </tr>

    <tr>
      <td>
        Speed\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Movement speed of the vehicle being created\
        Unit: Kilometer per hour (km/h)\
        **2. Input rules:**\
        Input only the value in numbers. Do not input the unit\
        For example: The vehicle runs at thirty kilometers per hour. Input the following value into this field/cell: ***30***
      </td>
    </tr>

    <tr>
      <td>
        Cost per km\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The cost for the vehicle being created per one kilometer during a delivery route\
        **2. Input rules:**\
        Input only the value in numbers. Do not input the unit\
        For example: The vehicle costs two thousand dollars to operate per one kilometer. Input the following value into this field/cell: ***2000***
      </td>
    </tr>

    <tr>
      <td>
        Fixed Cost\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The fixed cost of the vehicle being created during a delivery route, not depending on the route length\
        **2. Input rules:**\
        Input only the value in numbers. Do not input the unit\
        For example: The Fixed cost of the vehicle is two thousand dollars. Input the following value into this field/cell: ***2000***
      </td>
    </tr>

    <tr>
      <td>
        Default driver\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The default driver of the vehicle being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Select the default driver from the drop down menu\
        **Excel template:**\
        Copy the username of the appropriate driver on Web app, then paste into this cell\
        **Note:**\
        Username of the driver can be found under "Username" column in "Organizations > Organization List" tab\
        Only the drivers who are configured to have the same Vehicle Type with the vehicle being created can be chosen
      </td>
    </tr>

    <tr>
      <td>
        Active\
        (Webform)
      </td>

      <td>
        **1. Description:**\
        The active status of the vehicle being created\
        **2. Input rules:**\
        By default, the status of the vehicle is Active, represented by this icon: :fa-check-square:\
        To turn the status into Inactive, click on that icon
      </td>
    </tr>

    <tr>
      <td>
        Draught\
        (Excel import file)\
        (Optional)
      </td>

      <td>
        **This information field is only used in Freight transport - Barge model**\
        Input the following value into this cell: ***0***
      </td>
    </tr>
  </tbody>
</Table>

### Update Vehicle Information

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/system-operations#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

#### Update Single Vehicle

* Please refer to the article for detailed instruction on updating single vehicle [Update Single Vehicle](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-vehicles#update-single-vehicle)

#### Update Multiple Vehicles

* Please refer to the article for detailed instruction on updating mutiple vehicles [Update Multiple Vehicles](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-vehicles#update-multiple-vehicles)

### Export Vehicles

* Please refer to the article for detailed instruction on exporting vehicles [Export Vehicles](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-vehicles#export-vehicles)

### Delete Vehicles

* Please refer to the article for detailed instruction on deleting vehicles [Delete Vehicles](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-vehicles#delete-vehicles)

### Change Active Status of Vehicles

* Please refer to the article for detailed instruction on changing active status of vehicles [Change Active Status of Vehicles](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-vehicles#change-active-status-of-vehicle)

### Vehicle Status

* Please refer to the article for detailed instruction on viewing vehicles status [Vehicle Status](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-vehicles#vehicle-status)

### Filter Vehicles

* Please refer to the article for detailed instruction on filtering vehicles [Filter Vehicle](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-vehicles#filter-vehicles)

### Search Vehicles

* Please refer to the article for detailed instruction on searching vehicles [Search Vehicles](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-vehicles#search-vehicles)
