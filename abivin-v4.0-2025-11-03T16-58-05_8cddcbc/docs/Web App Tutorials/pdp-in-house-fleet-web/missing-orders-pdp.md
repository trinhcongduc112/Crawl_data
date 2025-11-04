---
title: Missing Orders PDP
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
## Missing Orders definition

* Missing Orders are Orders that can not be put into the optimized Delivery routes during the Route Optimization process due to various reasons.

## Locate Missing Orders

* During the Route Optimization process, on the Route Map screen, the Missing Orders will appear on the Timeline panel, right under the time bar.
* To view the entire list of missing orders, click on **Missing Orders** button on the top right of the map screen.
* The **Missing Orders** form will appear. You can click on the Order Code of a Missing Order to see the reason why that Order can not be put into the optimized Delivery route. The system will list all available active vehicles of the Branch from which that Missing Order also originates, and the corresponding why that Order can not be put into the Delivery route of those vehicles.

<Image title="morders.gif" alt={1904} className="border" border={true} src="https://files.readme.io/2bfcadf-morders.gif" />

## Missing Order reasons

* Below are some common reasons of Missing Orders.
* **Reason 1: Over Capacity** The weight and/or volume of the order exceeds the weight and/or volume capacity of every available vehicle.

<Image title="1.png" alt={1515} className="border" border={true} src="https://files.readme.io/425f2e2-1.png" />

* **Reason 2: This Vehicle capacity does not have enough space to deliver this Order. Please check the Vehicle volume and weight** The vehicle has been assigned some orders and thus doesn't have enough weight and/or volume capacity left to deliver that missing order.

<Image title="2.png" alt={1513} className="border" border={true} src="https://files.readme.io/f528469-2.png" />

* **Reason 3: Open/Close time of Customer does not match with Vehicle visit time** The planned arrival time of the vehicle is out of the working time of the customer.

<Image title="3.png" alt={1554} className="border" border={true} src="https://files.readme.io/d812a49-3.png" />

* **Reason 4: This Vehicle's temperature does not match with Product's temperature. Please check Vehicle's temperature** The vehicle doesn't support a particular product's temperature level included in the missing order.

<Image title="4.png" alt={1528} className="border" border={true} src="https://files.readme.io/3eb9e3e-4.png" />

* **Reason 5: This vehicle belongs to a different Depot, therefore can not deliver this order** The order and the available vehicles don't belong to the same Depot.

<Image title="5.png" alt={1512} className="border" border={true} src="https://files.readme.io/40cacf8-5.png" />

* **Reason 6:** The planned delivery time of the order is out of the vehicle working hours.

<Image title="6.png" alt={1557} className="border" border={true} src="https://files.readme.io/6614d3a-6.png" />

* **Reason 7:** The customer belongs to a particular Customer group that the vehicle can not deliver to.

<Image title="7.png" alt={1522} className="border" border={true} src="https://files.readme.io/290053a-7.png" />

* The working time of the Depot is not enough for the vehicle to come and load product.

<Image title="8.png" alt={1546} className="border" border={true} src="https://files.readme.io/b988de8-8.png" />

* The customer was configured to be **Truck only** or **Bike only** - Only accept the delivery medium to be Truck or Bike, and there is no available vehicle that meets that requirement.

<Image title="9.png" alt={1542} className="border" border={true} src="https://files.readme.io/9ec9906-9.png" />

<Image title="10.png" alt={1527} className="border" border={true} src="https://files.readme.io/7c6e230-10.png" />

## Retrieve Missing Orders from past dates

* You can retrieve Missing Orders from past dates and put them in the Order list of future dates so that you can attempt to replan them in future routing plans.

## Required Configurations

* You need to enable the following configuration at the **Branch**: **Allow Re-delivery Order**
* The CRUD rights of the Administrator User group also needs to be updated. For module **Orders**, the checkbox under the column **Integration – Input** must be ticked.

<Image title="bommpa7HUd.png" alt={815} className="border" border={true} src="https://files.readme.io/e25d917-bommpa7HUd.png" />

## Procedure to retrieve Missing Orders

* Navigate to **Orders > Sales Orders** tab.
* Hover your mouse over the icon :fa-plus-circle:, then click on the icon **Fetch old order** :fa-refresh:
* The form **Get Past Order** will appear.
* On this form, click on the field **Branch**. From the drop-down menu, select the branch from which you want to retrieve Missing Orders.
* Next, click on the calendar icon :fa-calendar-o: under the text **Get Failed Orders Date**. On the drop-down calendar, select the date on which there were Missing Orders.
* Then, click on the calendar icon :fa-calendar-o: under the text **Delivery Date**. On the drop-down calendar, select the date on which you want to re-plan the Missing Orders.
* **(Important)** Click on the checkbox **Missing orders** to specify that you want to retrieve Missing Orders.
* (Optional) You can also click on the checkbox **Not completed delivery** to also retrieve Failed Orders from the same selected date as the Missing Orders.
* Finally, click on the button **Fetch Order**.
* The system will immediately find the Missing Orders from the selected past date, then create ***new Orders*** that retain the same ***Order Codes*** attribute as those Missing Orders, and put them to the Order list of the selected future date.
* On the Order list, Orders that were created based on Missing Orders will be highlighted with green colour.
* See the illustration below to have a better understanding of this function.

<Image title="get failed orders.gif" alt={1904} className="border" border={true} src="https://files.readme.io/669e3a5-get_failed_orders.gif" />
