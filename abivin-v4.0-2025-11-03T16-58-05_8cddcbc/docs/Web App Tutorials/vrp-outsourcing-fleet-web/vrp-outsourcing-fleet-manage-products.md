---
title: Manage Products
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
* The products will be managed in two tabs: 
* **Products > Products**: This tab stores all the general information of the products managed by the organization
* **Products > Inventory**: This tab serves as a ledger to track the changes of product quantity in the Depot shelves throughout the manufacturing and sales processes
* The product can be ***Single item***:

<Image title="beer-bottle-129344-613740.jpg" alt={1200} border={true} src="https://files.readme.io/fa16dc4-beer-bottle-129344-613740.jpg">
  A beer bottle
</Image>

* Or they can come in a ***Case***, each case consists of multiple single items:

<Image title="00266_Beer_Crate_Surface_v005_01_Preview.RGB_color.0000.jpg8513BE2B-644A-4960-AC41-4CF2567B3547Default.jpg" alt={1480} border={true} src="https://files.readme.io/d72773e-00266_Beer_Crate_Surface_v005_01_Preview.RGB_color.0000.jpg8513BE2B-644A-4960-AC41-4CF2567B3547Default.jpg">
  A beer crate, carrying 20 units of beer bottles
</Image>

* In this model, each product case is considered a ***Stock Keeping Unit (SKU)***

## Locate the Products and Inventory tab

* Product general information: Navigate to **Products > Products** tab

<Image title="2019-10-22 13_50_47-Window.png" alt={1654} className="border" border={true} src="https://files.readme.io/3380472-2019-10-22_13_50_47-Window.png" />

* Product Inventory: Navigate to **Products > Inventory** tab

<Image title="2019-10-22 13_51_28-Window.png" alt={1654} className="border" border={true} src="https://files.readme.io/ba287ca-2019-10-22_13_51_28-Window.png" />

## Create products

* To create new products, you have to navigate to **Products > Inventory** tab

<Image title="Image 5.png" alt={1911} className="border" border={true} src="https://files.readme.io/bb1373a-Image_5.png" />

## Product information fields

### Basic product information fields

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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        The Depot which manages the product being created\
        **2. Input rules:**\
        Click on this field. Input the Organization Name/Organization Code of the appropriate Depot into the search bar, then select from the drop down menu\
        **Note:**\
        The Organization Name/Organization Code can be found under "Organization Name" and "Organization Code" columns in "Organizations > Organization List" tab
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        The product category in which the product being created belongs\
        **2. Input rules:**\
        **Web form:**\
        Click on this field and choose the appropriate value from the drop down menu\
        **Excel template:**\
        Copy the appropriate Product Category Code on Web app, then paste into this cell\
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        A management code assigned to the product being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Product 01" is not acceptable; "Product\_01" is acceptable\
        **Important Note:**\
        For products that you don't want to synchronize with the external resource planning system, input the prefix consists of the following two symbols: Hash and Underscore\
        For example: Products with product code "#\_Product01" will not be synchronized with the external resource planning system
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        Management code of the product that is on the upper level to the product being created\
        **2. Input rules:**\
        Copy the value in the Product Code cell then paste into this cell
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        Number of single items in a whole case, if the product being created is normally stored in a case\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: A beer crate has twenty four single bottles. Input the following value into the field/cell: 24
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        Price of a whole case of the product being created\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The product being created has the Case price of two hundred dollars. Input the following value into the field/cell: 200
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        Price of a single item of the product being created, if the sales orders include single items of that product, not just whole cases\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The product being created has the Item price of forty dollars per item. Input the following value into the field/cell: 40
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        The money value to be subtracted from the total value of any Sales order that includes the product being created\
        This value is fixed, regardless of how many whole cases/single items are loaded\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: You want to discount two dollars from the total value of any sales order that includes the product being created. Input the following value into the field/cell: 2\
        If there is no discount, input the following value into the field/cell: 0. Do not leave the field/cell blank
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        Weight (In kilogram, or kg) of a Case of the product being created\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point. Do not use comma\
        For example: The weight of a case is zero point eight kilogram. Input the following value into the field: 0.8
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        Volume (In cubic meter, or m3) of a Case of the product being created\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point. Do not use comma\
        For example: The volume of a case is zero point eight m3. Input the following value into the field/cell: 0.8
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        Quantity of the Cases for the product being created. Value in this field will show up under the "On-Hand" column in "Products > Inventory" tab\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The product being created has two hundred cases in the warehouse. Input the following value into the field/cell: 200
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        The unit of measure for the product being created\
        **2. Input rules:**\
        Format: Text\
        For example: The product being created is beer crate. Input the following value into the field/cell: Crate
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
        (Optional)
      </td>

      <td>
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        Conversion ratio from the unit of measure of the product being created to a default unit of measure specified by the management organization\
        This field is used to calculate the price of Transport service by product\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        For example: The default unit of measure specified by your organization is Pack. If the unit of measure of the product being created is Crate, around 2.5 times larger in volume (or other attributes, depends on how the management organization specifies) than Pack, input the following value into the field/cell: 2.5
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        The date when the product being created is officially started being produced\
        **2. Input rules:**\
        Format: mm/dd/yyyy (Month/Date/Year)\
        **Web form:**\
        Choose the date on the drop down calendar by clicking on this icon: :fa-caret-down:\
        **Excel template:**\
        Input in mm/dd/yyyy format, similar to Web form
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        The date when the product is officially deemed expired\
        After this date, the product will be hidden, not visible on the system\
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        Temperature level of the product being created\
        There are three temperature levels: Ambient; Chilled; Frozen\
        Read more about this configuration at this article: [**Optimize routes with Cold Chain**](https://docs.abivin.com/docs/optimize-routes-with-cold-chain)\
        **2. Input rules:**\
        **Web form:**\
        Click on the appropriate radio box\
        **Excel template:**\
        Input only one of these values into the cell: ***F, A, C***\
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
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
          Input the property into the cell in the format below:\
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
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        The serial number of the product being created\
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
        Tracking By\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        On Web form: Product Detail tab\
        On Excel template: Import\_Product\_Template\
        **1. Description:**\
        The tracking mode of the product being created\
        There are three mode options: Tracking by Serial; Tracking by Lot number; and No tracking\
        **2. Input rules:**\
        **Web form:**\
        Click on the appropriate radio box\
        **Excel template:**\
        If the product is tracked by Lot number, input the following value into this cell: ***1 - Lot Number***\
        If the product is tracked by Serial number, input the following value into this cell: ***2 - Serial Number***\
        If the product is not tracked, input the following value into this cell: ***0 - No Tracking***
      </td>
    </tr>
  </tbody>
</Table>

### Information fields of products tracked by Lot number

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
        Organization Code
        (Excel template)
        (Required)
      </td>

      <td>
        On Excel template: Import\_LotNumber\_Template\
        **1. Description:**\
        The Depot which manages the product being created/updated\
        **2. Input rules:**\
        Copy the Organization Code of the appropriate Depot on Web app, then paste into this cell\
        **Note:**\
        The Organization Code can be found under "Organization Code" column in "Organizations > Organization List" tab
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
        (Excel template)\
        (Required)
      </td>

      <td>
        On Excel template: Import\_LotNumber\_Template\
        **1. Description:**\
        The product code of the product you want to update\
        **2. Input rules:**\
        Copy the appropriate Product Code on Web app, then paste into this cell\
        **Note:**\
        The Product Code can be found under "Product Code" column in "Products > Inventory" tab
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
        Lot Number\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        On Web form: Lot Number tab\
        On Excel template: Import\_LotNumber\_Template\
        **1. Description:**\
        The product lot number of the product being created/updated\
        **2. Input rules:**\
        Format: Free-form\
        **Web form:**
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
        QC Number\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        On Web form: Lot Number tab\
        On Excel template: Import\_LotNumber\_Template\
        **1. Description:**\
        The quality checking number of the product being created/updated\
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
        On-hand Quantity\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        On Web form: Lot Number tab\
        On Excel template: Import\_LotNumber\_Template\
        **1. Description:**\
        The on-hand quantity of the product being created/updated\
        The value input into this field will replace the value currently displayed on Web app\
        **2. Input rules:**\
        Only input the value in numbers. Do not input the unit\
        For example: The product being updated is beer crate. You want to update the on-hand quantity of this product to two hundred thousand crates. Input the following value into this field/cell: 200000
      </td>
    </tr>
  </tbody>
</Table>

## Create product using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form

### Create product that is not tracked by Product Lot/Serial Number

* If the product being created is not tracked by Product Lot/Serial Number, click on **No tracking** radio box on in **Tracking by** field of **Product Detail** tab

### Create product that is tracked by Lot number

* If the product being created is tracked by Lot number, you have to click on **By lot number** radio box on in **Tracking by** field of **Product Detail** tab. After that, input other information fields on **Lot Number** tab

<Image title="KmrMvB2865.png" alt={803} className="border" border={true} src="https://files.readme.io/1765ccd-KmrMvB2865.png" />

<Image title="NvVC6NaWaf.png" alt={799} className="border" border={true} src="https://files.readme.io/d88cb34-NvVC6NaWaf.png" />

* On **Lot Number** tab, after you have input information into all three fields of a product lot: **Lot Number; QC Number; On-hand Quantity**, click on **Add Lot Number** to confirm creating that product lot. The recently created product lot will appear under the **On-hand Quantity** table below

<Image title="lot01.png" alt={888} className="border" border={true} src="https://files.readme.io/3454238-lot01.png" />

* You can continue to input information for other product lots following the steps above
* The total quantity of all product lots will be automatically calculated and displayed in the **Total Quantity** field

<Image title="multiplelots.png" alt={891} className="border" border={true} src="https://files.readme.io/cb035dd-multiplelots.png" />

* If you incorrectly input information for a product lot, you can click on the icon :fa-remove: of that product lot to remove it

<Image title="removelot.png" alt={891} className="border" border={true} src="https://files.readme.io/ea8afb2-removelot.png" />

## Create products using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template

### Create products that are not tracked by Product Lot/Serial Number

* You need to click on **Import Product** icon to download the correct Excel template ***Import\_Product\_Template.xlsx***

<Image title="Image 3.png" alt={1901} className="border" border={true} src="https://files.readme.io/31b9e0e-Image_3.png" />

* You will notice in the Excel template **Import\_Product\_Template**, there is no **Organization** field. Therefore, you also have to choose the management organization for the products being uploaded. On the **Upload Data** form, you need to click on the **Organizations** field, input the Organization Code of the ***Manufacturer*** into the search bar, select from the drop down menu. Next, click on the **All organization** :fa-square-o: check box. Then, click on **Start Upload**. The products being uploaded will show up in the inventory of all Depots under the Manufacturer

<Image title="AKp98ZXnMT.png" alt={591} className="border" border={true} src="https://files.readme.io/f2f0487-AKp98ZXnMT.png" />

### Create products that are tracked by Lot number

* First, you need to click on **Import Product** icon to download the Excel template ***Import\_Product\_Template.xlsx***

<Image title="Image 3.png" alt={1901} className="border" border={true} src="https://files.readme.io/536ef1f-Image_3.png" />

* If the products being created are tracked by Lot number, aside from using the Excel template ***Import\_Product\_Template.xlsx***, you will also have to click on **Import Inventory By Lot Number**, download the Excel template **Import\_LotNumber\_template.xlsx**, input information fields into that Excel template then upload onto the system

<Image title="Image 4.png" alt={1901} className="border" border={true} src="https://files.readme.io/e59158e-Image_4.png" />

* **Note:**
* In the Excel template **Import\_LotNumber\_template.xlsx**, if a product has multiple product lots, input the information for each product lot on a separate row

- If some products and their product lot number already exist on the system, then after you have uploaded the Excel template onto the system, the information input in the ***QC number*** and ***On-hand quantity*** fields of the Excel template will replace the existing information on the system for those products

## Update product information

* Navigate to **Products > Products** tab
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

> 📘 You will only be able to update product information in this tab. To update product quantity, please navigate to **Products > Inventory** tab and follow the instruction in this article: [**Manage Product Inventory**](https://docs.abivin.com/docs/manage-product-inventory#section-update-product-inventory-information)

<Image title="2019-10-22 14_15_31-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/139440d-2019-10-22_14_15_31-Window.png" />

## Delete product

* Navigate to **Products > Products** tab
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

<Image title="2019-10-22 14_22_36-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/a34e7aa-2019-10-22_14_22_36-Window.png" />

## Search product

* Users can search for a specific product by inputing either the ***Product Code*** or ***Product Name*** of that product into the search field :fa-search: on both the **Products** and **Inventory** tabs

<Image title="2019-10-22 14_23_20-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/f450778-2019-10-22_14_23_20-Window.png" />

<Image title="2019-10-22 14_24_03-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/8f5adb4-2019-10-22_14_24_03-Window.png" />

## Track product inventory changes

* As we have introduced at the beginning of the article, the **Products > Inventory** tab is where you can track the change of product inventory during the delivery process
* Below are the information fields that help you keep track of the inventory change of a particular product:

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
        On-hand
      </td>

      <td>
        The total SKU quantity that are physically located in the warehouse at the current time
      </td>
    </tr>

    <tr>
      <td>
        Picked
      </td>

      <td>
        The SKU quantity in the Depart way of all on-going sales orders that have actually been picked up from the warehouse onto the delivery vehicles
      </td>
    </tr>

    <tr>
      <td>
        On-SOrder
      </td>

      <td>
        The total SKU quantity in the Depart way of all on-going Sales orders
      </td>
    </tr>

    <tr>
      <td>
        Returning
      </td>

      <td>
        The SKU quantity in the Return way of all on-going sales orders that have actually been picked up from the customers onto the delivery vehicles
      </td>
    </tr>

    <tr>
      <td>
        On-ROrder
      </td>

      <td>
        The total SKU quantity in the Return way of all on-going Sales orders
      </td>
    </tr>

    <tr>
      <td>
        On-POrder
      </td>

      <td>
        The total SKU quantity of all on-going Purchase orders
      </td>
    </tr>
  </tbody>
</Table>

* The product inventory will change as the orders are performed. The mechanism for inventory chang is explained below

## For new product cases/items issued in Depart Way

### When the order was first created

* The value under **On-SOrder** column will increase by the amount shown under **Number Of Cases** column of the order
* The values under **Picked** and **On-hand** column will not change yet, because the products are still stored in the Depot, not yet loaded onto the delivery vehicle

### When the Corporation Administrator specifies the actual quantity of cases/items to be issued

* The value under **On-SOrder** column will remain the same as when the order was first created
* The values under **Picked** and **On-hand** columns will not change yet, because the products are still stored in the Depot, not yet loaded onto the delivery vehicle

### When the Depot manager updates status of Depart Way from "Open" to "Picked & Packed"

* The value under **On-hand** column will decrease by the amount shown under **Number Of Cases (Actual)** column of the order, to reflect the actual quantity of cases that has been taken from the Depot to the delivery vehicle
* The value under **Picked** column will increase by the amount shown under **Number Of Cases (Actual)** column of the order
* If the product is tracked by product lot, then the On-hand value of each product lot will decrease by the amount shown in the corresponding **Number of Cases** of that product lot in the order screen

<Image title="Image 1fsdf.png" alt={1705} className="border" border={true} src="https://files.readme.io/609e6ff-Image_1fsdf.png" />

* The value under **On-SOrder** column will still remain the same as when the Corporation Administrator specifies the actual quantity of cases/items to be issued

### When the status of Depart Way is updated from "Picked & Packed" to "Shipped"

* The value under **On-hand** column will increase by the difference between: 1. the amount shown under **Number Of Cases (Actual)** column, and 2. the amount shown under **Number Of Case Delivered** column of the order, to reflect the number of cases that the customer didn't receive and were handed back to your Depot
* If the product is tracked by product lot, then similarly, the On-hand value of each product lot will increase by the difference between these two fields of that product lot: 1. the amount shown under **Number Of Cases (Actual)** field , and 2. the amount shown under **Number Of Case Delivered** field
* The values under **Picked** and **On-SOrder** columns will shrink to the values before the order was created

## For empty product cases/items imported in Returned Way

### When the order was first created

* The value under **On-ROrder** column will increase by the exact value shown under **Number Of Cases (Actual)** column of the order
* The values under **Returning** and **On-hand** columns will not change yet, because the products are still stored in the Depot, not yet loaded onto the delivery vehicle

## Synchronize product inventory

## Manually synchronize

* To synchronize product inventory between the external resource planning system and Abivin vRoute, follow the steps below:
* Navigate to **Products > Inventory** tab
* Hover your mouse over the icon :fa-circle-plus:, then click on the **Fetch inventory from SAP** icon :fa-cloud-download:

<Image title="sap product.png" alt={1911} className="border" border={true} src="https://files.readme.io/805992d-sap_product.png" />

* The **Fetch inventory from SAP** form will appear. Here you will need to select the Depot which you want to synchronize the inventory status, by clicking on **Organization** field, then input the ***Organization Name/Organization Code*** of the appropriate Depot into the search bar, then select from the drop down menu
* **Note:** If you are the manage of a particular Depot, then the drop down menu will only show your Depot
* After selecting the Depot, click on **Fetch** button

<Image title="Selection_003.png" alt={388} className="border" border={true} src="https://files.readme.io/f671ffd-Selection_003.png" />

* The system will start synchronizing the inventory from the external resource planning system. After the synchronize process has completed, there will be a popup that reads **Fetch data successfully... Waiting to process**

![292](https://files.readme.io/4bc8c60-success_fetch.png "success fetch.png")

* Below is how this function synchronizes the inventory status of a particular product between the External resource planning system and Abivin vRoute, upon fetching the data from the External resource planning system

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Possible scenario
      </th>

      <th>
        Data fetched from the External resource planning system
      </th>

      <th>
        Abivin vRoute
      </th>

      <th>
        Synchronization result
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        Product lots exist, quantity is larger than zero
      </td>

      <td>
        Product lots don't exist yet
      </td>

      <td>
        Create the product lots on Abivin vRoute, with the same quantity as on the data
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        Product lots exist, quantity is larger than zero
      </td>

      <td>
        Product lots exist, quantity not the same as on the data
      </td>

      <td>
        Update the quantity of the product lots on Abivin vRoute to be the same as on the data
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        Product lots don't exist
      </td>

      <td>
        Product lots exist, quantity is larger than zero
      </td>

      <td>
        Update the quantity of the product lots on Abivin vRoute to be zero
      </td>
    </tr>
  </tbody>
</Table>

## Automatically synchronize

* Abivin vRoute will automatically synchronize the inventory status to the External resource planning system at the following time points: ***07:00; 12:00*** and ***18:00***
