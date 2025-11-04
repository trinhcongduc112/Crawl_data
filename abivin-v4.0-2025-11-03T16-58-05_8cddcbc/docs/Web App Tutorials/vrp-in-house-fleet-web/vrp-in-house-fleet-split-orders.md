---
title: Split Sales Orders
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
* By default, the system is configured so that ***each customer (delivery point) will be visited by one delivery vehicle in a whole route plan***. Therefore, if a customer places multiple orders, there could be two situations:
* **Situation 1:** The total weight/volume of these orders is less than or equal to the capacity of an active vehicle, the system will consolidate these orders to that vehicle
* **Situation 2:** The total weight/volume of these orders exceeds the capacity of every active vehicle. The system will not be able to automatically split these orders to several vehicles and therefore can not generate routes
* If situation 2 happens, you can use the **Split order** configuration to avoid cramming too many orders to one vehicle, by allocating each of these orders to one independent vehicles

## Configure orders to be Split orders

## Configure orders on Web form

* If you use Web form to create orders, click on **Splitted Order** check box for every order delivered to one customer

<Image title="2019-09-24 14_02_13-Window.png" alt={1658} className="border" border={true} src="https://files.readme.io/2d89479-2019-09-24_14_02_13-Window.png" />

## Configure orders on Excel template

* For all orders planned to be delivered to a specific customer, type **TRUE** into the **Splitted Order** field if you want them to be split orders

<Image title="2019-09-24 11_57_26-Window.png" alt={1606} className="border" border={true} src="https://files.readme.io/fefa723-2019-09-24_11_57_26-Window.png" />

## Perform Route optimization

* After configuring the orders as above, you can proceed to perform route optimization as usual. Each of the Split orders delivered to one customer will be assigned to one independent vehicle

<Image title="2019-09-24 17_23_44-Window.png" alt={1674} border={true} src="https://files.readme.io/8861494-2019-09-24_17_23_44-Window.png">
  Two independent vehicles delivering two split orders to one customer
</Image>

* **Note:** You will not be able to drag split orders from a vehicle to another vehicle

<Image title="drag split order.gif" alt={1676} className="border" border={true} src="https://files.readme.io/2d8b15b-drag_split_order.gif" />
