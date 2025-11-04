---
title: '[Inner City] VRP/DC Model'
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
* VRP/DC Model is the routing model in which your organization owns a number of warehouses (also known as Distribution center - DC). Each warehouse, which has its own customer base and vehicle fleet, is a delivery route's starting point and also where it is completed. In addition, a number of constraints like multimodal deliveries, weight volume capacities, time windows... can be considered by flexible algorithms to create the most optimal transportation plan.
* Upon receiving the Sales Orders placed by the Customers, the dispatcher will build a Route Plan for their vehicle fleet. Typically, a Route Plan will cover the following points: 
* 1 -  List of the vehicles that will be utilized
* 2 - How the Customers' orders should be allocated on the Delivery Route of each vehicle
* 3 - Timeline for each vehicle to perform the delivery tasks
* In order to optimize a route plan using VRP/DC Model, dispatchers must bear in mind the tutorials on how to manage each of Abivin vRoute System Resources (Organizations, Users & User Groups, Partners, Products & Product Categories, Orders, Vehicles, Tasks & Actions), which are demonstrated thoroughly in the next articles.
* After the route plan has been generated, the deliverers can start loading products from the warehouse shelves and start their delivery tasks. After the deliverers have completed the delivery, they will travel back to their warehouses, hand over collected cash, and end their working day.

> 👍 Compatible with PDP model
>
> * You can run this model simultaneously with the [PDP model](https://docs.abivin.com/docs/pdp-in-house-fleet-web) on the same account, provided that you have separate Organizations of Branch type for each model
> * Apart from the PDP model, none of the remaining models can run simultaneously with this model on the same account
