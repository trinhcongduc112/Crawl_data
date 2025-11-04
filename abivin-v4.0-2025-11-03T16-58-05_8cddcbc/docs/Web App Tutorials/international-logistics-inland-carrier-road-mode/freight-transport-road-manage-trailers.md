---
title: Manage Trailers
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
## Locate trailer tab

* Navigate to **Freights > Trailers** tab
* This tab is where all the trailers are listed

## Manage trailer

## Create trailer

### Trailer information fields

* A trailer will have these essential information fields:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Trailer Code
        (Web form + Excel template)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the trailer being created\
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
        Organization (Web form); Organization Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Transporter which manages the trailer being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the Organization Code/Organization Name of the appropriate Transporter into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the appropriate Transporter on Web app, then paste into this cell\
        **Note:**\
        The Organization Code and Organization Name can be found under "Organization Code" and "Organization Name" columns in "Organizations > Organization List" tab
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
        License plate number of the trailer being created\
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
        Type (Web form); Trailer Type (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The type code assigned to the trailer being created\
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
        Weight Level\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum weight (In kilogram) that the trailer being created is registered to be able to carry\
        **2. Input rules:**\
        Input only the value in number, do not input the unit\
        For example: The trailer being created is registered to have the weight level at fifty tons. Input the following value into the field/cell: 50000
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
        Initial Code (Web form); Trailer Initial Code (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The initial code of the trailer team to which the trailer being created belongs in real operation\
        **2. Input rules:**\
        Format: Must not contain spaces
      </td>
    </tr>
  </tbody>
</Table>

### Create single trailer using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form

### Create multiple trailers using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template
* After being created, a trailer will have additional information fields that are displayed on **Freights > Trailers** tab. Most of the fields will automatically be filled through the task submission on Mobile app when the trailer is in use

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Containers On Trailer
      </td>

      <td>
        List of the containers the trailer is currently carrying
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
        2nd Container Possible
      </td>

      <td>
        Specify whether the trailer can carry two containers at the same time or not
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
        Trailer Status
      </td>

      <td>
        The current status of the trailer\
        There are four statuses:\
        Unused\
        Containers attached\
        Vehicle attached\
        Vehicle and containers attached
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
        Trailer Position
      </td>

      <td>
        The location the trailer is currently parking at
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
        Attached Vehicle
      </td>

      <td>
        The truck tractor the trailer is currently attached to
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
        Attached Vehicle Status
      </td>

      <td>
        The current status of the truck tractor that the trailer is currently attached to
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
        Status
      </td>

      <td>
        The current active status of the trailer
      </td>
    </tr>
  </tbody>
</Table>

## Edit trailer information

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Delete trailer

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

## Change trailer status

* All trailers will automatically have their status as **Active** :fa-toggle-on: after being created. 
* If you want to change status for some of them, click on :fa-toggle-on: icon under **Action** column at the end of the trailer row to switch its status from **Active** :fa-toggle-on: to **Deactive** :fa-toggle-off: or vice versa

## Detach trailer from truck tractor

* If a trailer is not intentionally requested from Mobile app by a truck tractor driver, the driver can inform the dispatcher about this incident. Then, the dispatcher can deliberately *detach* the trailer from the truck tractor on Web app by clicking on the icon that reads **Detach trailer**

![1668](https://files.readme.io/6421b0d-detach_trailer.gif "detach trailer.gif")

## Validate quantity of containers currently on a trailer

* A trailer is designed to be able to carry a maximum of two 20ft containers, or one 40ft container (Which mean the maximum aggregated container length supported is 40 feet). Therefore, at the start of every shipment (When the truck tractor driver submit **SHIPPING STARTED** event), the system will perform a check on the status of the trailer, to ensure this condition is valid
* Upon checking, if this condition is not met, then the dispatcher needs to detach the containers currently carried on that trailer, in order to allow the shipment to be operated
* To detach the containers currently carried on a trailer, click on the icon **Detach Container(s)** of that trailer, then click **OK** on the pop-up message

<Image title="Freight - Detach container trailer.gif" alt={1916} className="border" border={true} src="https://files.readme.io/31a09ac-Freight_-_Detach_container_trailer.gif" />

## Search trailer

* To search for a specific trailer, input the **Trailer Code** of that trailer into the search field :fa-search:

<Image title="search cont.gif" alt={1668} className="border" border={true} src="https://files.readme.io/cf4b768-search_cont.gif" />

## Show or hide information columns

* You could show or hide specific information of the containers/trailers by clicking on the **Columns** :fa-caret-down: button, then tick on boxes on the drop down menu.

<Image title="show columns.gif" alt={1668} className="border" border={true} src="https://files.readme.io/d470112-show_columns.gif" />
