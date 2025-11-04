---
title: Manage Customers
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
* Customers are the individuals/organizations who have regular demand for your Products. They will place [Sales Orders]() to fulfill their demand
* In this model, each Depot/Sun/Crossdock will have its own separate customer base. Customers who belong to the customer base of a Depot/Sun/Crossdock can only place orders from that Depot/Sun/Crossdock and not from other Depots/Suns/Crossdocks

## Locate Customer List

* The Customers are listed on the **Partners > Customers** tab

![1903](https://files.readme.io/ac744f3-nh_chp_1.png "ảnh chụp 1.png")

<Image title="AHRaFdPc5g.png" alt={1920} border={true} src="https://files.readme.io/27a0609-AHRaFdPc5g.png">
  Illustration (Vietnamese)
</Image>

## Create Customers

* You have two methods to create the Customers: Webform and Excel import file

### Customer Information Fields

* Below are the information fields of the Customer in this model

> 📘 Apart from the information fields mentioned below, other information fields can be left blank

* On Web form, the information of a customer is present on two tabs:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Tab title
      </th>

      <th>
        Tab description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        [Main Setting](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#main-setting)
      </td>

      <td>
        Basic information of the customer
      </td>
    </tr>

    <tr>
      <td>
        [Email Setting](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#email-setting)
      </td>

      <td>
        Information in this tab is used for Electronic Proof of Delivery (e-POD) function\
        Read more about this configuration at the following article: [**Electronic Proof of Delivery (e-POD)**](https://docs.abivin.com/docs/electronic-proof-of-delivery#section-add-email-addresses-to-the-recipient-list)
      </td>
    </tr>
  </tbody>
</Table>

![1911](https://files.readme.io/0df7b51-nh_chp_2.png "ảnh chụp 2.png")

#### Main Setting

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
        Organization (Webform); Organization Code (Excel import file)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Depot/Sun/Crossdock which directly manages the Customer being created\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Input the Organization Name/Organization Code of the appropriate Depot/Sun/Crossdock into the search bar, then select from the drop-down menu\
        **Excel import file:**\
        Copy the Organization Code of the appropriate Depot/Sun/Crossdock on the Web app then paste it into this cell\
        **Note:**\
        The Organization Name and Organization Code can be found under the columns of the same name on the "Organizations > Organizations" tab
      </td>
    </tr>

    <tr>
      <td>
        Customer Code (Webform); Partner Code (Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the Customer being created\
        **2. Input rules:**\
        Format: Can input letters, numbers, special characters (including spaces)\
        **Note:**\
        One Customer Code can exist in the Customer base of multiple Depots/Suns/Crossdocks
      </td>
    </tr>

    <tr>
      <td>
        Mobile Number (Webform); Phone Number (Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The mobile number of the Customer being created\
        This mobile number will appear on the Mobile app of the Drivers/Salesmen. They will use this mobile number to contact the Customer\
        **2. Input rules:**\
        Format: Numbers\
        Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        Customer Group (Webform); Partner Group Code (Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The Customer Group in which the Customer being created belongs\
        Read more about this configuration at the following article: [**Customer Groups**](https://docs.abivin.com/docs/vrp-in-house-fleet-customer-groups)
      </td>
    </tr>

    <tr>
      <td>
        Home Number\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The landline phone number of the Customer being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Title\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The title of the Customer being created to help you identify their gender\
        **2. Input rules:**\
        **Web form**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Full Name\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Full name of the Customer being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Open Time; Close Time\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The regular time of day at which the receiving location of the Customer being created officially opens and closes\
        These timestamps will be taken into account during the Route Plan optimization process if the Hard Time Windows algorithm configuration is enabled. Read more in the following article: [**Hard Time Window**]()\
        **2. Input rules:**\
        Format: HH:mm (Hour:Minute; 24 hour format)\
        For example, the receiving location of the Customer opens at 8:30 A.M and closes at 5:30 P.M every day. Input the following values into the "Open Time" and "Close Time" fields/cells respectively: ***08:30; 17:30***\
        The "Close Time" value could exceed the 24:00 mark. If the delivery time from the Depot to the Customer being created usually exceeds 24 hours, the value input into the "Close time" field/cell should be larger than the sum of the "Open time" value and the approximate delivery time period\
        For example, the receiving location of the Customer opens at 6:30 A.M everyday, and the time needed to deliver from the manufacturing warehouse to that receiving location is approximately 72 hours. The value input into "Close time" field/cell, therefore, should be larger than the sum of these two values, which is: ***78:30***
      </td>
    </tr>

    <tr>
      <td>
        Time window\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The time period(s) of the day during which the customer will receive deliveries\
        Read more about this configuration at the following article: [**Hard Time Window Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-hard-time-window-constraint)\
        **2. Input rules:**\
        Format: HH:mm-HH:mm (Hour:Minute-Hour:Minute; 24 hour format)\
        Input only the value in numbers. Do not input the unit\
        For example: The customer will only receive products from 5:00 A.M. to 1:00 P.M. Input the following value into the field/cell: ***06:00-13:00***\
        If the Customer being created doesn't have a time window to receive products, leave this field blank\
        If the Customer being created has multiple time windows, separate two adjacent time windows by a semicolon (;). For example: ***06:00-13:00;14:00-18:00***
      </td>
    </tr>

    <tr>
      <td>
        Bike only; Truck only\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Determine the vehicle type that can deliver to the customer being created from the default vehicle types: Motorbike; Truck and Semi-truck\
        Read more about this configuration at the following article: [**Vehicle Type Requirement**](https://docs.abivin.com/docs/vrp-in-house-fleet-vehicle-type-requirement)
      </td>
    </tr>

    <tr>
      <td>
        Allow Vehicle Types\
        (Excel import file)\
        (Optional)
      </td>

      <td>
        This information field will only be visible if the following configuration is enabled: **Flexible Vehicle Type**\
        Read more about this configuration at the following article: [**Site-Dependent Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-site-dependent-constraint)\
        **1. Description:**\
        The vehicle types that are allowed to deliver to the customer being created\
        **2. Input rules:**\
        Copy the vehicle type codes on Web app, then paste into this cell\
        If the customer being created allows more than one vehicle type, separate two adjacent vehicle type codes with a comma\
        For example: The customer being created allows three vehicle types: "Type\_01, Type\_02" and "Type\_03"\
        You have to input the following value into this cell: ***Type\_01,Type\_02,Type\_03***
      </td>
    </tr>

    <tr>
      <td>
        MinTime Unloading & MaxTime Unloading (Webform); Min Time & Max Time (Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The minimum and maximum time period (In minutes) that the Customer being created imposes on every Vehicle when unloading Products at their receiving locations\
        Read more about this configuration in the following article: [**Service Time Calculation**](https://docs.abivin.com/docs/vrp-in-house-fleet-planned-service-time-calculation)\
        **2. Input rules:**\
        Format: Minutes\
        Input only the value in numbers. Do not input the unit\
        For example, the Customer being created requires every Vehicle to unload Products at their receiving locations in no less than twenty minutes and no longer than forty minutes. Input the following values into the "MinTime Unloading/Min time" and the "MaxTime Unloading/Max time" fields/cells, respectively: ***20; 40***
      </td>
    </tr>

    <tr>
      <td>
        Lunch time\
        (Excel import file)\
        (Optional)
      </td>

      <td>
        **This information field is no longer used. Leave this cell blank**
      </td>
    </tr>

    <tr>
      <td>
        Original Address (Webform); Street Address (Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The specific address of the Customer being created\
        This address will show up on the Mobile app of the Drivers/Salesmen\
        **2. Input rules:**\
        Format: Free-form\
        For example: ***100 Doc Ngu, Ba Dinh, Hanoi***
      </td>
    </tr>

    <tr>
      <td>
        Latitude; Longitude\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The coordinates of the Customer being created\
        **2. Input rules:**\
        Format: Decimal degrees, similar to Google map format\
        For example: ***21.020123; 105.819509***
      </td>
    </tr>

    <tr>
      <td>
        Search Address\
        (Web form)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        This field will help you automatically search for the address and the coordinate of the Customer being created using the Google Maps engine right within the Abivin vRoute Web app\
        **2. Input rules:**\
        Read about this function in the following section: [**Automatically search customer coordinates**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#section-automatically-search-customer-coordinates)
      </td>
    </tr>

    <tr>
      <td>
        Serial Number\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **This information field is only used in CRM Model**\
        **1. Description:**\
        The serial numbers of the products purchased by the customer being created\
        **2. Input rules:**\
        Format: Free-form\
        For example: ***SR001***
      </td>
    </tr>

    <tr>
      <td>
        Comment\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A short description about the customer being created\
        **2. Input rules:**\
        Format: Free-form\
        For example: ***Important Customer!***
      </td>
    </tr>
  </tbody>
</Table>

#### Other Settings

# Email Settings

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
        Email
        (Web form + Excel template)
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Email address of the main receiver from the customer being created, who will receive the Delivery note emails when orders are completed\
        **2. Input rules:**\
        Input the exact email into this field/cell\
        **Note when using Excel template:**\
        In the Excel template, before uploading, you must remove hyperlinks from all the email addresses\
        Read the following article for instruction: [**CRUD functions**](https://docs.abivin.com/docs/crud#section-remove-hyperlinks-from-email-addresses-before-upload)
      </td>
    </tr>

    <tr>
      <td>
        CC\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Email address of the person/organization who will also receive copies of the emails sent to the main receiver, and is visible to other receivers\
        **2. Input rules:**\
        Same with Email field
      </td>
    </tr>

    <tr>
      <td>
        BCC\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Email address of the person/organization who will also receive copies of the emails sent to the main receiver, but is not visible to other receivers\
        **2. Input rules:**\
        Same with Email field
      </td>
    </tr>
  </tbody>
</Table>

#### Sales Area

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
        Sales Code
        (Web form + Excel template)
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The unique sales code of the customer being created\
        Read more about this feature at the following article:\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Sales code 01" is invalid; "Sales\_code\_01" is valid
      </td>
    </tr>

    <tr>
      <td>
        MDP\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A unique Master Delivery Plan code assigned to the customer being created\
        Read more about this configuration in this article: [**Optimize routes with Familiarity constraint**](https://docs.abivin.com/docs/how-to-optimize-routes-with-familiarity-constraint)\
        **2. Input rules:**\
        Format: Can contain letters, numbers, special characters, and spaces\
        One Customer can have only one MDP code
      </td>
    </tr>

    <tr>
      <td>
        Tax Code\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Tax code of the customer being created\
        **2. Input rules:**\
        Format: Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        Invoice Address\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The address to send invoices to the customer being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

# Ship-to Profile  

* This is an exclusive tab for certain user accounts\
  Information of the customer for different manufacturing warehouses\
  Read more at the following section: Ship-to Profile

## Update customer information

### Update single customer using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

### Mass update multiple customers using Excel template

* You can also update multiple Customers at once using the Excel template. To do this, first, you need to copy and paste the Customer Codes of the existing Customers into the Excel template, then input new information into other fields. After that, just upload the Excel template as usual. The system will replace the existing Customer information with the new information in the Excel template

<Image title="S2I2eLLLHr.png" alt={735} className="border" border={true} src="https://files.readme.io/113f489-S2I2eLLLHr.png" />

## Delete customer

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

- **Note:** The system will prevent you from deleting Customers whose Orders (regardless of the Order Date) are in ***Open; Planned*** Planning Status. The system will display the following error message:

<Image title="0wYW8tOQyu.png" alt={292} border={true} src="https://files.readme.io/c3598f4-0wYW8tOQyu.png">
  Illustration (English)
</Image>

<Image title="9f1E6kugnS.png" alt={282} border={true} src="https://files.readme.io/5ae481c-9f1E6kugnS.png">
  Illustration (Vietnamese)
</Image>

## Export customer list

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-read-objects-on-excel-file-export-) article to know the general steps about exporting objects in Abivin vRoute

## Search and filter customer

### Search customer

* To search for a specific customer, input one of these following attribute of that customer into the search field: ***Title; Customer Code; Customer Name; Email; Mobile Number*** 

<Image title="tRTXIyJIpV.png" alt={1920} className="border" border={true} src="https://files.readme.io/6c8da21-tRTXIyJIpV.png" />

### Filter customer by Depot/Sun/Crossdock

* You can filter customers who are under direct management of a specific Depot/Sun/Crossdock by clicking on **Organization** :fa-caret-down: field, then input the ***Organization name*** of that Depot/Sun/Crossdock into the search bar. Customers who are under direct management of that Depot/Sun/Crossdock will show up shortly

<Image title="4FyYhRgZ9r.png" alt={1920} className="border" border={true} src="https://files.readme.io/4cff42b-4FyYhRgZ9r.png" />

### Filter customer by Customer group or Province/City

* You can filter the Customer list to show Customers who belong to the same Customer Group, or locate in the same Province/City by clicking on the corresponding column title, then select the Customer group or Province/City from the drop down menu. Customers who meet the selected conditions will show up shortly

<Image title="oxNfhV12Zq.png" alt={1920} border={true} src="https://files.readme.io/39b173c-oxNfhV12Zq.png">
  Filter customers by Customer group
</Image>

<Image title="StdR4wvn8b.png" alt={1920} border={true} src="https://files.readme.io/d3ad66c-StdR4wvn8b.png">
  Filter customers by Province/City
</Image>

> 👍 You can combine several filters for more accurate search results

## View Customers locations on Map

* You can view the locations of the customers on Map screen by clicking on the icon **Map View**
* The location of a customer will be signified by a blue location mark icon :fa-map-marker:. You can click on the location mark icon to display the Customer Name
* To go back to the Customer list, click on the icon **View Data Table** :fa-table:

<Image title="locate on map.gif" alt={1916} className="border" border={true} src="https://files.readme.io/748773d-locate_on_map.gif" />

## Retrieve Customer Address; Coordinates and Customer Group

* During the Customer creation/editing process, you can opt to manually input or let the system automatically retrieve the Customer address and coordinate information using Abivin built-in address engine or the Google Map engine

> 🚧 Automatic Customer Group allocation
>
> In order for the system to automatically allocate Customers into appropriate Customer Groups, then prior to creating Customers you have to create and set up the Customer Groups based on Administrative Divisions. The setup guide can be found in the following article : [**Geographic Clustering**](https://docs.abivin.com/docs/vrp-in-house-fleet-geographic-clustering#geographic-clustering-by-administrative-divisions)

### Manually input Customer address & coordinates

* On the Webform, you can manually input the Customer address into the **Original Address** field and the Customer coordinates into the **Latitude; Longitude** fields

<Image title="Image 24.png" alt={952} border={true} src="https://files.readme.io/7bff969-Image_24.png">
  Illustration (English)
</Image>

<Image title="LXb2GBhK8b.png" alt={927} border={true} src="https://files.readme.io/d9593c3-LXb2GBhK8b.png">
  Illustration (Vietnamese)
</Image>

* On the Excel import file, input the Customer address into the **City/Province; Address; Street Address; Town; District; Country** fields, and the Customer coordinate into the **Latitude; Longitude** fields

### Automatically retrieve Customer address & coordinate

* On the Webform, first, select the address engine you want to use by clicking on the address engine selection icon (Located next to the **Search Address** input field). A list will pop out displaying the two aforementioned address engines. Click on the desired engine to select it

<Image title="kH9hZL4bkk.png" alt={921} className="border" border={true} src="https://files.readme.io/cfc7fec-kH9hZL4bkk.png" />

* Next, input the specific address of that customer into the **Search Address** field. If you use the Abivin built-in address engine, you should input the address as detailed as possible (Building number, street, town, city, country, etc.) then click on the result on the dropdown list. If you use the Google address engine, you can simply input a part of the address, not necessarily the full address. After that, the engine will show a list of suggestions for you to choose from. Click on the correct suggestion

<Image title="nG6gCi7DiH.png" alt={942} className="border" border={true} src="https://files.readme.io/481a93f-nG6gCi7DiH.png" />

* After you have input and selected the most appropriate address result, the system will connect to the address engine database, retrieve the address and coordinate information, then input into the corresponding fields

<Image title="auto address.gif" alt={916} className="border" border={true} src="https://files.readme.io/4d8c916-auto_address.gif" />

* In case you think the returned coordinate information is incorrect, you can move your mouse onto the map thumbnail, use the middle scroll button to zoom in the map, use the left mouse button to drag and drop the red location mark icon to the location you think is more correct. When you release the left mouse button, the Latitude and Longitude values will update accordingly

<Image title="change coord.gif" alt={488} className="border" border={true} src="https://files.readme.io/3cde75c-change_coord.gif" />

* In the Customer import Excel template, input the Customer address into the **Address** cell and leave the **Latitude; Longitude; City/Province; Street Address; Town; District; Country** cells blank. After uploading the Excel template, the system will connect to the address engines and automatically fills in the address and coordinate fields of the Customers on the Web form. During this process, the Abivin built-in address engine will be connected first. If the Abivin built-in engine can not return results, the system will switch to the Google Map engine

> ❗️ When importing Customers using Excel template. the Google Map engine is only available for certain user accounts

* If any of the above cells have value, the system will use the input value instead of retrieving from the address engines' database

## Ship-to Profile

> ❗️ At the moment, the content in this section is exclusive for certain User accounts

* In actual operation, a Customer can receive deliveries from different Depots. Each Depot very likely manage the same Customer with different identification information. This identification information is defined as **Ship-to profile**

![441](https://files.readme.io/07a8992-123.png "123.png")

### Ship-to profile information

* Below are the information fields of a Ship-to profile

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
        Shipper Code
        (Webform + Excel import file)
      </td>

      <td>
        **1. Description:**\
        The Shipper that manages the Ship-to Profile being created\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Select the appropriate Shipper from the drop-down list\
        **Excel import file:**\
        Copy the Organization Code of the appropriate Shipper on the Web app then paste it into this cell
      </td>
    </tr>

    <tr>
      <td>
        Ship-To Code\
        (Webform + Excel import file)
      </td>

      <td>
        **1. Description:**\
        The management code that the Shipper assigns to the Customer's receiving location\
        **2. Input rules:**\
        Format: Can contain letters, numbers, special characters, spaces, and tone marks
      </td>
    </tr>

    <tr>
      <td>
        Ship-To Name\
        (Webform + Excel import file)
      </td>

      <td>
        **1. Description:**\
        The name that the Shipper assigns to the Customer's receiving location\
        **2. Input rules:**\
        Format: Can contain letters, numbers, special characters, spaces, and tone marks
      </td>
    </tr>

    <tr>
      <td>
        Ship-To Adress\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The address of the Customer's receiving location\
        **2. Input rules:**\
        Format: Can contain letters, numbers, special characters, spaces\
        For example: "100 Doc Ngu, Hanoi, Vietnam"
      </td>
    </tr>

    <tr>
      <td>
        Ship-To Expected Lead Time\
        (Webform + Excel import file)
      </td>

      <td>
        **1. Description:**\
        The expected lead time that the Customer's receiving location specifies for each of the Shippers associated with that Customer\
        This value will be used during the Route Plan optimization process\
        Read more in the following section: [**Ship-To Expected Lead Time**](https://docs.abivin.com/docs/vrp-dc-shipper#ship-to-expected-lead-time)\
        **2. Input rules:**
      </td>
    </tr>

    <tr>
      <td>
        Ship-To Time Window (HH:mm)\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The receiving time window of the Customer specified for each Ship-to Depot\
        **2. Input rules:**\
        Format: HH:mm-HH:mm (Hour:Minute-Hour:Minute; 24 hour format)\
        You can also click on the clock icon at the end of the field and select the appropriate time points there
      </td>
    </tr>

    <tr>
      <td>
        Ship-To Mobile Number\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The mobile number of the Customer specified for each Ship-to Depot\
        **2. Input rules:**\
        Format: Numbers only
      </td>
    </tr>

    <tr>
      <td>
        Ship-To Receiving Capacity\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The receiving capacity (In pallets) of the Customer specified for each Ship-to Depot\
        **2. Input rules:**\
        Format: Numbers only
      </td>
    </tr>
  </tbody>
</Table>

### Ship-To Expected Lead Time

* Ship-To Expected Lead Time is the lead time (By day) the Customer specified for each Ship-to Depot
* This value will be used to determine the delivery date range of the Orders originating from the Ship-to Depot to the Customer. Read more in the following article: [**Ship-to Depot Delivery**](https://docs.abivin.com/docs/vrp-in-house-fleet-ship-to-delivery)
* Below is the list of the Ship-To Expected Lead Time values:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Ship-To Expected Lead Time
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        N/A
      </td>

      <td>
        There is no Expected Lead Time between the Customer and the Ship-to Depot
      </td>
    </tr>

    <tr>
      <td>
        D0
      </td>

      <td>
        The Expected Lead Time between the Customer and the Ship-to Depot is zero-day
      </td>
    </tr>

    <tr>
      <td>
        D1
      </td>

      <td>
        The Expected Lead Time between the Customer and the Ship-to Depot is one day
      </td>
    </tr>

    <tr>
      <td>
        D2
      </td>

      <td>
        The Expected Lead Time between the Customer and the Ship-to Depot is two days
      </td>
    </tr>

    <tr>
      <td>
        D3
      </td>

      <td>
        The Expected Lead Time between the Customer and the Ship-to Depot is three days
      </td>
    </tr>

    <tr>
      <td>
        D4
      </td>

      <td>
        The Expected Lead Time between the Customer and the Ship-to Depot is four days
      </td>
    </tr>

    <tr>
      <td>
        D5
      </td>

      <td>
        The Expected Lead Time between the Customer and the Ship-to Depot is five days
      </td>
    </tr>

    <tr>
      <td>
        D6
      </td>

      <td>
        The Expected Lead Time between the Customer and the Ship-to Depot is six days
      </td>
    </tr>

    <tr>
      <td>
        D7
      </td>

      <td>
        The Expected Lead Time between the Customer and the Ship-to Depot is seven days
      </td>
    </tr>

    <tr>
      <td>
        D8
      </td>

      <td>
        The Expected Lead Time between the Customer and the Ship-to Depot is eight days
      </td>
    </tr>
  </tbody>
</Table>

* Input rules: On Web form, click on this field and select the appropriate lead time value from the drop-down list. On Excel template, for each Ship-to profile, input only one of the above nine values (From ***D0*** to ***D8***) into the **Ship-to Expected Lead Time** cell

### Add Ship-to profiles

* To add Ship-to profile for a customer, follow the steps below

#### Add Ship-to profiles on Web form

* Navigate to **Ship-to Profile** tab
* Input the information of each Ship-to profile into the information fields described above, then click on the button **Add to List**
* The recently created Ship-to profile will appear in the list below
* Repeat these steps for other Ship-to profiles of that Customer

<Image title="ship-to customer.gif" alt={952} className="border" border={true} src="https://files.readme.io/a64d245-ship-to_customer.gif" />

#### Add Ship-to profiles on Excel template

* On Excel template, if a customer has multiple Ship-to profiles, you need to put each Ship-to profile of that customer on a separate row
* **Important Note:** You have to duplicate every common information of the Customer between each row of its Ship-to profiles, else the Excel template can not be imported

<Image title="Image 28.png" alt={1635} className="border" border={true} src="https://files.readme.io/3d84c2c-Image_28.png" />

## Search & Filter Customers

### Filters no-coordinates customers

* You can filter Customers who don't have coordinates information (Which means their (Latitude; Longitude) are (0;0)) by clicking on the column **Validation Status** and tick the checkbox **No-Coordinate**

## Beginner's Guide

### Create a Customer

* Steps to create a single customer using Web form:
* Step 1: Navigate to **Partners > Customers** tab.
* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Create** (the :fa-pencil: symbol).

![2880](https://files.readme.io/2853671-Screen_Shot_2021-01-22_at_15.15.38.png "Screen Shot 2021-01-22 at 15.15.38.png")

* Step 3: Navigate to the **Main Setting** tab and input the required information:
* **Customer code:** Input the management code assigned to the customer being created.
* **Mobile Number:** Input the mobile number of the customer being created.
* **Organization:** Input the Depot/Sun/Crossdock of which the customer base contains the customer being created.
* **Parent Customer:** Input the higher level customer group in which the customer group being created belongs.
* **Full name:** Input the full name of the customer being created.
* **Open Time:** Input the regular time of day at which the customer organization officially starts working.
* **Close Time:** Input the regular time of day at which the customer organization officially closes.
* **Bike only; Truck only:** Choose TRUE or FALSE of these fields to determine the vehicle type that can deliver to the customer being created from the default vehicle types: Motorbike; Truck and Semi-truck. 
* **MinTime Unloading & MaxTime Unloading:** Input the minimum and maximum time period (In minutes) that the customer being created imposes on all vehicles when unloading products at their warehouse.
* **Customer Group:** Tick the checkbox of the Customer Group to which you want to allocate the Customer being edited. You can also input the Customer Group Code/Customer Group Name of the desired Customer Group into the search bar to filter faster. 
* Important note: Even though you can select multiple Customer Groups, in this model one Customer can only belong to one Customer Group. If you select multiple Customer Groups for a Customer, the system will not be able to generate the optimized Delivery Route for that Customer during the Route Plan optimization process
* **Original Address:** Input the specific address of the customer being created.
* **Latitude; Longitude:** Input the coordinates of the customer being created.
* *Example:* 

![854](https://files.readme.io/1d31cea-nh_chp_4.png "ảnh chụp 4.png")

![850](https://files.readme.io/1570b55-nh_chp_5.png "ảnh chụp 5.png")

* The fields above, if properly inputted, are enough to create a single and simple customer, please click [here](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#main-setting) to learn more about their notes and input rules.
* Step 4: Click **SAVE**.

## Customer Non-working Days

* To set up the Non-working Days of a particular Customer, navigate to the **Other Settings > Non-working Days** section
* **By week:** You can choose non-working days.
* **By Public Holidays:** You can choose holidays according to the country, where you work.
* **Add Custom day:** Add the holidays you want.

![864](https://files.readme.io/45f523f-nh_chp_6.png "ảnh chụp 6.png")

![864](https://files.readme.io/706c6e0-nh_chp_7.png "ảnh chụp 7.png")

## Ship-to Address

* To set up Client-specific sub-addresses, navigate to\
  **More Settings >Ship-to Address**
* **Stress adress:** You can enter another address.
* **Latitude; Longitude:** Input the coordinates of the customer being created.
* **Input rules:**\
  *Format: Decimal degrees, similar to Google map format\&#xA;*&#x46;or example: 21.020123; 105.819509\
  Click **ADD ADDRESS**.

<Image title="g3.png" alt={867} src="https://files.readme.io/6c1666c-g3.png">
  Illustration (Vietnamese)
</Image>

<Image title="g2.png" alt={868} src="https://files.readme.io/83bd0b5-g2.png">
  Illustration (English)
</Image>

* Change the secondary address at the Order screen\
  At the order screen, you can choose a secondary address for same-day delivery without changing the customer's address.
* **Note:** In a route day, each customer can create many orders but can only deliver to one address

<Image title="a5.png" alt={1155} src="https://files.readme.io/a3a7fd6-a5.png">
  Illustration (Vietnamese)
</Image>

<Image title="a4.png" alt={1154} src="https://files.readme.io/e3605da-a4.png">
  Illustration (English)
</Image>
