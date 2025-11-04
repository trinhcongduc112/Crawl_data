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
  pages:
    - type: link
      title: Manage Customers
      url: https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers
---
* In this model, each warehouse (Of Depot and Sun type, not Crossdock type) will have its own delivery fleet. By default, there are three Vehicle Types: **Truck; Semi-truck; Motorbike**
* Apart from the three default Vehicle Types, you can also create and manage custom Vehicle Types

## Locate Vehicle List

* The Vehicles are listed on the **Transportation > Vehicles** tab

<Image title="2019-10-22 15_03_44-Window.png" alt={1671} className="border" border={true} src="https://files.readme.io/f03839a-2019-10-22_15_03_44-Window.png" />

## Create Vehicles

* You have two methods to create the Vehicles:
* Method 1: Create single Vehicles via Webform
* Method 2: Create multiple Vehicles via Excel import file

### Vehicle information fields

* Below is the list of all information fields for vehicles of this model:

> 📘 Apart from the information fields mentioned below, other information fields can be left blank

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
        Organization (Webform); Organization Code (Excel import file)
        (Required Field)
      </td>

      <td>
        **1. Description:**\
        The Organization (Of Depot or Sun type) which directly manages the Vehicle being created\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Input the Organization Name/Organization Code of the appropriate Depot/Sun into the search bar, then select from the drop-down menu\
        **Excel import file:**\
        Copy the Organization Code of the appropriate Depot or Sun on the Web app then paste it into this cell\
        **Note:**\
        The Organization Name and Organization Code can be found under the "Organization Name" and "Organization Code" columns in the "Organizations > Organizations" tab\
        This information can not be changed once the vehicle has been created. Therefore, please pay extra attention
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
        The Vehicle Type of the Vehicle being created\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. On the drop-down list, select the appropriate Vehicle Type only from the three following types: bike; truck; semi-truck. Do not select any other type as they are not used in this model\
        **Excel import file:**\
        Input only one of the following three values into the cell (Input only the English values as shown, not in any other language): ***bike; truck; semi-truck***\
        These values represent the following default Vehicle Types of this model: Motorbike; Truck; Semi-truck\
        **Note when using the Excel import file:**\
        Do not input values that include uppercase letters into this cell, for example, ***Bike; TRUCK***\
        If you use the Flexible Vehicle Type configuration and have created the custom Vehicle Types, copy the Vehicle Type Code of the appropriate Vehicle Type on the Web app and paste it into this cell\
        The Vehicle Type Code can be found under the "Type Code" column in the "Transportation > Vehicle Type" tab\
        Read more about the Flexible Vehicle Type configuration in the following article:
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
        The management code assigned to the Vehicle being created\
        **2. Input rules:**\
        Length: Maximum 15 characters\
        Can contain letters, numbers. Must not contain special characters and spaces
      </td>
    </tr>

    <tr>
      <td>
        Start time; Stop time\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The official times of day when the Vehicle being created starts and stops working\
        These attributes will be used during the Route Plan optimization process\
        **2. Input rules:**\
        Format: HH:mm (24-hour format)\
        For example, the Vehicle being created starts working at 07:30 A.M and stops working at 08:30 P.M. Input the following values into the "Start time" and "Stop time" fields/cells, respectively: ***07:30; 20:30***\
        **Special Note:**\
        If the Vehicle being created is usually assigned Delivery Routes that need more than 24 hours to perform, the value input into the "Stop time" field/cell should be larger than the sum of the "Start time" value and the approximate time to perform those Delivery Routes\
        For example, the Vehicle being created starts working at 06:30 A.M. It is often assigned Delivery Routes that take more than 72 hours to perform. In this case, the value input into the "Stop time" field/cell should be larger than the sum of the above values, which is ***78:30***\
        On the Webform, if you leave these fields blank, upon saving the system will automatically fill the following values into these fields correspondingly: ***07:00; 18:00***
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
        The license plate number of the vehicle being created\
        **2. Input rules:**\
        Can contain letters and numbers. Cannot contain special characters (Characters that are not letters and numbers) and spaces
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
        A name assigned to the vehicle being created for easier management\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Temperature\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The product temperature levels that the vehicle being created can carry\
        Read more about this configuration at the following article: [**Cold Chain**](https://docs.abivin.com/docs/vrp-in-house-fleet-cold-chain)\
        **2. Input rules:**\
        **Web form:**\
        Click on this field, tick on check boxes of the supported temperature levels\
        For example: The vehicle being created can carry Frozen and Ambient products. Tick on the following check boxes: Frozen; Ambient\
        **Excel template:**\
        Input only one of these six values into the cell to specify the temperature levels supported by the vehicle being created: ***F; A; C; FA; FC; FAC***\
        The letters F; A; C represents the following temperature levels respectively: ***Frozen; Ambient; Chilled***\
        **Notes:**\
        On Web form, if you leave this field blank, upon saving the system will automatically choose the following checkbox: ***Ambient***
      </td>
    </tr>

    <tr>
      <td>
        Temp Zone\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The number of temperature zones available on the vehicle being created\
        Read more about this configuration at this article: [**Optimize routes with Cold Chain**](https://docs.abivin.com/docs/optimize-routes-with-cold-chain)\
        **2. Input rules:**\
        Input only the value in numbers. Do not input the unit\
        For example: The vehicle being created has two temperature zones in its cargo area. Input the following value into the field/cell: ***2***\
        **Note:**\
        The number of temperature zones available on a vehicle can be less than the number of temperature levels supported by that vehicle\
        For example: A vehicle has only one specialized temperature zone for Frozen product, but can still carry Ambient and Chilled products\
        On Web form, if you leave this field blank, upon saving the system will automatically fill the following value into this field: ***1***
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
        For example: The vehicle being created can carry maximum twelve cubic meters. Input the following value into the field/cell: ***12***\
        **Notes:**\
        On Web form, if you leave this field blank, upon saving the system will automatically fill the following value into this field: ***3***
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
        Input the value in numbers. Do not input the unit\
        For example: The vehicle being created can carry maximum three thousand kilograms. Input the following value into the field/cell: ***3000***\
        **Notes:**\
        On Web form, if you leave this field blank, upon saving the system will automatically fill the following value into this field: ***1500***
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
        The total weight of the vehicle, including all the components of the vehicle, the weight of the driver, product, fuel, and other things\
        This field is used for Road constraint by Gross weight. Read more about this configuration at the following article: [***Road Constraints***](https://docs.abivin.com/docs/vrp-in-house-fleet-road-constraints)\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The vehicle gross weight is three thousand kilograms. Input the following value into the field/cell: ***3000***
      </td>
    </tr>

    <tr>
      <td>
        Real Weight\
        (Web form)\
        (Optional)
      </td>

      <td>
        **This field is only used for Freight transport models**
      </td>
    </tr>

    <tr>
      <td>
        Cargo Area Length (m)\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Length of the cargo area of the vehicle being created\
        **2. Input rules:**\
        Format: Meter (m)\
        Input only the value in numbers. Do not input the unit\
        For example: The vehicle being created has the cargo area's length to be four point five metres. Input the following value into this field/cell: ***4.5***\
        If you do not have data of this field, just leave the field/cell blank\
        **Note:**\
        If the configuration "Oversized Goods Restriction" of the Manufacturer is enabled, this field/cell will become required, and the value input must be larger than 0
      </td>
    </tr>

    <tr>
      <td>
        Cargo Area Width (m)\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Width of the cargo area of the vehicle being created\
        **2. Input rules:**\
        Format: Meter (m)\
        Input only the value in numbers. Do not input the unit\
        For example: The vehicle being created has the cargo area's width to be four point five metres. Input the following value into this field/cell: ***4.5***\
        If you do not have data of this field, just leave the field/cell blank\
        **Note:**\
        If the configuration "Oversized Goods Restriction" of the Manufacturer is enabled, this field/cell will become required, and the value input must be larger than 0
      </td>
    </tr>

    <tr>
      <td>
        Cargo Area Height (m)\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Height of the cargo area of the vehicle being created\
        **2. Input rules:**\
        Format: Meter (m)\
        Input only the value in numbers. Do not input the unit\
        For example: The vehicle being created has the cargo area's height to be four point five metres. Input the following value into this field/cell: ***4.5***\
        If you do not have data of this field, just leave the field/cell blank\
        **Note:**\
        If the configuration "Oversized Goods Restriction" of the Manufacturer is enabled, this field/cell will become required, and the value input must be larger than 0
      </td>
    </tr>

    <tr>
      <td>
        Lunch start time; Lunch stop time\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The official times of day when the driver of the vehicle being created starts and stops the lunch break\
        **2. Input rules:**\
        Format: hh:mm (24 hour)\
        Input the value in numbers. Do not input the unit\
        For example: The lunch break starts at 12:30 A.M and stops at 1:30 P.M. Input the following values into the "Lunch start time" and "Lunch stop time" fields/cells correspondingly: ***12:30; 13:30***\
        **Notes:**\
        On Web form, if you leave these fields blank, upon saving the system will automatically fill the following value into these fields: ***12:00***
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
        Input the value in numbers. Do not input the unit\
        For example: The vehicle being created runs at thirty kilometers per hour. Input the following value into the field/cell: ***30***\
        **Notes:**\
        On Web form, if you leave this field blank, upon saving the system will automatically fill the following value into this field: ***40***
      </td>
    </tr>

    <tr>
      <td>
        Cost per km\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The cost for the vehicle being created per one kilometer during a delivery route\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The vehicle costs two thousand dollars to operate per one kilometer. Input the following value into the field/cell: ***2000***\
        **Notes:**\
        On Web form, if you leave this field blank, upon saving the system will automatically fill the following value into this field: ***0***
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
        The fixed cost of the vehicle being created during a delivery route, not depending on the route length\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The Fixed cost of the vehicle is two thousand dollars. Input the following value into the field/cell: ***2000***\
        **Notes:**\
        On Web form, if you leave this field blank, upon saving the system will automatically fill the following value into this field: ***0***
      </td>
    </tr>

    <tr>
      <td>
        Rental Cost\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The expense your organization have to pay a Subcontractor to rent the vehicle being created for a whole delivery route\
        Read more about this configuration at the following article:\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The Rental cost of the vehicle is five hundred dollars. Input the following value into the field/cell: ***500***\
        If the vehicle being created is not a rental vehicle, leave this field/cell blank\
        **Notes:**\
        On Web form, if you leave this field blank, upon saving the system will automatically fill the following value into this field: ***0***
      </td>
    </tr>

    <tr>
      <td>
        MDP\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The code assigned to the vehicle being created, to be used for Route optimization with Familiarity constraint\
        Read more about this configuration at the following article: [**Familiarity Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-familiarity-constraint)\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "MDP 1" is not acceptable; "MDP\_1" is acceptable\
        Leave the cell blank if there is no MDP code assigned to the vehicle\
        If the vehicle is assigned multiple MDP codes, separate two adjacent MDP codes by a comma and a space\
        For example: ***MDP\_1, MDP\_2***
      </td>
    </tr>

    <tr>
      <td>
        Maximum Single Order Volume (m3)\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The maximum volume per single Order that the vehicle allows\
        Unit: Cubic meter (m3)\
        Read more in the following article: [**Vehicle Capacity Constraint**](https://docs.abivin.com/docs/vrp-dc-vehicle-capacity-constraint)\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example, the vehicle only allows the maximum volume per single Order to be zero point six cubic meters. Input the following value into this field: ***0.6***\
        **Note:**\
        If you leave this field blank, the system will assume that the maximum volume per single Order that the vehicle allows equals to the total volume capacity of that vehicle, which is the value of the "Volume (m3)" field
      </td>
    </tr>

    <tr>
      <td>
        Maximum Single Order Weight (kg)\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The maximum weight per single Order that the vehicle allows\
        Read more in the following article: [**Vehicle Capacity Constraint**](https://docs.abivin.com/docs/vrp-dc-vehicle-capacity-constraint)\
        Unit: Kilogram (kg)\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example, the vehicle only allows the maximum weight per single Order to be six kilograms. Input the following value into this field: ***6***\
        **Note:**\
        If you leave this field blank, the system will assume that the maximum weight per single Order that the vehicle allows equals to the total weight capacity of that vehicle, which is the value of the "Weight (kg)" field
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
        The default driver of the vehicle being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Select the default driver from the drop down menu\
        **Excel template:**\
        Copy the Username of the appropriate driver on Web app, then paste into this cell\
        **Note:**\
        Username of the driver can be found under "Username" column in "Organizations > Organization List" tab\
        **Note:**\
        You can set one single driver to be the default driver for multiple vehicles\
        Only the drivers who are configured to have the same Vehicle Type attribute with the vehicle being created can be set as the default driver for that vehicle\
        For example: If a driver is configured to have the "Vehicle Type" attribute to be "bike", then you will only be able to select him as the default driver for a vehicle of "bike" type but not for a vehicle of "truck/semi-truck" types
      </td>
    </tr>

    <tr>
      <td>
        Accompanied vehicle\
        (Web form)\
        (Optional)
      </td>

      <td>
        **Note: This configuration applies only to the vehicles of this type: truck**\
        **1. Description:**\
        The motorbikes that will accompany the truck being created to deliver orders\
        **2. Input rules:**\
        Click on the field, then select the motorbike(s) from the drop down menu\
        Read more about this feature at this article: [**Accompanied Vehicles**](https://docs.abivin.com/docs/vrp-in-house-fleet-accompanied-vehicles)
      </td>
    </tr>

    <tr>
      <td>
        Registration Date\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The date when the registration certificate of the vehicle being created is deemed expired\
        **2. Input rules:**\
        Click on the field, choose the suitable date from the drop down calendar
      </td>
    </tr>

    <tr>
      <td>
        Active\
        (Web form)
      </td>

      <td>
        **1. Description:**\
        The active status of the vehicle being created\
        **2. Input rules:**\
        By default, the status of the vehicle is Active, represented by this icon: :fa-check-square:\
        To turn the status into Inactive, click on that icon
      </td>
    </tr>
  </tbody>
</Table>

## Update vehicle information

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Update single vehicle

* To update single vehicle, click on **Edit** icon :fa-pencil: of that vehicle

<Image title="2019-10-22 22_11_14-Window.png" alt={1915} className="border" border={true} src="https://files.readme.io/dfe5a85-2019-10-22_22_11_14-Window.png" />

## Update multiple vehicles

* You can update multiple vehicles using Excel template. The process is similar to when you create multiple vehicles using Excel template. Just change the information in the exact Excel template you used earlier to create the vehicles (**Important note**: The attributes ***Organization Code*** and ***Vehicle Code*** of the existing vehicles must remain the same), then, as you upload the updated Excel template, click on the check box **Overwriting existing data**

<Image title="Image 2.png" alt={590} className="border" border={true} src="https://files.readme.io/bf3be85-Image_2.png" />

## Export Vehicles

### Compulsory Configuration

* Before being able to export vehicle, you need to tick the check box **Export** of the module **Vehicle** for the User group in which your User account belongs

- To export vehicle, navigate to the tab **Transportation > Vehicles**. On this tab, hover over the icon :fa-plus-circle:, then click the icon **Export Data** :fa-download:. The vehicles will be downloaded as an Excel spreadsheet that you can view offline

## Delete vehicles

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute
* You can only delete vehicles which have the Vehicle Status to be ***Open***, not ***Planned/Locked***

<Image title="2019-10-22 22_11_37-Window.png" alt={1915} className="border" border={true} src="https://files.readme.io/54a6a34-2019-10-22_22_11_37-Window.png" />

## Change Active status of vehicle

* By default, all vehicles will have their status as ***active*** right after being created, symbolized by a :fa-check-square-o: icon under the **Active** tab
* If one or more vehicles have the **Vehicle status** to be ***Open*** - Meaning they are currently not assigned any delivery task, then you can change the active status of them
* First you have to select the vehicles by clicking on the corresponding check box icon :fa-square-o: of those vehicles on the first column of the vehicle list. You can also select all vehicles ***currently displayed on the page*** by clicking on the check box icon :fa-square-o: on the title bar above the vehicle list
* After you have selected the vehicles, click on the button **Bulk Updates**, then click on the text **Update Vehicles' active status**. The form **Vehicle Active Status Update** will appear. On that form, select the appropriate value (***Active*** or ***Inactive***) then click **OK**. Click **OK** one more time on the confirmation form

<Image title="update vehicle status.gif" alt={1912} className="border" border={true} src="https://files.readme.io/3118635-update_vehicle_status.gif" />

## Bulk Update Start Time & Stop Time of Vehicles

* You can change the attributes **Start Time** and **Stop Time** of multiple vehicles. First, follow the instruction for changing vehicle active status above to select multiple vehicles. Upon clicking on **Bulk Updates** button, click on **Update Vehicles' Start time** and **Update Vehicles' Stop time**, respectively. The form **Bulk updating vehicles' start time/Bulk updating vehicles' stop time** will appear. Input the desired Start Time/Stop Time into the field, then click **OK** to confirm changing

<Image title="Image 3.png" alt={590} className="border" border={true} src="https://files.readme.io/1d8aad3-Image_3.png" />

## Setup vehicles as Sub-contractor's

* During the creation/editing process on both Web form and Excel template, you can setup the vehicles as Sub-contractor's
* On Web form, first you need to click on the check box **Sub-contractor**. Upon clicking on that check box, three new information fields will appear right below

<Image title="vhc.png" alt={785} className="border" border={true} src="https://files.readme.io/ebd5852-vhc.png" />

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Sub-contractor information fields
      </th>

      <th>
        Description & Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Sub-contractor Name
      </td>

      <td>
        **1. Description:**\
        Name of the Sub-contractor\
        **2. Input rules:**\
        Format: Text and numbers
      </td>
    </tr>

    <tr>
      <td>
        Sub-contractor Code
      </td>

      <td>
        **1. Description:**\
        Code of the Sub-contractor\
        **2. Input rules:**\
        Format: Text and numbers, must not contain spaces\
        For example: "Contractor 01" is invalid;  "Contractor\_01" is valid
      </td>
    </tr>

    <tr>
      <td>
        Rental Cost
      </td>

      <td>
        **1. Description:**\
        Rental cost of the vehicle per route\
        Note: This is a fixed cost, regardless of the route length\
        **2. Input rules:**\
        Format: Numbers only\
        For example: The rental cost of the vehicle is five million Vietnam dong per route. Input the following value into this field: ***5000000***
      </td>
    </tr>
  </tbody>
</Table>

## Vehicle Status

* Below are the possible vehicle statuses in accordance with the Route Plan Optimization Process

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Vehicle Status
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Open
      </td>

      <td>
        The vehicle has not been assigned any Delivery Route, or the current time point has passed the estimated finish time of the Delivery Route assigned to the vehicle
      </td>
    </tr>

    <tr>
      <td>
        Planned
      </td>

      <td>
        The vehicle has been assigned a Delivery Route, but the Delivery Route has not yet been locked
      </td>
    </tr>

    <tr>
      <td>
        Locked
      </td>

      <td>
        The Delivery Route assigned to the vehicle has been locked or finalized
      </td>
    </tr>
  </tbody>
</Table>

* You can filter the vehicles having certain statuses by clicking on this field title then tick the appropriate checkboxes

- The vehicle status of a vehicle will update accordingly to every user or system activity related to that vehicle. The table below lists all possible vehicle status changes

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        User/System Activity
      </th>

      <th>
        Vehicle Status (Before)
      </th>

      <th>
        Vehicle Status (After)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Create vehicle
      </td>

      <td>
        None
      </td>

      <td>
        Open
      </td>
    </tr>

    <tr>
      <td>
        Delete vehicle
      </td>

      <td>
        Open
      </td>

      <td>
        None
      </td>
    </tr>

    <tr>
      <td>
        Vehicle is put into a Route Plan
      </td>

      <td>
        Open\
        Planned
      </td>

      <td>
        Planned
      </td>
    </tr>

    <tr>
      <td>
        The assigned planned Delivery Route is locked
      </td>

      <td>
        Planned
      </td>

      <td>
        Locked
      </td>
    </tr>

    <tr>
      <td>
        The assigned locked Delivery Route is unlocked
      </td>

      <td>
        Locked
      </td>

      <td>
        Planned
      </td>
    </tr>

    <tr>
      <td>
        The current time point has passed the estimated finish time point of the assigned Delivery Route
      </td>

      <td>
        Locked
      </td>

      <td>
        Open
      </td>
    </tr>

    <tr>
      <td>
        The driver submits the last task of the assigned Delivery Route ("End of Day" task)
      </td>

      <td>
        Locked
      </td>

      <td>
        Open
      </td>
    </tr>

    <tr>
      <td>
        The assigned Delivery Route is assigned to another vehicle (Change vehicle)
      </td>

      <td>
        Planned
      </td>

      <td>
        Open
      </td>
    </tr>

    <tr>
      <td>
        The assigned Delivery Route is moved to other vehicles or is removed from the Route Plan
      </td>

      <td>
        Planned
      </td>

      <td>
        Open
      </td>
    </tr>

    <tr>
      <td>
        The assigned Delivery Route is manually closed
      </td>

      <td>
        Locked
      </td>

      <td>
        Open
      </td>
    </tr>

    <tr>
      <td>
        External TMS returns the assigned Delivery Route result as Finished
      </td>

      <td>
        Locked
      </td>

      <td>
        Open
      </td>
    </tr>
  </tbody>
</Table>

## Filter Vehicles

## Filter by Vehicle Type

* To filter vehicles by vehicle type, follow the steps below:
* Step 1: Click on the **Type** column title
* Step 2: Upon clicking, a drop-down list will appear. On this list, tick the checkboxes of the wanted vehicle types. Alternatively, you can input the **Type Code/Type Name** attribute of the vehicle type into the search bar to filter faster
* After the vehicle types have been selected, the system will refresh the vehicle list and show the vehicles of the selected vehicle types

<Image title="filter vehicle type.gif" alt={1692} className="border" border={true} src="https://files.readme.io/ec690b6-filter_vehicle_type.gif" />

## Search Vehicles

* You can search for a single vehicle or multiple vehicles at once

## Search single vehicle

* To search for a single vehicle, first, make sure the textbox to the left of the search box displays ***Single***. If this textbox displays ***Multiple***, click on this textbox and select the Single text on the drop-down list

<Image title="3Qa5rggtGF.png" alt={423} className="border" border={true} src="https://files.readme.io/add127b-3Qa5rggtGF.png" />

* After that, input the Vehicle Code or License Plate of the vehicle you want to search into the search box. The system will return that vehicle

<Image title="wJmCCxqLYb.png" alt={954} className="border" border={true} src="https://files.readme.io/70450ac-wJmCCxqLYb.png" />

## Search multiple vehicles

* To search for a single vehicle, first, make sure the textbox to the left of the search box displays ***Multiple***. If this textbox displays ***Single***, click on this textbox and select the Multiple text on the drop-down list

<Image title="0yNJ2JVKkE.png" alt={419} className="border" border={true} src="https://files.readme.io/c2afc46-0yNJ2JVKkE.png" />

* After that, input the Vehicle Codes/License Plates of the vehicles you want to search into the search box (You can mix both Vehicle Codes and License Plates). Each time you input a Vehicle Code/License Plate in the search box, click the Space key on your keyboard to let the system know that you have fully input a Vehicle Code/License Plate. Continue to input other Vehicle Codes/License Plates using this method
* **Note**: You can only input a maximum of ***50*** Vehicle Codes/License Plates in the search box

<Image title="Uyav9j9xTk.png" alt={888} className="border" border={true} src="https://files.readme.io/a45537d-Uyav9j9xTk.png" />

* You can remove a particular Vehicle Code/License Plate from the search box by clicking its corresponding remove icon :fa-times-circle:
* To clear the whole search list, click the clear icon :fa-times: at the right end of the search box 

![426](https://files.readme.io/eea961f-NnNZc7r5ma.png "NnNZc7r5ma.png")

## Beginner's Guide

Here is the guide to help create a single vehicle using 2 methods:

### Create a Vehicle

* **Method 1:** Create a single vehicle using Web form:
* Step 1: Navigate to **Transportations >  Vehicles** tab.
* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Create** (the :fa-pencil: symbol).

![2880](https://files.readme.io/1d89b36-Screen_Shot_2021-01-22_at_14.55.20.png "Screen Shot 2021-01-22 at 14.55.20.png")

* Step 3: Input information to complete the [Vehicle information fields](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-vehicles#vehicle-information-fields). These are the required fields:
* **Organization:** Input the Organization Name/Organization Code of the appropriate management Depot/Sun into the search bar, then select from the drop down menu: ***Sample Depot***
* **Vehicle Type:** Select the suitable vehicle type from the following values: bike; truck; semi-truck.
* **Vehicle Code:** Input management code assigned to the vehicle being created.
* **License plate:** Input license Plate number of the vehicle being created.
* **Temperature:** Tick on check boxes of the supported temperature levels: Ambient, Chilled, Frozen.
* **Temp Zone:**  Input the number of temperature zones available on the vehicle being created.
* **Volume:** Input the maximum product capacity in cubic meter (m3) that the vehicle being created can carry.
* **Weight:** Input the maximum product capacity in kilograms (kg) that the vehicle being created can carry.
* **Start time (HH:mm):** Input the official times of a day when the vehicle being created starts working.
* **Stop time (HH:mm):** Input the official times of a day when the vehicle being created stops working.
* **Lunch start time (HH:mm):** Input the official times of a day when the driver of the vehicle being created starts the lunch break.
* **Lunch stop time (HH:mm):**  Input the official times of a day when the driver of the vehicle being created stops the lunch break.
* **Cost per km:** Input the cost for the vehicle being created per one kilometer during a delivery route.
* **Speed:** Input movement speed of the vehicle being created (Unit: Kilometer per hour (km/h)).
* **Fixed cost:** Input the fixed cost of the vehicle being created during a delivery route, not depending on the route length.
* **Rental cost:** Input the expense your organization have to pay a Subcontractor to rent the vehicle being created for a whole delivery route.
* For more information about notes and input rules of the above fields, please click [here](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-vehicles#vehicle-information-fields).
* *Example:*

![2880](https://files.readme.io/ba4c687-Screen_Shot_2021-01-22_at_15.07.44.png "Screen Shot 2021-01-22 at 15.07.44.png")

![2880](https://files.readme.io/92e4b77-Screen_Shot_2021-01-22_at_15.08.47.png "Screen Shot 2021-01-22 at 15.08.47.png")

![2880](https://files.readme.io/3dbaf05-Screen_Shot_2021-01-22_at_15.09.52.png "Screen Shot 2021-01-22 at 15.09.52.png")

* Step 3: Click **SAVE**.
* **Method 2:** Create a vehicle using Excel file:
* Step 1: Navigate to **Transportation > Vehicles** tab
* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Import Data** (the ⤓ symbol)
* Step 3: A window will pop up. Click **DOWNLOAD SAMPLE** to download Abivin's import template, then save it to your computer.

![2880](https://files.readme.io/8711e68-Screen_Shot_2021-02-01_at_10.07.19.png "Screen Shot 2021-02-01 at 10.07.19.png")

* Step 4: Open the import template and input data into the required fields:
* **Organization Code:** Copy the Organization Code of the Depot/Sun which manages the vehicle being created on Web app, then paste into this cell. For example: ***Sample Depot***
* **Vehicle Type:** You must input the exact same value as follows into the cell: ***truck***
* **Vehicle Code:** Input management code assigned to the vehicle being created. For example: ***SAMPLE-TRUCK***
* **License plate:** Input license Plate number of the vehicle being created. For example: ***29C-23456***. *Note:* This cell must not contain spaces.
* **Temperature:** Input only one of these six values into the cell to specify the temperature levels supported by the vehicle being created: ***F; A; C; FA; FC; FAC***. The letters F; A; C represents the following temperature levels respectively: ***Frozen; Ambient; Chilled***. In this case, input ***A*** into this cell as an example.
* **Temp Zone:**  Input the number of temperature zones available on the vehicle being created. For example: ***1***
* **Volume:** Input the maximum product capacity in cubic meter (m3) that the vehicle being created can carry. For example: ***3***
* **Weight:** Input the maximum product capacity in kilograms (kg) that the vehicle being created can carry. For example: ***600***
* **Start time (HH:mm):** Input the official times of a day when the vehicle being created starts working. For example: ***08:00***
* **Stop time (HH:mm):** Input the official times of a day when the vehicle being created stops working. For example: ***18:00***
* **Lunch start time (HH:mm):** Input the official times of a day when the driver of the vehicle being created starts the lunch break. For example: ***12:00***
* **Lunch stop time (HH:mm):**  Input the official times of a day when the driver of the vehicle being created stops the lunch break. For example: ***12:30***
* **Cost per km:** Input the cost for the vehicle being created per one kilometer during a delivery route. For example: ***2000***
* **Speed:** Input movement speed of the vehicle being created (Unit: Kilometer per hour (km/h)). For example: ***30***
* **Fixed cost:** Input the fixed cost of the vehicle being created during a delivery route, not depending on the route length. For example: ***2000000***
* For more information about the input rules of the above fields, please refer to the [Vehicle information fields](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-vehicles#vehicle-information-fields) section.
* Step 5: Drag and drop the Excel file you have just edited into the import area (the highlighted area in the picture below) or click on that area then select the file from your computer.

![2874](https://files.readme.io/b2c46ea-Screen_Shot_2021-02-01_at_11.21.28.png "Screen Shot 2021-02-01 at 11.21.28.png")

* After following the steps above, you shall see a message at the top right corner of the screen saying: **Completed upload**. The newly-created vehicle shall also appear on the vehicle list. This means you have successfully created a vehicle using an Excel file.

![2880](https://files.readme.io/10d0f72-Screen_Shot_2021-02-01_at_12.02.42.png "Screen Shot 2021-02-01 at 12.02.42.png")

## Vehicle Usage History

* Abivin vRoute system allows you to keep track of the Vehicle usage history. The detailed content is presented in the following article: [**Vehicle Usage History**](https://docs.abivin.com/docs/vrp-dc-vehicle-usage-history).
