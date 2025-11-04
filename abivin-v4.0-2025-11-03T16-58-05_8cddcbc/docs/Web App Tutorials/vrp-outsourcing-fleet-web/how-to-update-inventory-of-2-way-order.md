---
title: How to update inventory of 2-way order
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
Initially, the quantity of the product SP001 is 1000

![1366](https://files.readme.io/869e666-4.0.png "4.0.png")

Step 1: Create a sales order of SP001 with 300 units

![1366](https://files.readme.io/e5616a4-4.1.png "4.1.png")

300 inventory units will be displayed in the On-SOrder column

![1366](https://files.readme.io/16d0399-4.2.png "4.2.png")

Step 3: The transporter changes the Order status to Picked and Packed when driver picks up the goods at delivery point\
\--> 300 inventory units will appear in the Returning and On-ROrder

![1366](https://files.readme.io/bb8b902-3.3.png "3.3.png")

Step 3: The driver delivers the goods to the depot, the depot accounts will change the Order status to Shipped\
\--> 300 units of On-ROrder and Returning will move to the On-hand column. The quantity of On-hand increases from 1000 to 1300

![1366](https://files.readme.io/520f60f-4.4.png "4.4.png")

* If the order is not fulfilled, the transporter account will change the Order status to Canceled. Then the On-ROrder column will reduce a quantity equal to the amount ordered in the sales order
