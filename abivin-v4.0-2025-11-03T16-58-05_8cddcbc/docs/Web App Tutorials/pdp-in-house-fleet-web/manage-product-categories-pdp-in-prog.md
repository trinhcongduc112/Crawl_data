---
title: Manage Product Categories
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
## Locate Product categories tab

* Product categories are listed on **Products > Product Categories** tab

<Image title="2019-10-22 09_48_02-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/c31fcba-2019-10-22_09_48_02-Window.png" />

## Create Product category

* You have two methods to create Product Categories: Web form and Excel template:

### Create single Product category using Web form.

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using Web form.
* The input rules are described in the section [**Product Category Information Fields**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-product-categories#product-category-information-fields).

<Image title="2019-10-22 10_06_00-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/c345190-2019-10-22_10_06_00-Window.png" />

### Create multiple Product categories using Excel template.

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template.
* The input rules are described in the section [**Product Category Information Fields**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-product-categories#product-category-information-fields).
* Note: At the moment, the **Organization Code** field in the Excel template will have no effect.

<Image title="2019-10-23 11_58_43-Window.png" alt={757} className="border" border={true} src="https://files.readme.io/a0b05ed-2019-10-23_11_58_43-Window.png" />

* To choose the management organization for the product categories being created, on the **Upload data** form, click on the **Organization** field. On the search bar, input the **Organization Name** of the Organization you want to be the management Organization of the Product Categories, then select the suitable value. The management can either be: 1. Solely the Manufacturer or 2. Each Organization, based on the two scenarios below:

#### Scenario 1: You want the Manufacturer to solely manage all Product Categories

* To make the Manufacturer the sole management Organization of all Product Categories, you need to select the radio box **1PL** for the configuration **Business** in the **Manufacturer**

- On the form **Upload Data**, click on the **Organization** field. On the search bar, input the **Organization Name** of the Manufacturer, then select the returned value. After importing, the Product Categories will be managed by the Manufacturer

<Image title="2019-10-23 12_00_18-Window.png" alt={598} className="border" border={true} src="https://files.readme.io/d9d6297-2019-10-23_12_00_18-Window.png" />

#### Scenario 2: You want each Organization to manage its own Product Categories.

* To make each Organization manage its own Product Categories, you need to select the radio box **3PL** for the configuration **Business** in the **Manufacturer**.

- On the form **Upload Data**, click on the **Organization** field. On the search bar, input the **Organization Name** of the appropriate Organization, then select the returned value. After importing, the Product Categories will be managed by the selected Organization.
- **Note**: In this model, in order to create and use Products, you need to select the Organization of **Depot/Sun/xDock** type.

### Product category information fields

* Below are all the information fields of a product category:

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
        The management organization of the product category being created.\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the Organization Name of the appropriate Organization into the search bar, then select from the drop-down menu.\
        **Excel template:**\
        Leave this cell blank.
      </td>
    </tr>

    <tr>
      <td>
        Category Code (Web form); Product Category Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        A classification code assigned to the product category.\
        **2. Input rules:**\
        Format: Must not contain spaces.
      </td>
    </tr>

    <tr>
      <td>
        Parents (Web form); Parent Category Code (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Classification code of the upper-level product category, under which the product category is a lower-level category (If available).\
        For example, the product category "Beverages" with the management code "BVRG" could have lower-level categories such as "Sugar-free drinks" and "Sugary drinks"\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Type the Category Code of the upper-level product category into the search bar, then select from the drop-down menu.\
        If the product category being created doesn't have an upper-level product category, leave this field blank.\
        **Excel template:**\
        Copy the Category Code of the upper-level product category on the Web app, then paste into this cell.\
        If the product category being created doesn't have an upper-level product category, copy its own category code and paste into this cell.\
        The category code can be found under "Category Code" column in "Products > Product Categories" tab.
      </td>
    </tr>

    <tr>
      <td>
        Category Name (Web form); Product Category Name (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        A name assigned to the product category.\
        **2. Input rules:**\
        Format: Free-form
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
        The product category type assigned to the product category.\
        Values of this field depend on the actual product categories structure of your organization.\
        For example: Main Category; Sub Category.\
        **2. Input rules:**\
        Format: Free-form\
        **Note:**\
        This information field is not present in the Excel template. If you use the Excel template to create Product Categories, then after being uploaded, the system will automatically fill in this field with the following value: ***Category***.
      </td>
    </tr>

    <tr>
      <td>
        Description\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Short description of the product category. being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Unload Time Per Unit (min)\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Descriptions:**\
        The time period to unload a single item of every product that belongs to the Product Category being created.\
        Read more about this in the following section: Dynamic Loading/Unloading Time\
        **2. Input rules:**\
        Format: Minutes\
        Input only the value in numbers. Do not input the unit.\
        For example: The unloading for each unit/item of the product category being created is zero point two minutes. Input the following value into this field/cell: ***0.2***.
      </td>
    </tr>
  </tbody>
</Table>

## Update Product category

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute.

<Image title="2019-10-22 10_06_39-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/eb5d911-2019-10-22_10_06_39-Window.png" />

## Delete Product category

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute.

<Image title="2019-10-222 10_07_06-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/8728d84-2019-10-222_10_07_06-Window.png" />

## Search Product category

* If the Product category list is too long, the dispatcher can search for a specific product category by typing either its ***Category Code*** or ***Category Name*** into the **Search** :fa-search: field.

<Image title="2019-10-22 10_09_16-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/5854cfe-2019-10-22_10_09_16-Window.png" />
