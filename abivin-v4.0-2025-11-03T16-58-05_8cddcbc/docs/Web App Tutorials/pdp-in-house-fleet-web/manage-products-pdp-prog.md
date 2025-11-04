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
* The products will be managed in two tabs: 
* **Products > Products**: This tab stores the general information of the products 
* **Products > Inventory**: This tab serves as a ledger to track the changes of product inventory quantity in the warehouse shelves (Depot)
* The product can be ***Single item***:

<Image title="11c8e9b0150242ac110003.jpg" alt={1200} border={true} src="https://files.readme.io/31d57a9-11c8e9b0150242ac110003.jpg">
  An air conditioner
</Image>

* Or they can come in a ***Whole Case***, each whole case consists of certain number of single items:

<Image title="00266_Beer_Crate_Surface_v005_01_Preview.RGB_color.0000.jpg8513BE2B-644A-4960-AC41-4CF2567B3547Default.jpg" alt={1480} border={true} src="https://files.readme.io/d72773e-00266_Beer_Crate_Surface_v005_01_Preview.RGB_color.0000.jpg8513BE2B-644A-4960-AC41-4CF2567B3547Default.jpg">
  A beer crate, consisting of 20 beer bottles
</Image>

* In Abivin vRoute, the default managing unit of all products is **Whole Case**
* By default, the Product general information will be managed by the Manufacturer, while the Product inventory quantity will be managed by each Depot. However, you can make each Depot manage its own Product general information. Read more at the following section

## Locate the Products and Inventory tab

* Product general information: Navigate to **Products > Products** tab

<Image title="2019-10-22 13_50_47-Window.png" alt={1654} className="border" border={true} src="https://files.readme.io/3380472-2019-10-22_13_50_47-Window.png" />

* Product Inventory: Navigate to **Products > Inventory** tab

<Image title="2019-10-22 13_51_28-Window.png" alt={1654} className="border" border={true} src="https://files.readme.io/ba287ca-2019-10-22_13_51_28-Window.png" />

## Product information fields

> 📘 Apart from the information fields described below, other information fields can be left blank during the creation/update process

* Below are all the information fields of products of this model

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
        Organization Name of the warehouse (Depot) which manages the inventory of the product being created.\
        **2. Input rules:**\
        Click on this field. Input the Organization Name/Organization Code of the appropriate Depot into the search bar, then select from the drop-down menu.\
        **Note:**\
        The Organization Name/Organization Code can be found under columns of the same name in "Organizations > Organization List" tab.
      </td>
    </tr>

    <tr>
      <td>
        Organizations (Web form); Product Category Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The product category in which the product belongs to.\
        **2. Input rules:**\
        **Webform:**\
        Click on this field and choose the suitable value from the drop-down menu.\
        Copy the appropriate Product Category Code on the Web app, then paste into this cell.\
        The category code can be found under "Category Code" column in "Products > Product Categories" tab.
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
        A management code assigned to the product being created.\
        **2. Input rules:**\
        Format: Must not contain spaces.\
        For example: "Product 01" is not acceptable; "Product\_01" is acceptable.
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
        Name of the products.\
        **2. Input rules:**\
        Format: Free-form.
      </td>
    </tr>

    <tr>
      <td>
        Organization

        * (Excel template)\
          (Required)
      </td>

      <td>
        **1. Description:**\
        Type of organizations has been created.\
        **2. Input rules:**\
        **Webform:**\
        Choose from the drop-down list the suitable organization for the product.\
        \**Excel template*\
        Choose the organizations from the drop-down list in the file upload section.
      </td>
    </tr>

    <tr>
      <td>
        Items Per Case\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        A number of items in a whole case, if the product is stored in a case.\
        **2. Input rules:**\
        Format: Integer number only. The value must be larger than or at least equal to 1.\
        Input the value in numbers. Do not input the unit\
        For example: A beer crate has twenty-four bottles. Input the following value into the field/cell: ***24***.\
        **Notes when using Webform:**\
        If you accidentally leave this cell blank or input the value "0", the system will automatically fill the value "1".
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
        The price for a whole case of products.\
        **2. Input rules:**\
        Input the value in numbers. (Do not input the unit).\
        For example: The product has the Case price to be two hundred dollars per case. Input the following value into the field/cell: ***200***.
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
        Price of an item, if the sales orders include items of that product.\
        **2. Input rules:**\
        Input the value in numbers. (Do not input the unit)\
        For example: The product has the Item price to be forty dollars per item. Input the following value into the field/cell: ***40***.
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
        The money value to be subtracted from the total value of any Sales order that includes the product being created.\
        This value is fixed, regardless the quantity of whole case/single items being loaded.\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: You want to discount two dollars from the total value of any sales order that includes the product being created. Input the following value into the field/cell: ***2***.\
        If there is no discount, input the following value into the field/cell: ***0***.
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
        Weight (In kilogram, or kg) of the case or item\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point. (Do not use comma.\
        For example: The weight of a case is zero point eight kilograms. Input the following value into the field: ***0.8***.
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
        Volume (In cubic meter, or m3) of a Case or items.\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point or a comma, based on the setting of your computer\
        For example: The volume of a case is zero point eight m3. Input the following value into the field/cell: ***0.8***
      </td>
    </tr>

    <tr>
      <td>
        Length (m)\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Length of a whole case of the product being created\
        Unit: Meter (m)\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point or a comma, based on the setting of your computer.\
        For example: The length of a case is zero point eight meter. Input the following value into the field/cell: ***0.8***\
        If you do not have data of this field, just leave the field/cell blank.\
        **Note:**\
        If the configuration "Oversized Goods Restriction" of the Manufacturer is enabled, this field/cell will become required, and the value input must be larger than 0.
      </td>
    </tr>

    <tr>
      <td>
        Width (m)\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Width of the whole case of the product.\
        Unit: Meter (m)\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point or a comma, based on the setting of your computer.\
        For example: The width of a case is zero point eight meters. Input the following value into the field/cell: ***0.8***.\
        If you do not have data of this field, just leave the field/cell blank.\
        **Note:**\
        If the configuration "Oversized Goods Restriction" of the [Manufacturer ](http://google.com)is enabled, this field/cell will become required, and the value input must be larger than 0.
      </td>
    </tr>

    <tr>
      <td>
        Height (m)\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Height of the case of the .product.\
        Unit: Meter (m).\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point or a comma, based on the setting of your computer.\
        For example: The height of a case is zero point eight meters. Input the following value into the field/cell: ***0.8***\
        If you do not have data of this field, just leave the field/cell blank\
        **Note:**\
        If the configuration "Oversized Goods Restriction" of the Manufacturer is enabled, this field/cell will become required, and the value input must be larger than 0.
      </td>
    </tr>

    <tr>
      <td>
        On-hand Quantity\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Quantity of whole cases of the product. Value in this field will show up under the "On-Hand" column in "Products > Inventory" tab.\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The product being created has two hundred cases in the warehouse. Input the following value into the field/cell: ***200***.
      </td>
    </tr>

    <tr>
      <td>
        Form/Unit (Web form); Unit (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The unit of measure for the product being created\
        **2. Input rules:**\
        Format: Text\
        For example: The product being created is beer crate. Input the following value into the field/cell: Crate
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
        The date when the product is officially started being producing.\
        **2. Input rules:**\
        Format: mm/dd/yyyy\
        **Web form:**\
        Choose the date on the drop-down calendar by clicking on this icon: :fa-caret-down:\
        **Excel template:**\
        Input in mm/dd/yyyy format, similar to Webform.
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
        The date when the product is officially expired.\
        After this date, the product will be hidden, not visible on the system,\
        **2. Input rules:**\
        Same as the Start Date field
      </td>
    </tr>

    <tr>
      <td>
        Temperature (Web form); Temperature Level (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The temperature level of the product being created\
        There are three temperature levels: Ambient; Chilled; Frozen.\
        Read more about this configuration at this article: to track the changes of product inven.([https://docs.abivin.com/docs/optimize-routes-with-cold-chain](https://docs.abivin.com/docs/optimize-routes-with-cold-chain))\
        **2. Input rules:**\
        **Web form:**\
        Click on the field then choose the corresponding. Temperature type from the drop down menu.\
        **Excel template:**\
        Input only one of these values into the cell: ***F, A, C***\
        The above letters represent these temperature levels respectively: **...*Frozen, Ambient, Chilled***.
      </td>
    </tr>

    <tr>
      <td>
        Properties (Web form); Variant Property (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Special attributes of the product being created, to better manage the product.\
        Each property consists of three information fields:

        * \*Property Name\*\*: A name assigned to that property.
        * \*Property Type\*\*: Data type of the property: A string of text, A specific date or A number.
        * \*Property Value\*\*: Exact value of the property, only able to input after choosing Property Type
        * \*Note:**.\
          Each product can have multiple properties.\&#xA;**&#x32;. Input rules:\*\*\
          **Web form:**\
          Click on this icon to add one property: :fa-plus:\
          Input value into the fields of the property sequentially from left to right.\
          **Excel template:**\
          Input the property into the cell in the format below:\
          ***Property Name : Property Type : Property Value***\
          (Notice there is a space on each side of the colon).
        * \*Property Name\*\*: Input name of the property, similar to Webform.
        * \*Property Typ&#x65;**: Input either of these numbers: \***&#x31;, 2, &#x33;***.\
          These numbers represent these values in Webform respectively: ***&#x54;ext, Date, Number\*\*\*
        * \*Property Valu&#x65;**: Input the value of the property, similar to Webform.\&#xA;**&#x4E;ote:**\
          If there are multiple properties, two adjacent properties will be separated by a vertical line, with a space on each side of the vertical line.\
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
        Product Serial\
        (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The serial number of the product.\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Tracking By\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        **This information field is only used for VRP - Outsourcing fleet Model**\
        **2. Input rules:**\
        **Web form:**\
        Always click on the following radio box: ***No Tracking***\
        **Excel template:**\
        Always input the following value into the cell: ***0 - No Tracking***
      </td>
    </tr>

    <tr>
      <td>
        Number Of Layers\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Specify the maximum number of product cases (layers) of the product being created that can be stacked on top of one another inside the vehicle's container.\
        **2. Input Rules:**\
        Format: Number\
        For example: A maximum of one hundred cases of the product can be stacked on top of one another inside the vehicle's container. Input the following value into the field/cell: ***100***.\
        **Notes:**\
        The number of layers can not exceed the following value: ***1000***
      </td>
    </tr>

    <tr>
      <td>
        Facets\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Specify the facets (sides) of the product case that can be arranged to face the vehicle's container floor when loaded.\
        **2. Input Rules:**\
        **Web form:**\
        Click on the corresponding checkbox of the sides you want.\
        You can select multiple or all checkboxes

        * \*Excel template:**.\
          Input only one of the following seven values into this cell: \***&#x31;; 2; 3; 12; 13; 23; 123\*\*\*.\
          In which:\
          The value '1' means the Front and Back sides of the product case can face the vehicle container floor.\
          The value '2' means the Left and Right sides of the product case can face the vehicle container floor.\
          The value '3' means the Top and Bottom sides of the product case can face the vehicle container floor.
      </td>
    </tr>
  </tbody>
</Table>

## Create products

* To create new products, you have to navigate to **Products > Inventory** tab
* You can create products using two methods: Web form or Excel template

### Method 1: Create single product using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using the web form.
* During the product creation process, the information fields **Organization; Product Category** must be input first.

<Image title="create prod.png" alt={951} className="border" border={true} src="https://files.readme.io/e8ec777-create_prod.png" />

### Method 2: Create multiple products using Excel template

* This option is used when you want to create multiple products for multiple Depot/Sun/Crossdock at once. Note that the inventory quantity would be the same for every Depot/Sun/Crossdock
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template.
* **Note:** You need to click on the icon **Import Product** :fa-file: to download the correct Excel template ***Import\_Product\_Template.xlsx***.

<Image title="import product.png" alt={1908} className="border" border={true} src="https://files.readme.io/335e70c-import_product.png" />

* You will notice in the Excel template, there is no **Organization** field. Upon uploading the Excel template, you have to choose the management Organization for the products being uploaded, as follows:

#### Scenario 1: Import products inventory for a specific Depot

* To import the inventory for a specific Depot, click on the **Organizations** field, input the ***Organization Name/Organization Code*** of that Depot into the search bar, then select it from the drop down menu. Then, click on **Start Upload** button. The inventory being uploaded will show up only in the inventory of the selected Depot.

<Image title="2019-10-14 18_18_48-Window.png" alt={591} className="border" border={true} src="https://files.readme.io/d934707-2019-10-14_18_18_48-Window.png" />

#### Scenario 2: Import products inventory for all Depots under the management of a particular Organization.

* If you want to import products inventory for all Depots under the management of a particular organization, you need to click on the **Organizations** field, input the ***Organization Name/Organization Code*** of that upper-level Organization into the search bar, then select it from the drop-down menu. Next, click on the **All organization**  checkbox :fa-square-o:. When the check box icon turns to :fa-check-square-o:, that means the inventory will be updated for all Depots under that Organization. Then, click on **Start Upload** button. The products being uploaded will show up in the inventory of all Depots under that Organization.

<Image title="product-manu.png" alt={593} className="border" border={true} src="https://files.readme.io/0973efa-product-manu.png" />

* After being created, the products will show up on both **Products** and **Inventory** tabs

#### Notes when creating products using Excel template

* If you have selected the radio box **3PL** for the configuration **Business** of the **Manufacturer**, and you want to import products inventory for all Depots under the management of a particular Organization, then you need to make sure that all the Product Categories inside the Excel template have been created for that Organization as well as every organization under it.

## Update product information

* Navigate to **Products > Products** tab
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute.
* Note that you will only be able to update product information in this tab. To update product quantity, please navigate to **Products > Inventory** tab and follow the instruction in this article: [**Manage Product Inventory**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-product-inventory.)

<Image title="2019-10-22 14_15_31-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/139440d-2019-10-22_14_15_31-Window.png" />

## Delete product

* Navigate to **Products > Products** tab
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute.

<Image title="2019-10-22 14_22_36-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/a34e7aa-2019-10-22_14_22_36-Window.png" />

## Search product

* You can search for a specific product by inputing either the ***Product Code*** or ***Product Name*** of that product into the search field :fa-search: on both the **Products** and **Inventory** tabs.

<Image title="2019-10-22 14_23_20-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/f450778-2019-10-22_14_23_20-Window.png" />

<Image title="2019-10-22 14_24_03-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/8f5adb4-2019-10-22_14_24_03-Window.png" />
