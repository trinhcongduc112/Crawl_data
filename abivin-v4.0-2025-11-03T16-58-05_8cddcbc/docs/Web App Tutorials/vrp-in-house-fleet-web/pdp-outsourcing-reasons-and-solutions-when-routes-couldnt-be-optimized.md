---
title: Find reasons and solutions when routes couldn't be optimized
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
In the route optimization phase, there are occasions when the dispatchers can not optimize routes for some, or all orders. The system will return a message saying you need to check the input data. There could be a number of reasons that contribute to this issue. 

Below we have outlined some of the most common reasons, and also provide solution to each of the reason.

## Scenario 1: Improper vehicle capacity setup

## Description

* Capacity (Weight and/or volume) properties of the vehicle are setup less than those of the order
* For example, an order is weighted at 1500 kg, while the vehicle assigned to that order only has a capacity limit of 1000 kg

## Solution

* Edit the weight and volume properties of the vehicle to make sure they are greater than those of the order

## Scenario 2: Improper coordinates setup

## Description

* Customers and/or depots don't have coordinates (latitude, longitude) information

## Solution

* Check the configuration of the customers and depots. Provide accurate coordinates for the ones that are missing.
* Read more on how to get coordinates for places at [How to: Get accurate coordinates of places](https://docs.abivin.com/docs/how-to-get-coordinates-of-places)

## Scenario 3: Incompatible active times between vehicles and customers

## Description

* Active time of vehicles do not match active time of customers
* For example, active time of a vehicle is from 5:00 to 11:00, whereas active time of a customer is from 12:00 to 20:00

## Solution

* Reconfigure the **Open time**, **Close time** properties of the customers and/or **Start time**, **Stop time** properties of the vehicles so that there is overlap time between the active time periods of these two objects. The overlap period would be the time when the vehicles can deliver order to the customers
* For example, if we reconfigure the active time of the vehicle above as 5:00 to 17:00, then the vehicle would be able to deliver to the customer from 12:00 to 17:00

## Scenario 4: Incorrect time format setup

## Description

* Incorrect time format setup of vehicles and/or customers, does not match hh:mm 24 hour time format
* For example, a vehicle's stop time is input as 6.20 P.M. This is incorrect. The correct format should be 18:20

## Solution

* Check and set time points exactly to hh:mm 24 hour time format for all vehicles and customers (**Start time, Stop time, Lunch start time, Lunch stop time** for vehicles and **Open time, Close time** for customers)

## Scenario 5: Improper drivers and vehicles assignment

## Description

* Drivers aren't assigned vehicle types during set up, or drivers have been assigned vehicle types, but none vehicle of that vehicle types is active

## Solution

* Check and make sure drivers have been assigned vehicle type. Then check to make sure the driver's assigned vehicle type actually has active vehicles when creating orders

## Scenario 6: Inadequate active time for orders that require more than 24 hours to complete

## Description

* Active time setup for vehicles and/or customers are within a 24 hour period (From 00:00 to 23:59), while the generated routes for the orders requires more than 24 hour to complete

## Solution

* For long-distance customers, whose orders require more than 24 hours to complete, and the vehicles used to deliver to these customers, reconfigure the **Stop time** property of the vehicles and **Close time** property of the customers to more than 24:00 point (For example 150:00).

## Scenario 7: No Split order set up

## Description

* **Split order** configuration is not chosen when creating multiple orders scheduled to deliver to one single customer. In this case, if the vehicles's total capacity can not satisfy all the orders, then all the orders will be rejected

## Solution

* Make sure the **Split order** configuration is chosen when creating multiple orders scheduled to deliver to one single customer.

## Scenario 8: No assigned vehicles

> 📘 This scenario applies to organizations which manually assign orders to vehicles

## Description

* The dispatchers forgot to assign vehicle to deliver the order

## Solution

* The dispatchers need to assign vehicle to deliver the order before optimizing routes

## Scenario 9: Improper warehouse loading time format

## Description

* The warehouse has improper minimum and maximum loading time format, not in minute (mm) format 

## Solution

* Set the warehouse loading time in correct format
* For example, a warehouse has minimum loading time of fifteen minutes and the maximum loading time of forty five minutes, then input in the Min time field should be 15; and input the Max time field should be 45

## Scenario 10: Assign multiple orders to a single vehicle without locking routes

> 📘 This scenario applies to organizations which manually assign orders to vehicles

## Description

* The dispatchers assign multiple orders, which will need to be delivered to multiple customers, to a single vehicle at once. Routes for all orders are locked all at once after the optimization process.
* In this case, Abivin vRoute will perform the optimization for the first order only. The rest of the orders will not be optimized.

## Solution

* In Abivin vRoute logic, in this scenario, the dispatcher must lock route for the preceding order before proceeding to optimize route for the next order. Specifically, the dispatcher need to perform these steps:
  * Step 1. In **Sales orders** tab, choose the first order. Assign that order to the vehicle
  * Step 2. Navigate to **Transportation** tab to optimize route for this order
  * Step 3. Lock route for that order
  * Step 4. Go back to **Sales orders** tab, assign the second order to the same vehicle above
  * Step 5. Navigate to **Transportation** tab to optimize route for the second order. The dispatcher needs to manually choose Cut-off time for this second order at a time point later than the optimized finished time of the first order. If the dispatchers doesn't manually choose the Cut-off time, Abivin vRoute will automatically set the Cut-off time to 30 minutes later from the optimized finished time of the first order
  * Step 6. Lock route for this second order
* Repeat this process for the remaining orders  

> ❗️ In the scenario which there are both accurate and inaccurate configured orders, the dispatchers  need to reconfigure the inaccurate orders before locking routes. If the dispatchers still lock routes without reconfiguring the inaccurate orders, after routes are locked, they will not be able to reconfigure those orders
