---
title: Reports
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
> 📘 To maintain the system performance, we currently restrict the date range to export reports to no more than 1 month

## Compulsory Configurations

* You need to enable the configuration **Reports** at both the **Manufacturer** and the **Branch**
* You need to enable the module **Report** for the User group. Refer to this article: [**Manage Users**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#manufacturer-administrator-user-group)

> 🚧 Report Export Permission
>
> At the moment, only the user accounts that belong to the Manufacturer and Branch can view and export reports. User accounts that belong to the lower-level Organization Types, such as Depot, will not have this permission

## Locate Report tab

* Navigate to **Reports > Report** tab
* This tab is where you can generate and export reports

<Image title="1. Reports 1 (ENG).png" alt={1899} border={true} src="https://files.readme.io/f534c7a-1._Reports_1_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Reports 1.png" alt={1898} border={true} src="https://files.readme.io/d49444d-1._Reports_1.png">
  Illustration (Vietnamese)
</Image>

## General steps to generate and export report

> 📘
>
> The steps outlined below only apply to the following reports: ST02, ST04, ST05, ST08, ST09, ST10, ST12. For other reports, you will need to do additional steps

* **Step 1: Select the report:** Click on the field below the text **Report Type**, select the appropriate report from the drop down list

<Image title="report list.png" alt={464} border={true} src="https://files.readme.io/6e08aa1-report_list.png">
  Illustration (English)
</Image>

<Image title="2. All Reports (VIE).png" alt={581} border={true} src="https://files.readme.io/abde902-2._All_Reports_VIE.png">
  Illustration (Vietnamese)
</Image>

* **Step 2: Select the date range:** Click on the field below the text **Date Range**, select the appropriate date range from the drop-down calendars, then click on **Apply** to confirm selecting the date range. Alternatively, you could input the date range directly into the field in the following format: ***yyyy-mm-dd:yyyy-mm-dd***

<Image title="date range.png" alt={538} border={true} src="https://files.readme.io/4338611-date_range.png">
  Illustration (English)
</Image>

<Image title="2. Date Range (VIE).png" alt={598} border={true} src="https://files.readme.io/44d74fd-2._Date_Range_VIE.png">
  Illustration (Vietnamese)
</Image>

* If your selected date range exceeds 31 days, there will be an error message as below. In this case, please select another date range. 

<Image title="1. Error Message (ENG).png" alt={1920} border={true} src="https://files.readme.io/c7f0a56-1._Error_Message_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Error Message (VIE).png" alt={1920} border={true} src="https://files.readme.io/56511aa-1._Error_Message_VIE.png">
  Illustration (Vietnamese)
</Image>

* **Note:** If the language for display is a language other than Vietnamese (for example, English, Indonesian, Japanese...), the default language of reports is English. 

* **Step 3: Select whether there will be a header in the report or not** By default, you will see a toggle button :fa-toggle-off: named **Exclude Report Header**. When you leave this button off, there will not be a header of the report name and the date range

* If you want to add the report name and the date range to the report, click on that switch button. When the button changes to :fa-toggle-on:, the text will change to **Include Report Header**, which means in the report there will be a header of the report name and the date range, as in screenshots below

<Image title="header on.png" alt={1899} border={true} src="https://files.readme.io/d9040cd-header_on.png">
  Illustration (English)
</Image>

<Image title="Title (VIE).png" alt={1920} border={true} src="https://files.readme.io/aa7b4df-Title_VIE.png">
  Illustration (Vietnamese)
</Image>

* **Step 4: Download the report:** Click on the button **Download** :fa-download:. The system will immediately start gathering data based on your filters, and will generate a downloadable Excel template shortly

<Image title="download report.png" alt={673} border={true} src="https://files.readme.io/9fa0477-download_report.png">
  Illustration (English)
</Image>

<Image title="3. Download.png" alt={876} border={true} src="https://files.readme.io/7a056b5-3._Download.png">
  Illustration (Vietnamese)
</Image>

## ST01 - Orders By All Drivers

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Driver Code"
      </td>

      <td>
        Management code of the driver
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Driver Name"
      </td>

      <td>
        Name of the driver
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Vehicle Type"
      </td>

      <td>
        Vehicle type
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Re-delivered order"
      </td>

      <td>
        Total unplanned orders of the previous day dragged back to current route plan
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Net Re-delivered Revenue"
      </td>

      <td>
        Revenue of the previous day's total unplanned orders before discount
      </td>

      <td>
        Number
      </td>

      <td>
        VND
      </td>
    </tr>

    <tr>
      <td>
        "Number of Orders"
      </td>

      <td>
        Total orders in all locked/finalized route plans
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Net Revenue"
      </td>

      <td>
        Revenue from all orders (including that from all re-delivered orders) before discount
      </td>

      <td>
        Number
      </td>

      <td>
        VND
      </td>
    </tr>

    <tr>
      <td>
        "Total Order Weight"
      </td>

      <td>
        Total weight of the orders assigned to the vehicle. Data in this field is gathered from the total weight of the products in those orders
      </td>

      <td>
        Number
      </td>

      <td>
        Kilogram (kg)
      </td>
    </tr>

    <tr>
      <td>
        "Total Order Volume"
      </td>

      <td>
        Total volume of orders assigned to the vehicle. Data in this field is gathered from the total volume of the products in those orders
      </td>

      <td>
        Number
      </td>

      <td>
        Cubic meter (m3)
      </td>
    </tr>

    <tr>
      <td>
        "Planned Revenue"
      </td>

      <td>
        Revenue from orders in locked/finalized route plans (This is the same as Revenue displayed in the Route Plan View and calculated after discount)
      </td>

      <td>
        Number
      </td>

      <td>
        VND
      </td>
    </tr>

    <tr>
      <td>
        "Planned Cost"
      </td>

      <td>
        Costs from orders in locked/finalized route plans (This is the same as Costs displayed in the Route Plan View)
      </td>

      <td>
        Number
      </td>

      <td>
        VND
      </td>
    </tr>

    <tr>
      <td>
        "Planned Distance"
      </td>

      <td>
        Calculated distance of locked/finalized delivery routes (This is the same as Distance displayed in the Route Plan View)
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Planned Time"
      </td>

      <td>
        Delivery Time as planned in the Route Plan
      </td>

      <td>
        Number
      </td>

      <td>
        Hour(s)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Revenue"
      </td>

      <td>
        Revenue from successfully delivered orders
      </td>

      <td>
        Number
      </td>

      <td>
        VND
      </td>
    </tr>

    <tr>
      <td>
        "Actual Cost"
      </td>

      <td>
        Cost delivered as actual
      </td>

      <td>
        Number
      </td>

      <td>
        VND
      </td>
    </tr>

    <tr>
      <td>
        "Actual Distance"
      </td>

      <td>
        Distance delivered as actual
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Start Time"
      </td>

      <td>
        Actual start time of driver
      </td>

      <td>
        Date
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Actual End Time"
      </td>

      <td>
        Actual end time of driver
      </td>

      <td>
        Date
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Total Actual Time"
      </td>

      <td>
        Total actual time of the vehicle to deliver product.
      </td>

      <td>
        Number
      </td>

      <td>
        Hour(s)
      </td>
    </tr>

    <tr>
      <td>
        "VFR By Trips"
      </td>

      <td>
        Vehicle filling rate by volume
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "VFR By Weight"
      </td>

      <td>
        Vehicle filling rate by weight
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Fulfilled Orders"
      </td>

      <td>
        Number of orders that have been successfully delivered by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Net Revenue Delivered"
      </td>

      <td>
        Revenue from successfully delivered orders before discount as actual
      </td>

      <td>
        Number
      </td>

      <td>
        VND
      </td>
    </tr>

    <tr>
      <td>
        "Partially Fulfilled Orders"
      </td>

      <td>
        Number of orders that have been partially delivered by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Unfulfilled Orders"
      </td>

      <td>
        Numbers of orders that have not been delivered successfully by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Not Yet Fulfilled Orders"
      </td>

      <td>
        Number of orders that have not been delivered yet by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Number of off-200m check-in"
      </td>

      <td>
        Number of times when the distance between the vehicle check-in's location and the store is over 200 meters
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>
  </tbody>
</Table>

* **Calculation Formula**
* Re-delivered Order = Total Not-yet-fulfilled Orders + Total Unfulfilled Orders
* Net Re-delivered Revenue = Number Of Cases x Case Price + Number Of Items x Item Price
* Net Revenue = Number Of Cases x Case Price + Number Of Items x Item Price
* Total Actual Time = Check out Time - Check in Time

## ST02 - KPI Scoreboard

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data Type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        No.
      </td>

      <td>
        Numerical Order
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Delivery Date"
      </td>

      <td>
        The date on which the Order was performed
      </td>

      <td>
        Date\
        (Format: YYYY-MM-DD)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "VFR by Trips"
      </td>

      <td>
        The average vehicle fill rate (by volume) of all trips
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Truck Utilization"
      </td>

      <td>
        The ratio of the number of trucks used to Total Vehicle of all trucks
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Service Level"
      </td>

      <td>
        The ratio of the number of delivered orders to the number of planned orders of all drivers
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Driver Adoption"
      </td>

      <td>
        The ratio of the number of drivers who have used Abivin App to the total number of drivers
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Compliance Driver"
      </td>

      <td>
        The ratio of Executed Tasks over Planned tasks of all drivers
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Delivery GPS Compliance"
      </td>

      <td>
        The ratio of the number of correctly submitted Check-in tasks (In the distance of 200 meters from the customer location) over the total Number of Check-in tasks submitted by all drivers
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Planned Distance"
      </td>

      <td>
        The total planned distance of all vehicles (the figure can be checked in the Route Plan)
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Distance"
      </td>

      <td>
        The total actual distance traveled by all vehicles
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Kilometer Actual"
      </td>

      <td>
        The ratio of Actual Distance to Planned Distance
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>
  </tbody>
</Table>

* **Calculation Formula**
* VFR (Volume Fill Rate) = Sum of VFR of all trips/ Number of trips of all trucks
* Truck Utilizations (%) = Vehicle Used/Total Vehicles (Total vehicles include active vehicles and inactive ones)
* Service Level (%) = Total delivered orders/ Total planned orders of all drivers (**Total delivered orders** include Partially Fulfilled Orders and Fulfilled Orders)
* Driver Adoption ratio = Number of drivers who have used Abivin App during delivery trips/Total number of drivers in the route plan
* Compliance Driver ratio = All Executed Task/ Planned tasks of all drivers
* Delivery GPS Compliance = Number of correct Checkin (within 200m from the delivery stop)/ Total Number of Checkin of all drivers

## ST02.2 - KPI MTD Scoreboard

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Description
      </th>

      <th>
        Data Type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Day"
      </td>

      <td>
        The date of the order
      </td>

      <td>
        Date
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        "Depot Code"
      </td>

      <td>
        The management code of depot. This must be the same as Depot Code found in Web App
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Average VFR by Volume"
      </td>

      <td>
        The average fulfillment rate (VFR) of the vehicle by Volume of a depot
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Total Product Volume"
      </td>

      <td>
        Sum of volume of all products going out of each Depot each day
      </td>

      <td>
        Number
      </td>

      <td>
        Cubic meter (m3)
      </td>
    </tr>

    <tr>
      <td>
        "Planned Time Utilization"
      </td>

      <td>
        Average planned working time of all deliverymen from each depot (Unit: %)
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Time Utilization"
      </td>

      <td>
        Average actual working time of all deliverymen from each depot (Unit: %)
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Average Transaction Time"
      </td>

      <td>
        Average service time of all truck from each depot
      </td>

      <td>
        Number
      </td>

      <td>
        Minute(s)
      </td>
    </tr>

    <tr>
      <td>
        "Truck Utilization"
      </td>

      <td>
        The Truck Utilization rate of each depot (Unit: %)
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Number of Trucks"
      </td>

      <td>
        Total number of truck belong to each depot (excluding Rent Vehicles)
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Number of Used Trucks"
      </td>

      <td>
        Total number of assigned truck for each day of each depot.
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Average Drop Point"
      </td>

      <td>
        Average stops on each trip of each depot
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Percentage by Value of On-Time Orders  (Sponsor Item)"
      </td>

      <td>
        Percentage of orders that are executed on-time in a depot
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Percentage by Value of On-Time Orders (non Sponsor Item)"
      </td>

      <td>
        Percentage of non-sponsor orders that are executed on-time in a depot
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Service Level"
      </td>

      <td>
        The service level rate in a depot
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Percentage by Value of Rejected Orders (Sponsor Item)"
      </td>

      <td>
        Percentage of rejected delivery in a depot
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Percentage by Value of Rejected Orders (non Sponsor Item)"
      </td>

      <td>
        Percentage of non-sponsor rejected delivery in a depot
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Driver Adoption"
      </td>

      <td>
        The completion rate of the Drivers on orders
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Planner Adoption"
      </td>

      <td>
        The completion rate of the Planners on orders
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Total Adoption"
      </td>

      <td>
        The average of helper and planner compliance in executing orders
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Delivery GPS Compliance"
      </td>

      <td>
        The compliance rate of the drivers on each Task within 60m of each store
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Planned Distance"
      </td>

      <td>
        Total planned distance of all truck for each depot for 1 day
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Distance"
      </td>

      <td>
        Total actual travelled distance of all truck for each depot in 1 day
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Actual/Planned Distance (Ratio)"
      </td>

      <td>
        The actual rate of the distance for each delivery
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Route Plan Compliance"
      </td>

      <td>
        The compliance rate of the Route Plan Optimization
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>
  </tbody>
</Table>

* **Calculation Formula**
* Average VFR by Volume = Volume of all product going out of each Depot / Total capacity of all assigned trucks of each depot x 100%
* Planned Time Utilization = "(A) Planned working time of each deliveryman for 1 day / working hour in driver's contract x 100%\
  Result: Average of (A) of all deliverymen of each depot"
* Actual Time Utilization = "(B) Actual working time of each deliveryman for 1 day / working hour in driver's contract x 100%\
  Result: Average of (B) of all deliverymen of each depot (%)"
* Average Transaction Time = "(C) Average Service time of each truck at each stop\
  Result: Average of (C) all truck of each depot"
* Average Drop Point = "(D) Average number of the stop of each trip, for each truck\
  Result: Average of (D) of all truck of each depot"
* Percentage by Value of On-time Delivery (sponsor items) = Percentage of on-time delivery: Sum by value of all orders completed on the planned date with sponsored items / Sum by value of all order with sponsored items  x 100%
* Percentage by Value of On-time Delivery (non-sponsor items) Percentage of on-time delivery: Sum by value of all orders completed on the planned date with non-sponsor items / Sum by value of all orders with non sponsor items x 100%
* Percentage by Value of Rejected orders (sponsor items) = Percentage of rejected delivery: Sum by value of all orders rejected on the planned date with sponsor items / Sum by value of all orders on the planned date with sponsor items x 100%
* Percentage by Value of Rejected orders (non-sponsor items) = Percentage of rejected delivery: Sum by values of all orders rejected on the planned date with non-sponsor items / sum by value of all order on the planned date with non-sponsor items x 100%
* Driver Adoption = Total number of completed tasks through mobile of all deliverymen / Total number of tasks of all deliverymen of each depot x 100%
* Planner Adoption = Total number of orders vRoute is able to plan / Total number of orders input to vRoute x 100%
* Total Adoption = Average of driver and planner compliance x 100%
* Delivery GPS Compliance = Number of tasks completed by driver, for POD, within 60m of each store, for all store/ total number of tasks of all deliverymen x 100%

## ST03 - Orders By Single Driver

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "No."
      </td>

      <td>
        The numerical order of the Order in the report
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Date"
      </td>

      <td>
        The date on which the Order should have been performed (As planned)\
        Same as the attribute "Order Date" of the Order
      </td>

      <td>
        Date\
        (Format: YYYY-MM-DD)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Driver Code"
      </td>

      <td>
        Driver Code
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Driver Name"
      </td>

      <td>
        Full name of the driver
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Code"
      </td>

      <td>
        Customer Code
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Name"
      </td>

      <td>
        Customer Name
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Address"
      </td>

      <td>
        Customer Address
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Code"
      </td>

      <td>
        Order Code
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Salesman Code"
      </td>

      <td>
        Code of the Salesman who placed the Order (If that happened)
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Status"
      </td>

      <td>
        Status of the Order at the time the report was generated. Possible values are: Open; Shipped
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Planned Total Revenue"
      </td>

      <td>
        The total revenue generated from the order as planned. Data in this field is gathered directly from the order information
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit based on the attribute Country configured at the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        "Actual Total Revenue" (\*)
      </td>

      <td>
        The actual total revenue of the order. Data in this field is gathered from the amount that was manually submitted by the driver on the Mobile App.
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit based on the attribute Country configured at the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        "Fulfillment Status"
      </td>

      <td>
        The delivery status of the order at the time the report is generated. Possible values are: Fulfilled; Unfulfilled; Not Yet Fulfillment; Partially Fulfilled
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Unfulfilled Reason"
      </td>

      <td>
        The reason why the order could not be delivered to the customer (If that happens). Data in this field is taken from the reason that the driver selected on the Mobile App
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Lat"
      </td>

      <td>
        Latitude of the customer location
      </td>

      <td>
        Number\
        Format: Decimal Degrees
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Long"
      </td>

      <td>
        Longitude of the customer location
      </td>

      <td>
        Number\
        Format: Decimal Degrees
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Check-in Lat"
      </td>

      <td>
        Latitude of the location where the driver submitted the task Check-in
      </td>

      <td>
        Number\
        Format: Decimal Degrees
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Check-in Long"
      </td>

      <td>
        Longitude of the location where the driver submitted the task Check-in
      </td>

      <td>
        Number\
        Format: Decimal Degrees
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Distance Difference"
      </td>

      <td>
        The distance between the location where the driver submitted the task Check in and the actual location of the customer
      </td>

      <td>
        Number
      </td>

      <td>
        Meter (m)
      </td>
    </tr>

    <tr>
      <td>
        "Planned Index"
      </td>

      <td>
        The planned index of the customer on the Delivery route
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Task Name"
      </td>

      <td>
        The planned index of the customer plus the Customer Name
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Signature Status"
      </td>

      <td>
        The status to specify whether the customer has signed digitally when receiving the delivery or not. Possible values are: Not yet; Signed
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Email Sending Status"
      </td>

      <td>
        The status to specify whether the email with the Electronic proof of delivery was sent to the customer or not. Possible values are: Not yet; Sent
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Total Quantity"
      </td>

      <td>
        Total number of Items per Order planned
      </td>

      <td>
        Number
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        "Total Order Weight (kg)"
      </td>

      <td>
        Total Weight (in kg) per Order planned.
      </td>

      <td>
        Number\
        Format: Decimal Degrees
      </td>

      <td>
        Kilogram (kg)
      </td>
    </tr>

    <tr>
      <td>
        "Total Order Volume (m3)"
      </td>

      <td>
        Total Volume (in m3) per Order planned.
      </td>

      <td>
        Number\
        Format: Decimal Degrees
      </td>

      <td>
        Cubic meter (m3)
      </td>
    </tr>
  </tbody>
</Table>

* **(\*): Calculation formula:**

* Total Quantity  =  Number of Cases x Item per Case + Items

* Total Order Weight (kg) = Case Weight x Number of Cases + Case Weight x Number of Items / Item per Case

* Total Order Volume (m3) = Case Volume x Number of Cases + Case Volume x Number of Items / Item per Case

* **(\*): The data of this field is directly affected by the delivery result that the driver actually submitted on the Mobile App**:

* Actual Total Revenue = Planned Total Revenue, if the delivery result was submitted as **Completed**

* Actual Total Revenue \< Planned Total Revenue, if the delivery result was submitted as **Partly Delivered**

* The data cell is left blank, if the delivery result was submitted as **Not Completed**

## ST04 - Routes By Single Driver

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Driver Code"
      </td>

      <td>
        Management code of Driver
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Driver Name"
      </td>

      <td>
        Full name of the driver
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Planned Distance"
      </td>

      <td>
        Distance covered by the vehicle as planned
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Distance"
      </td>

      <td>
        Actual distance covered by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Number of Orders"
      </td>

      <td>
        Number of orders assigned to the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Fulfilled Orders"
      </td>

      <td>
        The number of orders successfully delivered
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Perfect Order Rate"
      </td>

      <td>
        Average rate of successfully delivered orders to number of  orders assigned to a driver within a selected time period
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Total Order Weight"
      </td>

      <td>
        Total weight of the orders assigned to the vehicle. Data in this field is gathered from the total weight of the products in those orders
      </td>

      <td>
        Number
      </td>

      <td>
        Kilogram (kg)
      </td>
    </tr>

    <tr>
      <td>
        "Total Order Volume"
      </td>

      <td>
        Total volume of orders assigned to the vehicle. Data in this field is gathered from the total volume of the products in those orders
      </td>

      <td>
        Number
      </td>

      <td>
        Cubic meter (m3)
      </td>
    </tr>

    <tr>
      <td>
        "Number of Off-200m"
      </td>

      <td>
        Number of times when the distance between the vehicle check-in's location and the store is over 200 meters
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "VFR by Trips"
      </td>

      <td>
        Average Vehicle Fill Rate of all vehicles by all trips (either by weight or volume, the one having the greater value will be displayed)
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>
  </tbody>
</Table>

## ST05 - Inventory By products

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "No."
      </td>

      <td>
        Numerical order of products according to Depot
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Organization Name"
      </td>

      <td>
        Name of the Depot
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Product Code"
      </td>

      <td>
        Management code of product.
      </td>

      <td>
        String (text, number and special characters) 
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Product Name"
      </td>

      <td>
        Product Name
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Product Unit"
      </td>

      <td>
        Product Unit
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Inventory Begin"
      </td>

      <td>
        Number of products in warehouse of the first day in date range selects to export the report.
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Inventory Purchase"
      </td>

      <td>
        Total products in Purchase order
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Inventory Sale"
      </td>

      <td>
        Total products in Sales order(only sales order whose status is shipped) and warehouse card (-)
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Inventory End"
      </td>

      <td>
        Number of products in warehouse on the last day of selected date range to export the report.
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>
  </tbody>
</Table>

* **Calculation Formula**
* Inventory Begin = On-hand Quantity at 0h of the start of the selected date range
* Inventory Purchase = The number of products in Purchase orders with status **Put Away** + Total Increase in the on-hand quantity of that product during the selected date range.
* Inventory Sale = The number of products in Sale orders with status **Shipped** + Total Decrease in the on-hand quantity of that product during the selected date range.
* Inventory End of a selected date range = Inventory Begin of the date range  + Inventory Purchase during the selected date range - Inventory Sale during the selected date range

## ST06 - Orders And Products

* To download this report, first follow from Step 1 to Step 3 that have been described in the section [**General steps to generate and export report**](https://docs.abivin.com/docs/vrp-in-house-fleet-reports#section-general-steps-to-generate-and-export-report). Then, before you click on **Download**, please take the additional steps below.
* **Step 4: Select Information fields:** Click on the field below the text **Shown Columns**, then select the appropriate information fields on the drop-down menu by clicking on the corresponding check box icon :fa-square-o:. When that icon turns to :fa-check-square:, that means an information field has been selected and will be presented on the report

<Image title="ST06 - Shown Columns (ENG).gif" alt={1903} border={true} src="https://files.readme.io/5b044ae-ST06_-_Shown_Columns_ENG.gif">
  Illustration (English)
</Image>

<Image title="ST06 - Column Shown.gif" alt={1903} className="border" border={true} src="https://files.readme.io/d1e460a-ST06_-_Column_Shown.gif" />

* **Step 5: Select Driver:** Click on the **Select Driver** field. Scroll the drop-down menu up and down to find the appropriate driver, or you could directly input the **Username/Full Name** of the desired driver into the search bar, then select from the drop down menu. If you want to export report for all drivers, click on the check box **Choose All Drivers**

<Image title="ST06 - Drivers.gif" alt={1899} border={true} src="https://files.readme.io/19b1249-ST06_-_Drivers.gif">
  Illustration (English)
</Image>

<Image title="ST06 - Drivers (VIE).gif" alt={1899} border={true} src="https://files.readme.io/90ec296-ST06_-_Drivers_VIE.gif">
  Illustration (Vietnamese)
</Image>

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data Type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "No."
      </td>

      <td>
        Numerical order of orders
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Code"
      </td>

      <td>
        Management code of the order
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Code"
      </td>

      <td>
        Management code of the customer
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Name"
      </td>

      <td>
        Name of the customer
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Mobile Number"
      </td>

      <td>
        Mobile number of the customer
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Address"
      </td>

      <td>
        Address of the customer
      </td>

      <td>
        Text and Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Driver Code"
      </td>

      <td>
        Management code of the driver
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Driver Name"
      </td>

      <td>
        Name of the driver
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Vehicle Code"
      </td>

      <td>
        Management code of the vehicle
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Delivery Date"
      </td>

      <td>
        The scheduled execution date of the order
      </td>

      <td>
        Date\
        (Format: YYYY/MM/DD)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Due Date"
      </td>

      <td>
        The actual date on which the order is completed
      </td>

      <td>
        Date\
        (Format: YYYY/MM/DD)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Product Code"
      </td>

      <td>
        Management code of a product loaded in the order
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Product Name"
      </td>

      <td>
        Name of a product loaded in the order
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Product Weight"
      </td>

      <td>
        Weight of a whole case of a product loaded in the order
      </td>

      <td>
        Number
      </td>

      <td>
        Kilogram (kg)
      </td>
    </tr>

    <tr>
      <td>
        "Product Volume"
      </td>

      <td>
        Volume of a whole case of a product loaded in the order
      </td>

      <td>
        Number
      </td>

      <td>
        Cubic metre (m3)
      </td>
    </tr>

    <tr>
      <td>
        "Case Price"
      </td>

      <td>
        Price of a whole case of a product loaded in the order
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit based on the attribute Country configured at the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        "Item Price"
      </td>

      <td>
        Price of a single item of a product loaded in the order
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit based on the attribute Country configured at the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        "Planned Items Delivered"
      </td>

      <td>
        Quantity of single items of a product that have been planned to be delivered
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Actual Items Delivered"
      </td>

      <td>
        Quantity of single items of a product that have been actually delivered
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Planned Cases Delivered"
      </td>

      <td>
        Quantity of whole cases of a product that have been planned to be delivered
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Actual Cases Delivered"
      </td>

      <td>
        Quantity of whole cases of a product that have been actually delivered
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Fulfillment Status"
      </td>

      <td>
        The delivery status of the order at the time the report is generated. Possible values are: Fulfilled; Unfulfilled; Not Yet Fulfillment; Partially Fulfilled
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Notes"
      </td>

      <td>
        Short note attached with the order
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>
  </tbody>
</Table>

## ST07 - Customers and Orders by date and by a single driver

* This report is designed specifically for orders of VRP model

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data Type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Customer Code"
      </td>

      <td>
        Customer code
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Name"
      </td>

      <td>
        Name of the customer
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Address"
      </td>

      <td>
        Customer address
      </td>

      <td>
        Text and Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Organization Code"
      </td>

      <td>
        Organization code of customer
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Last Visit Date"
      </td>

      <td>
        The delivery date that is closest to the date at which users export the report ST07.
      </td>

      <td>
        Date\
        (Format: YYYY-MM-DD)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Number of Orders"
      </td>

      <td>
        Total Number of orders assigned to a driver within a selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Total Revenue"
      </td>

      <td>
        The total revenue generated from the order as planned. Data in this field is gathered directly from the order information
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit based on the attribute Country configured at the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        "Actual Revenue" (\*)
      </td>

      <td>
        The actual total revenue of the order. Data in this field is gathered from the amount that was manually submitted by the driver on the Mobile App.
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit based on the attribute Country configured at the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        "Total Number of Visits"
      </td>

      <td>
        Total number of driver's check-ins in customers' location
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>
  </tbody>
</Table>

* (\*): The data of this field is directly affected by the delivery result that the driver actually submitted on the Mobile App:
* Actual Total Revenue = Planned Total Revenue, if the delivery result was submitted as **Completed**
* Actual Total Revenue \< Planned Total Revenue, if the delivery result was submitted as **Partly Delivered**
* The data cell is left blank, if the delivery result was submitted as **Not Completed**

## ST08 - Trip Utilization By Vehicles

* This report demonstrates the average amount of weight and volume that were utilized per trip by all the vehicles of the organization. This will help you manage your fleet more effectively as it can tell whether there is a vehicle having a low utilization rate so that you can make adjustments. 

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Vehicle Code"
      </td>

      <td>
        Management code of the vehicle
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "License Plate"
      </td>

      <td>
        License plate of the vehicle
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Number of Trips"
      </td>

      <td>
        Number of trips operated by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Vehicle Weight Capacity"
      </td>

      <td>
        The maximum product capacity by weight that the vehicle can carry
      </td>

      <td>
        Number
      </td>

      <td>
        Kilogram (kg)
      </td>
    </tr>

    <tr>
      <td>
        "Vehicle Volume Capacity"
      </td>

      <td>
        The maximum product capacity by volume that the vehicle can carry
      </td>

      <td>
        Number
      </td>

      <td>
        Cubic meter (m3)
      </td>
    </tr>

    <tr>
      <td>
        "Planned Total Weight"
      </td>

      <td>
        The total weight of products that the vehicle was supposed to carry according to plan
      </td>

      <td>
        Number
      </td>

      <td>
        Kilogram (kg)
      </td>
    </tr>

    <tr>
      <td>
        "Planned Total Volume"
      </td>

      <td>
        The total volume of products that the vehicle was supposed to carry according to plan
      </td>

      <td>
        Number
      </td>

      <td>
        Cubic meter (m3)
      </td>
    </tr>

    <tr>
      <td>
        "Weight Utilization"
      </td>

      <td>
        An indicator of how much product weight was carried by the vehicle compared to its capacity per trip
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>

    <tr>
      <td>
        "Volume Utilization"
      </td>

      <td>
        An indicator of how much product volume was carried by the vehicle compared to its capacity per trip
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>
  </tbody>
</Table>

* **Calculation Formula**
* Weight Utilization = (Planned Total Weight / Vehicle Weight Capacity) / Number of Trips x 100%
* Volume Utilization = (Planned Total Volume / Vehicle Volume Capacity) / Number of Trips x 100%

## ST09 - Total Orders By All Vehicles

* Dispatchers can refer to this type of report to see an overview of the orders assigned to each vehicle. In this report, you can know the amount of orders along with their weight and volume in total that each vehicle was in charge of. In addition, the number of orders is also divided into four categories based on the delivery results: **Fulfilled Orders; Partially Fulfilled Orders; Unfulfilled Orders; Not Yet Fulfilled Orders**

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Vehicle Code"
      </td>

      <td>
        Management code of the vehicle
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "License Plate"
      </td>

      <td>
        License plate of the vehicle
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Number of Orders"
      </td>

      <td>
        Number of orders assigned to the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Total Order Weight"
      </td>

      <td>
        Total weight of the orders assigned to the vehicle. Data in this field is gathered from the total weight of the products in those orders
      </td>

      <td>
        Number
      </td>

      <td>
        Kilogram (kg)
      </td>
    </tr>

    <tr>
      <td>
        "Total Order Volume"
      </td>

      <td>
        Total volume of orders assigned to the vehicle. Data in this field is gathered from the total volume of the products in those orders
      </td>

      <td>
        Number
      </td>

      <td>
        Cubic meter (m3)
      </td>
    </tr>

    <tr>
      <td>
        "Fulfilled Orders"
      </td>

      <td>
        Number of orders that have been successfully delivered by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Partially Fulfilled Orders"
      </td>

      <td>
        Number of orders that have been partially delivered by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Unfulfilled Orders"
      </td>

      <td>
        Numbers of orders that have not been delivered successfully by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Not Yet Fulfilled Orders"
      </td>

      <td>
        Number of orders that have not been delivered yet by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>
  </tbody>
</Table>

## ST10 - Total Routes By All Vehicles

* This type of report is used for collecting key statistics of the routes assigned to each vehicle. Those statistics help dispatchers to see if the vehicle went according to plan, considering its traveling distance and time. Notably, they can also be aware of the vehicle's average speed, the time the drivers spent doing their tasks on the Mobile App and the number of times when the check-in location is more than 200 meters away from the store. This report is important when dispatchers want to keep track and know the efficiency of the drivers' daily delivery tasks

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Vehicle Code"
      </td>

      <td>
        Management code of the vehicle
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "License Plate"
      </td>

      <td>
        License plate of the vehicle
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Planned Distance"
      </td>

      <td>
        Distance covered by the vehicle as planned
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Planned Time"
      </td>

      <td>
        Travelling time of the vehicle as planned
      </td>

      <td>
        Number
      </td>

      <td>
        Hour(s)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Distance"
      </td>

      <td>
        Actual distance covered by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Time"
      </td>

      <td>
        Actual travelling time  of the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        Hour(s)
      </td>
    </tr>

    <tr>
      <td>
        "Total Working Time"
      </td>

      <td>
        The duration between the time when the driver submits the "Load Products" task and the time when he submits the "End day" task
      </td>

      <td>
        Number
      </td>

      <td>
        Hour(s)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Average Speed"
      </td>

      <td>
        Actual speed of the vehicle on average
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer per hour (km/h)
      </td>
    </tr>

    <tr>
      <td>
        "Number of Off-200m"
      </td>

      <td>
        Number of times when the distance between the vehicle check-in's location and the store is over 200 meters
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "VFR by Trips"
      </td>

      <td>
        Average Vehicle Fill Rate of all vehicles by all trips (either by weight or volume, the one having the greater value will be displayed)
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>
  </tbody>
</Table>

* **Calculation Formula**
* Actual Average Speed = Actual Distance / Actual Time

## ST11 - Route By Single Vehicle

* This type of report gathers data from a single vehicle. Therefore, after selecting the Date Range, you have to select the vehicle from which you want information

<Image title="Screen Shot 2021-03-15 at 14.32.50.png" alt={2880} src="https://files.readme.io/b0c42b7-Screen_Shot_2021-03-15_at_14.32.50.png">
  Illustration Image (English)
</Image>

<Image title="Screen Shot 2021-03-15 at 14.37.02.png" alt={2880} src="https://files.readme.io/ad3bb74-Screen_Shot_2021-03-15_at_14.37.02.png">
  Illustration Image (Vietnamese)
</Image>

* The purpose of this report is similar to that of the report **ST10 - Routes By All Vehicles**. The only difference is that this report uses the data of a single vehicle based on each of its delivery dates

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "No."
      </td>

      <td>
        Numerical order
      </td>

      <td>
        Number
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        "Delivery Date"
      </td>

      <td>
        Delivery date of the vehicle
      </td>

      <td>
        Date (Format: DD-MM-YY)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Vehicle Code"
      </td>

      <td>
        Management code of the vehicle
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "License Plate"
      </td>

      <td>
        License plate of the vehicle
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Planned Distance"
      </td>

      <td>
        Distance covered by the vehicle as planned
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Planned Travelling Time"
      </td>

      <td>
        Travelling time of the vehicle as planned
      </td>

      <td>
        Number
      </td>

      <td>
        Hour(s)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Distance"
      </td>

      <td>
        Actual distance covered by the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer (km)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Travelling Time"
      </td>

      <td>
        Actual travelling time of the vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        Hour(s)
      </td>
    </tr>

    <tr>
      <td>
        "Actual Average Speed"
      </td>

      <td>
        Actual speed of the vehicle on average
      </td>

      <td>
        Number
      </td>

      <td>
        Kilometer per hour (km/h)
      </td>
    </tr>

    <tr>
      <td>
        "Number of Off-200m"
      </td>

      <td>
        Number of times when the distance between the vehicle check-in's location and the store is over 200 meters
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "VFR by Trips"
      </td>

      <td>
        Average Vehicle Fill Rate of the vehicle by its trips (either by weight or volume, the one having the greater value will be displayed)
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>
    </tr>
  </tbody>
</Table>

* **Calculation Formula**
* Actual Average Speed = Actual Distance / Actual Travelling Time

## ST12 - Order Status

* This type of report displays the detailed information of all the orders within the Date Range you have selected. Apart from the key information of the order such as its weight, volume, time window or fulfillment status , here you can also have a quick overview of who the customer of the order is, which driver is in charge of the order and which vehicle was assigned to deliver the order. Thus, the important objective of the report is to let the dispatchers notice the orders that have not been delivered on time, then they can trace back to the driver who is in charge and find out the possible reasons.

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>

      <th>
        Data type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "No."
      </td>

      <td>
        Numerical order
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Code"
      </td>

      <td>
        Management code of the order
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Route ID"
      </td>

      <td>
        ID code of the route delivered (containing the username of the driver and the order date)
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Code"
      </td>

      <td>
        Management code of the customer
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Name"
      </td>

      <td>
        Name of the customer
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Delivery Date"
      </td>

      <td>
        Delivery date of the vehicle
      </td>

      <td>
        Date (Format: YYYY-MM-DD)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Vehicle Code"
      </td>

      <td>
        Management code of the vehicle
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Driver Code"
      </td>

      <td>
        Username of the driver
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Weight"
      </td>

      <td>
        Weight of the order. Data in this field is gathered from the total weight of the products in the order
      </td>

      <td>
        Number
      </td>

      <td>
        Kilogram (kg)
      </td>
    </tr>

    <tr>
      <td>
        "Order Volume"
      </td>

      <td>
        Volume of the order. Data in this field is gathered from the total volume of the products in the order
      </td>

      <td>
        Number
      </td>

      <td>
        Cubic meter (m3)
      </td>
    </tr>

    <tr>
      <td>
        "Delivery Status"
      </td>

      <td>
        The delivery status of the order at the time the report is generated. Possible values are: Fulfilled; Unfulfilled; Not Yet Fulfillment; Partially Fulfilled
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Delivery Time Window"
      </td>

      <td>
        Delivery time window of the order
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Actual Delivery Time"
      </td>

      <td>
        Actual delivery time of the order
      </td>

      <td>
        Date & time (Format: DD-MM-YY hh:mm)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "On Time (Yes/No)"
      </td>

      <td>
        This field indicates whether the order has been delivered within the time window or not. The data is left blank if the order has not been fulfilled
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>
  </tbody>
</Table>

## ST13 - Balance Sheet By Single Driver

* You have to select a driver before downloading this type of report as it only uses the data of a single driver

<Image title="Screen Shot 2021-03-15 at 14.49.05.png" alt={2880} src="https://files.readme.io/6bab27d-Screen_Shot_2021-03-15_at_14.49.05.png">
  Illustration Image (English)
</Image>

<Image title="Screen Shot 2021-03-15 at 14.47.57.png" alt={2880} src="https://files.readme.io/f80e570-Screen_Shot_2021-03-15_at_14.47.57.png">
  Illustration Image (Vietnamese)
</Image>

* Dispatchers use this type of report to know the amount of money actually collected by each driver compared to the plan. This is crucial for cases when the amount of cash collected is not equal to the amount that drivers are supposed to collect. The dispatchers can know the cause for those cases based on the delivery status of the order, or they can look into more detail by contacting the driver in charge of the order as the information of the drivers and salesmen are also stated in this report

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Description
      </th>

      <th>
        Data Type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "No."
      </td>

      <td>
        Numerical order
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Date"
      </td>

      <td>
        The date on which the order needs to be delivered
      </td>

      <td>
        Date\
        (Format: YYYY-MM-DD)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Implementation Date"
      </td>

      <td>
        The date on which the driver actually started submitting tasks of the order on the Mobile app.Data in this field will be blank if those tasks are not submitted by the driver
      </td>

      <td>
        Date\
        (Format: YYYY-MM-DD)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Driver Code"
      </td>

      <td>
        Management code of the driver
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Driver Name"
      </td>

      <td>
        Name of the driver
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Code"
      </td>

      <td>
        Management code of the customer
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Name"
      </td>

      <td>
        Name of the customer
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Code"
      </td>

      <td>
        Management code of the driver
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Salesman Code"
      </td>

      <td>
        Management code of the salesman who placed the order
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Planned Total Revenue"
      </td>

      <td>
        The total revenue generated from the order as planned. Data in this field is gathered directly from the order information
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit based on the attribute Country configured at the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        "Actual Total Revenue" (\*)
      </td>

      <td>
        The actual total revenue of the order. Data in this field is gathered from the amount that was manually submitted by the driver on the Mobile App.
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit based on the attribute Country configured at the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        "Fulfillment Status"
      </td>

      <td>
        The delivery status of the order at the time the report is generated. Possible values are: Fulfilled; Unfulfilled; Not Yet Fulfillment; Partially Fulfilled
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Unfulfilled Reason"
      </td>

      <td>
        The reason why the order could not be delivered to the customer (If that happens). Data in this field is taken from the reason that the driver selected on the Mobile App
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>
  </tbody>
</Table>

* (\*): The data of this field is directly affected by the delivery result that the driver actually submitted on the Mobile App:
* Actual Total Revenue = Planned Total Revenue, if the delivery result was submitted as **Completed**
* Actual Total Revenue \< Planned Total Revenue, if the delivery result was submitted as **Partly Delivered**
* The data cell is left blank, if the delivery result was submitted as **Not Completed**

## ST14 - Delivery Statistics

* To download this type of report, after selecting the Date Range, you have to select Salesman in order for the report to gather data information of the salesman who placed the order. You can also tick the **Choose All Salesman** checkbox to gather data of all the salesmen who placed the orders within the chosen Date Range

<Image title="Screen Shot 2021-03-15 at 14.49.29.png" alt={2880} src="https://files.readme.io/51d50fe-Screen_Shot_2021-03-15_at_14.49.29.png">
  Illustration Image (English)
</Image>

<Image title="Screen Shot 2021-03-15 at 14.50.17.png" alt={2880} src="https://files.readme.io/16c9cd2-Screen_Shot_2021-03-15_at_14.50.17.png">
  Illustration Image (Vietnamese)
</Image>

* This type of report will help dispatchers be aware of which order was placed by which salesman as well as the revenue generated from that order. Therefore, it will be easier to keep track of the sales figures and assess the KPIs of each salesman

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Description
      </th>

      <th>
        Data Type
      </th>

      <th>
        Unit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "No."
      </td>

      <td>
        Numerical order
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Date"
      </td>

      <td>
        The date on which the order needs to be delivered
      </td>

      <td>
        Date (Format: YYYY-MM-DD)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Implementation Date"
      </td>

      <td>
        The date on which the driver actually started submitting tasks of the order on the Mobile app.Data in this field will be blank if those tasks are not submitted by the driver
      </td>

      <td>
        Date\
        (Format: YYYY-MM-DD)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Salesman Code"
      </td>

      <td>
        Management code of the salesman who placed the order
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Order Code"
      </td>

      <td>
        Management code of the order
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Planned Revenue"
      </td>

      <td>
        The total revenue generated from the order as planned. Data in this field is gathered directly from the order information
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit based on the attribute Country configured at the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        "Customer Code"
      </td>

      <td>
        Management code of the customer
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Customer Name"
      </td>

      <td>
        Name of the customer
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Driver Code"
      </td>

      <td>
        Management code of the driver
      </td>

      <td>
        String (text, number and special characters)
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        "Driver Name"
      </td>

      <td>
        Name of the driver
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>
    </tr>
  </tbody>
</Table>
