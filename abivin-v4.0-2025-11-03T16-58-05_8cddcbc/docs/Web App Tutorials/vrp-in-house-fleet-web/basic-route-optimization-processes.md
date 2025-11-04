---
title: Basic route optimization processes
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
* Assuming that you have done the following actions for the Depots/xDocs under your Branch management:
* Created orders (Please refer to the [**Manage Orders**](https://docs.abivin.com/docs/manage-distribution-center-order#section-create-orders) article for instruction)
* Configured vehicles and drivers (Please refer to the [**Manage Vehicles**](https://docs.abivin.com/docs/vehicle-management#section-create-vehicles) and [**Manage Drivers (Delivery men)**](https://docs.abivin.com/docs/manage-drivers-delivery-men) articles for instructions)
* You can now perform delivery route optimization for all orders starting from all Depots/xDocks under your Branch's management

## Route optimization screen description

* The route optimization screen is divide into two parts: The **Map** and the **Timeline panel**
* The Map will show the optimized routes of all vehicles
* The Timeline panel will show. Here you will be able to perform the route optimization process, as well as several other useful functions that will be described later on in this article and other dedicated articles
* You can change the width of the Timeline panel by clicking on the **Artboard** icons on the right side of the toolbar. The number of rows on each artboard icon corresponds to the number of vehicle rows shown on the Timeline panel
* You can also click on **All** to show the maximum 5 rows, or click on :fa-arrow-down: icon to completely hide the Timeline panel. To show it back, click on :fa-arrow-up: **Timeline panel** button

> 📘 Sometimes the :fa-arrow-up: **Timeline panel** button is hidden behind the information panel on the right side of the screen. You can show it by clicking on :fa-remove: icon of the information panel

## Basic route optimization process

* The basic route optimization process is divided into three phases:

## Phase 1: Choose the Branch and Execution date

* Navigate to **Transportation > Vehicle List** tab
* Click on **View Map** icon
* The **Optimization** screen will display
* Select the *Branch* for which you want to perform route optimization from the **Branch** field

> 📘 In case the network is slow and the **Branch** field doesn't display automatically, you can type the organization code of the branch into the field, then click :fa-times: icon. The system will sort out the branch with that code

* Next, click on **Date** field and select the *Execution Date* (Not the *Creation Date*) of the orders from the drop down calendar. You can also type the date directly into this field in the format mm/dd/yyyy (For example 07/22/2019)
* Click on **Select**

## Phase 2: Generate the optimized routes

* After configuring the *Branch* and the *Execution Date*, the system will pre-generate the orders delivered from all Depots/xDocks under the selected Branch's management, that will be executed on the selected date on a panel called **Timeline panel**
* To generate the optimized routes for all orders, you need to click on **Optimize** button at the bottom right of the Timeline panel, then click **Optimize** one more time on the pop up **Optimize Route** form
* The optimization process will start. This process will take in account the input data of various configurations and constraints that you have set earlier, and generate the most optimized delivery routes for the orders
* After a few moments, the optimized routes for all orders originated from the selected Branch will display on the Timeline panel
* During this phase, you can made some changes to the routes, such as Rearrange the orders sequence, Assign and re-assign driver, Update customer information or Remove customer from the route. All the basic functions will be described later

## Phase 3: Lock routes and send the delivery tasks to the drivers on Mobile app

* After you have made necessary changes, or if you see that the routes are appropriately optimized, you can send the delivery tasks to the assigned drivers on their Mobile app by clicking on **Lock Route** button at the bottom right of the Timeline panel, next to the **Optimize** button
* A form will pop out, asking you to confirm. Click **OK** to confirm locking the routes, or **Cancel** if you still want to make some change

## Driver assignment during route optimization

* There are two options to assign drivers to vehicles: *Before performing route optimization* (As described in the [**Manage Vehicles**](https://docs.abivin.com/docs/vehicle-management#section-assign-default-drivers-to-vehicles) article) and *During performing route optimization*
* Below we will talk about how you can assign, or re-assign driver during route optimization:
* At the center of the route there is a :fa-user: icon. This icon shows code of the driver who will operate that delivery route. This icon will have two forms, showing if the route has had an assigned driver or not:

- For a route that has not been locked, click on **Driver** :fa-user: icon on the Timeline panel
- The **Assign to Driver** form will appear. Click on the **Driver** field, select a suitable driver from the drop down menu and click **Assign** to confirm the assignment

<Image title="70f3557-p5.png" alt={1361} className="border" border={true} src="https://files.readme.io/1f6fb7f-70f3557-p5.png" />

![1918](https://files.readme.io/7ef80d4-p7.png "p7.png")

> ❗️ If the vehicle route has been locked, you will not be able to assign another driver for that vehicle

## View successfully optimized routes

* After optimization, the Timeline panel will display the optimized routes of all vehicles during their working time in a day
* The trucks will be represented by :fa-truck: icon, while the motorbikes will be represented by :fa-motorcycle: icon
* Click on the :fa-eye: icon of each vehicle will show its optimized route on the map
* You can also click on :fa-eye: icon next to **Vehicles** text on the Timeline bar to display the optimized routes of all vehicles

## Replay actual completed routes

* After the driver has completed a delivery route, you can replay the actual delivery route that he has performed by clicking on the switch button next to **PLAN** text on the Timeline panel
* The **PLAN** text will switch to **ACTUAL**, and on the bottom right of the Timeline panel will appear a set of different buttons, serving for playback functions of the completed delivery routes
* To replay a route, click on the :fa-eye: icon of that route, then click on **Replay** button
* Click **Pause** to pause the playback, or **Stop** to completely stop the playback

<Image title="replay route.gif" alt={1668} className="border" border={true} src="https://files.readme.io/aa7c730-replay_route.gif" />

## Unlock routes

* After the routes are locked, you can still unlock by clicking on **Unlock** button
* A form will pop out, asking you to confirm. Click **OK** to confirm unlocking the routes, or **Cancel** if you don't want to

## Rearrange orders on route

* Provided that you haven't locked the routes of one or more vehicles, you can rearrange their orders sequence by clicking and dragging the order on the vehicle's route, or to another vehicle's route

## Update customer coordinate information

* If one or more customers recently change their location without you knowing prior to performing route optimization, you can still update their new coordinate information:
* Clicking on their position on the route, the information panel will appear on the right side of the screen
* Click on **Update Customer Location** text on the panel, then input new coordinate information in the form that appears
* Click **OK** to confirm changing coordinate information

## Remove order from route

* You can remove the order to a customer from a route by clicking on the numerical order of that order on the Timeline panel, then click on **Remove Customer From Route** text and click **OK** on the pop out confirmation form

- On the Depot icon will show the vehicle fill rates of all orders over the vehicle capacity: On the left is weight; on the right is volume

* The number icons on the vehicle timeline bar represent the numerical order of the customers on the vehicle delivery route. Compare the position of each icon to the timeline bar on **Second section** will show the relative moment the vehicle reaches the customer place and delivers order

## View route information

* If you click on the Depot icon at the start of the route, on the right side of the screen will display an information panel of the route. Below is the information in that panel:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organization Code
      </td>

      <td>
        Code of the Depot
      </td>
    </tr>

    <tr>
      <td>
        Organization Name
      </td>

      <td>
        Name of the Depot
      </td>
    </tr>

    <tr>
      <td>
        Address
      </td>

      <td>
        Address of the Depot
      </td>
    </tr>

    <tr>
      <td>
        Reaching Time
      </td>

      <td>
        The time period in which the vehicle spends at the Depot
      </td>
    </tr>

    <tr>
      <td>
        Total Product Weight
      </td>

      <td>
        Total weight of all products in the route
      </td>
    </tr>

    <tr>
      <td>
        Total Product Volume
      </td>

      <td>
        Total volume of all products in the route
      </td>
    </tr>
  </tbody>
</Table>

## View and export Packing List and Order List

* At the end of the panel, you can also view the **Packing List** and **Order List** of the route by clicking on the corresponding text
* On the **Packing List** and **Order List** forms, you can also **Export** them to Excel templates to view offline

![624](https://files.readme.io/b7f0a4d-2019-08-26_14_47_13-Window.png "2019-08-26 14_47_13-Window.png")

![864](https://files.readme.io/7940475-2019-08-26_14_47_28-Window.png "2019-08-26 14_47_28-Window.png")

* On the route map, there will also be a bubble on top of the Depot location, showing the details of products loaded at that Depot, in Temperature
* It will show the percentage of 

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Property
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ORDERS
      </td>

      <td>
        The quantity of orders successfully optimized
      </td>
    </tr>

    <tr>
      <td>
        DISTANCE
      </td>

      <td>
        The aggregated distance of the generated delivery route
      </td>
    </tr>

    <tr>
      <td>
        COSTS
      </td>

      <td>
        The aggregated costs of the generated delivery route
      </td>
    </tr>

    <tr>
      <td>
        REVENUES
      </td>

      <td>
        The aggregated revenues of the generated delivery route
      </td>
    </tr>

    <tr>
      <td>
        PRODUCTIVITY
      </td>

      <td>
        The aggregated expected profit of the generated delivery route, equal to the result of the revenues minus the costs

        For example, the revenues is 5000000 VND, the costs is 4000000 VND, then the productivity will show 1000000
      </td>
    </tr>

    <tr>
      <td>
        REVENUES/DISTANCE
      </td>

      <td>
        The medium revenue of all orders over the delivery distance
      </td>
    </tr>

    <tr>
      <td>
        WEIGHT/CAPACITY
      </td>

      <td>
        The aggregated weight of all orders over the aggregated weight capacity of all utilized vehicles
      </td>
    </tr>

    <tr>
      <td>
        VOLUME/CAPACITY
      </td>

      <td>
        The aggregated volume of all orders over the aggregated volume capacity of all utilized vehicles
      </td>
    </tr>

    <tr>
      <td>
        TRUCK/BIKE/TOTAL
      </td>

      <td>
        The number of trucks, bikes, and the sum of those two vehicle types utilized for the optimized delivery route
      </td>
    </tr>

    <tr>
      <td>
        FAMILIARITY
      </td>

      <td>
        The percentage of Familiarity that the orders met, calculated by the the division of the over the total orders
      </td>
    </tr>
  </tbody>
</Table>

## Remove customer from route

* If for some reasons, during the optimization process, you know that an order to a customer will not be able to be performed, you can receive that order from the route by clicking on **Remove Customer From Route** text on the panel, then click **OK** on the confirmation form

## View missing orders

## View single missing order information

* The missing orders are displayed on the Timeline panel, just below the Timeline bar and above the optimized routes
* You can view the details of a specific missing order by clicking on its order code, a thumbnail will pop out showing the information of that order
* To copy the information of that order, click on **Copy to clipboard** :fa-file: icon on the thumbnail

- Below are the information fields of a missing order

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Customer ID
      </td>

      <td>
        Same as Customer Code
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Customer Name
      </td>

      <td>
        Name of the customer
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Order Code
      </td>

      <td>
        Code of the order
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Allow Vehicle Type
      </td>

      <td>
        Specify if the customer specifically requires a vehicle type to deliver order (Bike only or Truck only)
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        MDP Code
      </td>

      <td>
        The MDP code of the customer (If available)
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Route Index
      </td>

      <td>
        The index number for the rought
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Weight
      </td>

      <td>
        Weight of the order delivered to that customer
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Volume
      </td>

      <td>
        Volume of the order delivered to that customer
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Price
      </td>

      <td>
        The money value of the order delivered to that customer
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Position
      </td>

      <td>
        Coordinate information of the customer
      </td>
    </tr>
  </tbody>
</Table>

## View entire list of missing orders

* You can view the entire list of missing orders by either clicking on **Show more** button at the end of the Missing orders row on the Timeline panel, or clicking on **Missing orders** button on the top right of the map
