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

![1889](https://files.readme.io/e0575ac-CCCCC.png "CCCCC.png")

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
        The Transporter that will deliver to the customer being created\
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

* To update customer information, click on the pencil button to edit the information
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

![1670](https://files.readme.io/41d78dd-ssss.png "ssss.png")

![956](https://files.readme.io/564c5de-uuuuuuuu.png "uuuuuuuu.png")

## Delete customer

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute
* To delete customers you can use the X button to delete single customer or tick all of the customers and select the delete button.

![1709](https://files.readme.io/e3eb706-CCCCC.png "CCCCC.png")

## Export customer list

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-read-objects-on-excel-file-export-) article to know the general steps about exporting objects in Abivin vRoute

![161](https://files.readme.io/744a3a6-dddddasadsad.png "dddddasadsad.png")

## Search and filter customer

## Search customer

* To search for a specific customer, input either their ***Title, Customer Code, Customer Name, Email*** or ***Mobile Number*** into the search field

![1713](https://files.readme.io/a2e7e2b-ssss.png "ssss.png")

## Filter customer by Customer group or Province/City

* You can filter customer who belong to the same Customer group, or locate in the same Province/City by clicking on the corresponding column, then select the Customer group or Province/City from the drop down menu. Customers who meet the selected conditions will show up shortly

![1713](https://files.readme.io/9fb20a0-CCCCC.png "CCCCC.png")

> 👍 You can combine several filters for more accurate search results
