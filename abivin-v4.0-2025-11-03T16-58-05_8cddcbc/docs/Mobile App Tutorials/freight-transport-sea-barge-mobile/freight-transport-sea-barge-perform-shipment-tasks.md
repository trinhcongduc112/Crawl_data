---
title: Perform shipment tasks
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
## Perform shipment tasks

* On **Shipments** tab, tap on **Detail >** button of the first shipment being assigned. The app screen will redirect to the **Shipment detail** screen

<Image title="go to shipment.gif" alt={1764} className="border" border={true} src="https://files.readme.io/156b674-go_to_shipment.gif" />

* On the sub tab **Stop list** will show up the list of tasks that the barge captain need to be submit at each stop on the shipment route
* Below is the list and description of all tasks

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Task
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Shipping Started
      </td>

      <td>
        The shipment is started\
        Action to perform: Take photos (Can be configured to perform more actions)
      </td>
    </tr>

    <tr>
      <td>
        Shipping Completed
      </td>

      <td>
        The shipment is completed\
        Action to perform: Take photos (Can be configured to perform more actions)
      </td>
    </tr>

    <tr>
      <td>
        Arrived at Terminal
      </td>

      <td>
        The barge has come into the seaport area\
        Action to perform: Take photos (Can be configured to perform more actions)
      </td>
    </tr>

    <tr>
      <td>
        Departed at Terminal
      </td>

      <td>
        The barge has come out of the seaport area\
        Action to perform: Take photos (Can be configured to perform more actions)
      </td>
    </tr>

    <tr>
      <td>
        Berthing
      </td>

      <td>
        The barge has come into of the seaport's loading wharf area\
        Action to perform: Take photos (Can be configured to perform more actions)
      </td>
    </tr>

    <tr>
      <td>
        Unberthing
      </td>

      <td>
        The barge has come out of of the seaport's loading wharf area\
        Action to perform: Take photos (Can be configured to perform more actions)
      </td>
    </tr>

    <tr>
      <td>
        Loading Started
      </td>

      <td>
        Containers are started loading onto the barge\
        Action to perform: Take photos (Can be configured to perform more actions)
      </td>
    </tr>

    <tr>
      <td>
        Loading Finished
      </td>

      <td>
        Containers are finished loading onto the barge\
        Action to perform: Take photos (Can be configured to perform more actions)
      </td>
    </tr>

    <tr>
      <td>
        Unloading Started
      </td>

      <td>
        Containers are started unloading off the barge\
        Action to perform: Take photos (Can be configured to perform more actions)
      </td>
    </tr>

    <tr>
      <td>
        Unloading Finished
      </td>

      <td>
        Containers are finished unloading off the barge\
        Action to perform: Take photos (Can be configured to perform more actions)
      </td>
    </tr>
  </tbody>
</Table>

* To perform a certain task, the captain needs to tap on the title of that task
* The detail of that task will show up. The captain needs to perform every action required of that task, then tap on **Submit** to send the result of the task to the dispatcher on Web app

<Image title="Submit task.gif" alt={1705} className="border" border={true} src="https://files.readme.io/51dde40-Submit_task.gif" />

* Tasks that have not been performed will appear white. After being performed, the color will change to green

<Image title="2019-08-01 15_18_58-Window.png" alt={149} className="border" border={true} src="https://files.readme.io/3df8d61-2019-08-01_15_18_58-Window.png" />

* After the Dummy shipment has been completed, it will be moved to **History** tab. The captain can wait for a few moments while the dispatcher links the recently completed Dummy shipment to an Actual shipment
* After an Actual shipment has been linked, it will inherit all statuses of the linked completed Dummy shipment, as well as update the Drop Stops. The Actual shipment will then appear on **Shipment** tab
* The captain can now continue to perform the Actual shipment

## Perform Non-freight related routes

* Between an Actual shipment and the next assigned Dummy shipment, the captain might need to perform some [Non-freight related routes (NFR)](https://docs.abivin.com/docs/freight-transport-barge-manage-shipments#section-non-freight-related-route)
* The shipment code of the NFR route will be the Actual shipment code adding a **NFR \_0x** prefix, with x being the numerical order of the NFR. For example, an Actual shipment with the shipment code *Actual\_01* will have the first NFR route's shipment code as *NFR\_01\_Actual\_01*, the second NFR route's shipment code as *NFR\_02\_Actual\_01*, and so on
* The barge captain must perform these NFR routes sequentially, starting from the NFR route with shipment code *NFR\_01*

<Image title="NFR mobile.gif" alt={1764} className="border" border={true} src="https://files.readme.io/95f69c9-NFR_mobile.gif" />

## Perform other events

* While performing the shipment , the barge captain might face some issues such as damages, crashes and other problems
* To help the captain record all the issues that have arisen, as well as submit the issues to the dispatchers, on Mobile app the captain can use the **Perform other events** function
* This function can be executed following the steps below:
* Tap on the :fa-plus-circle: icon, then tap on **Create other event** :fa-pencil: icon
* The **Other events** screen will appear, showing the current date. Here the barge captain can input the content of the issue, including: **Name of the event**, **Details of the event**. The captain can also take photos as a form of proof
* After the captain has input all data necessary, he can submit the event by tapping on **Submit** button on the top right of the screen

<Image title="Submit extra task.gif" alt={1705} className="border" border={true} src="https://files.readme.io/1aec382-Submit_extra_task.gif" />

## Submit request to change Estimated Arrival Date

* Depends on actual operation, the captain can send request to change the Estimated Arrival Date for a specific Stop
* In order to be able to submit the request, the captain must not have had submitted the **In Port** task of that stop yet
* Below are the steps to submit the request:
* **Step 1**: On **Shipments** tab, tap on the **Estimated Arrival Date** field of the chosen Stop
* **Step 2**: Select the suitable Time (Date, Month, Year, Hour, Minute) on the calendar, then tap on **OK**

<Image title="change ETA mobile.gif" alt={1719} className="border" border={true} src="https://files.readme.io/8a955d5-change_ETA_mobile.gif" />

> 📘 The calendar appearance might vary between different devices and operating systems

* A message will pop out, informing the captain that the request has been sent successfully and will need to wait for the dispatcher's approval on Web app

<Image title="Screenshot_2019-07-31-09-15-23.png" alt={1024} className="border" border={true} src="https://files.readme.io/06ae3ef-Screenshot_2019-07-31-09-15-23.png" />

* After the dispatcher has made the decision, a second message will be sent to the Mobile app

<Image title="Screenshot_3.png" alt={1019} border={true} src="https://files.readme.io/225530e-Screenshot_3.png">
  Thông báo **Yêu cầu đã được chấp thuận**
</Image>

## Receive notifications from the dispatcher

* If the barge captain belongs to a list of people who will receive notifications from the dispatcher, he will receive notification when using the mobile app
* If the app is currently opened, the notification will pop out as below:

<Image title="Screenshot_8.png" alt={1021} className="border" border={true} src="https://files.readme.io/1e35323-Screenshot_8.png" />

* Or will show up at the **General notification** section of the device, if the app is not being opened

<Image title="Screenshot_6.png" alt={534} className="border" border={true} src="https://files.readme.io/4236835-Screenshot_6.png" />

* The captain can also see list of past notifications by tapping on the User icon :fa-user: on the top right of the app screen, then tap on :fa-bell: **Notification** text
* The **Notification list** will show up. Unread notifications will have a mild blue background, whereas read notifications will have a white background

<Image title="mobile noti.gif" alt={1772} className="border" border={true} src="https://files.readme.io/8c8b730-mobile_noti.gif" />

## View container note

* Each container of a shipment might container a short note. To view a container's note, you have to navigate to the Shipment detail screen. Next, tap on **Container** tab, then tap on the note of a container under **Note** column

<Image title="Image 7.png" alt={1760} className="border" border={true} src="https://files.readme.io/52df85a-Image_7.png" />
