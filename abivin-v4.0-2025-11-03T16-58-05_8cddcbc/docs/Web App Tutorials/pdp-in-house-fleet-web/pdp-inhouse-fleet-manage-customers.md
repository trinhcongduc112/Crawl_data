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
* In this model, the term **Customer** refers to the locations where the Vehicles will travel to and either pick up Products (Defined as the **Origin Customer**) or drop off Products (Defined as the **Destination Customer**)

## Locate Customer List

* The Customers are listed on the **Partners > Customers** tab

<Image title="1. Customers (ENG).png" alt={1920} border={true} src="https://files.readme.io/73ae3a6-1._Customers_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Customers (VIE).png" alt={1920} border={true} src="https://files.readme.io/5921ecf-1._Customers_VIE.png">
  Illustration (Vietnamese)
</Image>

## Create Customers

* You have two methods to create the Customers: Webform and Excel import file

### Customer Information Fields

* Below are the information fields of the Customer in this model

> 📘 Apart from the information fields mentioned below, other information fields can be left blank

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
        [Main Setting](https://docs.abivin.com/docs/pdp-inhouse-fleet-manage-customers#main-setting)
      </td>

      <td>
        Basic information of the customer
      </td>
    </tr>

    <tr>
      <td>
        [Email Setting](https://docs.abivin.com/docs/pdp-inhouse-fleet-manage-customers#email-setting)
      </td>

      <td>
        Information in this tab is used for the Electronic Proof of Delivery (e-POD) feature\
        Read more about this configuration at the following article: [**Electronic Proof of Delivery (e-POD)**](https://docs.abivin.com/docs/electronic-proof-of-delivery#section-add-email-addresses-to-the-recipient-list)
      </td>
    </tr>

    <tr>
      <td>
        [Ship-to Profile](https://docs.abivin.com/docs/pdp-inhouse-fleet-manage-customers#ship-to-profile)
      </td>

      <td>
        Information of the customer for different manufacturing warehouses
      </td>
    </tr>

    <tr>
      <td>
        [Sales Area](https://docs.abivin.com/docs/pdp-inhouse-fleet-manage-customers#sales-area)
      </td>

      <td>
        Extensive sales information of the customer
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2. Create (ENG).png" alt={1072} border={true} src="https://files.readme.io/a3de882-2._Create_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Create (VIE).png" alt={1073} border={true} src="https://files.readme.io/67ef30d-2._Create_VIE.png">
  Illustration (Vietnamese)
</Image>

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
        The Depot which directly manages the Customer being created\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Input the Organization Name/Organization Code of the appropriate Depot into the search bar then select it from the drop-down menu\
        **Excel import file:**\
        Copy the Organization Code of the appropriate Depot on the Web app then paste it into this cell\
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
        Time window\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The time period during which the Customer being created will receive deliveries\
        Read more about this configuration in the following article: [**Hard Time Window Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-hard-time-window-constraint)\
        **2. Input rules:**\
        Format: HH:mm-HH:mm (Hour:Minute-Hour:Minute; 24 hour format)\
        Input only the value in numbers. Do not input the unit\
        For example: The customer will only receive products from 5:00 A.M. to 1:00 P.M. Input the following value into this field/cell: ***06:00-13:00***\
        If the Customer being created doesn't have a time window to receive products, leave this field blank
      </td>
    </tr>

    <tr>
      <td>
        Original Address (Webform); Street Address (Excel import file)\
        (Optional)
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
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The coordinate information of the Customer being created\
        **2. Input rules:**\
        Format: Decimal degrees, similar to Google map format\
        For example: ***21.020123; 105.819509***
      </td>
    </tr>

    <tr>
      <td>
        Search Address\
        (Webform)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        This field will help you automatically search for the address and the coordinate of the Customer being created using the Google Maps engine right within the Abivin vRoute Web app\
        **2. Input rules:**\
        Read about this function in the following section: [**Automatically search customer coordinates**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#section-automatically-search-customer-coordinates)
      </td>
    </tr>
  </tbody>
</Table>

#### Email Setting

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

#### Ship-to Profile

* In actual operation, a Customer can receive deliveries from different Depots. Each Depot is very likely to manage the same Customer with different identification information. This identification information is defined as Ship-to profile
* Please refer to this article for more information [Ship-to Profile](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#ship-to-profile)

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
        The unique sales code of the customer being created

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
        A unique Master Delivery Plan code assigned to the customer being created

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
        Tax code of the customer being created

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
        The address to send invoices to the customer being created

        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

### Update Customer Information

* Please refer to this article for detailed instruction on updating customer information [Update Customer Information](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#update-customer-information)

### Delete Customer

* Please refer to this article for detailed instruction on deleting customer information [Delete Customer](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#delete-customer)

### Export Customer List

* Please refer to this article for detailed instruction on exporting Customer List [Export Customer List](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#export-customer-list)

### Search and Filter Customer

* Please refer to this article for detailed instruction on searching and filtering Customer [Search and Filter Customer](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#search-and-filter-customer)

### View Customer Location on Map

* Please refer to this article for detailed instruction on viewing customer location on Map [View Customers Location on Map](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#view-customers-locations-on-map)

### Retrieve Customer Address; Coordinates and Customer Group

#### Manually input Customer address & coordinates

* Please refer to this article for detailed instruction on manually inputting Customer address and Coordinates [Manually input Customer address & coordinates](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#manually-input-customer-address--coordinates)

#### Automatically retrieve Customer address & coordinate

* Please refer to this article for detailed instruction on automatically retrieving Customer address and Coordinates [Automatically retrieve Customer address & coordinates](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-customers#automatically-retrieve-customer-address--coordinate)
