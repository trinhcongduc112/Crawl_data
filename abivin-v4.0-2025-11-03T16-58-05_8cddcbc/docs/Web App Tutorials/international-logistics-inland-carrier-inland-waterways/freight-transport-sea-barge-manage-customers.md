---
title: Manage Customers
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
## Locate customer tab

* Navigate to **Partners > Customer List** tab
* This tab lists all the customers

## Create customers

## Customer information fields

* Below is the list of all essential information fields needed for customers of this model 

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
        Organization Name (Web form); Organization Code (Excel template)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Transporter which directly manages the customer being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the Organization Name/Organization Code of the Transporter into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the Transporter on Web app, then paste into this cell
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
        Customer Code (Web form); Partner Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the customer being created\
        **2. Input rules:**\
        **Web form:**\
        This code is automatically generated. You can assign a new code by typing into the field\
        **Excel template:**\
        Format: Free-form\
        Must not contain spaces\
        For example: "Customer 01" is not acceptable; "Customer\_01" is acceptable
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
        Mobile Number (Web form); Phone Number (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Mobile number of the customer being created\
        **2. Input rules:**\
        Format: Numbers\
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
        Latitude; Longitude\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Coordinate information of the customer being created\
        **2. Input rules:**\
        **Web form + Excel template:**\
        Format: Must be in Decimal degrees format\
        For example: 41.40338 and 2.17403\
        Read this article for instruction: [**Get coordinates of places**](https://docs.abivin.com/docs/how-to-get-coordinates-of-places)
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
        Full Name (Web form); Partner Name (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Full name of the customer being created\
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
        Address\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The number of the house, name of the road, and name of the town where the customer being created locates\
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
        Shipment Time Location (hours)\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The time period (hours) allowed to pick up containers at the customer's container parking space\
        **2. Input rules:**\
        Format: Integer number\
        Type only the value, do not type the unit\
        For example: If a partner A only allows one hour to pick up containers at their location, type this value into the field: 1
      </td>
    </tr>
  </tbody>
</Table>

## Option 1: Create single customer using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form

## Option 2: Create multiple customers using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template

## Update customer information

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Delete customer

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

## Export customer list

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-read-objects-on-excel-file-export-) article to know the general steps about exporting objects in Abivin vRoute

## Search and filter customer

## Search customer

* To search for a specific customer, input either their ***Title, Customer Code, Customer Name, Email*** or ***Mobile Number*** in the search field :fa-search: 

## Filter customer by Transporter

* You can filter customers of a specific Transporter by clicking on **Organization** :fa-caret-down: field, input the ***Organization Name*** of the Transporter into the search bar. The list of all customers of that Transporter will show up shortly

## Filter customer by Customer group or Province/City

* You can filter customer who belong to the same Customer group, or locate in the same Province/City by clicking on the corresponding column, then select the Customer group or Province/City from the drop down menu. Customers who meet the selected conditions will show up shortly

> 👍 You can combine several filters for more accurate search results
