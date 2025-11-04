---
title: Route Plan Optimization (Old Map View)
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
    - type: link
      title: Planned Loading/Unloading time
      url: >-
        https://docs.abivin.com/docs/vrp-in-house-fleet-planned-loading-and-unloading-time-calculation
---
* After you have created Sales Orders of all Depots under the management of a Branch, the next step is to perform the Route Plan Optimization process for those Orders
* In this model, a typical Route Plan optimization process comprises three phases:
* **Phase 1:** Select the Branch and the Route Plan date
* **Phase 2:** Generate the optimized Delivery Routes of the Vehicles on the selected Route Plan date
* **Phase 3:** Lock the optimized Delivery Routes and create the Delivery Tasks for the Drivers
* In order to get a better understanding of the Route Plan optimization process, we recommend you learn about the different delivery journey units of this model in the following section: [**Delivery Journey Units**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-map-view#delivery-journey-units)

## Necessary Preparations

* In order to perform the Route Plan optimization process, make sure the following resources have all the necessary information:
* 1 - The Depots/Sun/Crossdock: Latitude; Longitude; Open Time

<Image title="Jtc1B2KP6M.png" alt={738} border={true} src="https://files.readme.io/db174b8-Jtc1B2KP6M.png">
  Illustration (English)
</Image>

<Image title="2WVsRSXVvw.png" alt={738} border={true} src="https://files.readme.io/9157e4c-2WVsRSXVvw.png">
  Illustration (Vietnamese)
</Image>

* 2 - The Customer: Latitude; Longitude; Open Time; Close Time; Allowed Vehicle Types (The system default Vehicle Types - Motorbike; Truck/Semi-truck, or custom Vehicle Types input by the users); Minimum and Maximum Unloading Time

<Image title="2. Customer Update (ENG).png" alt={1076} border={true} src="https://files.readme.io/18cd21d-2._Customer_Update_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Customer Update (VIE).png" alt={1078} border={true} src="https://files.readme.io/2282275-2._Customer_Update_VIE.png">
  Illustration (Vietnamese)
</Image>

* 3 - The Vehicles: Start Time; Stop Time; Weight; Volume; Speed. You also need to set the Active Status of the Vehicles that you wish to use in the Route Plan optimization process to ***Active***

<Image title="3. Vehicle (ENG).png" alt={897} border={true} src="https://files.readme.io/dc2c472-3._Vehicle_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Vehicle (VIE).png" alt={900} border={true} src="https://files.readme.io/975db08-3._Vehicle_VIE.png">
  Illustration (Vietnamese)
</Image>

## Phase 1: Select Branch And Route Plan date

* Navigate to **Transportation > Vehicles** tab
* Click on the **View Map** icon on the toolbar

<Image title="nRrwJAnA38.png" alt={627} border={true} src="https://files.readme.io/296d296-nRrwJAnA38.png">
  Illustration (English)
</Image>

<Image title="4. Transportation Tab (VIE).png" alt={985} border={true} src="https://files.readme.io/c50d7de-4._Transportation_Tab_VIE.png">
  Illustration (Vietnamese)
</Image>

* You will be directed to the **Map** screen
* On the Map screen, a form will automatically appear. On this form, you have to select the **Branch** and the **Date** to generate the optimized Delivery Routes for the Vehicles

<Image title="2AaulhOKQu.png" alt={1920} border={true} src="https://files.readme.io/0fc34fe-2AaulhOKQu.png">
  Illustration (English)
</Image>

<Image title="5. Map Screen.png" alt={1920} border={true} src="https://files.readme.io/59f4856-5._Map_Screen.png">
  Illustration (Vietnamese)
</Image>

* **Branch:** Click on this field. Select the appropriate Branch from the drop-down list. Alternatively, you could input the Organization Name of the Branch into the search bar, the system will filter out the Branch being searched

<Image title="bCN3Nbo0Mu.png" alt={355} className="border" border={true} src="https://files.readme.io/a2f117d-bCN3Nbo0Mu.png" />

* **Date:** Click on the calendar :fa-calendar-o: icon. A drop-down calendar will appear to let you select the date on which you want to generate the optimized Delivery Routes for the Orders. This date equals the **Order Date** attribute of the Sales Orders. Alternatively, you can directly input the date in the field following the ***mm/dd/yyyy (Month/Date/Year)*** format

<Image title="cloJBKlSBR.png" alt={939} border={true} src="https://files.readme.io/746c17d-cloJBKlSBR.png">
  Illustration (English)
</Image>

<Image title="6. Date (VIE).png" alt={1039} border={true} src="https://files.readme.io/4efef65-6._Date_VIE.png">
  Illustration (Vietnamese)
</Image>

## Phase 2: Generate Optimized Delivery Routes

* After you have chosen the Branch and the Route Plan date, click **Select**
* The **Optimize Route** form will appear. On this form, click **Optimize**

<Image title="7. Optimize Route (ENG) 2.png" alt={442} border={true} src="https://files.readme.io/c80e913-7._Optimize_Route_ENG_2.png">
  Illustration (English)
</Image>

<Image title="7. Optimize Route (VIE) 2.png" alt={449} border={true} src="https://files.readme.io/945fb43-7._Optimize_Route_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* The system will start gathering all the Orders of which the **Order Date** attribute is the same as the Route Plan date that you have selected above, allocate them to the suitable active Vehicles, then display the optimized Delivery Route of the Vehicles on the Timeline panel

<Image title="8. Route Plan (ENG).png" alt={1920} border={true} src="https://files.readme.io/7e91ddd-8._Route_Plan_ENG.png">
  Illustration (English)
</Image>

<Image title="9. Route Plan (VIE).png" alt={1920} border={true} src="https://files.readme.io/a77c0d9-9._Route_Plan_VIE.png">
  Illustration (Vietnamese)
</Image>

* The default routing algorithm that the system utilizes is described in the following section: [**Default Routing Algorithm**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-map-view#default-routing-algorithm)
* To understand how the loading/unloading time (The unloading time is also referred to as the ***Service Time***) is calculated, please refer to the following article: [**Service Time Calculation**]()
* The Route Plan screen holds numerous information and functions. Please refer to the following section to learn more: [**Route Plan Screen Description**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-map-view#section-route-map-screen-description)
* In this phase, you can make necessary adjustments to the optimized Delivery Routes recently generated, such as Change Delivery Shift driver; Change Customer coordinates; Adjust Customer sequence on a Delivery Trip/Delivery Shift, etc. The detailed instructions are presented in the following article: [**Route Plan Adjustment (Map View)**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-adjustment)

## Phase 3: Lock Optimized Delivery Routes And Create Delivery Tasks

* If you see that the optimized Delivery Routes generated by the system have met your expectation, or after you have made appropriate adjustments, you can now lock the Delivery Routes by clicking on the **Lock Route** button
* A confirmation form will appear. Click **OK** to confirm

<Image title="10. Lock Route (ENG).png" alt={1920} border={true} src="https://files.readme.io/a4422d0-10._Lock_Route_ENG.png">
  Illustration Image (English)
</Image>

<Image title="10. Lock Route (VIE).png" alt={1918} border={true} src="https://files.readme.io/2534a9d-10._Lock_Route_VIE.png">
  Illustration Image (Vietnamese)
</Image>

> 📘 By default, the system will lock the Delivery Routes of all vehicles on the Timeline panel at once. If you wish to be able to manually select and lock the Delivery Routes of certain vehicles, please read the following article:

* After you have locked the Delivery Routes, the Delivery Routes color will turn gray on the Timeline panel
* The part of the Delivery Route that is recently locked is defined as a ***Delivery Shift***
* As a Delivery Shift is locked, the delivery tasks will be generated and sent to the Mobile app of the drivers who operate the vehicles. The delivery tasks will also show up in the **Tasks > Tasks** tab
* To track the actual delivery progress of the vehicle in real-time, you can use the Execution Timelines. Please refer to the following article for instruction: [**Delivery Progress Tracking**]()
* To update the result of the delivery tasks, head over to the **Tasks > Tasks** tab. Please refer to the following article for instruction: [**Manage Tasks**]()

<Image title="10. Locked Route (ENG).png" alt={1920} border={true} src="https://files.readme.io/f2f5124-10._Locked_Route_ENG.png">
  Illustration Image (English)
</Image>

<Image title="10. Locked Route (VIE).png" alt={1920} border={true} src="https://files.readme.io/dddc23b-10._Locked_Route_VIE.png">
  Illustration Image (Vietnamese)
</Image>

* In case you want to change certain elements of the recently locked Delivery Shifts (Such as remove or add Orders), you can unlock them
* To unlock the locked Delivery Shifts, click the **Unlock** button at the bottom right of the Timeline panel
* A confirmation dialog will display. Click **OK** to continue
* The system will revert the locked Delivery Shifts to ***Planned*** status

<Image title="11. Unlock Route (ENG).png" alt={1920} border={true} src="https://files.readme.io/e1dab9f-11._Unlock_Route_ENG.png">
  Illustration Image (English)
</Image>

<Image title="11. Unlock Route (VIE).png" alt={1920} border={true} src="https://files.readme.io/b79c0b0-11._Unlock_Route_VIE.png">
  Illustration Image (Vietnamese)
</Image>

## Default Routing Algorithm

* By default, if you don't enable any other additional algorithm configurations, the system will apply the fundamental constraints of the classic Vehicle Routing Problem to the optimized Delivery Routes:
* 1 - One visit per Customer: A Customer will be visited ***only once*** per Delivery Shift. This means that if a Customer places multiple Orders, the system will 1. allocate all of that Customer's Orders to one vehicle instead of several vehicles, and 2. plan the assigned vehicle to deliver all Orders of that Customer in one turn per Delivery Shift instead of several turns
* **Note**: This constraint might lead to a situation where there is no vehicle that has enough weight and/or volume capacity to carry the Orders of a particular Customer in one turn. In this situation, the system will treat that Customer's Orders as [**Unplanned (Missing) Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-unplanned-missing-orders)
* 2 - Closed Route: The Vehicles are planned to travel back to their managing Depots after completing all assigned delivery tasks

## Route Plan Screen Description

* The Route Plan screen is divided into two sections: The Route Map and the Timeline panel

<Image title="41TMeDp7kp.png" alt={1751} border={true} src="https://files.readme.io/2b2054a-41TMeDp7kp.png">
  Illustration Image (English)
</Image>

<Image title="12. Route Description (VIE).png" alt={1920} className="border" border={true} src="https://files.readme.io/b5dc41a-12._Route_Description_VIE.png" />

## Route Map Section

* To zoom in/zoom out the Route Map, move your mouse onto a point on the Route Map, then use the middle scroll button to zoom in/zoom out

<Image title="12. Interactions with Map (ENG).gif" alt={1920} border={true} src="https://files.readme.io/edf9c88-12._Interactions_with_Map_ENG.gif">
  Illustration (English)
</Image>

<Image title="12. Interactions with Map (VIE).gif" alt={1920} border={true} src="https://files.readme.io/0cfb4f7-12._Interactions_with_Map_VIE.gif">
  Illustration (Vietnamese)
</Image>

* To move around the Route Map, left-click on a point on the Route Map, then, with the left button still clicked, drag your mouse around

<Image title="13. Map Moving (ENG).gif" alt={1920} src="https://files.readme.io/795c58d-13._Map_Moving_ENG.gif">
  Illustration (English)
</Image>

<Image title="13. Map Moving (VIE).gif" alt={1920} src="https://files.readme.io/640b817-13._Map_Moving_VIE.gif">
  Illustration (Vietnamese)
</Image>

* To change the color theme of the Route Map, hover your mouse over the color box near the top left corner of the Route Map. The box will then expand and shows three color themes: Default; Light and Dark. Select the appropriate color theme

<Image title="14. Map Color (ENG).gif" alt={1920} src="https://files.readme.io/6e97b8a-14._Map_Color_ENG.gif">
  Illustration (English)
</Image>

<Image title="14. Map COlor (VIE) 2.gif" alt={1920} src="https://files.readme.io/361fe9e-14._Map_COlor_VIE_2.gif">
  Illustration (Vietnamese)
</Image>

* To view the Route Map in fullscreen mode, click on the **Toggle Fullscreen View** button at the bottom right of the Route Map

<Image title="15. Full Screen View (ENG).gif" alt={1920} src="https://files.readme.io/fce6cf8-15._Full_Screen_View_ENG.gif">
  Illustration (English)
</Image>

<Image title="15. Full Screen (VIE).gif" alt={1920} src="https://files.readme.io/e3777ca-15._Full_Screen_VIE.gif">
  Illustration (Vietnamese)
</Image>

* To see the actual photos of a particular road on the Route Map, you can use the **Street View** mode
* To access this mode, click on the Pegman icon :fa-child: above the Toggle Fullscreen View button, then drag it onto a point on the Route Map where you want to view the actual road. There will be a small thumbnail showing the actual photo that was taken at that point. Release the left mouse and you will be navigated to the Street View mode
* In the Street View mode, you can left-click and drag the mouse around to view more angles of the road
* You can also zoom in and zoom out just like in the Route Map
* To exit the Street View mode and return to the Route Map, click on the left arrow icon :fa-arrow-left: on the top left corner of the Street View

<Image title="16. Street View (ENG 2).gif" alt={1920} src="https://files.readme.io/3298806-16._Street_View_ENG_2.gif">
  Illustration (English)
</Image>

<Image title="16. Street View (VIE).gif" alt={1920} border={true} src="https://files.readme.io/7052147-16._Street_View_VIE.gif">
  Illustration (Vietnamese)
</Image>

## Timeline Panel Section

* The Timeline panel section consists of many parts:
* 1 - The Delivery Timelines
* 2 - The Vehicle List
* 3 - The Route Plan command buttons
* 4 - The Plan/Execution Timeline switch button
* 5 - The artboard icons
* 6 - The general Delivery Routes information bar
* 7 -  Missing Orders Indicator

<Image title="18. Panel Description (ENG) 2.png" alt={1708} border={true} src="https://files.readme.io/b6ab86a-18._Panel_Description_ENG_2.png">
  Illustration Image (English)
</Image>

<Image title="18. Panel Description (VIE).png" alt={1707} border={true} src="https://files.readme.io/1e13d4e-18._Panel_Description_VIE.png">
  Illustration Image (Vietnamese)
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

<Image title="19. Delivery Timeline Description 1.png" alt={80} border={true} src="https://files.readme.io/45699f8-19._Delivery_Timeline_Description_1.png">
  Time Block at the end of Delivery Trip
</Image>

* At the beginning of each Delivery Trip, the warehouse time block also has two percentage indicators on the two sides of the warehouse symbol

<Image title="19. Delivery Timeline Description 2.png" alt={128} border={true} src="https://files.readme.io/b6a5200-19._Delivery_Timeline_Description_2.png">
  Time Block at the beginning of Delivery Trip
</Image>

* The percentage indicator to the left of the warehouse symbol is the **Weight Load** indicator. It indicates the percentage of the total product weight over the weight capacity of the vehicle for a Delivery Trip
* For example, in a Delivery Trip, the vehicle is planned to load ***50 kilograms*** of product. Its weight capacity is ***500 kilograms***. The weight load indicator, therefore, will display ***10 percent***
* The percentage indicator to the right of the warehouse symbol is the **Volume Load** indicator. It indicates the percentage of the total product volume over the volume capacity of the vehicle for a Delivery Trip
* For example, in a Delivery Trip, the vehicle is planned to load ***5 cubic meters (5 m3)*** of product. Its volume capacity is ***50 cubic meters (50 m3)***. The volume load indicator, therefore, will display ***10 percent***
* The time periods that the vehicle spends at the Customers' locations to unload/deliver products are represented by the blank time blocks

<Image title="19. Delivery Timeline Description 3.png" alt={52} border={true} src="https://files.readme.io/e38ae36-19._Delivery_Timeline_Description_3.png">
  Symbol of Time Spent at Customer's Location
</Image>

* The thin line that connects the time blocks represents the traveling time of the vehicle

<Image title="19. Delivery Timeline Description 4.png" alt={193} border={true} src="https://files.readme.io/133d4cc-19._Delivery_Timeline_Description_4.png">
  Illustration of Vehicle's Travelling Time
</Image>

* If a Delivery Timeline is too long that it exceeds the screen length, you can click on the horizontal navigation bar near the bottom of the Timeline panel and drag it to the left or to the right to view the remaining part of that Delivery Timeline

<Image title="20. Horizontal Scroll (ENG).gif" alt={1920} border={true} src="https://files.readme.io/c3fd612-20._Horizontal_Scroll_ENG.gif">
  Illustration (English)
</Image>

<Image title="19. Scroll Horizon (VIE).gif" alt={1766} src="https://files.readme.io/ae82f95-19._Scroll_Horizon_VIE.gif">
  Illustration (Vietnamese)
</Image>

* To see the assigned driver of a Delivery Shift, hover over the person icon :fa-user: above the middle of that Delivery Shift's Delivery Timeline

<Image title="21. Driver (ENG).gif" alt={1766} border={true} src="https://files.readme.io/1e8d0d8-21._Driver_ENG.gif">
  Illustration (English)
</Image>

<Image title="21. Driver (VIE).gif" alt={1766} border={true} src="https://files.readme.io/43695d8-21._Driver_VIE.gif">
  Illustration (Vietnamese)
</Image>

* If the Delivery Shift hasn't yet been assigned a driver, the person icon :fa-user: will appear grayed out and has a slash over it

<Image title="21. Driver 2 (ENG).png" alt={1609} border={true} src="https://files.readme.io/a207729-21._Driver_2_ENG.png">
  Illustration (English)
</Image>

<Image title="21. Driver 2 (VIE).png" alt={1616} border={true} src="https://files.readme.io/cb74cee-21._Driver_2_VIE.png">
  Illustration (Vietnamese)
</Image>

* To assign a driver for a not-yet-assigned Delivery Shift, or to change the default driver of a Delivery Shift that has already had a driver, please follow the instruction in the following article: [**Route Plan Adjustment (Map View)**]()
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
        Unit: Kilogram (kg)
      </td>
    </tr>

    <tr>
      <td>
        Total Volume by Product
      </td>

      <td>
        The total volume of all products planned to be loaded onto the vehicle at the warehouse\
        Unit: Cubic metre (m3)
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Fill Rate By Volume (%)
      </td>

      <td>
        The Fill Rate of the vehicle based on the Volume of products loaded onto the vehicle\
        Unit: Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        The volume of each product
      </td>

      <td>
        The volume of each Product or SKU\
        Unit: Cubic metre (m3)
      </td>
    </tr>
  </tbody>
</Table>

* Below are the information fields on the Customer information panel

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
        The MDP code of the customer (If available)\
        Read more about this feature in the following article: [**Familiarity Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-familiarity-constraint)
      </td>
    </tr>

    <tr>
      <td>
        Customer Code
      </td>

      <td>
        The Customer Code of the customer
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
        Driver Name
      </td>

      <td>
        Name of the driver who is assigned to deliver to the customer
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
        Orders
      </td>

      <td>
        List of Order(s) planned to be delivered to the customer
      </td>
    </tr>

    <tr>
      <td>
        Time Window
      </td>

      <td>
        The time window of the order (If available)
      </td>
    </tr>

    <tr>
      <td>
        Familiarity
      </td>

      <td>
        Specify whether the vehicle has Familiarity relationship with the customer or not\
        Read more about this feature at the following article: [**Familiarity Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-familiarity-constraint)
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
        Open/close times
      </td>

      <td>
        The Open time and Close time of the customer
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
        Total Amount to Collect
      </td>

      <td>
        The total price of all orders to be delivered to the customer
      </td>
    </tr>
  </tbody>
</Table>

* On the warehouse information panel, apart from viewing the information, you can also view and export the Packing List, the Picking List, and the Order List. The instruction is described in the following section: [**View And Export Route Plan Documents**]()

<Image title="22. Picking List (ENG).gif" alt={1766} border={true} src="https://files.readme.io/99ad4c7-22._Picking_List_ENG.gif">
  Illustration (English)
</Image>

<Image title="22. Picking List, Packing List (VIE).gif" alt={1766} border={true} src="https://files.readme.io/b39d081-22._Picking_List_Packing_List_VIE.gif">
  Illustration (Vietnamese)
</Image>

* On the Customer information panel, apart from viewing the information, you can also 1. Remove the Customer from the current Route Plan (The instruction is described in the following article: [**Route Plan Adjustment (Map View)**]()), and 2. View and export the Product List of that Customer (The instruction is described in the following section: [**View And Export Route Plan Documents**]())

### Part 2. The Vehicle List

* The vehicle list is located to the left of the Delivery Timelines
* Here, you can view the list of vehicles that the system used for the current Route Plan, along with some other information about the vehicles
* 1 - Vehicle code
* 2 - Vehicle Type. The motorbike icon :fa-motorcycle: represents the Motorbike. The truck icon :fa-truck: icon represents the Truck/Semi-truck
* 3 - Driver name

<Image title="22. Vehicle Panel List.png" alt={1585} border={true} src="https://files.readme.io/0e4450d-22._Vehicle_Panel_List.png">
  Vehicle Panel (English)
</Image>

<Image title="22. Vehicle Panel List (VIE) 2.png" alt={1583} border={true} src="https://files.readme.io/4d30f13-22._Vehicle_Panel_List_VIE_2.png">
  Vehicle Panel (Vietnamese)
</Image>

* To show/hide the optimized Delivery Routes of the Vehicles on the Route Map, click on the corresponding eye icons :fa-eye: of the Vehicles on this list

<Image title="23. View Route Map (Vehicle) (ENG).png" alt={1637} border={true} src="https://files.readme.io/5921ea7-23._View_Route_Map_Vehicle_ENG.png">
  View Route Map of Selected Vehicles (English)
</Image>

<Image title="23. View Route Map (Vehicle) (VIE).png" alt={1583} border={true} src="https://files.readme.io/bb3fe32-23._View_Route_Map_Vehicle_VIE.png">
  View Route Map of Selected Vehicles (Vietnamese)
</Image>

* To view the optimized Delivery Routes of all Vehicles, click on the eye icon :fa-eye: next to the ***Vehicles*** text on the top left corner of the Timeline panel

<Image title="23. View Route Map (All Vehicle) (ENG).png" alt={1637} border={true} src="https://files.readme.io/77eb872-23._View_Route_Map_All_Vehicle_ENG.png">
  View Route Map of all Vehicles (English)
</Image>

<Image title="23. View Route Map (All Vehicle) (VIE).png" alt={1583} border={true} src="https://files.readme.io/f27c322-23._View_Route_Map_All_Vehicle_VIE.png">
  View Route Map of all Vehicles (Vietnamese)
</Image>

* To sort the vehicles by certain parameters (License Plate; Vehicle Type; Weight Capacity; Volume Capacity; Fill Rate by Volume), follow the steps below:
* Step 1: Click on the funnel icon to the right of the ***Vehicle*** text. A drop-down list will appear, showing the list of parameters
* Step 2: On the drop-down list, click the checkbox icons of the parameters by which you want to arrange the vehicles
* Step 3: Select the sorting mode for each parameter by clicking on the arrow icon at the end of each parameter. If you want to sort in ascending mode, leave the up arrow icon :fa-arrow-up:. If you want to sort in descending mode, click on that icon to switch it to the down arrow icon :fa-arrow-down:
* Step 4: Click **Apply**. The system will sort the vehicles by the selected parameters and sorting modes

<Image title="sortvehicle.gif" alt={1920} border={true} src="https://files.readme.io/a160689-sortvehicle.gif">
  Sort Vehicles (English)
</Image>

<Image title="23. Filter Search for Vehicle (VIE).gif" alt={1764} border={true} src="https://files.readme.io/f963f2d-23._Filter_Search_for_Vehicle_VIE.gif">
  Sort Vehicles (Vietnamese)
</Image>

* Here, you can also export some Route Plan documents: The Packing List and the Picking List. The detailed instruction is described in the following section: [**View And Export Route Plan Documents**]()

### Part 3. The Route Plan command buttons

* The set of buttons located at the bottom right of the Timeline Panel is the Route Plan command buttons. These buttons allow you to manipulate the Route Plan

<Image title="24. Command (ENG).png" alt={1920} border={true} src="https://files.readme.io/00bd322-24._Command_ENG.png">
  The Command Buttons (English)
</Image>

<Image title="24. Command (VIE).png" alt={1920} border={true} src="https://files.readme.io/36baf0a-24._Command_VIE.png">
  The Command Buttons (Vietnamese)
</Image>

### Part 4. The Plan/Execution Timeline switch button

* The switch button on the top left corner of the Timeline Panel is the Plan/Execution Timeline switch button
* Clicking on this button will switch between the Plan Delivery Timelines (The Delivery Timelines generated by the system) and the Execution Delivery Timelines (The actual Delivery Timelines when the vehicles begin to perform the delivery tasks)

<Image title="25. Plan and Execution (ENG).png" alt={1682} border={true} src="https://files.readme.io/8671fb2-25._Plan_and_Execution_ENG.png">
  Switch Plan and Execution (English)
</Image>

<Image title="25. Plan and Execution (VIE).png" alt={1685} border={true} src="https://files.readme.io/554836c-25._Plan_and_Execution_VIE.png">
  Switch Plan and Execution (Vietnamese)
</Image>

* The Execution Timeline allows you to track the delivery progress of the vehicles in real-time. Read more in the following article: [**Delivery Progress Tracking**](https://docs.abivin.com/docs/vrp-in-house-fleet-delivery-progress-tracking)

### Part 5. The Artboard icons

* The Artboard icons are located in the top right corner of the Timeline Panel.
* These icons allow you to change the number of the Delivery Timelines that will appear on the Timeline Panel
* The number of lines on each Artboard icon indicates the number of Delivery Timelines that will on the Timeline panel.
* You can click on the ***All*** text to display a maximum of ***six*** Delivery Timelines.
* If the number of Delivery Routes on the Timeline panel is more than six, you can click on an empty point on the Timeline Panel then use the middle scroll button on your mouse to scroll through the Delivery Routes
* To collapse the Timeline panel, click on the down arrow button :fa-arrow-down: to the left of the ***All*** text. After that, you can show the Timeline panel again by clicking on the **Show Timeline** button at the bottom right corner of the Map screen.

<Image title="26. Display Adjustment Board (ENG).png" alt={1680} border={true} src="https://files.readme.io/a868981-26._Display_Adjustment_Board_ENG.png">
  Illustration Image (English)
</Image>

<Image title="26. Display Adjustment Board.png" alt={1683} border={true} src="https://files.readme.io/07df1d0-26._Display_Adjustment_Board.png">
  Illustration Image (Vietnamese)
</Image>

### Part 6. The general Delivery Routes information bar

* At the bottom of the Timeline panel, you can see some general information related to the selected Delivery Route
* The information bar will update as you select more Delivery Routes

<Image title="route info.png" alt={1752} border={true} src="https://files.readme.io/6bfc2fa-route_info.png">
  General Delivery Route Information Bar (English)
</Image>

<Image title="27. General Delivery Board (VIe).png" alt={1681} src="https://files.readme.io/a84c9a9-27._General_Delivery_Board_VIe.png">
  General Delivery Routes Information Bar (Vietnamese)
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
        ORDERS
      </td>

      <td>
        The number of orders planned to be delivered by the selected vehicle
      </td>
    </tr>

    <tr>
      <td>
        DISTANCE
      </td>

      <td>
        The distance planned to be traveled by the selected vehicle
      </td>
    </tr>

    <tr>
      <td>
        COSTS
      </td>

      <td>
        The total estimated operational cost of the selected vehicle's Delivery Route\
        This cost is calculated by the following formula:\
        Total estimated operational cost  = Fixed cost + Cost per km x Distance
      </td>
    </tr>

    <tr>
      <td>
        REVENUES
      </td>

      <td>
        The planned revenues of the selected vehicle on the whole route\
        The revenue is calculated by adding up the total prices of all orders planned to be delivered by the selected vehicle
      </td>
    </tr>

    <tr>
      <td>
        PRODUCTIVITY
      </td>

      <td>
        The difference of the Revenues minus the Costs of the selected vehicle's Delivery Route
      </td>
    </tr>

    <tr>
      <td>
        REVENUES/DISTANCE
      </td>

      <td>
        The average revenue per one kilometer of the selected vehicle's Delivery Route
      </td>
    </tr>

    <tr>
      <td>
        WEIGHT/CAPACITY
      </td>

      <td>
        The total weight of all Orders  on the Delivery Route over the weight capacity of the selected vehicle
      </td>
    </tr>

    <tr>
      <td>
        VOLUME/CAPACITY
      </td>

      <td>
        The total volume of all Orders on the Delivery Route over the weight capacity of the selected vehicle
      </td>
    </tr>

    <tr>
      <td>
        TRUCK/BIKE/TOTAL
      </td>

      <td>
        The number of trucks/semi-trucks, the number of motorbikes, and the sum of all vehicles of these vehicle types that have been selected to perform the orders
      </td>
    </tr>

    <tr>
      <td>
        FAMILIARITY
      </td>

      <td>
        The number of orders that meet the familiarity criteria over the total number of orders delivered by the selected vehicle\
        Read more about this feature at the following article: [**Familiarity Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-familiarity-constraint)
      </td>
    </tr>
  </tbody>
</Table>

## Delivery Journey Units

* In this model, there are three delivery journey units: Delivery Trip, Delivery Shift, Delivery Route

## Delivery Trip

* Delivery Trip is the most fundamental delivery journey unit. It is the delivery journey unit in which the vehicle starts at the managing warehouse, travels to the Customers, and then travels back to the warehouse

<Image title="28. Delivery Trips.png" alt={390} border={true} src="https://files.readme.io/f6950d2-28._Delivery_Trips.png">
  A Typical Delivery Trip
</Image>

## Delivery Shift

* Delivery Shift is the journey unit that the system generates after you perform the Delivery Route locking phase

<Image title="28. Delivery Shift.png" alt={395} src="https://files.readme.io/d608158-28._Delivery_Shift.png">
  A Typical Delivery Shift
</Image>

* A Delivery Shift can consist of just a single Delivery Trip or multiple Delivery Trips
* The first delivery shift of the route will be started at the later of 
* 1. The open time of the Depot where the vehicles have to travel to and load products.
* 2. The starting time of the vehicles assigned.
* For example, an assigned vehicle starts at 2 AM, and the open time of the depot in charge is at 4 AM. Because the depot opens later than the assigned vehicle starts (4 AM is behind 2 AM), the depot's open time will be chosen as the start time of the first delivery shift.
* The following delivery shifts will be started after the delivery shifts right before them are finished and the cut-off time.

<Image title="17. Delivery Shift 4.png" alt={1715} src="https://files.readme.io/ac5968e-17._Delivery_Shift_4.png">
  Illustration (English)
</Image>

<Image title="17. Delivery Shift 4 (VIE).png" alt={1183} src="https://files.readme.io/bed7865-17._Delivery_Shift_4_VIE.png">
  Illustration (Vietnamese)
</Image>

## Delivery Route

* Delivery Route is the final delivery journey unit of a vehicle. It encompasses both the Delivery Trip and Delivery Shift
* A Delivery Route can consist of just a single Delivery Shift or multiple Delivery Shifts 

<Image title="28. Delivery Route 2.png" alt={1070} src="https://files.readme.io/106c0ae-28._Delivery_Route_2.png">
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

<Image title="29. Picking List (ENG).gif" alt={1764} border={true} src="https://files.readme.io/6765982-29._Picking_List_ENG.gif">
  View And Export Route Plan Documents\
  (English)
</Image>

<Image title="29. Picking List (VIE) 2.gif" alt={1764} border={true} src="https://files.readme.io/66cdb9d-29._Picking_List_VIE_2.gif">
  View And Export Route Plan Documents\
  (Vietnamese)
</Image>

* You can also view the Packing List/Picking List of the whole Route Plan by clicking the caret down icon :fa-caret-down: near the **Vehicle** text on the top left corner of the Timeline panel

<Image title="CngzJpU1nl.png" alt={1029} border={true} src="https://files.readme.io/c1968d4-CngzJpU1nl.png">
  Illustration Image (English)
</Image>

<Image title="30. Picking List.png" alt={1658} src="https://files.readme.io/003c2b4-30._Picking_List.png">
  Export Picking List/Packing List (Vietnamese)
</Image>

* To view the Product List of a Customer, click the respective time block of that Customer on the Timeline panel

<Image title="W60DE8wCyE.png" alt={1920} border={true} src="https://files.readme.io/66008f8-W60DE8wCyE.png">
  Illustration Image (English)
</Image>

<Image title="31. Product List.png" alt={1920} src="https://files.readme.io/db25e9b-31._Product_List.png">
  Product List (Vietnamese)
</Image>

* You can export these lists to Excel templates to view offline by clicking on the button **Export** :fa-download: 

<Image title="u62ep4NzaD.png" alt={544} border={true} src="https://files.readme.io/e0beaee-u62ep4NzaD.png">
  Illustration Image (English)
</Image>

<Image title="32. Product List 2.png" alt={793} src="https://files.readme.io/ed092a0-32._Product_List_2.png">
  Export Product List (Vietnamese)
</Image>

## Split Delivery

* There can be situations in which: A customer places multiple Orders, or just one Order, but the total weight and/or volume of the products exceeds the weight and/or volume capacity of each of the active delivery vehicle in the Depot
* This will cause the Orders of that customers to not be optimizable during the Route Optimization process (Defined as **Missing Orders**)

## Manually Split Orders

* If you see that a single Order has its weight and/or volume exceeding the weight and/or volume capacity of each of the active delivery vehicles in the Depot, you can manually split that Order into other smaller Orders that fit better for the delivery vehicles' capacity. Please refer to the following instruction to know the detailed steps: [**Manually split an Order into smaller Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#section-manually-split-an-order-into-smaller-orders)
* For example: 

## Automatically Split Orders

> 🚧 In order for this function to work, you need to enable the configuration **Split Delivery** at the Branch

* If an Order's weight and/or volume exceeds the weight and/or volume capacity of each of the active delivery vehicles in the Depot, then during the route optimization process, the system will try to automatically split that Order to several vehicles, according to the capacity of the vehicles. Vehicles with larger capacity will be selected first
* For example: The Order below, when initially created, is warned as ***Over-capacity***. It weights at ***6 kg***, while the Depot only has two active vehicles, one has the weight capacity to be ***4 kg***, the other has the weight capacity to be ***3 kg***

<Image title="over capa.png" alt={1917} border={true} src="https://files.readme.io/9fc4e6c-over_capa.png">
  Illustration Image (English)
</Image>

<Image title="31. Split Orders (VIE).png" alt={1920} src="https://files.readme.io/ab96bbe-31._Split_Orders_VIE.png">
  Overcapacity Orders
</Image>

* During the Route optimization process, the system will try to split that over capacity Order into smaller orders to fit the capacity of the above vehicles

* In this example, the Original Order has been split into two smaller Split Orders

* Notice that as you navigate to **Orders > Sales Orders** tab, you would see that beside the Original Order, the Split Orders will show up as well

<Image title="31. Split Orders (ENG).png" alt={1920} src="https://files.readme.io/b463e66-31._Split_Orders_ENG.png">
  Split Order (English)
</Image>

<Image title="31. Split Orders (VIE) 2.png" alt={1920} src="https://files.readme.io/9d72219-31._Split_Orders_VIE_2.png">
  Split Order (Vietnamese)
</Image>

* **Important Note**: If you want to edit the Original Order after it has been split during the Route Optimization process, you need to remove the optimized Delivery route. If the optimized Delivery route is still unlocked, you need to click on **Unlock** button one time to remove it. If the optimized Delivery route has been locked, you need to click on **Unlock** button two times to remove it

## Beginner's Guide

### Perform a Route Optimization

* Now that you have completed creating a sales order, the route plan optimization can be initiated after the following steps:
* Step 1: Navigate to **Transportation > Vehicles** tab.
* Step 2: Click on the **Organization** search bar, input the organization (in this case it is a depot/sun) then choose from the drop down menu.

![2880](https://files.readme.io/71c1ad2-Screen_Shot_2021-01-22_at_17.38.58.png "Screen Shot 2021-01-22 at 17.38.58.png")

* Step 3: You will see your order has been planned. Click the **View Map** icon on the toolbar.

![2880](https://files.readme.io/cea557d-Screen_Shot_2021-01-22_at_17.43.04.png "Screen Shot 2021-01-22 at 17.43.04.png")

* Step 4: Now you shall be directed to the **Map** screen. This is where you select the branch and date to generate the optimized Delivery Routes.
* **Branch:** Input the appropriate Branch and choose from the drop down list.
* **Date:** Click on the :fa-calendar-o: icon, then choose the date equal to the **Order Date** attribute of the Sales Order. 
* Next, click **SELECT**.

![2880](https://files.readme.io/2efa612-Screen_Shot_2021-01-22_at_17.46.40.png "Screen Shot 2021-01-22 at 17.46.40.png")

* Step 5: A table will pop up with information of the **Branch** and **Date** you have previously chosen. Click **OPTIMIZE**.

![2880](https://files.readme.io/2b7f1b5-Screen_Shot_2021-01-22_at_17.49.01.png "Screen Shot 2021-01-22 at 17.49.01.png")

* Now you shall see the route plan optimized on the Map screen as follows (you can click the :fa-eye: icon at the bottom left corner of the screen to highlight the route):

![2880](https://files.readme.io/34156ed-Screen_Shot_2021-01-22_at_17.54.58.png "Screen Shot 2021-01-22 at 17.54.58.png")

* There you have it! You have been guided through the simple steps to performing a route plan optimization using Abivin Vroute. Hope you will succeed!
