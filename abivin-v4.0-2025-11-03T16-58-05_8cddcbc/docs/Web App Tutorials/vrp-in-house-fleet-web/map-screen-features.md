---
title: Map screen features
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
