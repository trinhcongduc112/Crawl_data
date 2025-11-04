---
title: Why I cannot fetch old orders?
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
## I. Why I cannot fetch completed orders in the past?

**:fa-angle-right:Case:** The Fulfillment status of order SO-210720-001 was ***"Fulfilled"*** which means that this order was delivered successfully on 20/07/2021. As tomorrow has an alike order, you want to fetch order SO-210720-001 from 20/07 to 21/07. 

![1920](https://files.readme.io/1055fa8-Fcomplete1.png "Fcomplete1.png")

* Nevertheless, when you use  Old Order] fun function to get past order, there is no option for ***Completed orders***.

![1920](https://files.readme.io/6849f72-Fcomplete2.png "Fcomplete2.png")

**:fa-angle-right:Reason:** The system does not allow to fetch completed orders in the past due to an impact on Abivin's reports.

**:fa-angle-right:Solution:** In this situation, if you want to create an alike order as order SO-210720-001, please create new order with the same inputs but different order code via Web form or Excel file. Please read more [here](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#create-sales-orders) to know how to create a new order.

## II. Why I cannot fetch Not-Fulfilled orders in the past?

**:fa-angle-right:Case:** Regarding the image below, as the Fulfillment status of the order SO-210720-001 on 20/07/2021 was ***"Not Fulfilled"***, you want to fetch this order to 21/07/2021 to re-deliver.

![1920](https://files.readme.io/40fb708-1.png "1.png")

* Nevertheless, when you use rder] function  function to get past order, there is no option for ***Not fulfilled orders***.

![1920](https://files.readme.io/7e4689e-2.png "2.png")

**:fa-angle-right:Reason:** The system does not allow to fetch Not fulfilled Orders in the past due to an impact on Abivin's reports.

**:fa-angle-right:Solution:** Please choose the two following options to cope with the case:

1. Create new order with the same inputs but different order code via Web form or Excel file. Please read more [here](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#create-sales-orders) to know how to create a new order.
2. Notice the driver to submit ***"Not Complete"*** and select reasons in the Mobile App.

<Image title="3.jpg" alt={1125} width="smart" src="https://files.readme.io/1f75858-3.jpg" />

The Order's Fulfillment Status will then change to ***"Unfulfilled"*** and will be allowed to fetch to the day after using ].
[block:image.

![1920](https://files.readme.io/c720cd8-4.png "4.png")

> 📘 Notice
>
> * In order to know more about the  function, please find more information [here](https://docs.abivin.com/docs/vrp-in-house-fleet-failed-orders#route-plan-optimization-process).
> * If you are not clear about the "Fulfillment Status", please read more [here](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#types-of-order-status) to understand the how this status runs.
