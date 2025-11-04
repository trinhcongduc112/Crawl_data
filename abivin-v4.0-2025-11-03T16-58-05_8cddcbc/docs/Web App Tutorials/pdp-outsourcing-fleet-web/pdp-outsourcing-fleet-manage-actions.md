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
> ❗️ Error with Excel template
>
> At the moment, there is an error with the method of creating Action Codes using Excel template. Therefore, please use the Web form to create Action Codes instead. We will get this problem resolved soon!

## Create actions

* Navigate to **Tasks > Action List** tab

## Delete pre-generated action codes

* You will notice that a set of actions has been automatically created. These are the default action codes for VRP model
* You would need to delete those pre-generated actions by clicking on the icon :fa-square-o: on the toolbar, then click on the button **Delete All**

<Image title="delete ac code.png" alt={1904} className="border" border={true} src="https://files.readme.io/e88310b-delete_ac_code.png" />

## Create actions for PDP - Outsourcing Fleet Model

* After you have deleted those actions, you need to create the actions for this model, using Web form or Excel template
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template
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
        Organization Code
      </th>

      <th>
        Action Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        DEPOT\_DELIVERY
      </td>

      <td>
        Origin Depot Delivers
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>

      <td>
        Warehouseman of the Origin Depot hands products to the Transporter's driver
      </td>
    </tr>

    <tr>
      <td>
        DEPOT\_RECEIVING
      </td>

      <td>
        Destination Depot Receives
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>

      <td>
        Warehouseman of the Destination Depot receives products from the Transporter's driver
      </td>
    </tr>

    <tr>
      <td>
        LOADING\_AT\_DEPOT
      </td>

      <td>
        Driver Checks in at Destination Depot
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>

      <td>
        Transporter's driver checks in at the Destination Depot
      </td>
    </tr>

    <tr>
      <td>
        DELIVER\_PRODUCT
      </td>

      <td>
        Driver Delivers Product
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>

      <td>
        Transporter's driver hands the products to the Warehouseman of the Destination Depot
      </td>
    </tr>

    <tr>
      <td>
        BACK\_DEPOT
      </td>

      <td>
        Driver Back to Depot
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>

      <td>
        Transporter's driver checks in at the Transporter garage upon returning
      </td>
    </tr>

    <tr>
      <td>
        END\_DAY
      </td>

      <td>
        Driver Ends Day
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>

      <td>
        Transporter's driver ends working day at the Transporter garage
      </td>
    </tr>

    <tr>
      <td>
        TRANSIT
      </td>

      <td>
        Driver Transits
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>

      <td>
        Transporter's driver rests for 8 hours after working 24 hours (Including driving, loading/unloading products)
      </td>
    </tr>

    <tr>
      <td>
        LOADING\_AT\_STORE
      </td>

      <td>
        Driver Loads Products at Origin Depot
      </td>

      <td>
        Always input the Organization Code of the Manufacturer
      </td>

      <td>
        Transporter's driver loads products at the Origin Depot
      </td>
    </tr>
  </tbody>
</Table>

## Create forms for actions

## General steps

* Hover on the Action code for which you want to create form, then click on **Form Builder** :fa-cog: icon

<Image title="d397277-2019-11-02_21_53_45-Window.png" alt={1326} className="border" border={true} src="https://files.readme.io/37242bd-d397277-2019-11-02_21_53_45-Window.png" />

* You will be directed to the **Form Builder** screen, where you can start creating form for that Action code

<Image title="24f85fc-2019-11-02_21_55_10-Window (1).png" alt={1897} className="border" border={true} src="https://files.readme.io/1d80ced-24f85fc-2019-11-02_21_55_10-Window_1.png" />

* You will see a blue **Submit** button. You need to remove it by hovering your mouse over it, then click on the red :fa-remove: icon at the far right

<Image title="110bbaf-2019-11-02_22_04_17-Window (1).png" alt={1897} className="border" border={true} src="https://files.readme.io/b24f8f3-110bbaf-2019-11-02_22_04_17-Window_1.png" />

* Now you can begin to create form for the Action code, by dragging the appropriate component on the left side to the right side

<Image title="cc9fdc0-drag_component (1).gif" alt={1916} className="border" border={true} src="https://files.readme.io/fb7ebf0-cc9fdc0-drag_component_1.gif" />

* The set up form of the component will appear. Input data into that form, then click **Save**
* We will specify the detail for each component below

> ❗️ All data must be input exactly as shown on images, both lowercase and uppercase letters, unless otherwise specified

<Image title="ae64083-2019-11-02_22_13_30-Window (1).png" alt={1228} className="border" border={true} src="https://files.readme.io/dc629c4-ae64083-2019-11-02_22_13_30-Window_1.png" />

* **Note:** For some special components, you can drag other components inside them
* After you have finished configuring all components, scroll down the **Form Builder** screen, then click on **Save View** to finish creating the form for the Action code

<Image title="83ccff7-2019-11-04_13_47_00-Window (1).png" alt={1228} className="border" border={true} src="https://files.readme.io/f8d721e-83ccff7-2019-11-04_13_47_00-Window_1.png" />

* A pop up will appear to let you know you have succeeded creating the form

<Image title="698e035-2019-11-02_22_29_38-Window (1).png" alt={431} className="border" border={true} src="https://files.readme.io/98a1cb3-698e035-2019-11-02_22_29_38-Window_1.png" />

* Click on **Back** to get back to the Action list tab. You can continue to create forms for other Action codes

<Image title="592bb87-2019-11-02_22_31_00-Window (1).png" alt={1902} className="border" border={true} src="https://files.readme.io/807d0a9-592bb87-2019-11-02_22_31_00-Window_1.png" />

* We will now move on to create form for each action code

## DEPOT\_DELIVERY; DEPOT\_RECEIVING action codes

### **1.1 Shipping Information Panel**

* Component used: **Layout Components > Panel**
* Position: On top

<Image title="2019-10-24 11_14_17-Window.png" alt={1652} className="border" border={true} src="https://files.readme.io/d566e38-2019-10-24_11_14_17-Window.png" />

* Component content:
* Note: The value input into **Title** field can be changed freely

<Image title="2019-10-24 15_59_24-Window.png" alt={534} className="border" border={true} src="https://files.readme.io/91721bc-2019-10-24_15_59_24-Window.png" />

### **1.2 Warehouse Name Panel**

* Component used: **Basic Components > Text Field**
* Position: Inside **Shipping Information** panel

<Image title="2019-10-24 11_30_33-Window.png" alt={1620} className="border" border={true} src="https://files.readme.io/297ae7c-2019-10-24_11_30_33-Window.png" />

* Component content:
* Note: The value input into **Title** field can be changed freely

<Image title="2019-10-24 11_27_48-Window.png" alt={538} className="border" border={true} src="https://files.readme.io/f7d0e11-2019-10-24_11_27_48-Window.png" />

<Image title="2019-10-24 11_27_02-Window.png" alt={533} className="border" border={true} src="https://files.readme.io/bbba1d0-2019-10-24_11_27_02-Window.png" />

### **1.3 Transporter Name Panel**

* Component used: **Basic Components > Text Field**
* Position: Inside **Shipping Information** panel, below **Warehouse Name** panel

<Image title="2019-10-24 11_40_16-Window.png" alt={1613} className="border" border={true} src="https://files.readme.io/3a9c1f4-2019-10-24_11_40_16-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-10-24 11_39_25-Window.png" alt={539} className="border" border={true} src="https://files.readme.io/662a713-2019-10-24_11_39_25-Window.png" />

<Image title="2019-10-24 11_37_48-Window.png" alt={535} className="border" border={true} src="https://files.readme.io/6d2d9f8-2019-10-24_11_37_48-Window.png" />

### **1.4 Vehicle Information Panel**

* Component used: **Layout Components > Panel**
* Position: Below **Shipping Information** panel

<Image title="2019-10-24 11_46_06-Window.png" alt={1619} className="border" border={true} src="https://files.readme.io/9516ac7-2019-10-24_11_46_06-Window.png" />

* Component content:
* Note: The value input into **Title** field can be changed freely

<Image title="2019-10-24 11_49_11-Window.png" alt={524} className="border" border={true} src="https://files.readme.io/b84da51-2019-10-24_11_49_11-Window.png" />

### **1.5 Driver Name Panel**

* Component used: **Basic Components > Text Field**
* Position: Inside **Vehicle Information** panel

<Image title="2019-10-24 11_50_16-Window.png" alt={1613} className="border" border={true} src="https://files.readme.io/364d8b6-2019-10-24_11_50_16-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-10-24 11_51_55-Window.png" alt={528} className="border" border={true} src="https://files.readme.io/2a9f35a-2019-10-24_11_51_55-Window.png" />

<Image title="2019-10-24 11_55_50-Window.png" alt={531} className="border" border={true} src="https://files.readme.io/d2896d7-2019-10-24_11_55_50-Window.png" />

### **1.6 Vehicle License Plate Number Panel**

* Component used: **Basic Components > Select**
* Position: Inside **Vehicle Information** panel, below **Driver Name** panel

<Image title="2019-10-24 12_00_55-Window.png" alt={1639} className="border" border={true} src="https://files.readme.io/818674a-2019-10-24_12_00_55-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-10-24 12_02_18-Window.png" alt={540} className="border" border={true} src="https://files.readme.io/c7cbe4e-2019-10-24_12_02_18-Window.png" />

<Image title="2019-10-25 10_59_26-Window.png" alt={521} className="border" border={true} src="https://files.readme.io/522342f-2019-10-25_10_59_26-Window.png" />

<Image title="2019-10-24 15_15_42-Window.png" alt={533} className="border" border={true} src="https://files.readme.io/b867518-2019-10-24_15_15_42-Window.png" />

### **1.7 Order Information Panel**

* Component used: **Special Components > Container**
* Position: Below **Vehicle Information** panel

<Image title="2019-10-24 15_17_26-Window.png" alt={1631} className="border" border={true} src="https://files.readme.io/9f973a1-2019-10-24_15_17_26-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

![531](https://files.readme.io/134728f-2019-10-25_11_06_15-Window.png "2019-10-25 11_06_15-Window.png")

<Image title="2019-10-25 17_32_16-Window.png" alt={597} className="border" border={true} src="https://files.readme.io/8d4b69a-2019-10-25_17_32_16-Window.png" />

### **1.8 Check In Panel**

* Component used: **Special Components > File**
* Position: Below **Order Information** panel

<Image title="2019-10-24 15_44_25-Window.png" alt={1618} className="border" border={true} src="https://files.readme.io/1f37fa1-2019-10-24_15_44_25-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-10-25 11_12_02-Window.png" alt={534} className="border" border={true} src="https://files.readme.io/53c9838-2019-10-25_11_12_02-Window.png" />

<Image title="2019-10-25 17_33_02-Window.png" alt={611} className="border" border={true} src="https://files.readme.io/eca9da0-2019-10-25_17_33_02-Window.png" />

![522](https://files.readme.io/7c59bdd-2019-10-24_15_33_26-Window.png "2019-10-24 15_33_26-Window.png")

## TRANSIT action code

### **2.1 Check In Panel**

* Component used: **Special Components > File**

<Image title="2019-10-24 17_16_52-Window.png" alt={1631} className="border" border={true} src="https://files.readme.io/f4b6793-2019-10-24_17_16_52-Window.png" />

* Component content:
* Similar as [**Check In Panel**](https://docs.abivin.com/docs/pdp-outsourcing-manage-actions#section-1-8-check-in-panel) described above

## LOADING\_AT\_STORE action code

### **3.1 Order Information Panel**

* Component used: **Special Components > Container**
* Position: On top

<Image title="2019-10-24 17_32_03-Window.png" alt={1635} className="border" border={true} src="https://files.readme.io/237421f-2019-10-24_17_32_03-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-10-24 17_25_23-Window.png" alt={531} className="border" border={true} src="https://files.readme.io/baf9260-2019-10-24_17_25_23-Window.png" />

<Image title="2019-10-24 17_31_05-Window.png" alt={521} className="border" border={true} src="https://files.readme.io/f7900ca-2019-10-24_17_31_05-Window.png" />

### **3.2 Check In Panel**

* Component used: **Special Components > File**
* Position: Below **Order Information** panel

<Image title="2019-10-24 17_55_39-Window.png" alt={1638} className="border" border={true} src="https://files.readme.io/42fd641-2019-10-24_17_55_39-Window.png" />

* Component content:
* Similar as [**Check In Panel**](https://docs.abivin.com/docs/pdp-outsourcing-manage-actions#section-1-8-check-in-panel) described above

## LOADING\_AT\_DEPOT; END\_DAY action codes

### **4.1 Order Information Panel**

* Component used: **Layout Components > Panel**
* Position: On top

<Image title="2019-10-25 08_44_14-Window.png" alt={1619} className="border" border={true} src="https://files.readme.io/cf185a8-2019-10-25_08_44_14-Window.png" />

* Component content:
* Note: The value input into **Title** field can be changed freely

<Image title="2019-10-25 08_42_58-Window.png" alt={535} className="border" border={true} src="https://files.readme.io/f8ff2f5-2019-10-25_08_42_58-Window.png" />

### **4.2 Order Table Panel**

* Component used: **Layout Components > Table**
* Position: Inside **Order Information** panel

<Image title="2019-10-25 08_56_14-Window.png" alt={1618} className="border" border={true} src="https://files.readme.io/ca7f5a2-2019-10-25_08_56_14-Window.png" />

* Component content:

<Image title="2019-10-25 08_53_56-Window.png" alt={526} className="border" border={true} src="https://files.readme.io/67feb71-2019-10-25_08_53_56-Window.png" />

### **4.3 Order Code Panel**

* Position: Inside **Order Table** panel

<Image title="2019-10-25 09_02_58-Window.png" alt={1619} className="border" border={true} src="https://files.readme.io/2ba8782-2019-10-25_09_02_58-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-10-25 08_47_31-Window.png" alt={520} className="border" border={true} src="https://files.readme.io/14cf5d2-2019-10-25_08_47_31-Window.png" />

<Image title="2019-10-25 11_35_22-Window.png" alt={531} className="border" border={true} src="https://files.readme.io/7296836-2019-10-25_11_35_22-Window.png" />

<Image title="2019-10-25 08_49_46-Window.png" alt={527} className="border" border={true} src="https://files.readme.io/bdc0990-2019-10-25_08_49_46-Window.png" />

### **4.4 Total Order Weight Panel**

* Component used: **Basic Components > Text Field**
* Position: Inside **Order Table** panel, to the right of **Order Code** panel

<Image title="2019-10-25 09_10_18-Window.png" alt={1616} className="border" border={true} src="https://files.readme.io/1332ee5-2019-10-25_09_10_18-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-10-25 09_05_58-Window.png" alt={534} className="border" border={true} src="https://files.readme.io/1d14a74-2019-10-25_09_05_58-Window.png" />

<Image title="2019-10-25 09_08_34-Window.png" alt={533} className="border" border={true} src="https://files.readme.io/2af9056-2019-10-25_09_08_34-Window.png" />

<Image title="2019-10-25 09_09_29-Window.png" alt={530} className="border" border={true} src="https://files.readme.io/6cdc303-2019-10-25_09_09_29-Window.png" />

### **4.5 Check In Panel**

* Component used: **Special Components > File**
* Position: Below **Order Information** panel

<Image title="2019-10-25 09_24_19-Window.png" alt={1641} className="border" border={true} src="https://files.readme.io/68b3997-2019-10-25_09_24_19-Window.png" />

* Component content:
* Similar as [**Check In Panel**](https://docs.abivin.com/docs/pdp-outsourcing-manage-actions#section-1-8-check-in-panel) described above

## DELIVER\_PRODUCT;  BACK\_DEPOT action codes

### **5.1 Order Information Panel**

* Component used: **Special Components > Container**
* Position: On top

<Image title="2019-10-25 09_39_15-Window.png" alt={1637} className="border" border={true} src="https://files.readme.io/5000238-2019-10-25_09_39_15-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="2019-10-25 11_44_51-Window.png" alt={524} className="border" border={true} src="https://files.readme.io/0d99548-2019-10-25_11_44_51-Window.png" />

<Image title="2019-10-25 11_43_36-Window.png" alt={523} className="border" border={true} src="https://files.readme.io/e684f40-2019-10-25_11_43_36-Window.png" />

### **5.2 Check In Panel**

* Component used: **Special Components > File**
* Position: Below **Order Information** panel

<Image title="2019-10-25 09_38_23-Window.png" alt={1637} className="border" border={true} src="https://files.readme.io/139dbfb-2019-10-25_09_38_23-Window.png" />

* Component content:
* Similar as [**Check In Panel**](https://docs.abivin.com/docs/pdp-outsourcing-manage-actions#section-1-8-check-in-panel) described above
