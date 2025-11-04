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

* In the actual operation, the Terminal Tractor Drivers need to perform many manual tasks during the Shipment delivery process, such as lifting containers, stuffing goods into the containers, attaching and detaching trailers, etc. In the Abivin vRoute system, **Actions** is a feature to help the dispatcher digitize and track the delivery task results of the Terminal Tractor Drivers right on the Web app

## Locate Action Code List

* The Action Codes are listed on the **Tasks > Actions** tab

<Image title="wg9ZXPvGlQ.png" alt={1920} border={true} src="https://files.readme.io/75125fa-wg9ZXPvGlQ.png">
  Illustration (English)
</Image>

<Image title="k5qjJ4AFhc.png" alt={1920} border={true} src="https://files.readme.io/e2985e7-k5qjJ4AFhc.png">
  Illustration (Vietnamese)
</Image>

## Create Action Codes

### Delete Pre-generated Action Codes

* You will see that there are some pre-generated Action Codes when navigating to the **Tasks > Actions** tab. These are the Action Codes of the VRP/DC Model, which are automatically generated right after the Manufacturer was created. You have to delete these pre-generated Action Codes first and then create the correct set of Action Codes of this model
* To remove all the pre-generated Action Codes, click the checkbox icon :fa-square-o: on the title bar of the Action Code table to select all the Action Codes then click the **Delete All** button above the top right corner of the Action Code list

<Image title="1K5DH3aSs6.png" alt={1920} border={true} src="https://files.readme.io/a43dc80-1K5DH3aSs6.png">
  Illustration (English)
</Image>

* A confirmation dialog will appear. Click **Ok** to confirm removing the Action Codes

<Image title="H43efcxcgQ.png" alt={441} border={true} src="https://files.readme.io/af1e50b-H43efcxcgQ.png">
  Illustration (English)
</Image>

### Create New Action Codes

* After you have removed the pre-generated Action Codes, you can proceed to create the correct Action Codes of this model. Please note that you can only use the Excel import file to create the Action Codes
* In the Excel file, you must input the Organization Code of the top Organization - The Manufacturer, into the **Organization Code** cells of all the Action Codes
* The Organization Code can be found under the **Organization Code** column in the **Organizations > Organizations** tab
* Below is the list of all the Action Codes of this model

> ❗️ Note when using the Excel import file
>
> You must delete the quotation marks around the Action Code values in the table below when inputting them in the Excel import file. See the illustration images below the table for reference\
> The Action Name values can be changed freely, not necessarily need to be the same as in the table

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action Code
      </th>

      <th>
        Action Name (Can be changed)
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "SHIPPING\_STARTED"
      </td>

      <td>
        Shipment Starts
      </td>

      <td>
        The Terminal Tractor Driver starts the Shipment
      </td>
    </tr>

    <tr>
      <td>
        "SHIPPING\_COMPLETED"
      </td>

      <td>
        Shipment Completes
      </td>

      <td>
        The Terminal Tractor Driver completes the Shipment
      </td>
    </tr>

    <tr>
      <td>
        "GATE\_IN"
      </td>

      <td>
        Gate In
      </td>

      <td>
        The Terminal Tractor Driver checks in at a port
      </td>
    </tr>

    <tr>
      <td>
        "GATE\_OUT"
      </td>

      <td>
        Gate Out
      </td>

      <td>
        The Terminal Tractor Driver checks out of a port
      </td>
    </tr>

    <tr>
      <td>
        "LIFT*ON*(1)"\
        **Note: Insert the underscore \_ on both sides of the ON text**
      </td>

      <td>
        Lift On 1
      </td>

      <td>
        The Terminal Tractor Driver lifts a non-empty container onto the attrached trailer
      </td>
    </tr>

    <tr>
      <td>
        "LIFT*ON*(0)"\
        **Note: Insert the underscore \_ on both sides of the ON text**
      </td>

      <td>
        Lift On 0
      </td>

      <td>
        The Terminal Tractor Driver lifts an empty container onto the attached trailer
      </td>
    </tr>

    <tr>
      <td>
        "LIFT\_OFF "
      </td>

      <td>
        Lift Off
      </td>

      <td>
        The Terminal Tractor Driver lifts a container off the attached trailer
      </td>
    </tr>

    <tr>
      <td>
        "STUFFING\_START"
      </td>

      <td>
        Stuffing Start
      </td>

      <td>
        The Terminal Tractor Driver starts stuffing goods into a container
      </td>
    </tr>

    <tr>
      <td>
        "STUFFING\_FINISH"
      </td>

      <td>
        Stuffing Finish
      </td>

      <td>
        The Terminal Tractor Driver finishes stuffing goods into a container
      </td>
    </tr>

    <tr>
      <td>
        "DESTUFFING\_START"
      </td>

      <td>
        Destuffing Start
      </td>

      <td>
        The Terminal Tractor Driver starts taking goods out of a container
      </td>
    </tr>

    <tr>
      <td>
        "DESTUFFING\_FINISH"
      </td>

      <td>
        Destuffing Finish
      </td>

      <td>
        The Terminal Tractor Driver finishes taking goods out of a container
      </td>
    </tr>

    <tr>
      <td>
        "NOT\_FREIGHT\_RELATED"
      </td>

      <td>
        Non-freight Related
      </td>

      <td>
        The Terminal Tractor Driver checks in at a Stop that does not belong to the Shipment being operated
      </td>
    </tr>

    <tr>
      <td>
        "TRAILER\_ATTACH"
      </td>

      <td>
        Attach Trailer
      </td>

      <td>
        The Terminal Tractor Driver attaches a trailer to the terminal tractor
      </td>
    </tr>

    <tr>
      <td>
        "TRAILER\_DETACH"
      </td>

      <td>
        Detach Trailer
      </td>

      <td>
        The Terminal Tractor Driver detaches a trailer from the terminal tractor
      </td>
    </tr>
  </tbody>
</Table>

* Below are the screenshot of the Action codes in the Excel template

<Image title="q7ILFImL4m.png" alt={521} border={true} src="https://files.readme.io/3910997-q7ILFImL4m.png">
  Illustration (English)
</Image>

## Create forms for actions

* The action codes recently created above have defined the tasks of this model. However, they have not went in details what information will be gathered in each task, such as: When lifting container, what are the container numbers, is the container full or empty, etc. Forms will help flexibly define the detailed information for each action

### General steps to create forms for actions

* Below are the general steps to create form for a particular action
* Hover on the Action code for which you want to create form, then click on **Form Builder** :fa-cog: icon

<Image title="BQEFgXB14w.png" alt={1920} className="border" border={true} src="https://files.readme.io/14b992d-BQEFgXB14w.png" />

* You will be directed to the **Form Builder** screen, where you can start creating form for that Action code
* You will see a blue **Submit** button. You need to remove it by hovering your mouse over it, then click on the red :fa-remove: icon at the far right

![1897](https://files.readme.io/a6b9954-110bbaf-2019-11-02_22_04_17-Window.png "110bbaf-2019-11-02_22_04_17-Window.png")

* Now you can begin to create form for the Action code, by dragging the appropriate component on the left side to the right side

<Image title="cc9fdc0-drag_component.gif" alt={1916} className="border" border={true} src="https://files.readme.io/260f8d7-cc9fdc0-drag_component.gif" />

* The set up form of the component will appear. Input data into that form, then click **Save**
* We will specify the detail for each component below

<Image title="ae64083-2019-11-02_22_13_30-Window.png" alt={1228} className="border" border={true} src="https://files.readme.io/bb0d21d-ae64083-2019-11-02_22_13_30-Window.png" />

* **Note:** For some special components, you can drag other components ***inside*** them
* After you have finished configuring all components, scroll down the **Form Builder** screen, then click on **Save View** to finish creating the form for the Action code

<Image title="83ccff7-2019-11-04_13_47_00-Window.png" alt={1228} className="border" border={true} src="https://files.readme.io/b79005a-83ccff7-2019-11-04_13_47_00-Window.png" />

* A pop up will appear to let you know you have succeeded creating the form

<Image title="698e035-2019-11-02_22_29_38-Window.png" alt={431} className="border" border={true} src="https://files.readme.io/23a2246-698e035-2019-11-02_22_29_38-Window.png" />

* Click on **Back** to get back to the Action list tab. You can continue to create forms for other Action codes

<Image title="592bb87-2019-11-02_22_31_00-Window.png" alt={1902} className="border" border={true} src="https://files.readme.io/9484e16-592bb87-2019-11-02_22_31_00-Window.png" />

* Now we will move on to create form for each action code

## GATE\_IN; GATE\_OUT; LIFTON(0); LIFT\_OFF; STUFFING\_START; STUFFING\_FINISH; DESTUFFING\_START; DESTUFFING\_FINISH; NOT\_FREIGHT\_RELATED Action codes

### **1.1 Check In Panel**

* Component used: **Special Components > File**

<Image title="f4b6793-2019-10-24_17_16_52-Window.png" alt={1631} className="border" border={true} src="https://files.readme.io/850f9e1-f4b6793-2019-10-24_17_16_52-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="39afea5-53c9838-2019-10-25_11_12_02-Window.png" alt={534} className="border" border={true} src="https://files.readme.io/daf4ef1-39afea5-53c9838-2019-10-25_11_12_02-Window.png" />

<Image title="96548a2-eca9da0-2019-10-25_17_33_02-Window.png" alt={611} className="border" border={true} src="https://files.readme.io/70d7f73-96548a2-eca9da0-2019-10-25_17_33_02-Window.png" />

<Image title="68a5998-7c59bdd-2019-10-24_15_33_26-Window.png" alt={522} className="border" border={true} src="https://files.readme.io/4f6de56-68a5998-7c59bdd-2019-10-24_15_33_26-Window.png" />

## LIFTON(1) Action code

### **2.1 Container Panel**

* Component used: **Layout Components > Panel**
* Position: On top

<Image title="LIFT.1.png" alt={1896} className="border" border={true} src="https://files.readme.io/e7f7d71-LIFT.1.png" />

* Component content:
* Note: The value input into **Title** field can be changed freely

<Image title="Image 2.png" alt={602} className="border" border={true} src="https://files.readme.io/d778709-Image_2.png" />

### **2.2 Container Number field**

* Component used: **Basic Components > Text Field**
* Position: Inside **Container Panel**

<Image title="conno.png" alt={1896} className="border" border={true} src="https://files.readme.io/6c65b96-conno.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="conno3.png" alt={598} className="border" border={true} src="https://files.readme.io/322064a-conno3.png" />

<Image title="conno2.png" alt={375} className="border" border={true} src="https://files.readme.io/1de7541-conno2.png" />

* Note: To add more custom properties, click on **Add Value**

<Image title="conno4.png" alt={607} className="border" border={true} src="https://files.readme.io/be156d6-conno4.png" />

### **2.3 Seal Number field**

* Component used: **Basic Components > Text Field**
* Position: Inside **Container Panel**, below **Container Number field**

<Image title="sealno3.png" alt={1898} className="border" border={true} src="https://files.readme.io/b3caa86-sealno3.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="sealno2.png" alt={597} className="border" border={true} src="https://files.readme.io/49ed80a-sealno2.png" />

<Image title="sealno1.png" alt={597} className="border" border={true} src="https://files.readme.io/82d9afb-sealno1.png" />

### **2.4 Container Tare Weight field**

* Component used: **Basic Components > Number**
* Position: Inside **Container Panel**, below **Seal Number field**

<Image title="tare3.png" alt={1894} className="border" border={true} src="https://files.readme.io/573a729-tare3.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="tare2.png" alt={595} className="border" border={true} src="https://files.readme.io/1a01695-tare2.png" />

<Image title="tare1.png" alt={602} className="border" border={true} src="https://files.readme.io/2045a6c-tare1.png" />

### **2.5 Container Max Gross Weight field**

* Component used: **Basic Components > Number**
* Position: Inside **Container Panel**, below **Container Tare Weight field**

<Image title="maxgr03.png" alt={1896} className="border" border={true} src="https://files.readme.io/ebdc25c-maxgr03.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="maxgr01.png" alt={600} className="border" border={true} src="https://files.readme.io/b606861-maxgr01.png" />

<Image title="maxgr02.png" alt={595} className="border" border={true} src="https://files.readme.io/238c387-maxgr02.png" />

### **2.6 Container Photos Panel**

* Component used: **Special Components > File**
* Position: Inside **Container Panel**, below **Container Max Gross Weight field**

<Image title="conpho03.png" alt={1900} className="border" border={true} src="https://files.readme.io/6b9a95a-conpho03.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="conpho01.png" alt={602} className="border" border={true} src="https://files.readme.io/e23dc24-conpho01.png" />

* Note: The value of the property ***numberOfImages*** doesn't necessarily have to be ***5***. You can change to a different number according to how many photos you need

<Image title="conpho02.png" alt={591} className="border" border={true} src="https://files.readme.io/f88e39f-conpho02.png" />

## TRAILER\_ATTACH Action code

### **3.1 Trailer Selection panel**

* Component used: **Basic Components > Select**
* Position: On top

<Image title="Selection_009.png" alt={1857} className="border" border={true} src="https://files.readme.io/5285a86-Selection_009.png" />

* Component content:
* Tab **Display**
* Note: The value input into **Label** field can be changed freely

<Image title="Selection_001.png" alt={611} className="border" border={true} src="https://files.readme.io/3695ee5-Selection_001.png" />

* Tab **Data**

<Image title="Selection_002.png" alt={599} className="border" border={true} src="https://files.readme.io/5c79741-Selection_002.png" />

<Image title="Selection_003.png" alt={608} className="border" border={true} src="https://files.readme.io/89fc9af-Selection_003.png" />

* Tab **Validation**

<Image title="Selection_004.png" alt={359} className="border" border={true} src="https://files.readme.io/4f53f3d-Selection_004.png" />

* Tab **API**

<Image title="Selection_005.png" alt={580} className="border" border={true} src="https://files.readme.io/740c87d-Selection_005.png" />

### **3.2 Trailer Photos Panel**

* Component used: **Special Components > File**
* Position: Below **Trailer Selection panel**

<Image title="Selection_010.png" alt={1850} className="border" border={true} src="https://files.readme.io/1c1a204-Selection_010.png" />

* Component content:

## TRAILER\_DETACH Action code

### **4.1 Trailer Photos Panel**

* Component used: **Special Components > File**
* Position: On top

![1858](https://files.readme.io/3681cf6-Selection_011.png "Selection_011.png")

* Component content:
* Tab **Display**
* Note: The value input into **Label** field can be changed freely

<Image title="Selection_012.png" alt={608} className="border" border={true} src="https://files.readme.io/2fa0288-Selection_012.png" />

* Tab **API**
* Note: You can change the value input into the field **Value** to be a different number, as long as it is less than ***5***. The value input here equals to the maximum photos you can take when using the Mobile app

<Image title="Selection_013.png" alt={602} className="border" border={true} src="https://files.readme.io/1383fa5-Selection_013.png" />
