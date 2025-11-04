---
title: Route Plan Optimization (New Map View)
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: basic
      slug: pdp-in-house-fleet-planned-loading-unloading-time
      title: Planned Loading/Unloading time calculation
---
## Route Plan Definition

* Route Plan is the plan that consists of the optimized Delivery Routes of all Orders under a Branch on a particular day

## Tasks of the Route Planner

* After you have created Sales Orders for all Depots under the management of a Branch, the next step is to perform the Route Plan Optimization process for those Orders
* In this model, a typical Route Plan optimization process comprises three phases:
* **Phase 1:** Select the Branch and the Route Plan date
* **Phase 2:** Generate the optimized Delivery Routes of the Vehicles on the selected Route Plan date
* **Phase 3:** Lock the optimized Delivery Routes and create the Delivery Tasks for the Drivers
* In order to get a better understanding of the Route Plan optimization process, we recommend you learn about the different delivery journey units of this model in the following section: [**Delivery Journey Units**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-map-view#delivery-journey-units)

## Necessary Preparations

* **Configuration** 

- Choose the icon Edit Manufacturer:

<Image title="2.png" alt={1919} src="https://files.readme.io/0601042-2.png">
  Illustration (English)
</Image>

![1916](https://files.readme.io/a2f98d3-1.png "1.png")

* Choose on igurations] tab -> Ch tab -> Choose on dul=> C modul=> Choose studio ew] => Chọn b => Chọn button lock:i

<Image title="3.png" alt={1923} src="https://files.readme.io/1cad280-3.png">
  Illustration (English)
</Image>

<Image title="4.png" alt={1924} src="https://files.readme.io/77e718c-4.png">
  Illustration (VN)
</Image>

After selecting the studio New map view will display the Planning module

<Image title="1.4.png" alt={1918} src="https://files.readme.io/637cb0c-1.4.png">
  Illustration (English)
</Image>

<Image title="1.3.png" alt={1920} src="https://files.readme.io/5b2e18e-1.3.png">
  Illustration (VN)
</Image>

* In order to perform the Route Plan optimization process, make sure the following resources have all the necessary information:
* 1 - The Depots/Crossdock: Latitude; Longitude; Open Time

<Image title="6.png" alt={900} src="https://files.readme.io/7317f9d-6.png">
  Illustration (English)
</Image>

<Image title="7.png" alt={902} src="https://files.readme.io/11d95c2-7.png">
  Illustration (VN)
</Image>

* 2 - The Customer: Latitude; Longitude; Open Time; Close Time; Allowed Vehicle Types (The system default Vehicle Types - Motorbike; Truck/Semi-truck, or custom Vehicle Types input by the users); Minimum and Maximum Unloading Time

<Image title="8.png" alt={866} src="https://files.readme.io/0696b4b-8.png">
  Illustration (English)
</Image>

<Image title="9.png" alt={866} src="https://files.readme.io/b50ad91-9.png">
  Illustration (VN)
</Image>

* 3 - The Vehicles: Start Time; Stop Time; Weight; Volume; Speed. You also need to set the Active Status of the Vehicles that you wish to use in the Route Plan optimization process to ***Active***

<Image title="10.png" alt={711} src="https://files.readme.io/c09f01e-10.png">
  Illustration (English)
</Image>

<Image title="11.png" alt={718} src="https://files.readme.io/c8c4928-11.png">
  Illustration (VN)
</Image>

## Phase 1: Select Branch And Route Plan date

* Choose the Planning Modul : 
* **Create route plan:**
* When you haven't created a route: Choose an icon (+) => Choose to Create button => Choose Branch, Date => Choose Confirm button -> Display create route plan on the Planning module screen

<Image title="12.png" alt={464} src="https://files.readme.io/4942fe9-12.png">
  Illustration (English)
</Image>

<Image title="14.png" alt={471} src="https://files.readme.io/05e56d6-14.png">
  Illustration (VN)
</Image>

* **Import Route Plan** 
* When you haven't created a route: Choose an icon (+) => Choose to Import Route Plan button => Choose Organization, Date and Drop import file hể or click to upload => Choose to Start upload button -> Show route plan and shift the number of route plan according to import file

<Image title="15.png" alt={549} src="https://files.readme.io/774d16b-15.png">
  Illustration (English)
</Image>

<Image title="16.png" alt={558} src="https://files.readme.io/0971a96-16.png">
  Illustration (VN)
</Image>

* File import data template: 

<Image title="17.png" alt={1926} src="https://files.readme.io/232b9d8-17.png">
  Illustration (English)
</Image>

<Image title="18.png" alt={1914} src="https://files.readme.io/0da26b3-18.png">
  Illustration (VN)
</Image>

* After the user creates the route => Click on the **View Map** icon 

<Image title="19.png" alt={1908} src="https://files.readme.io/f426ae6-19.png">
  Illustration (English)
</Image>

<Image title="20.png" alt={1919} src="https://files.readme.io/2c0a576-20.png">
  Illustration (VN)
</Image>

* The route has not been optimized yet: You will be taken to the **Maps** screen \* On the Maps screen, a form will automatically appear. On this form, you have to select the **Branch** and **Date** to create a Vehicle-Optimized Delivery Route

<Image title="21.png" alt={514} src="https://files.readme.io/c13c978-21.png">
  Illustration (English)
</Image>

<Image title="23.png" alt={714} src="https://files.readme.io/7c3dd28-23.png">
  Illustration (VN)
</Image>

* **Branch:** Click on this field. Select the appropriate Branch from the drop-down list. Alternatively, you could input the Organization Name of the Branch into the search bar, the system will filter out the Branch being searched

<Image title="30.png" alt={578} src="https://files.readme.io/677f5ee-30.png">
  Illustration (English)
</Image>

* **Date:** Click on the calendar :fa-calendar-o: icon. A drop-down calendar will appear to let you select the date on which you want to generate the optimized Delivery Routes for the Orders. This date equals the **Order Date** attribute of the Sales Orders. Alternatively, you can directly input the date in the field following the ***mm/dd/yyyy (Month/Date/Year)*** format

<Image title="22.3.png" alt={1920} src="https://files.readme.io/bcb7564-22.3.png">
  Illustration (English)
</Image>

## Phase 2: Generate Optimized Delivery Routes

* **The route has not been optimized yet:** 
* After creating the route, select the map view icon. The **Optimize Route** form will appear. On this form, click choose button **Confirm** 

<Image title="31.png" alt={432} src="https://files.readme.io/1adaafd-31.png">
  Illustration (English)
</Image>

<Image title="32.png" alt={526} src="https://files.readme.io/4431aab-32.png">
  Illustration (VN)
</Image>

* The system will start gathering all the Orders of which the **Order Date** attribute is the same as the Route Plan date that you have selected above, allocate them to the suitable active Vehicles, then display the optimized Delivery Route of the Vehicles on the Timeline panel

<Image title="25.png" alt={1865} src="https://files.readme.io/4c0d908-25.png">
  Illustration (English)
</Image>

<Image title="24.png" alt={1861} src="https://files.readme.io/6ab3504-24.png">
  Illustration (VN)
</Image>

* **Optimized route or import route plan:** when the map view icon is selected, the route will be displayed on the map view screen according to the last optimization or according to the import route plan file.

<Image title="33.png" alt={1920} src="https://files.readme.io/de319af-33.png">
  Illustration (English)
</Image>

* The default routing algorithm that the system utilizes is described in the following section: [**Default Routing Algorithm**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-map-view#default-routing-algorithm)
* To understand how the loading/unloading time (The unloading time is also referred to as the ***Service Time***) is calculated, please refer to the following article: [**Service Time Calculation**]()
* The Route Plan screen holds numerous information and functions. Please refer to the following section to learn more: [**Route Plan Screen Description**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-map-view#section-route-map-screen-description)
* In this phase, you can make necessary adjustments to the optimized Delivery Routes recently generated, such as Change Delivery Shift driver; Change Customer coordinates; Adjust Customer sequence on a Delivery Trip/Delivery Shift, etc. The detailed instructions are presented in the following article: [**Route Plan Adjustment (Map View)**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-adjustment)

## Phase 3: Lock Optimized Delivery Routes And Create Delivery Tasks

* If you see that the optimized Delivery Routes generated by the system have met your expectation, or after you have made appropriate adjustments, you can now lock the Delivery Routes by clicking on the **Lock Route** button
* A confirmation form will appear. Click **Confirm** to confirmation

<Image title="34.png" alt={1868} src="https://files.readme.io/41be2e7-34.png">
  Illustration (English)
</Image>

<Image title="35.png" alt={1870} src="https://files.readme.io/9f8b7b6-35.png">
  Illustration (VN)
</Image>

> 📘 For customers using the mobile app, before locking the route, the user needs to assign a driver to the vehicle

* Once you have locked the Delivery Route, in the route the dashed lines will become solid lines on the Timeline panel
* Part of the recently locked Delivery Route is identified as ***Delivery Shift***
* When the Delivery Shift is locked, the delivery task will be created and sent to the mobile app of the vehicle driver. Delivery tasks will also show up in the **Tasks > Tasks** tab
* To track actual vehicle delivery progress in real-time, you can use Timelines. Please refer to the following article for instructions: [**Track delivery progress**]()
* To update the results of delivery tasks, go to the **Tasks > Tasks** tab. Please refer to the following article for instructions: [**Manage Tasks**]()

<Image title="36.png" alt={1871} src="https://files.readme.io/3a6a31a-36.png">
  Illustration (English)
</Image>

<Image title="37.png" alt={1872} src="https://files.readme.io/75cfbd3-37.png">
  Illustration (VN)
</Image>

* In case you want to change certain elements of the recently locked Delivery Shifts (Such as remove or add Orders), you can unlock them
* To unlock the locked Delivery Shifts, click the **Unlock** button at the bottom right of the Timeline panel
* A confirmation dialog will display. Click **OK** to continue
* The system will revert the locked Delivery Shifts to ***Planned*** status

<Image title="38.png" alt={1916} src="https://files.readme.io/c10bc4d-38.png">
  Illustration (English)
</Image>

<Image title="39.png" alt={1919} src="https://files.readme.io/2196a95-39.png">
  Illustration (VN)
</Image>

## Default Routing Algorithm

* By default, if you don't enable any other additional algorithm configurations, the system will apply the fundamental constraints of the classic Vehicle Routing Problem to the optimized Delivery Routes:
* 1 - One visit per Customer: A Customer will be visited ***only once*** per Delivery Shift. This means that if a Customer places multiple Orders, the system will 1. allocate all of that Customer's Orders to one vehicle instead of several vehicles, and 2. plan the assigned vehicle to deliver all Orders of that Customer in one turn per Delivery Shift instead of several turns
* **Note**: This constraint might lead to a situation where there is no vehicle that has enough weight and/or volume capacity to carry the Orders of a particular Customer in one turn. In this situation, the system will treat that Customer's Orders as [**Unplanned (Missing) Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-unplanned-missing-orders)
* 2 - Closed Route: The Vehicles are planned to travel back to their managing Depots after completing all assigned delivery tasks

## Route Plan Screen Description

* The Route Plan screen is divided into two sections: The Route Map and the Timeline panel

<Image title="41.png" alt={1919} src="https://files.readme.io/53ccc7a-41.png">
  Illustration (English)
</Image>

<Image title="40.png" alt={1920} src="https://files.readme.io/8678c2b-40.png">
  Illustration (Illustration (VN)
</Image>

## Route Map Section

* To zoom in/zoom out the Route Map, move your mouse onto a point on the Route Map, then use the middle scroll button to zoom in/zoom out

<Image title="42.gif" alt={1152} src="https://files.readme.io/4ed8c9a-42.gif">
  Illustration (English)
</Image>

<Image title="43.gif" alt={1152} src="https://files.readme.io/5c5c64d-43.gif">
  Illustration (VN)
</Image>

* To move around the Route Map, left-click on a point on the Route Map, then, with the left button still clicked, drag your mouse around

<Image title="44.gif" alt={1152} src="https://files.readme.io/e5bea19-44.gif">
  Illustration (English)
</Image>

<Image title="45.gif" alt={1152} src="https://files.readme.io/0d86297-45.gif">
  Illustration (VN)
</Image>

* To change the color theme of the Route Map, hover your mouse over the color box near the top left corner of the Route Map. The box will then expand and shows three color themes: Default; Light and Dark. Select the appropriate color theme

<Image title="47.gif" alt={1152} src="https://files.readme.io/c516100-47.gif">
  Illustration (English)
</Image>

<Image title="46.gif" alt={1152} src="https://files.readme.io/4ddd870-46.gif">
  Illustration (VN)
</Image>

* To see the actual photos of a particular road on the Route Map, you can use the **Street View** mode
* To access this mode, click on the Pegman icon :fa-child: above the Toggle Fullscreen View button, then drag it onto a point on the Route Map where you want to view the actual road. There will be a small thumbnail showing the actual photo that was taken at that point. Release the left mouse and you will be navigated to the Street View mode
* In the Street View mode, you can left-click and drag the mouse around to view more angles of the road
* You can also zoom in and zoom out just like in the Route Map
* To exit the Street View mode and return to the Route Map, click on the left arrow icon :fa-arrow-left: on the top left corner of the Street View

<Image title="48.gif" alt={1152} src="https://files.readme.io/900175d-48.gif">
  Illustration (English)
</Image>

<Image title="49.gif" alt={1152} src="https://files.readme.io/c4656b9-49.gif">
  Illustration (VN)
</Image>

## Timeline Panel Section

* The Timeline panel section consists of many parts:
* 1 - The Delivery Timelines
* 2 - The Vehicle List
* 3 - The Route Plan command buttons
* 4 - The Plan/Execution Timeline switch button
* 5 - The artboard icons
* 6 - The general Delivery Routes information bar
* 7 -  Missing Orders area/ New Orders area

<Image title="63.png" alt={1770} src="https://files.readme.io/c7af41b-63.png">
  Illustration (English)
</Image>

<Image title="64.png" alt={1771} src="https://files.readme.io/964850a-64.png">
  Illustration (VN)
</Image>

* We will go into details of each part below

### Part 1. The Delivery Timelines

* The Delivery Timelines of the Vehicles occupy most of the space of the Timeline panel
* The Delivery Timeline will visually present the following time points and time periods during the Vehicle's Delivery Route: 
* 1 - **Shift Start Time**: The time point that a Delivery Shift is supposed to start
* 2 - **Shift End Time**: The time point that a Delivery Shift is supposed to end
* 3 - **Loading Time**: The time period that the Vehicles use to load Products at the managing warehouses at the beginning of their Delivery Shift
* 4 - **Travel Time**: The time period that the Vehicles travel between the Delivery Stops on their assigned Delivery Routes
* 5 - **Unloading Time** (Also known as **Service Time**): The time period that the Vehicles use to deliver the Products at the Customers' receiving locations
* 6 - **Cut-off Time**: The designated time point to start the next Delivery Shift of a Vehicle (If the Delivery Route of that Vehicle consists of more than one Delivery Shift)

- On a Delivery Timeline, the two time periods that the vehicle spends at its managing warehouse at the beginning and end of a Delivery Trip are represented by the time blocks that have the warehouse symbol inside

<Image title="65.png" alt={63} src="https://files.readme.io/b09b65b-65.png">
  Illustration
</Image>

* At the beginning of each Delivery Trip, the warehouse time block also has two percentage indicators on the two sides of the warehouse symbol

<Image title="66.png" alt={151} src="https://files.readme.io/fda1962-66.png">
  Illustration
</Image>

* The percentage indicator to the left of the warehouse symbol is the **Weight Load** indicator. It indicates the percentage of the total product weight over the weight capacity of the vehicle for a Delivery Trip
* For example, in a Delivery Trip, the vehicle is planned to load ***50 kilograms*** of product. Its weight capacity is ***500 kilograms***. The weight load indicator, therefore, will display ***10 percent***
* The percentage indicator to the right of the warehouse symbol is the **Volume Load** indicator. It indicates the percentage of the total product volume over the volume capacity of the vehicle for a Delivery Trip
* For example, in a Delivery Trip, the vehicle is planned to load ***5 cubic meters (5 m3)*** of product. Its volume capacity is ***50 cubic meters (50 m3)***. The volume load indicator, therefore, will display ***10 percent***
* The time periods that the vehicle spends at the Customers' locations to unload/deliver products are represented by the blank time blocks

<Image title="67.png" alt={72} src="https://files.readme.io/40a2954-67.png">
  Illustration
</Image>

* * Dashed lines connecting time blocks represent vehicle travel time.

<Image title="68.png" alt={307} src="https://files.readme.io/90f50f3-68.png">
  Illustration
</Image>

* If a Delivery Timeline is too long that it exceeds the screen length, you can click on the horizontal navigation bar near the bottom of the Timeline panel and drag it to the left or to the right to view the remaining part of that Delivery Timeline

<Image title="70.gif" alt={1152} src="https://files.readme.io/ccd4bb2-70.gif">
  Illustration (English)
</Image>

<Image title="69.gif" alt={1152} src="https://files.readme.io/667b346-69.gif">
  Illustration (VN)
</Image>

* To view the assigned driver of the Delivery Shift, hover over the person icon :fa-user: above the center of the warehouse or stop of the Delivery Shift.

<Image title="72.gif" alt={1152} src="https://files.readme.io/71aea1f-72.gif">
  Illustration (English)
</Image>

<Image title="71.gif" alt={1152} src="https://files.readme.io/c7f8d90-71.gif">
  Illustration (VN)
</Image>

* As you click on a time block of the warehouse or of the Customer, an information panel will appear to the right of the Route Map. On this panel, you can see some information about the warehouse/Customer
* Below are the information fields on the warehouse information panel

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
        Organization Code of the warehouse
      </td>
    </tr>

    <tr>
      <td>
        Organization Name
      </td>

      <td>
        Organization Name of the warehouse
      </td>
    </tr>

    <tr>
      <td>
        Address
      </td>

      <td>
        Address of the warehouse
      </td>
    </tr>

    <tr>
      <td>
        Reaching Time
      </td>

      <td>
        The time points when the vehicle is planned to arrive at and leave the warehouse
      </td>
    </tr>

    <tr>
      <td>
        Total Weight by Product
      </td>

      <td>
        The total weight of all products planned to be loaded onto the vehicle at the warehouse\
        Unit: Kilogram (kg
      </td>
    </tr>

    <tr>
      <td>
        Total Volume by Product
      </td>

      <td>
        The total volume of all products planned to be loaded onto the vehicle at the warehouse\
        Unit: Cubic meter (m3)
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Fill Rate By Volume (%)
      </td>

      <td>
        The Fill Rate of the vehicle is based on the Volume of products loaded onto the vehicle\
        Unit: Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        The volume of each product
      </td>

      <td>
        The volume of each Product or SKU\
        Unit: Cubic meter (m3)
      </td>
    </tr>
  </tbody>
</Table>

Below are the information fields on the Customer information panel

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
        Customer Code
      </td>

      <td>
        The Customer Code the customer
      </td>
    </tr>

    <tr>
      <td>
        Customer Name
      </td>

      <td>
        The Customer Name of the customer
      </td>
    </tr>

    <tr>
      <td>
        Address
      </td>

      <td>
        Address of the customer
      </td>
    </tr>

    <tr>
      <td>
        MDP
      </td>

      <td>
        The MDP code of the customer (If available)\
        Read more about this feature in the following article: [**Familiarity Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-familiarity-constraint)
      </td>
    </tr>

    <tr>
      <td>
        Customer Time Window
      </td>

      <td>
        Client's time frame
      </td>
    </tr>

    <tr>
      <td>
        Open & Close
      </td>

      <td>
        The Open time and Close time of the customer
      </td>
    </tr>

    <tr>
      <td>
        Allow Vehicle Type
      </td>

      <td>
        Types of vehicles allowed use when delivering goods to customers
      </td>
    </tr>

    <tr>
      <td>
        Cluster
      </td>

      <td>
        Cluster customers
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Type
      </td>

      <td>
        Type of means of delivery to customers
      </td>
    </tr>

    <tr>
      <td>
        Temperature
      </td>

      <td>
        Temperature levels of the products planned to be delivered to the customer
      </td>
    </tr>

    <tr>
      <td>
        Reaching Time
      </td>

      <td>
        The time points when the vehicle is planned to arrive at and leave the customer
      </td>
    </tr>

    <tr>
      <td>
        Familiarity
      </td>

      <td>
        Specify whether the vehicle has Familiarity relationship with the customer or not\
        Read more about this feature in the following article: [**Familiarity Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-familiarity-constraint)
      </td>
    </tr>

    <tr>
      <td>
        Driver Name
      </td>

      <td>
        Name of the driver who is assigned to deliver to the customer
      </td>
    </tr>

    <tr>
      <td>
        Orders
      </td>

      <td>
        List of Order(s) planned to be delivered to the customer
      </td>
    </tr>

    <tr>
      <td>
        Product Categories
      </td>

      <td>
        Products will be grouped into Product Categories\
        Read more about this feature in the following article: s of the optimized Deliv ([https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-product-categories](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-product-categories))
      </td>
    </tr>

    <tr>
      <td>
        Orders Time Window
      </td>

      <td>
        The time window of the order (If available)
      </td>
    </tr>

    <tr>
      <td>
        Total Product Weight
      </td>

      <td>
        The total weight of all products on the selected Delivery Route
      </td>
    </tr>

    <tr>
      <td>
        Total Product Volume
      </td>

      <td>
        The total volume of all products planned to be delivered to the customer
      </td>
    </tr>

    <tr>
      <td>
        Fill Rate Weight
      </td>

      <td>
        The vehicle fill rate by weight of the vehicle\
        Unit: Percentage (%)\
        This percentage is calculated by dividing The total weight of all products planned to be delivered to the customer by the weight capacity of the vehicle
      </td>
    </tr>

    <tr>
      <td>
        Fill Rate Volume
      </td>

      <td>
        The vehicle fill rate by volume of the vehicle\
        Unit: Percentage (%)\
        This percentage is calculated by dividing The total volume of all products planned to be delivered to the customer by the volume capacity of the vehicle
      </td>
    </tr>

    <tr>
      <td>
        Total Amount
      </td>

      <td>
        The total price of all orders to be delivered to the customer
      </td>
    </tr>
  </tbody>
</Table>

* On the warehouse information panel, apart from viewing the information, you can also view the Packing List, the Picking List, and Export Route Plan. The instruction is described in the following section: [**View And Export Route Plan Documents**]()

<Image title="73.gif" alt={1152} src="https://files.readme.io/b7a7a40-73.gif">
  Illustration (English)
</Image>

<Image title="74.gif" alt={1152} src="https://files.readme.io/c435a5e-74.gif">
  Illustration (VN)
</Image>

* On the Customer information panel, apart from viewing the information, you can also 1. Remove the Customer from the current Route Plan (The instruction is described in the following article: [**Route Plan Adjustment (Map View)**]()), and 2. View and export the Product List of that Customer (The instruction is described in the following section: [**View And Export Route Plan Documents**]())

### Part 2. The Vehicle List

* The vehicle list is located to the left of the Delivery Timelines
* Here, you can view the list of vehicles that the system used for the current Route Plan, along with some other information about the vehicles
* 1 - Shift to code
* 2 - Vehicle code
* 3 - Vehicle Type. The motorbike icon :fa-motorcycle: represents the Motorbike. The truck icon :fa-truck: icon represents the Truck/Semi-truck

<Image title="76.png" alt={856} src="https://files.readme.io/452a893-76.png">
  Illustration (English)
</Image>

<Image title="75.png" alt={802} src="https://files.readme.io/7d652ab-75.png">
  Illustration (VN)
</Image>

* To show/hide the optimized Delivery Routes of the Vehicles on the Route Map and display the vehicle's information, click on the corresponding vehicle icons :fa-vehicle: of the Vehicles on this list

<Image title="77.png" alt={1770} src="https://files.readme.io/da21ae1-77.png">
  Illustration (English)
</Image>

<Image title="78.png" alt={1770} src="https://files.readme.io/286c4d5-78.png">
  Illustration (VN)
</Image>

* Below are the information fields on the vehicle belonging to the depot or branch information panel: 

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
        Vehicle Typ
      </td>

      <td>
        Vehicle type information
      </td>
    </tr>

    <tr>
      <td>
        License Plate
      </td>

      <td>
        License Plate of vehicle
      </td>
    </tr>

    <tr>
      <td>
        Assigned
      </td>

      <td>
        The driver's name assigned to the vehicle
      </td>
    </tr>

    <tr>
      <td>
        Temp. Config
      </td>

      <td>
        Temperature setting for vehicle: Ambient, Chilled, Frozen
      </td>
    </tr>

    <tr>
      <td>
        Temp. Zone
      </td>

      <td>
        The number of the temptation of the vehicle
      </td>
    </tr>

    <tr>
      <td>
        Speed
      </td>

      <td>
        Vehicle speed
      </td>
    </tr>

    <tr>
      <td>
        Start Time
      </td>

      <td>
        Vehicle start time
      </td>
    </tr>

    <tr>
      <td>
        Stop Time
      </td>

      <td>
        Vehicle stop time
      </td>
    </tr>

    <tr>
      <td>
        Shifts
      </td>

      <td>
        Shift to code
      </td>
    </tr>
  </tbody>
</Table>

* Below are the information fields on the vehicle belonging to the transporter information panel: 

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
        Organization Name
      </td>

      <td>
        Organization Name of vehicle
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Type
      </td>

      <td>
        Vehicle type information
      </td>
    </tr>

    <tr>
      <td>
        License Plate
      </td>

      <td>
        License Plate of vehicle
      </td>
    </tr>

    <tr>
      <td>
        Assigned
      </td>

      <td>
        The driver's name assigned to the vehicle
      </td>
    </tr>

    <tr>
      <td>
        Temp. Config
      </td>

      <td>
        Temperature setting for vehicle: Ambient, Chilled, Frozen
      </td>
    </tr>

    <tr>
      <td>
        Temp. Zone
      </td>

      <td>
        The number of the temptation of the vehicle
      </td>
    </tr>

    <tr>
      <td>
        Speed
      </td>

      <td>
        Vehicle speed
      </td>
    </tr>

    <tr>
      <td>
        Start Time
      </td>

      <td>
        Vehicle start time
      </td>
    </tr>

    <tr>
      <td>
        Stop Time
      </td>

      <td>
        Vehicle stop time
      </td>
    </tr>

    <tr>
      <td>
        Shipment Fees (VND)
      </td>

      <td>
        Shipment Fees của shift: Total of shift, Freight Fee, Dropping Fee, Unloading Fee, Intransit Fee.\
        Each shift will be formatted with a shift to code.
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Transportation Fee
>
> * Freight fee = The freight of each shipment will count based on the furthest points.\
>   Unit: Trip
> * Dropping fee = Unit price list \* All remaining points of each shipment (exclude the farthest point.\
>   Unit: intersection
> * Unloading fee = Total CBM of this point \* Unit price list.\
>   Unit: CBM
> * Intransit fees are incurred at intersections on roads where heavy vehicles are prohibited from entering. Fees are calculated based on the available price list. Fees are charged for fixed customers.\
>   Unit: CBM

* To sort the vehicles by specific parameters (License Plate; Vehicle Type; Vehicle Weight; Vehicle Volume; Vehicle Fill Rate, Time slot, Shift Code), follow the steps below:
* Step 1: Click on the icon of two arrows in the opposite direction to the right of the text ***Xe***. A drop-down list will appear, displaying a list of parameters.
* Step 2: On the drop-down list, click the checkbox icons of the parameters by which you want to arrange the vehicles
* Step 3: Select the sorting mode for each parameter by clicking on the arrow icon at the end of each parameter. If you want to sort in ascending mode, leave the up arrow icon :fa-arrow-up:. If you want to sort in descending mode, click on that icon to switch it to the down arrow icon :fa-arrow-down:
* Step 4: Click **Apply**. The system will sort the vehicles by the selected parameters and sorting modes

<Image title="81.gif" alt={1152} src="https://files.readme.io/aabc86a-81.gif">
  Illustration (English)
</Image>

<Image title="82.gif" alt={1152} src="https://files.readme.io/66c1fbd-82.gif">
  Illustration (VN)
</Image>

* Here, you can also export some Route Plan documents: The Packing List and the Picking List. The detailed instruction is described in the following section: [**View And Export Route Plan Documents**]()

### Part 3. The Route Plan command buttons

* The set of buttons located at the bottom right of the Timeline Panel is the Route Plan command buttons. These buttons allow you to manipulate the Route Plan

<Image title="83.png" alt={1919} src="https://files.readme.io/7108135-83.png">
  Illustration (English)
</Image>

<Image title="84.png" alt={1920} src="https://files.readme.io/38a6492-84.png">
  Illustration (VN)
</Image>

### Part 4. Button Plan and button Execution

* When you want to see the route in route planner mode:

<Image title="85.png" alt={1920} src="https://files.readme.io/6526a66-85.png">
  Illustration (English)
</Image>

<Image title="86.png" alt={1920} src="https://files.readme.io/c38605f-86.png">
  Illustration (VN)
</Image>

* When you want to see the route in actual route planner mode.  \* The Execution allows you to track the delivery progress of the vehicles in real-time. Read more in the following article: [**Delivery Progress Tracking**](https://docs.abivin.com/docs/vrp-in-house-fleet-delivery-progress-tracking)

<Image title="87.png" alt={1920} src="https://files.readme.io/c4781d1-87.png">
  Illustration (English)
</Image>

<Image title="88.png" alt={1920} src="https://files.readme.io/474b9ea-88.png">
  Illustration (VN)
</Image>

### Part 5. Artboard Icons

* The Artboard icons are in the top right corner of the Timeline Panel.
* These icons allow you to change the number of Delivery Terms that will appear on the Timesheet
* The number of lines per Artboard icon indicates how many Delivery Terms will be on the Timeline panel.
* You can click the number ***8*** to display respectively up to ***eight*** Delivery term.
* If the number of Delivery Routes on the Time board is more than eight, you can click an empty spot on the Time Board and then use the middle scroll button on your mouse to scroll through the Delivery Routes
* To collapse the Timeline panel, click the down arrow button :fa-arrow-down: to the left of the text ***All***. You can then show the Timeline panel again by clicking the **Show Timeline** button in the bottom right corner of the Maps screen.

<Image title="89.png" alt={1772} src="https://files.readme.io/9ecd8a2-89.png">
  Illustration (English)
</Image>

<Image title="90.png" alt={1774} src="https://files.readme.io/9943941-90.png">
  Illustration (VN)
</Image>

### Part 6. The general Delivery Routes information bar

* At the bottom of the Timeline panel, you can see some general information related to the selected Delivery Route
* The information bar will update as you select more Delivery Routes

<Image title="91.png" alt={1769} src="https://files.readme.io/8c02592-91.png">
  Illustration (English)
</Image>

<Image title="92.png" alt={1770} src="https://files.readme.io/ed4b7eb-92.png">
  Illustration (VN)
</Image>

* Below are the information fields on this information bar

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
        Shifts
      </td>

      <td>
        Total number of cases in the route
      </td>
    </tr>

    <tr>
      <td>
        Orders
      </td>

      <td>
        The number of orders planned to be delivered by the selected vehicle
      </td>
    </tr>

    <tr>
      <td>
        Distance
      </td>

      <td>
        The distance planned to be traveled by the selected vehicle
      </td>
    </tr>

    <tr>
      <td>
        Revenue
      </td>

      <td>
        The planned revenues of the selected vehicle on the whole route\
        The revenue is calculated by adding up the total prices of all orders planned to be delivered by the selected vehicle
      </td>
    </tr>

    <tr>
      <td>
        Costs
      </td>

      <td>
        The total estimated operational cost of the selected vehicle's Delivery Route\
        This cost is calculated by the following formula:\
        Total estimated operational cost  = Fixed cost + Cost per km x Distance
      </td>
    </tr>

    <tr>
      <td>
        Productivity
      </td>

      <td>
        The difference between the Revenues minus the Costs of the selected vehicle's Delivery Route
      </td>
    </tr>

    <tr>
      <td>
        Revenue/Distance
      </td>

      <td>
        The average revenue per one kilometer of the selected vehicle's Delivery Route
      </td>
    </tr>

    <tr>
      <td>
        Weight/Capacity
      </td>

      <td>
        The total weight of all Orders  on the Delivery Route over the weight capacity of the selected vehicle
      </td>
    </tr>

    <tr>
      <td>
        Volume/Capacity
      </td>

      <td>
        The total volume of all Orders on the Delivery Route over the weight capacity of the selected vehicle
      </td>
    </tr>

    <tr>
      <td>
        Truck/Bike/Total
      </td>

      <td>
        The number of trucks/semi-trucks, the number of motorbikes, and the sum of all vehicles of these vehicle types that have been selected to perform the orders
      </td>
    </tr>

    <tr>
      <td>
        Familiarity
      </td>

      <td>
        The number of orders that meet the familiarity criteria over the total number of orders delivered by the selected vehicle\
        Read more about this feature in the following article: [**Familiarity Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-familiarity-constraint)
      </td>
    </tr>
  </tbody>
</Table>

## Delivery Journey Units

* In this model, there are three delivery journey units: Delivery Trip, Delivery Shift, Delivery Route

## Delivery Trip

* Delivery Trip is the most fundamental delivery journey unit. It is the delivery journey unit in which the vehicle starts at the managing warehouse, travels to the Customers, and then travels back to the warehouse

<Image title="93.png" alt={419} src="https://files.readme.io/303c8e6-93.png">
  Illustration
</Image>

## Delivery Shift

* Delivery Shift is the journey unit that the system generates after you perform the Delivery Route locking phase

<Image title="94.png" alt={425} src="https://files.readme.io/adfd8ef-94.png">
  Illustration
</Image>

* A Delivery Shift can consist of just a single Delivery Trip or multiple Delivery Trips
* The first delivery shift of the route will be started at the later of 
* 1. The open time of the Depot where the vehicles have to travel to and load products.
* 2. The starting time of the vehicles assigned.
* For example, an assigned vehicle starts at 6 AM, and the open time of the depot in charge is at 7 AM. Because the depot opens later than the assigned vehicle starts (7 AM is behind 6 AM), the depot's open time will be chosen as the start time of the first delivery shift.
* The following delivery shifts will be started after the delivery shifts right before them are finished and the cut-off time.

<Image title="95.png" alt={1920} src="https://files.readme.io/fd3abde-95.png">
  Illustration
</Image>

## Delivery Route

* Delivery Route is the final delivery journey unit of a vehicle. It encompasses both the Delivery Trip and Delivery Shift
* A Delivery Route can consist of just a single Delivery Shift or multiple Delivery Shifts 

<Image title="96.png" alt={1165} src="https://files.readme.io/865462f-96.png">
  A Typical Delivery Route with 2 Delivery Shifts
</Image>

## View And Export Route Plan Documents

* On the Route Plan screen, you can view and export the Route Plan documents: Packing List; Picking List; Order List; Product List

## Packing List

* The Packing List details the Order detail for each separate Customer on a Delivery Trip

## Picking List

* The Picking List lays out what products have been taken out of the Depot shelves for a Delivery Trip

## Order List

* The Order List specifies the Orders on a Delivery Trip

## Product List

* The Product List shows the products to be delivered to a specific Customer
* To view the Packing List/Picking List/Order List of a Delivery Trip, click on the respective Depot time block of that Delivery Trip on the Timeline panel. Upon clicking, an information panel will appear on the right side of the Map screen. You can access each list by clicking the respective text at the bottom of the panel

<Image title="97.gif" alt={1152} src="https://files.readme.io/f14fd05-97.gif">
  View And Export Route Plan Documents\
  (English)
</Image>

<Image title="98.gif" alt={1152} src="https://files.readme.io/dce34f7-98.gif">
  View And Export Route Plan Documents\
  (Vietnamese)
</Image>

* To view the Packing List of a Customer, click the respective time block of that Customer on the Timeline panel

<Image title="99.png" alt={1918} src="https://files.readme.io/ab82da8-99.png">
  Illustration Image (English)
</Image>

<Image title="100.png" alt={1923} src="https://files.readme.io/59c9602-100.png">
  Product List (Vietnamese)
</Image>

* To view the Picking List of a Customer, click the respective time block of that Customer on the Timeline panel

<Image title="101.png" alt={1918} src="https://files.readme.io/5c25107-101.png">
  Illustration Image (English)
</Image>

<Image title="102.png" alt={1918} src="https://files.readme.io/e1b31b9-102.png">
  Illustration Image (Vietnamese)
</Image>

* You can export these lists to Excel templates to view offline by clicking on the button **Export** :fa-download: 

- Packing List

<Image title="103.png" alt={1098} src="https://files.readme.io/6a49c8b-103.png">
  Illustration (English)
</Image>

<Image title="104.png" alt={1092} src="https://files.readme.io/444935b-104.png">
  Illustration (Vietnamese)
</Image>

* Picking List

<Image title="105.png" alt={1096} src="https://files.readme.io/b003987-105.png">
  Illustration Image (English)
</Image>

<Image title="106.png" alt={1100} src="https://files.readme.io/09850fe-106.png">
  Export Product List (Vietnamese)
</Image>

## Split Delivery

* There can be situations in which: A customer places multiple Orders or just one Order, but the total weight and/or volume of the products exceeds the weight and/or volume capacity of each of the active delivery vehicles in the Depot
* This will cause the Orders of that customer to not be optimizable during the Route Optimization process (Defined as **Missing Orders**)

## Manually Split Orders

* If you see that a single Order has its weight and/or volume exceeding the weight and/or volume capacity of each of the active delivery vehicles in the Depot, you can manually split that Order into other smaller Orders that fit better for the delivery vehicles' capacity. Please refer to the following instruction to know the detailed steps: [**Manually split an Order into smaller Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#section-manually-split-an-order-into-smaller-orders)
* For example: 

## Automatically Split Orders

> 📘 In order for this function to work, you need to enable the configuration **Split Delivery** at the Branch

* If an Order's weight and/or volume exceeds the weight and/or volume capacity of each of the active delivery vehicles in the Depot, then during the route optimization process, the system will try to automatically split that Order into several vehicles, according to the capacity of the vehicles. Vehicles with larger capacity will be selected first
* For example: The Order below, when initially created, is warned as ***Over-capacity***. It weights at ***200 kg***, a volume of ***120 m3***, while the Depot only has two active vehicles, a volume capacity to be ***13 m3***, and a weight capacity to be ***1500 kg***

<Image title="107.png" alt={1902} src="https://files.readme.io/a48cb81-107.png">
  Illustration Image (English)
</Image>

<Image title="108.png" alt={1905} src="https://files.readme.io/08911ab-108.png">
  Illustration Image (Vietnamese)
</Image>

* **Important Note**: If you want to edit the Original Order after it has been split during the Route Optimization process, you need to remove the optimized Delivery route. If the optimized Delivery route is still unlocked, you need to click on the **Unlock** button one time to remove it. If the optimized Delivery route has been locked, you need to click on **Unlock** button two times to remove it.

## Features on Mapview screen

## 1. New order

* When a user wants to add an order to a routed date, follow these steps:\
  **- Created add order:** Please refer to the te**](https://docs.abivin ([https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#create-multiple-orders-using-excel-template](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#create-multiple-orders-using-excel-template))\
  **- Import order:** Please refer to the [**Create multiple Orders using Excel template**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#create-multiple-orders-using-excel-template)\
  **-  On the map view screen:** Choose the Planning module -> Choose icon map view of newly created router/import to add order => The new order list will be displayed on the new orders area for users to easily drag and drop into the route on Map view or Unplanned Orders.

- The map view screen: 

<Image title="6.png" alt={1920} src="https://files.readme.io/bdb742d-6.png">
  Illustration (English)
</Image>

<Image title="51.png" alt={1919} src="https://files.readme.io/0d65a75-51.png">
  Illustration (VN)
</Image>

* Unplanned Orders screen: 

<Image title="52.gif" alt={1152} src="https://files.readme.io/e20c22d-52.gif">
  Illustration (English)
</Image>

<Image title="51.png" alt={1919} src="https://files.readme.io/3321108-51.png">
  Illustration (English)
</Image>

* The user then performs the following actions on the new order:
  * Move the order to the vehicle on the route (the route is not locked): New order after move is displayed at the move position and not in the new order list.
  * Move the order to the vehicle on the route (the route is not locked):\
      For the close route, when you move a new order to the locked route, the system will automatically generate a new shift according to the time you choose to start the shift.\
      For the close route, you cannot move new orders to locked routes.\
      **On the Map view screen:** 

<Image title="54.gif" alt={1152} src="https://files.readme.io/1db3052-54.gif">
  Illustration (English)
</Image>

* Unplanned Orders screen:

<Image title="55.gif" alt={1152} src="https://files.readme.io/2b7a4f6-55.gif">
  Illustration (English)
</Image>

* If you find that Delivery Routes have met your expectations, or after you have made the appropriate adjustments, you can now lock Delivery Routes by clicking the **Lock Route** button. A confirmation form will appear. Click **OK** to confirm.

## 2. Quick Edit Mode

**Enabling Quick Edit Mode and Utilizing Its Features:**

* Configuration in Manufacturer: Navigate to Organizations Module > Organizations Resource > Edit > More Configurations > Route > Click on checkbox Edit mode Route Plan

<Image title="112.gif" alt={1152} src="https://files.readme.io/a347dfe-112.gif">
  Illustration (English)
</Image>

<Image title="111.gif" alt={1152} src="https://files.readme.io/e36a356-111.gif">
  Illustration (Vietnamese)
</Image>

* A toggle to switch on/off Edit mode on your Mapview

<Image title="109.png" alt={1919} src="https://files.readme.io/99bbccd-109.png">
  Illustration (English)
</Image>

<Image title="110.png" alt={1919} src="https://files.readme.io/123e9e2-110.png">
  Illustration (Vietnamese)
</Image>

* When switching to enable Edit mode, you perform the following operations: move a stop, move missing order, remove stop/ route, change the vehicle, assign driver, and change driver, ... after each operation will be displayed the number of operations at the History step.

<Image title="113.png" alt={1921} src="https://files.readme.io/04908d4-113.png">
  Illustration (English)
</Image>

![1919](https://files.readme.io/312258e-114.png "114.png")

## Update Ship-to Address

* Now you can easily select the address of the customer and the plan will be changed based on your selection
* First, choose the customer you want to change their address, then click on *Update Ship-to Address*

<Image title="Screenshot from 2023-03-09 09-19-37.png" alt={1843} src="https://files.readme.io/d342c75-Screenshot_from_2023-03-09_09-19-37.png">
  Update Ship-to Address
</Image>

* Then, the system will show a pop-up containing a list of ship-to address of the customer. Select the one you want to change

<Image title="Screenshot from 2023-03-09 09-32-12.png" alt={539} src="https://files.readme.io/b968b49-Screenshot_from_2023-03-09_09-32-12.png">
  Select appropriate address
</Image>

* The confirmation pop-up will be shown, click on Confirm button

![600](https://files.readme.io/65ac7bd-Screenshot_from_2023-03-09_09-33-35.png "Screenshot from 2023-03-09 09-33-35.png")

* The route will be changed and the address of the customer will be updated as the selected address

![475](https://files.readme.io/4b0a77d-Screenshot_from_2023-03-09_09-33-58.png "Screenshot from 2023-03-09 09-33-58.png")
