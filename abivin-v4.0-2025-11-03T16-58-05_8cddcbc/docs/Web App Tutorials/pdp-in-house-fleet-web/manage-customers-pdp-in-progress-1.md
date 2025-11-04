---
title: Manage Customers
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
* In this model, each Depot will have its own separate customer base. Customers who belong to the customer base of a Depot can only place orders from that Depot, not from others. 

## Locate Customer List

* Customers are listed on **Partners > Customer List** tab

<Image title="ooyEq8WtBg.png" alt={1920} className="border" border={true} src="https://files.readme.io/370c81f-ooyEq8WtBg.png" />

## Create customers

* You have two methods to create customers: Webform or Excel template.

## Method 1: Create a single customer using Webform

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating a single object using the web form.
* On Web form, the information of a customer is present on four tabs:

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
        Main Setting
      </td>

      <td>
        Basic information of the customer.
      </td>
    </tr>

    <tr>
      <td>
        Email Setting
      </td>

      <td>
        Email addresses of the customer.
      </td>
    </tr>

    <tr>
      <td>
        Shipt-to Profile
      </td>

      <td>
        * \*This is an exclusive tab for some user account&#x73;**.\
          Information about the receiving locations of the customer.\
          Read more from this following section: \[**&#x53;hip-to Profile\*\*]\([https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#section-ship-to-profile](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#section-ship-to-profile)).
      </td>
    </tr>

    <tr>
      <td>
        Sales Area
      </td>

      <td>
        Extensive sales information of the customer
      </td>
    </tr>
  </tbody>
</Table>

<Image title="creat cus.gif" alt={956} border={true} src="https://files.readme.io/13c0179-creat_cus.gif">
  Customer Web form
</Image>

## Method 2: Create multiple customers using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template.\
  .

## Customer information fields

* Below are all information fields of the customer in this model.

> 📘 Apart from the information fields mentioned below, other information fields can be left blank

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
        Tab: **Main Setting**
      </td>

      <td>
        Basic information of the customer.
      </td>
    </tr>

    <tr>
      <td>
        Organization (Webform); Organization Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Depot of which the customer base contains the customer.\
        **2. Input rules:**\
        Click on this field. Input the Organization. Name/Organization Code of the appropriate Depot into the search bar, then select from the drop-down menu.\
        Copy the Organization code of the appropriate Depot/ on the Web app, then paste into this cell.\
        **Note:**\
        The Organization Name and Organization Code can be found under the columns of the same name on tab **Organizations > Organization List**.
      </td>
    </tr>

    <tr>
      <td>
        Customer Code (Webform); Partner Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to each customer.\
        **2. Input rules:**\
        **Webform:**\
        Format: Must not contain spaces.\
        For example: "Customer 01" is not acceptable; "Customer\_01" is acceptable.\
        **Note:**\
        The customer code is unique. Two separate customers cannot have the same customer code\
        One customer code can only belong to one Depot customer base.
      </td>
    </tr>

    <tr>
      <td>
        Mobile Number (Web form); Phone Number (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Mobile number of the customer.\
        The drivers will contact the customer via this phone number.\
        **2. Input rules:**\
        Format: Numbers.\
        Must not contain spaces.
      </td>
    </tr>

    <tr>
      <td>
        Customer Group (Web form); Partner Group Code (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The group of customer that the customer being created belong to.\
        Read more about this configuration at the following article: [**Customer Groups**](https://docs.abivin.com/docs/vrp-in-house-fleet-customer-groups).
      </td>
    </tr>

    <tr>
      <td>
        Mobile Number (Web form); Phone Number (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Mobile number of the customer\
        The deliverymen will contact the customer via this mobile number.\
        **2. Input rules:**\
        Format: Numbers.\
        Must not contain spaces.
      </td>
    </tr>

    <tr>
      <td>
        Home Number\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Landline phone number of the customer.\
        **2. Input rules:**\
        Format: Free-form.
      </td>
    </tr>

    <tr>
      <td>
        Title\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The title of the customer used to identify their gender.\
        **2. Input rules:**\
        **Webform**\
        Format: Free-form.
      </td>
    </tr>

    <tr>
      <td>
        Full Name\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Full name of the customer.\
        **2. Input rules:**\
        Format: Free-form.
      </td>
    </tr>

    <tr>
      <td>
        Open Time; Close Time\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The regular time of day at which the customer organization officially starts working and closing.\
        **2. Input rules:**\
        Format: HH: mm (Hour: Minute; 24-hour format)\
        For example: The customer regularly starts working at 8:30 A.M and closes at 5:30 P.M every day.\
        Input the following values into "Open Time" and "Close Time" fields/cells respectively: ***08:30; 17:30***.\
        **Special Note:**\
        The "Close Time" value could exceed the 24:00 mark. If the time to deliver from the Depot to the customer being created usually exceeds 24 hours, the value input into "Close time" field/cell should be larger than the sum of the "Open time" value and the approximate delivery time period\
        For example: The customer opens at 6:30 A.M every day, and the time needed to deliver from the manufacturing warehouse to that customer is around 72 hours. The value input into "Close time" field/cell should, therefore, be larger than ***78:30***.
      </td>
    </tr>

    <tr>
      <td>
        Time window\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The only time period of a day during which the customer will receive deliveries.\
        Read more about this configuration at the following article: [**Hard Time Window Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-hard-time-window-constraint).\
        **2. Input rules:**\
        Format: HH:mm-HH: mm (Hour:Minute-Hour: Minute).\
        Input only the value in numbers. Do not input the unit.\
        For example: The customer will only receive products from 5:00 A.M. to 1:00 P.M. Input the following value into the field/cell: ***06:00-13:00***.\
        If the customer doesn't have a time window to receive products, leave this field blank.
      </td>
    </tr>

    <tr>
      <td>
        Bike only; Truck only\
        (Webform + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Determine the vehicle type that can deliver to the customer from the default vehicle types: Motorbike; Truck and Semi-truck.\
        Read more about this configuration at the following article: [**Vehicle Type Requirement**](https://docs.abivin.com/docs/vrp-in-house-fleet-vehicle-type-requirement).
      </td>
    </tr>

    <tr>
      <td>
        Allow Vehicle Types\
        (Excel template)\
        (Optional)
      </td>

      <td>
        This information field will only be visible if the following configuration is enabled: **Flexible Vehicle Type**\
        Read more about this configuration at the following article: [**Site-Dependent Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-site-dependent-constraint)\
        **1. Description:**\
        The vehicle types that are allowed to deliver to the customer being created\
        **2. Input rules:**\
        Copy the vehicle type codes on the Web app, then paste into this cell.\
        If the customer type allows more than one vehicle type, separate two adjacent vehicle type codes with a comma.\
        For example: The customer being created allows three vehicle types: "Type\_01, Type\_02" and "Type\_03".\
        You have to input the following value into this cell: ***Type\_01,Type\_02,Type\_03***.
      </td>
    </tr>

    <tr>
      <td>
        MinTime Unloading & MaxTime Unloading (Web form); Min Time & Max Time (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The minimum and maximum time period (In minutes) **that**the customer being created imposes on all vehicles when unloading products at their warehouse.\
        Read more about this configuration at the following article: [**Planned Loading/Unloading time**](https://docs.abivin.com/docs/vrp-in-house-fleet-planned-loading-and-unloading-time-calculation).\
        **2. Input rules:**\
        Format: Minutes\
        Input only the value in numbers. Do not input the unit.\
        For example: The customer requires each vehicle to unload products at their warehouse no less than twenty minutes and no longer than forty minutes. Input the following values into "MinTime Unloading/Min time" and "MaxTime. Unloading/Max time" fields/cells, respectively: ***20; 40***.
      </td>
    </tr>

    <tr>
      <td>
        Lunch time\
        (Excel template)\
        (Optional)
      </td>

      <td>
        **This information field is obsolete**
      </td>
    </tr>

    <tr>
      <td>
        Original Address (Web form); Street Address (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The specific address of the customer.\
        **2. Input rules:**\
        Format: Free-form.\
        For example: ***100 Doc Ngu, Ba Dinh, Hanoi***.
      </td>
    </tr>

    <tr>
      <td>
        Latitude; Longitude\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The location of the customer.\
        **2. Input rules:**\
        Format: Decimal degrees, similar to Google map format.\
        For example: ***21.020123; 105.819509***.
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
        This field will help you automatically search for the address and location of the customer using Google Maps, right within Abivin vRoute interface\
        **2. Input rules:**\
        Read about this function at the following section: [**Automatically search customer coordinates**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#section-automatically-search-customer-coordinates).
      </td>
    </tr>

    <tr>
      <td>
        Serial Number\
        (Web form + Excel template)\
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
        (Web form + Excel template)\
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

    <tr>
      <td>
        Tab: **Email Setting**
      </td>

      <td>
        Information in this tab is used for Electronic Proof of Delivery (e-POD) function\
        **Read more about this configuration at the following article: \[**&#x45;lectronic Proof of Delivery (e-POD)**]\([https://docs.abivin.com/docs/electronic-proof-of-delivery#section-add-email-addresses-to-the-recipient-list](https://docs.abivin.com/docs/electronic-proof-of-delivery#section-add-email-addresses-to-the-recipient-list))** 
      </td>
    </tr>

    <tr>
      <td>
        Email\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Email address of the main receiver from the customer lists, who will receive the Delivery note emails when orders are completed\
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

    <tr>
      <td>
        Tab: **Sales Area**
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Sales Code\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The unique sales code of the customers.\
        Read more about this feature at the following article:\
        **2. Input rules:**\
        Format: Must not contain spaces.\
        For example: "Sales code 01" is invalid; "Sales\_code\_01" is valid.
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
        A unique Master Delivery Plan code assigned to the customers.\
        Read more about this configuration in this article: [**Optimize routes with Familiarity constraint**](https://docs.abivin.com/docs/how-to-optimize-routes-with-familiarity-constraint)\
        **2. Input rules:**\
        **Webform + Excel template:**\
        Format: Must not contain spaces.\
        For example: "MDP code 01" is not acceptable; "MDP\_code\_01" is acceptable.\
        One customer can have only one MDP code.
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
        Tax Code of the customer.\
        **2. Input rules:**\
        Format: Must not contain spaces.
      </td>
    </tr>

    <tr>
      <td>
        Tab: **Ship-To Profile**
      </td>

      <td>
        **This is an exclusive tab for only one of our clients**\
        Read more about this in the following section: [**Ship-to Profile**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#section-ship-to-profile)
      </td>
    </tr>
  </tbody>
</Table>

## Update customer information

## Update single customer using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Mass update multiple customers using Excel template

## Delete customer

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

## Export customer list

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-read-objects-on-excel-file-export-) article to know the general steps about exporting objects in Abivin vRoute

## Search and filter customer

## Search customer

* To search for a specific customer, input one of these following attribute of that customer into the search field: ***Title; Customer Code; Customer Name; Email; Mobile Number*** 

<Image title="tRTXIyJIpV.png" alt={1920} className="border" border={true} src="https://files.readme.io/6c8da21-tRTXIyJIpV.png" />

## Filter customer by Depot/Sun/Crossdock

* You can filter customers who are under direct management of a specific Depot/Sun/Crossdock by clicking on **Organization** :fa-caret-down: field, then input the ***Organization name*** of that Depot/Sun/Crossdock into the search bar. Customers who are under direct management of that Depot/Sun/Crossdock will show up shortly.

<Image title="4FyYhRgZ9r.png" alt={1920} className="border" border={true} src="https://files.readme.io/4cff42b-4FyYhRgZ9r.png" />

## Filter customer by Customer group or Province/City

* You can filter customer belong to the same Customer group, or locate in the same Province/City by clicking on the corresponding column, then select the Customer group or Province/City from the drop-down menu. Customers who meet the selected conditions will show up shortly.

<Image title="oxNfhV12Zq.png" alt={1920} border={true} src="https://files.readme.io/39b173c-oxNfhV12Zq.png">
  Filter customers by Customer group
</Image>

<Image title="StdR4wvn8b.png" alt={1920} border={true} src="https://files.readme.io/d3ad66c-StdR4wvn8b.png">
  Filter customers by Province/City
</Image>

> 👍 You can combine several filters for more accurate search results

## View Customers locations on Map

* You can view the locations of the customers on Map screen by clicking on the icon **Map View**
* The location of a customer will be signified by a blue location mark icon :fa-map-marker: You can click on the location mark icon to display the Customer Name.
* To go back to the Customer list, click on the icon **View Data Table** :fa-table:

<Image title="locate on map.gif" alt={1916} className="border" border={true} src="https://files.readme.io/748773d-locate_on_map.gif" />

## Customer address & coordinates

## Manual Customer address & coordinates

* On Webform, you can manually input the customer address into **Original Address** field, and customer coordinates into **Latitude; Longitude** fields.

<Image title="Image 24.png" alt={952} className="border" border={true} src="https://files.readme.io/7bff969-Image_24.png" />

* On Excel template, input the customer address into **Street Address** field, and customer coordinates into **Latitude; Longitude** fields.

<Image title="manual add.png" alt={397} className="border" border={true} src="https://files.readme.io/610e61f-manual_add.png" />

## Automatic Customer address & coordinates

### Automatic Customer address & coordinates on Web form

* On Webform, you can let the system fill in the coordinates fields (Latitude; Longitude) instead of having to manually input them, just by inputting the specific address of that customer into the field **Search Address**.
* As you input, the system will connect with Google Maps, retrieve appropriate addresses based on what you input, and display them on the drop-down list. As you select an address from that list, the system will automatically fill in the following information fields for you: **Street Address; Town; District; City; Country; Latitude; Longitude**.

<Image title="address auto.gif" alt={956} className="border" border={true} src="https://files.readme.io/85875f8-address_auto.gif" />

* In case you're not certain the coordinates information is really correct, you can move your mouse onto the map thumbnail, use the middle scroll button to zoom in the map, use the left mouse button to drag and drop the red location mark icon to the exact location you intend. When you release the left mouse button, the coordinates information will update accordingly.

<Image title="change coord.gif" alt={488} className="border" border={true} src="https://files.readme.io/3cde75c-change_coord.gif" />

### Automatic Customer address & coordinates via Excel template

> 🚧
>
> At the moment, this feature is only enabled for certain User accounts

* It is also possible to let the system automatically find customer address and coordinates on Google Maps based on the value input into the field **Address** in the Excel template. After uploading the Excel template, the system will automatically connect to Google Map and fill in the following fields of the customer: **Search Address; Street Address; Town; District; City; Country; Latitude; Longitude**.

![930](https://files.readme.io/b41f1de-autoad.png "autoad.png")

* At the moment, this feature is only enabled for some specific user accounts. For other accounts, the system will still take the values input into the fields **Street Address; Latitude; Longitude** to input into the fields **Original Address; Latitude; Longitude** on the Web form.
* **Note**: For User accounts having this feature, if the fields **Latitude; Longitude** in the Excel template already have values, then the system will directly take these values and not connect to Google Map. Furthermore, the system will not base on the manually filled **Latitude; Longitude** values to automatically connect to Google Map and fill in the fields **Search Address; Street Address; Town; District; City; Country**.

## Search & Filter Customers

### Filters no-coordinates customers

* You can filter Customers who don't have coordinates information (Which means their (Latitude; Longitude) are (0;0)) by clicking on the column **Validation Status** and tick the checkbox **No-Coordinate**.
