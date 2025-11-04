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

* You need to enable the **Reports** configurations at both the **Manufacturer** and the **Branch**
* You need to enable the module **Report** for the User group. Refer to this article: [Manage Users](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#manufacturer-administrator-user-group)

## Locate Report tab

* Navigate to **Reports > Report** tab

<Image title="1. Reports (ENG).png" alt={1400} border={true} src="https://files.readme.io/818ddc0-1._Reports_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Reports (VIE).png" alt={1331} border={true} src="https://files.readme.io/7680505-1._Reports_VIE.png">
  Illustration (Vietnamese)
</Image>

* This tab is where you can generate and export reports

## General steps to generate and export report

* To generate and export the Reports, please follow the steps 
* Step 1: Click on **Report Type** field, select this report from the drop-down menu

<Image title="2. Reports (ENG).png" alt={1382} border={true} src="https://files.readme.io/2d2505b-2._Reports_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Reports (VIE).png" alt={1168} border={true} src="https://files.readme.io/e024df5-2._Reports_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 2: Select the date range: Click on the field below the text Date Range, select the appropriate date range from the drop-down calendars, then click on **Apply** to confirm selecting the date range. Alternatively, you could input the date range directly into the field in the following format: **yyyy-mm-dd:yyyy-mm-dd (Year-Month-Date:Year-Month-Date)**

<Image title="3. Date Range (ENG).png" alt={1133} border={true} src="https://files.readme.io/82179ba-3._Date_Range_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Date Range (VIE).png" alt={1209} border={true} src="https://files.readme.io/e1eb60b-3._Date_Range_VIE.png">
  Illustration (Vietnamese)
</Image>

* If your selected date range exceeds 31 days, there will be an error message as below. In this case, please select another date range.

<Image title="7. Duration (ENG).png" alt={1711} border={true} src="https://files.readme.io/4538c6b-7._Duration_ENG.png">
  Illustration (English)
</Image>

<Image title="7. Duration (VIE).png" alt={1728} border={true} src="https://files.readme.io/802a9a7-7._Duration_VIE.png">
  Illustration (Vietnamese)
</Image>

* Note: If the language for display is a language other than Vietnamese (for example, English, Indonesian, Japanese...), the default language of reports is English.

* Step 3: Select whether there will be a header in the Report or not 

* By default, you will see a toggle button :fa-toggle-off: named **Exclude Report Header**. When you leave this button off, there will not be a header of the report name and the date range

* If you want to add the report name and the date range to the report, click on that switch button. When the button changes to :fa-toggle-on:, the text will change to **Include Report Header**, which means in the report there will be a header of the report name and the date range, as in screenshots below

<Image title="7. Title (ENG).png" alt={1920} border={true} src="https://files.readme.io/424d58c-7._Title_ENG.png">
  Illustration (English)
</Image>

<Image title="7. Title (VIE).png" alt={1920} border={true} src="https://files.readme.io/06d5e7a-7._Title_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 4: Download the report: 
* Click on the button **Download** :fa-download:. The system will immediately start gathering data based on your filters, and will generate a downloadable Excel template shortly

<Image title="4. Download Button (VIE).png" alt={976} border={true} src="https://files.readme.io/273875a-4._Download_Button_VIE.png">
  Illustration (English)
</Image>

<Image title="4. Download Button (VIE).png" alt={976} border={true} src="https://files.readme.io/d056c74-4._Download_Button_VIE.png">
  Illustration (Vietnamese)
</Image>

## ST15 - Products and Tasks by PDP Orders

* Below is the list of all information fields in the report

<Table align={["left","left","left","left","left","left"]}>
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

      <th>
        Possible Values
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        No.
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

      <td>
        *
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        Order Code
      </td>

      <td>
        Code of the order
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        SO-190829-0001
      </td>
    </tr>

    <tr>
      <td>
        Order Date
      </td>

      <td>
        The date when the order was delivered
      </td>

      <td>
        Date\
        Format: Year-Month-Date (yyyy-mm-dd)
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        2019-05-08
      </td>
    </tr>

    <tr>
      <td>
        Driver Name
      </td>

      <td>
        Name of the driver who delivered the order
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        John Doe
      </td>
    </tr>

    <tr>
      <td>
        Truck Plate No.
      </td>

      <td>
        Plate numbers of the truck used to deliver the order
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        31K3-5152
      </td>
    </tr>

    <tr>
      <td>
        Truck Type
      </td>

      <td>
        Type of the truck used to deliver the order
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        Twelve wheels truck
      </td>
    </tr>

    <tr>
      <td>
        Origin Customer Name
      </td>

      <td>
        Name of the origin customer, from where the products were picked up
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        John Doe company
      </td>
    </tr>

    <tr>
      <td>
        Origin Customer Address
      </td>

      <td>
        Address of the origin customer, from where the products were picked up
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        1st road, valley A, city B, country C
      </td>
    </tr>

    <tr>
      <td>
        Destination Customer Name
      </td>

      <td>
        Name of the destination customer, to where the products were delivered
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        John Doe company
      </td>
    </tr>

    <tr>
      <td>
        Destination Customer Address
      </td>

      <td>
        Address of the destination customer, to where the products were delivered
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        1st road, valley A, city B, country C
      </td>
    </tr>

    <tr>
      <td>
        SKU
      </td>

      <td>
        The product loaded in the order
      </td>

      <td>
        Text & Number\
        Format: (Product Code) Product Name
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        (Product\_A\_Code) Product A Name
      </td>
    </tr>

    <tr>
      <td>
        Quantity
      </td>

      <td>
        Quantity of the product loaded in the order
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        100
      </td>
    </tr>

    <tr>
      <td>
        Quantity Type
      </td>

      <td>
        Unit type of the product loaded in the order
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        Pallet; Case; Item etc.
      </td>

      <td>
        Pallet
      </td>
    </tr>

    <tr>
      <td>
        Check By
      </td>

      <td>
        Name of the personnel who checked the order
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        John Doe
      </td>
    </tr>

    <tr>
      <td>
        Fulfillment Status
      </td>

      <td>
        Delivery result of the order at the time the report was generated
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        Fulfilled; Partially fulfilled; Not Yet Fulfillment; Unfulfilled
      </td>

      <td>
        Fulfilled
      </td>
    </tr>

    <tr>
      <td>
        Distance Difference (m)
      </td>

      <td>
        The distance that the driver actually traveled from the Origin Customer to the Destination Customer
      </td>

      <td>
        Number (Decimal)
      </td>

      <td>
        m (Meter)
      </td>

      <td>
        *
      </td>

      <td>
        90000.4
      </td>
    </tr>

    <tr>
      <td>
        Trip Hours
      </td>

      <td>
        The time duration during which the order was performed
      </td>

      <td>
        Time\
        Format: Hour:Minute:Second (hh:mm:ss)
      </td>

      <td>
        *
      </td>

      <td>

      </td>

      <td>
        40:36:30
      </td>
    </tr>

    <tr>
      <td>
        Arrival check-in Date/Time
      </td>

      <td>
        The specific Date and Time when the driver arrived at the Destination Customer location
      </td>

      <td>
        Date/Time\
        Format: Year-Month-Date Hour:Minute:Second (yyyy-mm-dd hh:mm:ss)
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        2019-05-08 09:06:06
      </td>
    </tr>

    <tr>
      <td>
        Unloading start check-in Date/Time
      </td>

      <td>
        The specific Date and Time the Unloading task started at the Destination Customer location
      </td>

      <td>
        Date/Time\
        (yyyy-mm-dd hh:mm:ss)

        (Year-Month-Date Hour:Minute:Second)
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        2019-05-08 09:06:06
      </td>
    </tr>

    <tr>
      <td>
        Signature Status
      </td>

      <td>
        The status of the customer signing digitally upon receiving the products
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        Signed; Not Yet
      </td>

      <td>
        Signed
      </td>
    </tr>

    <tr>
      <td>
        Signature Sign-on date
      </td>

      <td>
        The date on which the customer digitally signed upon receiving the products
      </td>

      <td>
        Date\
        Format: Year-Month-Date (yyyy-mm-dd)
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        2019-05-08
      </td>
    </tr>

    <tr>
      <td>
        Email Sending Status
      </td>

      <td>
        The status of sending email enclosed with the Proof of Delivery
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        Not yet; Sent
      </td>

      <td>
        Sent
      </td>
    </tr>
  </tbody>
</Table>

## ST21 - Orders By Drivers

* Below is the list of all information fields in the report

<Table align={["left","left","left","left","left","left"]}>
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

      <th>
        Possible Values
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        No.
      </td>

      <td>
        Numerical order of the driver
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        Driver Code
      </td>

      <td>
        Management code of the driver
      </td>

      <td>
        Text, Number, Special characters
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        Driver01
      </td>
    </tr>

    <tr>
      <td>
        Driver Name
      </td>

      <td>
        Name of the driver
      </td>

      <td>
        Text, Number, Special characters
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        Bui Anh Tuan
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Type
      </td>

      <td>
        The vehicle type operated by the driver
      </td>

      <td>
        Text, Number, Special characters
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        vehicle\_type\_1
      </td>
    </tr>

    <tr>
      <td>
        Number Of Orders
      </td>

      <td>
        Number of sales orders delivered by the driver
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        4
      </td>
    </tr>

    <tr>
      <td>
        Total Order Weight (kg)
      </td>

      <td>
        Total weight of all Orders delivered by the driver during the selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        Kilogram (kg)
      </td>

      <td>
        *
      </td>

      <td>
        5.5
      </td>
    </tr>

    <tr>
      <td>
        Total Order Volume (m3)
      </td>

      <td>
        Total volume of all Orders delivered by the driver during the selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        Cubic metre (m3)
      </td>

      <td>
        *
      </td>

      <td>
        5.5
      </td>
    </tr>

    <tr>
      <td>
        Planned Revenue
      </td>

      <td>
        The projected revenue of all Orders planned to be delivered by the driver during the selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit\
        (Based on the Currency configuration at the Manufacturer)
      </td>

      <td>
        *
      </td>

      <td>
        5.5
      </td>
    </tr>

    <tr>
      <td>
        Planned Cost
      </td>

      <td>
        The projected cost of all Delivery Routes planned to be performed by the driver during the selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit\
        (Based on the Currency configuration at the Manufacturer)
      </td>

      <td>
        *
      </td>

      <td>
        5.5
      </td>
    </tr>

    <tr>
      <td>
        Planned Distance (km)
      </td>

      <td>
        The projected distance of all Delivery Routes planned to be performed by the driver during the selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        Kilomet (km)
      </td>

      <td>
        *
      </td>

      <td>
        5.5
      </td>
    </tr>

    <tr>
      <td>
        Planned Time (hours)
      </td>

      <td>
        The projected time period to perform all Delivery Routes assigned to the driver during the selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        Hour (h)
      </td>

      <td>
        *
      </td>

      <td>
        5.5
      </td>
    </tr>

    <tr>
      <td>
        Actual Revenue
      </td>

      <td>
        The actual revenue received by the driver during the selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit\
        (Based on the Currency configuration at the Manufacturer)
      </td>

      <td>
        *
      </td>

      <td>
        5.5
      </td>
    </tr>

    <tr>
      <td>
        Actual Cost
      </td>

      <td>
        The actual cost of all Delivery Routes performed by the driver during the selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit\
        (Based on the Currency configuration at the Manufacturer)
      </td>

      <td>
        *
      </td>

      <td>
        5.5
      </td>
    </tr>

    <tr>
      <td>
        Actual Distance (km)
      </td>

      <td>
        The actual distance of all Delivery Routes performed by the driver during the selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        Kilomet (km)
      </td>

      <td>
        *
      </td>

      <td>
        42.3
      </td>
    </tr>

    <tr>
      <td>
        Actual Time (hours)
      </td>

      <td>
        The actual delivery time period of the driver during the selected date range\
        This time period is calculated by subtracting the Check-in time of the first task from the Check-out time of the last task on the Mobile app during the selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        Hour (h)
      </td>

      <td>
        *
      </td>

      <td>
        4.4
      </td>
    </tr>

    <tr>
      <td>
        VFR By Weight (%)
      </td>

      <td>
        The avarage vehicle fill rate (By weight) of all Delivery Routes actually performed by the vehicle during the selected date range
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>

      <td>
        *
      </td>

      <td>
        0
      </td>
    </tr>

    <tr>
      <td>
        Fulfilled Orders (#)
      </td>

      <td>
        Number of Orders that were delivered and have the delivery result as "Completed" at the time the report is exported
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        4.3
      </td>
    </tr>

    <tr>
      <td>
        Partially Fulfilled Orders (#)
      </td>

      <td>
        Number of Orders that were delivered and have the delivery result as "Partly Delivered" at the time the report is exported
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        4
      </td>
    </tr>

    <tr>
      <td>
        Unfulfilled Orders (#)
      </td>

      <td>
        Number of Orders that were delivered and have the delivery result as "Not Completed" at the time the report is exported
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        4
      </td>
    </tr>

    <tr>
      <td>
        Not Yet Fulfilled Orders (#)
      </td>

      <td>
        Number of Orders that have been put on optimized Delivery Routes, but were not yet delivered at the time the report is exported
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        4
      </td>
    </tr>

    <tr>
      <td>
        Number of Off-200m Check-in (#)
      </td>

      <td>
        The number of when the driver submitted the Check-in task outside the 200 meter range from the Customer locations
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        4
      </td>
    </tr>
  </tbody>
</Table>

* Note:
* At the moment, the VFR (By both weight and volume) of PDP Models hasn't been formulated yet, therefore the column **VFR By Weight (%)** will have no value
* For this model, all Orders are considered to always be successfully delivered, therefore the two columns **Partially Fulfilled Orders (#)** and **Unfulfilled Orders (#)** will have no value

## ST22 - PDP KPI Scoreboard

* Below is the list of all information fields in the report

<Table align={["left","left","left","left","left","left"]}>
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

      <th>
        Possible Values
      </th>

      <th>
        Example
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

      <td>
        *
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        Delivery Date
      </td>

      <td>
        The date when the order was performed
      </td>

      <td>
        Date\
        Format: Year-Month-Date (yyyy-mm-dd)
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        2019-10-03
      </td>
    </tr>

    <tr>
      <td>
        Truck Utilization (%)
      </td>

      <td>
        The ratio of the number of trucks used during the selected date range over the total number of all available trucks
      </td>

      <td>
        Number
      </td>

      <td>
        percentage (%)
      </td>

      <td>
        *
      </td>

      <td>
        9.09
      </td>
    </tr>

    <tr>
      <td>
        Service Level (%)
      </td>

      <td>
        The ratio of the number of delivered orders over the number of planned orders of all drivers
      </td>

      <td>
        Number
      </td>

      <td>
        percentage (%)
      </td>

      <td>
        *
      </td>

      <td>
        33.33
      </td>
    </tr>

    <tr>
      <td>
        Driver Adoption (%)
      </td>

      <td>
        The ratio of the number of drivers who have used Abivin App over the total number of drivers
      </td>

      <td>
        Number
      </td>

      <td>
        percentage (%)
      </td>

      <td>
        *
      </td>

      <td>
        9.09
      </td>
    </tr>

    <tr>
      <td>
        Compliance Driver (%)
      </td>

      <td>
        The ratio of Executed Tasks over Planned tasks of all drivers
      </td>

      <td>
        Number
      </td>

      <td>
        percentage (%)
      </td>

      <td>
        *
      </td>

      <td>
        42.86
      </td>
    </tr>

    <tr>
      <td>
        Delivery GPS Compliance
      </td>

      <td>
        The ratio of the number of correctly submitted Check-in tasks (In the distance of 200 meters from the customer location) over the total Number of Check-in tasks submitted by all drivers
      </td>

      <td>
        Number
      </td>

      <td>
        percentage (%)
      </td>

      <td>
        *
      </td>

      <td>
        52.7
      </td>
    </tr>

    <tr>
      <td>
        Planned Distance (km)
      </td>

      <td>
        The total planned distance of all vehicles
      </td>

      <td>
        Number
      </td>

      <td>
        kilometer (km)
      </td>

      <td>
        *
      </td>

      <td>
        122.89
      </td>
    </tr>

    <tr>
      <td>
        Actual Distance (km)
      </td>

      <td>
        The total actual distance traveled by all vehicles
      </td>

      <td>
        Number
      </td>

      <td>
        kilometer (km)
      </td>

      <td>
        *
      </td>

      <td>
        101.1
      </td>
    </tr>

    <tr>
      <td>
        Kilometer Actual (Ratio)
      </td>

      <td>
        The ratio of Actual Distance over Planned Distance of all vehicles
      </td>

      <td>
        Number
      </td>

      <td>
        percentage (%)
      </td>

      <td>
        *
      </td>

      <td>
        34.3
      </td>
    </tr>
  </tbody>
</Table>

## ST23 - PDP Orders by a single driver

### Steps to Export the Report ST23

* Step 1: Click on **Report Type** field, select this report from the drop-down menu

<Image title="st 23 (ENG).png" alt={771} border={true} src="https://files.readme.io/74af285-st_23_ENG.png">
  Illustration (English)
</Image>

<Image title="Select (VIE).png" alt={758} border={true} src="https://files.readme.io/bf75743-Select_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 2: Click on **Date Range** field, select the suitable date range from the drop down calendars

<Image title="1. ST23 (ENG).png" alt={1551} border={true} src="https://files.readme.io/0333b9d-1._ST23_ENG.png">
  Illustration (English)
</Image>

<Image title="1. ST23 (VIE).png" alt={1546} border={true} src="https://files.readme.io/c818f56-1._ST23_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 3: Next, click on **Select drivers** field, select the driver for whom you want to export report from the drop-down menu. You can select multiple drivers at once

<Image title="8. Select (ENG).png" alt={1574} border={true} src="https://files.readme.io/6efdc92-8._Select_ENG.png">
  Illustration (English)
</Image>

<Image title="8. Select (VIE).png" alt={1574} src="https://files.readme.io/71f655d-8._Select_VIE.png">
  Illustration (Vietnamese)
</Image>

* If you want to export report for all drivers, click on **Choose All Drivers** check box

<Image title="9. All (ENG).png" alt={1458} border={true} src="https://files.readme.io/1ccd0ec-9._All_ENG.png">
  Illustration (English)
</Image>

<Image title="9. All (VIE).png" alt={1481} border={true} src="https://files.readme.io/5de3236-9._All_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 4: Finally, click on **Download** button. The system will immediately gather data and export the report into a downloadable Excel template after a short moment
* (Optional) If you want to include a header in the Excel template, you can click on the toggle button **Exclude Report Header** :fa-toggle-off:. When that button changes to **Include Report Header** :fa-toggle-on:, in the Excel template there will be a header

<Image title="3. ST23 - Meerge (ENG).png" alt={1920} border={true} src="https://files.readme.io/b7ed081-3._ST23_-_Meerge_ENG.png">
  Illustration (English)
</Image>

<Image title="9. ST23 (Merge) (VIE).png" alt={1920} border={true} src="https://files.readme.io/dceba75-9._ST23_Merge_VIE.png">
  Illustration (Vietnamese)
</Image>

### Report ST23 - Information fields

* Below is the list of all information fields in the report

<Table align={["left","left","left","left","left","left"]}>
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

      <th>
        Possible values
      </th>

      <th>
        Examples
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        No.
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

      <td>
        *
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        Order Date
      </td>

      <td>
        The date when the order was performed
      </td>

      <td>
        Date\
        Format: Year-Month-Date (yyyy-mm-dd)
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        2019-09-22
      </td>
    </tr>

    <tr>
      <td>
        Driver Code
      </td>

      <td>
        Code of the driver who delivered the order
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        Driver\_01
      </td>
    </tr>

    <tr>
      <td>
        Driver Name
      </td>

      <td>
        Name of the driver who delivered the order
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        John Doe
      </td>
    </tr>

    <tr>
      <td>
        Customer Code
      </td>

      <td>
        Code of the customer who placed the order
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        Customer\_01
      </td>
    </tr>

    <tr>
      <td>
        Customer Name
      </td>

      <td>
        Name of the customer who placed the order
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        John Doe
      </td>
    </tr>

    <tr>
      <td>
        Customer Address
      </td>

      <td>
        Address of the customer who placed the order
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        100 Doc Ngu, Hanoi, Vietnam
      </td>
    </tr>

    <tr>
      <td>
        Order code
      </td>

      <td>
        Code of the order
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        SO\_001
      </td>
    </tr>

    <tr>
      <td>
        Order status
      </td>

      <td>
        Execution status of the order at the time the report was generated
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        Open; Shipped
      </td>

      <td>
        Open
      </td>
    </tr>

    <tr>
      <td>
        Planned Total revenue
      </td>

      <td>
        Total revenue of the order as planned
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit (VND; MMK; Rp etc.)
      </td>

      <td>
        *
      </td>

      <td>
        10000000
      </td>
    </tr>

    <tr>
      <td>
        Actual Total Revenue
      </td>

      <td>
        Total Revenue of the order as actually performed
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit (VND; MMK; Rp etc.)
      </td>

      <td>
        *
      </td>

      <td>
        8000000
      </td>
    </tr>

    <tr>
      <td>
        Fulfillment Status
      </td>

      <td>
        Delivery result of the order at the time the report was generated
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        Fulfilled; Partially fulfilled; Not Yet Fulfillment; Unfulfilled
      </td>

      <td>
        Not Yet Fulfillment
      </td>
    </tr>

    <tr>
      <td>
        Order Unfulfilled Reason
      </td>

      <td>
        Reason the order was not delivered successfully
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        Customer has closed
      </td>
    </tr>

    <tr>
      <td>
        Customer Lat
      </td>

      <td>
        Latitude of the customer location
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        21.044640
      </td>
    </tr>

    <tr>
      <td>
        Customer Long
      </td>

      <td>
        Longitude of the customer location
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        105.813726
      </td>
    </tr>

    <tr>
      <td>
        Checkin Lat
      </td>

      <td>
        Latitude of the location where the driver submitted the check in task
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        21.044640
      </td>
    </tr>

    <tr>
      <td>
        Check-in Long
      </td>

      <td>
        Longitude of the location where the driver submitted the check in task
      </td>

      <td>
        Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        105.813726
      </td>
    </tr>

    <tr>
      <td>
        Distance Difference (m)
      </td>

      <td>
        The distance between the location where the driver submitted the 'Check in' task and the actual customer location
      </td>

      <td>
        Number
      </td>

      <td>
        m (meter)
      </td>

      <td>
        *
      </td>

      <td>
        20
      </td>
    </tr>

    <tr>
      <td>
        Task Name
      </td>

      <td>
        The most recent task on Mobile app of the driver at the time the report was exported
      </td>

      <td>
        Text & Number
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        4. John Doe
      </td>
    </tr>

    <tr>
      <td>
        Signature Status
      </td>

      <td>
        Specify whether the customer has signed digitally upon receiving the products or not
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        Not yet; Signed
      </td>

      <td>
        Signed
      </td>
    </tr>

    <tr>
      <td>
        Email Sending Status
      </td>

      <td>
        Specify whether the Delivery Note email enclosed with the Proof of Delivery has been sent to the customer or not
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        Not yet; Sent
      </td>

      <td>
        Sent
      </td>
    </tr>
  </tbody>
</Table>
