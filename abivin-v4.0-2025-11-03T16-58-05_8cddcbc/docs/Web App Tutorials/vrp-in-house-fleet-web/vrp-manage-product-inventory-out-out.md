---
title: Manage Product Inventory
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
## General information

* After the products have been created, the depot administrators can start tracking the transaction status of the products in **Products > Inventory** tab

<Image title="2019-08-02 14_47_12-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/e1bfc5a-2019-08-02_14_47_12-Window.png" />

* Apart from the general information fields of the products (which have been inputted during the creation process), in **Products > Inventory** tab, there are some other other information fields which deal directly with the changes in quantity of the products:

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
        The quantity of a specific product physically available on your organization warehouse shelves
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
        Picked
      </td>

      <td>
        The aggregate quantity of a specific finished product which has been picked out of your organization's warehouse shelves and put on to the delivery vehicles, about to be delivered to other locations (Partner or Customer warehouses)
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
        On-SOrder
      </td>

      <td>
        Short for: On Sales Order\
        The aggregate quantity of a specific product on all on-going sales orders
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
        Returning
      </td>

      <td>
        The aggregate quantity of products (Product packaging, Returned finished products) which has been picked out of your partners's warehouse shelves and put on to the delivery vehicles, about to be delivered to your organization warehouse
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
        On-ROrder
      </td>

      <td>
        Short for: On Return Order\
        The aggregate quantity of a specific product on all on-going return orders
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
        On-POrder
      </td>

      <td>
        Short for: On Purchase Order\
        The aggregate quantity of a specific product on all on-going purchase orders
      </td>
    </tr>
  </tbody>
</Table>

* For a product, the number displayed in each of the above fields will change accordingly to the operation status of all orders which have that specific product 

## Filter inventory by warehouse

* If you are the top administrator, you can view inventory of every warehouses (Depot/Sun/Xdock) under your management
* Click on the **Organization** field next to the **Search:fa-search:** field, type the name of the warehouse into this field and choose from the drop down menu
* Next, click on the **Date** :fa-calendar: field next to the **Organization** field. Choose a date from the calendar
* After doing the above two steps, a list of products will show up, following two criteria:
* They are under the chosen warehouse's management
* They have the **Due Date (End Date)** attribute set before the chosen date above

<Image title="inventory filter.gif" alt={1676} className="border" border={true} src="https://files.readme.io/501fde7-inventory_filter.gif" />

## View product transaction history

* To view the transaction history of a specific product, click on that product row. The row will immediately expand and show two tabs:
* **Product Details**: This tab shows the general information of the product

<Image title="2019-10-22 14_47_42-Window.png" alt={1653} className="border" border={true} src="https://files.readme.io/7c85b2d-2019-10-22_14_47_42-Window.png" />

* **History**: This tab shows the transaction history of the product. Each change in the quantity of the product will be recorded and shown here

<Image title="2019-10-22 14_48_06-Window.png" alt={1653} className="border" border={true} src="https://files.readme.io/0d827c3-2019-10-22_14_48_06-Window.png" />

* You can click directly on an order in this tab to view details of that order

<Image title="inventory history.gif" alt={1676} className="border" border={true} src="https://files.readme.io/52cb387-inventory_history.gif" />

## Update product inventory information

## Update on Web form

* On **Product Details** sub tab of a specific products, you can change some attributes of that product, including: ***Start Date***, ***Due Date***, and more importantly ***Quantity***
* **Start Date, Due Date**: Change by clicking on those fields and choose from the drop down calendar; or type directly onto the fields
* **Quantity**: Input the desired quantity into the field, write a short description for the change at the **Note** field
* After inputting all the necessary changes, click **Update** to confirm the change

<Image title="change inventory.gif" alt={1676} className="border" border={true} src="https://files.readme.io/45d1338-change_inventory.gif" />

* A **Warehouse card** will be generated automatically with the prefix **TK**, reflecting the change in the product quantity. This feature will come in handy for organizations who want to change product quantity without having to create Sales/Purchase orders (Which in turn will generate business invoices according to accounting practices)

<Image title="2019-08-02 15_28_17-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/4f46f94-2019-08-02_15_28_17-Window.png" />

## Update by Excel file

* You can bulk update multiple products by uploading the Excel file, similar to creating products
* Warehouse cards will also be created when using this option
* You have to make sure the ***Product Codes*** of the existing products are not changed. To ensure, copy the Product Code of the existing products on Web app (Under **Product Code** column in **Products > Inventory** tab), then paste into **Product Code** cell in the Excel template

<Image title="2019-10-22 14_40_09-Window.png" alt={1676} className="border" border={true} src="https://files.readme.io/6428172-2019-10-22_14_40_09-Window.png" />

## Import inventory by lot number

* If you want to replace the inventory of some specific products by their lot numbers, you can use the 

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
        Organization Code
      </td>

      <td>
        **1. Description:**\
        The Depot that directly manages the product\
        **2. Input rules:**\
        Copy the Organization Code of the appropriate Depot on Web app, then paste into this cell\
        The Organization Code can be found under "Organization Code" column in "Organization List > Organization Code" tab
      </td>
    </tr>

    <tr>
      <td>
        Product Code
      </td>

      <td>
        **1. Description:**\
        The product\
        **2. Input rules:**\
        Copy the appropriate Product Code on Web app, then paste into this cell\
        The Product Code can be found under "Product Code" column in "Products > Inventory" tab
      </td>
    </tr>

    <tr>
      <td>
        Lot Number
      </td>

      <td>
        **1. Description:**\
        The lot number of the product\
        **2. Input rules:**\
        Input the appropriate lot number into this cell\
        If the product already has a lot number on Web app, it will be replaced with this new value
      </td>
    </tr>

    <tr>
      <td>
        QC Number
      </td>

      <td>
        **1. Description:**\
        The QC number of the product\
        **2. Input rules:**\
        Input the appropriate QC number into this cell
      </td>
    </tr>

    <tr>
      <td>
        On-hand Quantity
      </td>

      <td>
        **1. Description:**\
        The new On-hand quantity of the product\
        The value input in this cell will replace the value currently displayed under "On-hand" column in "Products > Inventory" tab\
        **2. Input rules:**\
        Input only the value in numbers. Do not input the unit
      </td>
    </tr>
  </tbody>
</Table>

## Export product inventory information

* To export the product inventory information to an offline record, follow the below steps:
* Click on the **Organizations** field, type the ***Organization Name*** of the warehouse you want to export inventory information, then choose from the drop down menu
* Hover over the :fa-plus-circle: icon, then click on **Export** :fa-download: icon
* Inventory data of the chosen warehouse will be generated and can be downloaded shortly as an Excel file

<Image title="export inventory.gif" alt={1676} className="border" border={true} src="https://files.readme.io/43dcca4-export_inventory.gif" />

## Create product variant

* **Product variant** is an easy way for you to create an entire new product based on a current product, which will retain certain information fields of that current product, without having to create from scratch
* To create a product variant, follow the steps below
* Click on the **Product code** of the products you want to create variants
* On the **Product Details** sub tab, click on **Create Product Variant** button

<Image title="2019-10-28 15_21_04-Window.png" alt={1898} className="border" border={true} src="https://files.readme.io/0a56e29-2019-10-28_15_21_04-Window.png" />

* On **Create Product Variant** form, almost all basic information fields of the selected current product will be retained
* The product code of the product variant being created will be automatically filled in the following format\
  ***PV-yymmdd-xxxx***
* **PV** stands for Product Variant
* **yy** is the last two digits of the current year
* **mm** is the current month
* **dd** is the current date
* **xxxx** is the numerical order of the product variant being created
* You could make changes to all of the pre-filled fields
* Next, do not forget to specify the quantity of the new product variant in the **Quantity** field
* After you have filled every information fields, click on **Create** to finish creating the product variant

<Image title="2019-10-28 2-Window.png" alt={993} className="border" border={true} src="https://files.readme.io/2732d59-2019-10-28_2-Window.png" />
