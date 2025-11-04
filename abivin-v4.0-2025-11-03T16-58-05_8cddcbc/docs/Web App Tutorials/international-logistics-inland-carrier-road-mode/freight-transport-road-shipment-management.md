---
title: Manage shipments
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
* Navigate to **Tasks > Shipment List** tab
* This is where all the shipments, created from within Abivin vRoute or transmitted from other transportation management system, are listed
* Below are the functions you can perform with the shipments in Abivin vRoute

## Create shipment

* Please refer to the **[CRUD](https://docs.abivin.com/docs/crud#section-create)** article to get the general steps on how to create shipments

![1673](https://files.readme.io/ba07bd0-create_shipment.png "create shipment.png")

* During the creation process, you will need to input various information related to the shipment. Below are the detailed description of each information field

## Shipment Detail

* These are the general, basic information of the shipment

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Shipment Code
      </td>

      <td>
        Management code of the shipment
      </td>
    </tr>

    <tr>
      <td>
        Customer
      </td>

      <td>
        Customer of the shipment
      </td>
    </tr>

    <tr>
      <td>
        Move Perspective
      </td>

      <td>
        The direction (from the port) of the shipment: Import or Export
      </td>
    </tr>

    <tr>
      <td>
        Start Date, Due Date
      </td>

      <td>
        The dates on which the shipment is supposed to start and finish
      </td>
    </tr>

    <tr>
      <td>
        Shipment Note
      </td>

      <td>
        Short description about the shipment
      </td>
    </tr>

    <tr>
      <td>
        Billing Code
      </td>

      <td>
        Billing Code of the shipment
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        Status of the shipment when first received from the source transportation management system
      </td>
    </tr>
  </tbody>
</Table>

## Shipment Assigned

* These are the information related to the vehicle, trailer, driver which the shipment is assigned to

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Vehicle
      </td>

      <td>
        Management code of the assigned truck tractor on which the shipment is carried
      </td>
    </tr>

    <tr>
      <td>
        Trailer
      </td>

      <td>
        Management code of the assigned trailer on which the shipment is carried
      </td>
    </tr>

    <tr>
      <td>
        Driver
      </td>

      <td>
        Management code of the assigned truck tractor driver by whom the shipment is delivered
      </td>
    </tr>

    <tr>
      <td>
        Request Shipment by
      </td>

      <td>
        Name of the driver who requests the shipment
      </td>
    </tr>
  </tbody>
</Table>

## Add stop in shipments

* To add stop points to the shipment, click on the **Add Stop** :fa-plus-square: icon at the bottom right corner of the **Add New Shipment** screen.

<Image title="add shipment stops.png" alt={1673} className="border" border={true} src="https://files.readme.io/f5bf1aa-add_shipment_stops.png" />

* You will have to input the information of each stop point as below:

### Shipment Stops

* These are the information of the stop points on the shipment route

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Stop Name
      </td>

      <td>
        Specific name of the Stop
      </td>
    </tr>

    <tr>
      <td>
        Stop Type
      </td>

      <td>
        Type of the Stop (See below table)
      </td>
    </tr>

    <tr>
      <td>
        Tasks
      </td>

      <td>
        Tasks operated at the Stop
      </td>
    </tr>

    <tr>
      <td>
        Containers
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

### Stop Type

* These are the information of the type of each stop point

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Stop Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Origin
      </td>

      <td>
        The First stop of the shipment route
      </td>
    </tr>

    <tr>
      <td>
        Drop
      </td>

      <td>
        Stop where goods are unloaded
      </td>
    </tr>

    <tr>
      <td>
        Pick
      </td>

      <td>
        Stop where goods are picked up
      </td>
    </tr>

    <tr>
      <td>
        Pick & Delivery
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Destination
      </td>

      <td>
        The Final stop of the shipment route
      </td>
    </tr>
  </tbody>
</Table>

## Assign and un-assign shipment

## Assign shipment

* If a shipment recently transmitted from other external transportation management system doesn't have assignee information yet, the dispatcher can manually assign that shipment to a truck tractor and trailer by clicking on that shipment code. 
* On the **Shipment Details** screen, the dispatcher needs to click on the **Vehicle** and **Trailer** fields sequentially and choose the suitable truck tractor and trailer from the drop down menus. After that, the dispatcher needs to click on **Update** button to confirm the assignment. The truck tractor driver will receive the assigned shipment on the mobile app immediately

<Image title="assign shipment.gif" alt={1668} className="border" border={true} src="https://files.readme.io/30487f6-assign_shipment.gif" />

## Un-assign shipment

* In case there are changes in the delivery plan, the dispatcher can un-assign a truck tractor/trailer from delivering a specific shipment by clicking on **Reset** button on the **Shipment Details** screen, then click **OK** on the pop out message
* That shipment status will revert from **Vehicle Assigned** back to **Not Assigned**

<Image title="Freight - Unassign.gif" alt={1916} className="border" border={true} src="https://files.readme.io/25e4388-Freight_-_Unassign.gif" />

## Approve shipment request

* Option 1: The dispatcher will receive notifications of new shipment requests on the **Notifications** :fa-envelope-o: section on the top right of the Web app screen. The dispatcher can click on that notification. The **Shipment Details** screen will appear. The dispatcher can either click **Approve** to confirm assigning that shipment to the truck tractor driver who sent request; or **Decline** if he wants to assign that shipment to another driver later on

<Image title="Freight - Approve noti.gif" alt={1916} className="border" border={true} src="https://files.readme.io/9605651-Freight_-_Approve_noti.gif" />

* Option 2: The dispatcher can click on **Requesting Shipments** button on the toolbar above the shipment list. This will filter and show all the shipments being requested. The dispatcher can click on a specific shipment code to get to the **Shipment Details** screen. Here, he can perform approval or disapproval like in Option 1

<Image title="Freight - Approve list.gif" alt={1916} className="border" border={true} src="https://files.readme.io/caa9172-Freight_-_Approve_list.gif" />

* If there is more than one dispatcher, the shipment request notifications will appear on all dispatchers's accounts, so that the dispatchers can allocate the workload between themselves reasonably
* Abivin vRoute can support the dispatcher to reduce workload by automatically approving shipment requests based on certain conditions, such as: Comparing the time the driver submits shipment request (**Request time**), the time needed to pick up the container (**Pick-up time**), and the latest time the container is officially allowed to be placed at the pick up destination (**Location time**). 
* For example, the dispatcher can set a condition like this: If **Request time + Pick-up time > Location time**, then the shipment request will be automatically approved, reducing the workload for the dispatcher

## Search shipment tasks

* Navigate to **Tasks > Task List** tab
* This tab is where the tasks of all in-progress shipments are listed
* To search for the tasks of a specific shipment, the dispatcher can type the shipment code into the **Search field** :fa-search:. After a few moments, all tasks related to this shipment will appear

<Image title="Freight - shipment tasks.gif" alt={1916} className="border" border={true} src="https://files.readme.io/a5b0410-Freight_-_shipment_tasks.gif" />

* The dispatcher can see details about each task. Each task will have these essential information fields:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Task Code
      </td>

      <td>
        Management Code of the task
      </td>
    </tr>

    <tr>
      <td>
        Task Name
      </td>

      <td>
        Specific name of the task
      </td>
    </tr>

    <tr>
      <td>
        Organizations
      </td>

      <td>
        The organization who performed the task
      </td>
    </tr>

    <tr>
      <td>
        Assigned to
      </td>

      <td>
        The semi-truck who performed the task
      </td>
    </tr>

    <tr>
      <td>
        Customer
      </td>

      <td>
        Customer of the shipment
      </td>
    </tr>

    <tr>
      <td>
        Created At
      </td>

      <td>
        Creation date of the task on Abivin vRoute server
      </td>
    </tr>

    <tr>
      <td>
        Start Date
      </td>

      <td>
        Official date when the task starts
      </td>
    </tr>

    <tr>
      <td>
        Completed Date
      </td>

      <td>
        Official date when the task finishes
      </td>
    </tr>

    <tr>
      <td>
        Results
      </td>

      <td>
        Result of the task. The dispatcher can insert comments about the task here by clicking on :fa-edit: icon
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        Status of the task: Completed, Deleted, Open, Progressing, Rejected
      </td>
    </tr>

    <tr>
      <td>
        Edit
      </td>

      <td>
        Edit
      </td>
    </tr>
  </tbody>
</Table>

## Refresh shipment list

* To get the latest shipments forwarded from other transportation management system, or to update the status of the shipments, click on **Refresh** :fa-refresh: icon on the toolbar above the shipment list

<Image title="refresh shipment.gif" alt={1668} className="border" border={true} src="https://files.readme.io/1676bb8-refresh_shipment.gif" />

## Filter shipment information

* To easily manage the shipments, the dispatcher can filter some information fields, including: **Leg number, Move Perspective, Container Numbers, Start and End locations, Status, Vehicle** and **Driver**
* To do this, the dispatcher needs to click on :fa-caret-down: icon next to the above fields on the toolbar above the shipment list. On the drop down menu, the dispatcher can click on the :fa-square-o: icon next to the item he wants to filter out

<Image title="Filter shipment info.gif" alt={1668} className="border" border={true} src="https://files.readme.io/1bf321f-Filter_shipment_info.gif" />

## Delete shipment

* Please refer to the **[CRUD](https://docs.abivin.com/docs/crud#section-delete)** article to get the general steps on how to delete shipments

## View shipment location

* On the shipment list screen, use the horizontal scroll bar to scroll all the way to the end of the shipment rows. You will notice there are a **View map** icon at the end of each shipment, under the **Actions** tab. Clicking on that icon will open a map screen, on which you can see the location of the shipment
* To update the latest location of the shipment, click on **Refresh** button at the bottom of the map screen

<Image title="Freight - View map.gif" alt={1916} className="border" border={true} src="https://files.readme.io/86b304f-Freight_-_View_map.gif" />

## View shipment documents

* On the shipment list, click on the shipment code
* The **Shipment details** screen will appear, listing details of every tasks of that shipment, along with the photos that the driver has submitted

<Image title="freight - shipment photo.png" alt={1915} className="border" border={true} src="https://files.readme.io/c65e0b8-freight_-_shipment_photo.png" />
