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
## Create actions

* Navigate to **Tasks > Action List** tab
* You will notice that a set of actions has been automatically created. These are the default action codes for VRP model

<Image title="2019-11-02 21_37_03-Window.png" alt={1914} className="border" border={true} src="https://files.readme.io/410850a-2019-11-02_21_37_03-Window.png" />

* In case there are no action code, you can create the action using Excel template. Below are the information fields of the actions

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action Code (Compulsory)
      </th>

      <th>
        Action Name (Can be changed)
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
        Loading Products at Depot
      </td>

      <td>
        Always use the organization code of the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        DELIVER\_PRODUCT
      </td>

      <td>
        Deliver Products to customer
      </td>

      <td>
        Always use the organization code of the Manufacturer
      </td>
    </tr>

    <tr>
      <td>
        END\_DAY
      </td>

      <td>
        End of Day
      </td>

      <td>
        Always use the organization code of the Manufacturer
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
        Always use the organization code of the Manufacturer
      </td>
    </tr>
  </tbody>
</Table>

## Create forms for actions

## General steps

* Hover on the Action code for which you want to create form, then click on **Form Builder** :fa-cog: icon

<Image title="2019-11-02 21_53_45-Window.png" alt={1326} className="border" border={true} src="https://files.readme.io/d397277-2019-11-02_21_53_45-Window.png" />

* You will be directed to the **Form Builder** screen, where you can start creating form for that Action code

<Image title="2019-11-02 21_55_10-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/24f85fc-2019-11-02_21_55_10-Window.png" />

* You will see a blue **Submit** button. You need to remove it by hovering your mouse over it, then click on the red :fa-remove: icon at the far right

<Image title="2019-11-02 22_04_17-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/110bbaf-2019-11-02_22_04_17-Window.png" />

* Now you can begin to create form for the Action code, by dragging the appropriate component on the left side to the right side

<Image title="drag component.gif" alt={1916} className="border" border={true} src="https://files.readme.io/cc9fdc0-drag_component.gif" />

* The set up form of the component will appear. Input data into that form, then click **Save**
* We will specify the detail for each component below

<Image title="2019-11-02 22_13_30-Window.png" alt={1228} className="border" border={true} src="https://files.readme.io/ae64083-2019-11-02_22_13_30-Window.png" />

* **Note:** For some special components, you can drag other components inside them
* After you have finished configuring all components, scroll down the **Form Builder** screen, then click on **Save View** to finish creating the form for the Action code

<Image title="2019-11-04 13_47_00-Window.png" alt={1228} className="border" border={true} src="https://files.readme.io/83ccff7-2019-11-04_13_47_00-Window.png" />

* A pop up will appear to let you know you have succeeded creating the form

<Image title="2019-11-02 22_29_38-Window.png" alt={431} className="border" border={true} src="https://files.readme.io/698e035-2019-11-02_22_29_38-Window.png" />

* Click on **Back** to get back to the Action list tab. You can continue to create forms for other Action codes

<Image title="2019-11-02 22_31_00-Window.png" alt={1902} className="border" border={true} src="https://files.readme.io/592bb87-2019-11-02_22_31_00-Window.png" />

* We will now move on to create form for each action code

## **LOADING\_AT\_DEPOT Action code**

### **1.1 Order Information panel**

* Component used: **Layout Components > Panel**
* Position: On top

<Image title="2019-11-04 13_52_10-Window.png" alt={1903} className="border" border={true} src="https://files.readme.io/90d2939-2019-11-04_13_52_10-Window.png" />

* Component content:
* Note: The value input into **Title** field can be changed freely

<Image title="2019-11-04 13_48_22-Window.png" alt={599} className="border" border={true} src="https://files.readme.io/189fc3d-2019-11-04_13_48_22-Window.png" />

<Image title="2019-11-04 13_49_57-Window.png" alt={599} className="border" border={true} src="https://files.readme.io/85d4e14-2019-11-04_13_49_57-Window.png" />

### **1.2 Order Information Table**

* Component used: **Layout Components > Table**
* Position: Inside **Order Information Panel** component

<Image title="2019-11-04 13_57_16-Window.png" alt={1900} className="border" border={true} src="https://files.readme.io/1cfc40f-2019-11-04_13_57_16-Window.png" />

* Component content:

<Image title="2019-11-04 13_54_00-Window.png" alt={602} className="border" border={true} src="https://files.readme.io/70d9dc5-2019-11-04_13_54_00-Window.png" />

<Image title="2019-11-04 13_56_13-Window.png" alt={603} className="border" border={true} src="https://files.readme.io/8e396e5-2019-11-04_13_56_13-Window.png" />

### **1.3 Order Code Field**

* Component used: **Basic Components > Text Field**
* Position: Inside **Order Information Table** component

<Image title="2019-11-04 14_03_03-Window.png" alt={1901} className="border" border={true} src="https://files.readme.io/0750c80-2019-11-04_14_03_03-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-11-04 13_59_15-Window.png" alt={603} className="border" border={true} src="https://files.readme.io/e91bb38-2019-11-04_13_59_15-Window.png" />

<Image title="2019-11-04 14_02_00-Window.png" alt={612} className="border" border={true} src="https://files.readme.io/e66aa4b-2019-11-04_14_02_00-Window.png" />

### **1.4 Customer Code Field**

* Component used: **Basic Components > Text Field**
* Position: Inside **Order Information Table** component, to the right of **Order Code Field** component

<Image title="2019-11-04 14_09_11-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/4c15df6-2019-11-04_14_09_11-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-11-04 14_06_00-Window.png" alt={596} className="border" border={true} src="https://files.readme.io/2c729e7-2019-11-04_14_06_00-Window.png" />

![600](https://files.readme.io/e7b1b00-2019-11-04_14_08_20-Window.png "2019-11-04 14_08_20-Window.png")

### **1.5 Customer Name Field**

* Component used: **Basic Components > Text Field**
* Position: Inside **Order Information Table** component, to the right of **Customer Code Field** component

<Image title="2019-11-04 14_15_12-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/d1e6f95-2019-11-04_14_15_12-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-11-04 14_11_29-Window.png" alt={595} className="border" border={true} src="https://files.readme.io/8f48daf-2019-11-04_14_11_29-Window.png" />

<Image title="2019-11-04 14_14_18-Window.png" alt={605} className="border" border={true} src="https://files.readme.io/31bb994-2019-11-04_14_14_18-Window.png" />

### **1.6 Amount of Money to be collected Field**

* Component used: **Basic Components > Text Field**
* Position: Inside **Order Information Table** component, to the right of **Customer Name Field** component

<Image title="2019-11-04 14_21_40-Window.png" alt={1909} className="border" border={true} src="https://files.readme.io/9e78ad1-2019-11-04_14_21_40-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-11-04 14_17_40-Window.png" alt={602} className="border" border={true} src="https://files.readme.io/b0883b9-2019-11-04_14_17_40-Window.png" />

<Image title="2019-11-04 14_20_29-Window.png" alt={606} className="border" border={true} src="https://files.readme.io/0fa8b46-2019-11-04_14_20_29-Window.png" />

### **1.7 Check In panel**

* There are two options on how the driver performs the Check In action

#### **1.7.1 Check In with the coordinate information of the location where the driver is standing**

* Component used: **Special Components > Address**
* Position: Below **Order Information panel** component

<Image title="2019-11-04 14_45_02-Window.png" alt={1892} className="border" border={true} src="https://files.readme.io/617fd3b-2019-11-04_14_45_02-Window.png" />

* Component content:

<Image title="2019-11-04 14_32_01-Window.png" alt={597} className="border" border={true} src="https://files.readme.io/c4c940f-2019-11-04_14_32_01-Window.png" />

<Image title="2019-11-04 14_38_14-Window.png" alt={312} className="border" border={true} src="https://files.readme.io/774309f-2019-11-04_14_38_14-Window.png" />

#### **1.7.2 Check In with an image of the location where the driver is standing**

* Component used: **Special Components > File**
* Position: Below **Order Information panel** component
* Component content:

![409](https://files.readme.io/8e2224c-2019-11-04_15_37_59-Abivin_vApp.png "2019-11-04 15_37_59-Abivin vApp.png")

<Image title="2019-11-04 15_08_34-Window.png" alt={358} className="border" border={true} src="https://files.readme.io/a22c8a9-2019-11-04_15_08_34-Window.png" />

### **1.8 Order Status Confirmation panel**

* Component used: **Layout Components > Panel** 
* Position: Below **Check In panel** component

<Image title="2019-11-04 14_56_23-Window.png" alt={1903} className="border" border={true} src="https://files.readme.io/21dd960-2019-11-04_14_56_23-Window.png" />

* Component content:
* Note: The value input into **Title** field can be changed freely

<Image title="2019-11-04 14_50_16-Window.png" alt={599} className="border" border={true} src="https://files.readme.io/31dbcbc-2019-11-04_14_50_16-Window.png" />

### **1.9 Confirm to have taken products out of the warehouse Checkbox**

* Position: Inside **Order Status Confirmation panel** component

<Image title="2019-11-04 15_09_48-Window.png" alt={1897} className="border" border={true} src="https://files.readme.io/0cca580-2019-11-04_15_09_48-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-11-04 15_05_58-Window.png" alt={590} className="border" border={true} src="https://files.readme.io/35a153c-2019-11-04_15_05_58-Window.png" />

<Image title="2019-11-04 15_08_34-Window.png" alt={358} className="border" border={true} src="https://files.readme.io/51b7acd-2019-11-04_15_08_34-Window.png" />

### **1.10 Confirm to have left the warehouse Checkbox**

* Position: Inside **Order Status Confirmation panel** component, below **Confirm to have taken products out of the warehouse checkbox** component

<Image title="2019-11-04 15_13_29-Window.png" alt={1893} className="border" border={true} src="https://files.readme.io/047046e-2019-11-04_15_13_29-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-11-04 15_11_13-Window.png" alt={594} className="border" border={true} src="https://files.readme.io/cdbe37f-2019-11-04_15_11_13-Window.png" />

<Image title="2019-11-04 15_08_34-Window.png" alt={358} className="border" border={true} src="https://files.readme.io/0ba1468-2019-11-04_15_08_34-Window.png" />

## **DELIVER\_PRODUCT Action code**

### **2.1 Check In panel**

* See instruction [**above**](https://docs.abivin.com/docs/vrp-outsourcing-manage-actions#section-1-7-check-in-panel)

### **2.2 Bill receiving confirmation panel**

* Component used: **Layout Components > Panel**
* Position: Below **Check In panel** component

<Image title="2019-11-04 16_20_00-Window.png" alt={1902} className="border" border={true} src="https://files.readme.io/2ca1a9e-2019-11-04_16_20_00-Window.png" />

* Component content:
* Note: The value input into **Title** field can be changed freely

<Image title="112.png" alt={597} className="border" border={true} src="https://files.readme.io/79a17c3-112.png" />

### **2.3 Bill receiving confirmation check box**

* Component used: **Basic Components > Check Box**
* Position: Inside **Bill receiving confirmation panel**
* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2323.png" alt={596} className="border" border={true} src="https://files.readme.io/c323e6b-2323.png" />

<Image title="53453.png" alt={602} className="border" border={true} src="https://files.readme.io/9740507-53453.png" />

<Image title="354352.png" alt={371} className="border" border={true} src="https://files.readme.io/96b391c-354352.png" />

## **BACK\_DEPOT Action code**

### **3.1 Check In panel**

* See instruction [**above**](https://docs.abivin.com/docs/vrp-outsourcing-manage-actions#section-1-7-check-in-panel)

### **3.2 Update status at the end of day panel**

* Component used: **Layout Components > Panel**
* Position: Below **Check In panel** component

<Image title="2019-11-04 16_27_06-Window.png" alt={597} className="border" border={true} src="https://files.readme.io/63d54af-2019-11-04_16_27_06-Window.png" />

### **3.3 Confirm to have handed all redundant products to the warehouse manager Check box**

* Component used: **Basic Components > Check Box**
* Position: Inside **Update status at the end of day panel** component

<Image title="2019-11-04 16_48_40-Window.png" alt={1896} className="border" border={true} src="https://files.readme.io/65b2b7c-2019-11-04_16_48_40-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-11-04 16_51_29-Window.png" alt={610} className="border" border={true} src="https://files.readme.io/e5c808f-2019-11-04_16_51_29-Window.png" />

<Image title="2019-11-04 16_30_19-Window.png" alt={356} className="border" border={true} src="https://files.readme.io/11573aa-2019-11-04_16_30_19-Window.png" />

### **3.4 Confirm to have handed all collected cash to accountant Check box**

* Component used: **Basic Components > Check Box**
* Position: Inside **Update status at the end of day panel** component, below **Confirm to have handed all redundant products to the warehouse manager Check box** component

<Image title="2019-11-04 16_38_24-Window.png" alt={1892} className="border" border={true} src="https://files.readme.io/3439f8c-2019-11-04_16_38_24-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-11-04 16_37_38-Window.png" alt={602} className="border" border={true} src="https://files.readme.io/e660728-2019-11-04_16_37_38-Window.png" />

<Image title="2019-11-04 16_30_19-Window.png" alt={356} className="border" border={true} src="https://files.readme.io/efaa218-2019-11-04_16_30_19-Window.png" />

## **END\_DAY Action code**

### **4.1 Check In panel**

* See instruction [**above**](https://docs.abivin.com/docs/vrp-outsourcing-manage-actions#section-1-7-check-in-panel)
