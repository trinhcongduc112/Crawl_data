---
title: Unplanned (Missing) Orders
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
> 📘 This article only provides information about Unplanned (Missing) Orders on the Route Plan (Map View) screen. For the Route Plan (List View) screen, please refer to the following article: [**Route Plan (List View)**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-list-view#move-unplanned-orders-back-to-delivery-route)

## Unplanned (Missing) Order Definition

* Unplanned (Missing) Orders are 1. Orders that the system does not put into the optimized Delivery Routes during the Route Plan Optimization process because they violate certain constraints, or 2. Orders that the system puts into the optimized Delivery Routes during the Route Plan Optimization process, but have been manually removed from the optimized Delivery Routes by the Route Dispatchers

## Identify Unplanned (Missing) Orders

### Identify Unplanned (Missing) Orders During The Order Creation Process

* Right after an Order has been created using the Webform or the Excel import file, the system has a nifty feature to warn you if an Order will be treated as an Unplanned (Missing) Order or not. This can help you save time to troubleshoot the problem
* First, on the Order list table, show the **Validation Status** column

<Image title="HbfMnUMKHn.png" alt={337} border={true} src="https://files.readme.io/b43424d-HbfMnUMKHn.png">
  Illustration (English)
</Image>

<Image title="J5mXhaDFZY.png" alt={181} border={true} src="https://files.readme.io/9c9133f-J5mXhaDFZY.png">
  Illustration (Vietnamese)
</Image>

* Then, look at the statuses of the Orders under this column. There are three statuses that will confirm an Order as the Unplanned (Missing) Order:
* 1 - **Over-capacity**: The Order's weight and/or volume exceeds the weight and/or volume capacity of every active Vehicle of the Depot from where that Order originates
* 2 - **No-coordinate**: The Customer of that Order doesn't have enough coordinate information. They lack the latitude or the longitude or both
* 3 - **No weight/volume**: All the Products in the Orders don't have the weight and/or volume information

<Image title="d5tC2K80Sg.png" alt={1717} border={true} src="https://files.readme.io/44fe37a-d5tC2K80Sg.png">
  Illustration (English)
</Image>

<Image title="6.png" alt={1690} src="https://files.readme.io/cff6d11-6.png">
  Illustration (Vietnamese)
</Image>

* Note: At the moment, the system only compares an Order's weight/volume against the weight/volume capacity of the active Vehicles right at the moment that Order is created. Therefore, if the Order is identified as over-capacity at the time of its creation, then the ***Over-capacity*** status will still persist even if you create new Vehicles, edit the existing active Vehicles, or switch the inactive but capacity-satisfied Vehicles into active status. However, when you carry out the Route Plan optimization process, the system will still be able to put that over-capacity Order into an optimized Delivery Route if there are capacity-satisfied active Vehicles

### Identify Unplanned (Missing) Orders During The Route Plan Optimization Process

* During the Route Plan optimization process, if the system detects some Orders as Unplanned (Missing) Orders, then the system will not put those Orders into any optimized Delivery Route of the Vehicles
* The list of Unplanned (Missing) Orders will appear right below the timeline bar of the Timeline panel, above the timelines of the Vehicle
* Note that the Timeline panel will only show a maximum of ***5*** Unplanned (Missing) Orders. To see more Unplanned (Missing) Orders, click the right caret icon :fa-caret-square-o-right: located to the right of the Unplanned (Missing) Orders list

<Image title="lVQHdTLzGU.png" alt={658} border={true} src="https://files.readme.io/90c229c-lVQHdTLzGU.png">
  Missing Orders (English)
</Image>

<Image title="1. Missing Orders (VIE) 2.png" alt={1052} src="https://files.readme.io/e911881-1._Missing_Orders_VIE_2.png">
  Missing Orders (Vietnamese)
</Image>

* To see the whole list of Unplanned (Missing) Orders of the current Route Plan, click the three dots button at the very end of the Timeline panel

<Image title="5zeQlOmbn7.png" alt={1543} className="border" border={true} src="https://files.readme.io/7e3ec9c-5zeQlOmbn7.png" />

* Alternatively, you can click the **Missing Orders** button located on the top right corner of the map screen

<Image title="mjxqJJRtU5.png" alt={498} border={true} src="https://files.readme.io/72406c8-mjxqJJRtU5.png">
  Illustration (English)
</Image>

<Image title="7.png" alt={452} src="https://files.readme.io/9d4efe1-7.png">
  Illustration (Vietnamese)
</Image>

* As you click either of those buttons, the **Missing Orders** form will appear. This form will group the Unplanned (Missing) Orders by Customers

- To view the detailed reason why a specific Order was deemed an Unplanned (Missing) Order, click on the respective Order Code of that Order. As you click, another form will pop out. On this form, the system will list all the available active Vehicles of the same Branch (Not just the same Depot) from where that Unplanned (Missing) Orders originates as well as the corresponding reason why the system can not put that Order into the optimized Delivery Route of each of those active Vehicles, if available

<Image title="morders.gif" alt={1904} border={true} src="https://files.readme.io/2bfcadf-morders.gif">
  Missing Orders Form (English)
</Image>

![1920](https://files.readme.io/91ebdd8-lololololol.gif "lololololol.gif")

## Unplanned (Missing) Order reasons

* Below are some common reasons of Unplanned (Missing) Orders
* **Reason 1: Over Capacity** The weight and/or volume of the order exceeds the weight and/or volume capacity of every available vehicles

<Image title="1.png" alt={1515} border={true} src="https://files.readme.io/425f2e2-1.png">
  Reasons - Overcapacity (English)
</Image>

<Image title="3. Reasons - Over-Capacity.png" alt={1477} src="https://files.readme.io/421c2d6-3._Reasons_-_Over-Capacity.png">
  Reasons - Overcapacity (Vietnamese)
</Image>

* **Reason 2: This Vehicle capacity does not have enough space to deliver this Order. Please check the Vehicle volume and weight** The vehicle has been assigned some orders and thus doesn't have enough weight and/or volume capacity left to deliver that missing order

<Image title="2.png" alt={1513} className="border" border={true} src="https://files.readme.io/f528469-2.png" />

* **Reason 3: Open/Close time of Customer does not match with Vehicle visit time** The planned arrival time of the vehicle is out of the working time of the customer

<Image title="3.png" alt={1554} className="border" border={true} src="https://files.readme.io/d812a49-3.png" />

* **Reason 4: This Vehicle's temperature does not match with Product's temperature. Please check Vehicle's temperature** The vehicle doesn't support a particular product's temperature level included in the missing order

<Image title="4.png" alt={1528} className="border" border={true} src="https://files.readme.io/3eb9e3e-4.png" />

* **Reason 5: This vehicle belongs to a different Depot, therefore can not deliver this order** The order and the available vehicles don't belong to the same Depot/Sun

<Image title="5.png" alt={1512} className="border" border={true} src="https://files.readme.io/40cacf8-5.png" />

* **Reason 6:** The planned delivery time of the order is out of the vehicle working hours

<Image title="6.png" alt={1557} border={true} src="https://files.readme.io/6614d3a-6.png">
  Reasons - Vehicles' Close Time (English)
</Image>

<Image title="3. Reasons - Closed Time.png" alt={1492} src="https://files.readme.io/024e130-3._Reasons_-_Closed_Time.png">
  Reasons - Vehicles' Close Time (Vietnamese)
</Image>

* **Reason 7:** The customer belongs to a particular Customer group that the vehicle can not deliver to

<Image title="7.png" alt={1522} className="border" border={true} src="https://files.readme.io/290053a-7.png" />

* The working time of the Crossdock is not enough for the vehicle to come and load product

<Image title="8.png" alt={1546} className="border" border={true} src="https://files.readme.io/b988de8-8.png" />

* The customer was configured to be **Truck only** or **Bike only** - Only accept the delivery medium to be Truck or Bike, and there is no available vehicle that meets that requirement

<Image title="9.png" alt={1542} border={true} src="https://files.readme.io/9ec9906-9.png">
  Reasons - Truck Only (English)
</Image>

<Image title="3. Reasons - Truck Only.png" alt={1491} src="https://files.readme.io/bd7fcb6-3._Reasons_-_Truck_Only.png">
  Reasons - Truck Only (Vietnamese)
</Image>

<Image title="10.png" alt={1527} border={true} src="https://files.readme.io/7c6e230-10.png">
  Reasons - Bike Only (English)
</Image>

<Image title="3. Reasons - Bike Only.png" alt={1495} src="https://files.readme.io/9f530ff-3._Reasons_-_Bike_Only.png">
  Reasons - Bike Only (Vietnamese)
</Image>

## Retrieve Unplanned (Missing) Orders From Past Dates

* You can retrieve Unplanned (Missing) Orders from past dates and put them in the Order list of future dates so that you can attempt to replan them in the future Route Plans

## Compulsory Configurations

* First, you need to enable the **Allow Re-delivery Order** configuration at the **Manufacturer** (Located in the **More Configurations > System** section)

<Image title="4. Allow Re-Delivery Order.png" alt={935} src="https://files.readme.io/2c21543-4._Allow_Re-Delivery_Order.png">
  Allow Re-Delivery Order (English)
</Image>

<Image title="4. Allow Re-Delivery Order (VIE).png" alt={934} src="https://files.readme.io/db38dfb-4._Allow_Re-Delivery_Order_VIE.png">
  Allow Re-Delivery Order (Vietnamese)
</Image>

* The CRUD rights of the Administrator User group also needs to be updated. For module **Orders**, the check box under the column **Integration – Input** must be ticked

<Image title="5. Integration - Input (ENG).png" alt={1060} border={true} src="https://files.readme.io/49391f6-5._Integration_-_Input_ENG.png">
  Integration - Input (English)
</Image>

<Image title="5. Integration - Input (VIE) 2.png" alt={1056} src="https://files.readme.io/1113e9a-5._Integration_-_Input_VIE_2.png">
  Integration - Input (Vietnamese)
</Image>

### Procedure to retrieve Missing Orders

* Navigate to the **Orders > Sales Orders** tab

* Hover your mouse over the icon :fa-plus-circle:, then click on the icon **Fetch old order** :fa-refresh:

* The form **Get Past Order** will appear

* On this form, click on the field **Branch**. From the drop-down menu, select the branch from which you want to retrieve Missing Orders

* Next, click on the calendar icon :fa-calendar-o: under the text **Get Failed Orders Date**. On the drop-down calendar, select the date on which there were Missing Orders

* Then, click on the calendar icon :fa-calendar-o: under the text **Delivery Date**. On the drop-down calendar, select the date on which you want to replan the Missing Orders

* **(Important)** Click on the check box **Missing orders** to specify that you want to retrieve Missing Orders

* (Optional) You can also click on the check box **Not completed delivery** to also retrieve Failed Orders from the same selected date as the Missing Orders

* Finally, click on the button **Fetch Order**

* The system will immediately find the Missing Orders from the selected past date, then create ***new Orders*** that retain the same ***Order Codes*** attribute as those Missing Orders, and put them to the Order list of the selected future date

* On the Order list, Orders that were created based on Missing Orders will be highlighted with green color

* See the illustration below to have a better understanding of this function

<Image title="get failed orders.gif" alt={1904} border={true} src="https://files.readme.io/669e3a5-get_failed_orders.gif">
  Get Failed Orders (English)
</Image>

<Image title="0202020202020202020.gif" alt={1920} src="https://files.readme.io/31ac6dc-0202020202020202020.gif">
  Get Failed Orders (Vietnamese)
</Image>
