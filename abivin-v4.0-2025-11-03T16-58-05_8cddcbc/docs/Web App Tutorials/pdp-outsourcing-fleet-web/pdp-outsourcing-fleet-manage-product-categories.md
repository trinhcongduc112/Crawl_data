---
title: Manage Product Categories
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
In Abivin vRoute, products will be grouped into ***Product Categories*** for easier management

## Locate Product categories tab

* Navigate to **Products > Product Categories** tab
* This tab lists all the product categories

<Image title="2019-10-22 09_48_02-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/c31fcba-2019-10-22_09_48_02-Window.png" />

## Create Product category

## Create single Product category using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form

<Image title="2019-10-22 10_06_00-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/c345190-2019-10-22_10_06_00-Window.png" />

## Create multiple Product categories using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template
* Note: At the moment, the **Organization Code** field in the Excel template will have no effect

<Image title="2019-10-23 11_58_43-Window.png" alt={757} className="border" border={true} src="https://files.readme.io/a0b05ed-2019-10-23_11_58_43-Window.png" />

* To choose the management organization for the product categories being created, on the **Upload data** form, click on the **Organization** field, input the Organization Name of the ***Manufacturer*** into the search bar, then select from the drop down menu

<Image title="2019-10-23 12_00_18-Window.png" alt={598} className="border" border={true} src="https://files.readme.io/d9d6297-2019-10-23_12_00_18-Window.png" />

## Product category information fields

* Below are all the information fields of a product category

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
        Organizations (Web form); Organization Code (Excel template)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management organization of the product category being created\
        In this model, it is the Manufacturer\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the Organization Name of the Manufacturer into the search bar, then select from the drop down menu\
        **Excel template:**\
        Leave this cell blank
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
        Category Code (Web form); Product Category Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        A management code assigned to the product category being created\
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

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Parents (Web form); Parent Category Code (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Management code of the upper level product category, under which the product category being created is a lower level category (If available)\
        For example, the product category "Beverages" with the management code "BVRG" could have lower level categories such as "Sugar-free drinks" and "Sugary drinks"\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Type the Category Code of the upper level product category into the search bar, then select from the drop down menu\
        If the product category being created doesn't have an upper level product category, leave this field blank\
        **Excel template:**\
        Copy the Category Code of the upper level product category on Web app, then paste into this cell\
        If the product category being created doesn't have an upper level product category, copy its own category code and paste into this cell\
        The category code can be found under "Category Code" column in "Products > Product Categories" tab
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
        Category Name (Web form); Product Category Name (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        A name assigned to the product category being created\
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
        Category Type\
        (Web form)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The product category type assigned to the product category being created\
        Values of this field depend on the actual product categories structure of your organization\
        For example: Main Category; Sub Category\
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
        Description\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Short description about the product category being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

## Update Product category

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

<Image title="2019-10-22 10_06_39-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/eb5d911-2019-10-22_10_06_39-Window.png" />

## Delete Product category

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

<Image title="2019-10-222 10_07_06-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/8728d84-2019-10-222_10_07_06-Window.png" />

## Search Product category

* If the Product category list is too long, the dispatcher can search for a specific product category by typing either its ***Category Code*** or ***Category Name*** into the **Search** :fa-search: field

<Image title="2019-10-22 10_09_16-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/5854cfe-2019-10-22_10_09_16-Window.png" />
