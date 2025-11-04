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

## Locate Products and Inventory tabs

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
        Length (m)\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Length of a unit of the product being created\
        Unit: Metre (m)\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point. Do not use comma\
        For example: Length of a product unit is two point five metres. Input the following value into the field/cell: 2.5
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
        Width (m)\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Width of a unit of the product being created\
        Unit: Metre (m)\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point. Do not use comma\
        For example: Width of a product unit is two point five metres. Input the following value into the field/cell: 2.5
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
        Height (m)\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Height of a unit of the product being created\
        Unit: Metre (m)\
        **2. Input rules:**\
        Input the value in numbers. Do not input the unit\
        If the value is a decimal, separate the whole number part and the fractional part by a decimal point. Do not use comma\
        For example: Height of a product unit is two point five metres. Input the following value into the field/cell: 2.5
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
        **1. Description:**\
        Case quantity of the product being created. The value input into this field will show up under the "On-Hand" column in "Products > Inventory" tab\
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
        **This information field is only effective in VRP - Outsourcing Fleet Model**\
        **1. Description:**\
        The tracking mode of the product being created\
        **2. Input rules:**\
        **Web form:**\
        Always select the following radio box: **No Tracking\***\
        **Excel template:**\
        Always input the following value into this cell: ***0 - No Tracking***
      </td>
    </tr>
  </tbody>
</Table>

## Create product using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form

## Create products using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template
* **Note:** You need to click on **Import Product** icon to download the correct Excel template ***Import\_Product\_Template.xlsx***

- You will notice in the Excel template, there is no **Organization** field. Therefore, upon uploading the Excel template, you also have to choose the management organization for the products being uploaded, as follows:

### There is Distributor organization in your organization chart

* You need to click on the **Organizations** field, input the ***Organization Name*** or ***Organization Code*** of the ***Distributor*** into the search field, then select from the drop down menu
* Next, click on the check box **All organization** :fa-square-o:. The products being uploaded will show up in the inventory of all Depots under the management of the Distributor

### There is no Distributor organization in your organization chart

* You need to click on the **Organizations** field, input the ***Organization Name*** or ***Organization Code*** of the ***Manufacturer*** into the search field, then select from the drop down menu
* Next, click on the check box **All organization** :fa-square-o:. The products being uploaded will show up in the inventory of all Depots

<Image title="AKp98ZXnMT.png" alt={591} className="border" border={true} src="https://files.readme.io/f2f0487-AKp98ZXnMT.png" />

## Update product information

* Navigate to **Products > Products** tab
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

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

## Synchronize product inventory

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
