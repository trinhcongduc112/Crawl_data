---
title: Manage Actions
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
## Action Definition

* During a typical delivery process, the drivers need to perform certain manual tasks, which includes (In chronological order): 
* 1 - Check-in at the Depot at the beginning of the working day or working shift
* 2 - Load products onto the delivery vehicles and leave the Depot
* 3 - Check-in at the Customer locations upon arriving, hand over products to the Customers, receive payment, and confirm the delivery result
* 4 - Travel back to the Depot; hand over collected payment and returned products (If available) to the warehouse managers, perform necessary paperwork, and finally Check-out of the Depot, end their working shift (or working day)
* Apart from the usual delivery tasks, unexpected events might occur that hinder the delivery process, such as vehicle failure; traffic jams, etc.. The drivers need to record those events and inform the dispatchers
* To help the dispatcher manage the tasks of the drivers in the most efficient way possible, in Abivin vRoute we provide the **Actions** feature. This feature allows the dispatchers to digitize the actual manual delivery tasks of the drivers by shifting them onto the Mobile app, provide a solution to manage the works of the drivers on the Web app in real-time, getting rid of the tedious manual paperwork. Each of the delivery tasks mentioned above will be represented by a resource called the **Action Code**

## Locate Action Code list

* Action Codes are listed in the **Tasks > Actions** tab

<Image title="Screen Shot 2021-02-25 at 09.25.06.png" alt={2880} border={true} src="https://files.readme.io/c3ad7ce-Screen_Shot_2021-02-25_at_09.25.06.png">
  Illustration (English)
</Image>

<Image title="Screen Shot 2021-02-25 at 09.26.09.png" alt={2878} border={true} src="https://files.readme.io/72eaf43-Screen_Shot_2021-02-25_at_09.26.09.png">
  Illustration (Vietnamese)
</Image>

## Create Action Codes

* On the **Tasks > Actions** tab you will notice that a set of Action Codes has been automatically created. These are the default Action Codes of the VRP/DC model
* In case the Action Code list is empty or the Action Codes appear differently than the ones shown in the Action Code table below, you need to create the correct Action Codes using the Excel import file. **DO NOT** use the Webform to create the Action Codes

### Action Code information fields

* Below are the Action Codes of this model
* Notes: Delete the quotation marks when you input the Action Codes in the Excel import file

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action Code
      </th>

      <th>
        Action Name (Can be changed)
      </th>

      <th>
        Action Description
      </th>

      <th>
        Organization Code
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "LOADING\_AT\_DEPOT"
        (Required)
      </td>

      <td>
        Load Products at Depot
      </td>

      <td>
        The drivers check in and load products at the Depot at the beginning of  the Delivery Trip
      </td>

      <td>
        Always input the Organization Code of the: **Manufacturer**
      </td>
    </tr>

    <tr>
      <td>
        "DELIVER\_PRODUCT"\
        (Required)
      </td>

      <td>
        Deliver Products to customer
      </td>

      <td>
        The drivers travel to the customers' locations, hand over the products to the customers, receive payment and confirm delivery results
      </td>

      <td>
        Always input the Organization Code of the: **Manufacturer**
      </td>
    </tr>

    <tr>
      <td>
        "BACK\_DEPOT"\
        (Required)
      </td>

      <td>
        Go back to Depot
      </td>

      <td>
        The drivers travel back to the Depot, hand over collected money and returned products (If available) to the Depot manager and perform required warehouse paperworks
      </td>

      <td>
        Always input the Organization Code of the: **Manufacturer**
      </td>
    </tr>

    <tr>
      <td>
        "END\_DAY"\
        (Required)
      </td>

      <td>
        End Delivery shift
      </td>

      <td>
        The drivers check out of the Depot, end their Delivery Shift
      </td>

      <td>
        Always input the Organization Code of the: **Manufacturer**
      </td>
    </tr>

    <tr>
      <td>
        "EXTRA\_TASK"\
        (Optional)
      </td>

      <td>
        Extra Task
      </td>

      <td>
        The drivers inform unexpected event during the Delivery process
      </td>

      <td>
        Always input the Organization Code of the: **Manufacturer**
      </td>
    </tr>
  </tbody>
</Table>

* Here is how the Action Codes Excel import file should look like:

<Image title="NbPpVbZ0Hd.png" alt={829} border={true} src="https://files.readme.io/ff70114-NbPpVbZ0Hd.png">
  Illustration (English + Vietnamese)
</Image>

## Create Forms For Action Codes

* The Action Codes recently created have not yet had any information inside. Imagine them as blank Excel spreadsheets. In order for the Mobile app users to see and perform their tasks on the Mobile app, you have to build the display/input fields for each Action Code using the **Form Building** function

### Enable Form Building Function

* By default, the system will not allow you to create forms for the Action Codes. In the **Tasks > Actions** tab, under the **Edit** column there are only two icons like so

<Image title="Hjhqqk77U7.png" alt={1458} className="border" border={true} src="https://files.readme.io/0fb8582-Hjhqqk77U7.png" />

* You need to enable the Form Building function for the Top Administrator User Group
* To do this, follow the steps below:
* 1 - Navigate to the **Organizations > User Groups** tab
* 2 - Click the **Edit** icon :fa-pencil: of the Administrator User Group of the Manufacturer
* 3 - On the **Update Group** form, scroll down until you see the **Module** section. Tick the ***All*** checkbox of the **Task Actions** module

<Image title="N0UqarKnWd.png" alt={1682} className="border" border={true} src="https://files.readme.io/9afad11-N0UqarKnWd.png" />

* 4 - Click **Save** to confirm the change
* Now, navigate back to the **Tasks > Actions** tab and refresh your Web app (Hit the **Ctrl F5** key combination on your keyboard). After refreshing, notice there are two more icons under the **Edit** column

<Image title="3dgzuZjq2m.png" alt={1349} className="border" border={true} src="https://files.readme.io/1a12b7e-3dgzuZjq2m.png" />

* Notice the cog icon :fa-cog:. It is the **Form Builder** icon. This will allow you to build forms for the Action Codes

### General Steps To Build Forms For Action Codes

* Each Action Code will display different information and require different input from the Mobile app users, therefore each of them needs to have different forms
* This section will explain only the most general steps to build the forms for an Action Code. Below we will explain in more details the specific information needed for each Action Code
* Below are the general steps to build forms for an Action Codes 
* 1 - Click the **Form Builder** icon :fa-cog: of the Action Code

<Image title="iHSajK7nLs.png" alt={1453} className="border" border={true} src="https://files.readme.io/71d9cdb-iHSajK7nLs.png" />

* 2 - You will be navigated to the **Form Builder** screen

<Image title="2019-11-02 21_55_10-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/24f85fc-2019-11-02_21_55_10-Window.png" />

* 3 - You will see a blue button titled **Submit**. You need to remove that button by hovering your mouse over it, then click on the red remove icon :fa-remove: on the far right

<Image title="zip4MIrvia.png" alt={1314} className="border" border={true} src="https://files.readme.io/1ae93de-zip4MIrvia.png" />

* 4 - Now, look at the panel on the left side. This is the Component panel, from which you can select which component to use for the Action Code
* There are three sub-sections on this panel: **Basic Components; Special Components; Layout Components**. Clicking on each sub-section title will reveal the components of that sub-section

<Image title="VSPiVJcEvB.png" alt={1574} className="border" border={true} src="https://files.readme.io/df52bb3-VSPiVJcEvB.png" />

* To use a component for the Action Code, simply left-click and drag that component to the intended space on the right side

<Image title="drag component.gif" alt={1916} className="border" border={true} src="https://files.readme.io/cc9fdc0-drag_component.gif" />

* If the Action Code contains multiple components, you can flexibly position the components. For example, a component can be placed ***above*** or ***below*** another component. With the Layout Components, you can even drag the Basic Components to ***within*** them

<Image title="drag component inside.gif" alt={1916} className="border" border={true} src="https://files.readme.io/b5a8354-drag_component_inside.gif" />

* After the component has been moved to the intended space, the setup form of the component will appear. Input data into that form, then click the green **Save** button to save the form
* We will specify the input detail for each component below

<Image title="2019-11-02 22_13_30-Window.png" alt={1228} className="border" border={true} src="https://files.readme.io/ae64083-2019-11-02_22_13_30-Window.png" />

* **IMPORTANT** After you have finished setting up all the necessary components, do not close this screen just yet. You need to scroll to the bottom of the **Form Builder** screen then click on the green **Save View** button in order to save all the forms you have set up so far

<Image title="2019-11-04 13_47_00-Window.png" alt={1228} className="border" border={true} src="https://files.readme.io/83ccff7-2019-11-04_13_47_00-Window.png" />

* A success message will appear

<Image title="2019-11-02 22_29_38-Window.png" alt={431} className="border" border={true} src="https://files.readme.io/698e035-2019-11-02_22_29_38-Window.png" />

* Now that the Action Code has been successfully set up, you can click on the **Back** text on the top left of the screen to get back to the Action Code list tab. There you can continue to build forms for other Action Codes

<Image title="2019-11-02 22_31_00-Window.png" alt={1902} className="border" border={true} src="https://files.readme.io/592bb87-2019-11-02_22_31_00-Window.png" />

* Below are the chronological steps to build the forms for each Action Code

### 1. LOADING\_AT\_DEPOT Action Code

* For this Action Code, you will need to build the following forms (Click on the text to directly navigate to the content):
* 1 - [The Order information table](), which shows the information of the Orders that the Drivers need to load onto their Vehicles at the Depot at the start of their assigned Delivery Shift
* 2 - [The Check-in panel](), which allows the Drivers to check-in at the start of their Delivery Shifts
* 3 - [The confirmation panel](), through which the Drivers will confirm several statuses before actually leaving the Depot such as: Have finished loading Products; Have left the warehouse etc.
* Here is how the final Action Code will look like after you have completed building its forms:

<Image title="sOFIVHpxX4.png" alt={1230} border={true} src="https://files.readme.io/c474dbf-sOFIVHpxX4.png">
  Illustration (English)
</Image>

<Image title="sdggMUCoyy.png" alt={1227} border={true} src="https://files.readme.io/30a5149-sdggMUCoyy.png">
  Illustration (Vietnamese)
</Image>

#### 1.1. Order Information Table

##### 1.1.1. Order Information Panel

* Component used: **Layout Components > Panel**
* Position: On top

<Image title="2019-11-04 13_52_10-Window.png" alt={1903} className="border" border={true} src="https://files.readme.io/90d2939-2019-11-04_13_52_10-Window.png" />

* Component content:
* On the component setup form of this component, you need to input information into two tabs, **Display** and **API**
* Note: The value input into the **Title** field in the **Display** tab can be changed freely. It doesn't necessarily need to be ***Order Information***

<Image title="2019-11-04 13_48_22-Window.png" alt={599} border={true} src="https://files.readme.io/189fc3d-2019-11-04_13_48_22-Window.png">
  Illustration (English)
</Image>

<Image title="5zJu63DAVV.png" alt={609} border={true} src="https://files.readme.io/0bfedc4-5zJu63DAVV.png">
  Illustration (Vietnamese)
</Image>

* In the **API** tab, you will need to input exactly as shown in the table below (Notice the lowercase and uppercase letters)
* Note: For the **Custom Properties** field, you will first need to click on its text to expand it. Next, you need to click the **Add Value** button to add a Key-Value row

<Image title="fBbbOruNeP.png" alt={554} className="border" border={true} src="https://files.readme.io/6e9fd67-fBbbOruNeP.png" />

* To ensure there is no mistake, you can simply copy the values in the table below and paste into the component setup form of yours

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Value To Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Property Name"
      </td>

      <td>
        ***orderList***
      </td>
    </tr>

    <tr>
      <td>
        "Custom Properties"
      </td>

      <td>
        For the "Key" field, input the following value: ***url***\
        For the "Value" field, input the following value: ***/order/list/***
      </td>
    </tr>
  </tbody>
</Table>

* Here is how this tab looks after you have input the needed information

<Image title="2019-11-04 13_49_57-Window.png" alt={599} className="border" border={true} src="https://files.readme.io/85d4e14-2019-11-04_13_49_57-Window.png" />

##### 1.1.2. Order Information Table

* Component used: **Layout Components > Table**
* Position: Inside the Order Information panel

<Image title="2019-11-04 13_57_16-Window.png" alt={1900} className="border" border={true} src="https://files.readme.io/1cfc40f-2019-11-04_13_57_16-Window.png" />

* Component content:
* On the component setup form of this component, you need to input information into two tabs, **Display** and **API**

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Value To Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Display" tab
        "Number of Rows"
      </td>

      <td>
        ***1***
      </td>
    </tr>

    <tr>
      <td>
        "Display" tab\
        "Number of Columns"
      </td>

      <td>
        ***4***
      </td>
    </tr>

    <tr>
      <td>
        "API" tab\
        "Custom Properties"
      </td>

      <td>
        For the "Key" field, input the following value: ***url***\
        For the "Value" field, input the following value: ***/order/list/***
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2019-11-04 13_54_00-Window.png" alt={602} className="border" border={true} src="https://files.readme.io/70d9dc5-2019-11-04_13_54_00-Window.png" />

<Image title="2019-11-04 13_56_13-Window.png" alt={603} className="border" border={true} src="https://files.readme.io/8e396e5-2019-11-04_13_56_13-Window.png" />

##### 1.1.3. Order Code Column

* Component used: **Basic Components > Text Field**
* Position: Inside the Order Information Table

<Image title="2019-11-04 14_03_03-Window.png" alt={1901} className="border" border={true} src="https://files.readme.io/0750c80-2019-11-04_14_03_03-Window.png" />

* Component content:
* On the component setup form of this component, you need to input information into two tabs, **Display** and **API**
* Note: The value input into the **Title** field in the **Display** tab can be changed freely. It doesn't necessarily need to be ***Order Code***

<Image title="2019-11-04 13_59_15-Window.png" alt={603} className="border" border={true} src="https://files.readme.io/e91bb38-2019-11-04_13_59_15-Window.png" />

* For the **API** tab, you need to input the exact value as shown in the table below

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Value To Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Property Name"
      </td>

      <td>
        ***orderCode***
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2019-11-04 14_02_00-Window.png" alt={612} className="border" border={true} src="https://files.readme.io/e66aa4b-2019-11-04_14_02_00-Window.png" />

##### 1.1.4. Customer Code Column

* Component used: **Basic Components > Text Field**
* Position: Inside the Order Information Table, to the right of the Order Code Column

<Image title="2019-11-04 14_09_11-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/4c15df6-2019-11-04_14_09_11-Window.png" />

* Component content:
* On the component setup form of this component, you need to input information into two tabs, **Display** and **API**
* Note: The value input into the **Label** field in the **Display** tab can be changed freely

<Image title="2019-11-04 14_06_00-Window.png" alt={596} className="border" border={true} src="https://files.readme.io/2c729e7-2019-11-04_14_06_00-Window.png" />

* For the **API** tab, you need to input the exact value as shown in the table below

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Value To Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Property Name"
      </td>

      <td>
        ***customerInfo.customerCode***
      </td>
    </tr>
  </tbody>
</Table>

![600](https://files.readme.io/e7b1b00-2019-11-04_14_08_20-Window.png "2019-11-04 14_08_20-Window.png")

##### 1.1.5. Customer Name Column

* Component used: **Basic Components > Text Field**
* Position: Inside the Order Information Table, to the right of the Customer Code Column

<Image title="2019-11-04 14_15_12-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/d1e6f95-2019-11-04_14_15_12-Window.png" />

* Component content:
* On the component setup form of this component, you need to input information into two tabs, **Display** and **API**
* Note: The value input into the **Label** field in the **Display** tab can be changed freely

<Image title="2019-11-04 14_11_29-Window.png" alt={595} className="border" border={true} src="https://files.readme.io/8f48daf-2019-11-04_14_11_29-Window.png" />

* For the **API** tab, you need to input the exact value as shown in the table below

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Value To Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Property Name"
      </td>

      <td>
        ***customerInfo.fullName***
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2019-11-04 14_14_18-Window.png" alt={605} className="border" border={true} src="https://files.readme.io/31bb994-2019-11-04_14_14_18-Window.png" />

##### 1.1.6. Total Amount Column

* Component used: **Basic Components > Text Field**
* Position: Inside the Order Information Table, to the right of the Customer Name Column

<Image title="2019-11-04 14_21_40-Window.png" alt={1909} className="border" border={true} src="https://files.readme.io/9e78ad1-2019-11-04_14_21_40-Window.png" />

* Component content:
* On the component setup form of this component, you need to input information into two tabs, **Display** and **API**
* Note: The value input into the **Label** field can be changed freely

<Image title="2019-11-04 14_17_40-Window.png" alt={602} className="border" border={true} src="https://files.readme.io/b0883b9-2019-11-04_14_17_40-Window.png" />

* For the **API** tab, you need to input the exact value as shown in the table below

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Value To Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Property Name"
      </td>

      <td>
        ***totalPrice***
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2019-11-04 14_20_29-Window.png" alt={606} className="border" border={true} src="https://files.readme.io/0fa8b46-2019-11-04_14_20_29-Window.png" />

#### 1.2. Check-In panel

* There are two options on how the driver can perform the Check-In action: 
* Option 1. Check-in by submitting the coordinate information of the driver's current location
* Option 2. Check-in by taking a photo of the warehouse

##### 1.2.1. Check-in By Submitting The Coordinate Information Of The Driver's Current Location

* Component used: **Special Components > Address**
* Position: Below the Order Information panel

<Image title="2019-11-04 14_45_02-Window.png" alt={1892} className="border" border={true} src="https://files.readme.io/617fd3b-2019-11-04_14_45_02-Window.png" />

* Component content:
* Note: The value input into the **Label** field can be changed freely

<Image title="2019-11-04 14_32_01-Window.png" alt={597} className="border" border={true} src="https://files.readme.io/c4c940f-2019-11-04_14_32_01-Window.png" />

* In the **Validation** tab, if you tick the **Required** checkbox, the Drivers will not be able to submit the Loading at Depot task without performing the Check-in action. If you leave this checkbox unticked, the Drivers will be able to submit this task without having to perform the Check-in action

<Image title="2019-11-04 14_38_14-Window.png" alt={312} className="border" border={true} src="https://files.readme.io/774309f-2019-11-04_14_38_14-Window.png" />

##### 1.2.2. Check-in By Taking A Photo Of The Warehouse

* Component used: **Special Components > File**
* Position: Below the Order Information panel
* Component content:
* Note: The value input into the **Label** field can be changed freely

![409](https://files.readme.io/8e2224c-2019-11-04_15_37_59-Abivin_vApp.png "2019-11-04 15_37_59-Abivin vApp.png")

* In the **Validation** tab, if you tick the **Required** checkbox, the Drivers will not be able to submit the Loading at Depot task without performing the Check-in action. If you leave this checkbox unticked, the Drivers will be able to submit this task without having to perform the Check-in action
* We strongly recommend you tick this checkbox because the moment that the Drivers perform this Check-in action will be recorded as the beginning timestamp of the Loading at Depot task and will reflect it on the Execution timeline of Route Plan (Map View) screen. If you don't tick this checkbox, the Drivers might bypass this action, thus the system will have no record of this task's beginning timestamp

<Image title="2019-11-04 15_08_34-Window.png" alt={358} className="border" border={true} src="https://files.readme.io/a22c8a9-2019-11-04_15_08_34-Window.png" />

* For the **API** tab, you need to input the exact value as shown in the table below

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Value To Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Property Name"
      </td>

      <td>
        (Required. Do not leave this field blank) ***checkIn***
      </td>
    </tr>

    <tr>
      <td>
        "Custom Properties"
      </td>

      <td>
        (Required) Key-Value 1: Specify if the Drivers can select a pre taken picture or will need to take a new picture\
        For the "Key" field, input the following value: ***isHideSelectFromLibrary***\
        For the "Value" field, input the following value: ***true***\
        (Optional) Key-Value 2: Specify the maximum distance (In meters) from the Drivers' current standing location to the warehouse location (Taken from the coordinate information of the Depot) that the Drivers can still submit the Loading at Depot task\
        For the "Key" field, input the following value: ***distanceFilter***\
        For the "Value" field, input a value as you wish. For example, if you want to prevent the Drivers from submitting this task if they stand farther than one hundred meters from the warehouse, input the following value into this field: ***100***
      </td>
    </tr>
  </tbody>
</Table>

<Image title="CSVfacy4vS.png" alt={608} className="border" border={true} src="https://files.readme.io/a87f461-CSVfacy4vS.png" />

#### 1.3. Status Confirmation Section

##### 1.3.1. Status Confirmation Panel

* Component used: **Layout Components > Panel** 
* Position: Below the Check-In panel

<Image title="2019-11-04 14_56_23-Window.png" alt={1903} className="border" border={true} src="https://files.readme.io/21dd960-2019-11-04_14_56_23-Window.png" />

* Component content:
* Note: The value input into the **Title** field can be changed freely

<Image title="2019-11-04 14_50_16-Window.png" alt={599} className="border" border={true} src="https://files.readme.io/31dbcbc-2019-11-04_14_50_16-Window.png" />

* Next is the confirmation statuses. You can add as many confirmation statuses as you want. Below we will present a sample confirmation status

#### 1.3.2. Confirm to have taken products out of the warehouse Checkbox

* Component used: **Basic Components > Check Box** 
* Position: Inside the Status Confirmation Panel

<Image title="2019-11-04 15_09_48-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/0cca580-2019-11-04_15_09_48-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-11-04 15_05_58-Window.png" alt={590} className="border" border={true} src="https://files.readme.io/35a153c-2019-11-04_15_05_58-Window.png" />

* In the **Validation** tab, if you tick the **Required** checkbox, the Drivers will not be able to submit the Loading at Depot task without confirming this status. If you leave this checkbox unticked, the Drivers will be able to submit this task without having to confirm this status

<Image title="2019-11-04 15_08_34-Window.png" alt={358} className="border" border={true} src="https://files.readme.io/51b7acd-2019-11-04_15_08_34-Window.png" />

### 2. DELIVER\_PRODUCT Action code

* For this Action Code, you will need to build the following forms:
* 1 - The Check-in panel, which allows the Drivers to check-in when they arrive at the Customers' receiving locations
* 2 - The delivery result section, which allows the Drivers to specify the delivery result
* (Optional) 3 - The Customer document photos section, which allows the Drivers to take pictures of important Customer documents such as invoices, deb book, etc.
* (Optional) 4 - The Customer signature section, which allows the Customers to sign directly on the mobile device of the Drivers
* Here is how the final Action Code will look like after you have completed building its forms:

<Image title="gbg8MX8PjE.png" alt={1225} border={true} src="https://files.readme.io/52754ed-gbg8MX8PjE.png">
  Illustration (English)
</Image>

<Image title="lcJMnjNcO8.png" alt={1225} border={true} src="https://files.readme.io/57da4d6-lcJMnjNcO8.png">
  Illustration (Vietnamese)
</Image>

#### 2.1. Check-In panel

* The setup instruction is quite similar to the [Check-in panel of the LOADING\_AT\_DEPOT Action Code](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-actions#12-check-in-panel)
* If you also wish to set a maximum distance between the current standing locations of the Drivers and the Customers' actual receiving locations (Taken from the Customer coordinate information), then replace the ***distanceFilter*** key with the ***Geofencing*** key like so

<Image title="B2e31HFG6v.png" alt={606} className="border" border={true} src="https://files.readme.io/eb52d73-B2e31HFG6v.png" />

#### 2.2. Delivery Result Section

* Component used: **Special Components > Container**
* Position: Below the Check-in panel

<Image title="2019-11-04 16_20_00-Window.png" alt={1902} className="border" border={true} src="https://files.readme.io/2ca1a9e-2019-11-04_16_20_00-Window.png" />

* Component content:
* Note: The value input into the **Label** field can be changed freely

<Image title="2019-11-04 16_13_08-Window.png" alt={595} className="border" border={true} src="https://files.readme.io/5fcad7b-2019-11-04_16_13_08-Window.png" />

* For the **API** tab, you need to input the exact value as shown in the table below

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Value To Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Custom Propertise"
      </td>

      <td>
        (Required) Key-Value 1:\
        For the "Key" field, input the following value: ***data***\
        For the "Value" field, input the following value: ***\{}***\
        (Required) Key-Value 2:\
        For the "Key" field, input the following value: ***url***\
        For the "Value" field, input the following value: ***/orders/list/***
      </td>
    </tr>
  </tbody>
</Table>

<Image title="form.png" alt={609} className="border" border={true} src="https://files.readme.io/cf9bd11-form.png" />

#### 2.3. Customer Document Photos Section

* Component used: **Special Components > File**
* Position: Below the Delivery Result section
* Component content:
* Note: The value input into the **Label** field in the **Display** tab can be changed freely
* Do not forget to tick the **Multiple Values** checkbox. If this checkbox is not ticked, you will not be able to take multiple photos

<Image title="lIYeKZEcvI.png" alt={1243} className="border" border={true} src="https://files.readme.io/977ab0c-lIYeKZEcvI.png" />

* In the **API** tab, input the exact values as shown in the table below

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Value To Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Property Name"
      </td>

      <td>
        (Required) ***checkIn2***\
        DO NOT input the "checkIn" value, as it will cause conflict with the Check-in panel
      </td>
    </tr>

    <tr>
      <td>
        "Custom Properties"
      </td>

      <td>
        (Required) Key-Value 1:\
        For the "Key" field, input the following value: ***isHideSelectFromLibrary***\
        For the "Value" field, input the following value: ***true***\
        (Required) Key-Value 2: This Key-Value pair will specify the maximum number of photos that the Drivers can take\
        For the "Key" field, input the following value: ***numberOfimages***\
        For the "Value" field, input the a suitable number. For example, if you want to allow the Drivers to take up to eight photos, input the following value: ***8***
      </td>
    </tr>
  </tbody>
</Table>

<Image title="MRocGdbeG8.png" alt={603} className="border" border={true} src="https://files.readme.io/5e15cc3-MRocGdbeG8.png" />

#### 2.4. Customer Signature Section

* Component used: **Special Components > Signature**
* Position: Below the Customer Document Photos section (If available) or the Delivery Result section
* Component content: You do not need to input anything

### 3. BACK\_DEPOT Action code

#### 3.1. Check In panel

* The setup instruction is similar to the [Check-in panel of the LOADING\_AT\_DEPOT Action Code](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-actions#12-check-in-panel)

### 4. END\_DAY Action code

#### 4.1. Check In panel

* The setup instruction is similar to the [Check-in panel of the LOADING\_AT\_DEPOT Action Code](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-actions#12-check-in-panel)

#### 4.2. Update status at the end of day panel

* Component used: **Layout Components > Panel**
* Position: Below **Check In panel** component

<Image title="2019-11-04 16_27_06-Window.png" alt={597} className="border" border={true} src="https://files.readme.io/63d54af-2019-11-04_16_27_06-Window.png" />

#### 4.3. Confirm to have handed all redundant products to the warehouse manager Check box

* Component used: **Basic Components > Check Box**
* Position: Inside **Update status at the end of day panel** component

<Image title="2019-11-04 16_48_40-Window.png" alt={1896} className="border" border={true} src="https://files.readme.io/65b2b7c-2019-11-04_16_48_40-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-11-04 16_51_29-Window.png" alt={610} className="border" border={true} src="https://files.readme.io/e5c808f-2019-11-04_16_51_29-Window.png" />

<Image title="2019-11-04 16_30_19-Window.png" alt={356} className="border" border={true} src="https://files.readme.io/11573aa-2019-11-04_16_30_19-Window.png" />

#### 4.4. Confirm to have handed all collected cash to accountant Check box

* Component used: **Basic Components > Check Box**
* Position: Inside **Update status at the end of day panel** component, below **Confirm to have handed all redundant products to the warehouse manager Check box** component

<Image title="2019-11-04 16_38_24-Window.png" alt={1892} className="border" border={true} src="https://files.readme.io/3439f8c-2019-11-04_16_38_24-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-11-04 16_37_38-Window.png" alt={602} className="border" border={true} src="https://files.readme.io/e660728-2019-11-04_16_37_38-Window.png" />

<Image title="2019-11-04 16_30_19-Window.png" alt={356} className="border" border={true} src="https://files.readme.io/efaa218-2019-11-04_16_30_19-Window.png" />

### 5. EXTRA\_TASK Action code

#### 5.1. Check In panel

* Set up similarly to the [**1.7. Check In panel**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-actions#17-check-in-panel) section above

#### 5.2. Input Extra Task Type

* Component used: **Basic Components > Radio**
* Position: Below **Check In panel** component

![1920](https://files.readme.io/b714aa4-1.png "1.png")

* Component content:
* Note: The value input into **Label** field can be changed freely

![1231](https://files.readme.io/2561e53-1.png "1.png")

#### 5.3. Input Description

* Component used: **Basic Components > Text Field**
* Position: Below **Extra Task Type** component

![1920](https://files.readme.io/80ce765-2.png "2.png")

* Component content:
* Note: The value input into **Label** field can be changed freely

![1236](https://files.readme.io/b69dc2e-1.png "1.png")

#### 5.4. Input Price

* Component used: **Basic Components > Number**
* Position: Below **Description** component

![1920](https://files.readme.io/6a2a403-2.png "2.png")

* Component content:
* Note: The value input into **Label** field can be changed freely

![1236](https://files.readme.io/9bdee7f-1.png "1.png")
