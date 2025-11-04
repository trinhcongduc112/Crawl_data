---
title: Hard Time Window
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
## Hard Time Window Constraint Definition

* During the delivery process, more often than not your Customers will demand their Orders to be delivered within a specific time window
* For example, your Customer is a supermarket chain that operates 24/7. However, they will only accept the deliveries within 04 hours daily, from 03:00 A.M. to 07:00 A.M.
* In Abivin vRoute system, this constraint is defined as the **Hard Time Window**. In this article, we will show you how to solve this constraint

## Hard Time Window Types

* First, we will walk you through the types of Hard Time Window in Abivin vRoute system. Currently, there are five types:
* 1 - Customer Group Hard Time Window. This Hard Time Window is used for the Customer Groups. The Customers within the applied Customer Group will be affected by this Hard Time Window
* 2 - Customer Open-Close Time Window
* 3 - Customer Custom Time Window. Apart from the Open-Close Time Window, each Customer can have another Hard Time Window
* 4 - Ship-to Hard Time Window. This Hard Time Window is applied to the Ship-to locations of a Customer
* 5 - Order Hard Time Window. This Hard Time Window is applied to the Sales Orders of a particular Customer

### Hard Time Window Constraint Priority Levels

* For User accounts who don't use the Customer Ship-to Profile feature, the Hard Time Window priority level is as follows:
* Order Hard Time Window (If available) > Customer Custom Hard Time Window (If available) > Customer Open-Close Time Window > Customer Group Hard Time Window (If available)
* If more than one of these hard time window types exist for a Customer's Order, they must have a mutual intersection time period, otherwise, the Order will not be optimizable during the Route Plan optimization process and will be deemed Unplanned Order
* For User accounts who use the Customer Ship-to Profile feature, the Hard Time Window priority level is as follows:
* Order Hard Time Window (If available) > Ship-to Hard Time Window (If available) > Customer Group Hard Time Window (If available)

## Enable Hard Time Windows Configuration

* You need to enable the **Hard Time Windows** configuration at the **Branch**. This configuration is located in the **More Configurations > Algorithm** sub-tab

<Image title="sDBX6ODNNd.png" alt={1485} className="border" border={true} src="https://files.readme.io/af816af-sDBX6ODNNd.png" />

* Next, you have to set up the Hard Time Windows

## Setup Hard Time Windows

### Setup Hard Time Windows for Customer Groups

#### Setup Hard Time Windows for Customer Groups on Webform

* You can input the hard time window of a Customer Group in the **Group Time Window** field. The Customer Group hard time window must be in the following format: ***HH:mm-HH:mm*** (24-hour format)
* If the Customer Group has multiple hard time windows, separate two adjacent hard time windows only by a semicolon, for example, ***04:00-12:00;14:00-23:00***

<Image title="lZuEWK2e0E.png" alt={956} className="border" border={true} src="https://files.readme.io/d7eb56d-lZuEWK2e0E.png" />

#### Setup Hard Time Windows for Customer Groups in Excel Import File

* You can input the hard time window of a Customer Group in the **Group Time Windows** cell. The Customer Group hard time window must be in the following format: ***HH:mm-HH:mm*** (24-hour format)
* If the Customer Group has multiple hard time windows, separate two adjacent hard time windows only by a semicolon, for example, ***04:00-12:00;14:00-23:00***
* If the information of a Customer Group spans across multiple rows, make sure to copy and paste the hard time windows of that Customer Group across all its rows

<Image title="55nswvcP3c.png" alt={393} className="border" border={true} src="https://files.readme.io/590dab5-55nswvcP3c.png" />

### Setup Hard Time Windows for Customers

#### Setup Hard Time Windows for Customers on Webform

* You can input the hard time window of a Customer in the **Time Window** field (Located in the **Main Setting** tab) in the following format: ***HH:mm-HH:mm*** (24-hour format)
* If the Customer has multiple hard time windows, separate two adjacent hard time windows only by a semicolon, for example, ***04:00-12:00;14:00-23:00***

<Image title="9aBlYoVMmt.png" alt={941} className="border" border={true} src="https://files.readme.io/47cafce-9aBlYoVMmt.png" />

#### Setup Hard Time Windows for Customers in Excel Import File

* In the Customer Excel import file, you can input the Hard Time Window of a Customer into their respective **Time Window** cell, also in the format ***HH:mm-HH:mm*** (24-hour format)
* If the Customer has multiple hard time windows, separate two adjacent hard time windows only by a semicolon, for example, ***04:00-12:00;14:00-23:00***

<Image title="lWjyof4TC7.png" alt={227} className="border" border={true} src="https://files.readme.io/99ab539-lWjyof4TC7.png" />

## Setup Hard Time Window for Sales Orders

### Setup Hard Time Window for Sales Orders on Webform

* On Webform, the hard time window of a Sales Order is input in the **Order Time Window** field, following the **HH:mm-HH:mm** format (24 hour format)
* If the Sales Order has multiple hard time windows, separate two adjacent hard time windows only by a semicolon. For example: ***06:00-07:00;09:00-10:00***

<Image title="rwK6an7Ijl.png" alt={624} className="border" border={true} src="https://files.readme.io/b4e7535-rwK6an7Ijl.png" />

### Setup Hard Time Window for Sales Orders in Excel Import File

* In the Excel import file, input the hard time window of the Sales Order into the **Time Window** cell
* If the Sales Order has multiple hard time windows, separate two adjacents hard time windows only by a semicolon. For example: ***06:00-07:00;09:00-10:00***
* If the information of a Sales Order spans across multiple rows, make sure to copy the hard time window values of that Order across all of its rows

<Image title="ddO4EibCUj.png" alt={278} className="border" border={true} src="https://files.readme.io/2e1a9dd-ddO4EibCUj.png" />

## Route Plan Optimization With Hard Time Windows

* After setting the hard time windows, you can proceed to the Route Plan Optimization process
* The system will take into account the hard time windows and calculate the optimized Delivery Routes that satisfy those hard time windows
* If a Customer places multiple Sales Orders, and each of the Sales Orders has a different hard time window, then you have to make sure that the hard time windows of these Orders have a mutual intersection period, otherwise the system will not be able to generate the optimized Delivery Route for them
* For example, a Customer places three Orders, ***01; 02: 03***
* The hard time window of Order 01 is ***03:00-07:00***
* The hard time window of Order 02 is ***05:00-08:00***
* The hard time window of Order 03 is ***06:00-09:00***
* As you can see, the hard time windows of these three Orders share an intersection period, ***06:00-07:00***. During the Route Plan optimization process, the system will try to generate the Delivery Route for these Orders within that intersection period
