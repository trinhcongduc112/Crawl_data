---
title: Dashboards
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
## Locate dashboard tab

* You are the dispatcher. On Web app, you can view the shipment status in a visual way through **Dashboard** function
* Navigate to **Reports > Dashboard** tab
* Click on **Select Dashboard Type** field, there are three types of dashboards to choose
* [1. Barge Plan (Internal)](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-barge-plan-internal-dashboard)
* [2. Barge Plan (External)](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-barge-plan-external-dashboard)
* [3. Gathering Plan](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-gathering-plan-dashboard)

<Image title="2019-11-06 12_33_04-Window.png" alt={1891} className="border" border={true} src="https://files.readme.io/fd94d81-2019-11-06_12_33_04-Window.png" />

## Barge Plandashboard

* The dashboard **Barge Plan** is designed to track the loading/unloading status of the barges at specific locations and timeframes, for shipments which have the **Order Type** attribute to be either ***Internal*** or ***External***

## Barge Plan (Internal) dashboard interface

* The Barge Plan (Internal) dashboard interface consists of three sections
* [Section 1: Barge Plan (Internal) dashboard toolbar](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-section-1-barge-plan-internal-dashboard-toolbar)
* [Section 2: Barge Plan (Internal) dashboard charts](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-section-2-barge-plan-internal-dashboard-charts)
* [Section 3: Barge Plan (Internal) dashboard barge information table](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-section-3-barge-plan-internal-dashboard-barge-information-table) 

<Image title="2019-11-06 12_34_12-Window.png" alt={1898} className="border" border={true} src="https://files.readme.io/fa9940e-2019-11-06_12_34_12-Window.png" />

### Section 1: Barge Plan (Internal) dashboard toolbar

* The toolbar has three information fields: ***Date Range; Select Location*** and ***Select Barge***. Through these fields, the dispatcher can filter information and view the dashboard as intended
* In addition, there are two buttons: ***Refresh*** - Refresh the page to update the most current status; and ***Download*** - Export an Excel template with the current filters

<Image title="2019-11-06 12_36_47-Window.png" alt={1734} className="border" border={true} src="https://files.readme.io/b89d8d8-2019-11-06_12_36_47-Window.png" />

### Section 2: Barge Plan (Internal) dashboard charts

* The screen is split into two sides. On the right side is **LOAD (Dummy)** charts. These charts shows the container units ***planned to be picked up*** of all Dummy shipments at a specific location. On the left side is **DISC (Actual)** charts. These charts  shows the container units ***planned to be dropped off*** of all Actual shipments at a specific location
* Both the LOAD (Dummy) charts and DISC (Actual) charts are made up of two chart types: **Bar chart** and **Pie chart**:
* The Bar chart shows the quantity of each container type (20 feet Dry Full, 40 feet Dry Full, 45 feet Dry Full, 20 feet Refrigerated Full, 40 feet Refrigerated Full, 20 feet Empty, 40 feet Empty, 45 feet Empty)
* The Pie chart also shows the quantity of each container type, but has been converted into [***Twenty-foot equivalent units (TEUs)***](https://en.wikipedia.org/wiki/Twenty-foot_equivalent_unit) 

<Image title="2019-11-06 11_53_29-Window.png" alt={1693} className="border" border={true} src="https://files.readme.io/eca9f3f-2019-11-06_11_53_29-Window.png" />

### Section 3: Barge Plan (Internal) dashboard barge information table

<Image title="Untitled-1.png" alt={1681} className="border" border={true} src="https://files.readme.io/0abe407-Untitled-1.png" />

* Below the charts is the barge information table. This table tracks the status of the barges which have visited, or are currently mooring at a specific location

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
        Numerical order
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Name
      </td>

      <td>
        Name or Vehicle code (If there is no name yet) of the barge
      </td>
    </tr>

    <tr>
      <td>
        From
      </td>

      <td>
        Organization Code of the Pick Stop - The location where the containers are picked up
      </td>
    </tr>

    <tr>
      <td>
        To
      </td>

      <td>
        Organization Code of the Drop Stop - The location where the containers are dropped off
      </td>
    </tr>

    <tr>
      <td>
        Dummy ID import
      </td>

      <td>
        The ID (Shipment code) of the Dummy shipment of Import type
      </td>
    </tr>

    <tr>
      <td>
        Dummy ID export
      </td>

      <td>
        The ID (Shipment code) of the Dummy shipment of Export type
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        Current status of the barge
      </td>
    </tr>

    <tr>
      <td>
        ETA
      </td>

      <td>
        Short for Estimated Time of Arrival
      </td>
    </tr>

    <tr>
      <td>
        ATA
      </td>

      <td>
        Short for Actual Time of Arrival
      </td>
    </tr>

    <tr>
      <td>
        ATB
      </td>

      <td>
        Short for Actual Time of Berthing
      </td>
    </tr>

    <tr>
      <td>
        ATD
      </td>

      <td>
        Short for Actual Time of Departure
      </td>
    </tr>

    <tr>
      <td>
        Waiting
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Draught
      </td>

      <td>
        The draught level (Unit: Meter) of the barge
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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

## View Barge Plan (Internal) dashboard

* To view the dashboard, the dispatcher needs to create filters on the toolbar in the following steps:
* **Select Location**: The dispatcher needs to choose a location by clicking on **Select Location** field, then type the ***Organization Code*** of the location into the search bar and select it from the drop down menu

> 📘 The dispatcher can select up to ***13 locations*** to view at once

* **Select Date**: The dashboard will show the current date on default. The dispatcher can choose another date to view by clicking on the :fa-calendar-o: icon  and select a date from the drop down calendar
* **Select Barge**: Click on the **Select Barge** field. On the drop down menu is the list of all barges currently mooring at the selected location area. The dispatcher can choose to view the container units of all barges at that location, by clicking on **All barges** text, or view a specific barge by clicking on the corresponding vehicle code of the barge from the drop down menu

<Image title="2019-11-06 11_51_32-Window.png" alt={1175} className="border" border={true} src="https://files.readme.io/42fb683-2019-11-06_11_51_32-Window.png" />

* The dispatcher can click on **Refresh** button to update the most current status
* As a barge submitted the **Out Port** task at a location, meaning the barge has picked up or dropped off the container units at that location according to the shipment plan, the container units will be subtracted from the data displayed on the dashboard upon refreshing

<Image title="22019-11-06 11_47_29-Window.png" alt={1885} className="border" border={true} src="https://files.readme.io/52588c5-22019-11-06_11_47_29-Window.png" />

* To export the information to view offline, the dispatcher can click on **Download** button. The system will gather data based on the current filter and export an Excel template

<Image title="2019-11-06 11_47_29-Window.png" alt={1885} className="border" border={true} src="https://files.readme.io/f9d65d8-2019-11-06_11_47_29-Window.png" />

## Barge Plan (External) dashboard

* The **Barge Plan (External)** dashboard is designed to track the load/unload status of the barges at specific locations and timeframes, for shipments which have the **Order Type** attribute to be ***External***

## Barge Plan (External) dashboard interface

* The Barge Plan (External) dashboard interface consists of three sections
* [Section 1: Barge Plan (External) dashboard toolbar](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-section-1-barge-plan-external-dashboard-toolbar)
* [Section 2: Barge Plan (External) dashboard charts](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-section-2-barge-plan-external-dashboard-charts)
* [Section 3: Barge Plan (External) dashboard barge information table](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-section-3-barge-plan-external-dashboard-barge-information-table)

<Image title="Image 2.png" alt={1863} className="border" border={true} src="https://files.readme.io/54fa30c-Image_2.png" />

### Section 1: Barge Plan (External) dashboard toolbar

* The toolbar has three information fields: ***Date Range; Select Location*** and ***Select Barge***. Through these fields, you can filter information and view the dashboard as intended
* In addition, there are two buttons: ***Refresh*** - Refresh the page to update the most current status; and ***Download*** - Export an Excel template with the current filters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description & Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Date Range
      </td>

      <td>
        **1. Description:**\
        The date range which contains the creation date of the shipments\
        **2. Input rules:**\
        [Click on this link](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-step-1-select-date-range-for-the-barge-plan-external-dashboard)
      </td>
    </tr>

    <tr>
      <td>
        Location
      </td>

      <td>
        **1. Description:**\
        The stops you want to display on the dashboard\
        **2. Input rules:**\
        [Click on this link](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-step-2-select-location-for-the-barge-plan-external-dashboard)
      </td>
    </tr>

    <tr>
      <td>
        Barge
      </td>

      <td>
        **1. Description:**\
        The barges that have visited, are currently mooring at, or will visit the selected stops\
        **2. Input rules:**\
        [Click on this link](https://docs.abivin.com/docs/freight-transport-sea-barge-dashboards#section-step-3-select-barge-for-the-barge-plan-external-dashboard)
      </td>
    </tr>
  </tbody>
</Table>

### Section 2: Barge Plan (External) dashboard charts

* The screen is split into two sides. On the right side is **Load** charts. These charts shows the container units which are ***planned to be picked up*** of all  External shipments at a specific location. On the left side is **Unload** charts. These charts shows the container units which are ***planned to be dropped off*** of all External shipments at a specific location
* Both the Unload and Load charts are made up of two chart types: **Bar chart** and **Pie chart**:
* The Bar chart shows the quantity of each container type (20 feet Dry Full, 40 feet Dry Full, 45 feet Dry Full, 20 feet Refrigerated Full, 40 feet Refrigerated Full, 20 feet Empty, 40 feet Empty, 45 feet Empty)
* The Pie chart also shows the quantity of each container type, but has been converted into [***Twenty-foot equivalent units (TEUs)***](https://en.wikipedia.org/wiki/Twenty-foot_equivalent_unit)

### Section 3: Barge Plan (External) dashboard barge information table

* Below the charts is the barge information table. This table tracks the status of the barges which have visited, or are currently mooring at a specific location

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
        Numerical order of the barges that will visit, have visited or are currently mooring at the location\
        The barges will be sorted based on the ETA - Estimated Time of Arrival at that specific location. The barge which has the earlier ETA will be sorted on top
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Name
      </td>

      <td>
        Name or Vehicle code (If there is no name yet) of the barge
      </td>
    </tr>

    <tr>
      <td>
        From
      </td>

      <td>
        Organization Code of the Pick Stops - The locations where the barge will visit to load containers\
        For shipments that have a Pick Stop to be the same as the selected location, this field will be blank
      </td>
    </tr>

    <tr>
      <td>
        To
      </td>

      <td>
        Organization Code of the Drop Stops - The locations where the barge will visit to unload containers\
        For shipments that have a Drop Stop to be the same as the selected location, this field will be blank
      </td>
    </tr>

    <tr>
      <td>
        Shipment Id
      </td>

      <td>
        ID (Shipment Code) of the shipment
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        Status of the barge at the stop
      </td>
    </tr>

    <tr>
      <td>
        ETA
      </td>

      <td>
        Short for Estimated Time of Arrival - The time the barge is planned to arrive at a stop\
        Unit: hh:mm dd/mm (Hour:Minute Date/Month)
      </td>
    </tr>

    <tr>
      <td>
        ATA
      </td>

      <td>
        Short for Actual Time of Arrival - The time the barge actually arrives and unloads containers at a stop\
        This field will take the value of the time when the barge captain submits the task "In Port" on Mobile app\
        Unit: hh:mm dd/mm (Hour:Minute Date/Month)
      </td>
    </tr>

    <tr>
      <td>
        ATB
      </td>

      <td>
        Short for Actual Time of Berthing -  The time the barge actually moores at a stop's berth\
        Unit: hh:mm dd/mm (Hour:Minute Date/Month)
      </td>
    </tr>

    <tr>
      <td>
        ATD
      </td>

      <td>
        Short for Actual Time of Departure - The time the barge actually departs from a stop\
        Unit: hh:mm dd/mm (Hour:Minute Date/Month)
      </td>
    </tr>

    <tr>
      <td>
        Waiting
      </td>

      <td>
        The time period between: 1. The time the barge captain submit the task "In Port" at a stop, and 2. The time when the barge captain submits the task "Line Up Started" (For Pick Stop) or "Unload Started" (For Drop Stop)\
        Unit: hh:mm:ss (Hour:Minute:Second)
      </td>
    </tr>

    <tr>
      <td>
        Draught
      </td>

      <td>
        The draught level (Unit: Meter) of the barge
      </td>
    </tr>
  </tbody>
</Table>

## View Barge Plan (External) dashboard

* To view the dashboard, you need to create filters on the toolbar in the following steps:

### Step 1: Select Date Range for the Barge Plan (External) dashboard

* The dashboard will show the current date on default. You can select another date range to view by clicking on the calendar icon :fa-calendar-o: and select a date range from the drop down calendars

<Image title="Image 3.png" alt={532} className="border" border={true} src="https://files.readme.io/0a63ac0-Image_3.png" />

### Step 2: Select Location for the Barge Plan (External) dashboard

* You need to select the location(s) by clicking on **Select Location** field, then input the ***Organization Code*** of the desired location into the search bar and select from the drop down menu
* You can select up to ***13 locations***

<Image title="Image 5.png" alt={406} className="border" border={true} src="https://files.readme.io/4d6ac1c-Image_5.png" />

### Step 3: Select Barge for the Barge Plan (External) dashboard

* Click on the **Select Barge** field. On the drop down menu is the list of all barges of which shipment routes contain the selected locations. You can select all barges by clicking on the text **All Barge**, or select a specific barge by clicking on the corresponding vehicle code of the barge from the drop down menu

<Image title="Image 6.png" alt={400} className="border" border={true} src="https://files.readme.io/df9409f-Image_6.png" />

## Update Barge Plan (External) dashboard status

* You can click on **Refresh** button to update the most current status of the dashboard
* As the barge captain submits the **Out Port** task at a location, which means the barge has loaded/unloaded the container units at that location according to the shipment plan, then upon refreshing, the dashboard will display the container units of the remaining locations, after subtracting the container units of the above location

## Export Barge Plan (External) dashboard

* To export the dashboard information to view offline, you can click on **Download** button. The system will gather data based on the current filter and export an Excel template

## Barge Plan (External) dashboard information display rules

* Below are the information display rules that apply to all shipments 

### After the barge captain has submitted the "In Port" task at a stop

* Status of the barge at that stop will be ***LINE\_UP\_AWAITING***
* Status of the barge at the following stop(s) after that stop will be ***PLAN\_RECEIVED***

### After the barge captain has submitted the "Out Port" task at a stop

* Status of the barge at that stop will be hidden from the dashboard (This also applies to every stops that precede that stop in the shipment, if available)
* Status of the barge at the very next stop after that stop will be ***IN\_TRANSIT***
* Status of the barge at the remaining stop(s) of the shipment will be ***PLAN\_RECEIVED***

### After the barge captain has submitted the "Shipping Completed" task at the last stop of the last shipment

* The dashboard will display the barge status at the last stop of the last shipment
* There will be two scenarios:
* Scenario 1: The barge is not assigned any next shipment. The barge status will be ***PLAN\_AWAITING***
* Scenario 2: The barge is assigned another shipment. The barge status will be ***PLAN\_EXISTS***

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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

      </td>

      <td>

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
