---
title: Manage Customer Groups
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
## Definition of Customer Group

* In Abivin vRoute, you can allocate the customer base of a Depot into separate customer groups. There are three types of customer groups:
* **Type 1: Multi-associated customer groups:** Customer groups that have associations with other Customer groups

<Image title="inter group.png" alt={81} border={true} src="https://files.readme.io/1e44949-inter_group.png">
  Multi-associated customer group
</Image>

* **Type 2: Self-associated customer groups:** Customer groups that are independent. They do not have any association with other Customer groups

<Image title="self-associated.png" alt={83} border={true} src="https://files.readme.io/ba02d81-self-associated.png">
  Self-associated customer group
</Image>

* **Type 3: No-associated customer groups:** Customer groups that are neither Multi-associated nor Self-associated

<Image title="normal group.png" alt={83} border={true} src="https://files.readme.io/c9880f2-normal_group.png">
  No-associated customer group
</Image>

* During the route optimization process, the vehicle fleet of a Depot will be utilized according to the following rules:
* First, some vehicles will be selected to only deliver to Multi-associated customer groups which have associations between themselves
* Next, some of the remaining vehicles will be selected to only deliver to each of the Self-associated customer groups. Note that no two Self-associated customer groups share the same delivery vehicles with each other
* Finally, the remaining vehicles will be selected to deliver to No-associated customer groups, as well as customers who do not belong to any particular customer group
* Below is an illustration to help you understand easier

<Image title="csgroup.png" alt={689} className="border" border={true} src="https://files.readme.io/2cec8a0-csgroup.png" />

## Access Customer Group List

* The Customer Groups are listed in the **Partners > Customer Groups** tab

<Image title="cg eng.png" alt={1920} border={true} src="https://files.readme.io/0a9adc2-cg_eng.png">
  Illustration (English)
</Image>

## Create Customer Groups

* You have two methods to create Customer Groups: Webform or Excel template

### Customer group information fields

* Below is the list of information fields of a Customer Group

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
        Organizations (Web form); Organization Code (Excel template)
        (Required)
      </td>

      <td>
        **1. Description:**\
        Branch which manages the customer group being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field, then select the suitable Branch\
        **Excel template:**\
        Copy the Organization Code of Branch on Web app then paste into this cell\
        The Organization Code can be found under "Organization Code" column in "Organizations > Organization List" tab
      </td>
    </tr>

    <tr>
      <td>
        Group Code (Web form); Partner Group Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the customer group being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Group 01" is invalid; "Group\_01" is valid
      </td>
    </tr>

    <tr>
      <td>
        Group Name (Web form); Partner Group Name (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Name of the customer group being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Group Parent (Web form); Parent Group Code (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The upper level Customer group in which the customer group being created belongs\
        **2. Input rules:**\
        This information field is used for CRM model, and does not have any effect on Routing plan model. Just leave the field/cell blank
      </td>
    </tr>

    <tr>
      <td>
        Group Time Windows\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The time window(s) of the Customer Group being created\
        The delivery fleet can only deliver to the Customers of the Customer Group during the time windows input here\
        If you use the user-drawing Geographical clusters feature, this information will be required. Read more in the following article: [**Geographical Clustering**](https://docs.abivin.com/docs/vrp-in-house-fleet-geographical-clustering#geographical-clustering-by-user-drawing)\
        **2. Input rules:**\
        Format: HH:mm-HH:mm (Hour:Minute-Hour:Minute, 24 hour format)\
        If the Customer Group has multiple time windows, separate two adjacent time windows only by a semicolon (;)\
        For example: ***04:00-11:00;13:00-22:00***
      </td>
    </tr>

    <tr>
      <td>
        Associated Group & Self-associated (Web form); Associated Group Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**

        * \*Associated Groups\*\*: The field to specify the Customer group(s) with which the customer group being created has association, if it is an Inter-associated customer group
        * \*Self-associate&#x64;**: The checkbox to confirm whether the customer group being created is a self-associated customer group or not\&#xA;**&#x32;. Input rules:\*\*\
          **Web form:**\
          If the Customer group being created is an Inter-associated customer group: Click on the "Associated Group" field, select the suitable Customer group to associate from the drop down menu. You can select multiple customer groups\
          If the Customer group being created is Self-associated: Click on "Self-associated" checkbox\
          If the Customer group being created is a Normal customer group: Do not input anything\
          **Excel template:**\
          If the Customer group being created is an Inter-associated Customer group: Copy the group code(s) of the Customer group(s) with which it associates, and paste into this cell\
          The Customer Group code can be found under "Group Code" column in  "Partners > Customer Groups" tab\
          If the Customer group being created has more than one associated Customer group, separate two adjacent associated customer group codes only by a comma\
          For example: **Group\_01,Group\_02**\
          If the Customer group being created is a Self-associated Customer group: Copy its own Group code in the "Partner Group Code" cell and paste into this cell\
          If the Customer group being created is Normal Customer group: Leave this cell blank
      </td>
    </tr>

    <tr>
      <td>
        Group description\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A short description of the customer group being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Partner Group Type\
        (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Type of the group being created\
        **2. Input rules:**\
        Always input the following value into this cell: CUSTOMER
      </td>
    </tr>

    <tr>
      <td>
        Group Cluster (Web form); Clustering Group Type (Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The geographic clustering level applied to the Customer Group being created\
        There are three possible geographic clustering levels, from highest to lowest: By Province, By District, By Town\
        **2. Input rules:**\
        Refer to the following section: Customer Group Geographic Clustering
      </td>
    </tr>

    <tr>
      <td>
        Province\
         (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The province(s) in which Customers of the Customer Group being created locate\
        **2. Input rules:**\
        Refer to the following section: Customer Group Geographic Clustering
      </td>
    </tr>

    <tr>
      <td>
        District\
         (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The district(s) in which Customers of the Customer Group being created locate\
        **2. Input rules:**\
        Refer to the following section: Customer Group Geographic Clustering
      </td>
    </tr>

    <tr>
      <td>
        Town\
         (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The town(s) in which Customers of the Customer Group being created locate\
        **2. Input rules:**\
        Refer to the following section: Customer Group Geographic Clustering
      </td>
    </tr>
  </tbody>
</Table>

### Notes when creating Multi-associated Customer Groups

* If some customer groups have associations with each other, you have to specify the associated customer groups for each one of them. See illustrations below of three Multi-associated customer groups

<Image title="Untitled-2.png" alt={858} border={true} src="https://files.readme.io/1528308-Untitled-2.png">
  Specify associated customer groups on Web app
</Image>

<Image title="2019-11-03 16_39_32-Window.png" alt={560} border={true} src="https://files.readme.io/ac973db-2019-11-03_16_39_32-Window.png">
  Specify associated customer groups in Excel template
</Image>

## Allocate Customers To Customer groups

### Allocate Customers Using The Webform

* If there are just several Customers which have been created earlier than the Customer Groups, you can use the Webform to allocate them to the Customer Groups
* 1 - Navigate to **Partners > Customers** tab
* 2 - Click the **Edit** icon :fa-pencil: of the wanted Customer
* 3 - The **Update Customer** form will appear. In this form, click on the **Customer Groups** field. Tick the checkbox of the Customer Group to which you want to allocate the Customer being edited. You can also input the Customer Group Code/Customer Group Name of the desired Customer Group into the search bar to filter faster
* **Important note**: Even though you can select multiple Customer Groups, in this model one Customer can only belong to ***one*** Customer Group. If you select multiple Customer Groups for a Customer, the system will not be able to generate the optimized Delivery Route for that Customer during the Route Plan optimization process
* 4 - Click **Save** to confirm the change

<Image title="Untitled 2.gif" alt={1920} border={true} src="https://files.readme.io/b6d5af2-Untitled_2.gif">
  Illustration (English)
</Image>

<Image title="2402.gif" alt={1920} border={true} src="https://files.readme.io/275f074-2402.gif">
  Illustration (Vietnamese)
</Image>

### Allocate Customers Using The Excel Import File

* If there are: 1. multiple Customers which have been created earlier than the Customer Groups, or 2. multiple new Customers, you can use the Excel import file to allocate them to the Customer Groups
* 1 - Download the Excel import file from the Web app. Input the information of the new Customers as well as the existing Customers which you want to allocate to the Customer Groups 
* **Note**: For the existing Customers, you can export them to the Excel file, then copy the information from the export file into the import file
* 2 - Copy the **Customer Group Code** of the appropriate Customer Group on the Web app. The Customer Group Code can be found under the **Group Code** column in the **Partners > Customer Groups** tab 
* 3 - In the Customer Excel import file, paste the Customer Group Code into the **Partner Group Code** cell of each Customer
* 4 - Upload the Customer Excel import file onto the Web app

<Image title="Merged 1.png" alt={1920} border={true} src="https://files.readme.io/bf84e55-Merged_1.png">
  Illustration (English)
</Image>

<Image title="Merged 3.png" alt={1920} border={true} src="https://files.readme.io/2c6e057-Merged_3.png">
  Illustration (Vietnamese)
</Image>

## Update Customer Groups

* You have two methods to update Customer Groups
* Method 1: Update a single Customer Group using the Webform
* Method 2: Update multiple Customer Groups using the Excel import file

## Update Single Customer Group Using The Webform

## Bulk Update Multiple Customer Groups Via Excel Import File

* If you wish to update multiple Customer Groups at once, you can use the Excel Customer Group import file
* To do that, perform the steps below:
* 1: Copy the management codes of the Customer Groups you wish to update from the Web App (Can be found under **Group Code** column in tab **Partners > Customer Groups**) and the Organization Codes of their managing Depots (Can be found under **Organization Code** column in **Organizations > Organizations** tab) then paste into the **Partner Group Code** and **Organization Code**cells in the Excel import file, respectively
* 2: Input the new information of the Customer Groups into other cells then save the file
* 3: Open the **Upload Data** form. On this form, tick the **Overwriting existing data** checkbox then upload the Excel import file. Upon importing, the system will replace the data of the existing Customer Groups as you intend

<Image title="n8WHUk8jhI.png" alt={1184} border={true} src="https://files.readme.io/f31503a-n8WHUk8jhI.png">
  Upload Data Form (English & Vietnamese)
</Image>

## Route optimization

* After configuring the customer groups as above, you can proceed to create orders and optimize routes as usual
* The system will perform checking the data of the customers to see what customer groups they belong to, and allocate the vehicles accordingly
* Below is an example of using customer groups
* Customer ***Customer-01-017*** belongs to Customer group ***Associated Group 01***; Customer ***Customer-01-016*** belongs to Customer group ***Associated Group 02***. These two customer groups are Inter-associated customer groups and have associations with each other
* Customer ***Customer-01-015*** belongs to Customer group ***Self-associated Group 01***; Customer ***Customer-01-014*** belongs to Customer group ***Self-associated Group 02***. These two customer groups are two Self-associated customer groups
* Customer ***Customer-01-013*** belongs to customer group ***Normal Group 01***; Customer ***Customer-01-012*** belongs to customer group ***Normal Group 02***. These two customer groups are Normal customer groups
* Customer ***Customer-01-011*** doesn't belong to any customer group

<Image title="2019-11-03 15_49_44-Window.png" alt={1066} className="border" border={true} src="https://files.readme.io/110f5aa-2019-11-03_15_49_44-Window.png" />

* These seven customers place orders on the same date. During the route optimization process, the vehicles fleet have been allocated as follow:
* One vehicle will deliver to ***Customer-01-017*** and ***Customer-01-016*** only
* One vehicle will deliver to ***Customer-01-015*** only
* One vehicle will deliver to ***Customer-01-014*** only
* One vehicle will deliver to ***Customer-01-013***, ***Customer-01-012*** and ***Customer-01-011***

<Image title="2019-11-03 15_59_37-Window.png" alt={1914} className="border" border={true} src="https://files.readme.io/2e5f7a7-2019-11-03_15_59_37-Window.png" />

## Customer Group Geographic Clustering by Administrative Division

* Customer Group by Administrative Division is a feature to help group Customers that locate in the same administrative division (Province/District/Town). During the Route Plan Optimization process, the routing algorithm will use this information to distribute the delivery vehicles accordingly. Read more in this article: [**Geographic Clustering by Administrative Divisions**](https://docs.abivin.com/docs/vrp-in-house-fleet-geographical-clustering#geographical-clustering-by-administrative-divisions)

## Customer Group Geographic Clustering by User-drawing

## Beginner's Guide

### Create a Customer Group

* Here is how you can create a customer group using Web form:
* Step 1: Navigate to **Partners > Customer Groups** tab.
* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Create** (the :fa-pencil: symbol).

![2880](https://files.readme.io/6b33a68-Screen_Shot_2021-01-22_at_15.18.11.png "Screen Shot 2021-01-22 at 15.18.11.png")

* Step 3: Input the required fields:
* **Organizations:** Input Branch which manages the customer group being created: ***Sample Branch***
* **Group Code:** Input the management code assigned to the customer group being created: ***SAMPLE-CUSTOMERGROUP***
* **Group Name:** Input the name of the customer group being created: ***Sample Customer Group***
* **Associated Group:** Choose one of the three types of customer groups: No-associated; Self-associated; Multi-associated. Please click [here](https://docs.abivin.com/docs/vrp-in-house-fleet-customer-groups#definition-of-customer-group) to learn more about these types.
* *Example:* 

![2880](https://files.readme.io/b68e16a-Screen_Shot_2021-01-22_at_15.24.51.png "Screen Shot 2021-01-22 at 15.24.51.png")

* To learn more about notes and input rules of the fields above, please click [here](https://docs.abivin.com/docs/vrp-in-house-fleet-customer-groups#definition-of-customer-group).
* Step 4: Click **SAVE**.
