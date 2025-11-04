---
title: Manage Sales Orders
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
      title: Route Optimization
      url: https://docs.abivin.com/docs/vrp-in-house-fleet-route-optimization
---
## Locate Sales Orders List

* Sales Orders are listed on **Orders > Sales Orders** tab

<Image title="1.png" alt={1920} border={true} src="https://files.readme.io/faca2e5-1.png">
  Illustration Image (English)
</Image>

<Image title="2.png" alt={1920} src="https://files.readme.io/1475261-2.png">
  Illustration Image (Vietnamese)
</Image>

## Create Sales Orders

* Orders can be created using two methods: Web form & Excel template

### Sales Order information fields

* Below are all information fields of a Sales Order

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
        Created On
        (Web form)
      </td>

      <td>
        The date on which the Order was created\
        This information field will always take the current date displayed on your computer
      </td>
    </tr>

    <tr>
      <td>
        From Depot\
        (Web form)\
        (Required)
      </td>

      <td>
        The Depot from where the Order will start
      </td>
    </tr>

    <tr>
      <td>
        Order Date\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        The date on which the Order is planned to be performed and completed
      </td>
    </tr>

    <tr>
      <td>
        Due Date\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **This information field is only intended for certain user accounts which use external TMS**\
        The date on which the Order is planned to be delivered. After this date, the Order can no longer be performed
      </td>
    </tr>

    <tr>
      <td>
        ETA Date\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **This information field is only intended for certain user accounts which use external TMS**\
        The date on which the Order is estimated to arrive at the Ship-to location
      </td>
    </tr>

    <tr>
      <td>
        ETD Date\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **This information field is only intended for certain user accounts which use external TMS**\
        The date on which the Order is estimated to start from the Ship-to Depot location
      </td>
    </tr>

    <tr>
      <td>
        Manually\
        (Web form)\
        (Optional)
      </td>

      <td>
        **This information field is only intended for certain user accounts**\
        Manually input the ETA Date of the Order
      </td>
    </tr>

    <tr>
      <td>
        Order Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Management code assigned to the Order\
        Format: Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        Order Type\
        (Excel template)\
        (Required)
      </td>

      <td>
        Specify the Type of the Order
      </td>
    </tr>

    <tr>
      <td>
        Customer Code (Web form); Partner Code (Excel template)\
        (Required)
      </td>

      <td>
        Customer Code of the customer that creates the Sales Order
      </td>
    </tr>

    <tr>
      <td>
        Invoice Code\
        (Web form)\
        (Optional)
      </td>

      <td>
        Code of the commercial invoice associated with the order
      </td>
    </tr>

    <tr>
      <td>
        Check by\
        (Web form)\
        (Optional)
      </td>

      <td>
        Name of the personnel who performs checking errors of the order
      </td>
    </tr>

    <tr>
      <td>
        Order Time Window (Web form); Time Window (Excel template)\
        (Optional)
      </td>

      <td>
        The time period(s) the customer can receive the Order\
        **Note:**\
        An Order can have multiple time windows. The Order time windows must be within the Customer time window, else the Order will not be executable
      </td>
    </tr>

    <tr>
      <td>
        Product Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Code of the product assigned by the customer
      </td>
    </tr>

    <tr>
      <td>
        Number Of Cases\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        The case quantity of a particular product loaded in the order being created
      </td>
    </tr>

    <tr>
      <td>
        Number Of Items\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        The single item quantity of a particular product loaded in the order being created
      </td>
    </tr>

    <tr>
      <td>
        Customer Discount\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        The money value to be discounted for the customers, will be subtracted from the field "Total price" of the order being created (If the total price is automatically calculated)
      </td>
    </tr>

    <tr>
      <td>
        Order Discount (Web form) Sale Discount (Excel template)\
        (Optional)
      </td>

      <td>
        Sales Discount, will be subtracted from the field "Total price" of the order being created (If the total price is automatically calculated)
      </td>
    </tr>

    <tr>
      <td>
        Promotion Discount\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        Promotion Discount, will be subtracted from the field "Total price" of the order being created  (If the total price is automatically calculated)
      </td>
    </tr>

    <tr>
      <td>
        IMVD Discount\
        (Excel template)\
        (Optional)
      </td>

      <td>
        IMVD Discount, will be subtracted from the field "Amount" of the product on Web form
      </td>
    </tr>

    <tr>
      <td>
        Total Price\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        The total price of the order
      </td>
    </tr>

    <tr>
      <td>
        Lot Number\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        The ordinal number of the product lot from where the products loaded in the Order were picked up
      </td>
    </tr>

    <tr>
      <td>
        Service Time\
        (Excel template)\
        (Optional)
      </td>

      <td>
        The manually input unloading time period of the Order being created at the customer warehouse
      </td>
    </tr>

    <tr>
      <td>
        Pickup Order\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        Specify whether the order being created is a Pickup Order or not\
        Read more in the following article:
      </td>
    </tr>

    <tr>
      <td>
        Separate Vehicle (Web form); Splitted (Excel template)\
        (Optional)
      </td>

      <td>
        Specify whether the Orders placed by the same customer will be delivered by separate vehicles or not\
        Read more in the following article: [**Separate Vehicle Delivery (Split Order)**](https://docs.abivin.com/docs/vrp-in-house-fleet-separate-vehicle-delivery)
      </td>
    </tr>

    <tr>
      <td>
        Expired Date\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        The Date when a product loaded in the order being created is deemed expired, no longer usable
      </td>
    </tr>

    <tr>
      <td>
        Note\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        A short note about the order being created\
        The note will appear on the Mobile app of the driver who delivers this order
      </td>
    </tr>

    <tr>
      <td>
        Ship-To Depot Code\
        (Web form)
      </td>

      <td>
        **This information field is only intended for certain user accounts which use external TMS**\
        The Depot (On external TMS) where products will actually be loaded before delivering to the Ship-to location
      </td>
    </tr>

    <tr>
      <td>
        Ship-to Code\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **This information field is only intended for certain user accounts which use external TMS**\
        The location where the Customer will actually receive products
      </td>
    </tr>

    <tr>
      <td>
        Active Status\
        (Excel template)\
        (Optional)
      </td>

      <td>
        Specify whether the Orders being created will be put into the Route Plan Optimization process after being imported or not
      </td>
    </tr>

    <tr>
      <td>
        Estimated Distance\
        (Web form)\
        (Automatic)
      </td>

      <td>
        The estimated driveway distance for vehicles of Truck type between the Depot location to the Customer location as suggested by Google Map engine
      </td>
    </tr>
  </tbody>
</Table>

### Create single Order using Web form

* Please refer to the [System Operations](doc:system-operations#create-records) article to know the general steps about creating single object using Web form

- Below are the input rules when using Web form

#### **1.1. From Depot**

* Click on this field. On the search bar, input the **Organization Code/Organization Name** of the appropriate Depot, then select the returned value

#### **1.2. To Customer**

> ❗️ The field **From Depot** must be input before this field

* Click on this field. On the search bar, input the **Customer Code/Customer Name** of the appropriate Customer, then select the returned value

#### **1.3. Order Code**

* The Order Code is automatically generated in the following format:\
  ***SO-yymmdd-xxxxx***
* In which:
* 1 - ***SO*** stands for ***Sales Order***
* 2 - ***yy*** are the last two digits of the current year. For example: The current year is ***2019***, then the ***yy*** value would be ***19***
* 3 - ***mm*** is the current month. For example: The current month is ***October***, then the ***mm*** value would be ***10***
* 4 - ***dd*** is the current date. For example: The current date is ***Sixteenth***, then the ***dd*** value would be ***16***
* 5 - ***xxxxx*** is the ordinal number of the Order. This ordinal number will automatically increase each time you open the form **Create Sales Order**. For example: ***00001; 00023; 11111*** and so on
* You can also change the Order Code to your own format. Note that the Order Code must not contain spaces

#### **1.4. Product**

* Click on the field on the same row with the button **Add Product** (Below the text **Search**). On the search bar, input the **Product Name/Product Code** of the wanted Product, then select the returned value. Click on the button **Add Product** to add that Product to the Order
* The recently added Product will appear on the Product table below
* Repeat these steps to add more Products
* If you accidentally add a wrong Product, click on the respective recycle bin icon :fa-trash: of that Product (Under the column **Remove** on the Product table) to remove it
* Input the whole case/single item quantity of the Product into the fields **Cases** and **Items** on the Product table
* If the Product has an Expiry Date, click on the calendar icon :fa-calendar: of the field **Expired Date** then select the appropriate date on the drop down calendar. Alternatively, you can directly input the Expiry Date in the format ***mm/dd/yyyy***. If you don't have this information, just leave that field blank
* If the Product whole cases/single items were taken from a specific Product Lot in the warehouse, input in the field **Lot Number**. If you don't have this information, just leave that field blank
* Notice the value in the field **Line Price** will change accordingly to the whole case/single item quantity. The Line Price is calculated using the following formula:
* ***Line Price = Whole Case Quantity x Whole Case Price + Single Item Quantity x Single Item Price***

#### **1.5. Order Time Window**

* If the Customer demands a specific Time Window for the Order, input in this field.
* The time window format is HH:mm-HH:mm, for example 11:00-13:00
* The Order Time Window will be taken into account during the Route Plan Optimization process
* **Important Note**: The Order Time Window must have overlapping period with the Customer Time Window, else the Order will not be optimizable

#### **1.6. Customer Discount; Sales Discount; Promotion Discount**

* If the Order has these discounts, input in the respective fields, else you can leave them blank

#### **1.7. Total Price**

* By default, the Total Price of the Order is automatically calculated using the following formula:
* ***Total Price = Aggregated Line Price of all Products - sum of (Customer Discount; Sales Discount; Promotion Discount)***
* If you wish to manually set a Total Price for the Order, tick the checkbox **Manual Total Price** then manually input your desired Total price

#### **1.8. Pickup Order; Separate Vehicle**

* If you want the Order to be a Pickup Order, tick the checkbox **Pickup Order**
* If a Customer places multiple Orders, and you want each of those Orders delivered by separate vehicles, then tick the checkbox **Separate Vehicle**
* **Note**: The checkbox **Separate Vehicle** will not be visible if the configuration **Split Delivery** is enabled at the **Branch**

#### **1.9. Invoice Code; Check By; Note**

* These information fields are optional. If you don't have information, just leave these fields blank

#### **1.10. Ship-to Code; Ship-to Depot Code; Due Date; ETA Date; ETD Date**

> 🚧 As has been mentioned above, these fields are only intended for certain user accounts which use external TMS

* If the Customers has Ship-to locations, click on the field **Ship-to Code**, select the appropriate Ship-to location from the drop down list
* **Note:** Refer to the following article to know how to create Ship-to locations for Customers: s**]

  ### Create multi

### Create multiple Orders using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template
* Below is the instruction to input in the information fields

#### **2.1. Order Date**

* Input in either ***dd/mm/yyyy*** or ***mm/dd/yyyy*** format, based on the current Date format of your computer

<Image title="2019-10-29 10_28_30-.png" alt={1906} border={true} src="https://files.readme.io/85866aa-2019-10-29_10_28_30-.png">
  Illustration Image (English)
</Image>

<Image title="9.png" alt={1895} src="https://files.readme.io/b350bf4-9.png">
  Illustration Image (Vietnamese)
</Image>

#### **2.2. Order Code**

* The Order code must not contain spaces

<Image title="2019-10-29 10_27_39-Window.png" alt={133} border={true} src="https://files.readme.io/93afcef-2019-10-29_10_27_39-Window.png">
  Illustration Image (English)
</Image>

<Image title="1.png" alt={108} src="https://files.readme.io/0933e18-1.png">
  Illustration Image (Vietnamese)
</Image>

#### **2.3. Order Type**

* Always input the following value into this cell: ***SALES***

<Image title="2019-10-29 10_26_59-Window.png" alt={113} border={true} src="https://files.readme.io/64b1dde-2019-10-29_10_26_59-Window.png">
  Illustration Image (English)
</Image>

<Image title="2.png" alt={115} src="https://files.readme.io/e14d4e0-2.png">
  Illustration Image (Vietnamese)
</Image>

#### **2.4. Partner Code**

* Copy the **Customer Code** of the appropriate customer on Web app, then paste into this cell
* The Customer Code can be found under **Customer Code** column in **Partners > Customer List** tab

<Image title="2019-10-29 08_45_57-Window.png" alt={1905} border={true} src="https://files.readme.io/a5f41a4-2019-10-29_08_45_57-Window.png">
  Illustration Image (English)
</Image>

<Image title="1.png" alt={1913} src="https://files.readme.io/9a0107d-1.png">
  Illustration Image (Vietnamese)
</Image>

#### **2.5. Product**

##### **2.5.1. Product Code**

* Copy the **Product Code** of the product on Web app, then paste into this cell
* The Product Code can be found under **Product Code** column in **Products > Inventory** tab

<Image title="2.png" alt={1920} border={true} src="https://files.readme.io/9821f05-2.png">
  Illustration Image (English)
</Image>

<Image title="1.png" alt={1920} src="https://files.readme.io/909292b-1.png">
  Illustration Image (Vietnamese)
</Image>

* If the Order contains multiple producs, you need to place each product on a separate row. Note that you have to copy and paste the all commom attributes of the Order across all product rows, such as: ***Order Code; Order Type; Partner Code, Order Type etc.***

<Image title="TdDx5hMDLW.png" alt={899} border={true} src="https://files.readme.io/4cd5680-TdDx5hMDLW.png">
  Illustration Image (English)
</Image>

<Image title="1.png" alt={791} src="https://files.readme.io/1cc3f65-1.png">
  Illustration Image (Vietnamese)
</Image>

##### **2.5.2. Number of Cases; Number of Items**

* Input the quantity of cases and single items of each product into their corresponding **Number of Cases** and **Number of Items** cells

<Image title="1.png" alt={750} border={true} src="https://files.readme.io/38f3084-1.png">
  Illustration Image (English)
</Image>

<Image title="2.png" alt={791} src="https://files.readme.io/c9d33e5-2.png">
  Illustration Image (Vietnamese)
</Image>

* If there is zero case of a particular product being loaded, input the value ***0*** into the corresponding cell **Number of Cases** of that product. Do not leave that cell blank
* If there is zero single item of a particular product being loaded, input the value ***0*** into the corresponding cell **Number of Items** of that product. Do not leave that cell blank

##### **2.5.3. Lot Number; Expired Date**

* If the product loaded in the order has an Expired Date, input in either ***dd/mm/yyyy*** or ***mm/dd/yyyy*** format, based on the current Date format of your computer
* These fields are optional. Leave them blank if you don't have information

#### **2.6. Time Window**

* If there is a time window, always input in the following format: ***hh:mm-hh:mm*** (24 hour format)
* The time point must not exceed ***23:59***
* If there is no time window, leave the cell blank

<Image title="2019-10-29 08_58_21-Window.png" alt={135} border={true} src="https://files.readme.io/b68ac2a-2019-10-29_08_58_21-Window.png">
  Illustration Image (English)
</Image>

<Image title="3.png" alt={106} src="https://files.readme.io/1869775-3.png">
  Illustration Image (Vietnamese)
</Image>

#### **2.7. Total Price**

* If you want the system to automatically calculate the order price, leave this cell blank

<Image title="2.png" alt={851} className="border" border={true} src="https://files.readme.io/5256ea1-2.png" />

* If you don't want the system to automatically calculate the Total price, input your own Total price into this cell. If the Order contains multiple products, input the same Total price value on all the product rows

<Image title="1.png" alt={852} className="border" border={true} src="https://files.readme.io/8340b58-1.png" />

#### **2.8. Customer Discount; Sale Discount; Promotion Discount; IMVD Discount**

* **Note:** These discounts will only take effect if you let the system automatically calculate the total price of the order
* The IMVD discount will be subtracted directly from the price of each product (See blue rectangles)
* The Customer Discount; Sale Discount; Promotion Discount must be input the same for every products of an order (See red rectangles)
* The total price will be calculated in this formula: ***Sum of product prices (After subtracting the IMVD discounts) - (Sum of Customer Discount; Sale Discount & Promotion Discount) = Total Order Price*** (See green rectangle)

<Image title="1.png" alt={535} className="border" border={true} src="https://files.readme.io/49c4a5e-1.png" />

#### **2.10. Pickup Order**

* If the order being created is a Pickup Order, input the following value into this cell: ***1***
* If the order being created is not a Pickup Order, input the following value into this cell: ***0***. You could also just leave this cell blank

<Image title="4.png" alt={152} className="border" border={true} src="https://files.readme.io/446fbdd-4.png" />

#### **2.9. Splitted Order**

* If the order being created is a Split Order,  input the following value into this cell: ***TRUE***
* If the order being created is not a Split Order,  input the following value into this cell: ***FALSE*** into the cell. You could also just leave this cell blank

<Image title="5.png" alt={116} className="border" border={true} src="https://files.readme.io/cc4ef3d-5.png" />

#### **2.10. Service Time (minutes)**

* Input only the value in numbers. Do not input the unit
* For example: If the order being created has the service time at five minutes, input the following value into this cell: ***5***
* If the order does not have a service time, leave this cell blank

#### **2.11. Note**

* These fields are optional. Leave them blank if you don't have information
* If the product has an Expired Date, input in either ***dd/mm/yyyy*** or ***mm/dd/yyyy*** format, based on the current Date format of your computer

#### **2.12. Active**

* If you want to change the status of the orders. Input **Active** into this cell
* **Note:** You can also change the Active status of the Orders after they have been uploaded onto the Web app

## Update unlocked order

* If an order has not been locked, you can edit its information
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

<Image title="2019-10-29 15_39_42-Window.png" alt={1913} className="border" border={true} src="https://files.readme.io/0b4c0b1-2019-10-29_15_39_42-Window.png" />

## Delete unlocked order

* If an order has not been locked, you can delete it

## Delete single order

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-single-object) article to know the general steps about deleting single object in Abivin vRoute

<Image title="2019-10-29 14_06_06-Window.png" alt={1909} className="border" border={true} src="https://files.readme.io/f163947-2019-10-29_14_06_06-Window.png" />

## Delete multiple orders

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-multiple-objects) article to know the general steps about deleting multiple objects in Abivin vRoute

<Image title="2019-10-29 14_08_27-Window.png" alt={1909} border={true} src="https://files.readme.io/a54281f-2019-10-29_14_08_27-Window.png">
  Delete several orders at once
</Image>

<Image title="2019-10-29 14_08_53-Window.png" alt={1909} border={true} src="https://files.readme.io/f7d244f-2019-10-29_14_08_53-Window.png">
  Delete all orders of a page at once
</Image>

## Refresh Orders

* To get the latest statuses of the Orders, or to make the Orders' details show with the changes you've just made to their elements (Partners; Products), you can use the function **Refresh Orders**
* To refresh the Order List, click on the button **Refresh** :fa-refresh: on the toolbar above the Order List

- **Note**: The refresh function will get the lastest update of the entire Order List, not just the Orders currently displayed

## Search and Filter Orders

### Search Orders

* You have two Order searching methods: 
* Method 1: Single search method, used to search for a single Order
* Method 2: Multiple search method, used to search multiple Orders at once
* To switch between these two searching methods, click on the text box to the left of the search bar and select the preferred method from the drop-down list

<Image title="jcYLiJe0V9.png" alt={413} border={true} src="https://files.readme.io/cf316f4-jcYLiJe0V9.png">
  Illustration (English)
</Image>

<Image title="qYHkKykMJQ.png" alt={417} border={true} src="https://files.readme.io/604760a-qYHkKykMJQ.png">
  Illustration (Vietnamese)
</Image>

* If the current searching method is Single search, you can search for a single Order by inputting one of the following attributes of the wanted Order into the search bar: **Order Code; Customer Name; Customer Code**

<Image title="dXpNVDN9Ga.png" alt={472} border={true} src="https://files.readme.io/a6e8b7c-dXpNVDN9Ga.png">
  Illustration (English)
</Image>

* If the searching method is Multiple search, you can search for multiple Order Codes at once. To do this, sequentially input each of the wanted Order Codes into the search bar, with each two adjacent Order Codes separated only by a comma (,). If earlier you have imported the Orders using the Order Excel import file, you can simply copy the Order Codes from the file and paste them into the search bar, the system will automatically separate the Order Codes for you

<Image title="K8MIiclyue.png" alt={636} border={true} src="https://files.readme.io/e1f53e5-K8MIiclyue.png">
  Illustration (English)
</Image>

<Image title="searchmultiorder.gif" alt={1912} className="border" border={true} src="https://files.readme.io/f65804e-searchmultiorder.gif" />

* **Note**: You can only search for a maximum of ***50*** Order Codes each time. If you input more than 50 Order Codes into the search bar, the system will display a warning

<Image title="RNX5ipwlgx.png" alt={413} className="border" border={true} src="https://files.readme.io/5cfe6bb-RNX5ipwlgx.png" />

* When searching multiple Orders, you can remove a specific Order from the search bar by clicking its respective remove icon :fa-times-circle:. To remove all Order Codes from the search bar, click the clear icon :fa-times: at the top right corner of the search bar

<Image title="OZHecWdnbq.png" alt={400} className="border" border={true} src="https://files.readme.io/95ab8ae-OZHecWdnbq.png" />

### Filter orders

* You can filter orders originated from a specific **Depot/Sun** or **xDock** via the **Organization** field on the toolbar
* Type the ***Organization Code*** or ***Organization Name*** of the Depot/Sun/xDock in the search bar, then select from the drop down menu
* Orders that originated from the selected Depot/Sun/xDock will show up

<Image title="2019-10-29 15_28_4w9-Window.png" alt={1907} className="border" border={true} src="https://files.readme.io/f6a2a11-2019-10-29_15_28_4w9-Window.png" />

#### Filter orders by Execution date or Creation date

* Please refer to the [Search & Filter Functions](doc:search-and-filter-functions) article to know the general steps about filter objects by date in Abivin vRoute
* Notice there are two calendar fields on the toolbar. The calendar on the left is used to filter the **Execution date** of the orders; while the calendar on the right is used to filter the **Creation date** of the orders

<Image title="2019-10-29 15_28_49-Window.png" alt={1907} border={true} src="https://files.readme.io/3139c53-2019-10-29_15_28_49-Window.png">
  Filter orders that have the creation dates within the selected date range
</Image>

<Image title="2019-10-29 15_27_42-Window.png" alt={1907} border={true} src="https://files.readme.io/fde7306-2019-10-29_15_27_42-Window.png">
  Filter orders that have the execution dates within the selected date range
</Image>

## Bulk Update Orders

* Bulk update, as its name suggests, is the function to mass update a certain attribute of multiple Orders at once
* At the moment, the Bulk update function allows you to update the following attributes:
* 1 - Order Date
* 2 - Active Status
* 3 - Expected 

### Bulk Update Order Date

* You can update the Order Date attribute of multiple Orders at once. To do that, follow the steps below:
* Step 1: Tick the corresponding checkbox icons :fa-square-o: of the wanted Orders
* Step 2: Click the **Action** button located above the top right corner of the Order table
* Step 3: Click the **Update Order Date** option on the drop-down menu
* Step 4: The **Update Order Date** form will appear. On this form, click the calendar icon :fa-calendar: at the end of the date field. On the drop-down calendar, select the appropriate date. Alternatively, you can input the date directly on the date field following the ***mm/dd/yyyy (Month/Date/Year)*** format
* Step 5: Click **Update** to confirm the change

### Bulk Update Order Active Status

* You can update the Active Status of multiple Orders which have the ***Open/Planned*** Planning Status
* To do that, follow the steps below:
* Step 1: Tick the corresponding checkbox icons :fa-square-o: of the wanted Orders
* Step 2: Click the **Action** button located above the top right corner of the Order table
* Step 3: Click the **Update Active Status** option on the drop-down menu
* Step 4: The **Update Active Status** form displays. On this form, click on the field below the ***Active Status*** text. Select between the two statuses ***Active*** and ***Inactive***
* Step 5: After selecting the appropriate Active Status, click **Update**
* The system will update the Active Status of the selected Orders

<Image title="bulkupdateordereng.gif" alt={1912} border={true} src="https://files.readme.io/987fe37-bulkupdateordereng.gif">
  Illustration GIF (English)
</Image>

<Image title="bulkupdateordervie.gif" alt={1912} border={true} src="https://files.readme.io/7659d2e-bulkupdateordervie.gif">
  Illustration GIF (Vietnamese)
</Image>

* **Note**: 
* 1 - If the Planning Status of all selected Orders is ***Locked/Finalized***, you will not be able to change their Active Status. The system will display the following message:

<Image title="hg8ArQGOkS.png" alt={592} className="border" border={true} src="https://files.readme.io/66649e8-hg8ArQGOkS.png" />

* 2 - If among the selected Orders, some have the Planning Status to be ***Locked/Finalized*** and some have the Planning Status to be ***Open/Planned***, you will still be able to change the Active Status of the Open/Planned Orders. The system will display the following message:
* If you click **Confirm**, you can continue changing the Active Status of the Open/Planned Orders

<Image title="jis0zFc2fZ.png" alt={591} className="border" border={true} src="https://files.readme.io/e139bf5-jis0zFc2fZ.png" />

## Types Of Order Status

* An Order has various kind of statuses. Below are the list of all kinds of Order status, their meanings and possible values

### Order Status

* This status indicates the current state of the Order during the Delivery process
* Below are the possible statuses

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Possible statuses
      </th>

      <th>
        Status description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Open
      </td>

      <td>
        The default status of all newly created Orders
      </td>
    </tr>

    <tr>
      <td>
        Picking & Packing
      </td>

      <td>
        Products of the Orders are being picked from the warehouse shelves and packed into delivery boxes
      </td>
    </tr>

    <tr>
      <td>
        Picked & Packed
      </td>

      <td>
        Products of the Orders have been fully picked and packed into delivery boxes, ready to be loaded onto the delivery vehicles
      </td>
    </tr>

    <tr>
      <td>
        Shipping
      </td>

      <td>
        The Order is being carried by the delivery vehicles to the customers location
      </td>
    </tr>

    <tr>
      <td>
        Shipped
      </td>

      <td>
        The Order is being processed (Regardless of the delivery result)
      </td>
    </tr>

    <tr>
      <td>
        Canceled
      </td>

      <td>
        The Order is canceled by the dispatchers on Web app
      </td>
    </tr>
  </tbody>
</Table>

### Fulfillment Status

* This status indicates the delivery result of the Order
* Below are the possible statuses

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Possible statuses
      </th>

      <th>
        Status description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Not Fulfilled
      </td>

      <td>
        The default status of all newly created Orders\
        The products of the Order are still being carried on the delivery vehicle, haven't been handed to the customers yet
      </td>
    </tr>

    <tr>
      <td>
        Fulfilled
      </td>

      <td>
        All products in the Order were handed to the customer
      </td>
    </tr>

    <tr>
      <td>
        Partially Fulfilled
      </td>

      <td>
        Some, not all products in the Order were handed to the customer
      </td>
    </tr>

    <tr>
      <td>
        Unfulfilled
      </td>

      <td>
        There were no product handed to the customer
      </td>
    </tr>
  </tbody>
</Table>

### Planning Status

* This status indicates the current state of the Order within the Routing Plan
* Below are the possible statuses

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Possible statuses
      </th>

      <th>
        Status description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Open
      </td>

      <td>
        The default status of all newly created Orders\
        This status means the Order has not yet been put into the Route Plan Optimization process\
        Orders having this status can still be edited
      </td>
    </tr>

    <tr>
      <td>
        Planned
      </td>

      <td>
        An Order will have this status if it was successfully put on an optimized Delivery Route, but the optimized Delivery Route hasn't been locked yet\
        Orders having this status can still be edited
      </td>
    </tr>

    <tr>
      <td>
        Locked
      </td>

      <td>
        An Order will have this status if it was successfully put on an optimized Delivery Route, and the optimized Delivery Route has been locked\
        Orders having this status can't be edited
      </td>
    </tr>

    <tr>
      <td>
        Finalized
      </td>

      <td>
        An Order will have this status if the Delivery Route on which that Order was put has been finalized\
        Orders having this status can't be edited
      </td>
    </tr>
  </tbody>
</Table>

### Validation Status

* This status acts as a warning sign when the data of an Order violates a certain compulsory condition for it to be optimized
* Below are the possible statuses

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Possible statuses
      </th>

      <th>
        Status description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        No-coordinate
      </td>

      <td>
        The customer who placed the Order lacks coordinates information (Latitude; Longitude)
      </td>
    </tr>

    <tr>
      <td>
        Over-capacity
      </td>

      <td>
        The weight and/or volume of the Order exceeds the weight and/or volume capacity of all active vehicles in the Depot
      </td>
    </tr>

    <tr>
      <td>
        No-weight/volume
      </td>

      <td>
        Both the weight and volume of the Order equals zero, which means there is zero product loaded in that Order
      </td>
    </tr>
  </tbody>
</Table>

### Active Status

* This status determines whether an Order will be forwarded to the Route Planning process or not
* Below are the possible statuses

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Possible statuses
      </th>

      <th>
        Status description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Active
      </td>

      <td>
        The default status of all newly created Orders\
        Orders with this status will be forwarded to the Route Planning process
      </td>
    </tr>

    <tr>
      <td>
        Inactive
      </td>

      <td>
        Orders with this status will not be forwarded to the Route Planning process
      </td>
    </tr>
  </tbody>
</Table>

### Synchronization Status

> 🚧 This status is only intended for user accounts which use the external Transportation Management Systems (TMS)

* Displays the synchronization result of the Orders between Abivin vRoute and the external Transportation Management System (TMS)
* Below are the possible statuses

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Possible status
      </th>

      <th>
        Status description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Synced
      </td>

      <td>
        The orders were synced with the external TMS
      </td>
    </tr>

    <tr>
      <td>
        Not Synced
      </td>

      <td>
        The orders weren't synced with the external TMS
      </td>
    </tr>
  </tbody>
</Table>

### Pickup

* This status determines whether an Order is a Pickup Order or not
* Below are the possible statuses

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Possible status
      </th>

      <th>
        Status description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Yes
      </td>

      <td>
        The Order is a Pickup Order
      </td>
    </tr>

    <tr>
      <td>
        No
      </td>

      <td>
        The Order is not a Pickup Order
      </td>
    </tr>
  </tbody>
</Table>

### Order statuses during external TMS integration

> 🚧 This sections is only intended for user accounts that use external TMS

* Below is the changes in each Type of statuses of a particular Order during the integration with the external TMS

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>

      </th>

      <th>
        Planning Status
      </th>

      <th>
        Active Status
      </th>

      <th>
        Order Status
      </th>

      <th>
        Fulfillment Status
      </th>

      <th>
        Sync Status
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Before Route Planning
      </td>

      <td>
        Open
      </td>

      <td>
        Active
      </td>

      <td>
        Open
      </td>

      <td>
        Not Fulfilled
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        During Route Planning (Not yet locked Delivery Routes)
      </td>

      <td>
        Planned
      </td>

      <td>
        Active
      </td>

      <td>
        Open
      </td>

      <td>
        Not Fulfilled
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        During Route Planning (Locked Delivery Routes)
      </td>

      <td>
        Locked
      </td>

      <td>
        Active
      </td>

      <td>
        Picked & Packed
      </td>

      <td>
        Not Fulfilled
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        During Route Planning\
        (Finalized Delivery Routes)
      </td>

      <td>
        Finalized
      </td>

      <td>
        Active
      </td>

      <td>
        Picked & Packed
      </td>

      <td>
        Not Fulfilled
      </td>

      <td>
        No
      </td>
    </tr>

    <tr>
      <td>
        After TMS synchronization\
        (Manifest-In)
      </td>

      <td>
        Finalized
      </td>

      <td>
        Active
      </td>

      <td>
        Shipping\
        (= IN-TRANSIT)
      </td>

      <td>
        Fulfilled
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        When TMS sends "Delivered"  (Status-Out)
      </td>

      <td>
        Finalized
      </td>

      <td>
        Active
      </td>

      <td>
        Shipped\
        (= DELIVERED)
      </td>

      <td>
        Fulfilled
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        When TMS sends "Canceled" (Status-Out)
      </td>

      <td>
        Finalized
      </td>

      <td>
        Active
      </td>

      <td>
        Canceled
      </td>

      <td>
        Unfulfilled
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        When Planner manually closes Delivery Routes
      </td>

      <td>
        Finalized
      </td>

      <td>
        Active
      </td>

      <td>
        Shipped
      </td>

      <td>
        Fulfilled
      </td>

      <td>
        Yes
      </td>
    </tr>
  </tbody>
</Table>

## Unplanned (Missing) Orders & Failed Orders

## Unplanned (Missing) Orders

* Unplanned (Missing) Orders are Orders that the system automatically doesn't put into the optimized any Delivery Route during the Route Optimization process due to various reasons or have been successfully put into the optimized Delivery Routes but have later been manually removed off the optimized Delivery Routes by the users
* Please refer to the following article for in-depth details: [**Unplanned (Missing Orders)**](https://docs.abivin.com/docs/vrp-in-house-fleet-unplanned-missing-orders)

## Failed Orders

* Failed Orders: Orders that were successfully put into the optimized Delivery route during the Route Optimization process. However, during the Delivery process, the drivers could not deliver them to the customers for various reasons, which lead to them selecting [***Not Completed*** delivery result](https://docs.abivin.com/docs/vrp-in-house-fleet-driver-mobile-app#not-completed-result) on the Mobile app. On the Order list, the Fulfillment Status of Failed Orders are ***Unfulfilled***
* Please refer to the following article for in-depth details: [**Failed Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-failed-orders)

## Salesmen & Consumers Orders Approval

> 🚧 In order for this function to work, the configuration **Allow Approve Order** must be enabled at the Branch

* If there are Orders submitted from the Mobile app [by the Salesmen](https://docs.abivin.com/docs/vrp-in-house-fleet-salesman-mobile) or [by the Consumers](https://docs.abivin.com/docs/consumer-app-general-instruction), then you, as the dispatcher, have to make decisions whether to **Approve** - Allow those Orders to be performed, or **Reject** - Not allow those Orders to be performed. After you have made decisions about the Orders, you have to decide whether to put the approved Orders into the Route Plan Optimization process or not

### Approve/Reject orders

* Under **Approve** column, the recently submitted Orders will have two buttons: **Reject** (Red button with the symbol :fa-ban:) and **Approve** (Blue button with the symbol :fa-check-circle-o:)

<Image title="order_01.png" alt={1505} className="border" border={true} src="https://files.readme.io/2710df2-order_01.png" />

* To reject or approve an Order, simply click on the appropriate button and click **OK** on the confirmation dialog

<Image title="approve reject order.gif" alt={1908} className="border" border={true} src="https://files.readme.io/2d2e7f8-approve_reject_order.gif" />

### Put approved Orders into the Route Plan Optimization process

* By default, all approved Orders will be put into the Route Plan Optimization process, indicated by the value ***Active*** under the column **Active Status**
* If you do not wish to put certain Orders into the route optimization process, click on the value ***Active*** then select the value ***Inactive*** on the drop-down list

<Image title="not approved order.png" alt={1638} className="border" border={true} src="https://files.readme.io/149db3b-not_approved_order.png" />

## Automatically Split Over-capacity Orders

> ❗️ You have to enable the configuration **Split Delivery** at the **Branch**

* Over-capacity Orders are Orders which have the attribute **Weight** and/or **Volume** to exceed the carrying capacity of all active vehicles from the same Depot of those Orders
* During the Route Plan Optimization process, the system can automatically split those over-capacity Orders into smaller Orders to fit the capacity of the available active vehicles. If there are multiple over-capacity Orders, the system will start splitting from the largest over-capacity Orders to the highest capacity vehicle, and will continue to split lesser over-capacity Orders to lesser capacity vehicles
* The Orders automatically split from the original over-capacity Orders will be assigned Order Codes that equals to the Order Code of the original over-capacity Orders plus the suffix sharp symbol (#) and  ordinal number
* For example: The original over-capacity Order has the Order Code to be ***Order\_01***. The first Order split from tha original over-capacity Order will have the Order Code to be ***Order\_01#1***, the second Order split from the original over-capacity Order will have the Order Code to be ***Order\_01#2*** and so on
* Below is an illustration of an original over-capacity Order ***OD—17*** and three automatically split Orders off that original over-capacity Order: ***OD—17#1; OD—17#2; OD—17#3***

<Image title="tXSwyF78xT.png" alt={1685} className="border" border={true} src="https://files.readme.io/3dbb5a1-tXSwyF78xT.png" />

* **Notes:**
* During the Route Plan Optimization process, if you haven't locked the Delivery Routes on which exist the Orders that have been automatically split off the original over-capacity Orders, and you click on the button **Unlock**, then over at the tab **Orders > Sales Orders**, all the automatically split Orders will disappear, only the original Orders will remain

<Image title="split order.gif" alt={1916} className="border" border={true} src="https://files.readme.io/9dd2ac0-split_order.gif" />

## Manually split Orders

* You can manually split Orders before and during the Route Plan Optimization process

### Complusory configurations

* You have to enable the configuration **Allow Manual Split Order** at the **Manufacturer**. After enabling, make sure to log out then log in again in order for the configuration to take effect

> ❗️ Only Orders created AFTER this configuration has been enabled will be splitable (Having the icon Split)

### Manually split Orders before Route Plan Optimization process

* If the current Planning Status of an Order is ***Open***, which means that Order has not been put into any optimized Delivery Route, then you can split that Order into smaller Orders
* Click on the icon **Split** (Under the column **Edit**) of the Order you want to split

<Image title="screenshot-vapp.abivin.com-2020.05.31-20_54_05.png" alt={1700} border={true} src="https://files.readme.io/767f785-screenshot-vapp.abivin.com-2020.05.31-20_54_05.png">
  Split icon
</Image>

* The form **Split Order** will appear
* On the left of the form is the Original Order, and on the right of the form is the list of small Orders split from the Original Order

<Image title="S46hC8X0XT.png" alt={1626} className="border" border={true} src="https://files.readme.io/8e23a09-S46hC8X0XT.png" />

* To split the whole case/single item quantity of a particular product, input the desired value into the input box on the left of the current whole case/single item quantity. Perform the same step with other products. After you have input the appropriate whole case/single item quantity to be split, click on the double right angle icon **fa-angle-double-right** on the middle of the form
* As you click on that icon, a new Order will appear on the list **New Order**

<Image title="teuT62NWbm.gif" alt={1631} className="border" border={true} src="https://files.readme.io/d97701a-teuT62NWbm.gif" />

* The recently split Order will automatically be assigned an Order code that equals to the Order code of the Original Order plus the suffix sharp symbol (#) and an ordinal number
* For example: The Original Order has the Order Code to be ***Order\_01***. The first Order split from the Original Order will have the Order Code to be ***Order\_01#1***, the second Order split from the Original Order will have the Order Code to be ***Order\_01#2*** and so on
* Notice that the whole case/single item quantity and the Total Weight/Total Volume of the Original Order will decrease accordingly each time you split an Order off that Original Order
* You can continue to split new Orders off the Original Order by clicking on the plus icon :fa-plus: on the top right corner of the list **New Order**. As you click on this icon, a new tab will appear on the right of the previously split Order. Now you need to click on the tab title of the new to switch to the details of the that new Order. Now continue to split the whole case/single item quantity off the Original Order for that new Order using the steps described above

<Image title="h6wZkgiGKx.gif" alt={1627} className="border" border={true} src="https://files.readme.io/f762824-h6wZkgiGKx.gif" />

* On this form, you can remove a new Order that have been split off the Original Order by clicking on the remove icon :fa-close: on the tab title of that Order. After removing, the whole case/single item quantity that were allocated to that Order will automatically be added back to the remaining whole case/single item quantity of the Original Order

<Image title="remove split.png" alt={649} className="border" border={true} src="https://files.readme.io/1ad4330-remove_split.png" />

* After you have finished splitting the Original Order, click on the button **Split** on the form

<Image title="save split.png" alt={1534} className="border" border={true} src="https://files.readme.io/2e00714-save_split.png" />

* Once you finish splitting Orders and save, the Original Order Code will disappear. The remaining whole case/single item quantity of the Original Order will be saved into a new Order. The Order Code of the new Order equals to the Order Code of the Original Order, adding the suffix ***#*** plus the ordinal number right after the ordinal number of the last Order split off the Oiginal Order code
* For example: The Original Order has the Order Code ***SO-200414-00027***. You have split two (2) Orders off that Original Order in one turn. After saving, the remaining whole case/single item quantity of the Original Order will be saved into a new Order with the Order Code ***SO-200414-00027#3***

<Image title="remaining order.png" alt={1634} className="border" border={true} src="https://files.readme.io/b2c1629-remaining_order.png" />

* **Note**: 
* You can also split an Order that was earlier been split off from another Order

<Image title="VwEsk5OsPB.gif" alt={1920} className="border" border={true} src="https://files.readme.io/df80fa2-VwEsk5OsPB.gif" />

* If you delete ***all*** Orders that have been split off from an Original Order, the system will revive the Original Order

<Image title="UpG5aE9Iyk.gif" alt={1920} className="border" border={true} src="https://files.readme.io/6218db8-UpG5aE9Iyk.gif" />

### Manually split Orders during Route Plan Optimization process

* When you use the Route Plan (List View) feature to optimize the Orders, you can manually split Orders after the Delivery Routes on which those Orders are put have been locked
* Read more at the following article: [**Route Plan (List View)**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-list-view#manually-split-orders-on-locked-delivery-routes)

## Sales Order Master Filter Tool

* We have a powerful Order filter tool called **Master Filter** which can assist you greatly when you want to filter the Sales Order based on various attributes

### Access Order Master Filter Tool

* To access the Master Filter tool, click on the funnel icon to the left of the **Columns** button, located over the top right corner of the Order list table

<Image title="tviTZ7tB7K.png" alt={492} border={true} src="https://files.readme.io/bd394e9-tviTZ7tB7K.png">
  Illustration (English)
</Image>

<Image title="Cz1EUEgca8.png" alt={492} border={true} src="https://files.readme.io/0c735cd-Cz1EUEgca8.png">
  Illustration (Vietnamese)
</Image>

* Upon clicking, the Master Filter tool will appear like so

<Image title="X21ZIaxqcL.png" alt={702} border={true} src="https://files.readme.io/65bf314-X21ZIaxqcL.png">
  Illustration (English)
</Image>

<Image title="phaNA0MC31.png" alt={691} border={true} src="https://files.readme.io/679df7d-phaNA0MC31.png">
  Illustration (Vietnamese)
</Image>

### Create Filter On The Order Master Filter Tool

* On the tool, you will see three drop-down boxes.

<Image title="GeGhSS92AI.png" alt={692} border={true} src="https://files.readme.io/2b4b569-GeGhSS92AI.png">
  Illustration (English)
</Image>

<Image title="5DBI1tRkAg.png" alt={688} border={true} src="https://files.readme.io/3613a0f-5DBI1tRkAg.png">
  Illustration (Vietnamese)
</Image>

* The first drop-down box lets you select the Order attribute from the following: **Order Date; ETA at Delivery Stop; ETD at Delivery Stop; Estimated Distance; Planning Status; Active Status**
* The second drop-down box lets you select the operator related to the selected attribute
* The operator list will be different for different attributes:

#### Operators For The "Order Date; ETA at Delivery Stop; ETD at Delivery Stop" Attributes

* If the selected attribute is one of the following: **Order Date; ETA at Delivery Stop; ETD at Delivery Stop**, then the possible operators would be: **Is; Is Today; Is Before Date; Is After Date; Is Today & Earlier; Is Today & Later**
* The operator **Is** means you want to filter out the Orders of which the selected Order attribute (For example, Order Date) is a specific date. To select the date, click on the calendar icon :fa-calendar-o: on the third drop-down box and select the desired date. Alternatively, you can directly input the date into the box following the ***Month/Date/Year mm/dd/yyyy*** format
* The operator **Is Today** means the current date on your computer. If this operator is selected, the third drop-down box will gray out
* The operator **Is Before Date** means you want to filter out the Orders of which the selected Order attribute is within the range of a specific selected date and all the past dates (No limit) before the selected date
* The operator **Is After Date** means you want to filter out the Orders of which the selected Order attribute is within the range of a specific selected date and all the future dates (No limit) after the selected date
* The operator **Is Today & Earlier** means you want to filter out the Orders of which the selected Order attribute is within the range of the current date and all the past dates (No limit) before the current date
* The operator **Is Today & Later** means you want to filter out the Orders of which the selected Order attribute is within the range of the current date and all the future dates (No limit) after the current date

#### Operators For The "Estimated Distance" Attribute

* If the selected attribute is **Estimated Distance**, then the possible operators would be: **Is; Is Greater Than; Is Smaller Than**
* The operator **Is** means you want to filter out the Orders of which the estimated distance between the Depot and the Customer is a specific distance. Input the desired value (In kilometer, km) into the third box
* The operator **Is Greater Than** means you want to filter out the Orders of which the estimated distance between the Depot and the Customer is greater than a specific distance. Input the desired value (In kilometer, km) into the third box
* The operator **Is Smaller Than** means you want to filter out the Orders of which the estimated distance between the Depot and the Customer is smaller than a specific distance. Input the desired value (In kilometer, km) into the third box

#### Operators For The "Planning Status; Active Status" Attributes

* If the selected attribute is **Planning Status; Active Status**, then the possible operators would be: **Is**
* For the Planning Status attribute, the possible values from the third box would be: ***Open; Planned; Locked***
* For the Active Status attribute, the possible values from the third box would be: ***Active; Inactive***

### Create Additional Filters On The Order Master Filter Tool

* You can use a combination of more than one filter to filter out the desired Orders more precisely. To create an additional filter besides the existing ones, click the **+ ADD FILTER** button. Another row will appear below the previous filter
* At the beginning of the next row, there is a box to let you choose the relationship between the previous filter and the current filter.
* If you choose the operator **AND**, that means the system will filter out the Orders that satisfy ***both*** the previous filter and the current filter
* If you choose the operator **OR**, that means the system will filter out the Orders that satisfy ***either*** the previous filter or the current filter

### Use Filter/Group Of Filters

* After you have created the necessary filter/group of filters, click the **Apply** button to apply that filter/group of filters to the current Order list

<Image title="FIg3SHZDup.png" alt={691} border={true} src="https://files.readme.io/721cda0-FIg3SHZDup.png">
  Illustration (English)
</Image>

<Image title="xtAkrHgd6v.png" alt={690} border={true} src="https://files.readme.io/92fc4aa-xtAkrHgd6v.png">
  Illustration (Vietnamese)
</Image>

### Remove Filter From The Order Master Filter Tool

* To remove a filter, click the remove icon :fa-remove: at the end of the filter row

<Image title="xcLDmnBM8T.png" alt={692} border={true} src="https://files.readme.io/f794b13-xcLDmnBM8T.png">
  Illustration (English)
</Image>

<Image title="O9WXIRWPag.png" alt={690} border={true} src="https://files.readme.io/293b3be-O9WXIRWPag.png">
  Illustration (Vietnamese)
</Image>

### Save Filter/Group Of Filters As Templates

* You can save a filter/group of filters as a template and use the template in the future without having to set up the filter/group of filters from scratch every time
* To save a filter/group of filters as a template, click the **TEMPLATES** :fa-floppy-o: button

<Image title="syKRZIwnIA.png" alt={693} border={true} src="https://files.readme.io/6a5283f-syKRZIwnIA.png">
  Illustration (English)
</Image>

<Image title="dpLoJEJYXv.png" alt={695} border={true} src="https://files.readme.io/fce4b33-dpLoJEJYXv.png">
  Illustration (Vietnamese)
</Image>

* Upon clicking, the **Filter Template** form will appear. On this form, click on the **Save Active Filters** :fa-floppy-o: text

<Image title="Kw6kureK56.png" alt={691} border={true} src="https://files.readme.io/19df2c2-Kw6kureK56.png">
  Illustration (English)
</Image>

<Image title="LWpirfU30Q.png" alt={692} border={true} src="https://files.readme.io/02c1387-LWpirfU30Q.png">
  Illustration (Vietnamese)
</Image>

* Upon clicking, a form titled **Save New Filter** will appear. Input the name for the filter/group of filters you want to save into the **New Filter Name** field then click **Save**

<Image title="Mf2Mno8dv7.png" alt={493} border={true} src="https://files.readme.io/00a5414-Mf2Mno8dv7.png">
  Illustration (English)
</Image>

<Image title="3TPu4ivmXW.png" alt={494} border={true} src="https://files.readme.io/c197194-3TPu4ivmXW.png">
  Illustration (Vietnamese)
</Image>

* The template recently saved will appear under the **SAVE FILTERS** section

<Image title="aSQ7coK2sA.png" alt={441} border={true} src="https://files.readme.io/837113d-aSQ7coK2sA.png">
  Illustration (English)
</Image>

<Image title="PLGmDa6gOC.png" alt={440} border={true} src="https://files.readme.io/79bee18-PLGmDa6gOC.png">
  Illustration (Vietnamese)
</Image>

### Find Saved Filter Template

* To find a saved filter template, input the template name into the search bar :fa-search: at the top of the Filter Template form

<Image title="LPDpxhkPPn.png" alt={440} border={true} src="https://files.readme.io/c27ad1f-LPDpxhkPPn.png">
  Illustration (English)
</Image>

<Image title="3S0EmdifjE.png" alt={439} border={true} src="https://files.readme.io/5afd5ca-3S0EmdifjE.png">
  Illustration (Vietnamese)
</Image>

### Edit Name Of Saved Filter Template

* To edit the name of a saved filter template, click on its respective **Edit** icon :fa-pencil:. Upon clicking, the name field of the saved filter template will become editable. Edit as you wish then click the checkmark icon :fa-check: to save the new name. If you wish to discard the change and remain the current name, click the clear icon :fa-remove:

<Image title="jFbrFbbYtK.png" alt={412} border={true} src="https://files.readme.io/bb0e082-jFbrFbbYtK.png">
  Illustration (English)
</Image>

<Image title="0Fd6T7qJLS.png" alt={420} border={true} src="https://files.readme.io/4e53e79-0Fd6T7qJLS.png">
  Illustration (Vietnamese)
</Image>

### Delete Saved Filter Template

* To delete a saved filter template, click on its respective **Remove** icon :fa-trash: 

## Beginner's Guide

Now that you have done creating Organization Modules, Users, Vehicles, Customers and Products, you are ready to create a Sales Order.

### Create a Sales Order

* Creating a single sales order using Web form can be done through the following steps:
* Step 1: Navigate to **Orders > Sales Orders** tab.
* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Create** (the :fa-pencil: symbol).

![2880](https://files.readme.io/d0f5ba3-Screen_Shot_2021-01-22_at_17.05.25.png "Screen Shot 2021-01-22 at 17.05.25.png")

* Step 3: Input information into the required fields:
* **Order Code:** Input the management code assigned to the Order.
* **Order Date:** Input the date on which the Order is planned to be performed and completed.
* **From Depot:** Input the Depot from where the Order will start, then choose the suitable value from the drop down menu.
* **To Customer:** Input the Customer Code of the customer that creates the Sales Order, then choose from the drop down menu.

![2880](https://files.readme.io/ff5aea1-Screen_Shot_2021-01-22_at_17.26.19.png "Screen Shot 2021-01-22 at 17.26.19.png")

* **Product:** Click on the field on the same row with the button **Add Product** (Below the text **Search**). On the search bar, input the **Product Name/Product Code** of the wanted Product, then select the returned value. Next, click on the button **Add Product** to add that Product to the Order. The recently added Product will appear on the Product table below. Finally, input the number of ***Cases*** and ***Items*** (if any) into the table. 

![2880](https://files.readme.io/21fedaa-Screen_Shot_2021-01-22_at_17.29.00.png "Screen Shot 2021-01-22 at 17.29.00.png")

* Step 4: Click **SAVE**.
