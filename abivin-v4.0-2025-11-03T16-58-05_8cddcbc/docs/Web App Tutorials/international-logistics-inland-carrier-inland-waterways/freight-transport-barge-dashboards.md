---
title: Dashboards
excerpt: This article is being edited
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
## Locate Dashboard Tab

* You are the dispatcher. On Web app, you can view the shipment status in a visual way through **Dashboard** function
* Navigate to **Reports > Dashboard** tab
* Click on the field  **Select Dashboard Type**, there are two dashboards types to choose
* [1. Barge Plan](https://docs.abivin.com/docs/freight-transport-barge-dashboards#barge-plan-dashboard)
* [2. Gathering Plan](https://docs.abivin.com/docs/freight-transport-barge-dashboards#gathering-plan-dashboard)

<Image title="2019-11-06 12_33_04-Window.png" alt={1891} className="border" border={true} src="https://files.readme.io/fd94d81-2019-11-06_12_33_04-Window.png" />

## Barge Plan Dashboard

* The dashboard **Barge Plan** is designed to track the loading/unloading status of the barges at specific locations and timeframes, for shipments which have the **Order Type** attribute to be either ***Internal*** or ***External***

### Barge Plan dashboard interface

* The Barge Plan dashboard interface consists of three sections
* [Section 1: Barge Plan dashboard toolbar](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-section-1-barge-plan-dashboard-toolbar)
* [Section 2: Barge Plan dashboard charts](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-section-2-barge-plan-dashboard-charts)
* [Section 3: Barge Plan dashboard barge information table](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-section-3-barge-plan-dashboard-barge-information-table) 

#### Section 1: Barge Plan dashboard toolbar

* The toolbar has three information fields: ***Date Range; Select Location*** and ***Select Barge***. Through these fields, the dispatcher can filter information and view the dashboard as intended
* In addition, there are two buttons: ***Refresh*** - Refresh the page to update the most current status; and ***Download*** - Export an Excel template with the current filters

<Image title="2019-11-06 12_36_47-Window.png" alt={1734} className="border" border={true} src="https://files.readme.io/b89d8d8-2019-11-06_12_36_47-Window.png" />

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
        Date Range
      </td>

      <td>
        Select the creation dates of the Shipments (The dates on which the Shipments were created on Abivin Web app or forwarded from the External Transportation Management System)
      </td>
    </tr>

    <tr>
      <td>
        Select Location
      </td>

      <td>
        Select the Shipment Stops on where the containers were picked up (Pick Stops) or dropped off (Drop Stops)
      </td>
    </tr>

    <tr>
      <td>
        Select Barge
      </td>

      <td>
        Select the barges of which assigned Shipments contain the selected locations
      </td>
    </tr>
  </tbody>
</Table>

#### Section 2: Barge Plan dashboard charts

* The screen is split into two sides. On the right side are **Load** charts. These charts shows the container units ***planned to be picked up*** of all Dummy Shipments at the selected Pick Stops. On the left side is **Unload** charts. These charts shows the container units ***planned to be dropped off*** of all Actual Shipments (Or Dummy Shipments that have not been linked with its corresponding Internal Actual Shipments) at the selected Drop Stops
* Both the Load and Unload charts are made up of two chart types: **Bar chart** and **Donut chart**. The Bar chart shows the quantity of each container type (20 feet Dry Full, 40 feet Dry Full, 45 feet Dry Full, 20 feet Refrigerated Full, 40 feet Refrigerated Full, 20 feet Empty, 40 feet Empty, 45 feet Empty). The Donut chart also shows the quantity of each container type but in [***Twenty-foot equivalent units (TEUs)***](https://en.wikipedia.org/wiki/Twenty-foot_equivalent_unit) instead (Each 40 feet/45 feet container unit will be converted into two 20 feet container units)

#### Section 3: Barge Plan dashboard barge information table

* Below the charts is the barge information table. This table tracks the status of the barges of which assigned Shipments contain the selected Stops
* The table is presented in a block-type view. Each block represents a selected Stop. Within the block of a Stop, the table will display the list of barges of which assigned Shipments contain that Stop. Information of each barge is displayed on a separate row
* Below are the display mechanism for each shipment event of a barge within a particular Stop

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Shipment Event
      </th>

      <th>
        Display Mechanism
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Newly created Shipment
        (Dummy; Internal Actual; External Actual; NFR Shipments)
      </td>

      <td>
        Displays the assigned barge at every Stops of the Shipment with the barge status: ***PLAN\_EXISTS***\
        Note:\
        If the barge currently has an ongoing Shipment and a pending Shipment that have the same Stop, then only the ongoing Shipment will be displayed\
        The barge will still be displayed at the Drop Stops if the Shipment is a Dummy Shipment
      </td>
    </tr>

    <tr>
      <td>
        Submission of the event "Shipment started"\
        (Dummy; External Actual; NFR Shipments)
      </td>

      <td>
        Displays the assigned barge at every Stops of the Shipment with the barge status: ***PLAN\_RECEIVED***\
        Status at the first Stop will be the same as the barge status
      </td>
    </tr>

    <tr>
      <td>
        Submissions of events prior to "Out Port"
      </td>

      <td>
        At the current Stop: barge status changes accordingly as the barge captain submits tasks at that Stop\
        At the remaining Stops: displays the assigned barge with the barge status: ***PLAN\_RECEIVED***
      </td>
    </tr>

    <tr>
      <td>
        Submission of the event "Out Port"
      </td>

      <td>
        At the recently left Stop (Except for the last Pick Stop of a Dummy Shipment), there are two scenarios:\
        Scenario 1: If at that Stop, the barge is not assigned a pending Shipment, then the barge will no longer be displayed\
        Scenario 2: If at that Stop, the barge is assigned a pending Shipment, then the barge will still  be displayed with the status: ***PLAN\_EXISTS***\
        If the recently left Stop is the last Pick Stop of a Dummy Shipment, then the barge will still be displayed until that Dummy Shipment is linked with its corresponding Internal Actual Shipment, with the status: ***IN\_TRANSIT***\
        At the next Stop of the Dummy Shipment, the barge status will update to: ***IN\_TRANSIT***\
        At the remaining Stops of the Dummy Shipment, the barge status will still be: ***PLAN\_RECEIVED***\
        If the recently left Stop is the last Pick Stop of an External Actual Shipment, then at the remaining Stops of the Shipment, the barge status will be: ***IN\_TRANSIT***
      </td>
    </tr>

    <tr>
      <td>
        Submission of the event "Shipment Completed"\
        (Dummy Shipments)
      </td>

      <td>
        The barge status at all Stops remain the same
      </td>
    </tr>

    <tr>
      <td>
        After Dummy Shipment is linked with its corresponding Internal Actual Shipment
      </td>

      <td>
        At the last Pick Stop of the Shipment, the barge will no longer be displayed\
        At the remaining Stops, the barge will still be displayed. The information of the Dummy Shipment will be replaced by the information of its corresponding Internal Actual Shipment, except for the information fields Import Shipment Code and Export Shipment Code (If available) will still display the Dummy Shipment Code\
        At the remaining Drop Stops of the Shipment, the barge status will be: ***IN\_TRANSIT***
      </td>
    </tr>

    <tr>
      <td>
        Submission of the event "In Port"
      </td>

      <td>
        At the current Stop: barge status changes accordingly as the barge captain submits tasks at that Stop\
        At the remaining Stops: The barge status remain the same
      </td>
    </tr>

    <tr>
      <td>
        Submission of the event "Shipment Completed"\
        (Actual; NFR Shipments)
      </td>

      <td>
        If the barge doesn't have a pending Shipment: Displays the barge at the last Stops with the status: ***PLAN\_AWAITING***\
        If the barge has a pending Shipment: Displays the information of the pending Shipment\
        If the first Stop of the pending Shipment is not the same as the last Stop of the recently completed Shipment: Displays the barge at the last Stop of the recently completed Shipment until the event "Shipment Started" of the pending Shipment is submitted
      </td>
    </tr>
  </tbody>
</Table>

* **Note**: If a barge is currently not assigned any Shipment, then you can make that barge inactive over at the vehicle list. After the barge becomes inactive, it will not be visible on the dashboard. If you make the barge active again, it will only be displayed on the dashboard when it is assigned a Shipment
* Below are the descriptions of the table information fields

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
        SQ
      </td>

      <td>
        Numerical order of the barges of which assigned Shipments contain that Stop
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Name
      </td>

      <td>
        Vehicle Name or Vehicle Code (If Vehicle Name has not been input) of the barge
      </td>
    </tr>

    <tr>
      <td>
        From
      </td>

      <td>
        Organization Code of all Pick Stops - The locations where the containers are picked up and will be dropped off at that Stop\
        Note\
        If that Stop is the last Stop in the barge's NFR Shipment, then there will be the sufix ">>" after that Shipment Code. For example: ***Stop\_01>>***\
        If that Stop is the last Stop in the barge's NFR Shipment, then this field will be blank
      </td>
    </tr>

    <tr>
      <td>
        To
      </td>

      <td>
        Organization Code of all Drop Stops - The location where the containers will be dropped off after being picked up at that Stop\
        Note:\
        If that Stop is the first Stop in the barge's NFR Shipment, then there will be the prefix ">>" before that Shipment Code. For example: ***>>Stop\_01***\
        If that Stop is the last Stop in the barge's NFR Shipment, then this field will be blank\
        If that Stop is the last Stop of the preceding Shipment, and also the first Stop of the pending Shipment, then this field will display the corresponding Drop Stop of the pending Shipment
      </td>
    </tr>

    <tr>
      <td>
        Import Shipment Code
      </td>

      <td>
        The Shipment Codes of the Import Shipments (Shipments in which that Stop is a Drop Stop)\
        Note:\
        If that Stop is the Pick Stop of the Shipment, then this field will be blank\
        If the Shipment is an Internal Actual Shipment, then the table will still display the Shipment Code of its corresponding Dummy Shipment instead of its own Shipment Code\
        If that Stop is the first or last Stop of the barge's NFR Shipment, this field will be blank\
        If that Stop is the last Stop of the preceding Dummy/External Actual Shipment, then this field will display the Shipment Code of the preceding Shipment. This also applies to the NFR Shipments
      </td>
    </tr>

    <tr>
      <td>
        Export Shipment Code
      </td>

      <td>
        The Shipment codes of the Export Shipments (Shipments in which that Stop is a Pick Stop)\
        Note:\
        If that Stop is the Drop Stop of the Shipment, then this field will be blank\
        If that Stop is the first or last Stop of the barge's NFR Shipment, this field will be blank
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        Current status of the barge at the time the Dashboard is accessed\
        Below are the possible statuses

        * **PLAN\_AWAITING\***: The barge hasn't been assigned any pending Shipment
        * **PLAN\_EXISTS\***: The barge has been assigned a Shipment, but the barge captain hasn't submitted any task of that Shipment on Mobile app yet
        * **PLAN\_RECEIVED\***: The barge captain has started submitting tasks of the assigned Shipment on Mobile app
        * **IN\_TRANSIT\***: The barge has completed the Dummy Shipment, the barge captain has submitted the task "Out Port" on Mobile app
      </td>
    </tr>

    <tr>
      <td>
        ETA
      </td>

      <td>
        Short for Estimated Time of Arrival - The time point when the barge is planned to arrive at that Stop\
        This value has been input during the Shipment creation process
      </td>
    </tr>

    <tr>
      <td>
        ATA
      </td>

      <td>
        Short for Actual Time of Arrival - The time point when the barge actually arrived at that Stop\
        This time point is determined by the time the barge captain submitted the task "In Port" on Mobile app
      </td>
    </tr>

    <tr>
      <td>
        ATB
      </td>

      <td>
        Short for Actual Time of Berthing - The time point when the barge actually arrived at the wharf in that Stop\
        This time point is determined by the time the barge captain submitted the task "In Wharves" on Mobile app
      </td>
    </tr>

    <tr>
      <td>
        ATD
      </td>

      <td>
        Short for Actual Time of Departure - The time point when the barge actually departed from that Stop\
        This time point is determined by the time the barge captain submitted the task "Out Port" on Mobile app
      </td>
    </tr>

    <tr>
      <td>
        Waiting
      </td>

      <td>
        The time period during which the barge is idle at the seaport\
        The Waiting time formula is rather lengthy and is described in the following section
      </td>
    </tr>

    <tr>
      <td>
        Draught
      </td>

      <td>
        The draught level (Unit: Meter) of the barge\
        The value in this field is the same as the attribute "Draught" of the barge
      </td>
    </tr>
  </tbody>
</Table>

### View Barge Plan dashboard

* To view the dashboard, the dispatcher needs to create filters on the toolbar in the following steps:
* **Select Location**: The dispatcher needs to choose a location by clicking on **Select Location** field, then type the ***Organization Code*** of the location into the search bar and select it from the drop down menu

> 📘 The dispatcher can select up to ***13 locations*** to view at once

* **Select Date**: The dashboard will show the current date on default. The dispatcher can choose another date to view by clicking on the :fa-calendar-o: icon  and select a date from the drop down calendar
* **Select Barge**: Click on the **Select Barge** field. On the drop down menu is the list of all barges currently mooring at the selected location area. The dispatcher can choose to view the container units of all barges at that location, by clicking on **All barges** text, or view a specific barge by clicking on the corresponding vehicle code of the barge from the drop down menu
* **Note**: If a barge has [***become inactive***](https://docs.abivin.com/docs/freight-transport-sea-barge-manage-barges#change-barge-active-status), it will not be visible on the barge list

<Image title="2019-11-06 11_51_32-Window.png" alt={1175} className="border" border={true} src="https://files.readme.io/42fb683-2019-11-06_11_51_32-Window.png" />

* The dispatcher can click on **Refresh** button to update the most current status
* As a barge submitted the **Out Port** task at a location, meaning the barge has picked up or dropped off the container units at that location according to the shipment plan, the container units will be subtracted from the data displayed on the dashboard upon refreshing

<Image title="22019-11-06 11_47_29-Window.png" alt={1885} className="border" border={true} src="https://files.readme.io/52588c5-22019-11-06_11_47_29-Window.png" />

* To export the information to view offline, the dispatcher can click on **Download** button. The system will gather data based on the current filter and export an Excel template

<Image title="2019-11-06 11_47_29-Window.png" alt={1885} className="border" border={true} src="https://files.readme.io/f9d65d8-2019-11-06_11_47_29-Window.png" />

## Gathering Plan dashboard

* The **Gathering Plan** dashboard is designed to view the container units ***planned to be gathered and loaded*** to a specific vessel, from all Dummy and Actual shipments

## Gathering Plan dashboard interface

* The Gathering Plan dashboard interface consists of three sections

<Image title="2019-11-06 14_25_55-Window.png" alt={1890} className="border" border={true} src="https://files.readme.io/43ecef1-2019-11-06_14_25_55-Window.png" />

### Section 1: Gathering Plan dashboard toolbar

<Image title="2019-11-06 12_27_23-Window.png" alt={652} className="border" border={true} src="https://files.readme.io/4bff802-2019-11-06_12_27_23-Window.png" />

* The toolbar has two information fields: ***Vessel*** and ***Select Barge***. Through these fields, the dispatcher can filter information and view the dashboard as intended
* On the toolbar, there are also three information fields that are transferred from the external general control system

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
        CLS ICD
      </td>

      <td>
        Short for: Closing Time of Inland Container Depot
      </td>
    </tr>

    <tr>
      <td>
        ETB
      </td>

      <td>
        Short for: Estimated Time of Berthing
      </td>
    </tr>

    <tr>
      <td>
        ETD
      </td>

      <td>
        Short for: Estimated Time of Departure
      </td>
    </tr>
  </tbody>
</Table>

* In addition, there are two buttons: ***Refresh*** - Refresh the page to update the most current status; and ***Download*** - Export an Excel template with the current filters

![280](https://files.readme.io/6ec7e26-2019-11-06_12_31_14-Window.png "2019-11-06 12_31_14-Window.png")

### Section 2: Gathering Plan dashboard chart

* On the left side of that dashboard is an area to display **Total Export Containers** chart of the selected vessel

<Image title="2019-11-06 12_27_13-Window.png" alt={831} className="border" border={true} src="https://files.readme.io/df73d58-2019-11-06_12_27_13-Window.png" />

### Section 3: Gathering Plan dashboard information table

<Image title="Untitled-2.png" alt={1673} className="border" border={true} src="https://files.readme.io/c0684e8-Untitled-2.png" />

* This table displays the information of the barges and shipments related to the selected vessel

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
        Barge
      </td>

      <td>
        License plate number of the barge
      </td>
    </tr>

    <tr>
      <td>
        Shipment
      </td>

      <td>
        Code of the Shipment
      </td>
    </tr>

    <tr>
      <td>
        Pick Location
      </td>

      <td>
        Organization Code of the Pick Stop
      </td>
    </tr>

    <tr>
      <td>
        Pick ATA
      </td>

      <td>
        Short for: Actual Time of Arrival at the Pick Stop
      </td>
    </tr>

    <tr>
      <td>
        Pick ATB
      </td>

      <td>
        Short for: Actual Time of Berthing at the Pick Stop
      </td>
    </tr>

    <tr>
      <td>
        Pick ATD
      </td>

      <td>
        Short for: Actual Time of Departure at the Pick Stop
      </td>
    </tr>

    <tr>
      <td>
        Drop ETA
      </td>

      <td>
        Short for: Estimated Time of Arrival at the Drop Stop
      </td>
    </tr>

    <tr>
      <td>
        Drop ATA
      </td>

      <td>
        Short for: Actual Time of Arrival at the Drop Stop
      </td>
    </tr>

    <tr>
      <td>
        20"Hang
      </td>

      <td>
        The quantity of non-empty 20 feet dry container units
      </td>
    </tr>

    <tr>
      <td>
        40"Hang
      </td>

      <td>
        The quantity of non-empty 40 feet dry container units
      </td>
    </tr>

    <tr>
      <td>
        45"Hang
      </td>

      <td>
        The quantity of non-empty 45 feet dry container units
      </td>
    </tr>

    <tr>
      <td>
        20"Lạnh
      </td>

      <td>
        The quantity of non-empty 20 feet reefer container units
      </td>
    </tr>

    <tr>
      <td>
        40"Lạnh
      </td>

      <td>
        The quantity of non-empty 40 feet reefer container units
      </td>
    </tr>

    <tr>
      <td>
        20"Rỗng
      </td>

      <td>
        The quantity of empty 20 feet container units
      </td>
    </tr>

    <tr>
      <td>
        40"Rỗng
      </td>

      <td>
        The quantity of empty 40 feet container units
      </td>
    </tr>

    <tr>
      <td>
        44"Rỗng
      </td>

      <td>
        The quantity of empty 45 feet container units
      </td>
    </tr>

    <tr>
      <td>
        Cold TEUs
      </td>

      <td>
        The total non-empty reefer container units in Twenty Foot Equivalent Units
      </td>
    </tr>

    <tr>
      <td>
        TEUs
      </td>

      <td>
        The total container units in Twenty Foot Equivalent Units
      </td>
    </tr>
  </tbody>
</Table>

## View Gathering Plan dashboard

* To view the dashboard, the dispatcher needs to create filters on the toolbar in the following steps:
* **Select Vessel**: Click on the **Vessel** field, type the ***Vessel code*** into the search bar then choose from the drop down menu
* **Select Barge**: Click on the **Select Barge** field, input the ***Barge code*** into the search bar then choose from the drop down menu

<Image title="2019-11-06 12_27_23-Window.png" alt={652} className="border" border={true} src="https://files.readme.io/91ab822-2019-11-06_12_27_23-Window.png" />

* The dispatcher can click on **Refresh** button to update the most current status
* To export the information to view offline, the dispatcher can click on **Download** button. The system will gather data based on the current filter and export an Excel template

<Image title="2019-11-06 12_31_14-Window.png" alt={280} className="border" border={true} src="https://files.readme.io/7348d23-2019-11-06_12_31_14-Window.png" />
