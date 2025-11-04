---
title: Manage Containers
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
* This article will guide you on how to manage trailers and containers

## Manage container types

* Navigate to **Freights > Container Types** tab
* This tab is where all the container types are listed
* Before being able to create containers, the dispatcher first needs to create container types

<Image title="container type.png" alt={1673} className="border" border={true} src="https://files.readme.io/10e5cd8-container_type.png" />

## Create container type

### Container type information fields

* A container type will have these essential information fields:

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
        The transporter which manages the container type code being created\
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
        Container Type Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The type of the container type being created\
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
        Container Length\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The length (in feet) of the container type being created\
        **2. Input rules:**\
        Input the value in number. Do not input the unit\
        For example: The container type being created has the length at twenty feet. Input the following value into the field/cell: 20
      </td>
    </tr>
  </tbody>
</Table>

## Edit container type information

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Delete container type

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

## Manage containers

* Navigate to **Freights > Containers** tab
* This tab is where all the containers are listed

<Image title="container tab.png" alt={1673} className="border" border={true} src="https://files.readme.io/ad49599-container_tab.png" />

## Create container

### Container information fields

* Below are the information fields of a container

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
        The transporter which manages the container being created\
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
        Container Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the container being created\
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
        Seal No\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The numbers printed on the seal lock of the container being created\
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
        Container Type\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The container type of the container being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Select the appropriate container type from the drop down menu\
        **Excel template:**\
        Copy the appropriate container type code on Web app, then paste into this cell\
        **Note:**\
        The container type code can be found under "Container Type Code" column in "Freights > Container Types" tab
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
        Tare Weight\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The weight (In kilogram) of the container being created when it is empty\
        **2. Input rules:**\
        Input only the value in number, do not input the unit\
        For example: The container being created has the tare weight at two point five tons. Input the following value into the field/cell: 2500
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
        Net Weight (Web form); Total Weight (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum goods weight (In kilogram) the container being created can carry\
        **2. Input rules:**\
        Input only the value in number, do not input the unit\
        For example: The container being created can carry at maximum twenty five tons. Input the following value into the field/cell: 25000
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
        Gross Weight (Web form); Max Gross (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum goods weight (In kilogram) the container being created can carry, plus the tare weight of that container\
        **2. Input rules:**\
        Input only the value in number, do not input the unit\
        For example: The container being created has the gross weight at thirty tons. Input the following value into the field/cell: 30000
      </td>
    </tr>
  </tbody>
</Table>

## Create single container using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form

## Create multiple containers using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template

* After being created, a container will have additional information fields:

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
        Attached Vehicle
      </td>

      <td>
        The truck tractor that is currently carrying the container
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
        Attached Trailer
      </td>

      <td>
        The trailer that is currently carrying the container
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
        Location
      </td>

      <td>
        The location where the container is currently placed
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
        Stuffing status
      </td>

      <td>
        The status\
        There are two statuses:\
        Full - The container has goods inside\
        Empty - The container doesn't have goods inside
      </td>
    </tr>
  </tbody>
</Table>

## Edit container information

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Delete container

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

## Change container status

* All containers will automatically have their status as **Active** :fa-toggle-on: after being created.
* If you want to change status for some of them, click on :fa-toggle-on: icon under **Action** column at the end of the container row to switch its status from **Active** :fa-toggle-on: to **Deactive** :fa-toggle-off: or vice versa.

<Image title="active container.gif" alt={1668} className="border" border={true} src="https://files.readme.io/80bf382-active_container.gif" />

## Search for container

* To search for a specific container , you could type information related to that container in the **Search field**

<Image title="search cont.gif" alt={1668} className="border" border={true} src="https://files.readme.io/cf4b768-search_cont.gif" />

## Show or hide information columns

* You could show or hide specific information of the containers/trailers by clicking on the **Columns** :fa-caret-down: button, then tick on boxes on the drop down menu

<Image title="show columns.gif" alt={1668} className="border" border={true} src="https://files.readme.io/d470112-show_columns.gif" />
