---
title: Manage Organizations (Eng)
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: link
      title: Configurations by Organization type
      url: >-
        https://docs.abivin.com/docs/vrp-in-house-fleet-configurations-by-organization-type
---
## Organization Definition

* In Abivin vRoute system, we strive to simulate the actual Organizational chart of the business, so that the users can manage the resources more efficiently
* The **Organization** resource is created to achieve that. Once you have [registered a master account on our system](https://docs.abivin.com/docs/web-app-account#register-new-account), you can start building your Organizational chart

## Organization Types and Hierarchy Chart

* In Abivin vRoute system in general and in this model in particular, the Organizations can be classified into two types based on whether they are required or optional:
* **Required Organization Type**. The Organization Types that without which your account will not be able to function
* **Optional Organization Type**. The Organization Types that are not strictly required. You can create them later based on your specific needs

### Required Organization Types

Below are the required Organization Types of this model:

* **Manufacturer**. An Organization Type that represents the Headquarter of your business. This Organization Type will manage all resources. A Manufacturer is the top-level Organization. One account can have ***only one*** Manufacturer.
* **Branch**. An Organization Type that represents the Planning Department. This Organization Type will be in charge of the various configurations and the Route Plan optimization process. A Branch is either the direct lower-level Organization of the Manufacturer or the Distributor (The Distributor is described below). One account can have multiple Branches.
* **Depot**. An Organization Type that represents the Warehouse. This Organization Type directly manages the resources that are necessary for the delivery activities, such as Products, Customers; Vehicles and Orders. A Depot is the direct lower-level Organization of the Branch. Each Branch can have multiple Depots beneath it.

### Optional Organization Types

Apart from the required Organization Types above, there are several optional Organization Types:

* **Distributor**. This Organization Type represents the regional branch management office. It is useful if your business spans across a wide geographical area and have multiple smaller branches. The Distributor is the direct lower-level Organization of the Manufacturer and the direct upper-level Organization of the Branch. One account can have multiple Distributors. One Distributor can have multiple Branches beneath it
* **Sun**. Another Warehouse Organization Type, considered as the second-level warehouse below the Depot. The Sun will receive Products from the direct upper-level Depot then distributes them to its own Customer base. A Sun is the direct lower-level Organization of the Depot\
  Read more about this Organization Type in the following article: [**Sun**](https://docs.abivin.com/docs/vrp-in-house-fleet-sun)
* **Crossdock**. Another Warehouse Organization Type, considered as the second-level warehouse below the Depot. The Crossdock will temporarily store Products from the direct upper-level Depot before distributing them to their Customer base. A Crossdock is the direct lower-level Organization of the Depot\
  Read more about this Organization Type in the following article: [**Crossdock**](https://docs.abivin.com/docs/vrp-in-house-fleet-crossdock)
* **Shipper**. This is a special Organization Type. It is used when you set up your account as a third-party logistics service provider (Carrier or Distributor), having business relationships with various suppliers/owners of Products. This Organization Type represents the Product suppliers/owners. A Shipper is the direct lower-level Organization of either the Distributor or the Manufacturer\
  Read more about this Organization Type in the following article: [**Shipper**](https://docs.abivin.com/docs/vrp-dc-shipper)

## Account Setup Orientation

* In this model, you can set up your account in two orientations: Shipper-oriented and Carrier/Distributor-oriented

### Shipper-oriented Account Setup

* You should set up your account in this orientation if you are the Shipper, the supplier/owner of the Products. You have your own vehicle fleet and you use your vehicle fleet to distribute your Products to the distribution channels or the consumers
* This account setup orientation has several characteristics:
* 1 - Organizational chart: Your organizational chart does not need to have the Organizations of Shipper type
* 2 - Product management mechanism: You need to select the Shipper-oriented Product management mechanism, which is described in the [**Manage Product Categories**]() and [**Manage Products**]() article

### Carrier/Distributor-oriented Account Setup

* You should set up your account in this orientation if you are the Carrier and/or the Distributor, provide third-party logistics services for the Shippers such as transportation and warehousing. You have your own vehicle fleet and you use your vehicle fleet to distribute the Shippers' Products to the distribution channels or the consumers
* This account setup orientation has several characteristics:
* 1 - Organizational chart: Your organizational chart needs to have the Organizations of Shipper type. Each Shipper Organization represents one Shipper with which you has a business relationship
* 2 - Product management mechanism: You need to select the Carrier/Distributor-oriented Product management mechanism, which is described in the [**Manage Product Categories**]() and [**Manage Products**]() article

## Locate Organization List

* The Organizations are listed on the **Organizations > Organizations** tab

<Image title="Org list.png" alt={1676} border={true} src="https://files.readme.io/d6b1903-Org_list.png">
  Illustration (English)
</Image>

<Image title="1.png" alt={1920} border={true} src="https://files.readme.io/fc569bb-1.png">
  Illustration (Vietnamese)
</Image>

## Create Organizations

* You have two methods to create the Organizations: Webform and Excel import file

### Create the Manufacturer

* The Manufacturer is the first Organization you have to create. This Organization can only be created using the Webform
* To create the Manufacturer, follow the steps below
* Step 1: On the **Organizations > Organizations** tab (The screen that you see right after logging in to your newly created account), hover over the circle plus icon :fa-plus-circle: then click the **Create** icon :fa-pencil: 
* Step 2: On the **Create Organization** Webform, input the Organization Code and the Organization Name of the Manufacturer into the **Organization Code** and **Organization Name** fields then click **Save**

<Image title="6MIhbJT5Iq.png" alt={745} border={true} src="https://files.readme.io/4e04a43-6MIhbJT5Iq.png">
  Illustration (English)
</Image>

<Image title="lhNNUsZdbO.png" alt={745} border={true} src="https://files.readme.io/1108635-lhNNUsZdbO.png">
  Illustration (Vietnamese)
</Image>

* After the Manufacturer has been created, click its **Edit** icon :fa-pencil:. On the **Update Organization** form, click on the **Parent Organization** field and select itself as its own Parent Organization. Next, click on the **Organization Categories** field, select the ***Manufacturer*** Organization Type from the drop-down menu. Click **Save** to confirm the change

<Image title="TPN7EOgpTA.png" alt={741} border={true} src="https://files.readme.io/5e34ff1-TPN7EOgpTA.png">
  Illustration (English)
</Image>

<Image title="jCkCPXljZN.png" alt={745} border={true} src="https://files.readme.io/23f8aec-jCkCPXljZN.png">
  Illustration (Vietnamese)
</Image>

* Now the Manufacturer has been fully set up. You can move on to create other lower-level Organizations using either the Webform or the Excel import file

### Create Lower-level Organizations

* After the Manufacturer has been created, you can create other lower-level Organizations using either the Webform or the Excel import file
* If you create the Organizations using the Excel import file, there are some notes that you should be aware of:
* 1 - When you create the direct lower-level Organizations of the Manufacturer - The Distributor or the Branch, you must copy the exact Organization Code of the Manufacturer on the Web app then paste that value into the **Parent Organization Code** cell of the Distributor/Branch being created in the Excel import file

<Image title="2019-10-23 13_54_14-Window.png" alt={1674} border={true} src="https://files.readme.io/e5161e8-2019-10-23_13_54_14-Window.png">
  Illustration (English)
</Image>

<Image title="6.png" alt={1920} border={true} src="https://files.readme.io/45b1e28-6.png">
  Illustration (Vietnamese)
</Image>

* 2 - When you create the Organizations that have yet to exist on the Web app, follow this step to create the parent-child relationship between an upper-level Organization and its direct lower-level Organizations (For example, a Branch and its Depot) in the Excel import file: Copy the Organization Code of the upper-level Organization from its **Organization Code** cell then paste that value into the **Parent Organization Code** cells of its direct lower-level Organizations

<Image title="2019-09-08 22_48_58-Window.png" alt={1917} border={true} src="https://files.readme.io/d22f800-2019-09-08_22_48_58-Window.png">
  Illustration Image (English)
</Image>

<Image title="7.png" alt={1919} border={true} src="https://files.readme.io/0eaca0d-7.png">
  Illustration Image (Vietnamese)
</Image>

### Organization Information Fields

* Below are the information fields and input rules for the Organization of this model

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Description & Input Rules
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organization Code
        (Webform + Excel import file)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Organization Code assigned to the Organization being created\
        **2. Input rules:**\
        Format: Can contain letters, numbers, special characters. Must not contain spaces\
        For example, "Org\_01" is valid; "Org 01" is invalid\
        **Notes:**\
        When you use the Webform, the input value will automatically be capitalized\
        For example: If you input the value "Sample\_Organization\_Code", it will automatically be capitalized into "SAMPLE\_ORGANIZATION\_CODE"\
        When you use the Excel import file, the input value will not be automatically capitalized after importing\
        This code is case sensitive\
        For example, "Sample\_Organization\_Code" is different from "SAMPLE\_ORGANIZATION\_CODE". Please pay attention when copying the code
      </td>
    </tr>

    <tr>
      <td>
        Organization Name\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Name of the Organization being created\
        **2. Input rules:**\
        Format: Can contain letters, numbers, special characters, and spaces
      </td>
    </tr>

    <tr>
      <td>
        Parent Organization (Webform); Parent Organization Code (Excel import file)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The direct upper-level Organization of the Organization being created\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Input the Organization Name/Organization Code of the upper-level Organization of the Organization being created into the search bar, then select it from the drop-down menu\
        **Excel import file:**\
        Copy the Organization Code of the upper-level Organization of the Organization being created on the Web app, then paste it into this cell\
        **Note:**\
        The Organization Name and Organization Code can be found under the "Organization Name" and "Organization Code" columns in the "Organizations > Organizations" tab
      </td>
    </tr>

    <tr>
      <td>
        Organization Category (Webform); Organization Category Code (Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Specify the Organization Type of the Shipper being created\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Select the appropriate Organization Type from the drop-down menu\
        **Excel import file:**\
        If the Organization being created is a Distributor, input the following value into this cell (Remove the quotation marks when inputting): ***"DISTRIBUTOR"***\
        If the Organization being created is a Branch, input the following value into this cell (Remove the quotation marks when inputting): ***"BRANCH"***\
        If the Organization being created is a Depot, input the following value into this cell (Remove the quotation marks when inputting): ***"DEPOT"***\
        If the Organization being created is a Sun, input the following value into this cell (Remove the quotation marks when inputting): ***"SUN"***\
        If the Organization being created is a Crossdock, input the following value into this cell (Remove the quotation marks when inputting): ***"CROSSDOCK"***\
        If the Organization being created is a Shipper, input the following value into this cell (Remove the quotation marks when inputting): ***"SHIPPER"***\
        **Notes when using the Excel import file:**\
        You must input the values exactly in English and in uppercase letters, as shown above. Do not input in any other language and lowercase letters
      </td>
    </tr>

    <tr>
      <td>
        Latitude, Longitude\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The coordinate information of the Organization being created\
        **2. Input rules:**\
        Format: Decimal Degrees\
        For example: 41.40338 and 2.17403\
        Read this article for instruction: [**Get coordinate information of places**](https://docs.abivin.com/docs/how-to-get-coordinates-of-places)\
        **Note:**\
        These information fields are very important for Organizations of Depot/Sun/Crossdock types as they will be used during the Route Plan Optimization process
      </td>
    </tr>

    <tr>
      <td>
        Open Time; Close Time\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The official working time of the Organization being created\
        **2. Input rules:**\
        Format: HH:mm (Hour:Minute; 24 hour format)\
        For example, the Organization being created starts working at 08:30 A.M and closes at 05:30 P.M everyday. You need to input the following values in the "Open Time" and "Close Time" fields/cells respectively: ***08:30; 17:30***\
        **Note:**\
        The "Open Time" field is very important for Organizations of Depot; Sun; Crossdock types as it will be used during the Route Plan Optimization process
      </td>
    </tr>

    <tr>
      <td>
        Phone Number\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Phone number of the Organization being created\
        **2. Input rules:**\
        Format: Numbers only. Must not contain spaces\
        For example: "0901810800" is valid; "090 181 0800" or "090.181.0800" is invalid
      </td>
    </tr>

    <tr>
      <td>
        Address\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Official address where the Organization being created is located\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Country\
        (Webform)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Set the country where your business locates\
        **2. Input rules:**\
        Click on this field, select the appropriate country from the drop-down list
      </td>
    </tr>

    <tr>
      <td>
        Currency\
        (Webform)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Set the currency unit throughout the system\
        **2. Input rules:**\
        The currency unit will automatically update as you select the Country information above\
        You can manually set the currency unit by clicking on this field and select the appropriate currency unit from the drop down list
      </td>
    </tr>

    <tr>
      <td>
        SMS Branding\
        (Webform)\
        (Optional)
      </td>

      <td>
        **This information field is only required for some specific accounts**\
        **1. Description:**\
        The SMS Branding service that your Organization currently uses\
        **2. Input rules:**\
        Format: Text and numbers
      </td>
    </tr>

    <tr>
      <td>
        First weekday\
        (Webform)\
        (Optional)
      </td>

      <td>
        **This information field is only required for some specific accounts**\
        **1. Description:**\
        Set the first working day in a week\
        This value will affect a particular report\
        **2. Input rules:**\
        Click on this field. Select the appropriate day from the drop down list
      </td>
    </tr>

    <tr>
      <td>
        Working days\
        (Webform)\
        (Optional)
      </td>

      <td>
        **This information field is only required for some specific accounts**\
        **1. Description:**\
        Set the working days in a week\
        This value will affect a particular report\
        **2. Input rules:**\
        Click on this field. Select the appropriate day from the drop down list
      </td>
    </tr>

    <tr>
      <td>
        TimeZone\
        (Webform)\
        (Optional)\
        (Only effective for Manufacturer)
      </td>

      <td>
        **1. Description:**\
        The Timezone of your Organization's geographical location\
        **2. Input rules:**\
        Click on this field. Select the appropriate time zone from the drop down list
      </td>
    </tr>

    <tr>
      <td>
        Founded At\
        (Webform)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The date when the organization was officially established\
        **2. Input rules:**\
        Click on the calendar icon. Select the appropriate date from the drop down calendar
      </td>
    </tr>

    <tr>
      <td>
        Description\
        (Webform)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A short description about the organization being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Time Break\
        (Webform)\
        (Optional)
      </td>

      <td>
        **This information field is only required for some specific accounts**\
        **1. Description:**\
        The time break during which the Depot being created will not allow the vehicles to come in and pick up products\
        **2. Input rules:**\
        Format: HH:mm (Hour:Minute; 24 hour format)\
        If there are multiple time breaks, separate two adjacent time breaks by a colon (;)\
        For example: A Depot has two time break periods: From 8 A.M to 9:30 A.M and from 11:30 A.M to 1:30 P.M. Input the following value into this field:\
        ***08:00-09:30;11:30-13:30***
      </td>
    </tr>
  </tbody>
</Table>

#### Organization Information On Webform

* On the Webform, the information of an Organization is present on two tabs: **Main Information** and **More Configuration**
* The Main Information tab holds the basic information of the Organization
* The More Configuration tab holds the specific information for each Organization Type. As you select the attribute **Organization Category** on the **Main Information** tab, this tab will update accordingly and gray out the information fields not related to the selected Organization Type

<Image title="zguejJcl6u.png" alt={1452} border={true} src="https://files.readme.io/738c704-zguejJcl6u.png">
  Illustration (English)
</Image>

<Image title="3.png" alt={1494} border={true} src="https://files.readme.io/797c30c-3.png">
  Illustration (Vietnamese)
</Image>

* We have a dedicated article for the configurations on the More Configuration tab: [**Configurations by Organization Type**](https://docs.abivin.com/docs/vrp-in-house-fleet-configurations-by-organization-type)

## Update Organization

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Delete Organization

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

> ❗️ BE VERY CAREFUL WHEN DELETING ORGANIZATIONS
>
> If you delete an organization, all resources of that organization as well as the resources of all organizations beneath it will be deleted\
> For example: If you delete a Branch, the resources of that Branch as well as of all Depots directly under that Branch will be deleted

## Search and Filter Organization

### Search Organization

* Enter either the **Organization Code** or the **Organization Name** of the organization you want to search in the search box :fa-search: 
* The system will filter and return result shortly

<Image title="Search org.gif" alt={1672} border={true} src="https://files.readme.io/55364f1-Search_org.gif">
  Illustration Image (English)
</Image>

<Image title="Search.gif" alt={1920} border={true} src="https://files.readme.io/cf227aa-Search.gif">
  Illustration Image (Vietnamese)
</Image>

### Filter Organization

* You can filter Organization that are the same **Organization Type** or share the same **Parent Organization** by clicking on the **Organization Categories** and **Parent Organization** columns then ticking on boxes in the drop down menus

<Image title="2019-10-14 09_47_15-Window.png" alt={1674} border={true} src="https://files.readme.io/2d23aca-2019-10-14_09_47_15-Window.png">
  Illustration Image (English)
</Image>

<Image title="Sort.gif" alt={1920} border={true} src="https://files.readme.io/894d8c1-Sort.gif">
  Illustration Image (Vietnamese)
</Image>

* You can also search an organization quicker by typing the ***Organization Name*** or ***Organization Code*** of its upper level organization in the search bar of **Parent Organization** column; or the ***Organization Type*** in the search bar **Organization Categories** column

<Image title="Untitled Project.gif" alt={1920} border={true} src="https://files.readme.io/3b69362-Untitled_Project.gif">
  Illustration Image (English)
</Image>

<Image title="Vie.gif" alt={1920} border={true} src="https://files.readme.io/244d899-Vie.gif">
  Illustration Image (Vietnamese)
</Image>

* You can combine these two filters for more accurate search results

## Locate Organizations on the map

* To view locations of organizations on the map, click on **View Map** icon (Next to the **Search** :fa-search: field)

<Image title="2019-10-14 09_49_08-Window.png" alt={1672} border={true} src="https://files.readme.io/a512d5d-2019-10-14_09_49_08-Window.png">
  Illustration Image (English)
</Image>

<Image title="1.png" alt={1920} border={true} src="https://files.readme.io/a8ddd0a-1.png">
  Illustration Image (Vietnamese)
</Image>

* On the map, each organization is marked by a :fa-map-marker: symbol
* Click on each :fa-map-marker: symbol to show the label of the organization
* Click on **View data table** :fa-table: icon to get back to the organization list screen

<Image title="2019-10-14 09_50_02-Window.png" alt={1672} border={true} src="https://files.readme.io/7a3c446-2019-10-14_09_50_02-Window.png">
  Illustration Image (English)
</Image>

<Image title="2.png" alt={1920} border={true} src="https://files.readme.io/a94622b-2.png">
  Illustration Image (Vietnamese)
</Image>

## Beginner's Guide

* This section is intended for new users who have just started using the system. We will provide you the most basic setup to get you up and running as quickly as possible. After you have complete the basic, feel free to tinker around on your own
* Fundamentally, in your account, you will need an Organization hierarchy that consists of one Manufacturer, one Branch, and one Depot

<Image title="org chart.png" alt={281} className="border" border={true} src="https://files.readme.io/e094392-org_chart.png" />

### Create the Manufacturer

* To start off, let's create an Organization of **Manufacturer** type.
* Step 1: Navigate to the **Organizations > Organizations** tab.
* Step 2: Hover over the orange plus circle icon :fa-plus-circle: then click the **Create** icon :fa-pencil:

- Step 3: On the Webform, input the information of your Manufacturer as per the instruction in the [**Create the Manufacturer**](https://docs.abivin.com/docs/vrp-dc-manage-organizations-eng#create-the-manufacturer) section above

### Create the Branch and the Depot

* Next, let's move on to create the Branch and the Depot
* Since you are probably familiar with using the Webform by now, I suggest you switch to using the Excel import file for this task. Using the Excel import file is also much preferred when you want to create multiple Organizations (Or other resources for that matter) at once
* In the Excel import file, let's do as below:
* For the Branch, you just need to input its information into the following cells: **Organization Code; Organization Name; Parent Organization Code; Organization Category Code**. Do note that you need to copy the Organization Code of the Manufacturer created above from the Web app then paste that value into the **Parent Organization Code** cell of the Branch being created to generate the parent-child relationship between these two Organizations
* For the Depot, you just need to input its information into the following cells: **Organization Code; Organization Name; Parent Organization Code; Latitude; Longitude; Open Time; Close Time; Min Time (minute); Max Time (minute); Organization Category Code**. For the **Parent Organization Code** cell, copy and paste the value from the **Organization Code** of the Branch above to generate the parent-child relationship between these two Organizations
* Please refer to the following section to know the description and the input rules for the above information fields: [**Organization Information Fields**](https://docs.abivin.com/docs/vrp-dc-manage-organizations-eng#organization-information-fields)
