---
title: Manage Organizations
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
New phrases her

## Locate Organizations List

* The Organizations are listed in the **Organizations > Organizations** tab 

<Image title="Org list.png" alt={1676} border={true} src="https://files.readme.io/d6b1903-Org_list.png">
  Illustration (English)
</Image>

<Image title="kgTiy2AWzo.png" alt={1920} border={true} src="https://files.readme.io/47604ab-kgTiy2AWzo.png">
  Illustration (Vietnamese)
</Image>

## Organization Types and Hierarchy Chart

* In this model, there are four compulsory Organization Types : **Manufacturer; Branch; Depot; Transporter**
* The hierarchy and functions of each  Organization Type is listed in the below table:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Organization Type
      </th>

      <th>
        Direct Upper-level Organization type
      </th>

      <th>
        Functions and Resources
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Manufacturer
      </td>

      <td>
        Manufacturer (Itself)
      </td>

      <td>
        Have the management rights over all resources
      </td>
    </tr>

    <tr>
      <td>
        Branch
      </td>

      <td>
        Manufacturer
      </td>

      <td>
        Directly manage the Order Creation/Inspection and Route Plan optimization processes of the subordinate Depots
      </td>
    </tr>

    <tr>
      <td>
        Depot
      </td>

      <td>
        Branch
      </td>

      <td>
        The Depots where the products are stored\
        There are three Depot types:\
        Internal Depot: Depots directly managed by your organizations\
        Customer Depot: Depots managed by your organization's customers\
        Supplier Depot: Depots managed by your organization's suppliers\
        Read more about the Depot type at the following section: [**Special notes when creating Depots**](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-organizations#special-notes-when-creating-depots)
      </td>
    </tr>

    <tr>
      <td>
        Transporter
      </td>

      <td>
        Branch
      </td>

      <td>
        Provide Transport Services to deliver the products between the Depots
      </td>
    </tr>
  </tbody>
</Table>

* On one account, you can create only one Manufacturer, multiple Branches, Depots and Transporters

<Image title="PDP 2 Org chart.png" alt={701} border={true} src="https://files.readme.io/95541ce-PDP_2_Org_chart.png">
  Organization Hierarchy Chart
</Image>

## Create Organizations

* The Organizations can be created using two methods: Webform and Excel template

### Organization information fields

* Below is the list of information fields of organizations of this model

> 📘 Apart from the information fields mentioned below, other information fields belong to other models and can be left blank during the creation/editing process

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
        Parent Organization (Web form); Parent Organization Code (Excel template)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The direct upper-level Organization of the Organization being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Select the appropriate upper-level Organization from the drop-down menu. Alternatively, you can input the Organization Name/Organization Code of the wanted Organization into the search bar to quickly filter it out\
        **Excel file:**\
        Copy the Organization Code of the upper-level Organization of the Organization being created from the Web app, then paste it into this cell\
        The Organization Name and Organization Code can be found under the "Organization Name" and "Organization Code" columns in the "Organizations > Organization List" tab
      </td>
    </tr>

    <tr>
      <td>
        Organization Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Organization Code assigned to the organization being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Org 01" is not acceptable; "Org\_01" is acceptable\
        **Note:**\
        When you use the Web form, the organization code will automatically be capitalized\
        For example: If you input "Sample\_Organization\_Code", it will automatically be converted into "SAMPLE\_ORGANIZATION\_CODE"\
        This code is case sensitive\
        For example: "Sample\_Organization\_Code" is different than "SAMPLE\_ORGANIZATION\_CODE". Please pay attention when copying the code
      </td>
    </tr>

    <tr>
      <td>
        Organization Name\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Name of the organization being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Organization Category (Web form); Organization Category Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Organization Type of the organization being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field and choose the appropriate Organization Type from the drop down menu\
        **Excel template:**\
        Input one of the following values into the cell to specify the organization type of the organization being created (Note: Input all letters in uppercase format): ***BRANCH; DEPOT; TRANSPORTER***
      </td>
    </tr>

    <tr>
      <td>
        Depot Type\
        (Web form)\
        (Required for organizations of Depot type)
      </td>

      <td>
        **This information field will only be visible if the Organization Type value is Depot**\
        **1. Description:**\
        Specify the Depot Type of the Depot being created\
        There are three types:

        * **Internal Depot\***: Your Organization owns the Depot being created
        * **Customer Depot**: Your Organization's Customers own the Depot being created
        * \*Supplier Depo&#x74;**: Your Organization's Suppliers own the Depot being created\&#xA;**&#x32;. Input rules:\*\*\
          Click on this field. Select the appropriate value from the drop-down list
      </td>
    </tr>

    <tr>
      <td>
        Latitude, Longitude\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **This information field is very important for organizations of Depot and Transporter types. They will be used during the Route Plan Optimization process**\
        **1. Description:**\
        Coordinate information of the organization being created\
        **2. Input rules:**\
        Format: Decimal Degrees\
        For example: 41.40338 and 2.17403\
        Read the following article for instruction: [**Get coordinate information of places**](https://docs.abivin.com/docs/how-to-get-coordinates-of-places)
      </td>
    </tr>

    <tr>
      <td>
        Open Time; Close Time\
        (Web form + Excel template)\
        (Required for organizations of Depot type)
      </td>

      <td>
        **This information field is very important for organizations of Depot and Transporter types. They will be used during the Route Plan Optimization process**\
        **1. Description:**\
        The regular time of day at which the organization being created officially starts working and closes\
        **2. Input rules:**\
        Format: HH:mm (24 hour format)\
        For example: The organization being created regularly starts working at 8:30 A.M and closes at 5:30 P.M everyday. You need to input the following values in the Open Time and Close Time fields/cells respectively: 08:30 and 17:30
      </td>
    </tr>

    <tr>
      <td>
        Phone Number\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Phone contact of the organization being created\
        **2. Input rules:**\
        Format: Numbers only. Must not contain spaces\
        For example: "090 181 0800" or "090.181.0800" is not acceptable; "0901810800" is acceptable
      </td>
    </tr>

    <tr>
      <td>
        Address\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Official address where the organization being created is located\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Supplier's Depot (Web form); Supplier Depot (Excel template)\
        (Required for organizations of Depot type)
      </td>

      <td>
        **1. Description:**\
        Specify whether the Depot being created belongs to the supplier or not\
        In this model, the warehousemen of Supplier's Depots will not perform any task on Mobile app. Specify a Depot as Supplier's Depot will stop the Web app from creating tasks on the Mobile app of that Depot's warehousemen\
        **2. Input rules:**\
        **Web form:**\
        If the Depot being created belongs to the supplier, click on the corresponding radio box\
        **Excel template:**\
        If the Depot being created belongs to the supplier, input the following value into this cell: TRUE\
        If the Depot being created doesn't belongs to the supplier, leave this cell blank
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        **2. Input rules:**\
        [Click on this link](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-organizations#special-notes-when-creating-depots)
      </td>
    </tr>
  </tbody>
</Table>

### Option 1: Create single organization using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form
* When using Web form, information fields of an organization must be input in the sequence below to ensure no mistakes:

1. Parent Organization
2. Organization Categories
3. Organization Code
4. Organization Name
5. Latitude, Longitude
6. Phone Number; Address
7. Other optional information fields

<Image title="2019-10-14 09_16_34-Window.png" alt={1655} className="border" border={true} src="https://files.readme.io/544d27f-2019-10-14_09_16_34-Window.png" />

### Option 2: Create multiple organizations using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template

### Create the Manufacturer

* Please refer to the following article for instruction: [**Create the Manufacturer**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-organizations#create-the-manufacturer)

### Create lower level organizations

* The process to create organizations have been described above. Below are some notes when using the Excel template
* When creating the organization directly under the Manufacturer - The Distributor, you must copy the exact Organization Code of the Manufacturer on Web app then paste into the **Parent Organization Code** cell of the Distributor in the Excel template

<Image title="2019-10-23 13_54_14-Window.png" alt={1674} className="border" border={true} src="https://files.readme.io/e5161e8-2019-10-23_13_54_14-Window.png" />

* For other organizations, as you input the Organization Code for them, copy their Organization Codes then paste into the **Parent Organization Code** cells of their direct lower level organizations

<Image title="2019-09-08 22_48_58-Window.png" alt={1917} className="border" border={true} src="https://files.readme.io/d22f800-2019-09-08_22_48_58-Window.png" />

## Update Organization

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Delete Organization

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

## Search and Filter Organization

### Search Organization

* Enter either the **Organization Code** or the **Organization Name** of the organization you want to search in the search box :fa-search: 
* The system will filter and return result shortly

<Image title="Search org.gif" alt={1672} className="border" border={true} src="https://files.readme.io/55364f1-Search_org.gif" />

### Filter Organization

* You can filter Organization that are of the same **Organization Type** or share the same **Parent Organization** by clicking on the **Organization Categories** and **Parent Organization** columns then ticking on boxes in the drop-down menus

<Image title="2019-10-14 09_47_15-Window.png" alt={1674} className="border" border={true} src="https://files.readme.io/2d23aca-2019-10-14_09_47_15-Window.png" />

* You can also search an organization quicker by typing the ***Organization Name*** or ***Organization Code*** of its upper level organization in the search bar of **Parent Organization** column; or the ***Organization Type*** in the search bar **Organization Categories** column

<Image title="2019-10-14 09_48_06-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/4fd487a-2019-10-14_09_48_06-Window.png" />

* You can combine these two filters for more accurate search results

## Locate Organizations on the map

* To view locations of organizations on the map, click on **View Map** icon (Next to the **Search** :fa-search: field)

<Image title="2019-10-14 09_49_08-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/a512d5d-2019-10-14_09_49_08-Window.png" />

* On the map, each organization is marked by a :fa-map-marker: symbol
* Click on each :fa-map-marker: symbol to show the label of the organization
* Click on **View data table** :fa-table: icon to get back to the organization list screen

<Image title="2019-10-14 09_50_02-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/7a3c446-2019-10-14_09_50_02-Window.png" />
