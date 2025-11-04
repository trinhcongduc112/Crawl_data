---
title: Manage Vehicle Types
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
* In this model, you would have to manually create the Vehicle Types instead of using the default Vehicle Types as in the VRP/DC model

## Locate Vehicle Type List

* The Vehicle Types are listed in the **Transportation > Vehicle Type** tab

<Image title="1. Tab (ENG).png" alt={1920} border={true} src="https://files.readme.io/0a4db2a-1._Tab_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Tab (VIE).png" alt={1920} border={true} src="https://files.readme.io/8723aa7-1._Tab_VIE.png">
  Illustration (Vietnamese)
</Image>

## Create Vehicle Types

* You can create the Vehicle Types using two methods: Webform and Excel import file
* First off, we would like to introduce two product loading methods used in this model:
* Method 1: Products are placed on pallets. The pallets will then be lifted onto the Vehicles' cargo space

<Image title="TrucknTrailer_Blog1-010919.jpg" alt={933} className="border" border={true} src="https://files.readme.io/10e32af-TrucknTrailer_Blog1-010919.jpg" />

* Method 2: Products are placed directly onto the Vehicles' cargo space floor without pallets

<Image title="fletes-1-min.jpg" alt={1200} className="border" border={true} src="https://files.readme.io/e551195-fletes-1-min.jpg" />

* Each of these product loading methods has a different loading/unloading time defined in Abivin vRoute system as the **Palletized Time** and **Non-Palletized Time**

## Create Vehicle Types

* You have two methods to create the Vehicles Types:
* Method 1: Create single Vehicles via Webform
* Method 2: Create multiple Vehicles via Excel import file

### Vehicle Types information fields

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
        (Webform)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Branch under which the Vehicle Type being created belongs\
        **2. Input rules:**\
        Click on this field. Select the appropriate Branch from the drop-down menu
      </td>
    </tr>

    <tr>
      <td>
        Type Code (Webform); Vehicle Type Code (Excel file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the Vehicle Type being created\
        **2. Input rules:**\
        Format: Free-form. Must not contain spaces\
        For example: "Vehicle Type 01" is not acceptable; "Vehicle\_Type-01" is acceptable
      </td>
    </tr>

    <tr>
      <td>
        Type Name (Webform); Vehicle Type Name (Excel file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The name assigned to the Vehicle Type being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Palletized Time (minute)\
        (Webform + Excel file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The time duration (In minutes) for the Vehicles of the Vehicle Type being created to load products with pallet onto their cargo space\
        This time duration will be used during the Route Plan optimization process if you create Orders that are set up to use pallets\
        **2. Input rules:**\
        Input only the value in number, do not input the unit\
        For example: Vehicles of the Vehicle Type being created takes five minutes to load products with pallets onto their cargo space. Input the following value into this field: ***5***
      </td>
    </tr>

    <tr>
      <td>
        Non-Palletized Time (minutes)\
        (Webform + Excel file)\
        (Excel file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The time duration (In minutes) for the Vehicles of the Vehicle Type being created to load products without pallet onto their cargo space\
        This time duration will be used during the Route Plan optimization process if you create Orders that are not set up to use pallets\
        **2. Input rules:**\
        Input only the value in number, do not input the unit\
        For example: Vehicles of the Vehicle Type being created takes five minutes to load products without pallets onto their cargo space. Input the following value into this field: ***5***
      </td>
    </tr>
  </tbody>
</Table>

## Update Vehicle Type Information

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/system-operations#section-update-objects) article to know the general steps about updating objects in Abivin vRoute
* To update a Vehicle Type, click on **Edit** icon :fa-pencil: of that vehicle

<Image title="2. Edit (ENG).png" alt={1920} border={true} src="https://files.readme.io/095d24a-2._Edit_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Edit (VIE).png" alt={1920} border={true} src="https://files.readme.io/b53c415-2._Edit_VIE.png">
  Illustration (Vietnamese)
</Image>

## Delete Vehicle Types

### Delete a single Vehicle Type

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/system-operations#section-update-objects) article to know the general steps about deleting objects in Abivin vRoute
* To delete a Vehicle Type, in the **Edit** column, click on **Delete** icon :fa-remove: of that vehicle
* A form named **Confirmation** will show up, click **OK** to delete the selected Vehicle Type

<Image title="3. Delete (ENG).png" alt={1731} border={true} src="https://files.readme.io/a37fdde-3._Delete_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Delete (VIE).png" alt={1728} border={true} src="https://files.readme.io/c0177e7-3._Delete_VIE.png">
  Illustration (Vietnamese)
</Image>

### Delete multiple Vehicle Types

* Tick the box :fa-square-o: of the Vehicle Types you want to delete. A **Delete** button will show up next to the Organization Search bar.
* When you click the **Delete** button, a form named **Confirmation** will show up on screen, click **OK** to delete the selected Vehicle Types

<Image title="4. Bulk Delete (ENG).png" alt={1729} border={true} src="https://files.readme.io/9f2b558-4._Bulk_Delete_ENG.png">
  Illustration (English)
</Image>

<Image title="4. Bulk Delete (VIE).png" alt={1730} border={true} src="https://files.readme.io/6696c02-4._Bulk_Delete_VIE.png">
  Illustration (Vietnamese)
</Image>
