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
> 📘 In this model, the vehicles are under direct management of the Transporters

## Locate vehicle list

* Navigate to **Transportation > Vehicle List** tab
* This tab lists all the available vehicles in your organization

<Image title="2019-10-22 15_03_44-Window.png" alt={1671} className="border" border={true} src="https://files.readme.io/f03839a-2019-10-22_15_03_44-Window.png" />

## Create vehicles

## Create single vehicle using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using Web form
* **Note:** 
* During the creation process, the **Organization** and **Vehicle Type** fields must be inputted first

<Image title="2019-10-22 15_09_37-Window.png" alt={790} className="border" border={true} src="https://files.readme.io/11c78e8-2019-10-22_15_09_37-Window.png" />

## Create multiple vehicles using Excel template

* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) to know the general steps about creating multiple objects using Excel template

## Vehicle information fields

* Below is the list of all information fields for vehicles of this model:

> 📘 You don't necessarily need to input in all information fields
>
> Apart from the information fields mentioned below, other information fields can be left blank during the creation process

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
        The Organization (Of Transporter type) which manages the vehicle being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the appropriate Organization Name/Organization Code of the appropriate Transporter into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the appropriate Transporter on Web app, then paste into this cell\
        **Note:**\
        The Organization Name and Organization Code can be found under "Organization Name" and "Organization Code" columns in "Organizations > Organization List" tab\
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
        Vehicle Type\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Vehicle type of the vehicle being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Select the suitable vehicle type from the following values: bike; truck; semi-truck\
        **Excel template:**\
        Input one of the following values into the cell: bike; truck; semi-truck
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
        Start time; Stop time\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The official times of day when the vehicle being created starts and stops working\
        **2. Input rules:**\
        Format: hh:mm (24 hour)\
        For example: The vehicle starts working at 7:30 A.M and stops working at 8:30 P.M. Input the following values into the "Start time" and "Stop time" fields/cells correspondingly: 07:30 and 20:30
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
        Format: Must not contain spaces
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
        A name assigned to the vehicle being created for easier management\
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
        Temperature\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The product temperature levels supported by the vehicle being created\
        **2. Input rules:**\
        **Web form:**\
        Tick on all three check boxes: Frozen, Chilled, Ambient\
        **Excel template:**\
        Input the following value into this cell: ***FAC***\
        The letters F; A; C represents Frozen; Ambien and Chilled temperature levels respectively
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
        The number of temperature zones available on the vehicle being created\
        **2. Input rules:**\
        Input the following value into this field/cell: ***3***
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
        The maximum product capacity in cubic meter (m3) that the vehicle being created can carry\
        **2. Input rules:**\
        Input only the value in numbers. Do not input the unit\
        For example: The vehicle being created can carry maximum twelve cubic meters. Input the following value into the field/cell: 12
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
        The maximum product capacity in kilograms (kg) that the vehicle being created can carry\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The vehicle being created can carry maximum three thousand kilograms. Input the following value into the field/cell: 3000
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
        The total weight of the vehicle, including all the components of the vehicle, the weight of the driver, product, fuel, and other things\
        This field is used for Road constraint by Gross weight. Read more about this configuration at the following article: [***Vehicle gross weight constraint***](https://docs.abivin.com/docs/how-to-optimize-routes-with-road-constraints#section-vehicle-gross-weight-constraint)\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The vehicle gross weight is three thousand kilograms. Input the following value into the field/cell: 3000
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
        (Required)
      </td>

      <td>
        **1. Description:**\
        This field is only used for Freight transport models\
        **2. Input rules:**\
        Input the following value into this field: ***0***
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
        For example: The lunch break starts at 12:30 A.M and stops at 1:30 P.M. Input the following values into the "Lunch start time" and "Lunch stop time" fields/cells correspondingly: 12:30 and 13:30
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
        Input the value in numbers. Do not input the unit\
        For example: The vehicle being created runs at thirty kilometers per hour. Input the following value into the field/cell: 30
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
        The cost for the vehicle being created per one kilometer during a delivery route\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The vehicle costs two thousand dollars to operate per one kilometer. Input the following value into the field/cell: 2000
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
        The fixed cost of the vehicle being created during a delivery route, not depending on the route length\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The Fixed cost of the vehicle is two thousand dollars. Input the following value into the field/cell: 2000
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
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The expense your organization have to pay a Subcontractor to rent the vehicle being created for a whole delivery route\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The Rental cost of the vehicle is five hundred dollars. Input the following value into the field/cell: 500\
        If the vehicle being created is not a rental vehicle, leave this field/cell blank
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
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The code assigned to the vehicle being created, to be used for Route optimization with Familiarity constraint\
        (Read more about this configuration at this article: [**Optimize routes with Familiarity constraint**](https://docs.abivin.com/docs/how-to-optimize-routes-with-familiarity-constraint))\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "MDP 1" is not acceptable; "MDP\_1" is acceptable\
        Leave the cell blank if there is no MDP code assigned to the vehicle\
        If the vehicle is assigned multiple MDP codes, separate two adjacent MDP codes by a comma and a space\
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
        Default driver\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The default driver of the vehicle being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field, choose the default driver from the drop down menu\
        **Excel template:**\
        Copy the username of the driver on Web app, then paste into this cell\
        **Note:**\
        Username of the driver can be found under "Username" column in "Organizations > Organization List" tab\
        **Note:**\
        Only the drivers who are configured to have the same Vehicle Type with the vehicle being created can be chosen
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
        Read more about this feature at this article: [**Optimize routes with Accompanied vehicles feature**](https://docs.abivin.com/docs/accompanied-vehicles)
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

      </td>

      <td>

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

* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-update-objects) to know the general steps about updating objects in Abivin vRoute

<Image title="2019-10-22 22_11_14-Window.png" alt={1915} className="border" border={true} src="https://files.readme.io/dfe5a85-2019-10-22_22_11_14-Window.png" />

## Delete vehicles

* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-delete-objects) to know the general steps about deleting objects in Abivin vRoute

<Image title="2019-10-22 22_11_37-Window.png" alt={1915} className="border" border={true} src="https://files.readme.io/54a6a34-2019-10-22_22_11_37-Window.png" />

## Change vehicle active status

* By default, all vehicles will have their status as ***active*** right after being created, symbolized by a :fa-check-square-o: icon under the **Active** tab
* To change the status of a vehicle into inactive, you can click on that :fa-check-square-o: icon. That icon will change into :fa-square-o:, meaning that vehicle status has changed to **Inactive**

<Image title="2019-10-15 11_03_02-Window.png" alt={1671} className="border" border={true} src="https://files.readme.io/49f7a85-2019-10-15_11_03_02-Window.png" />
