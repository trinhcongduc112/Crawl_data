---
title: Route Map Screen Functions
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
* On the Map screen, aside from the Plan Timeline, you can also access the Execution Timeline once you have optimized and locked the routes
* The Execution Timeline serves as a tracking timeline, where you can view the actual execution of the orders
* To access the Execution Timeline, click on the :fa-toggle-of: button next to **Plan** text on the Timeline panel

<Image title="VMY8CJ9Pkw.png" alt={1920} className="border" border={true} src="https://files.readme.io/24e21bd-VMY8CJ9Pkw.png" />

* The **Execution Timeline panel** will appear

<Image title="UkRYps41q8.png" alt={1920} className="border" border={true} src="https://files.readme.io/d8350e1-UkRYps41q8.png" />

* Below we will list the features of the Execution Timeline

## View delivery results

* You can see the delivery result of each customer by the color of the checkmark icon :fa-check-circle: on the planned timeline horizon

<Image title="7Q1new4CYt.png" alt={441} className="border" border={true} src="https://files.readme.io/23b4897-7Q1new4CYt.png" />

* The color of that icon represents the Delivery status of the order:
* **Green**: The order was **Successfully delivered**
* **Orange**: The order was **Partially delivered**
* **Black**: The order was **Not delivered**

## View execution timestamps

* On the Execution Timeline panel, you can see that below each Plan Timeline of the vehicle, there is an additional timeline. That is the **Execution Timeline**

<Image title="KQeMIeMMtR.png" alt={1920} className="border" border={true} src="https://files.readme.io/2a10e7e-KQeMIeMMtR.png" />

* On the Execution Timeline, the timeline blocks indicate the time period the driver has actually spent at a particular location (Manufacturer depot or Customer store/warehouse). The timeline block is calculated based on the time of the submitted tasks on Mobile app

<Image title="9TEOG9Vp5e.png" alt={1199} className="border" border={true} src="https://files.readme.io/46a07e7-9TEOG9Vp5e.png" />

* You can use the horizontal scrollbar to scroll the timeline horizon from left to right and vice versa

<Image title="B5mEVUqJCM.png" alt={1920} className="border" border={true} src="https://files.readme.io/396858f-B5mEVUqJCM.png" />

* You can change the width of the Timeline panel by clicking on the **Artboard** icons on the top right side of the Timeline panel. The number of rows on each artboard icon corresponds to the number of vehicle rows shown on the Timeline panel
* Clicking on the **All** text will show (limit is 5 rows), while clicking on the :fa-arrow-down: icon will collapse the panel
* If the Timeline panel doesn't show all timelines of the vehicles, you can click on a blank point on the panel, then use the mouse scroll wheel to scroll the panel up and down

<Image title="jHeNQVclvZ.png" alt={1920} className="border" border={true} src="https://files.readme.io/6a81aa2-jHeNQVclvZ.png" />

## Replay actual travel routes

* You can view the actual delivery route of a vehicle in real time, or after that vehicle has completed the delivery route, following the steps below
* Click on on the switch button :fa-toggle-off: next to **PLAN** text on the Timeline panel
* The **PLAN** text will switch to **EXECUTE**
* Click on the :fa-eye: icon of the vehicle which you want to tview the actual delivery route. On the bottom right of the Timeline panel will appear a set of different buttons, serving for playback functions of the actual delivery route
* To view the actual delivery route, click on **Replay** button
* The system will playback the actual travel route of that vehicle on the map screen
* You can click on **Pause** button to temporarily pause the playback; or **Stop** button to completely stop the playback

<Image title="replay route.gif" alt={1668} className="border" border={true} src="https://files.readme.io/aa7c730-replay_route.gif" />

## View customer information

* When you click on the timeline block of a particular customer, on the right side of the map screen will appear a panel showing various information of that customer
* You can view customer information on both Plan and Execution timelines. On Execution timeline, if a customer has been checked in by the vehicle, the panel will also display the check in photo

<Image title="2ldVsnB7JJ.png" alt={1920} border={true} src="https://files.readme.io/6a6a76e-2ldVsnB7JJ.png">
  Check In photo
</Image>

* Below are the information of a customer

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
        MDP
      </td>

      <td>
        Familiarity code of that customer\
        If the vehicle doesn't have familiarity relationship with that customer, this field will be blank
      </td>
    </tr>

    <tr>
      <td>
        Customer Code
      </td>

      <td>
        Management code of that customer
      </td>
    </tr>

    <tr>
      <td>
        Customer Name
      </td>

      <td>
        Name of that customer
      </td>
    </tr>

    <tr>
      <td>
        Driver Name
      </td>

      <td>
        Name of the driver
      </td>
    </tr>

    <tr>
      <td>
        Address
      </td>

      <td>
        Address of that customer
      </td>
    </tr>

    <tr>
      <td>
        Orders
      </td>

      <td>
        List of the orders delivered to that customer
      </td>
    </tr>

    <tr>
      <td>
        Type
      </td>

      <td>
        Product category codes of the products loaded in the orders delivered to that customer
      </td>
    </tr>

    <tr>
      <td>
        Time Window
      </td>

      <td>
        Time window of the order\
        If there is no time window, the value in this field will be: N/A
      </td>
    </tr>

    <tr>
      <td>
        Familiarity
      </td>

      <td>
        Specify whether the vehicle has familiarity relationship with that customer or not\
        If the vehicle has familiarity relationship with that customer, the value in this field will be: Yes\
        If the vehicle doesn't have familiarity relationship with that customer, the value in this field will be: No
      </td>
    </tr>

    <tr>
      <td>
        Temperature
      </td>

      <td>
        Temperature levels of the products in the orders delivered to that customer
      </td>
    </tr>

    <tr>
      <td>
        Reaching Time
      </td>

      <td>
        The planned time period that the vehicle stays at that customer's store/warehouse to deliver the orders
      </td>
    </tr>

    <tr>
      <td>
        Open/close times
      </td>

      <td>
        Open time and Close time of that customer
      </td>
    </tr>

    <tr>
      <td>
        Total Product Weight
      </td>

      <td>
        Total weight of all orders delivered to that customers
      </td>
    </tr>

    <tr>
      <td>
        Total Product Volume
      </td>

      <td>
        Total volume of all orders delivered to that customers
      </td>
    </tr>

    <tr>
      <td>
        Fill Rate Volume
      </td>

      <td>
        The vehicle fill rate by volume of all orders delivered to that customers
      </td>
    </tr>

    <tr>
      <td>
        Fill Rate Weight
      </td>

      <td>
        The vehicle fill rate by weight of all orders delivered to that customers
      </td>
    </tr>

    <tr>
      <td>
        Total Amount to Collect
      </td>

      <td>
        Amount of money to be collected from that customer, equals to the total price of all orders delivered to that customer
      </td>
    </tr>
  </tbody>
</Table>

## View route information

* You can view the detailed information of a particular route or several routes by clicking on the corresponding :fa-eye: icon of those routes
* You can also view the detailed information of all routes by clicking on the :fa-eye: icon next to **Vehicle** text
* The detailed information will display on the status bar at the bottom of the Timeline panel

<Image title="Wxj699wvIq.png" alt={1920} border={true} src="https://files.readme.io/d250b33-Wxj699wvIq.png">
  Select route of one vehicle
</Image>

<Image title="rPPgXdB6ot.png" alt={1920} border={true} src="https://files.readme.io/3658ea7-rPPgXdB6ot.png">
  Select routes of several vehicles
</Image>

<Image title="AQhvvSt8Co.png" alt={1920} border={true} src="https://files.readme.io/56cbd45-AQhvvSt8Co.png">
  Select routes of all vehicles
</Image>

* Below is the list of information fields of a route

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
        Orders
      </td>

      <td>
        The number of orders on the selected route(s)
      </td>
    </tr>

    <tr>
      <td>
        Distance
      </td>

      <td>
        The projected travel distance of the vehicle(s)\
        Unit: Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        Costs
      </td>

      <td>
        The projected operation cost needed to perform the selected route(s)\
        Unit: The currency unit according to the "Country" information field of the Manufacturer (VND for Vietnam; MMK for Myanmar; Rp for Indonesia)
      </td>
    </tr>

    <tr>
      <td>
        Revenues
      </td>

      <td>
        The projected revenue of the selected route(s)\
        Unit: The currency unit according to the "Country" information field of the Manufacturer (VND for Vietnam; MMK for Myanmar; Rp for Indonesia)
      </td>
    </tr>

    <tr>
      <td>
        Productivity
      </td>

      <td>
        The projected profit of the selected route(s)\
        Unit: The currency unit according to the "Country" information field of the Manufacturer (VND for Vietnam; MMK for Myanmar; Rp for Indonesia)
      </td>
    </tr>

    <tr>
      <td>
        Revenues/Distance
      </td>

      <td>
        The projected revenue per kilometer\
        Unit: VND/km or MMK/km or Rp/km
      </td>
    </tr>

    <tr>
      <td>
        Weight/Capacity
      </td>

      <td>
        The total weights of all orders over the weight capacity of the vehicle(s)\
        Unit: kilogram (kg)
      </td>
    </tr>

    <tr>
      <td>
        Volume/Capacity
      </td>

      <td>
        The total volume of all orders over the volume capacity of the vehicle(s)\
        Unit: cubic metre (m3)
      </td>
    </tr>

    <tr>
      <td>
        Truck/Bike/Total
      </td>

      <td>
        The number of delivery vehicles utilized which are Truck/Semi-truck; Motorbike and the total number of vehicles utilized
      </td>
    </tr>

    <tr>
      <td>
        Familiarity
      </td>

      <td>
        The ratio of the number of customers whose familiarity constraint have been met over the total number of customers
      </td>
    </tr>
  </tbody>
</Table>

## View and export lists

## Packing List and Order List

* **Packing List** is the detailed list of the products that have been packed at the Depot, including the Product Code; Product Name; Quantity and Weight
* **Order List** is the detailed list of the orders and destination customers
* To view these lists, click on the vehicle icon :fa-truck: of a vehicle. The information panel of that vehicle will appear on the right side of the map screen. Scroll down that panel and click on the corresponding text **Packing List** or **Order List**
* Below are the information fields of each list

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Packing List
      </th>

      <th>
        Order List
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Total Weight
      </td>

      <td>
        Total Orders
      </td>
    </tr>

    <tr>
      <td>
        Total Cases
      </td>

      <td>
        Total Costs
      </td>
    </tr>

    <tr>
      <td>
        Total Items
      </td>

      <td>
        Total Revenues
      </td>
    </tr>

    <tr>
      <td>
        Product Code
      </td>

      <td>
        Total Profits
      </td>
    </tr>

    <tr>
      <td>
        Product Name
      </td>

      <td>
        Order Code
      </td>
    </tr>

    <tr>
      <td>
        Weight (kg)
      </td>

      <td>
        Customer Code
      </td>
    </tr>

    <tr>
      <td>
        Cases
      </td>

      <td>
        Customer Name
      </td>
    </tr>

    <tr>
      <td>
        Items
      </td>

      <td>
        Customer Address
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Amount (VND)
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Note
      </td>
    </tr>
  </tbody>
</Table>

<Image title="SLbXFLBlcv.png" alt={1920} className="border" border={true} src="https://files.readme.io/1d2980c-SLbXFLBlcv.png" />

* The list will appear. To export click on the **Export** button

<Image title="nCmDVd3r1r.png" alt={1024} border={true} src="https://files.readme.io/149c942-nCmDVd3r1r.png">
  Packing List
</Image>

<Image title="Image 7.png" alt={1044} border={true} src="https://files.readme.io/6863df3-Image_7.png">
  Order List
</Image>

## Picking List

* **Picking List** is the combination of the **Packing List** and **Order List** mentioned above. This list provides the delivery information of each vehicle, including: License Plate; Order Code; Customer Code; Customer Name; Product Code; Product Name; Quantity of single product items

<Image title="ji958U4km0.png" alt={699} border={true} src="https://files.readme.io/61672bb-ji958U4km0.png">
  Picking List
</Image>

## Filter delivery man (Driver)

* You can view the list of delivery men (Drivers) who have been assigned the delivery tasks, by clicking on **Filter Deliverers** button on the top right of the map screen
* The form **Filter Deliverers** will appear. Here you can view the list of all Transporters and the vehicle that have been utilized for the current delivery plan
* You can click on the building icon :fa-home: next to each Transporter's name to show/hide the vehicles of that Transporter

<Image title="Selection_010.png" alt={1912} className="border" border={true} src="https://files.readme.io/c121105-Selection_010.png" />

## Export route plan

* After you have optimized the delivery routes of all vehicles, you can export the whole route plan by following the steps below
* On the Timeline panel, click on the **Export Planned Route(s)** icon :fa-download: next to the text **VEHICLE**

![1911](https://files.readme.io/4ef6b5f-Selection_011.png "Selection_011.png")

* The route plan will be exported immediately in the form of an Excel template that you can view offline
* Below are the information fields in the Route Plan Excel template

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
        No.
      </td>

      <td>
        Numerical order of the Order
      </td>
    </tr>

    <tr>
      <td>
        Order Code
      </td>

      <td>
        Management code of the Order
      </td>
    </tr>

    <tr>
      <td>
        Product Name
      </td>

      <td>
        Name of the product
      </td>
    </tr>

    <tr>
      <td>
        Trip Code
      </td>

      <td>
        Code of the Delivery Trip on which the Order was put
      </td>
    </tr>

    <tr>
      <td>
        Origin Pickup
      </td>

      <td>
        Name of the Origin Depot, where the Transporter vehicle will pick up products
      </td>
    </tr>

    <tr>
      <td>
        Destination Delivery
      </td>

      <td>
        Name of the Destination Depot, where the Transporter vehicle will deliver products
      </td>
    </tr>

    <tr>
      <td>
        Cost Bearer Description
      </td>

      <td>
        Description about the Depot that will bear the incurred Charge
      </td>
    </tr>

    <tr>
      <td>
        Transporter Code
      </td>

      <td>
        Management code of the Transporter that delivered the Order
      </td>
    </tr>

    <tr>
      <td>
        Transporter Name
      </td>

      <td>
        Name of the Transporter that delivered the Order
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Type Code
      </td>

      <td>
        Management code of the Transporter's Vehicle type that delivered the Order
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Type Name
      </td>

      <td>
        Name of the Transporter's Vehicle type that delivered the Order
      </td>
    </tr>

    <tr>
      <td>
        Transport Service Price
      </td>

      <td>
        The original Transport Service Price of the Transporter's Vehicle Type
      </td>
    </tr>

    <tr>
      <td>
        After Discount Rate
      </td>

      <td>
        The actually applied Transport service price percentage (After subtracting the discount percentage)\
        Format: Percentage
      </td>
    </tr>

    <tr>
      <td>
        Surcharge
      </td>

      <td>
        The extra Transport service rate of the Order (If this Order is the second Order on the delivery route of the assigned vehicle)
      </td>
    </tr>

    <tr>
      <td>
        Total Service Price
      </td>

      <td>
        The actual transport service price after discount
      </td>
    </tr>

    <tr>
      <td>
        License Plate
      </td>

      <td>
        License Plate numbers of the vehicle which delivered the Order
      </td>
    </tr>

    <tr>
      <td>
        Driver Name
      </td>

      <td>
        Name of the driver who operated the vehicle
      </td>
    </tr>

    <tr>
      <td>
        Driver Phone Number
      </td>

      <td>
        Phone number of the vehicle's driver
      </td>
    </tr>

    <tr>
      <td>
        Planned Delivery Date
      </td>

      <td>
        The date on which the Order was put on the optimized Delivery Route
      </td>
    </tr>

    <tr>
      <td>
        Origin Warehouseman Username
      </td>

      <td>
        Username of the Origin Depot's warehouseman
      </td>
    </tr>

    <tr>
      <td>
        Origin Warehouseman Name
      </td>

      <td>
        Name of the Origin Depot's warehouseman
      </td>
    </tr>

    <tr>
      <td>
        Origin Warehouseman Phone Number
      </td>

      <td>
        Phone number of the Origin Depot's warehouseman
      </td>
    </tr>

    <tr>
      <td>
        Destination Warehouseman Username
      </td>

      <td>
        Username of the Destination Depot's warehouseman
      </td>
    </tr>

    <tr>
      <td>
        Destination Warehouseman Name
      </td>

      <td>
        Name of the Destination Depot's warehouseman
      </td>
    </tr>

    <tr>
      <td>
        Destination Warehouseman Phone Number
      </td>

      <td>
        Phone number of the Destination Depot's warehouseman
      </td>
    </tr>

    <tr>
      <td>
        Branch Name
      </td>

      <td>
        Name of the Branch which directly manages the Order
      </td>
    </tr>
  </tbody>
</Table>
