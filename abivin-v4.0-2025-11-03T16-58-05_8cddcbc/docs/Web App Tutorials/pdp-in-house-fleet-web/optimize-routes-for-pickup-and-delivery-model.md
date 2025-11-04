---
title: PDP model
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
## Enable Long-haul model

Step 1: Go to the Organization tab, select the organization with branch type to edit

![1348](https://files.readme.io/95e3c16-X1.png "X1.png")

Step 2: Checkbox into the Long Haul cell, then click Save button

![1350](https://files.readme.io/d3ac99f-X2.png "X2.png")

## Config the Group List to display the Longhaul Orders menu

Step 1: Go to the Group List, select a group to edit

![1346](https://files.readme.io/4141918-X3.png "X3.png")

Step 2: Checkbox into the Longhaul orders in the permission table, then click the Save button

![1348](https://files.readme.io/14991fc-X4.png "X4.png")

After step 2, the Longhaul Orders will display at the sidebar section

![1359](https://files.readme.io/c84a57b-X5.png "X5.png")

## Create a customer in the same city

Step 1: Go to the Partners menu, click on the Province List, select the organization to get the Province/City code\
**Note:** In the case you want to add more city, please contact the support group

![1349](https://files.readme.io/8493b0a-X6.png "X6.png")

Step 2: For the import customer, enter the province/city code in the City column (that in step 1).

![1343](https://files.readme.io/246f123-X7.png "X7.png")

## Create a Vehicle Type

Step 1: Go to the Transporation menu, click on the Vehicle Type tab, then hover on the "+" button to create a vehicle type

![1358](https://files.readme.io/537f075-X8.png "X8.png")

Step 2: Enter the information of the vehicle type

* Organization: Select the Organization only the Branch type
* Type Code: Vehicle type code defined by an admin user, example: Truck2T
* Palletized Time (minutes)/Non-palletized Time(minutes): Loading time is determined by vehicle type and whether the order is in pallet or not.
* Type Name: Vehicle type name\
  Step 3: Click the Save button

![1355](https://files.readme.io/50a45b1-X9.png "X9.png")

## Create a Vehicle

Step 1: Go to the Transportation menu, click on the Vehicle List tab, then hover on the "+" button to create a vehicle

![1348](https://files.readme.io/4f2cede-X10.png "X10.png")

Step 2: Enter the vehicle information:\
**Note:**

* Vehicle Type: Select the vehicle type list that was created on the Vehicle Type tab 

![1350](https://files.readme.io/9c5517a-X11.png "X11.png")

* For the rented (subcontractor) vehicle, scroll down then checkbox into the Sub-contractor cell, enter the Sub-contractor name, rental cost
* Customer can reserve a specific vehicle for a date range
* Reserved vehicle will not be used in routing, regardless of reserved date 

![1349](https://files.readme.io/1c73570-X12.png "X12.png")

Step 3: Click the Create button to save information of the vehicle

![1349](https://files.readme.io/ea14984-X13.png "X13.png")

## Create a long-haul order

Step 1: Go the the Longhaul Orders menu, hover on the "+" icon to create a order

![1347](https://files.readme.io/996fe48-X14.png "X14.png")

Step 2: Enter information of the order:

* 2.1. Select the type of the order: It has 2 order type: FTL(full-truckload) and LTL (less-than-truckload)
* For the FTL type order have an origin and a single destination\*
* For the LTL type order have multiple origins (in the same city) and a single destination\*
  * 2.2. Select the warehouse, the delivery date of that order ( select a range date)
  * 2.3. Select the Destination (delivery location)  with respective time window

![1348](https://files.readme.io/7c217e9-X15.png "X15.png")

* 2.4. Select the Origin (pickup location) with respective time window. For the LTL type, click on the "+" to add more Origin location

![1350](https://files.readme.io/4ec02e8-X16.png "X16.png")

* 2.5. Select the Vehicle Type that the vehicle can delivery the order
* 2.6. Select the Sub-contractor: has 3 options:\
  *No - That order will not be assigned to any rental vehicle if the order is failed*\
  *Always - That order always be assigned to the rental vehicle*\
  *Use if needed - If the order is failed couldn't in the route, it will be assigned for the vehile*

![1352](https://files.readme.io/198c569-X17.png "X17.png")

* 2.7. Select the product of the warehouse, then click the ADD button\
  \*- If untick on the Palletized cell, you must enter the number of case/item for each product

- In tick on the Palletized cell, you must enter the pallet for each product\* 

![1350](https://files.readme.io/7fa74e0-X18.png "X18.png")

* 2.8. Enter the total weights, total volumes, total price of the order 

![1352](https://files.readme.io/0ab2b4c-X19.png "X19.png")

Step 3: Click the Save button

![1349](https://files.readme.io/548a88e-X20.png "X20.png")

**Some notes for the long-haul orders:**

* The order code isn't duplicate for all days
* Vehicle type must be defined in the order ( an order that request 20T truck can't be assigned to a 30T truck)
* Subcontractor name must be defined in the vehicle list
* For the order is over the current date, it's displayed on the Past Order tab. For that order, you can only edit the past order, don't allow create a past order.

## Optimize the long-haul route

Step 1: After create the long-haul order, go to the Transporation tab, click on the maps icon, select the branch to start optimize the route

![1364](https://files.readme.io/2c42e5e-X21.png "X21.png")

Step 2: Click the Optimize Route button

![1358](https://files.readme.io/445636b-X22.png "X22.png")

After optimizing, the route will be display as the picture below:

![1917](https://files.readme.io/7711142-a1.png "a1.png")

* Like Order, routing is no longer divided by date. Instead, there will the universal timeline kept running all the time.
* 2.1. For vehicle currently at WH, the earliest starting time will be 5 hours from the optimization time
* 2.2. The gray highlight bar: Vehicles will drive for 24 hours then rest for 8 hours before continue driving.

![1919](https://files.readme.io/55f423e-X24.png "X24.png")

* 2.3. The red marker is Origin location
* 2.4. The green marker is Destination location

![1360](https://files.readme.io/c53c5ae-X25.png "X25.png")

* 2.5.  Loading time is determined by vehicle type and whether the order is in pallet or not ( by minutes)
* Planned orders will be locked 3 hours before it's departure. Before that time, it can still be re-assigned to other vehicle. Tasks for drivers will be generated at locking time.

## Assign driver for vehicle

Each vehicle will be assigned to 2 drivers: 1 main-drivers and 1 sub-drivers. Only assign drivers for main vehicle (not sub-contractor)\
Step 1: Go to the route, click on the driver icon in the route

![1366](https://files.readme.io/ddc1186-X26.png "X26.png")

Step 2: Select the Sub-Driver: Can select one or multiple sub-driver, then click the Assign button

![1362](https://files.readme.io/aad01b1-X27.png "X27.png")

After assigned for the sub-driver, tasks for driver will be generated for both the main driver and sub-driver.

## Lock routes

Step 1:

* If you lock the route for the first time by click on the In these ste  button the markers will highlight green as below picture. In these step, the route only lock to last destination of the trip ( didn't locked "Stop of the trip" marker) 

![1365](https://files.readme.io/7c4b0a5-X30.png "X30.png")

* For the routes that has many orders: If you lock route for the first time, the route only lock to last destination of the first orders.

![1916](https://files.readme.io/61c59c4-X32.png "X32.png")

* To lock for all trip, you must click on the Lock route button again.

![1919](https://files.readme.io/2223f42-X33.png "X33.png")

Step 2: To create an End of trip task you have to lock for the second time. After that, marker "Stop of the trip" will highlight as below picture

![1365](https://files.readme.io/d84b15d-X31.png "X31.png")

Step 3: After locked routes, go to the task list to check tasks for the drivers

![1350](https://files.readme.io/cf33ada-X28.png "X28.png")
