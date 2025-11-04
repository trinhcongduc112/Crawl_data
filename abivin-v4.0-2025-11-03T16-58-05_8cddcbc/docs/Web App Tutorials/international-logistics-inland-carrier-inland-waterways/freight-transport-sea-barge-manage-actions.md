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

* During a typical Shipment delivery process, the barge captains need to perform certain manual tasks, which includes (In chronological order): 
* 1 - Travel to the container-loading seaports
* 2 - Travel into the wharf areas within the container-loading seaports
* 3 - Line up with other barges, waiting for their turns to dock at the wharves and load the containers onto the barges
* 4 - Complete the container loading task, exit the wharf areas and the container-loading seaports
* 6 - Travel to the container-unloading seaports, unload the containers at the wharves within the container-unloading seaports
* 7 - Complete the Shipments
* To help the dispatcher manage the tasks of the barge captains in the most efficient way possible, we provide the **Actions** feature in Abivin vRoute system. This feature allows the dispatchers to digitize the actual manual delivery tasks of the barge captains by shifting them onto the Mobile app, provide a solution to manage the works of the barge captains on the Web app in real-time, getting rid of the tedious manual paperwork. Each of the delivery tasks mentioned above will be represented by a resource called the **Action Code**

## Locate Action Code List

* The Action Codes are listed on the **Tasks > Actions** tab

<Image title="1K5DH3aSs6s.png" alt={1920} className="border" border={true} src="https://files.readme.io/10724f4-1K5DH3aSs6s.png" />

## Create Action Codes

### Delete Pre-generated Action Codes

* When you navigate to the **Tasks > Actions** tab, you will see that there are some pre-generated Action Codes. These are the Action Codes of the VRP/DC Model that the system automatically creates after the Manufacturer is created. You will have to delete them first, then create the proper Action Code set of this model
* To delete the pre-generated Action Codes, follow the steps below
* Click on the checkbox icon :fa-square-o: on the title bar of the Action Code list to select all the Action Codes
* Click on the red **Delete All** button above the top right corner of the Action Code list

<Image title="1K5DH3aSs6.png" alt={1920} className="border" border={true} src="https://files.readme.io/a43dc80-1K5DH3aSs6.png" />

* A confirmation form will appear. Click **Ok** to confirm deleting the Action Codes

<Image title="H43efcxcgQ.png" alt={441} className="border" border={true} src="https://files.readme.io/af1e50b-H43efcxcgQ.png" />

* Now you can proceed to create the Action Codes of this model. Note that you will need to use the Excel import file to create the Action Codes. Do not use the Webform
* Here are the input rules for each information field in the Excel file
* For the **Action Code** cells, you must copy and paste the values from the **Action Code** column in the table below. Note that you must remove the quotation marks from the Action Code values
* For the **Organization Code** cells, you must input the Organization Code of the top organization, the **Manufacturer**. The Organization Code of the Manufacturer can be found under the **Organization Code** column in the **Organizations > Organizations** tab
* For the **Action Name** cells, you can use the suggested values in the table below or input your desired names
* Below is the list of all Action Codes of this model

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action Code
      </th>

      <th>
        Action Name
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "IN\_PORT"
        (Required)
      </td>

      <td>
        In Port
      </td>

      <td>
        The barge enters a seaport\
        (Applied to both the container-loading and container-unloading seaports)
      </td>
    </tr>

    <tr>
      <td>
        "IN\_WHARVES"\
        (Required)
      </td>

      <td>
        In Wharves
      </td>

      <td>
        The barge enters the wharf area within a seaport\
        (Applied to both the container-loading and container-unloading seaports)
      </td>
    </tr>

    <tr>
      <td>
        "LINED\_UP\_STARTED"\
        (Required)
      </td>

      <td>
        Line Up Started
      </td>

      <td>
        The barge starts loading containers at the docked wharf in the container-loading seaport
      </td>
    </tr>

    <tr>
      <td>
        "LINED\_UP\_COMPLETED"\
        (Required)
      </td>

      <td>
        Line Up Completed
      </td>

      <td>
        The barge completes loading containers at the docked wharf in the container-loading seaport
      </td>
    </tr>

    <tr>
      <td>
        "OUT\_WHARVES"\
        (Required)
      </td>

      <td>
        Out Wharves
      </td>

      <td>
        The barge exits the wharf area\
        (Applied to both the container-loading and container-unloading seaports)
      </td>
    </tr>

    <tr>
      <td>
        "OUT\_PORT"\
        (Required)
      </td>

      <td>
        Out Port
      </td>

      <td>
        The barge exits the seaport\
        (Applied to both the container-loading and container-unloading seaports)
      </td>
    </tr>

    <tr>
      <td>
        "UNLOAD\_STARTED"\
        (Required)
      </td>

      <td>
        Unload Started
      </td>

      <td>
        The barge starts unloading containers at the docked wharf in the container-unloading seaport
      </td>
    </tr>

    <tr>
      <td>
        "UNLOAD\_COMPLETED"\
        (Required)
      </td>

      <td>
        Unload Completed
      </td>

      <td>
        The barge completes unloading containers at the docked wharf in the container-unloading seaport
      </td>
    </tr>

    <tr>
      <td>
        "SHIPPING\_STARTED"\
        (Required)
      </td>

      <td>
        Shipping Started
      </td>

      <td>
        The barge starts the Shipment
      </td>
    </tr>

    <tr>
      <td>
        "SHIPPING\_COMPLETED"\
        (Required)
      </td>

      <td>
        Shipping Completed
      </td>

      <td>
        The barge completes the Shipment
      </td>
    </tr>

    <tr>
      <td>
        "OTHER\_TASK"\
        (Optional)
      </td>

      <td>
        Other tasks
      </td>

      <td>
        The barge captain records the events not related to the Shipment being operated
      </td>
    </tr>
  </tbody>
</Table>

* Here is how the Excel import file should look like

<Image title="LWPHjxOZ4t.png" alt={426} border={true} src="https://files.readme.io/3218f57-LWPHjxOZ4t.png">
  Illustration (English)
</Image>

<Image title="R4HJ1CXlPc.png" alt={417} border={true} src="https://files.readme.io/1c153c4-R4HJ1CXlPc.png">
  Illustration (Vietnamese)
</Image>

## Create Forms For Action Codes

* The Action Codes recently created have not yet had any information inside. Imagine them as blank Excel spreadsheets. In order for the Mobile app users to see and perform their tasks on the Mobile app, you have to build the display/input fields for each Action Code using the **Form Building** function

### Enable Form Building Function

* First, you need to enable the form building function. Please refer to the [**Manage Actions**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-actions#enable-form-building-function) article of the VRP/DC model for the general instruction

### General Steps To Build Forms For Action Codes

* After you have enabled the form building function, you can proceed to build the forms for each Action Code. Please refer to the [**Manage Actions**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-actions#general-steps-to-build-forms-for-action-codes) article of the VRP/DC model for the general instruction
* Now we will move on to create forms for each Action Code

### All Action codes

#### 1.1 Check In Panel

* Component used: **Special Components > File**

<Image title="850f9e1-f4b6793-2019-10-24_17_16_52-Window.png" alt={1631} className="border" border={true} src="https://files.readme.io/598bd24-850f9e1-f4b6793-2019-10-24_17_16_52-Window.png" />

* Component content:
* Note: The value input into **Label** field can be changed freely

<Image title="70d7f73-96548a2-eca9da0-2019-10-25_17_33_02-Window.png" alt={611} className="border" border={true} src="https://files.readme.io/1f4fded-70d7f73-96548a2-eca9da0-2019-10-25_17_33_02-Window.png" />

<Image title="4f6de56-68a5998-7c59bdd-2019-10-24_15_33_26-Window.png" alt={522} className="border" border={true} src="https://files.readme.io/c81bdf7-4f6de56-68a5998-7c59bdd-2019-10-24_15_33_26-Window.png" />
