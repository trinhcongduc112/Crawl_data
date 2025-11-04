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
## Locate Organizations list

* Navigate to **Organizations > Organization List** tab
* This tab lists all organizations which you either belong in or have the management rights over, if you are the administrator user

<Image title="Org list.png" alt={1676} className="border" border={true} src="https://files.readme.io/d6b1903-Org_list.png" />

## Organization Types and Hierarchy Chart

* In Freight transport - Road model, essentially there are two organization types needed: ***Manufacturer*** and ***Transporter***
* The function of each organization is in the below table:

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
        Resources
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

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Transporter
      </td>

      <td>
        Manufacturer
      </td>

      <td>
        Directly manages the customers; barges, containers and barge captains
      </td>
    </tr>
  </tbody>
</Table>

## Create Organizations

## Organization information fields

* Below is the list of information fields of organizations of this model

> 📘 Except for the information fields mentioned below, all other information fields can be left blank

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
        The direct upper level organization of the organization being created\
        **2. Input rules:**\
        **Web form:**\
        Click on that field, type either the Organization Name or Organization Code of the upper level organization of the organization being created into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the upper level organization of the organization being created on Web app, then paste into this cell\
        **Note:**\
        The Organization Name and Organization Code of organizations can be found under "Organization Name" and "Organization Code" columns in "Organizations > Organization List" tab
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
        Organization Categories (Web form); Organization Category Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Organization Type of the organization being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field and choose the appropriate Organization Type from the drop down menu\
        **Excel template:**\
        If the organization being created is the Transporter, input the following value into the cell: TRANSPORTER
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
        Latitude, Longitude\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
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
        Open Time; Close Time\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The regular time of day at which the organization being created officially starts working and closes\
        **2. Input rules:**\
        Format: hh:mm (24 hour format)\
        For example: The organization being created regularly starts working at 8:30 A.M and closes at 5:30 P.M everyday. You need to input the following values in the Open Time field and Close Time fields: 08:30 and 17:30
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
  </tbody>
</Table>

* You will have 2 options to create organizations:

## Option 1: Create single organization using Web form

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

## Option 2: Create multiple organizations using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template

## Create the Manufacturer

* You have to create the top organization - The Manufacturer, using Web form
* For this organization, you would not be able to select its **Organization type** from the **Organization Categories** field right away, because the **Parent Organization** field is not yet set up

<Image title="2019-10-21 220_40_34-Window.png" alt={1898} className="border" border={true} src="https://files.readme.io/e37dd8c-2019-10-21_220_40_34-Window.png" />

* In order to do so, input other necessary information (***Organization Code; Organization Name; Address; Latitude; Longitude***), click **Save** in order for Abivin vRoute to recognize the newly created Manufacturer in the database

<Image title="2019-10-21 20_39_25-Window.png" alt={1898} className="border" border={true} src="https://files.readme.io/04332a7-2019-10-21_20_39_25-Window.png" />

* Next, click on **Edit** :fa-pencil: icon of the Manufacturer

<Image title="2019-10-21 20_40_34-Window.png" alt={1898} className="border" border={true} src="https://files.readme.io/42602f1-2019-10-21_20_40_34-Window.png" />

* On the **Organization Information** screen, click on **Parent Organization** field and select itself as its own Parent Organization

<Image title="2019-10-21 20_57_01-Window.png" alt={1910} className="border" border={true} src="https://files.readme.io/4e15d5e-2019-10-21_20_57_01-Window.png" />

* After that, click on the **Organization Categories** field, select **Manufacture** from the drop down menu

<Image title="2019-10-21 21_33_34-Window.png" alt={1913} className="border" border={true} src="https://files.readme.io/10a3778-2019-10-21_21_33_34-Window.png" />

* Click **Save** to confirm the change
* Now the Manufacturer has been fully set up. You can move on to create other lower level organizations

<Image title="2019-10-21 21_34_54-Window.png" alt={1913} className="border" border={true} src="https://files.readme.io/a4b6578-2019-10-21_21_34_54-Window.png" />

## Create lower level organizations

* After the Manufacturer has been created, you are able to create the lower level organizations either on Web form or by using Excel template
* When creating organizations directly under the Manufacturer, you must copy the exact Organization Code of the Manufacturer on Web app then paste into the **Parent Organization Code** cells of those direct lower level organizations in the Excel template

<Image title="2019-10-23 13_54_14-Window.png" alt={1674} className="border" border={true} src="https://files.readme.io/e5161e8-2019-10-23_13_54_14-Window.png" />

* For other organizations, as you write the Organization Code for them, copy their Organization Codes then paste into the **Parent Organization Code** cells of their direct lower level organizations

<Image title="2019-09-08 22_48_58-Window.png" alt={1917} className="border" border={true} src="https://files.readme.io/d22f800-2019-09-08_22_48_58-Window.png" />

## Update Organization

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Delete Organization

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

## Search and Filter Organization

## Search Organization

* Input the **Organization Code/Organization Name** of the organization you want to search into the search box :fa-search: 
* The system will filter and return result shortly

<Image title="Search org.gif" alt={1672} className="border" border={true} src="https://files.readme.io/55364f1-Search_org.gif" />

## Filter Organization

* You can filter Organization that are the same **Organization Type** or share the same **Parent Organization** by clicking on the **Organization Categories** and **Parent Organization** columns then ticking on boxes in the drop down menus

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
