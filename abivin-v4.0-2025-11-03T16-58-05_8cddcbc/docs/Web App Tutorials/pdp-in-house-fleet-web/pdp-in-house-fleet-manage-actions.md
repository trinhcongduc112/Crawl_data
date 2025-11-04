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
## Definition of Actions

* **Actions** in PDP Model are defined and served exactly the same way as in VRP/DC Model. For more information on Actions, please refer to this article: [Definition of Actions](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-actions#definition-of-actions)

> ❗️ All data must be input exactly as shown on images, both lowercase and uppercase letters, unless specified otherwise

## Locate Action Code List

* Action Codes are listed in the **Tasks > Actions** 

<Image title="1. Actions List (ENG).png" alt={1920} border={true} src="https://files.readme.io/ea7c714-1._Actions_List_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Actions List (VIE) 2.png" alt={1920} border={true} src="https://files.readme.io/c0ea5dd-1._Actions_List_VIE_2.png">
  Illustration (Vietnamese)
</Image>

## Create Action Codes

* Navigate to tab **Tasks > Actions**
* You will notice that a set of actions has been automatically created. These are the default action codes for VRP model

<Image title="2. Default (ENG).png" alt={1920} border={true} src="https://files.readme.io/00d0044-2._Default_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Default (VIE).png" alt={1920} border={true} src="https://files.readme.io/ceb73e6-2._Default_VIE.png">
  Illustration (Vietnamese)
</Image>

* You would need to delete all those actions by clicking on the icon :fa-square-o: on the left of column **Action Code**, then click on the button **Delete All**

<Image title="3. Delete (ENG) 2.png" alt={1920} border={true} src="https://files.readme.io/4147207-3._Delete_ENG_2.png">
  Illustration (English)
</Image>

<Image title="1. Actions List (VIE) 3.png" alt={1899} border={true} src="https://files.readme.io/5dbd441-1._Actions_List_VIE_3.png">
  Illustration (Vietnamese)
</Image>

#### Action Code information fields

* In case the Action Code list is empty or the Action Codes appear differently than the ones shown in the above image, you need to create the correct Action Codes using the Excel import file. **DO NOT** use the Webform to create Action Codes
* Below are the information fields of the actions of this model:

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action Code (Compulsory)
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
        LOADING\_AT\_DEPOT
      </td>

      <td>
        Driver Starts
      </td>

      <td>
        Driver starts at the garage
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        LOADING\_AT\_STORE
      </td>

      <td>
        Load Products at Origin customer
      </td>

      <td>
        Driver loading products at the Origin customer
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        TRANSIT
      </td>

      <td>
        Driver Resting
      </td>

      <td>
        Driver rests after each eight hours of working (Including driving and loading/unloading products at the customer locations)
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        DELIVER\_PRODUCT
      </td>

      <td>
        Deliver products at Destination customer
      </td>

      <td>
        Driver delivers products at the Destination customer
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        BACK\_DEPOT
      </td>

      <td>
        Back to Depot
      </td>

      <td>
        Driver travels back to garage
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        END\_DAY
      </td>

      <td>
        End Delivery shift
      </td>

      <td>
        Driver ends the delivery shift
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>
    </tr>
  </tbody>
</Table>

## Create Forms for Action Codes

### Enable Form Building Function

* The Action Codes recently created have not yet had any information inside. Imagine them as blank Excel spreadsheets. In order for the Mobile app users to see and perform their tasks on the Mobile app, you have to build the display/input fields for each Action Code using the Form Building function
* The steps to enable the form building function in PDP model are the same as those in the VRP/DC Model. Please refer to this article for more information: [Enable Form Building Function](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-actions#enable-form-building-function)

### General Steps to Build Forms for Action Codes

* The steps to build form for Action Codes in PDP model are the same as those in the VRP/DC Model. Please refer to this article for more information: [General Steps to Build Forms for Action Codes](https://docs.abivin.com/docs/pdp-in-house-fleet-manage-actions#general-steps-to-build-forms-for-action-codes)

* We will now move on to create forms for each action code

## 1. LOADING\_AT\_DEPOT action codes

* For this Action Code, you will need to build the Arrival Check In Panel, which allows the Drivers to check-in at the parking garage.
* Here is how the final Action Code will look like after you have completed building its forms:

<Image title="Arrrival Check In (ENG).png" alt={1296} border={true} src="https://files.readme.io/010d865-Arrrival_Check_In_ENG.png">
  Illustration (English)
</Image>

<Image title="Arrrival Check In (VIE).png" alt={1302} border={true} src="https://files.readme.io/2d14425-Arrrival_Check_In_VIE.png">
  Illustration (Vietnamese)
</Image>

### 1.1 Arrival Check In Panel

* Component used: **Special Components > File**
* Position: On top

<Image title="1. Arrival Check In Component (ENG).png" alt={1890} border={true} src="https://files.readme.io/6ed6e1b-1._Arrival_Check_In_Component_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Arrival Check In Component (VIE).png" alt={1898} border={true} src="https://files.readme.io/0ab444d-1._Arrival_Check_In_Component_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="39afea5-53c9838-2019-10-25_11_12_02-Window.png" alt={534} className="border" border={true} src="https://files.readme.io/08b296a-39afea5-53c9838-2019-10-25_11_12_02-Window.png" />

<Image title="1. Check In Panel - Label (VIE).png" alt={601} className="border" border={true} src="https://files.readme.io/fe0a1d4-1._Check_In_Panel_-_Label_VIE.png" />

* In the **Validation** tab, if you tick the **Required** checkbox, the Drivers will not be able to submit the **Loading at Depot** task without performing the Check-in action. If you leave this checkbox unticked, the Drivers will be able to submit this task without having to perform the Check-in action
* We strongly recommend you tick this checkbox because the moment that the Drivers perform this Check-in action will be recorded as the beginning timestamp of the Loading at Depot task and will reflect it on the Execution timeline of Route Plan (Map View) screen. If you don't tick this checkbox, the Drivers might bypass this action, thus the system will have no record of this task's beginning timestamp

<Image title="96548a2-eca9da0-2019-10-25_17_33_02-Window.png" alt={611} className="border" border={true} src="https://files.readme.io/b613dd4-96548a2-eca9da0-2019-10-25_17_33_02-Window.png" />

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
        Custom Properties
      </td>

      <td>
        Key-Value 1: Specify if the Drivers can select a pre taken picture or will need to take a new picture\
        For the "Key" field, input the following value: isHideSelectFromLibrary\
        For the "Value" field, input the following value: true
      </td>
    </tr>
  </tbody>
</Table>

<Image title="68a5998-7c59bdd-2019-10-24_15_33_26-Window.png" alt={522} className="border" border={true} src="https://files.readme.io/6e8c07f-68a5998-7c59bdd-2019-10-24_15_33_26-Window.png" />

## 2. LOADING\_AT\_STORE action code

* For this Action Code, you will need to build the following forms:
* 1 - A Check-in Panel, which allows drivers to check in when they load goods at the customer's location
* 2 - Confirm Loading Status Panel, which allows drivers to confirm that products are taken out from the customer's store
* 3 - Signature Panel, which allows the Customers to sign directly on the mobile device of the Drivers
* Here is how the final Action Code will look like after you have completed building its forms:

<Image title="Loading At Store (ENG).png" alt={1303} border={true} src="https://files.readme.io/4392190-Loading_At_Store_ENG.png">
  Illustration (English)
</Image>

<Image title="Loading At Store (VIE).png" alt={1299} border={true} src="https://files.readme.io/f3d494c-Loading_At_Store_VIE.png">
  Illustration (Vietnamese)
</Image>

### 2.1 Check In Panel

* Component used: **Special Components > File**
* Position: On top

<Image title="1. Arrival Check In (ENG) 2.png" alt={1891} border={true} src="https://files.readme.io/039ccb8-1._Arrival_Check_In_ENG_2.png">
  Illustration (English)
</Image>

<Image title="2. Loading at Store (VIE).png" alt={1920} border={true} src="https://files.readme.io/78e7606-2._Loading_at_Store_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Similar as [**Check In Panel**](https://docs.abivin.com/docs/pdp-in-house-fleet-manage-actions#11-arrival-check-in-panel) described above

### 2.2 Confirm Loading Status Panel

* Component used: **Layout Components > Panel**
* Position: Below **Check In** Panel

<Image title="4. Confirm Loading Status.png" alt={1920} border={true} src="https://files.readme.io/ab33fb7-4._Confirm_Loading_Status.png">
  Illustration (English)
</Image>

<Image title="2. Confirm Loading Status (VIE).png" alt={1883} border={true} src="https://files.readme.io/dc16339-2._Confirm_Loading_Status_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Note: The value input into **Title** field can be changed freely

<Image title="2. Confirm Loading Status (ENG).png" alt={613} border={true} src="https://files.readme.io/f3145d8-2._Confirm_Loading_Status_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Confirm Loading Status (VIE) 2.png" alt={600} border={true} src="https://files.readme.io/b403ed3-2._Confirm_Loading_Status_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* Next is the confirmation statuses. You can add as many confirmation statuses as you want. Below we will present a sample confirmation status

### 2.3 Confirm products are taken out Checkbox

* Component used: **Basic Components > Check Box**
* Position: Inside **Confirm Loading Status** panel component

<Image title="5. Confirm 3.png" alt={1920} border={true} src="https://files.readme.io/70d45f4-5._Confirm_3.png">
  Illustration (English)
</Image>

<Image title="2. Confirm products taken out (VIE).png" alt={1886} border={true} src="https://files.readme.io/2c8d34f-2._Confirm_products_taken_out_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="3. COnfirm Products are taken out (ENG).png" alt={611} border={true} src="https://files.readme.io/97b9776-3._COnfirm_Products_are_taken_out_ENG.png">
  Illustration (English)
</Image>

<Image title="3. COnfirm Products are taken out (VIE) 2.png" alt={604} border={true} src="https://files.readme.io/60863e7-3._COnfirm_Products_are_taken_out_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* In the **Validation** tab, if you tick the **Required** checkbox, the Drivers will not be able to submit the **Loading at Store** task without confirming this status. If you leave this checkbox unticked, the Drivers will be able to submit this task without having to confirm this status

<Image title="5. Confirm 5.png" alt={603} className="border" border={true} src="https://files.readme.io/d53aca1-5._Confirm_5.png" />

### 2.4 Signature

* Component used: **Special Components > Signature**
* Position: Below the panel **Confirm Loading Status** 

<Image title="5. Confirm 6.png" alt={1920} border={true} src="https://files.readme.io/5c4199f-5._Confirm_6.png">
  Illustration (English)
</Image>

<Image title="3. Signature (VIE).png" alt={1895} border={true} src="https://files.readme.io/33eb7e5-3._Signature_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content: You do not need to input anything
* In the **Validation** tab, if you tick the **Required** checkbox, the Drivers will not be able to submit the **Loading at Store** task without submitting the Signature. If you leave this checkbox unticked, the Drivers will be able to submit this task without having to perform the Signature action

<Image title="6. Signature 2.png" alt={611} className="border" border={true} src="https://files.readme.io/8c94c1f-6._Signature_2.png" />

## 3. TRANSIT action code

### 3.1 Check In Panel

* Component used: **Special Components > File**

<Image title="f4b6793-2019-10-24_17_16_52-Window.png" alt={1631} className="border" border={true} src="https://files.readme.io/47b039a-f4b6793-2019-10-24_17_16_52-Window.png" />

* Component content:
* Similar as [**Check In Panel**](https://docs.abivin.com/docs/pdp-in-house-fleet-manage-actions#11-arrival-check-in-panel) described above

## 4. DELIVER\_PRODUCT action codes

* For this Action Code, you will need to build the following forms:
* 1 - The Arrival Check-in panel, which allows the Drivers to check-in when they arrive at the Customers' receiving locations
* 2 - The Unloading Check-in section, which allows the Drivers to specify the delivery result
* 3 - The Customer signature section, which allows the Customers to sign directly on the mobile device of the Drivers
* Here is how the final Action Code will look like after you have completed building its forms:

<Image title="DELIVER PRODUCT (ENG).png" alt={1297} border={true} src="https://files.readme.io/8b2d3fe-DELIVER_PRODUCT_ENG.png">
  Illustration (English)
</Image>

<Image title="DELIVER PRODUCT (VIE).png" alt={1295} border={true} src="https://files.readme.io/14e5362-DELIVER_PRODUCT_VIE.png">
  Illustration (Vietnamese)
</Image>

### 4.1 Arrival Check In Panel

* Component used: **Special Components > File**
* Position: On top

<Image title="1. Arrival Check In Component (ENG).png" alt={1890} border={true} src="https://files.readme.io/8382605-1._Arrival_Check_In_Component_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Arrival Check In Component (VIE).png" alt={1898} border={true} src="https://files.readme.io/86ca948-1._Arrival_Check_In_Component_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Similar as [**Check In Panel**](https://docs.abivin.com/docs/pdp-in-house-fleet-manage-actions#11-arrival-check-in-panel) described above

### 4.2 Unloading Check In Panel

* Component used: **Special Components > File**
* Position: Below **Loading Check In** panel

<Image title="4. Unloading Check IN (VIE).png" alt={1887} border={true} src="https://files.readme.io/04b2c78-4._Unloading_Check_IN_VIE.png">
  Illustration (English)
</Image>

<Image title="4. Unloading Check IN (VIE) 2.png" alt={1896} border={true} src="https://files.readme.io/9c61aeb-4._Unloading_Check_IN_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Similar as [**Check In Panel**](https://docs.abivin.com/docs/pdp-in-house-fleet-manage-actions#11-arrival-check-in-panel) described above

### 4.3 Signature

* Component used: **Special Components > Signature**
* Position: Below **Unloading Check In** panel

<Image title="11. Deliver Product 1.png" alt={1898} src="https://files.readme.io/599f300-11._Deliver_Product_1.png">
  Illustration (English)
</Image>

<Image title="Signature (VIE).png" alt={1878} border={true} src="https://files.readme.io/f6b859b-Signature_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content: 
* Similar as [**Signature**](https://docs.abivin.com/docs/pdp-in-house-fleet-manage-actions#24-signature) described above.

## 5. BACK\_DEPOT action codes

* For this Action Code, you will need to build the Check In Panel, which allows the Drivers to check-in as they return to the Depot. 
* Here is how the final Action Code will look like after you have completed building its forms:

<Image title="CHeck In.png" alt={1302} border={true} src="https://files.readme.io/543465e-CHeck_In.png">
  Illustration (English)
</Image>

<Image title="1. Arrival Check In Component (VIE) 4.png" alt={1298} border={true} src="https://files.readme.io/a68f14f-1._Arrival_Check_In_Component_VIE_4.png">
  Illustration (Vietnamese)
</Image>

* Component used: **Special Components > File**
* Position: On top

<Image title="9. Back Depot.png" alt={1896} border={true} src="https://files.readme.io/f2cf527-9._Back_Depot.png">
  Illustration (English)
</Image>

<Image title="1. Arrival Check In (VIE) 2.png" alt={1878} border={true} src="https://files.readme.io/8d57a5b-1._Arrival_Check_In_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Similar as [**Check In Panel**](https://docs.abivin.com/docs/pdp-in-house-fleet-manage-actions#11-arrival-check-in-panel) described above

## 6. END\_DAY action codes

* For this Action Code, you will need to build the following forms:\
  1 - The Delivery Performance Table, which shows the information of the Orders that the Drivers have delivered\
  2 - The Check-in panel, which allows the Drivers to check-in at the end of their Delivery Shifts
* Here is how the final Action Code will look like after you have completed building its forms: 

<Image title="END DAY (ENG).png" alt={1316} border={true} src="https://files.readme.io/f7ae192-END_DAY_ENG.png">
  Illustration (English)
</Image>

<Image title="END DAY (VIE).png" alt={1286} src="https://files.readme.io/0f070d8-END_DAY_VIE.png">
  Illustration (Vietnamese)
</Image>

### 6.1 Delivery Performance Panel

* Component used: **Layout Components > Panel**
* Position: On top

<Image title="8. End Day 1.png" alt={1898} className="border" border={true} src="https://files.readme.io/27cddbd-8._End_Day_1.png" />

* Component content:
* On the component setup form of this component, you need to input information into two tabs, **Display** and **API**
* Note: The value input into the **Title** field in the **Display** tab can be changed freely. It doesn't necessarily need to be **Delivery Performance**

<Image title="5. Delivery Result (ENG).png" alt={599} border={true} src="https://files.readme.io/64259a3-5._Delivery_Result_ENG.png">
  Illustration (English)
</Image>

<Image title="5. Delivery Result (VIE).png" alt={613} border={true} src="https://files.readme.io/8980307-5._Delivery_Result_VIE.png">
  Illustration (Vietnamese)
</Image>

* In the **API** tab, you will need to input exactly as shown in the table below (Notice the lowercase and uppercase letters)
* Note: For the **Custom Properties** field, you will first need to click on its text to expand it. Next, you need to click the **Add Value** button to add a **Key**-Value row

![576](https://files.readme.io/1ea40ed-6._Custom_Properties.png "6. Custom Properties.png")

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
        Property Name
      </td>

      <td>
        ***orderList***
      </td>
    </tr>

    <tr>
      <td>
        Custom Properties
      </td>

      <td>
        For the "Key" field, input the following value: ***url***\
        For the "Value" field, input the following value: ***/order/list/***
      </td>
    </tr>
  </tbody>
</Table>

* Here is how this tab looks after you have input the needed information

<Image title="full.png" alt={599} className="border" border={true} src="https://files.readme.io/bf69bbc-full.png" />

### 6.2 Delivery Performance Table

* Component used: **Layout Components > Table**
* Position: Inside **Delivery Performance** panel

<Image title="8. End Day 6.png" alt={1916} className="border" border={true} src="https://files.readme.io/60f4819-8._End_Day_6.png" />

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

<Image title="Columns.png" alt={607} className="border" border={true} src="https://files.readme.io/cfbc950-Columns.png" />

<Image title="column 2.png" alt={603} className="border" border={true} src="https://files.readme.io/066190c-column_2.png" />

### 6.3 Order Code Field

* Component used: **Basic Components > Text Field**
* Position: Inside the **Delivery Performance** panel

<Image title="8. End Day 3.png" alt={1897} className="border" border={true} src="https://files.readme.io/e737d2a-8._End_Day_3.png" />

* Component content
* On the component setup form of this component, you need to input information into two tabs, **Display** and **API**
* Note: The value input into the **Label** field in the **Display** tab can be changed freely. It doesn't necessarily need to be **Order Code**

<Image title="7. Order Code (ENG).png" alt={597} border={true} src="https://files.readme.io/0c2e533-7._Order_Code_ENG.png">
  Illustration (English)
</Image>

<Image title="7. Order Code (VIE).png" alt={604} border={true} src="https://files.readme.io/ae3f24e-7._Order_Code_VIE.png">
  Illustration (Vietnamese)
</Image>

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
        Property Name
      </td>

      <td>
        ***orderCode***
      </td>
    </tr>
  </tbody>
</Table>

<Image title="7. Order Code 2 (ENG).png" alt={593} className="border" border={true} src="https://files.readme.io/e107fc9-7._Order_Code_2_ENG.png" />

### 6.4 Customer Code Field

* Component used: **Basic Components > Text Field**
* Position: Inside the **Delivery Performance** panel, to the right of the **Order Code** Field

<Image title="8. End Day 10.png" alt={1901} className="border" border={true} src="https://files.readme.io/bbd8973-8._End_Day_10.png" />

* Component content:
* On the component setup form of this component, you need to input information into two tabs, **Display** and **API**
* Note: The value input into the **Label** field in the **Display** tab can be changed freely

<Image title="8. Customer Code.png" alt={586} border={true} src="https://files.readme.io/56b893c-8._Customer_Code.png">
  Illustration (English)
</Image>

<Image title="8. Customer Code (VIE).png" alt={597} border={true} src="https://files.readme.io/3fb08d1-8._Customer_Code_VIE.png">
  Illustration (Vietnamese)
</Image>

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
        Property Name
      </td>

      <td>
        customerInfo.customerCode
      </td>
    </tr>
  </tbody>
</Table>

<Image title="8. Customer Code (ENG).png" alt={600} className="border" border={true} src="https://files.readme.io/a9c6ede-8._Customer_Code_ENG.png" />

### 6.5 Customer Name Field

* Component used: **Basic Components > Text Field**
* Position: Inside the **Delivery Performance** Table, to the right of the **Customer Code** Field

<Image title="8. End Day 11.png" alt={1901} className="border" border={true} src="https://files.readme.io/413a915-8._End_Day_11.png" />

* Component content:
* On the component setup form of this component, you need to input information into two tabs, **Display** and **API**
* Note: The value input into the **Label** field in the **Display** tab can be changed freely

<Image title="9. Customer Name (ENG 2).png" alt={595} border={true} src="https://files.readme.io/bbddcf0-9._Customer_Name_ENG_2.png">
  Illustration (English)
</Image>

<Image title="9. Customer Name (VIE).png" alt={603} border={true} src="https://files.readme.io/2af075a-9._Customer_Name_VIE.png">
  Illustration (Vietnamese)
</Image>

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
        Property Name
      </td>

      <td>
        ***customerInfo.fullName***
      </td>
    </tr>
  </tbody>
</Table>

<Image title="Customer Name.png" alt={605} className="border" border={true} src="https://files.readme.io/81d1255-Customer_Name.png" />

### 6.6 Total Amount Field

* Component used: **Basic Components > Text Field**
* Position: Inside the **Delivery Performance** Table, to the right of the **Customer Name** Field

<Image title="8. End Day 12.png" alt={1898} border={true} src="https://files.readme.io/c0e4a21-8._End_Day_12.png">
  Illustration (English)
</Image>

<Image title="9. End Day (VIE) 2.png" alt={1879} border={true} src="https://files.readme.io/725cfeb-9._End_Day_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* On the component setup form of this component, you need to input information into two tabs, **Display** and **API**
* Note: The value input into the **Label** field in the **Display** tab can be changed freely

<Image title="10. Total Amount (ENG).png" alt={593} border={true} src="https://files.readme.io/52b7078-10._Total_Amount_ENG.png">
  Illustration (English)
</Image>

<Image title="10. Total Amount (VIE).png" alt={604} border={true} src="https://files.readme.io/eee6d73-10._Total_Amount_VIE.png">
  Illustration (Vietnamese)
</Image>

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
        Property Name
      </td>

      <td>
        ***totalPrice***
      </td>
    </tr>
  </tbody>
</Table>

<Image title="Total Amount.png" alt={606} className="border" border={true} src="https://files.readme.io/65a65d3-Total_Amount.png" />

### 6.7 Check In Panel

* Component used: **Special Components > File**
* Position: Below **Delivery Performance** Panel

<Image title="8. End Day 13.png" alt={1896} border={true} src="https://files.readme.io/51969d7-8._End_Day_13.png">
  Illustration (English)
</Image>

<Image title="9. End Day (VIE).png" alt={1898} border={true} src="https://files.readme.io/3977afe-9._End_Day_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Similar as [**Check In Panel**](https://docs.abivin.com/docs/pdp-in-house-fleet-manage-actions#11-arrival-check-in-panel) described above

## 7. EXTRA\_TASK action codes

* For this Action Code, you will need to build the following forms:
* 1 - Check In Panel, which allows drivers to take photos at the place where drivers take on extra tasks
* 2 - Extra Task Type Panel, which allows drivers to specify the type of extra task
* 3 - Description Panel, which allows drivers to enter a detailed description of the extra task
* 4 - Cost Panel, which allows drivers to enter the amount of fee or cost incurred in the extra task.
* Here is how the final Action Code will look like after you have completed building its forms:

<Image title="EXTRA TASK (ENG).png" alt={1304} border={true} src="https://files.readme.io/0ccdee7-EXTRA_TASK_ENG.png">
  Illustration (English)
</Image>

<Image title="EXTRA TASK (VIE).png" alt={1304} border={true} src="https://files.readme.io/b6943bf-EXTRA_TASK_VIE.png">
  Illustration (Vietnamese)
</Image>

### 7.1 Check In Panel

* Component used: **Special Components > File**
* Position: On top

<Image title="9. Back Depot.png" alt={1896} border={true} src="https://files.readme.io/91acac2-9._Back_Depot.png">
  Illustration (English)
</Image>

<Image title="1. Arrival Check In Component (VIE).png" alt={1898} border={true} src="https://files.readme.io/66b86f7-1._Arrival_Check_In_Component_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Similar as [**Check In Panel**](https://docs.abivin.com/docs/pdp-in-house-fleet-manage-actions#11-arrival-check-in-panel) described above

### 7.2 Input Extra Task Type

* Component used: **Basic Components > Radio**
* Position: Below **Check In** panel component

<Image title="10. Extra Task 1.png" alt={1895} border={true} src="https://files.readme.io/ca7e075-10._Extra_Task_1.png">
  Illustration (English)
</Image>

<Image title="10. Extra Task - Task Type (VIE).png" alt={1888} border={true} src="https://files.readme.io/cbe3a7d-10._Extra_Task_-_Task_Type_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="10. Extra Task 2.png" alt={596} border={true} src="https://files.readme.io/e853057-10._Extra_Task_2.png">
  Illustration (English)
</Image>

<Image title="10. Extra Task - Task Type (VIE) 2.png" alt={600} className="border" border={true} src="https://files.readme.io/f6958cc-10._Extra_Task_-_Task_Type_VIE_2.png" />

* You can also add more options to the list by clicking the button **Add Value** below the list

<Image title="Add value.png" alt={594} className="border" border={true} src="https://files.readme.io/e785ffd-Add_value.png" />

### 7.3. Input Description

* Component used: **Basic Components > Text Field**
* Position: Below **Extra Task Type** component

<Image title="10. Extra Task 3.png" alt={1892} border={true} src="https://files.readme.io/a4bd7bb-10._Extra_Task_3.png">
  Illustration (English)
</Image>

<Image title="10, Extra Task - Description (VIE).png" alt={1890} border={true} src="https://files.readme.io/1fd8e24-10_Extra_Task_-_Description_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="14. Description (ENG).png" alt={603} border={true} src="https://files.readme.io/7db0508-14._Description_ENG.png">
  Illustration (English)
</Image>

<Image title="14. Description (VIE).png" alt={588} border={true} src="https://files.readme.io/14a2d91-14._Description_VIE.png">
  Illustration (Vietnamese)
</Image>

* In the **Validation** tab, if you tick the **Required** checkbox, the Drivers will not be able to submit the **Extra task** without entering the description of the extra task. If you leave this checkbox unticked, the Drivers will be able to submit this task without having to enter the description of the extra task. 
* You could also set the **Minimum Length** and the **Maximum Length** of the description of the extra tasks by entering the number of characters in the corresponding fields. If you have no intention to restrict the length of the description, you could leave these two fields blank.

<Image title="Description.png" alt={602} className="border" border={true} src="https://files.readme.io/9a4f8b2-Description.png" />

### 7.4 Input Cost

* Component used: **Basic Components > Number**
* Position: Below **Description** component

<Image title="10. Extra Task 4.png" alt={1899} border={true} src="https://files.readme.io/d2e64b9-10._Extra_Task_4.png">
  Illustration (English)
</Image>

<Image title="10, Extra Task - Cost (VIE).png" alt={1890} src="https://files.readme.io/c8c86b1-10_Extra_Task_-_Cost_VIE.png">
  Illustration (Vietnamese)
</Image>

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="12. Cost (ENG).png" alt={595} border={true} src="https://files.readme.io/f00fe37-12._Cost_ENG.png">
  Illustration (English)
</Image>

<Image title="12. Cost (VIE).png" alt={605} border={true} src="https://files.readme.io/ab9c92f-12._Cost_VIE.png">
  Illustration (Vietnamese)
</Image>

* In the **Validation** tab, if you tick the **Required** checkbox, the Drivers will not be able to submit the **Extra task** without entering the cost incurred. If you leave this checkbox unticked, the Drivers will be able to submit this task without having to enter the cost of the extra task. 
* You could also set the **Minimum Value** and the **Maximum Value** of the cost incurred on the extra tasks by entering the amount in corresponding fields. If you have no intention to restrict the amount incurred, you could leave these two fields blank.

<Image title="13. Cost Component.png" alt={605} className="border" border={true} src="https://files.readme.io/bcf43af-13._Cost_Component.png" />
