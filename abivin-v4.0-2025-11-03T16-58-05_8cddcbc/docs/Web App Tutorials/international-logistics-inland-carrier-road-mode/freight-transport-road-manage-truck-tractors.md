---
title: Manage Terminal Tractors
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
* In Freight Transport - Road Model, the terminal tractors are under direct management of the ***Transporter***

## Locate terminal tractors list

* Navigate to **Transportation > Vehicle List** tab
* This tab lists all terminal tractors under the management of your organization

<Image title="2019-10-22 15_03_44-Window.png" alt={1671} className="border" border={true} src="https://files.readme.io/f03839a-2019-10-22_15_03_44-Window.png" />

## Create terminal tractors

## Terminal tractor information fields

* Below is the list of all information fields of a terminal tractor

> 📘 Except for the information fields mentioned below, other information fields can be left blank

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
        The Transporter which will manage the terminal tractor being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field, input the Organization Name/Organization Code of the management Transporter into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the Transporter which manages the terminal tractor being created on Web app, then paste into this cell\
        **Note:**\
        The Organization Name and Organization Code can be found under "Organization Name" and "Organization Code" columns in "Organizations > Organization List" tab\
        This information can not be changed once the terminal tractor has been created. Therefore, please pay extra attention
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
        Vehicle type of the truck tractor being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field then choose the following value from the drop down menu: tl\
        **Excel template:**\
        Input the following value into the cell: tl
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
        A name assigned to the truck tractor being created for easier management\
        **2. Input rules:**\
        Format: Free-form
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
        License Plate number of the truck tractor being created\
        **2. Input rules:**\
        Format: Must not contain spaces
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
        Management code assigned to the truck tractor being created\
        **2. Input rules:**\
        Maximum 15 characters\
        Letters and numbers are inputtable. Special characters (Not letters and numbers) will not be inputtable\
        Must not contain spaces
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
        The product temperature levels supported by the truck tractor being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field, tick on check boxes of all temperature levels: Frozen, Ambient, Chilled\
        **Excel template:**\
        Input the following value into the cell: ***FAC***
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
        The number of temperature zones available on the truck tractor being created\
        **2. Input rules:**\
        Input the following value into the field/cell: ***3***
      </td>
    </tr>

    <tr>
      <td>
        Volume (Web form); Capacity Volume (m3) (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum product capacity in cubic meter (m3) that the truck tractor being created can carry\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example, if the truck tractor can carry maximum twelve cubic meters, input the following value into the field/cell: ***12***
      </td>
    </tr>

    <tr>
      <td>
        Weight (Web form); Capacity Weight (kg) (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum product capacity in kilograms (kg) that the truck tractor being created can carry\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: If the truck tractor being created can carry maximum three thousand kilograms, input the following value into the field/cell: ***3000***
      </td>
    </tr>

    <tr>
      <td>
        Gross weight\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The total weight of the truck tractor, including all the components of the truck tractor, the weight of the captain, product, fuel, and other things\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: If the truck tractor gross weight is three thousand kilograms, input the following value into the field/cell: ***3000***
      </td>
    </tr>

    <tr>
      <td>
        Real weight\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The actual weight the truck tractor being created can carry\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: The truck tractor is registered to have the real weight information at three thousand kilograms, input the following value into the field/cell: ***3000***
      </td>
    </tr>

    <tr>
      <td>
        Start time; Stop time\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The official times of day when the truck tractor being created starts and stops working\
        **2. Input rules:**\
        Format: hh:mm (24 hour)\
        Input only the value into this field, do not input the unit\
        For example: The truck tractor starts working at 7:30 A.M and stops working at 8:30 P.M. Input the following values into the "Start time" and "Stop time" fields/cells correspondingly: ***07:30; 20:30***
      </td>
    </tr>

    <tr>
      <td>
        Lunch start time; Lunch stop time\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **Note: This information field is only effective in VRP model**\
        **1. Description:**\
        The official times of day when the driver of the truck tractor being created starts and stops the lunch break\
        **2. Input rules:**\
        Format: hh:mm (24 hour)\
        Input only the value into this field, do not input the unit\
        For example: The lunch break starts at 12:30 A.M and stops at 1:30 P.M. Input the following values into the "Lunch start time" and "Lunch stop time" fields/cells correspondingly: ***12:30; 13:30***
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
        Movement speed of the truck tractor being created\
        Unit: Kilometer per hour (km/h)\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: The truck tractor runs at thirty kilometers per hour. Input the following value into the field/cell: ***30***
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
        The cost for the truck tractor being created per one kilometer during a delivery route\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: The truck tractor costs two thousand dollars to operate per one kilometer. Input the following value into the field/cell: ***2000***
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
        The fixed cost of the truck tractor being created during a delivery route, not depending on the route length\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: The Fixed cost of the truck tractor is two thousand dollars. Input the following value into the field/cell: ***2000***
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Identification Number\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The unique identification code of the truck tractor being created, usually printed on the driver's side of the dashboard\
        **2. Input rules:**\
        Maximum 17 characters\
        All letters and numbers are inputtable, except for the following: Special characters and spaces; letters I (i), O (o), and Q (q) (These three letters can cause confusion with the numbers 1 and 0).
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Engine Number\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The number printed on the engine of the truck tractor being created\
        **2. Input rules:**\
        Maximum 15 characters\
        Letters and numbers are inputtable. Special characters (Not letters and numbers) and spaces will not be inputtable
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
        A code assigned by the management organization and can be printed out and pasted onto the truck tractor being created. This code is similar to the Vehicle code in Abivin vRoute system, but is used by the organization for external management\
        **2. Input rules:**\
        Maximum 15 characters\
        Spaces will not be inputtable\
        All letters, numbers and special characters will be inputtable. Spaces will not be inputtable
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Description\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Short description about the truck tractor being created\
        **2. Input rules:**\
        Format: Free-form
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
        The default driver of the truck tractor being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field, choose the default driver from the drop down menu\
        **Excel template:**\
        Copy the username of the driver on Web app, then paste into this cell\
        **Note:**\
        Username of the driver can be found under "Username" column in "Organizations > Organization List" tab
      </td>
    </tr>

    <tr>
      <td>
        Location\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The current location of the truck tractor being created\
        **2. Input rules:**\
        If you want to update the current location of the truck tractor, click on this field, input the Organization code of the desired location into the search bar and select from the drop down menu\
        The location codes can be found under "Customer Code" column in "Partners > Customer List" tab
      </td>
    </tr>

    <tr>
      <td>
        Device ID (IMEI or MAC Address)\
        (Web form)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The IMEI or MAC Address of the mobile device equipped for the Terminal tractor being created, used to track the current location of the terminal tractor during delivery progress\
        **2. Input rules:**\
        Input the IMEI or MAC Address of the mobile device equipped for the vehicle into this field
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
        The date when the registration certificate of the terminal tractor being created is deemed expired\
        **2. Input rules:**\
        Click on the field, choose the suitable date from the drop down calendar
      </td>
    </tr>
  </tbody>
</Table>

## Create single terminal tractor using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form
* **Note:** 
* During the creation process, the **Organization** and **Vehicle Type** fields must be input first

<Image title="2019-10-22 15_09_37-Window.png" alt={790} className="border" border={true} src="https://files.readme.io/11c78e8-2019-10-22_15_09_37-Window.png" />

## Create multiple terminal tractors using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template

## Store IMEI/MAC address of the terminal tractor's equipped mobile device

* As have been mentioned, in this model, each terminal tractor will be equipped a mobile device (A tablet to be specific). The terminal tractor drivers will receive and submit shipment tasks on the equipped tablet instead of their smartphones. On Web app, the dispatcher can track the current location of the terminal tractors via the GPS information of the equipped tablets. The Web dispatcher first need to store the IMEI/MAC address of each terminal tractor's equipped tablet
* First, the Web dispatcher needs to decide whether to manage the terminal tractor's equipped tablet by IMEI or by MAC Address by doing the following:
* Navigate to the tab **Organizations > Organizations**
* Click **Edit** :fa-pencil: icon of the **Transporter**
* On the form **More Configurations**, navigate to the sub-tab **Mobile**. In the section **Shipment Device ID Type**, select between the two values **IMEI** or **MAC Address**. Click **Save** to confirm the change
* Next, navigate to the tab **Transportation > Vehicle**
* Click **Edit** :fa-pencil: icon of each terminal tractor
* On the form **Update Vehicle**, scroll down until you see the field **Device ID (IMEI or MAC Address)**. Input either the IMEI or MAC Address of the terminal tractor's equipped tablet into this field accordingly to the setting you chose earlier at the Transporter (Note: The MAC Address must be input in capital letters). Click **Save** to confirm the change
* Repeat the above step for the remaining barges

## Update terminal tractor information

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

<Image title="2019-10-22 22_11_14-Window.png" alt={1915} className="border" border={true} src="https://files.readme.io/dfe5a85-2019-10-22_22_11_14-Window.png" />

## Delete terminal tractor

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

<Image title="2019-10-22 22_11_37-Window.png" alt={1915} className="border" border={true} src="https://files.readme.io/54a6a34-2019-10-22_22_11_37-Window.png" />

## Change terminal tractor active status

* By default, all terminal tractors will have their status as ***Active*** right after being created, symbolized by a :fa-check-square-o: icon under the **Active** tab
* To change the status of a terminal tractor into inactive, you can click on that :fa-check-square-o: icon. That icon will change into :fa-square-o:, meaning that terminal tractor status has changed to ***Inactive***

<Image title="2019-10-15 11_03_02-Window.png" alt={1671} className="border" border={true} src="https://files.readme.io/49f7a85-2019-10-15_11_03_02-Window.png" />
