---
title: Route Plan Optimization
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: link
      title: Transporter Driver
      url: >-
        https://docs.abivin.com/docs/pdp-outsourcing-fleet-transporter-driver-mobile-app
---
## Tasks of the Route Planner

* After you have accepted Orders forwarded from the Order Inspector, you can proceed to the Route Plan Optimization process

### Route Plan Optimization process

* The route optimization process consists of three phases:
* [Phase 1: Gather orders and allocate to vehicles](https://docs.abivin.com/docs/pdp-outsourcing-fleet-route-optimization#section-phase-1-gather-orders-and-allocate-to-vehicles)
* [Phase 2: Generate optimized routes](https://docs.abivin.com/docs/pdp-outsourcing-fleet-route-optimization#section-phase-2-generate-optimized-routes)
* [Phase 3: Lock optimized routes and forward to the Transporter](https://docs.abivin.com/docs/pdp-outsourcing-fleet-route-optimization#section-phase-3-lock-optimized-routes-and-forward-to-the-transporter)

### **Phase 1: Gather orders and allocate to vehicles**

* Log in to your account
* Navigate to **Transportation > Vehicle List** tab
* Click on **View Map** icon on the toolbar

<Image title="2019-10-25 15_24_42-Window.png" alt={1674} className="border" border={true} src="https://files.readme.io/a75f255-2019-10-25_15_24_42-Window.png" />

* You will be navigated to the screen **Map view**. In the middle of this screen, a form will show up. On this form, you need to select the ***Branch*** and ***Date*** to optimize Delivery Routes
* 1 - **Branch:** Click on the **Branch** field. Input the Organization Name of the Branch into the search bar, then select from the drop down menu
* 2 - **Date:** Always select the ***current date*** as displayed on your computer

<Image title="2019-10-25 16_11_19-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/63b2118-2019-10-25_16_11_19-Window.png" />

* Next, click on **Select** button. The system will immediately gather all orders which have the **Date range** attribute to contain the selected date above. Then, the system will perform checking of all transporters to find the appropriate vehicles, then display them on the Timeline panel

* Along with that, the form **Optimization Result** will show up. On this form, you will see the list of routes, along with the cheapest transport service rate of each route that has been automatically selected by the system

* The selected vehicles are the ones that meet the following requirements:

* Their managing transporter provide transport services for the Origin Depots and Destinations Depots of the orders with their Vehicle Type

* Their transport service rates are the cheapest in comparison with other Transporters, or other vehicle types within their managing transporter

* Their cargo areas provide enough space to carry products of the orders being optimized

> ❗️ Make sure you have filled the following information fields for products: **Length; Width; Height**; and the following information fields for vehicles: **Cargo Space Length; Cargo Space Width; Cargo Space Height**

<Image title="2019-10-25 15_26_50-Window.png" alt={1055} border={true} src="https://files.readme.io/58761b6-2019-10-25_15_26_50-Window.png">
  Optimization Result form
</Image>

* You can click on the numerical order of a specific route (Under the **Route** column) to display more information about the transport service cost of that route on **Details** sub tab

<Image title="2019-10-25 15_51_46-Window.png" alt={1075} className="border" border={true} src="https://files.readme.io/c9d2731-2019-10-25_15_51_46-Window.png" />

* If you click on the sub-tab **More results**, you can see a list of other Transporters which also provide Transport Service for the same Delivery Route as the selected Transporter, but were not chosen due to being more expensive

<Image title="2019-10-25 15_52_15-Window.png" alt={1075} className="border" border={true} src="https://files.readme.io/5747540-2019-10-25_15_52_15-Window.png" />

### **Phase 2: Generate optimized routes**

* After the system has gathered the orders and allocated them to the vehicles with the cheapest transport services, you can proceed to generate optimized routes for those orders
* You can choose to optimize routes for a single vehicle or multiple vehicles by clicking on the corresponding :fa-eye: icon of each vehicle. You can also select all vehicles by clicking on the :fa-eye: icon next to the text **Vehicles** 

<Image title="2019-10-26 22_18_42-Window.png" alt={1913} border={true} src="https://files.readme.io/6c66f72-2019-10-26_22_18_42-Window.png">
  Select single route
</Image>

<Image title="2019-10-26 22_19_07-Window.png" alt={1913} border={true} src="https://files.readme.io/714e608-2019-10-26_22_19_07-Window.png">
  Select multiple routes
</Image>

<Image title="2019-10-26 22_19_207-Window.png" alt={1913} border={true} src="https://files.readme.io/5fed260-2019-10-26_22_19_207-Window.png">
  Select all routes
</Image>

* After the vehicles have been selected, click on the **Optimize** button at the bottom right of the Timeline panel
* After a few moments, the optimized routes for the selected vehicles will be generated. The **Planned start time** - The time point when the vehicles are supposed to start their assigned orders will be the result of the comparison between the **Open Time** of the transporter warehouse and the **Start Time** of those vehicles. Whichever time point is later will be selected as the Planned start time of the vehicles
* For example, the transporter garage has the **Open Time** field set at ***06:00***

<Image title="2019-10-26 22_17_27-Window.png" alt={1891} className="border" border={true} src="https://files.readme.io/3418519-2019-10-26_22_17_27-Window.png" />

* While the selected vehicle of the transporter has the **Start Time** field set at ***08:10***

<Image title="2019-10-26 21_48_20-Window.png" alt={794} className="border" border={true} src="https://files.readme.io/dd44a7f-2019-10-26_21_48_20-Window.png" />

* The optimized Planned Start time of the route therefore will be ***08:10***

<Image title="2019-10-26 21_47_27-Window.png" alt={1913} className="border" border={true} src="https://files.readme.io/1e63b32-2019-10-26_21_47_27-Window.png" />

### **Phase 3: Lock optimized routes and forward to the Transporter**

* After you see that the optimized routes have passed your requirements, you can proceed to lock the routes and forward the routes to the chosen Transporter(s)
* Similar to optimizing routes, you can choose to lock routes of a single vehicle, several vehicles or all vehicles by clicking on the corresponding :fa-eye: icon, then click on **Lock Route** button

<Image title="2019-10-26 22_23_44-Window.png" alt={1913} className="border" border={true} src="https://files.readme.io/61a1bd0-2019-10-26_22_23_44-Window.png" />

### (Optional) Re-optimize route when a Transporter declined the forwarded route

* In the scenario a Transporter declines the forwarded route, you will be notified via email. The locked route forwarded to that Transporter will be unlocked. You will have to perform route optimization again (Phase 1 to Phase 3)
* During the route optimization process, the Transporter who declined will be left out of the Transport service optimization process (For that route only)

### Some notes when optimize route

#### Order quantity constraint per Delivery shift

* At the moment, the routing algorithm of this model only allows one vehicle to perform a maximum of ***three orders*** in a Delivery shift. If you try to optimize route for more than three orders, you must have at least two active vehicles, else some orders will be regarded as **Missing orders** - Orders that were failed to be optimized

<Image title="Image 2.png" alt={1750} border={true} src="https://files.readme.io/293e3d1-Image_2.png">
  One active vehicle, four orders. One order is regarded as Missing order
</Image>

<Image title="Image 3.png" alt={1110} border={true} src="https://files.readme.io/545b930-Image_3.png">
  Two active vehicles, four orders. One vehicle will deliver one order; the other vehicle will deliver three orders
</Image>

* If a vehicle is assigned several LTL orders which have the same Origin Depot, then the routing algorithm will arrange the Destination Depot sequence of these Orders based on the distance from the Destination Depots to the Origin Depot. Order of the farthest Destination Depot will be delivered first, while Order of the nearest Destination Depot will be delivered last

<Image title="Image 9.png" alt={1916} className="border" border={true} src="https://files.readme.io/b76e757-Image_9.png" />

<Image title="2019-10-27 15_50_36-Window.png" alt={1915} className="border" border={true} src="https://files.readme.io/52682e8-2019-10-27_15_50_36-Window.png" />

* After that, navigate to **PDP Orders > Current Order** tab to create the next orders for that vehicle (Note that you can't create more than three orders)
* Next, navigate to **Transportation > Vehicle List** tab, and begin optimizing routes for the next orders
* On the **Optimization Result** form, click on **Re-Optimize** button

<Image title="2019-10-27 16_05_13-Window.png" alt={1028} className="border" border={true} src="https://files.readme.io/441b614-2019-10-27_16_05_13-Window.png" />

* You will notice there is a form asking you to choose the **Cut-off Time**. This is a time period (In hours) to specify the time gap between the ***Planned Finish time*** of the first three orders route and the ***Planned Start time*** of the next orders route
* Input the desired value into the field, then click on **Optimize** button

<Image title="2019-10-27 15_56_50-Window.png" alt={393} className="border" border={true} src="https://files.readme.io/dc1a228-2019-10-27_15_56_50-Window.png" />

* The system will take into account the Cut-off Time and calculates the Planned Start time of the next orders route accordingly
* For example, the first three orders have the Planned Finish time to be at ***13:10***. The Cut-off time is ***1 hour***. Therefore, the Planned Start time of the next orders will be ***14:10***

<Image title="2019-10-27 16_00_02-Window.png" alt={1912} className="border" border={true} src="https://files.readme.io/5468072-2019-10-27_16_00_02-Window.png" />

### **Unlock locked routes**

* If for some reasons, the routing plan has some changes, you can still make changes to the routes that have been locked, by using the unlock function
* Select the vehicle of which locked routes will need to be changed
* Click on the **Unlock** button at the bottom of the Timeline panel, next to the **Lock Route** button
* Similar to when you lock routes, you can select one single vehicle, several vehicles or all vehicles. Also, only one order of each vehicle's route could be unlocked each time

<Image title="2019-10-27 19_33_47-Window.png" alt={1916} className="border" border={true} src="https://files.readme.io/289b23f-2019-10-27_19_33_47-Window.png" />

> ❗️ BE CAREFUL WHEN USING THIS FUNCTION!
>
> Even if the drivers have already performed some tasks and submitted on their Mobile app, you can still unlock the routes and thus erase all the submitted tasks of the drivers. Therefore be extra careful when using this function

## Tasks of the Transporter Administrator

* You are the Administrator of the Transporter. After the Route Planner has locked routes, if you are the transporter with the most optimized (cheapest) transport service rates, the locked routes will be forwarded to your account. You will also be notified via email

## Make decision about the forwarded optimized routes

* To make decision about the forwarded optimized routes, please follow the steps below:
* Log in with your account
* Navigate to **Transportation > Vehicle List** tab
* Click on **View Map** icon on the toolbar

<Image title="Selection_006 1.png" alt={1904} className="border" border={true} src="https://files.readme.io/dcd97e5-Selection_006_1.png" />

* You will be navigated to the map screen
* A form will appear, here you will need to select the ***Branch*** for which you perform transport services by clicking on the field below the text **Branch**, input the Organization Name of the Branch into the search bar, then select from the drop down menu
* Next, click on the field below the text **Date**, select the ***current date*** on the drop down calendar
* Then, click on **Select**

<Image title="Selection_007.png" alt={1912} className="border" border={true} src="https://files.readme.io/2b565cd-Selection_007.png" />

* The system will display the locked routes that have been forwarded from the Route Planner to you
* You can select one or more routes by clicking on the corresponding :fa-eye: icons on the row of each route; or select all routes by clicking on :fa-eye: icon next to the text **Vehicle**

<Image title="Selection_005 1.png" alt={1910} border={true} src="https://files.readme.io/21776fb-Selection_005_1.png">
  Select single route
</Image>

<Image title="Selection_005 2.png" alt={1910} border={true} src="https://files.readme.io/e25c224-Selection_005_2.png">
  Select multiple routes
</Image>

<Image title="Selection_005 3.png" alt={1910} border={true} src="https://files.readme.io/93946b9-Selection_005_3.png">
  Select all routes
</Image>

* After you have selected the route, you can decide whether to ***Accept*** a route - Allowing the route tasks to be sent to your driver's Mobile app; or ***Decline*** - Not allowing the route tasks to be sent to your driver's Mobile app, by clicking on the corresponding button at the bottom of the Timeline panel

<Image title="Selection_005 4.png" alt={1910} className="border" border={true} src="https://files.readme.io/b643c81-Selection_005_4.png" />

* As you accept a Delivery Route, the Driver of the assigned vehicle will be able to [**perform his delivery tasks on the Mobile app**](https://docs.abivin.com/docs/pdp-outsourcing-fleet-transporter-driver-mobile-app)

## Reassign vehicle, driver

* In the scenario the vehicle and/or the driver can not perform the assigned route, you can assign the route to other vehicle/driver by following the steps below:
* On the Timeline panel, click on the corresponding user icon :fa-user: (Located on the middle of the Delivery Route) of the vehicle which you want to reassign
* The form **Assign to Driver** will appear

<Image title="Image 12.png" alt={1916} className="border" border={true} src="https://files.readme.io/351ff38-Image_12.png" />

* To reassign another driver to operate a Delivery Route of a vehicle, click on the field below the text **Main Driver**. The drop down list will display the ***Usernames*** of all [***active drivers***](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-users#section-change-active-status-of-drivers) under your management (Only drivers who are not currently assigned other routes will be shown) Select the appropriate driver from that list
* Likewise, you can reassign the route to another vehicle by clicking on the field below the text **Truck License**. The drop down list will display the ***License Plates*** of all [***active vehicles***](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-vehicles#section-change-vehicle-active-status) under your management (Only vehicles which are not currently assigned other routes will be shown). Select the appropriate vehicle from that list
* After you have selected the appropriate driver and/or vehicle, click on **Assign**. Upon doing that, all delivery tasks of the route will be removed from the Mobile app of the former driver, and will be forwarded to the Mobile app of the recently selected driver instead

## Route description

## **Other functions of the Route Planner**

### **Create additional Delivery Shifts for vehicles**

* As has been mentioned above, a vehicle can only perform a maximum of three orders in a Delivery Shift. Therefore, If you want to assign more than three orders to a vehicle, you have to allocate those Orders into separate Delivery Shifts by doing the following
* Create, optimize route and lock route for the first three orders
