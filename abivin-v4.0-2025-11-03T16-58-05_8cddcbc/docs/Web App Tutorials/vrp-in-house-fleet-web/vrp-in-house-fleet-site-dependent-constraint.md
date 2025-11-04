---
title: Flexible Vehicle Types
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
* In VRP/DC model, apart from the default Vehicle Types (Motorbike, Truck, Semi Truck), the system also allows you to flexibly create the custom Vehicle Types that your organization currently utilizes

## Enable Flexible Vehicle Type Configuration

* In order to be able to create the custom Vehicle Types, you will first need to enable the **Flexible Vehicle Type** at the Manufacturer. To do this, follow the steps below
* Log in to the master account
* Navigate to the **Organizations > Organizations** tab
* Click the **Edit** icon :fa-pencil: of the Manufacturer
* On the **Update Organization** form, navigate to the **More Configuration > Route** sub-tab
* Tick the **Flexible Vehicle Type** checkbox
* Click **Save** to confirm the change
* You might need to log out then log in to your account again for this configuration to take effect

<Image title="u24mpz7CSf.png" alt={732} border={true} src="https://files.readme.io/7a98643-u24mpz7CSf.png">
  Illustration (English)
</Image>

<Image title="m0gHgMR71P.png" alt={732} border={true} src="https://files.readme.io/0019024-m0gHgMR71P.png">
  Illustration (Vietnamese)
</Image>

## Locate Vehicle Type List

* The custom Vehicle Types are listed on the **Transportation > Vehicle Types** tab

## Create Custom Vehicle Types

* You have two methods to create the custom Vehicle Types: Webform and Excel import file

### Vehicle Type Information Fields

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
      </td>

      <td>
        **1. Description:**\
        The Branch that directly manages the Vehicle Type being created\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Select the appropriate Branch from the drop-down menu\
        **Excel import file:**\
        Copy the Organization Code of the appropriate Branch on the Web app then paste it into this cell\
        The Organization Code can be found under the "Organization Code" column in the "Organizations > Organizations" tab
      </td>
    </tr>

    <tr>
      <td>
        Type Code
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the Vehicle Type being created\
        **2. Input rules:**\
        Format: Can contain letters, numbers, and only the following special characters: period (.), comma (,), slash (/), hyphen (-), dash (\_)\
        Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        Type Name
      </td>

      <td>
        **1. Description:**\
        The name assigned to the Vehicle Type being created\
        **2. Input rules:**\
        Format: Can contain letters, numbers, special characters, and spaces
      </td>
    </tr>

    <tr>
      <td>
        Palletized Time (minute)
      </td>

      <td>
        **This information field will only be effective in the PDP models**\
        **1. Description:**\
        The time duration (In minutes) for every Vehicle of the Vehicle Type being created to load Products placed on pallets onto their cargo space (Irrespective of the amount of Product)\
        **2. Input rules:**\
        Input only the value in number. Do not input the unit\
        For example, Vehicles of the Vehicle Type being created takes five minutes to load Products placed on pallets onto their cargo space. Input the following value into this field/cell: ***5***
      </td>
    </tr>

    <tr>
      <td>
        Non-Palletized Time (minutes)
      </td>

      <td>
        **This information field will only be effective in the PDP models**\
        **1. Description:**\
        The time duration (In minutes) for every Vehicle of the Vehicle Type being created to load Products not placed on pallets onto their cargo space (Irrespective of the amount of Product)\
        **2. Input rules:**\
        Input only the value in number. Do not input the unit\
        For example, Vehicles of the Vehicle Type being created takes five minutes to load Products not placed on pallets onto their cargo space. Input the following value into this field/cell: ***5***
      </td>
    </tr>
  </tbody>
</Table>

## Associate Vehicles With Vehicle Types

### Associate Vehicles With Vehicle Types On The Webform

* To associate the existing/new Vehicles with the Vehicle Types, follow the instruction below:
* Navigate to the **Transportation > Vehicles** tab
* Click the **Edit** icon :fa-pencil: of the desired Vehicle
* On the **Update Vehicle** form, click on the **Vehicle Type** field then choose the desired Vehicle Type from the drop-down menu
* Click **Update** to confirm the change

### Associate Vehicles With Vehicle Types In The Excel Import File

* When you use the Excel import file to create new Vehicles or update the existing Vehicles, in order to associate a particular Vehicle with a particular Vehicle Type, you will need to copy the Vehicle Type Code of the desired Vehicle Type on the Web app then paste it into the **Vehicle Type** cell of the desired Vehicle

## Associate Customers With Vehicle types

* In actual transport operation, based on certain parameters such as the size of the Customers' deliveries, the distance to the Customers' receiving locations, the road infrastructure, etc., the route dispatchers/planners will arrange the Vehicle fleet accordingly so that specific Customers will be served only by some specific Vehicle Types. This section will explain how to associate the Customers with the Vehicle Types on Abivin vRoute

### Associate Customers With Vehicle types On The Webform

* In order to associate the Vehicle Types with the existing Customers or the new Customers using the Webform, follow the instruction below:
* Navigate to the **Partners > Customers** tab
* (For the new Customers) Open the Customer creation Webform
* (For the existing Customers) Click the **Edit** icon :fa-pencil: of the desired Customer
* On the **Create/Update Customer** form, after you have selected the Depot, click on the **Allow Vehicle Types** field. The drop-down list will show the Vehicle Types of the Branch that directly manages the selected Depot. Tick the desired Vehicle Type(s) on that list. You can also input the Vehicle Type Code/Vehicle Type Name of the desired Vehicle Type into the search bar to filter it out faster

### Associate Customers With Vehicle Types In The Excel Import File

* When you use the Excel import file to create new Customers or update the existing Customers, if you wish to associate a particular Customer with one or more existing Vehicle Types, follow the given steps below:
* Copy the Vehicle Type Code of the desired Vehicle Type on the Web app then paste it into the respective **Allow Vehicle Types** cell of the desired Customer in the Excel import file
* If that Customer allows multiple Vehicle Types, separate two adjacent Vehicle Type Codes only by a comma (,)

## Route Plan Optimization With Flexible Vehicle Types

* After you have set up:
* 1 - The Vehicle Types and Vehicles
* 2 - The Customers' allowed Vehicle Types
* You can carry out the Route Plan optimization process
* During the Route Plan optimization process, the system will take into account the setups above and generate the Route Plan in which each Customer will be served exactly by their allowed Vehicle Types
