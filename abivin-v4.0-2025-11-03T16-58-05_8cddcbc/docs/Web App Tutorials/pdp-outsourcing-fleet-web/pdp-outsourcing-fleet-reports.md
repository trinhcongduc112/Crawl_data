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
## Locate Report tab

* Navigate to **Reports > Report** tab
* This tab is where you can generate and export reports

## General steps to generate and export report

* **Step 1: Select the report:** Click on the field **Report Type**. Select the appropriate report from the drop down list

<Image title="HcwM8hyt5D.png" alt={337} className="border" border={true} src="https://files.readme.io/4306964-HcwM8hyt5D.png" />

* **Step 2: Select the date range:** Click on the field below the text **Date Range**. Select the appropriate date range from the drop down calendars, then click on **Apply** to confirm selecting the date range. Alternatively, you could input the date range directly into the field in the following format: ***yyyy-mm-dd:yyyy-mm-dd***

> 📘 If the selected date range spans more than ***31 days***, then instead of being directly downloadable from the Web app, the report will be sent to the email address associated with the account which export that report

<Image title="sZUsBsa2Nn.png" alt={912} className="border" border={true} src="https://files.readme.io/c4b788b-sZUsBsa2Nn.png" />

* **Step 3: Select whether there will be header in the report or not**: By default, you will see a toggle button :fa-toggle-off: that reads **Exclude Report Header**. That means in the downloaded Excel spreadsheet, there will not be a header mentioning the report name and the date range
* If you want to add the report name and the date range to the report, click on that switch button. When the button changes to :fa-toggle-on:, the text will change to **Include Report Header**, which means in the report there will be a header of the report name and the date range, like below

![1901](https://files.readme.io/feb4ff8-Selection_003.png "Selection_003.png")

* **Step 4: Download the report:** Click on the button **Download** :fa-download:. The system will immediately start gathering data based on your filters, and will generate a downloadable Excel spreadsheet shortly

<Image title="CZB8PDp7UH.png" alt={699} className="border" border={true} src="https://files.readme.io/c914789-CZB8PDp7UH.png" />

## ST15 - Products and Tasks by PDP Orders

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

## ST16 - Transport Service Cost by PDP Orders

* This report will keep track of the Transport Service cost of PDP Orders paid by particular Depots, delivered by particular Transporters during a certain date range

### Report ST16 - Export instruction

* Click on **Report Type** field, select this report from the drop down menu
* Next, click on **Created Date** field. From the drop down calendars, select the date range during which the Orders were created
* Then, click on **Delivery Date** field. From the drop down calendars, select the date range during which the Orders were actually delivered to the destination locations

<Image title="Selection_002.png" alt={1892} className="border" border={true} src="https://files.readme.io/88a00dd-Selection_002.png" />

* Click on the field **Select Service Payer**. On the drop down list, click on the search bar, input the **Organization Name** of the appropriate Depot and select the returned value. Repeat these steps to select more Depots
* Continue to click on the field **Select transporter**. On the drop down list, click on the search bar, input the **Organization Name** of the appropriate Transporter and select the returned value. Repeat these steps to select more Transporters
* Finally, click on **Download** button. The system will immediately gather data and generate a downloadable Excel spreadsheet to view offline
* (Optional) If you want to include a header in the Excel spreadsheet, you can click on the toggle button **Exclude Report Header** :fa-toggle-off:. When that button changes to **Include Report Header** :fa-toggle-on:, in the Excel spreadsheet there will be a header

<Image title="Selection_003.png" alt={1901} className="border" border={true} src="https://files.readme.io/15af36e-Selection_003.png" />

### Report ST16 - Information fields

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
        Numerical order of the Sales order
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
        Management code of the Sales order
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
        S.O.#1
      </td>
    </tr>

    <tr>
      <td>
        Branch Name
      </td>

      <td>
        Name of the Branch that managed the Sales order
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
        Branch A1
      </td>
    </tr>

    <tr>
      <td>
        Product Name
      </td>

      <td>
        Name of the product loaded in the Sales order
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
        Product A1
      </td>
    </tr>

    <tr>
      <td>
        Origin Pickup
      </td>

      <td>
        Name of the Origin Depot, where the Transporter vehicle will pick up products
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
        Depot A1
      </td>
    </tr>

    <tr>
      <td>
        Destination Delivery
      </td>

      <td>
        Name of the Destination Depot, where the Transporter vehicle will drop off products
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
        Depot A1
      </td>
    </tr>

    <tr>
      <td>
        Transporter
      </td>

      <td>
        Name of the Transporter which have been selected to deliver the order
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
        Transporter A1
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Type
      </td>

      <td>
        The vehicle type that have been selected to deliver the order
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
        Vehicle Type A1
      </td>
    </tr>

    <tr>
      <td>
        Transporter Service Price
      </td>

      <td>
        The original transport service price of the order\
        This field will have a value larger than zero if the Order is the first Order on the Delivery Route of the assigned vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit\
        For example: VND
      </td>

      <td>
        *
      </td>

      <td>
        4500000
      </td>
    </tr>

    <tr>
      <td>
        After Discount Rate
      </td>

      <td>
        The rate (After subtracting the fixed discount rate of 15%) to be multiplied with the original transport service price rate in order to calculate the discounted transport service price of the order\
        This field will have a value if the Order is not the first Order on the Delivery Route of the assigned vehicle
      </td>

      <td>
        Number
      </td>

      <td>
        Percentage (%)
      </td>

      <td>
        85%
      </td>

      <td>
        85%
      </td>
    </tr>

    <tr>
      <td>
        Surcharge
      </td>

      <td>
        The transport service surcharge of the order (If applicable)\
        This field will have a value if the Order is not the first Order on the Delivery Route of the assigned vehicle\
        The value in this field will be the same value under the column "Surcharge" of the Order on the form "Optimization Result" during the Route Plan optimization process
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit\
        For example: VND
      </td>

      <td>
        500000\
        1000000
      </td>

      <td>
        500000
      </td>
    </tr>

    <tr>
      <td>
        Total Service Price
      </td>

      <td>
        Total Transport service price of the Order\
        The value in this field is the same value under the column "Amount" of that exact Order on the form "Optimization Result" during the Route Plan optimization process
      </td>

      <td>
        Number
      </td>

      <td>
        Currency unit\
        For example: VND
      </td>

      <td>
        *
      </td>

      <td>
        234000
      </td>
    </tr>

    <tr>
      <td>
        License Plate
      </td>

      <td>
        License plate numbers of the vehicle that delivered the order
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
        30K3-5155
      </td>
    </tr>

    <tr>
      <td>
        Driver Name
      </td>

      <td>
        Name of the driver who operated the delivery vehicle
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
        Driver Phone Number
      </td>

      <td>
        Phone number of the driver
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
        012345678
      </td>
    </tr>

    <tr>
      <td>
        Order Creation Date
      </td>

      <td>
        The date on which the order was created
      </td>

      <td>
        Date\
        Format: Date/Month/Year (dd/mm/yyyy)
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        30/01/2020
      </td>
    </tr>

    <tr>
      <td>
        Due date
      </td>

      <td>
        The planned date on which the order is supposed to be completed\
        The value in this field is the same as the value input into the field "Date" of the Order
      </td>

      <td>
        Date\
        Format: Date/Month/Year (dd/mm/yyyy)
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        30/01/2020
      </td>
    </tr>

    <tr>
      <td>
        Actual Delivery Time
      </td>

      <td>
        The date on which the Order is actually delivered to the Destination Depot
      </td>

      <td>
        Date\
        Format: Date/Month/Year (dd/mm/yyyy)
      </td>

      <td>
        *
      </td>

      <td>
        *
      </td>

      <td>
        30/01/2020
      </td>
    </tr>

    <tr>
      <td>
        Planning Status
      </td>

      <td>
        Planning status of the Order at the time the report was exported
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        Approved\
        Not Submitted\
        Routed\
        Submitted
      </td>

      <td>
        Approved
      </td>
    </tr>

    <tr>
      <td>
        Origin Shipping Status
      </td>

      <td>
        Status of the Origin Depot's warehouseman handing products to the Transporter's driver at the time the report was exported
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        NOT FULFILLED\
        SHIP FULFILLED\
        SHIP PARTIALLY (LESS)\
        SHIP PARTIALLY (MORE)\
        SHIP UNFULFILLED
      </td>

      <td>
        SHIP FULFILLED
      </td>
    </tr>

    <tr>
      <td>
        Origin Pickup Status
      </td>

      <td>
        Status of the Transporter's driver picking up products at the Origin Depot at the time the report was exported
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        NOT FULFILLED\
        PICKUP FULFILLED\
        PICKUP PARTIALLY (LESS)\
        PICKUP PARTIALLY (MORE)\
        PICKUP UNFULFILLED
      </td>

      <td>
        PICKUP FULFILLED
      </td>
    </tr>

    <tr>
      <td>
        Destination Receiving Status
      </td>

      <td>
        Status of the Destination Depot's warehouseman receiving products from the Transporter's driver at the time the report was exported
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        NOT FULFILLED\
        RECEIVE FULFILLED\
        RECEIVE PARTIALLY (LESS)\
        RECEIVE PARTIALLY (MORE)\
        RECEIVE UNFULFILLED
      </td>

      <td>
        RECEIVE FULFILLED
      </td>
    </tr>

    <tr>
      <td>
        Destination Delivery Status
      </td>

      <td>
        Status of the Transporter's driver delivering products to the Destination Depot at the time the report was exported
      </td>

      <td>
        Text
      </td>

      <td>
        *
      </td>

      <td>
        NOT FULFILLED\
        DELIVERY FULFILLED\
        DELIVERY PARTIALLY (LESS)\
        DELIVERY PARTIALLY (MORE)\
        DELIVERY UNFULFILLED
      </td>

      <td>
        DELIVERY FULFILLED
      </td>
    </tr>

    <tr>
      <td>
        Service Payer Organization Name
      </td>

      <td>
        Organization Name of the Depot that has to pay the Transport Service price of the Order
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
        Depot B52
      </td>
    </tr>

    <tr>
      <td>
        Service Payer Organization Description
      </td>

      <td>
        Description about the Depot that has to pay the Transport Service price of the Order\
        The value in this field is the same value as the attribute "Description" of the Depot
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
        This depot only works for twelve hours
      </td>
    </tr>
  </tbody>
</Table>

## ST18 - PDP Transporter Review

### Report ST18 - Export instruction

* Click on **Report Type** field, select this report from the drop down menu
* Then, click on **Date Range** field. From the drop down calendars, select the date range during which the orders were created and executed

- Finally, click on **Download** button. The system will immediately gather data and export the report into a downloadable Excel template after a short moment
- (Optional) If you want to include a header in the Excel template, you can click on the toggle button **Exclude Report Header** :fa-toggle-off:. When that button changes to **Include Report Header** :fa-toggle-on:, in the Excel template there will be a header

### Report ST18 - Information fields

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
        Transporter Code
      </td>

      <td>
        The management code of the Transporter
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
        Transporter\_ABC
      </td>
    </tr>

    <tr>
      <td>
        Transporter Name
      </td>

      <td>
        Name of the Transporter
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
        John Doe transport service
      </td>
    </tr>

    <tr>
      <td>
        Number Of Orders
      </td>

      <td>
        The quantity of orders performed by the Transporter during the selected date range
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
        122
      </td>
    </tr>

    <tr>
      <td>
        Total Order Weight
      </td>

      <td>
        The total weight of all orders performed by the Transporter
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
        23000
      </td>
    </tr>

    <tr>
      <td>
        Total Order Volume
      </td>

      <td>
        The total volume of all orders performed by the Transporter
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
        23000
      </td>
    </tr>

    <tr>
      <td>
        Total Service Cost
      </td>

      <td>
        The total transport service cost of all orders performed by the Transporter
      </td>

      <td>
        Number
      </td>

      <td>
        Currency Unit\
        For example: VND
      </td>

      <td>
        *
      </td>

      <td>
        40000000
      </td>
    </tr>

    <tr>
      <td>
        Fulfilled Orders
      </td>

      <td>
        The quantity of orders that have the Destination Delivery Status to be:\
        ***DELIVERY FULFILLED***
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
        Partially Fulfilled (Less) Orders
      </td>

      <td>
        The quantity of orders that have the Destination Delivery Status to be:\
        ***DELIVERY PARTIALLY (LESS)***
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
        Partially Fulfilled (More) Orders
      </td>

      <td>
        The quantity of orders that have the Destination Delivery Status to be:\
        ***DELIVERY PARTIALLY (MORE)***
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
        Unfulfilled Orders
      </td>

      <td>
        The quantity of orders that have the Destination Delivery Status to be:\
        ***UNFULFILLED***
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
        Not Yet Fulfilled Orders
      </td>

      <td>
        The quantity of orders that have the Destination Delivery Status to be:\
        ***NOT FULFILLED***
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
        Late Delivered Orders
      </td>

      <td>
        The quantity of orders that have the Delivery task submitted on Mobile app at later time points than were planned on Web app
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
        Declined Orders
      </td>

      <td>
        The quantity of orders that were declined by the Transporter (The Transporter is in blacklist)
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
  </tbody>
</Table>

## ST21 - Orders By Drivers

### Report ST21 - Export instruction

* Click on **Report Type** field, select this report from the drop down menu
* Then, click on **Date Range** field. From the drop down calendars, select the date range during which the orders were created and executed

- Finally, click on **Download** button. The system will immediately gather data and export the report into a downloadable Excel template after a short moment
- (Optional) If you want to include a header in the Excel template, you can click on the toggle button **Exclude Report Header** :fa-toggle-off:. When that button changes to **Include Report Header** :fa-toggle-on:, in the Excel template there will be a header

### Report ST21 - Information fields

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

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

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

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

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

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

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

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

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

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Total Order Weight
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Total Order Volume
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Planned Revenue
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Planned Cost
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Planned Distance
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Planned Time
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Actual Revenue
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Actual Cost
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Actual Distance
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Actual Start Time
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Actual End Time
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Actual Time
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        VFR By Weight
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Fulfilled Orders
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Partially Fulfilled Orders
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Unfulfilled Orders
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Not Yet Fulfilled Orders
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Number Of Off-200m Check-in
      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

## ST22 - PDP KPI Scoreboard

### Report ST22 - Export instruction

* Click on **Report Type** field, select this report from the drop down menu

### Report ST22 - Information fields

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

### Report ST23 - Export instruction

* Click on **Report Type** field, select this report from the drop down menu

<Image title="2019-11-08 17_14_12-[ST22] PDP KPI Scoreboard 2019-11-08_10_06.xlsx  [Protected View] - Excel.png" alt={1895} className="border" border={true} src="https://files.readme.io/29f109e-2019-11-08_17_14_12-ST22_PDP_KPI_Scoreboard_2019-11-08_10_06.xlsx_Protected_View_-_Excel.png" />

* Click on **Date Range** field, select the suitable date range from the drop down calendars

<Image title="2019-11-08 17_20_43-Abivin vApp.png" alt={1895} className="border" border={true} src="https://files.readme.io/4c535f7-2019-11-08_17_20_43-Abivin_vApp.png" />

* Next, click on **Select drivers** field, select the driver for whom you want to export report from the drop down menu. You can select multiple drivers at once

<Image title="2019-11-08 17_16_29-Abivin vApp.png" alt={1895} className="border" border={true} src="https://files.readme.io/4827217-2019-11-08_17_16_29-Abivin_vApp.png" />

* If you want to export report for all drivers, click on **Choose All Drivers** check box

<Image title="2019-11-08 17_16_54-Abivin vApp.png" alt={1895} className="border" border={true} src="https://files.readme.io/758d1b2-2019-11-08_17_16_54-Abivin_vApp.png" />

* Finally, click on **Download** button. The system will immediately gather data and export the report into a downloadable Excel template after a short moment
* (Optional) If you want to include a header in the Excel template, you can click on the toggle button **Exclude Report Header** :fa-toggle-off:. When that button changes to **Include Report Header** :fa-toggle-on:, in the Excel template there will be a header

![1901](https://files.readme.io/5f9aab1-Selection_003.png "Selection_003.png")

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
