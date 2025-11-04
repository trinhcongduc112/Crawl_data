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
  pages:
    - type: link
      title: Manage Products
      url: https://docs.abivin.com/docs/vrp-in-house-fleet-manage-products
---
## Locate Product Category List

* The Product Categories are listed on the **Products > Product Categories** tab

<Image title="2019-10-22 09_48_02-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/c31fcba-2019-10-22_09_48_02-Window.png" />

## Product Management Mechanisms

* In Abivin vRoute system, there are two Product management mechanisms:
* 1 - Shipper-oriented Product Management Mechanism: This mechanism is used when you want to set up your account as the Shipper
* 2 - Carrier/Distributor-oriented Product Management Mechanism: This mechanism is used when you want to set up your account as the Carrier/Distributor

### Mechanism 1: Shipper-oriented Product Management Mechanism

* This mechanism should be used when you are the Shipper, directly produce and supply your Products to the Product distribution channels or the Consumers by your own vehicle fleet 
* In this mechanism, the Manufacturer Organization will be the sole management Organization of all Product Categories. All lower-level Organizations will inherit the Product Categories from the Manufacturer
* This management mechanism is enabled by default. To know whether your account is currently set up in this mechanism or not, follow the steps below:
* Navigate to the **Organizations > Organizations** tab
* Click the **Edit** icon :fa-pencil: of the Manufacturer
* On the **Update Organization** form, navigate to the **More Configuration > Model** sub-tab
* Look at the **Business** section. If the **1PL** radio box is currently ticked, that means your account is already using this mechanism

<Image title="8vtMlLtoTV.png" alt={741} className="border" border={true} src="https://files.readme.io/543286d-8vtMlLtoTV.png" />

### Mechanism 2: Carrier/Distributor-oriented Product Management Mechanism

* This mechanism is useful when you want to set up your account as the third-party logistics service provider (Also known as the Carrier or Transporter), which provides the transportation services for various Shippers
* In this mechanism, the Organizations of each Shipper will have their own Product Categories
* If you wish to switch to using this mechanism, tick the **3PL** radio box instead (The steps to navigate to the setting area is described above in Mechanism 1)

<Image title="4tO1BSH1Yw.png" alt={734} className="border" border={true} src="https://files.readme.io/4160db1-4tO1BSH1Yw.png" />

* With each of these Product management mechanisms, the creation process of the Product Category, as well as the Product, will differ in certain steps

## Create Product Categories

* You have two methods to create the Product Categories: Webform and Excel import file
* Below we will specify the input rules for each Product management mechanism

### Create Product Categories For Shipper-Oriented Accounts

* If your account is set up following the Product management mechanism 1, follow the input rules in the table below

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Description & Input Rules
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organizations (Webform); Organization Code (Excel import file)
        (Required on Webform)
      </td>

      <td>
        **1. Description:**\
        The Organization that directly manages the Product Category being created\
        For this management mechanism, it is the Manufacturer\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Input the Organization Code/Organization Name of the Manufacturer into the search bar then select it from the drop-down menu\
        **Excel import file:**\
        This information field is no longer used in the Excel import file. Leave this cell blank. You will select the management Organization later when importing the file, which we will talk about below this table
      </td>
    </tr>

    <tr>
      <td>
        Category Code (Webform); Product Category Code (Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the Product Category being created\
        **2. Input rules:**\
        Format: Can contain letters, numbers, special characters. Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        Parents (Webform); Parent Category Code (Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The upper-level Product Category (If any) under which the Product Category being created is the lower-level category\
        For example, the Product Category "Beverages" with the management code "BVRG" could have some lower-level categories such as "Sugar-free drinks" and "Sugary drinks"\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Input the Category Code of the upper-level Product Category into the search bar then select it from the drop-down menu\
        If the Product Category being created doesn't have the upper-level Product Category, leave this field blank\
        **Excel import file:**\
        If the Product Category being created has an existing upper-level Product Category, copy the Category Code of the upper-level Product Category on the Web app then paste it into this cell\
        If the Product Category being created doesn't have an upper-level Product Category, you can leave this cell blank\
        The Product Category Code can be found under the "Category Code" column in the "Products > Product Categories" tab
      </td>
    </tr>

    <tr>
      <td>
        Category Name (Webform); Product Category Name (Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        A name assigned to the Product Category being created\
        **2. Input rules:**\
        Format: Can contain letters, numbers, special characters, and spaces
      </td>
    </tr>

    <tr>
      <td>
        Category Type\
        (Webform)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The specific type of the Product Category being created\
        For example, Main Category, Sub Category\
        **2. Input rules:**\
        **Webform:**\
        Format: Can contain letters, numbers, special characters, and spaces\
        **Note:**\
        This information field is not present in the Excel import file. If you use the Excel import file to create the Product Categories, then after being uploaded, the system will automatically fill in this field with the following value (No quotation marks): ***'Category'***
      </td>
    </tr>

    <tr>
      <td>
        Description\
        (Webform)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A short description about the Product Category being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Unload Time Per Unit (min)\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Descriptions:**\
        The time period to unload a single item of every Product that belongs to the Product Category being created at the Customer's Ship-to locations\
        This information field is used in the Multi-Depot Carrier Service Time calculation mechanism. Read more about this configuration in the following article: [**Service Time Calculation**](https://docs.abivin.com/docs/vrp-in-house-fleet-planned-service-time-calculation#multi-depot-carrier-service-time)\
        **2. Input rules:**\
        Format: Minutes\
        Input only the value in numbers. Do not input the unit\
        For example, the unloading time for every single item of the Product Category being created at the Customer's Ship-to locations is zero point two minutes. Input the following value into this field/cell: ***0.2***
      </td>
    </tr>
  </tbody>
</Table>

* As mentioned above, the **Organization Code** field in the Excel import file is no longer used. Therefore, when you import this file, on the **Upload Data** form, you need to do one more step which is to select the management Organization of the Product Categories. To do this, follow the steps below:
* Step 1: Click the **Organization** field at the bottom left of the form
* Step 2: Select the **Manufacturer** on the drop-down list. Alternatively, you can input the Organization Code/Organization Name of the Manufacturer into the search field to filter it out faster
* Step 3: Click **Start Upload**

### Create Product Categories For Carrier/Distributor-Oriented User Accounts

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Description & Input Rules
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organizations (Webform); Organization Code (Excel import file)
        (Required on Webform)
      </td>

      <td>
        **1. Description:**\
        The Organization that directly manages the Product Category being created\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Input the Organization Code/Organization Name of the appropriate Organization into the search bar then select it from the drop-down menu\
        **Excel import file:**\
        This information field is no longer used in the Excel import file. Leave this cell blank. You will select the management Organization later when importing the file
      </td>
    </tr>

    <tr>
      <td>
        Category Code (Webform); Product Category Code (Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the Product Category being created\
        **2. Input rules:**\
        Format: Can contain letters, numbers, special characters. Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        Parents (Webform); Parent Category Code (Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The upper-level Product Category (If any) under which the Product Category being created is the lower-level category\
        For example, the Product Category "Beverages" with the management code "BVRG" could have some lower-level categories such as "Sugar-free drinks" and "Sugary drinks"\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Input the Category Code of the upper-level Product Category into the search bar then select it from the drop-down menu\
        If the Product Category being created doesn't have the upper-level Product Category, leave this field blank\
        **Excel import file:**\
        Copy the Category Code of the upper-level Product Category on the Web app then paste it into this cell\
        If the Product Category being created doesn't have an upper-level Product Category, leave this cell blank\
        The Product Category Code can be found under the "Category Code" column in the "Products > Product Categories" tab
      </td>
    </tr>

    <tr>
      <td>
        Category Name (Webform); Product Category Name (Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        A name assigned to the Product Category being created\
        **2. Input rules:**\
        Format: Can contain letters, numbers, special characters, and spaces
      </td>
    </tr>

    <tr>
      <td>
        Category Type\
        (Webform)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The specific type of the Product Category being created\
        For example, Main Category, Sub Category\
        **2. Input rules:**\
        **Webform:**\
        Format: Can contain letters, numbers, special characters, and spaces\
        **Note:**\
        This information field is not present in the Excel import file. If you use the Excel import file to create the Product Categories, then after being uploaded, the system will automatically fill in this field with the following value (No quotation marks): ***'Category'***
      </td>
    </tr>

    <tr>
      <td>
        Description\
        (Webform)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A short description about the Product Category being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Unload Time Per Unit (min)\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Descriptions:**\
        The time period to unload a single item of every Product that belongs to the Product Category being created at the Customer's Ship-to locations\
        This information field is used in the Multi-Depot Carrier Service Time calculation mechanism. Read more about this configuration in the following article: [**Service Time Calculation**](https://docs.abivin.com/docs/vrp-in-house-fleet-planned-service-time-calculation#multi-depot-carrier-service-time)\
        **2. Input rules:**\
        Format: Minutes\
        Input only the value in numbers. Do not input the unit\
        For example, The unloading time for every single item of the Product Category being created at the Customer's Ship-to locations is zero point two minutes. Input the following value into this field/cell: ***0.2***
      </td>
    </tr>
  </tbody>
</Table>

* As mentioned above, the **Organization Code** field in the Excel import file is no longer used. Therefore, when you import this file, on the **Upload Data** form, you need to do one more step which is to select the management Organization of the Product Categories. To do this, follow the steps below:
* Step 1: Click the **Organization** field at the bottom left of the form
* Step 2: Select the appropriate Organization on the drop-down list. Alternatively, you can input the Organization Code/Organization Name of the Organization into the search field to filter it out faster
* Step 3: Click **Start Upload**
* Note: If you wish to create the same Product Categories for multiple Organizations at once, you could use a trick, that is to select the upper-level Organization of all the wanted Organizations on the  **Upload Data** form, then tick the  **All Organization** checkbox before importing. Using this trick, the Product Categories being imported will be created for the selected upper-level Organization as well as all of its lower-level Organizations
* For example: In the illustration image below, I have selected a Branch. After importing, the Product Categories will be created for that Branch as well as all the Depots/Suns/xDocks under that Branch

<Image title="y5BynIvUpT.png" alt={593} className="border" border={true} src="https://files.readme.io/31198e7-y5BynIvUpT.png" />

## Update Product category

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

<Image title="2019-10-22 10_06_39-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/eb5d911-2019-10-22_10_06_39-Window.png" />

## Delete Product category

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

<Image title="2019-10-222 10_07_06-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/8728d84-2019-10-222_10_07_06-Window.png" />

## Search Product category

* If the Product category list is too long, the dispatcher can search for a specific product category by typing either its ***Category Code*** or ***Category Name*** into the **Search** :fa-search: field

<Image title="2019-10-22 10_09_16-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/5854cfe-2019-10-22_10_09_16-Window.png" />

## Beginner's Guide

### Create a Product Category

* Here is the guide to creating a product category using Web form:
* Step 1: Navigate to **Products > Product Categories** tab.
* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Create** (the :fa-pencil: symbol).

![2880](https://files.readme.io/d91e211-Screen_Shot_2021-01-22_at_15.54.15.png "Screen Shot 2021-01-22 at 15.54.15.png")

* Step 3: Input information to the required fields to complete the **Category information** 
* **Organizations:** Input the Organization Name of the appropriate Organization into the search bar, then select from the drop down menu: ***Sample Depot***
* **Category Code:** Input the management code assigned to the product category being created.
* **Category Name:** Input the product category type assigned to the product category being created. Values of this field depend on the actual product categories structure of your organization. For example: Main Category; Sub Category.
* *Example:*

![2872](https://files.readme.io/712eb42-Screenshot1616.png "Screenshot1616.png")

* Step 4: Click **SAVE**.
