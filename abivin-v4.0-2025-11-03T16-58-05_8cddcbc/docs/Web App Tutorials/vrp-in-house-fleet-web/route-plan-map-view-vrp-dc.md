---
title: Route Plan (Map View) (For RnD)
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
* After you have created Sales Orders of all Depots under the management of a Branch, the next step is to perform the Route Plan Optimization process for those Orders
 
## Precondition to Optimize Route Plan

* In order to optimize Route Plan, please make sure the following resources have the necessary information as below:
* 1 - The **Depots/Sun/Crossdock**: Information about **Latitude; Longitude; Open Time**

<Image title="1. Depot-Sun-Crossdock (ENG).png" alt={841} border={true} src="https://files.readme.io/1898bc0-1._Depot-Sun-Crossdock_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Depot-Sun-Crossdock (VIE).png" alt={841} border={true} src="https://files.readme.io/9f584b1-1._Depot-Sun-Crossdock_VIE.png">
  Illustration (Vietnamese)
</Image>

* 2 - The **Customer**: Information about **Latitude; Longitude; Open and Close Time, Allowed Vehicle Types** (The system default Vehicle Types - Motorbike; Truck/Semi-truck, or user-input Vehicle Types); **Minimum and Maximum Unloading Time**

<Image title="2. Customer Update (ENG).png" alt={1076} border={true} src="https://files.readme.io/18cd21d-2._Customer_Update_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Customer Update (VIE).png" alt={1078} border={true} src="https://files.readme.io/2282275-2._Customer_Update_VIE.png">
  Illustration (Vietnamese)
</Image>

* 3 - The **Vehicles**: Information about **Start and Stop Time; Weight and Volume Capacity; Speed**. You also need to set the vehicles you wish to use in the Route Plan in ***Active*** status

<Image title="3. Vehicle (ENG).png" alt={897} border={true} src="https://files.readme.io/dc2c472-3._Vehicle_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Vehicle (VIE).png" alt={900} border={true} src="https://files.readme.io/975db08-3._Vehicle_VIE.png">
  Illustration (Vietnamese)
</Image>

## Switching between Route Plan Map View and Route Plan List View

For more information, please refer to this link t View)]
[block:api-head

## Optimize and Interact with the Route Plan

### Optimize the Route Plan

* Step 1: Navigate to **Planning** tab. You will be directed to the **Map** screen

<Image title="10. Map View (ENG).png" alt={1920} border={true} src="https://files.readme.io/196803c-10._Map_View_ENG.png">
  Illustration (English)
</Image>

<Image title="10. Map View (VIE).png" alt={1920} border={true} src="https://files.readme.io/d2f7435-10._Map_View_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 2: On the form named **Create Route Plan**, click on the field **Organization** to select a **Branch** you want to optimize the Route Plan from the drop-down list. Alternatively, you could enter the Organization Name/Organization Code of the desired Branch into the search bar then select the returned value.

<Image title="1. Branch (ENG).png" alt={1734} border={true} src="https://files.readme.io/d364d1f-1._Branch_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Branch (VIE).png" alt={1734} border={true} src="https://files.readme.io/474cf56-1._Branch_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 3: Click on the calendar :fa-calendar-o: icon. A drop-down calendar will appear to let you select the date on which you want to generate the optimized Route Plan for the Orders. This date should be the **Order Date** in the Sales Orders. Alternatively, you can directly enter the date in the field following the format of ***mm/dd/yyyy (Month/Date/Year)***

<Image title="cloJBKlSBR.png" alt={939} border={true} src="https://files.readme.io/746c17d-cloJBKlSBR.png">
  Illustration (English)
</Image>

<Image title="6. Date (VIE).png" alt={1039} border={true} src="https://files.readme.io/4efef65-6._Date_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 4: Click **Select** to proceed

<Image title="2. Select (ENG).png" alt={1732} border={true} src="https://files.readme.io/a442d98-2._Select_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Select (VIE).png" alt={1730} border={true} src="https://files.readme.io/873b16e-2._Select_VIE.png">
  Illustration (Vietnamese)
</Image>

* After that, a form named **Confirmation** will appear. On this form, click **Confirm**

<Image title="3. Confirm (ENG).png" alt={1733} border={true} src="https://files.readme.io/3f3dcbf-3._Confirm_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Confirm (VIE).png" alt={1729} border={true} src="https://files.readme.io/abb7323-3._Confirm_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 5: The system will gather all Orders with the same **Order Date** as the date you have selected above, allocate them to the suitable active Vehicles, and present the optimized Route Plan for the Vehicles on the Timeline Panel.
* The optimized Route Plan line will be in the dashed line. When there is more than one Route Plan, each Route will have its own distinct color as in the photo below. 

<Image title="17. Route Plan (ENG).png" alt={1920} border={true} src="https://files.readme.io/1128567-17._Route_Plan_ENG.png">
  Illustration (English)
</Image>

<Image title="17. Route Plan (VIE).png" alt={1920} border={true} src="https://files.readme.io/af84d41-17._Route_Plan_VIE.png">
  Illustration (Vietnamese)
</Image>

* In this phase, you can make necessary adjustments to the optimized Delivery Routes recently generated, such as Change Delivery Shift driver; Change Customer coordinates; Adjust Customer sequence on a Delivery Trip/Delivery Shift, etc. The detailed instructions are presented in the following article: [**Route Plan Adjustment (Map View)**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-adjustment)

### Manipulate the Optimized Route Plan

#### Lock the Optimized Route Plan

* If you see that the Route Plan optimized by the system has met your expectation, or after you have made appropriate adjustments to the Route Plan and now agreed with it, you can now lock the Delivery Routes by clicking on the **Lock Route** button
* A confirmation form will appear. Click **OK** to confirm

<Image title="17. Lock Route (ENG).png" alt={1920} border={true} src="https://files.readme.io/62a8f7a-17._Lock_Route_ENG.png">
  Illustration (English)
</Image>

<Image title="17. Lock Route (VIE).png" alt={1920} border={true} src="https://files.readme.io/6e726d4-17._Lock_Route_VIE.png">
  Illustration (Vietnamese)
</Image>

* Please refer to this article for more information on the feature [**Lock Delivery Routes and Shifts**](https://docs.abivin.com/docs/route-plan-adjustment-map-view-mapview-rnd#lock-delivery-routes-and-shifts)

> 📘 By default, the system will lock the Delivery Routes of all vehicles on the Timeline panel at once. If you wish to be able to manually select and lock the Delivery Routes of certain vehicles, please read the following article:

* After you have locked the Route Plan, the Route Plan color will turn gray on the Timeline Panel
* The part of the Route Plan that is recently locked is defined as a ***Delivery Shift***
* As a Delivery Shift is locked, the delivery tasks will be generated and sent to the Mobile app of the drivers who operate the vehicles. The delivery tasks will also show up in the **Tasks > Tasks** tab
* To track the actual delivery progress of the vehicle in real-time, you can use the Execution Timelines. Please refer to the following article for instruction: [**Delivery Progress Tracking**](https://docs.abivin.com/docs/delivery-progress-tracking-vrp-dc-model)
* To update the result of the delivery tasks, head over to the **Tasks > Tasks** tab. Please refer to the following article for instruction: [**Manage Tasks**]()

<Image title="2. Locked Route (ENG).png" alt={1732} border={true} src="https://files.readme.io/d46ee9a-2._Locked_Route_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Locked Route (VIE).png" alt={1731} border={true} src="https://files.readme.io/7568536-2._Locked_Route_VIE.png">
  Illustration (Vietnamese)
</Image>

#### Unlock the Route Plan

* In case you want to change certain elements of the recently locked Delivery Shifts (Such as remove or add Orders), you can unlock them
* To unlock the locked Delivery Shifts, click the **Unlock** button at the bottom right of the Timeline panel
* A confirmation dialog will display. Click **OK** to continue
* The system will revert the locked Delivery Shifts to ***Planned*** status

<Image title="2. Unlock Route (ENG).png" alt={1730} border={true} src="https://files.readme.io/e3e7477-2._Unlock_Route_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Unlock Route (VIE).png" alt={1730} border={true} src="https://files.readme.io/978f6de-2._Unlock_Route_VIE.png">
  Illustration (Vietnamese)
</Image>

* In this phase, you can make necessary adjustments to the optimized Delivery Routes recently generated, such as Change Delivery Shift driver; Change Customer coordinates; Adjust Customer sequence on a Delivery Trip/Delivery Shift, etc. The detailed instructions are presented in the following article: [**Route Plan Adjustment (Map View)**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-adjustment)
* Please refer to this article for more information on the feature [**Unlock Delivery Routes and Shifts**](https://docs.abivin.com/docs/route-plan-adjustment-map-view-mapview-rnd#unlock-locked-delivery-shifts)

## The Route Plan Screen

* The Route Plan screen is divided into two sections: 
* 1 - The Route Map 
* 2 - The Timeline Panel

<Image title="4. Route Plan Screen (ENG).png" alt={1731} src="https://files.readme.io/a3475aa-4._Route_Plan_Screen_ENG.png">
  Illustration (English)
</Image>

<Image title="4. Route Plan Screen (VIE).png" alt={1733} border={true} src="https://files.readme.io/47390d1-4._Route_Plan_Screen_VIE.png">
  Illustration (Vietnamese)
</Image>

### The Route Map Screen

#### Manipulate the Route Map Screen

* In the top left corner of the Route Map section, you can see the row containing the information about the Branch and Date of the route plan. To reselect that information, click on that row and choose a new **Branch** or **Date** from the pop-up window

<Image title="17. Branch (ENG).gif" alt={1920} border={true} src="https://files.readme.io/7e2b917-17._Branch_ENG.gif">
  Illustration (English)
</Image>

<Image title="17. Branch (VIE).gif" alt={1920} className="border" border={true} src="https://files.readme.io/32db047-17._Branch_VIE.gif" />

* You can easily switch from the current Map View to List View by clicking on the **List View** button (:fa-list-ul: icon) right beside the **Branch - Date** row. Make sure to turn on the **Show Route List View** configuration to use this feature. It is located in the Manufacturer's settings (MORE CONFIGURATIONS > Route)
* For more information, please refer to Route Plan (List View) article
* To zoom in/zoom out the Route Map, move your mouse onto a point on the Route Map, then use the middle scroll button to zoom in/zoom out

<Image title="19. Zoom (ENG).gif" alt={1920} border={true} src="https://files.readme.io/e1e09bf-19._Zoom_ENG.gif">
  Illustration (English)
</Image>

<Image title="19. Zoom (VIE).gif" alt={1920} border={true} src="https://files.readme.io/50825e8-19._Zoom_VIE.gif">
  Illustration (Vietnamese)
</Image>

* To move around the Route Map, left-click on a point on the Route Map, hold your mouse, and then move it to the desired direction

<Image title="18. Zoom (ENG).gif" alt={1920} border={true} src="https://files.readme.io/9f7cef8-18._Zoom_ENG.gif">
  Illustration (English)
</Image>

<Image title="18. Map Moving (VIE).gif" alt={1920} src="https://files.readme.io/18d6f24-18._Map_Moving_VIE.gif">
  Illustration (Vietnamese)
</Image>

* To change the color theme of the Route Map, hover your mouse over the color box near the top left corner of the Route Map. The box will then expand and show three color themes: Default, Light, and Dark. Click on the one you wish to change the theme to

<Image title="20. Color (ENG).gif" alt={1920} border={true} src="https://files.readme.io/278d31d-20._Color_ENG.gif">
  Illustration (English)
</Image>

<Image title="20. Color (VIE).gif" alt={1920} border={true} src="https://files.readme.io/3cf1332-20._Color_VIE.gif">
  Illustration (Vietnamese)
</Image>

* To view the Route Map in fullscreen mode, click on the **Enter Fullscreen View** button at the top left corner of the Route Map, beyond the **Default Theme** button

<Image title="18. Full Screen (ENG).png" alt={1436} border={true} src="https://files.readme.io/3b9fea2-18._Full_Screen_ENG.png">
  Illustration (English)
</Image>

<Image title="18. Full Screen (VIE).png" alt={1357} border={true} src="https://files.readme.io/c07e52c-18._Full_Screen_VIE.png">
  Illustration (Vietnamese)
</Image>

* To see the actual photos of a particular road on the Route Map, you can use the **Street View** mode
* To access this mode, click on the Pegman icon :fa-child: above the Toggle Fullscreen View button, then drag it onto a point on the Route Map where you want to view the actual road. There will be a small thumbnail showing the actual photo that was taken at that point. Release the left mouse and you will be navigated to the Street View mode
* In the Street View mode, you can left-click and drag the mouse around to view more angles of the road
* You can also zoom in and zoom out just like in the Route Map
* To exit the Street View mode and return to the Route Map, click on the left arrow icon :fa-arrow-left: on the top left corner of the Street View

<Image title="1. Street View (ENG).gif" alt={1728} border={true} src="https://files.readme.io/42a848f-1._Street_View_ENG.gif">
  Illustration (English)
</Image>

<Image title="1. Street View (VIE).gif" alt={1728} border={true} src="https://files.readme.io/11d2229-1._Street_View_VIE.gif">
  Illustration (Vietnamese)
</Image>

### The Timeline Panel

* Whereas the Route Map section provides an illustration of the Delivery Routes on the map, the Timeline Panel is where you can view the timeline of each Delivery Route, perform actions such as locking and unlocking, re-optimizing, and make adjustments to the Route Plan
* The Timeline Panel consists of these parts as listed below:
* 1 - Timeline Header
* 2 - Routing Date 
* 3 - Vehicle List
* 4 - Delivery Timeline
* 5 - Delivery Route's general information bar
* 6 - Route Plan command buttons

<Image title="4. Timeline Panel (ENG).png" alt={1732} border={true} src="https://files.readme.io/33320d9-4._Timeline_Panel_ENG.png">
  Illustration (English)
</Image>

<Image title="4. Timeline Panel (VIE).png" alt={1729} border={true} src="https://files.readme.io/68ebe64-4._Timeline_Panel_VIE.png">
  Illustration (Vietnamese)
</Image>

* Below is the detailed information of each part:

#### 1. The Timeline Header

* In the Timeline Header, you could do the following things
* [Switch between **Plan** Delivery Timeline and **Execution** Delivery Timeline](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#switching-between-route-plan-map-view-and-route-plan-list-view)
* [Expand/Collapse/Hide/Display the Delivery Timeline as well as adjust the number of the Delivery Trips displayed on the Delivery Timeline](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#expandcollapsehidedisplay-and-adjust-the-number-of-the-delivery-routes-displayed-on-the-delivery-timeline)
* [Display and check the reasons for Unplanned Orders](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#display-and-check-the-reasons-for-unplanned-orders)
* [Set up Road Constraints](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#set-up-road-constraints)
* [Manage the Filter based on Vehicle Code, Planning Status, and Sync Status](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#manage-filters)

##### **Plan/Execution Timeline Switch**

* On the left of the Timeline Header, you can see two buttons named **PLAN** and **EXECUTION**
* The Plan Timeline is set as default when you enter the Map View screen. It shows the Timeline of the Delivery Routes planned by the system based on the Route Optimization result

<Image title="5. Plan (ENG).png" alt={1731} border={true} src="https://files.readme.io/219a390-5._Plan_ENG.png">
  Illustration (English)
</Image>

<Image title="5. Plan (VIE).png" alt={1729} border={true} src="https://files.readme.io/120dd96-5._Plan_VIE.png">
  Illustration (Vietnamese)
</Image>

* Clicking on the **EXECUTION** button will turn the **Plan** Timeline to the **Execution** Timeline. Here, the actual timeline of the Delivery Routes executed by the drivers is displayed. The data is gathered directly from the real-time execution of the delivery tasks submitted by the drivers via their Mobile App

<Image title="5. Execution (ENG).png" alt={1730} border={true} src="https://files.readme.io/a3a5968-5._Execution_ENG.png">
  Illustration (English)
</Image>

<Image title="5. Execution (VIE).png" alt={1731} border={true} src="https://files.readme.io/2025d8e-5._Execution_VIE.png">
  Illustration (Vietnamese)
</Image>

##### Expand/Collapse/Hide/Display and Adjust the number of the Delivery Routes displayed on the Delivery Timeline

* On the right corner of the Timeline Header, there are two buttons named **EXPAND** and **COLLAPSE**
* The Delivery Timeline is set to default to displaying a certain number of Delivery Routes. If there are more Delivery Routes than those being displayed, click the **EXPAND** button to expand the Timeline Panel to a greater height, showing more Delivery Routes

<Image title="6. Expand (ENG).png" alt={1730} border={true} src="https://files.readme.io/61ce62d-6._Expand_ENG.png">
  Illustration (English)
</Image>

<Image title="6. Expand (VIE).png" alt={1731} border={true} src="https://files.readme.io/195dd7f-6._Expand_VIE.png">
  Illustration (Vietnamese)
</Image>

* On the other hand, clicking the **COLLAPSE** button will hide the whole Timeline Panel. To show the Timeline, click the button **SHOW TIMELINE**

<Image title="17. Show Timeline (ENG).gif" alt={1594} border={true} src="https://files.readme.io/c4e61c9-17._Show_Timeline_ENG.gif">
  Illustration (English)
</Image>

* To adjust the number of Delivery Routes displayed on the Delivery Timeline, on the top right corner of the Timeline Header, you could click the downward angle icon :fa-angle-down: to decrease the number of Delivery Routes or click the upward angle icon :fa-angle-up: to increase the number of Delivery Routes displayed on the Timeline.
* To see all the Routes, please scroll down until you find the Routes you want to see.

<Image title="7. Increase (ENG).png" alt={1730} border={true} src="https://files.readme.io/a0110d9-7._Increase_ENG.png">
  Illustration (English)
</Image>

<Image title="7. Increase (VIE).png" alt={1731} border={true} src="https://files.readme.io/9fa3c4c-7._Increase_VIE.png">
  Illustration (Vietnamese)
</Image>

##### Display and check the reasons for Unplanned Orders

##### Set up Road Constraints

##### Manage Filters

#### 2. Routing Date

* Below the Timeline Header lies the Routing Date bar. This bar shows the dates it will take for the Delivery Routes to be delivered
* This information is based on the Route Optimization result and follows the MM/DD/YYYY (Month/Date/Year) format

<Image title="2. Routing Date (ENG).png" alt={1729} border={true} src="https://files.readme.io/c6b09e3-2._Routing_Date_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Routing Date (VIE).png" alt={1731} border={true} src="https://files.readme.io/ad47ba3-2._Routing_Date_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 3. Vehicle List

* The vehicle list is located on the left of the Timeline Panel Section, below the Routing Date bar

<Image title="12. Vehicle List (ENG).png" alt={1267} border={true} src="https://files.readme.io/dca33d5-12._Vehicle_List_ENG.png">
  Illustration (English)
</Image>

<Image title="12. Vehicle List (VIE).png" alt={1268} border={true} src="https://files.readme.io/57e7c6d-12._Vehicle_List_VIE.png">
  Illustration (Vietnamese)
</Image>

* In the Vehicle List, you can do the following things:
* [View the list of Vehicle used in the Route Plan](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#view-the-list-of-vehicle-used-in-the-route-plan)
* [Sort Vehicles based on certain criteria (License Plate, Vehicle Type, Vehicle Fill Rate...)](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#sort-vehicles-based-on-certain-criteria)
* [Export Route Plan documents (Picking List/Packing List)](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#export-route-plan-documents-picking-listpacking-list)
* [Search Order Code/Store Code](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#search-order-codestore-code)
* View [Shift Details](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#view-shift-details) and [Stop Details](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#view-stop-details) and [Depot Details](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#view-depot-details)

##### View the list of Vehicle used in the Route Plan

* On the Vehicle List, you can view the list of vehicles used for the current Route Plan, along with their key information
* 1 - **Driver Name**: Name of the Driver taking charge of the Vehicle in use
* 2 - **License Plate**: The License Plate Number of the Vehicle in use
* 3 - **Username**: The Username of the Driver using Mobile App
* 4 - **Vehicle Type**: The Motorbike icon :fa-motorcycle: represents the Vehicle in use is Motorbike. The Truck icon :fa-truck: icon represents the Vehicle in use is Truck/Semi-truck

<Image title="8. Vehicle List (ENG).png" alt={392} border={true} src="https://files.readme.io/892220b-8._Vehicle_List_ENG.png">
  Illustration (English)
</Image>

<Image title="8. Vehicle List (VIE).png" alt={383} border={true} src="https://files.readme.io/f783db4-8._Vehicle_List_VIE.png">
  Illustration (Vietnamese)
</Image>

* In the Vehicle List, when you click the Vehicle icon (either :fa-truck: or :fa-motorcycle:), the Vehicle icon will then be highlighted and there will be a Vehicle Details Sidebar showing up in the right corner of the screen. This Sidebar will show the information of the selected Vehicle.

<Image title="13. Vehicle Details (ENG).png" alt={1731} border={true} src="https://files.readme.io/2f884c9-13._Vehicle_Details_ENG.png">
  Illustration (English)
</Image>

<Image title="13. Vehicle Details (VIE) 2.png" alt={1730} border={true} src="https://files.readme.io/ab228aa-13._Vehicle_Details_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* Here is the information fields of Vehicle displayed in the sidebar 

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Field Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Vehicle Type
      </td>

      <td>
        The Vehicle Type of the selected Vehicle\
        (Example: Truck, Semi-truck...)
      </td>
    </tr>

    <tr>
      <td>
        License Plate
      </td>

      <td>
        The License Plate Number of the selected Vehicle
      </td>
    </tr>

    <tr>
      <td>
        Assigned
      </td>

      <td>
        This field shows the name of the driver taking charge of the selected Vehicle.

        * If the selected Vehicle has been assigned to a specific driver, this field will show the Full Name of the Driver

        - If the selected Vehicle has not been assigned to any driver, this field will show the value **N/A**
      </td>
    </tr>

    <tr>
      <td>
        Temp. Config
      </td>

      <td>
        The Temperature Levels supported by the selected Vehicle\
        The Temperature Levels supported by the Vehicle can be **Ambient**, **Chilled**, **Frozen**.\
        Please refer to this article for detailed information  [Cold Chain](doc:vrp-in-house-fleet-cold-chain)
      </td>
    </tr>

    <tr>
      <td>
        Temp. Zone
      </td>

      <td>
        The number of Temperature Zones of the selected Vehicles

        * Example: If the selected Vehicle supports products with **Ambient** and **Chilled**, the number of the Temp. Zone is **2**, hence in the field **Temp. Zone**, the value **2** will be displayed
      </td>
    </tr>

    <tr>
      <td>
        Position
      </td>

      <td>
        The Position of the selected Vehicle
      </td>
    </tr>

    <tr>
      <td>
        Speed
      </td>

      <td>
        The Speed of the selected Vehicle
      </td>
    </tr>

    <tr>
      <td>
        Start Time
      </td>

      <td>
        The working start time of the selected vehicle.\
        The working start time will be in the format **HH:mm** **(Hour:Minute)** (24 hours)

        * Example: The working start time of the selected Vehicle is at 17:30, in the field **Start Time**, the value **17:30** will be displayed
      </td>
    </tr>

    <tr>
      <td>
        Stop Time
      </td>

      <td>
        The working stop time of the selected vehicle.\
        The working stop time will be in the format **HH:mm** **(Hour:Minute)** (24 hours)

        * Example: The working stop time of the selected Vehicle is at 22:30, in the field **Start Time**, the value **22:30** will be displayed
      </td>
    </tr>

    <tr>
      <td>
        Shifts
      </td>

      <td>
        This field displays the Shift Code of the Shifts delivered by the selected Vehicle.
      </td>
    </tr>
  </tbody>
</Table>

##### View Shift Details and Stop Details

###### View Shift Details

* To view the Shift Details, please follow these steps
* Step 1: Navigate to the **Vehicle List**, select the Vehicle you want to see details then click on the Vehicle icon on the right of the list. You can scroll down The Vehicle icon will be highlighted after you click.

<Image title="13. Vehicle Details (ENG).png" alt={1731} border={true} src="https://files.readme.io/063e27b-13._Vehicle_Details_ENG.png">
  Illustration (English)
</Image>

<Image title="13. Vehicle Details (VIE) 2.png" alt={1730} border={true} src="https://files.readme.io/d9ec21d-13._Vehicle_Details_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* Step 2: On the form named **Vehicle** on the right side of the screen, scroll down to find **Shifts** then click the Shift Code 

<Image title="14. Shifts (ENG) 2.png" alt={516} border={true} src="https://files.readme.io/668beba-14._Shifts_ENG_2.png">
  Illustration (English)
</Image>

<Image title="14. Shifts (VIE).png" alt={514} border={true} src="https://files.readme.io/b050619-14._Shifts_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 3: After you click the **Shift Code**, the form **Shift Details** will pop up on the right of the screen. The form will have the **Shift Code** as the title and will show details of all Delivery Trips within the selected Shift. You can scroll down to see all Trips, Stops, and Depots of the Delivery Shifts. There will be two scenarios
* **Scenario 1**: You view **Shift Details** in the **Plan** Delivery Timeline
* **Scenario 2**: You view **Shift Details** in the **Execution** Delivery Timeline

###### **Scenario 1**: If you view **Shift Details** in the **Plan** Delivery Timeline

* In this case, the **Shift Details** will show the following information

<Image title="18. Shift Details (ENG).png" alt={1730} border={true} src="https://files.readme.io/7dcac75-18._Shift_Details_ENG.png">
  Illustration (English)
</Image>

<Image title="18. Plan + Shift (VIE).png" alt={1731} border={true} src="https://files.readme.io/f261c6d-18._Plan__Shift_VIE.png">
  Illustration (Vietnamese)
</Image>

* The **Depot** icon in the **Planned** Delivery Timeline, whose color corresponds with the color of the Route

<Image title="Depot.png" alt={167} src="https://files.readme.io/3c48364-Depot.png">
  Illustration
</Image>

* The **Stop** icon in the **Planned** Delivery Timeline, whose color corresponds with the color of the Route. The **Stop** will be numbered throughout the Route

<Image title="Stop.png" alt={145} src="https://files.readme.io/db5ddeb-Stop.png">
  Illustration
</Image>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field (Shift Details in Plan Delivery Timeline
      </th>

      <th>
        Field Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Trip Code
      </td>

      <td>
        The management code of the Trip automatically generated by the system

        The Trip Code will be in the format\
        **TRIP-YYMMDD-XXXX#x**
      </td>
    </tr>

    <tr>
      <td>
        Depot Name
      </td>

      <td>
        The name of the Depot, from which the drivers check-in and load products
      </td>
    </tr>

    <tr>
      <td>
        Depot Address
      </td>

      <td>
        The address of the Depot, from which the drivers check-in
      </td>
    </tr>

    <tr>
      <td>
        ETA - ETD at Depot
      </td>

      <td>
        The planned Depot Check-in (**ETA**) and the planned Depot Check-out (**ETD**)\
        The ETA - ETD time will be in the format **MM/DD/YYYY HH:mm - MM/DD/YYYY HH:mm**\
        (**Month/Date/Year Hour:minute - Month/Date/Year Hour:minute**)

        * Example: The estimated time of arrival at a Depot is **14 May 2021 at 13:00** and the estimated time of departure from a Depot is **15 May 2021 at 17:30**, the ETA - ETD will be\
          **05/14/2021 13:00 - 05/15/2021 17:30**
      </td>
    </tr>

    <tr>
      <td>
        Customer Name
      </td>

      <td>
        The name of the customer who receives the orders
      </td>
    </tr>

    <tr>
      <td>
        Address (of Customer's Location)
      </td>

      <td>
        The address of the Customer's location
      </td>
    </tr>

    <tr>
      <td>
        ETA - ETD (at Customer's Location)
      </td>

      <td>
        The planned Customer's Location Check-in (**ETA**) and the planned Customer's Location Check-out (**ETD**)\
        The ETA - ETD time will be in the format **MM/DD/YYYY HH:mm - MM/DD/YYYY HH:mm**\
        (**Month/Date/Year Hour:minute - Month/Date/Year Hour:minute**)

        * Example: The estimated time of arrival at a Customer's location is **06 May 2021 at 13:00** and the estimated time of departure from a Customer's location is **07 May 2021 at 17:30**, the ETA - ETD will be\
          **05/06/2021 13:00 - 05/07/2021 17:30**
      </td>
    </tr>
  </tbody>
</Table>

###### **Scenario 2**: If you view **Shift Details** in the **Execution** Delivery Timeline

* In this case, it means that you are viewing the Delivery Progress in the Actual Timeline. Please refer to this link for detailed information [View Shift Details in Execution Delivery Timeline](https://docs.abivin.com/docs/delivery-progress-tracking-clone-for-rnd#view-shift-details-in-execution-delivery-timeline)

###### View Stop Details

* To view the details about the Delivery Stop, you should follow the steps to view the Shift Details as mentioned above
* After you click the **Shift Code**, the form **Shift Details** will pop up on the right of the screen. The form will have the **Shift Code** as the title and will show details of all Delivery Trips within the selected Shift. You can scroll down to see all Stops of Delivery Shifts.
* There will be two scenarios
* **Scenario 1**: You view **Stop Details** in the **Plan** Delivery Timeline
* **Scenario 2**: You view **Stop Details** in the **Execution** Delivery Timeline

###### **Scenario 1**: If you view **Stop Details** in the **Plan** Delivery Timeline,

* On the form **Shift Details**, click the icon of the **Stop** you would like to view details

<Image title="20. Stop (ENG).png" alt={514} border={true} src="https://files.readme.io/eef9900-20._Stop_ENG.png">
  Illustration (English)
</Image>

<Image title="20. Stop (VIE).png" alt={514} border={true} src="https://files.readme.io/ce31321-20._Stop_VIE.png">
  Illustration (Vietnamese)
</Image>

* A form with the title in the format **Customer\<Customer Code>** will show up on the right corner of the screen

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Field Name
      </th>

      <th>
        Field Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Customer Code
      </td>

      <td>
        The management code of the selected Customer
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Code
      </td>

      <td>
        The management code of the Vehicle that delivered orders in the selected Stop
      </td>
    </tr>

    <tr>
      <td>
        Address
      </td>

      <td>
        The address of the Customer's Location
      </td>
    </tr>

    <tr>
      <td>
        MDP
      </td>

      <td>
        The MDP code of the customer (If available)\
        Read more about this feature at the following article: [**Familiarity Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-familiarity-constraint)
      </td>
    </tr>

    <tr>
      <td>
        Customer Time Window
      </td>

      <td>
        The Time Window of the Customer's Location
      </td>
    </tr>

    <tr>
      <td>
        Open & Close
      </td>

      <td>
        The Open Time and Close Time of the Customer's Location\
        The Open Time and Close Time are in the format 

        * **HH:mm - HH:mm\*** (24 hours)\
          (\*\*Hour:minute - Hour:minute)

        Example: If a Customer's Location opens at 7:30AM and closes at 08:30PM, the field **Open & Close** would be displayed as follows

        ***07:30 - 20:30***
      </td>
    </tr>

    <tr>
      <td>
        Allow Vehicle Type
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Cluster
      </td>

      <td>
        The Customer Group Code
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Type
      </td>

      <td>
        The Type of the selected Vehicle
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
        ETA - ETD (at Customer's Location)
      </td>

      <td>
        The planned Customer's Location Check-in (ETA) and the planned Customer's Location Check-out (ETD)\
        The ETA - ETD time will be in the format **MM/DD/YYYY HH:mm - MM/DD/YYYY HH:mm**\
        ((**Month/Date/Year Hour:minute - Month/Date/Year Hour:minute**)

        * Example: The estimated time of arrival at a Customer's location is **06 May 2021 at 13:00** and the estimated time of departure from a Customer's location is **07 May 2021 at 17:30**, the ETA - ETD will be\
          **05/06/2021 13:00 - 05/07/2021 17:30**
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
        Driver Name
      </td>

      <td>
        Name of the driver who is in charge of delivering orders to the Customer
      </td>
    </tr>

    <tr>
      <td>
        Orders
      </td>

      <td>
        The management code of the Orders in the selected Stop
      </td>
    </tr>

    <tr>
      <td>
        Product Categories
      </td>

      <td>
        The categories of Products delivered to the selected Stop
      </td>
    </tr>

    <tr>
      <td>
        Orders Time Window
      </td>

      <td>
        Delivery Time Window of Orders (if available)
      </td>
    </tr>

    <tr>
      <td>
        Total Product Weight
      </td>

      <td>
        The total weight of all products in the selected Stop\
        Unit: Kg (kilogram)
      </td>
    </tr>

    <tr>
      <td>
        Total Product Volume
      </td>

      <td>
        The total volume of all products in the selected Stop\
        Unit: Cubic meter (m3)
      </td>
    </tr>

    <tr>
      <td>
        Fill Rate Weight
      </td>

      <td>
        The Vehicle Fill Rate by Vehicle Weight\
        Unit: Percentage (%)

        * Formula\
          Fill Rate Weight = ext step is to perform the Route Plan Optimization process for those Orders
          ## Precondition to Optimiz / The Weight capacity of the Vehicle) x 100
      </td>
    </tr>

    <tr>
      <td>
        Fill Rate Volume
      </td>

      <td>
        The Vehicle Fill Rate by Vehicle Volume\
        Unit: Percentage (%)

        * Formula\
          Fill Rate Volume = next step is to perform the Route Plan Optimization process for those Orders
            ## Precondition to Optimi / The Volume capacity of the Vehicle) x 100
      </td>
    </tr>

    <tr>
      <td>
        Total Amount
      </td>

      <td>
        Total amount to collect as planned

        * Formula\
          Total amount to collect (Planned) = Total Order Price of the selected Stop - Total Promotion and Discount of the selected Stop
      </td>
    </tr>
  </tbody>
</Table>

###### **Scenario 2**: If you view **Stop Details** in the **Execution** Delivery Timeline

* In this case, it means that you are viewing the Delivery Progress in the Actual Timeline. Please refer to this link for detailed information [View Stop Details in Execution Delivery Timeline](https://docs.abivin.com/docs/delivery-progress-tracking-clone-for-rnd#view-shift-details-in-execution-delivery-timeline)

###### View Depot Details

* On the map, the icon for **Depot** is in the form as in the photo below. The color of the **Depot** may vary depending on the color of each route plan. When you hover the mouse onto the Depot icon, the name of the Depot will show up

<Image title="16. Depot (Icon) 2.png" alt={56} border={true} src="https://files.readme.io/ef3418b-16._Depot_Icon_2.png">
  Illustration
</Image>

* On the map, the icon for **Sun** is in the form as in the photo below. The color of the **Sun** may vary depending on the color of each route plan. When you hover the mouse onto the Sun icon, the name of the Sun will show up

<Image title="16. SUN (Icon) (VRP).png" alt={56} border={true} src="https://files.readme.io/ef32c58-16._SUN_Icon_VRP.png">
  Illustration
</Image>

* On the map, the icon for **Crossdock (xDock)** is in the form as in the photo below. The color of the **xDock** may vary depending on the color of each route plan. When you hover the mouse onto the xDock icon, the name of the xDock will show up

<Image title="16. xDock (Icon) (VRP).png" alt={68} border={true} src="https://files.readme.io/ffa8c75-16._xDock_Icon_VRP.png">
  Illustration
</Image>

* Here is the list of information in the form **Depot Details**

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Field Name
      </th>

      <th>
        Field Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organization Code
      </td>

      <td>
        The management code of the selected Depot
      </td>
    </tr>

    <tr>
      <td>
        Organization Name
      </td>

      <td>
        The Name of the selected Depot
      </td>
    </tr>

    <tr>
      <td>
        Address
      </td>

      <td>
        The address of the selected Depot
      </td>
    </tr>

    <tr>
      <td>
        ETA - ETD
      </td>

      <td>
        Estimated Time of Arrival (ETA): The estimated time when the driver arrives at the store 

        Estimated Time of Departure (ETD): The estimated time when the driver leaves the store

        Format: MM/DD/YYYY HH:mm - MM/DD/YYYY HH:mm

        * Example: The estimated time of arrival at a Customer's location is **06 May 2021 at 13:00** and the estimated time of departure from a Customer's location is **07 May 2021 at 17:30**, the ETA - ETD will be\
          **05/06/2021 13:00 - 05/07/2021 17:30**
      </td>
    </tr>

    <tr>
      <td>
        Total Weight
      </td>

      <td>
        The total weight of all Orders in the selected Trip\
        Unit of measure: Kg (kilogram)
      </td>
    </tr>

    <tr>
      <td>
        Total Volume
      </td>

      <td>
        The total volume of all Orders in the selected Trip\
        Unit of measure: m3 (cubic meter)
      </td>
    </tr>

    <tr>
      <td>
        Fill Rate Weight
      </td>

      <td>
        The Fill Rate based on Weight of the selected Trip\
        Unit of measure: % (percent)

        Fill Rate Weight of Trip = (Total Weight of Orders in the selected Trip / Maximum Weight Capacity of the Vehicle) x 100
      </td>
    </tr>

    <tr>
      <td>
        Fill Rate Volume
      </td>

      <td>
        The Fill Rate based on Volume of the selected Trip\
        Unit of measure: % (percent)

        Fill Rate Volume of Trip = (Total Volume of Orders in the selected Trip / Maximum Volume Capacity of the Vehicle) x 100
      </td>
    </tr>

    <tr>
      <td>
        Temperature
      </td>

      <td>
        The Volume percentage based on the Products' Temperature Level against the capacity against the Vehicle Capacity in the selected Trip.

        Temperature = (Total Volume of Products in each Temperature Level / Total Volume of the selected Trip) x 100

        This information is displayed when you enable the configuration **Use Cold Chain**. Please refer to this article for more information\
        [Cold Chain](doc:vrp-in-house-fleet-cold-chain)
      </td>
    </tr>
  </tbody>
</Table>

##### Export Route Plan documents (Picking List/Packing List)

* Here, you can also export some Route Plan documents: The Packing List and the Picking List. The detailed instruction is described in the following section: [**View And Export Route Plan Documents**]()

##### Sort Vehicles based on certain criteria

* To sort the vehicles by certain criteria (License Plate; Vehicle Type; Vehicle Weight; Vehicle Volume; Fill Rate by Volume), follow the steps below:
* Step 1: Click on the funnel icon to the right of the ***Vehicle*** text. A drop-down list will appear, showing the list of criteria

<Image title="9. Sort - Merge (ENG).png" alt={384} border={true} src="https://files.readme.io/91ae912-9._Sort_-_Merge_ENG.png">
  Illustration (English)
</Image>

<Image title="9. Sort - Merge (VIE).png" alt={408} border={true} src="https://files.readme.io/1be440e-9._Sort_-_Merge_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 2: On the drop-down list, click the checkbox icons of the parameters by which you want to arrange the vehicles. You can select multiple checkboxes. In this case, the ones chosen prior to the next will be prioritized

<Image title="11. Tick (ENG).png" alt={326} border={true} src="https://files.readme.io/f9f1128-11._Tick_ENG.png">
  Illustration (English)
</Image>

<Image title="11. Tick (VIE).png" alt={333} border={true} src="https://files.readme.io/e919b6e-11._Tick_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 3: Select the sorting mode for each parameter by clicking on the arrow icon at the end of each parameter. If you want to sort in ascending mode, leave the up arrow icon :fa-arrow-up:. 

<Image title="9. Filter (ENG).png" alt={327} border={true} src="https://files.readme.io/41a17f4-9._Filter_ENG.png">
  Illustration (English)
</Image>

<Image title="9. Filter (VIE).png" alt={408} border={true} src="https://files.readme.io/60396c2-9._Filter_VIE.png">
  Illustration (Vietnamese)
</Image>

* If you want to sort in descending mode, click on that icon to switch it to the down arrow icon :fa-arrow-down:

<Image title="10. Desc (ENG).png" alt={326} border={true} src="https://files.readme.io/9e5a481-10._Desc_ENG.png">
  Illustration (English)
</Image>

<Image title="10. Desc 2 (VIE).png" alt={333} border={true} src="https://files.readme.io/74935a1-10._Desc_2_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 4: Click **Apply**. The system will sort the vehicles by the selected parameters and sorting modes
* **Note**: If you log out of the Web App, the sort order will be reset to default

<Image title="12. Apply (ENG).png" alt={326} border={true} src="https://files.readme.io/8fe6d0c-12._Apply_ENG.png">
  Illustration (English)
</Image>

<Image title="12. Apply (VIE).png" alt={333} border={true} src="https://files.readme.io/5a07035-12._Apply_VIE.png">
  Illustration (Vietnamese)
</Image>

##### Search Order Code/Store Code

##### Export Route Plan documents (Picking List/Packing List)

* Here, you can also export some Route Plan documents: The Packing List and the Picking List. The detailed instruction is described in the following section: [**View And Export Route Plan Documents**]()

#### 4. The Delivery Timeline

* On the Delivery Timeline, you could do the following things

* View Depot Details

* View Customer Details

* View the Planned Delivery Timeline and Actual Delivery Timeline

* Assign Drivers for Shifts, View Shifts, and Remove Shifts from Route Plan

* This part takes up the most space in the Timeline Panel Section since it demonstrates the entire timeline of each generated Route Plan

* A Delivery Timeline will visually present the following time periods: 

* 1 - The time period to load products at the managing warehouses at the beginning of the Delivery Route. This time period is defined as the ***Loading Time***

* 2 - The time period to travel

* 3 - The time period to deliver products at the Customers' locations. This time period is defined as the ***Unloading Time*** or ***Service Time***

* 4 - The time period to handover collected payment and perform paperwork at the managing warehouses at the end of the Delivery Route

* 5 - The Cut-off time - the time period between two adjacent Delivery Shifts of a vehicle, if the Delivery Route consists of more than one Delivery Shift. During this time period, the vehicle will have no activity

<Image title="19. Time Panel Description.png" alt={1702} border={true} src="https://files.readme.io/1bde307-19._Time_Panel_Description.png">
  Illustration (English)
</Image>

* On a Delivery Timeline, the time periods that the vehicle spends at its managing warehouse at the beginning of a Delivery Trip are represented by the time blocks that have the warehouse symbol inside
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
        Read more about this feature at the following article: [**Familiarity Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-familiarity-constraint)
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

#### 5. The Route Plan command buttons

* The set of buttons located at the bottom right of the Timeline Panel are the Route Plan command buttons. These buttons allow you to manipulate the Route Plan

<Image title="24. Command (ENG).png" alt={1920} border={true} src="https://files.readme.io/00bd322-24._Command_ENG.png">
  The Command Buttons (English)
</Image>

<Image title="24. Command (VIE).png" alt={1920} border={true} src="https://files.readme.io/36baf0a-24._Command_VIE.png">
  The Command Buttons (Vietnamese)
</Image>

#### 6. The Plan/Execution Timeline switch button

<Image title="25. Plan and Execution (ENG).png" alt={1682} border={true} src="https://files.readme.io/8671fb2-25._Plan_and_Execution_ENG.png">
  Switch Plan and Execution (English)
</Image>

<Image title="25. Plan and Execution (VIE).png" alt={1685} border={true} src="https://files.readme.io/554836c-25._Plan_and_Execution_VIE.png">
  Switch Plan and Execution (Vietnamese)
</Image>

* The Execution Timeline allows you to track the delivery progress of the vehicles in real-time. Read more in the following article: [**Delivery Progress Tracking**](https://docs.abivin.com/docs/vrp-in-house-fleet-delivery-progress-tracking)

#### 7. The Artboard icons

* The Artboard icons located on the top right corner of the Timeline Panel
* These icons allow you to change the number of the Delivery Timelines that will appear on the Timeline Panel
* The number of lines on each Artboard icon indicates the number of Delivery Timelines that will on the Timeline panel
* You can click on the ***All*** text to display a maximum of ***six*** Delivery Timelines
* If the number of Delivery Routes on the Timeline panel is more than six, you can click on an empty point on the Timeline Panel then use the middle scroll button on your mouse to scroll through the Delivery Routes
* To collapse the Timeline panel, click on the down arrow button :fa-arrow-down: to the left of the ***All*** text. After that, you can show the Timeline panel again by clicking on the **Show Timeline** button at the bottom right corner of the Map screen

<Image title="26. Display Adjustment Board (ENG).png" alt={1680} border={true} src="https://files.readme.io/a868981-26._Display_Adjustment_Board_ENG.png">
  Illustration Image (English)
</Image>

<Image title="26. Display Adjustment Board.png" alt={1683} border={true} src="https://files.readme.io/07df1d0-26._Display_Adjustment_Board.png">
  Illustration Image (Vietnamese)
</Image>

#### 8. The general Delivery Routes information bar

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
        The distance planned to be travelled by the selected vehicle
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
        The average revenue per one kilometre of the selected vehicle's Delivery Route
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

## Route Plan Underlying Mechanism Explanations

#### Default Routing Algorithm

* By default, if you don't enable any other additional algorithm configurations, the system will apply the fundamental constraints of the classic Vehicle Routing Problem to the optimized Delivery Routes:
* 1 - One visit per Customer: A Customer will be visited ***only once*** per Delivery Shift. This means that if a Customer places multiple Orders, the system will 1. allocate all of that Customer's Orders to one vehicle instead of several vehicles, and 2. plan the assigned vehicle to deliver all Orders of that Customer in one turns per Delivery Shift instead of several turns
* **Note**: This constraint might lead to a situation where there is no vehicle that has enough weight and/or volume capacity to carry the Orders of a particular Customer in one turn. In this situation, the system will treat that Customer's Orders as [**Unplanned (Missing) Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-unplanned-missing-orders)
* 2 - Closed Route: The Vehicles are planned to travel back to their managing Depots after completing all assigned delivery tasks

#### Loading/Unloading Time

* To understand how the Loading/Unloading Time (The Unloading Time is also referred to as the ***Service Time***) is calculated, please refer to the following article: [**Service Time Calculation**]()

#### Delivery Journey Units

* In this model, there are three Delivery Journey Units, which are Delivery Trip, Delivery Shift, and Delivery Route

##### Delivery Trip

* Delivery Trip is the most fundamental delivery journey unit. It is the delivery journey unit in which the vehicle starts at the managing warehouse, travels to the Customers, and then travels back to the warehouse

<Image title="28. Delivery Trips.png" alt={390} border={true} src="https://files.readme.io/f6950d2-28._Delivery_Trips.png">
  A Typical Delivery Trip
</Image>

##### Delivery Shift

* Delivery Shift is the journey unit that the system generates after you perform the Delivery Route locking phase

<Image title="28. Delivery Shift.png" alt={395} border={true} src="https://files.readme.io/d608158-28._Delivery_Shift.png">
  A Typical Delivery Shift
</Image>

* A Delivery Shift can consist of just a single Delivery Trip or multiple Delivery Trips
* The first delivery shift of the route will be started at the later of 
* 1. The open time of the Depot where the vehicles have to travel to and load products.
* 2. The starting time of the vehicles assigned.
* For example, an assigned vehicle starts at 2 AM, and the open time of the depot in charge is at 4 AM. Because the depot opens later than the assigned vehicle starts (4 AM is behind 2 AM), the depot's open time will be chosen as the start time of the first delivery shift.
* The following delivery shifts will be started after the delivery shifts right before them are finished and the cut-off time.

<Image title="17. Delivery Shift 4.png" alt={1715} border={true} src="https://files.readme.io/ac5968e-17._Delivery_Shift_4.png">
  Illustration (English)
</Image>

<Image title="17. Delivery Shift 4 (VIE).png" alt={1183} border={true} src="https://files.readme.io/bed7865-17._Delivery_Shift_4_VIE.png">
  Illustration (Vietnamese)
</Image>

##### Delivery Route

* Delivery Route is the final delivery journey unit of a vehicle. It encompasses both the Delivery Trip and Delivery Shift
* A Delivery Route can consist of just a single Delivery Shift or multiple Delivery Shifts 

<Image title="28. Delivery Route 2.png" alt={1070} border={true} src="https://files.readme.io/106c0ae-28._Delivery_Route_2.png">
  A Typical Delivery Route with 2 Delivery Shifts
</Image>

## View And Export Route Plan Documents

#### Order Details

*
* On the Route Plan screen, you can view and export the Route Plan documents: Packing List; Picking List; Order List; Product List

#### Packing List

* The Packing List details the Order detail for each separate Customer on a Delivery Trip

#### Picking List

* The Picking List lays out what products have been taken out of the Depot shelves for a Delivery Trip

#### Order List

* The Order List specifies the Orders on a Delivery Trip

#### Product List

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

<Image title="30. Picking List.png" alt={1658} border={true} src="https://files.readme.io/003c2b4-30._Picking_List.png">
  Export Picking List/Packing List (Vietnamese)
</Image>

* To view the Product List of a Customer, click the respective time block of that Customer on the Timeline panel

<Image title="W60DE8wCyE.png" alt={1920} border={true} src="https://files.readme.io/66008f8-W60DE8wCyE.png">
  Illustration Image (English)
</Image>

<Image title="31. Product List.png" alt={1920} border={true} src="https://files.readme.io/db25e9b-31._Product_List.png">
  Product List (Vietnamese)
</Image>

* You can export these lists to Excel templates to view offline by clicking on the button **Export** :fa-download: 

<Image title="u62ep4NzaD.png" alt={544} border={true} src="https://files.readme.io/e0beaee-u62ep4NzaD.png">
  Illustration Image (English)
</Image>

<Image title="32. Product List 2.png" alt={793} border={true} src="https://files.readme.io/ed092a0-32._Product_List_2.png">
  Export Product List (Vietnamese)
</Image>

## Split Delivery

* There can be situations in which: A customer places multiple Orders, or just one Order, but the total weight and/or volume of the products exceeds the weight and/or volume capacity of each of the active delivery vehicle in the Depot
* This will cause the Orders of that customers to not be optimizable during the Route Optimization process (Defined as **Missing Orders**)

#### Manually Split Orders

* If you see that a single Order has its weight and/or volume exceeding the weight and/or volume capacity of each of the active delivery vehicles in the Depot, you can manually split that Order into other smaller Orders that fit better for the delivery vehicles' capacity. Please refer to the following instruction to know the detailed steps: [**Manually split an Order into smaller Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#section-manually-split-an-order-into-smaller-orders)
* For example: 

#### Automatically Split Orders

> 🚧 In order for this function to work, you need to enable the configuration **Split Delivery** at the Branch

* If an Order's weight and/or volume exceeds the weight and/or volume capacity of each of the active delivery vehicles in the Depot, then during the route optimization process, the system will try to automatically split that Order to several vehicles, according to the capacity of the vehicles. Vehicles with larger capacity will be selected first
* For example: The Order below, when initially created, is warned as ***Over-capacity***. It weights at ***6 kg***, while the Depot only has two active vehicles, one has the weight capacity to be ***4 kg***, the other has the weight capacity to be ***3 kg***

<Image title="over capa.png" alt={1917} border={true} src="https://files.readme.io/9fc4e6c-over_capa.png">
  Illustration Image (English)
</Image>

<Image title="31. Split Orders (VIE).png" alt={1920} border={true} src="https://files.readme.io/ab96bbe-31._Split_Orders_VIE.png">
  Overcapacity Orders
</Image>

* During the Route optimization process, the system will try to split that over capacity Order into smaller orders to fit the capacity of the above vehicles

* In this example, the Original Order has been split into two smaller Split Orders

* Notice that as you navigate to **Orders > Sales Orders** tab, you would see that beside the Original Order, the Split Orders will show up as well

<Image title="31. Split Orders (ENG).png" alt={1920} border={true} src="https://files.readme.io/b463e66-31._Split_Orders_ENG.png">
  Split Order (English)
</Image>

<Image title="31. Split Orders (VIE) 2.png" alt={1920} border={true} src="https://files.readme.io/9d72219-31._Split_Orders_VIE_2.png">
  Split Order (Vietnamese)
</Image>

* **Important Note**: If you want to edit the Original Order after it has been split during the Route Optimization process, you need to remove the optimized Delivery route. If the optimized Delivery route is still unlocked, you need to click on **Unlock** button one time to remove it. If the optimized Delivery route has been locked, you need to click on **Unlock** button two times to remove it

## Beginner's Guide

### Perform a Route Optimization

* Now that you have completed creating a sales order, the route plan optimization can be initiated after the following steps:
* Step 1: Navigate to **Transportation > Vehicles** tab.
* Step 2: Click on the **Organization** search bar, input the organization (in this case it is a depot/sun) then choose from the drop down menu.

<Image title="Screen Shot 2021-01-22 at 17.38.58.png" alt={2880} className="border" border={true} src="https://files.readme.io/71c1ad2-Screen_Shot_2021-01-22_at_17.38.58.png" />

* Step 3: You will see your order has been planned. Click the **View Map** icon on the toolbar.

<Image title="Screen Shot 2021-01-22 at 17.43.04.png" alt={2880} className="border" border={true} src="https://files.readme.io/cea557d-Screen_Shot_2021-01-22_at_17.43.04.png" />

* Step 4: Now you shall be directed to the **Map** screen. This is where you select the branch and date to generate the optimized Delivery Routes.
* **Branch:** Input the appropriate Branch and choose from the drop down list.
* **Date:** Click on the :fa-calendar-o: icon, then choose the date equal to the **Order Date** attribute of the Sales Order. 
* Next, click **SELECT**.

<Image title="Screen Shot 2021-01-22 at 17.46.40.png" alt={2880} className="border" border={true} src="https://files.readme.io/2efa612-Screen_Shot_2021-01-22_at_17.46.40.png" />

* Step 5: A table will pop up with information of the **Branch** and **Date** you have previously chosen. Click **OPTIMIZE**.

<Image title="Screen Shot 2021-01-22 at 17.49.01.png" alt={2880} className="border" border={true} src="https://files.readme.io/2b7f1b5-Screen_Shot_2021-01-22_at_17.49.01.png" />

* Now you shall see the route plan optimized on the Map screen as follows (you can click the :fa-eye: icon at the bottom left corner of the screen to highlight the route):

<Image title="Screen Shot 2021-01-22 at 17.54.58.png" alt={2880} className="border" border={true} src="https://files.readme.io/34156ed-Screen_Shot_2021-01-22_at_17.54.58.png" />

* There you have it! You have been guided through the simple steps to performing a route plan optimization using Abivin Vroute. Hope you will succeed!