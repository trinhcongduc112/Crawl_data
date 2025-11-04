---
title: Delivery Progress Tracking (Clone for RnD - PDP)
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
## Track Delivery Progress by Vehicle

* On the Map screen, aside from the Plan Timeline, you can also access the Execution Timeline once you have optimized and locked the routes
* The Execution Timeline serves as a tracking timeline, where you can view the real-time delivery progress of the vehicles
* To access the Execution Timeline, click on the switch button  :fa-toggle-off: next to the text **Plan** on the Timeline panel

<Image title="1. EXE (VIE).png" alt={1733} border={true} src="https://files.readme.io/b775aba-1._EXE_VIE.png">
  Illustration (English)
</Image>

<Image title="1. EXE (VIE) 3.png" alt={1733} border={true} src="https://files.readme.io/f6e5f4a-1._EXE_VIE_3.png">
  Illustration (Vietnamese)
</Image>

## The Route Map Screen in Execution

### The Route Map Screen

#### Manipulate the Route Map Screen (Execution)

* Manipulations with the Route Map Screen (Execution) are the same as in the Route Map Screen (Plan). Please refer to this article [Manipulate the Route Map Screen](https://docs.abivin.com/docs/route-plan-map-view-vrp-dc#manipulate-the-route-map-screen)

#### The icons on Route Map Screen (Execution)

* The vehicle icon on the Route Map Screen (Execution) is the **Truck** icon

<Image title="2. truck Icon.png" alt={190} className="border" border={true} src="https://files.readme.io/b3caff5-2._truck_Icon.png" />

* The Route Plan line in the Route Map Screen (Execution) will be the line of small route segments tracked by the GPS of the Mobile App. The color of the line will vary directly with the real-time Vehicle's speed, changing from Red to Green. 
* The line of the small route segment will be in Red color when the Vehicle's speed is 0 km/h

![248](https://files.readme.io/9530900-Red_1.png "Red 1.png")

* The line of the small route segment will be in Green color when the Vehicle's speed is greater than or equal to 30 km/h

![245](https://files.readme.io/9b9dfe3-Green_1.png "Green 1.png")

* When you hover the mouse onto the Stop icon on the Route Map Screen, the name of the Stop will show up. On the right corner of the Stop will be the arrow icon, signifying the **Origin Customer** and **Destination Customer**. 
* The Stop with the ascending arrow icon :fa-arrow-up: will be the **Origin Customer**

<Image title="Org (PDP).png" alt={119} className="border" border={true} src="https://files.readme.io/e12c87a-Org_PDP.png" />

* The Stop with the descending arrow icon :fa-arrow-down: will be the **Destination Customer**

<Image title="Des (EXE) (PDP).png" alt={111} className="border" border={true} src="https://files.readme.io/309f573-Des_EXE_PDP.png" />

* In the Execution Timeline, you will see a colored dot on the top left of the Stop icon, which signifies the status of the Orders in the selected Stop
* The color of that icon represents the Delivery status of the order in the selected Stop:
* **Green color**: The Orders of that Delivery Stop were ***Fulfilled***

<Image title="Org (PDP).png" alt={119} className="border" border={true} src="https://files.readme.io/c35b92f-Org_PDP.png" />

* **Orange color**: The Orders of that Delivery Stop were ***Partially Fulfilled***

<Image title="Partially.png" alt={126} className="border" border={true} src="https://files.readme.io/32b57b8-Partially.png" />

* **Red color**: The Orders of that Delivery Stop were ***Unfulfilled***

<Image title="Unfulfilled.png" alt={127} className="border" border={true} src="https://files.readme.io/3b67698-Unfulfilled.png" />

* When you click the icon, you will be directed to the side panel showing [Stop Details in Execution](https://docs.abivin.com/docs/delivery-progress-tracking-vrp-dc-model#view-stop-details-in-execution-delivery-timeline)

### The Timeline Panel (Execution)

* Whereas the Route Map section provides an illustration of the Delivery Routes on the map, the Timeline Panel is where you can view the timeline of each Delivery Route, perform actions such as locking and unlocking, re-optimizing, and make adjustments to the Route Plan

* The Timeline Panel consists of these parts as listed below:

* 1 - Timeline Header

* 2 - Routing Date 

* 3 - Vehicle List

* 4 - Delivery Timeline

* 5 - Delivery Route's general information bar

* 6 - Route Plan command buttons

* Below we will list the features of the Execution Timeline

* 1 - View actual delivery result

* 2 - Replay actual delivery routes

* 3 - View customer information

## View Shift Details in Execution Delivery Timeline

* To view the Shift Details in the Execution Delivery Timeline, please follow these steps
* Step 1: Navigate to the **Vehicle List**, switch to the **Execution** button 
* Step 2: Select the Vehicle you want to see details then click on the Vehicle icon on the right of the list. You can scroll down The Vehicle icon will be highlighted after you click.

<Image title="18. Exe + Shift (ENG).png" alt={1732} border={true} src="https://files.readme.io/27f3c71-18._Exe__Shift_ENG.png">
  Illustration (English)
</Image>

<Image title="18. Exe + Shift (VIE).png" alt={1731} border={true} src="https://files.readme.io/548c477-18._Exe__Shift_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 3: On the form named **Vehicle** on the right side of the screen, scroll down to find **Shifts** then click the Shift Code 

<Image title="14. Shifts (ENG).png" alt={498} border={true} src="https://files.readme.io/fbdf948-14._Shifts_ENG.png">
  Illustration (English)
</Image>

<Image title="14. Shifts (VIE).png" alt={514} border={true} src="https://files.readme.io/3c4e608-14._Shifts_VIE.png">
  Illustration (Vietnamese)
</Image>

* If you view **Shift Details** in the **Execution** Delivery Timeline, the **Shift Details** will show the following information
* The **Depot** icon in the **Execution** Delivery Timeline, whose color corresponds with the color of the Route

<Image title="Depot (EXE).png" alt={155} border={true} src="https://files.readme.io/4848a07-Depot_EXE.png">
  Illustration
</Image>

* The color of the dot on the top right of the **Stop** icon in the **Execution** Delivery Timeline will vary depending on the Delivery Status of Orders submitted by the Drivers via Mobile App.
* **Green color**: The Orders of that Delivery Stop were **Fulfilled**. 

<Image title="Stop 1 (EXE).png" alt={152} border={true} src="https://files.readme.io/c84cb46-Stop_1_EXE.png">
  Illustration
</Image>

* **Orange color**: The Orders of that Delivery Stop were **Partially Fulfilled**

<Image title="Stop  (EXE).png" alt={146} border={true} src="https://files.readme.io/4623b0e-Stop_EXE.png">
  Illustration
</Image>

* **Red color**: The Orders of that Delivery Stop were **Unfulfilled**

<Image title="Stop 3 (EXE).png" alt={260} src="https://files.readme.io/06ef248-Stop_3_EXE.png">
  Illustration
</Image>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field (Shift Details in Execution Delivery Timeline
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
        ATA - ATD (at Depot)
      </td>

      <td>
        The **actual** Depot Check-in (**ATA**) and the **actual** Depot Check-out (**ATD**). This is the time when the Drivers click **Submit** and the system acknowledges successful submission for the Task **Check-In/Check-out** on the Mobile Application.

        The ATA - ATD time will be in the format **MM/DD/YYYY HH:mm - MM/DD/YYYY HH:mm**

        * For example: The actual time of arrival (actual Depot Check-in) at a Depot is **14 May 2021 at 13:00** and the actual time of departure (actual Depot-Check-out) from a Depot is **15 May 2021 at 17:30**, the ATA - ATD will be\
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
        Address (Customer's Location)
      </td>

      <td>
        The address of the Customer's location
      </td>
    </tr>

    <tr>
      <td>
        ATA - ATD (at Customer's Location)
      </td>

      <td>
        The **actual** Customer's Location Check-in (**ATA**) and the **actual** Customer's Location Check-out (**ATD**). This is the time when the Drivers click **Submit** for the Task **Check-In/Check-out** on the Mobile Application.

        The ATA - ATD time will be in the format **MM/DD/YYYY HH:mm - MM/DD/YYYY HH:mm**

        * For example: The actual time of arrival (actual Customer's Location Check-in) at a Depot is **06 May 2021 at 13:00** and the actual time of departure (actual Customer's Location Check-out) from a Depot is **08 May 2021 at 17:30**, the ATA - ATD will be\
          **05/06/2021 13:00 - 05/08/2021 17:30**
      </td>
    </tr>
  </tbody>
</Table>

## View Stop Details in Execution Delivery Timeline

* To view the details about the Delivery Stop, you should follow the steps to view the Shift Details as mentioned above
* After you click the **Shift Code**, the form **Shift Details** will pop up on the right of the screen. The form will have the **Shift Code** as the title and will show details of all Delivery Trips within the selected Shift. You can scroll down to see all Stops of Delivery Shifts.
* On the form **Shift Details**, click the icon of the **Stop** you would like to view details

- A form with the title in the format **Customer\<Customer Code>** will show up on the right corner of the screen

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
        Arrival Time
      </td>

      <td>
        The actual time at which the Drivers checked in at the Customer's Location when the Drivers successfully submit the result of Check-In Task via Mobile App\
        The Arrival Time will be in the format

        * \*HH:mm:ss\*\* (Hour:Minute:Second)

        - For example: If the Driver checked in at Customer's Location at 8:07 AM, the **Arrival Time** will be displayed as follows **8:07:00**
      </td>
    </tr>

    <tr>
      <td>
        Left Time
      </td>

      <td>
        The actual time at which the Drivers checked in at the Customer's Location when the Drivers successfully submit the result of Check-Out Task via Mobile App\
        The Left Time will be in the format

        * \*HH:mm:ss\*\* (Hour:Minute:Second)

        - For example: If the Driver checked out at Customer's Location at 8:15 AM, the **Left Time** will be displayed as follows **8:15:00**
      </td>
    </tr>

    <tr>
      <td>
        Total Amount Collected
      </td>

      <td>
        The actual total amount collected from all Orders in the selected Stop when the drivers submit the Delivery Results via the Mobile App
      </td>
    </tr>

    <tr>
      <td>
        Distance from Stop
      </td>

      <td>
        The distance from the Check-in position to the Customer's Location\
        Unit: Metre (m)
      </td>
    </tr>

    <tr>
      <td>
        Checked-in Position
      </td>

      <td>
        The coordinates of the Checked-in position. The Checked-in Position will be in the format\
        **Latitude, Longitude**
      </td>
    </tr>
  </tbody>
</Table>

* The other fields in the form providing details about the Stop are exactly the same as those in the form in \*Plan\*\* Delivery Timeline. Please click here for more information  can see the d

## View actual delivery result

* You can see the delivery result of each customer by the color of the checkmark icon :fa-check-circle: on the planned timeline horizon

<Image title="12. Actual (EXE).png" alt={496} className="border" border={true} src="https://files.readme.io/2c02919-12._Actual_EXE.png" />

* The color of that icon represents the Delivery status of the order:
* **Green color**: The Orders of that Delivery Stop were ***Successfully Delivered***
* **Orange color**: The Orders of that Delivery Stop were ***Partially Delivered***
* **Black color**: The Orders of that Delivery Stop were ***Not Delivered***

<Image title="Image 1.png" alt={131} className="border" border={true} src="https://files.readme.io/2de2c22-Image_1.png" />

* On the map area above, the border colors of the marker symbols of the Delivery Stops will also be different according to the delivery result:
* **Green color**: The Orders of that Delivery Stop were ***Successfully Delivered***

<Image title="N6YsSp9NqS.png" alt={65} className="border" border={true} src="https://files.readme.io/c9e4359-N6YsSp9NqS.png" />

* **Orange color**: The Orders of that Delivery Stop were ***Partially Delivered***

<Image title="9OAe5jv7nj.png" alt={75} className="border" border={true} src="https://files.readme.io/274884c-9OAe5jv7nj.png" />

* **Red color**: The Orders of that Delivery Stop were ***Not Delivered***

<Image title="K3tdrhKEGc.png" alt={71} className="border" border={true} src="https://files.readme.io/7fbcb82-K3tdrhKEGc.png" />

## View actual delivery time points

* On the Execution Timeline panel, you can see that below the Plan Timeline of each vehicle, there is an additional timeline. That is the **Execution Timeline**

<Image title="KQeMIeMMtR.png" alt={1920} className="border" border={true} src="https://files.readme.io/2a10e7e-KQeMIeMMtR.png" />

* On the Execution Timeline, the time blocks indicate the time period the driver has actually spent at a particular location (Manufacturing warehouse or Customer store/warehouse). They record the time points when the delivery tasks are submitted on Mobile app

<Image title="9TEOG9Vp5e.png" alt={1199} className="border" border={true} src="https://files.readme.io/46a07e7-9TEOG9Vp5e.png" />

* You can use the horizontal scrollbar to scroll the timeline horizon from left to right and vice versa

<Image title="B5mEVUqJCM.png" alt={1920} className="border" border={true} src="https://files.readme.io/396858f-B5mEVUqJCM.png" />

* You can change the width of the Timeline panel by clicking on the **Artboard** icons on the top right side of the Timeline panel. The number of rows on each artboard icon corresponds to the number of vehicle rows shown on the Timeline panel
* Clicking on the **All** text will show (limit is 5 rows), while clicking on the :fa-arrow-down: icon will collapse the panel
* If the Timeline panel doesn't show all timelines of the vehicles, you can click on a blank point on the panel, then use the mouse scroll wheel to scroll the panel up and down

<Image title="jHeNQVclvZ.png" alt={1920} className="border" border={true} src="https://files.readme.io/6a81aa2-jHeNQVclvZ.png" />

## Replay actual delivery routes

* You can view the actual delivery route of a vehicle in real time, or after that vehicle has completed the delivery route, following the steps below
* On the Execution Timeline Panel, click on the :fa-eye: icon of the vehicle which you want to replay the actual delivery route. On the bottom right of the Timeline panel will appear a new set of buttons, serving for playback functions of the actual delivery route
* To view the actual delivery route, click on **Replay** button
* The system will playback the actual delivery route of that vehicle on the map screen
* You can click on **Pause** button to temporarily pause the playback; or **Stop** button to completely stop the playback

<Image title="replay route.gif" alt={1668} className="border" border={true} src="https://files.readme.io/aa7c730-replay_route.gif" />

* As you replay the actual delivery route of the vehicle, you might notice that some parts of the actual delivery route display different colors from the rest. Below is the meaning of each color
* 1 - Red color: 

<Image title="QmlVNWZobo.png" alt={90} className="border" border={true} src="https://files.readme.io/1d7bf00-QmlVNWZobo.png" />

* There are two possibilities
* The first possibility, the Mobile app lost the GPS signal. In this case, the part of the delivery route having this color will look very disorganized (might consist of various slanting straight lines)
* The second possibility, the driver traveled at a slower speed than the speed of the Vehicle. In this case, the part of the delivery route having this color will still look normal
* 2 - Vivid green color: The vehicle traveled approximately at the same speed registered on the system

<Image title="FTSAlrJlLW.png" alt={92} className="border" border={true} src="https://files.readme.io/35e2f78-FTSAlrJlLW.png" />

* 3 - Dark green color: The vehicle traveled relatively faster than the speed registered on the system

<Image title="AM2jq15KoO.png" alt={91} className="border" border={true} src="https://files.readme.io/33d36fd-AM2jq15KoO.png" />

## View customer information

* When you click on the timeline block of a particular customer, on the right side of the map screen will appear a panel showing various information of that customer
* You can view customer information on both Plan and Execution timelines. On Execution timeline, if a customer has been checked in by the vehicle, the panel will also display the check in photo

<Image title="2ldVsnB7JJ.png" alt={1920} border={true} src="https://files.readme.io/6a6a76e-2ldVsnB7JJ.png">
  Check In photo
</Image>

## View route information

* You can view the detailed information of a particular route or several routes by clicking on the corresponding :fa-eye: icon of those routes
* You can also view the detailed information of all routes by clicking on the :fa-eye: icon next to **Vehicle** text
* The detailed information will display on the status bar at the bottom of the Timeline panel

## View and export lists

### Packing List and Order List

* **Packing List** is the detailed list of the products that have been packed at the Depot, including the Product Code; Product Name; Quantity and Weight
* **Order List** is the detailed list of the orders and destination customers
* To view these lists, first click on the timeline block of the Depot. The information panel of that Depot will appear on the right side of the map screen. Scroll down that panel and click on the corresponding text **Packing List** or **Order List**

<Image title="SLbXFLBlcv.png" alt={1920} className="border" border={true} src="https://files.readme.io/1d2980c-SLbXFLBlcv.png" />

* The list will appear. To export click on the **Export** button

<Image title="nCmDVd3r1r.png" alt={1024} border={true} src="https://files.readme.io/149c942-nCmDVd3r1r.png">
  Packing List
</Image>

<Image title="wYRWdhMLkG.png" alt={976} border={true} src="https://files.readme.io/127d549-wYRWdhMLkG.png">
  Order List
</Image>

### Picking List

* **Picking List** is the combination of the **Packing List** and **Order List** mentioned above. This list provides the delivery information of each vehicle, including: License Plate; Order Code; Customer Code; Customer Name; Product Code; Product Name; Quantity of single product items

<Image title="ji958U4km0.png" alt={699} border={true} src="https://files.readme.io/61672bb-ji958U4km0.png">
  Picking List
</Image>

## Filter delivery man (Driver)

* You can view the list of delivery men (Drivers) who have been assigned the delivery tasks, by clicking on **Filter Deliverers** button on the top right of the map screen
* You can filter this list by the Vehicle type (Truck/Semi-truck; Motorbike); by the Depot or the Branch

<Image title="U6C9Vmbefo.png" alt={1920} className="border" border={true} src="https://files.readme.io/382b12e-U6C9Vmbefo.png" />

## Track Delivery Progress by Order Tasks

* Navigate to **Tasks > Task List** tab
* Click on the **Date** field on the toolbar. On the drop down calendar, select the date range in which the order you're finding falls into
* Next, click on **Order Code** column and input the ***Order Code*** of the order you want to check status into the search bar, then click on the corresponding check box :fa-square-o: of the order from the drop down menu

> 👍 You can select multiple order codes on the drop down menu

* The system will filter out all tasks related to that order

<Image title="order tasks.gif" alt={1916} className="border" border={true} src="https://files.readme.io/e92da46-order_tasks.gif" />