---
title: Inventory Quantities
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
In inventory management, it is easy to overlook the precision of SKU quantity in the warehouse. Answering the question "How many SKUs do we have at the moment?" is not that obvious. How do you define "to have"? Are the in-transit products just leaving the warehouse counted in the quantity we are having? Are the products purchased two days ago, coming into the warehouse counted in the quantity? What is the correct quantity we can sell today or sell for the next 2 days? This page aims to make this concept clear.

A warehouse manager worries the most about the right **On-hand Quantity** inside the warehouse. One must make sure the goods are taken out with a [Sales Orders](doc:orders#section-sales-order) and brought in with a [Purchase Order](doc:orders#section-purchase-order). Without these orders, a warehouse manager must fight to his death to protect the goods inside the warehouse.

We define the following quantities to be tracked per SKU or Product Code in Abivin vRoute v3.0:

* On-hand quantity: the total of items we have physically available on the warehouse shelf
* Picked quantity: the total number of items that have already been picked in sales orders and are awaiting shipment in the shipping area.
* On-SOrder quantity: the total number of items ordered by your customers (across all Sales orders that are not yet on Status "Shipped"). This number is what you need to be fulfilling to complete sales!
* On-POrder quantity: This number is how many you’ve ordered from your supplier/vendor but haven’t received. This also includes quantities of items being made in a work order.
* Owned quantity: This is the number of items you possess. It is equal to the total of On-hand quantity and Picked quantity.
* Available quantity: This is the number of items you have left if you fulfill all open Sales Orders and is therefore equal to Owned quantity – On-SOrder Quantity. (i.e. what’s left after you’ve shipped all your current orders).
* Anticipated Quantity: This determines whether or not you need to reorder more stock. It equals Owned quantity – On-SOrder quantity + On-POrder quantity. This way, it takes into account all physical items, subtracts the number you need to fulfill to your customers, and adds the number you already have on open Purchase Orders.
