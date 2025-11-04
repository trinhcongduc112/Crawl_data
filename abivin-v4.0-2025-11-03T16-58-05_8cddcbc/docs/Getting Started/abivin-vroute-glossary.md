---
title: Abivin vRoute Glossary
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
## VRP Model

### Vehicle Routing Problem (VRP) Definition

* Vehicle Routing Problem (Abbreviated as VRP) is the classic vehicle routing plan model, in which the delivery Vehicles will pick up Products from a **Distribution Center (DC)** then deliver to the Customers. After the Vehicles have completed the deliveries, they will travel back to the Distribution Center

![1306](https://files.readme.io/74ae14d-1_DArXB0ZvAu2zjh8P7lxIFA.png "1_DArXB0ZvAu2zjh8P7lxIFA.png")

### Distribution Center

* Distribution Center is the warehouse in which the Products are stored before being distributed to other places. In the VRP/DC Model, the distribution centers are categorized into three kinds based on their levels and functions: **Depot; Sun; Crossdock**

#### Depot

* Depot is the first-level distribution center. From the Depot, the Products can be directly distributed to the Customers or to the second-level distribution centers (Sun and/or Crossdock)

#### Sun

* Sun is a type of second-level distribution center below the Depot. The Sun is primarily used to distribute the Products to smaller-scale Customers. Products will be transported from the Depot to the Sun, and then being distributed from the Sun to their Customers

#### Crossdock

* Crossdock is another type of second-level distribution center below the Depot. Unlike the Sun, the Crossdock will only act as a temporary storage warehouse. The Products will be transported from the Depot to the Crossdock, stored in the Crossdock for a short time, and then will be distributed to the Customers

### Delivery Journey Units

* In Abivin vRoute system, there are some delivery journey unit terms that you need to know: **Delivery Trip; Delivery Shift; Delivery Route; Route Plan**

#### Delivery Trip

* The Delivery Trip is the smallest delivery journey unit. A Delivery Trip is a route in which a Vehicle starts at a Distribution Center, delivers Products to the Customers, then travels back to the Distribution Center

#### Delivery Shift

* The Delivery Shift is the delivery journey unit that is generated once the Route Dispatcher/Route Planner performs the route locking function for a Vehicle. A Delivery Shift can either consist of just one Delivery Trip or several Delivery Trips

#### Delivery Route

* The Delivery Route is simply the total route of a Vehicle in a specific route plan date. A Delivery Route can either consist of just one Delivery Shift or several Delivery Shifts
* A Delivery Route can either be a **Closed Route** or an **Open Route**

##### Closed Route

* Closed Route is the Delivery Route in which the Vehicle will travel back to the Distribution Center once it completes the delivery for the last Customer. The first and the last Stops on the Vehicle's Delivery Route are the same (The Distribution Center), hence the Delivery Route is regarded as ***closed*** 

##### Open Route

* Open Route is the Delivery Route in which the Vehicle will stop at the location of the last Customer once it completes the delivery there. The first Delivery Stop and the last Delivery Stop on the Vehicle's Delivery Route are not the same, hence the Delivery Route is regarded as ***open***

#### Route Plan

* The Route Plan is the whole routing plan of a Branch on the route plan date. The Route Plan consists of all the total Delivery Routes of all the Vehicles of all the Distribution Centers (Depots/Suns/Crossdocks) under a specific Branch
* The image below describes these delivery journey units

<Image title="TRIP SHIFT ROUTE.png" alt={1914} border={true} src="https://files.readme.io/11aaa01-TRIP_SHIFT_ROUTE.png">
  A whole delivery route of a vehicle, consisting of two shifts and five trips
</Image>

* **Delivery vehicles**: The vehicle that will deliver products from the distribution centers to customers
* **Order**: 
* **Sales Order**: Orders in which the organization of the user sells products to their customers
* **Pickup Order**: For some products, after delivering the products to the customers, the manufacturer will receive the empty *product cases* back from their customers. This kind of order is defined as the **Pickup Order**. These orders are deemed to have absolutely no effect on the delivery vehicle's weight/volume capacity
* **Purchase Order**: Orders in which the organization of the user buys products from their suppliers to replenish the warehouse inventory
* **Travel time**: The time period to travel from one location to the next location on the delivery route
* **Loading time**: The time period to load products to the delivery vehicles from the warehouse shelves
* **Unloading time**: The time period to unload products from the delivery vehicles to the warehouse shelves
* **Service time**: The time period to unload products specified for each order, if there are multiple orders to one customer

<Image title="2019-10-08 11_58_09-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/bd0860b-2019-10-08_11_58_09-Window.png" />

* Tasks at the distribution center:
* **Pick**: The act of picking products from the distribution center shelves to prepare for the sales order
* **Pack**: The act of allocating the products picked into separate boxes or pallets before loading onto the delivery vehicles
* Tasks of an order:
* **Sales order**: The vehicle loads products at the distribution center, travels to the customers and unloads products at each customer warehouse. After completely unloading all products in the order, the vehicle returns to the distribution center and end its trip

- **Purchase order**: The vehicle loads products at the supplier warehouse, travels to the user organization warehouse and unloads products there. After completely unloading all products in the order, the vehicle returns to the supplier warehouse and end its trip

* **Pickup order**: The vehicle starts at the distribution center, travel to the customers and loads products at each customer warehouse. After loading all products in the order, the vehicle returns to the distribution center, unloads the products and ends its trip

## PDP Model

* **Pickup and Delivery Problem (Abbreviated as PDP)**: A specific model developed from the base of Vehicle Routing Problem model. In this model, the vehicles start from the Depot, but instead of loading products at the Depot, they will travel to one or two locations - known as the **Origin customer**, and load products there. After that they will deliver products to one location - known as the **Destination customer**
* There are two kinds of PDP order:
* **Less than Truckload order (Abbreviated as LTL order)**: The vehicle will pick up products at multiple Origin customers and deliver to one Destination customer

<Image title="pdp.png" alt={967} className="border" border={true} src="https://files.readme.io/ede6d3f-pdp.png" />

* **Full Truckload order (Abbreviated as FTL order)**: The vehicle will pick up products at one Origin customer and deliver to one Destination customer

<Image title="pdp ftl .png" alt={967} className="border" border={true} src="https://files.readme.io/7390d1b-pdp_ftl_.png" />

* The delivery route of a vehicle can be made up of multiple shifts. Two adjacent shifts are separated by a time period called **Cut-off time**

<Image title="2019-10-08 15_42_45-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/102a203-2019-10-08_15_42_45-Window.png" />

* Tasks at a location:
* **Pick**: The act of loading products onto the vehicle at the Origin customer warehouse
* **Drop**: The act of unloading products from the vehicle at the Destination customer warehouse
* **Line-haul**: The movement of products from the pick-up locations to drop-off locations in a complete PDP route. There are three kinds of line-haul based on the route length:
* **Short-haul**: Line-hauls that have the route length lower than 250 kilometers
* **Medium-haul**: Line-hauls that have the route length ranging from 250 to 450 kilometers
* **Long-haul**:  Line-hauls that have the route length larger than 450 kilometers
* **Deadheads**: The movement in which the delivery vehicles carry no products. This kind of movement happen when the vehicles travel from the last drop-off location back to the warehouse to end their delivery routes
* **Palletized products**: Products that are placed on pallets before being loaded onto delivery vehicles
* **Non-Palletized products**: Products that are placed into normal delivery boxes and loaded onto delivery vehicles without pallets
* **Pickup time**: The time period to load products at the Origin customer warehouse
* **Delivery time**: The time period to unload products at the Destination customer warehouse
* **Travel time**: The time period to travel from the a location to the next location on the delivery route

<Image title="2019-10-08 15_19_28-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/2cf012b-2019-10-08_15_19_28-Window.png" />

* **Rest time**: The time period (Default is 8 hours) the driver takes to rest after each 24 straight hours of working (Including travelling and loading/unloading)

<Image title="2019-10-08 15_14_02-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/d447f7b-2019-10-08_15_14_02-Window.png" />

* **Waiting time**: The time period between the moment the vehicle reaches a location (Both Origin customer and Destination customer) and the moment that location officially opens

<Image title="2019-10-08 15_15_49-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/a15ce3b-2019-10-08_15_15_49-Window.png" />

## Freight Transport Model

* Freight transport is the transportation model in which products are being transported in bulk (container) between ports (Dry ports and Sea ports)
* This model is divided into two sub models:
* **Freight transport - Road model**: This model uses semi-trailer trucks to carry containers between dry ports. The containers will later on be distributed in the mainland

<Image title="inline_image_preview.jpg" alt={590} className="border" border={true} src="https://files.readme.io/93242c7-inline_image_preview.jpg" />

* **Freight transport - Barge model**: This model uses barges to carry containers between inland water ports. The containers will later on be gathered and loaded on to a vessel to travel to other countries

<Image title="teubooker.jpg" alt={1000} className="border" border={true} src="https://files.readme.io/c2efa97-teubooker.jpg" />

* **Shipment**: The act of moving freight between multiple locations
* **Shipment stops**: The locations on the shipment route. At each shipment stop the vehicle will need to perform a group of tasks
* **Pick stop**: A type of shipment stop where containers are picked up onto the vehicles
* **Drop stop**: A type of shipment stop where containers are dropped off from the vehicles 
* There are two types of shipment:
* **Dummy shipment**: The pre-planned shipment. Shipments of this type hold accurate information about the Pick stops
* **Actual shipment**: The shipment that follows up a completed Dummy shipment. Shipments of this type hold accurate information about the Drop stops
* **Shipment Leg**: The fundamental delivery journey of a shipment, in which the vehicle travels from one Stop to the next Stop
* **Non-freight related route (Abbreviated as NFR)**: Similar to ***Deadhead*** in PDP model, in which the vehicle travels without carrying any container
* **Actual Time of Arrival (Abbreviated as ATA)**: The time at which a semi-trailer truck or barge actually arrives at a certain stop on the route of its assigned shipment 
* **Actual Time of Departure (Abbreviated as ATD)**: The time at which a semi-trailer truck or barge actually departs from a certain stop on the route of its assigned shipment
* **Actual Time of Berthing (Abbreviated as ATB)**: The time at which a vessel actually berths at a port/terminal
* **Estimated Time of Arrival (Abbreviated as ETA)**: The time at which a semi-trailer truck or barge is expected to arrive at a certain stop on the route of its assigned shipment 
* **Estimated Time of Departure (Abbreviated as ETD)**: The time at which a semi-trailer truck or barge is expected to depart from a certain stop on the route of its assigned shipment
* **Estimated Time of Berthing (Abbreviated as ETB)**: The time at which a vessel is expected to berth at a port/terminal
