---
title: How to update inventory of 1-way order
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
Initially, the quantity of the product SP005 is 1000

![1366](https://files.readme.io/c2cf7b7-2.0.png "2.0.png")

Step 1: Create a sales order of SP005 with 200 units

![1366](https://files.readme.io/2c69bf7-2.1.png "2.1.png")

Step 2: Once the controlling company selects the first point, 200 units will appear in the On-SOrder

![1366](https://files.readme.io/b9a1f84-2.2.png "2.2.png")

Step 3: KSXOUT changes the Order status to Picked and Packed when driver picks up the goods

![1366](https://files.readme.io/b40fc51-2.3.png "2.3.png")

\*200 units move from the On-hand column to the Picked column. The quantity in the On-hand will reduce from 1000 to 800

![1366](https://files.readme.io/30ab381-2.4.png "2.4.png")

Step 4: When the driver finishes delivery, transporter account changes the Order status to Shipped

![1366](https://files.readme.io/0ee3b8a-2.5.png "2.5.png")

The inventory quantity of On-SOrder and Picked disappears, 800 units appear in the On-hand column

![1366](https://files.readme.io/081bdfd-2.6.png "2.6.png")

* If the order is not fulfilled, the depot account will change the Order status to Canceled. Then the On-SOrder column will reduce a quantity equal to the amount ordered in the sales order
