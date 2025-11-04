---
title: Why I cannot change the Order date?
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
## Why I cannot change the Order date?

:fa-angle-right: **Case:** After choosing dit] a a specific order, changing the Order Date and ave], , the system pops up a notification "Order code exists". 

![1920](https://files.readme.io/f011226-Gif1.gif "Gif1.gif")

:fa-angle-right: **Reason:** The Order was an Unfulfilled Order or Missing Order existing in the past and re-delivered using Fetch Order feature. If the Order date is changed, there will be a new order coinciding with the Past Order which is not allowed to happen. In order to know whether the Order is Fetch Order or not, follow these instructions:

* **Step 1:** Go to er], se, search you want-to-change order code.
* **Step 2:** If that Order code is filled in green color, it is a fetch order.

![1920](https://files.readme.io/86e858c-1.png "1.png")

:fa-angle-right: **Solution:** Below are 3 solutions to change the Order date even the order is a fetch order.

* **Solution 1:** Add prefix to the Order code.

![1920](https://files.readme.io/eee10b1-Gif2.gif "Gif2.gif")

> 📘 Notice
>
> You can edit the Order Code only when the route plan for that order is not locked. Therefore, the above solution is for fetched order but not the past order which the route plan was locked.

* **Solution 2:** Delete past order.

![1920](https://files.readme.io/0336469-2.png "2.png")

> 📘 Notice
>
> * Please remember to lengthen the duration to view all the past orders. 

* **Solution 3:** Create new order with different order code but the same inputs directly on the website or via file uploading. Please read more in [Manage Sales Orders](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders) to know how to create or import new orders.

![1920](https://files.readme.io/d13eb66-3.png "3.png")
