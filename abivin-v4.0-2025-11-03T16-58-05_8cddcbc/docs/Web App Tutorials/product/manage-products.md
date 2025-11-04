---
title: Manage Products
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
> ❗️ Before being able to create Products, you must create Product categories first. Please read this article for instruction: [**Manage Product categories**](https://docs.abivin.com/docs/manage-product-categories)

* The products will be managed in two tabs: 
* **Products > Products**: Serves as a storage for the all the general information of the products managed by the organization
* **Products > Inventory**: Serves as a ledger to track the changes of product quantity in the warehouse (Depot/Sun/Xdock) throughout the manufacturing and sales processes
* Depends on the type of products, they can come in single unit:

<Image title="11c8e9b0150242ac110003.jpg" alt={1200} border={true} src="https://files.readme.io/31d57a9-11c8e9b0150242ac110003.jpg">
  An air conditioner
</Image>

* Or they can come in a *case* comprised of several product units:

<Image title="00266_Beer_Crate_Surface_v005_01_Preview.RGB_color.0000.jpg8513BE2B-644A-4960-AC41-4CF2567B3547Default.jpg" alt={1480} border={true} src="https://files.readme.io/d72773e-00266_Beer_Crate_Surface_v005_01_Preview.RGB_color.0000.jpg8513BE2B-644A-4960-AC41-4CF2567B3547Default.jpg">
  A beer crate, carrying 20 units of beer bottles
</Image>

## Locate the Products and Inventory tab

* Product general information: Navigate to **Products > Products** tab

<Image title="2019-10-22 13_50_47-Window.png" alt={1654} className="border" border={true} src="https://files.readme.io/3380472-2019-10-22_13_50_47-Window.png" />

* Product Inventory: Navigate to **Products > Inventory** tab

<Image title="2019-10-22 13_51_28-Window.png" alt={1654} className="border" border={true} src="https://files.readme.io/ba287ca-2019-10-22_13_51_28-Window.png" />

## Create products

## Create single product using Web form

* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) to know the general steps about creating single object using web form
* During the creation process, the information fields of a product must be inputted in the below sequence to ensure no mistakes:

1. Organization
2. Product Category
3. Product Code
4. Product Name
5. Case Price
6. Quantity
7. Item Price
8. Number Per Case
9. Weight; Volume
10. Start Date; End Date
11. Temperature
12. Other optional information fields (Product Discount; Form/Unit; Conversion Unit; Properties)

<Image title="2019-10-22 14_05_35-Window.png" alt={798} className="border" border={true} src="https://files.readme.io/8c63a2b-2019-10-22_14_05_35-Window.png" />

## Create multiple products using Excel template

* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) to know the general steps about creating multiple objects using Excel template
* You will notice in the Excel template, there is no **Organization** field. This is because one Excel template can only have product data of only one Depot/Sun/xDock. Therefore, you also have to choose the management organization for the products being uploaded, as follows:

### Upload products for a single warehouse

* To import inventory for a single warehouse (Depot; Sun or Crossdock), click on the **Organizations** field on the bottom left of the **Upload data** form, inputting the Organization Code of the warehouse and select from the drop down menu, then click **Start Upload**. After uploading, the products will show up only in the inventory of the chosen warehouse

<Image title="2019-10-14 18_20_23-Window.png" alt={591} className="border" border={true} src="https://files.readme.io/3f7be4b-2019-10-14_18_20_23-Window.png" />

### Upload products for all organizations

* You need to click on the **Organizations** field, choose the ***Distributor***. Then click on the **All organization** :fa-square-o: check box. The products being uploaded will show up in the inventory of all Depots under the Distributor

<Image title="2019-10-14 18_18_48-Window.png" alt={591} className="border" border={true} src="https://files.readme.io/d934707-2019-10-14_18_18_48-Window.png" />

* After being created, the products will show up on both **Products** and **Inventory** tabs

## Product information fields

* Below are all the information fields of products:

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
        (Web form)
        (Required)
      </td>

      <td>
        **1. Description:**\
        Organization Name of the warehouse (Depot/Sun/Xdock) which manages the product being created\
        **2. Input rules:**\
        Click on this field, type the Organization name into the search bar, then select from the drop down menu
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
        Product Category (Web form); Product Category Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The product category in which the product being created belongs\
        **2. Input rules:**\
        **Web form:**\
        Click on this field and choose the suitable value from the drop down menu\
        **Excel template:**\
        Copy the Product Category Code on Web app, then paste into this cell\
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
        Product Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        A management code assigned to the product being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Product 01" is not acceptable; "Product\_01" is acceptable
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
        Parent Product Code\
        (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Management code of the product that is on the upper level to the product being created\
        **2. Input rules:**\
        Copy the value in the Product Code cell then paste into this cell. Otherwise, the Excel file would not be able to upload onto the system
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
        Product Name\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Product name of the product being created\
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
        Number Per Case\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Number of single products units in a packing case, if the product being created is normally stored in a case\
        **2. Input rules:**\
        Type only the value in numbers. Do not type the unit\
        For example: A beer crate has twenty four bottles of beer. Type this value into the field/cell: 24
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
        Case Price\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Price of a whole case for the product being created\
        **2. Input rules:**\
        Type only the value in numbers. Do not type the unit\
        For example: The product being created has the Case price of two hundred dollars. Then type only Type this value into the field/cell: 200
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
        Item Price\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Price of a single unit for the product being created\
        **2. Input rules:**\
        Type only the value in numbers. Do not type the unit\
        For example: The product being created has the Item price of forty dollars per item. Type this value into the field/cell: 40
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
        Product Discount\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The money value per product unit to be subtracted from the total value of the product being created when creating Sales order for large customers - Customers who have established long term business relationship with your organization\
        **2. Input rules:**\
        Type only the value in numbers. Do not type the unit\
        For example: You want to discount two dollars per product unit. Type this value into the field/cell: 2\
        If there is no discount, type this value into the field/cell: 0. Do not leave the field/cell blank
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
        Weight (kg)\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Weight (In kilogram, or kg) of a Case of the product being created\
        **2. Input rules:**\
        Type only the value in numbers. Do not type the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point. Do not use comma\
        For example: The weight of a case is zero point eight kilogram. Type this value into the field: 0.8. Do not type 0,8
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
        Volume (m3)\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Volume (In cubic meter, or m3) of a Case of the product being created\
        **2. Input rules:**\
        Type only the value in numbers. Do not type the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point. Do not use comma\
        For example: The volume of a case is zero point eight m3. Type this value into the field/cell: 0.8. Do not type this value: 0,8
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
        Quantity\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Quantity of the Cases for the product being created. Value in this field will show up under the "On-Hand" column in "Products > Inventory" tab\
        **2. Input rules:**\
        Type only the value in numbers. Do not type the unit\
        For example: You want the product being created has two hundred cases in the warehouse. Type this value into the field/cell: 200
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
        Form/Unit (Web form); Unit (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Packing unit of the product being created\
        **2. Input rules:**\
        Type the unit\
        For example: The product being created has its packing unit to be Crate. Type this value into the field/cell: Crate
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
        Conversion Unit\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Conversion ratio to compare the packing unit of the product being created to a default packing unit value specified by the management organization\
        This field is used to calculate the price of Transport service by product\
        **2. Input rules:**\
        Type only the value in numbers\
        For example: The default packing unit value is a Pack. If the product being created is a Crate, around 2.5 times larger in volume (or other attributes, depends on how the management organization specifies) than a Pack. Type this value into the field/cell: 2.5. Do not type this value: 2,5\
        If your organization does not use this conversion unit, type this value: 1
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
        Start Date\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The date when the product being created is officially gone into production

        **2. Input rules:**\
        Format: mm/dd/yyyy\
        **Web form:**\
        Choose the date on the drop down calendar by clicking on this icon: :fa-caret-down:\
        **Excel template:**\
        Type in mm/dd/yyyy format, similar to Web form
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
        End Date\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The date when the product is officially deemed expired\
        After this date, the product will disappear from the system\
        **2. Input rules:**\
        Same as Start Date field
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
        Temperature (Web form); Temperature Level (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Temperature level of the product being created\
        Read more about this configuration at this article: [**Optimize routes with Cold Chain**](https://docs.abivin.com/docs/optimize-routes-with-cold-chain)\
        **2. Input rules:**\
        **Web form:**\
        Click on the field then choose the corresponding Temperature type from the drop down menu\
        **Excel template:**\
        Type only one of these values  into the cell: ***F, A, C***\
        The above letters represent these temperature levels respectively: ***Frozen, Ambient, Chilled***
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
        Properties (Web form); Variant Property (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Special attributes of the product being created, to better manage the product\
        Each property consists of three information fields:

        * \*Property Name\*\*: A name assigned to that property
        * \*Property Type\*\*: Data type of the property: A string of text, A specific date or A number
        * \*Property Valu&#x65;**: Exact value of the property, only able to input after choosing Property Type\&#xA;**&#x4E;ote:**\
          Each product can have multiple properties\&#xA;**&#x32;. Input rules:\*\*\
          **Web form:**\
          Click on this icon to add one property: :fa-plus:\
          Input value into the fields of the property sequentially from left to right\
          **Excel template:**\
          Type the property in the cell in the format below:\
          ***Property Name : Property Type : Property Value***\
          (Notice there is a space on each side of the colon)
        * \*Property Nam&#x65;**: Input name of the property, similar to Web form\&#xA;**&#x50;roperty Typ&#x65;**: Input either of these numbers: \***&#x31;, 2, &#x33;***\
          These numbers represent these values in Web form respectively:***&#x54;ext, Date, Number\*\*\*
        * \*Property Valu&#x65;**: Input the value of the property, similar to Web form\&#xA;**&#x4E;ote:**\
          If there are multiple properties, two adjacent properties will be separated by a vertical line, with a space on each side of the vertical line\
          For example:\
          \***&#x43;olor : 1 : Red | Expiry : 2 : 12/20/201&#x38;***\
          Means there are two properties:\&#xA;***&#x46;irst property:\*\*\*
        * Property Name:\* Color
        * Property Type:\* Text
        * Property Value:\* Red\
          ***Second property:***
        * Property Name:\* Expiry
        * Property Type:\* Date
        * Property Value:\* 12/20/2018
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
        Product Serial\
        (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The serial number of the product being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

## Update product information

* Navigate to **Products > Products** tab
* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-update-objects) to know the general steps about updating objects in Abivin vRoute

> 📘 You will only be able to update product information in this tab. To update product quantity, please navigate to **Products > Inventory** tab and follow the instruction in this article: [**Manage Product Inventory**](https://docs.abivin.com/docs/manage-product-inventory#section-update-product-inventory-information)

<Image title="2019-10-22 14_15_31-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/139440d-2019-10-22_14_15_31-Window.png" />

## Delete product

* Navigate to **Products > Products** tab
* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

<Image title="2019-10-22 14_22_36-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/a34e7aa-2019-10-22_14_22_36-Window.png" />

## Search product

* Users can search for a specific product by inputing either the ***Product Code*** or ***Product Name*** of that product into the search field :fa-search: on both the **Products** and **Inventory** tabs

<Image title="2019-10-22 14_23_20-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/f450778-2019-10-22_14_23_20-Window.png" />

<Image title="2019-10-22 14_24_03-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/8f5adb4-2019-10-22_14_24_03-Window.png" />
