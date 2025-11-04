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
On the **Shipments** tab, the driver can see the current status of his shipment, with the following information:

* The organization which manages the truck tractor
* Driver Name
* Truck tractor license plate number
* Trailer license plate number
* Name of the shipment
* Status of the shipment (Assigned shipment, shipment being approved, shipment being operated)
* The information of the first and last destination of the shipment, including: Names of the destinations, Planned departure date, Planned arrival date
* Bill of Lading (BOL) number
* Gross weight
* The shipment progress bar

<Image title="Screenshot_20190723-104535_Abivin vRoute v30.jpg" alt={1080} className="border" border={true} src="https://files.readme.io/d12a4b7-Screenshot_20190723-104535_Abivin_vRoute_v30.jpg" />

## Perform shipment tasks

* By tapping on the shipment, the driver can view in details the shipment information, including all the events (or tasks) that he needs to perform at each stop point of the shipment route, in order to complete the shipment

<Image title="Screenshot_20190723-105050_Abivin vRoute v30.jpg" alt={1080} className="border" border={true} src="https://files.readme.io/ca314e1-Screenshot_20190723-105050_Abivin_vRoute_v30.jpg" />

* The list of events that can happen during a shipment is in the below table: 

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Event (Task) Code
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "SHIPPING STARTED"
      </td>

      <td>
        The shipment is started. This is the first task of every shipment
      </td>
    </tr>

    <tr>
      <td>
        "SHIPPING COMPLETED"
      </td>

      <td>
        The shipment is finished. This is the last task of every shipment
      </td>
    </tr>

    <tr>
      <td>
        "GATE IN"
      </td>

      <td>
        The truck tractor comes into the stop point
      </td>
    </tr>

    <tr>
      <td>
        "GATE OUT"
      </td>

      <td>
        The truck tractor comes out of the stop point
      </td>
    </tr>

    <tr>
      <td>
        "TRAILER ATTACH"
      </td>

      <td>
        The trailer is attached (or hooked) to the truck tractor
      </td>
    </tr>

    <tr>
      <td>
        "TRAILER DETACH"
      </td>

      <td>
        The trailer is detached (or unhooked) from the truck tractor
      </td>
    </tr>

    <tr>
      <td>
        "LIFT ON (1)"
      </td>

      <td>
        An empty container is lifted on the trailer
      </td>
    </tr>

    <tr>
      <td>
        "LIFT ON (0)"
      </td>

      <td>
        A non-empty container is lifted on the trailer
      </td>
    </tr>

    <tr>
      <td>
        "LIFT OFF"
      </td>

      <td>
        A container is lifted off the trailer
      </td>
    </tr>

    <tr>
      <td>
        "STUFFING START"
      </td>

      <td>
        Start loading goods into the container
      </td>
    </tr>

    <tr>
      <td>
        "STUFFING FINISH"
      </td>

      <td>
        Finish loading goods into the container
      </td>
    </tr>

    <tr>
      <td>
        "DESTUFFING START"
      </td>

      <td>
        Start unloading goods off the container
      </td>
    </tr>

    <tr>
      <td>
        "DESTUFFING FINISH"
      </td>

      <td>
        Finish unloading goods off the container
      </td>
    </tr>
  </tbody>
</Table>

* In order to complete a shipment, the driver needs to complete every tasks assigned in that shipment, in chronological order
* Upon completing each task, the driver needs to take photos of the task as a form of proof, then tap on **Submit** to submit the photos to Abivin vRoute server. For each task, the driver could submit up to 5 photos
* As long as the driver hasn't submitted the **SHIPPING COMPLETED** task, he can re-submit photos of other tasks as many times as he needs to
* For the **LIFT ON (1)** events, in which the driver picks up empty containers onto the trailer, besides taking pictures of the containers, the driver needs to input the container information
* Below are the container information fields:

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
        Container Number
        (Required)
      </td>

      <td>
        **1. Description:**\
        The numbers printed on the container doors\
        **2. Input rules:**\
        Must be 11 characters long (First 4 characters are letters, last 7 characters are numbers) and complies with [**ISO standard**](https://en.wikipedia.org/wiki/ISO_6346)
      </td>
    </tr>

    <tr>
      <td>
        Seal Number\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The numbers printed on the container seal lock of the container\
        **2. Input rules:**\
        Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        Max Gross Weight\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Max capacity of the container, including its own tare weight\
        **2. Input rules:**\
        Must be 5 characters long, all are numbers. Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        Tare Weight\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Weight of the empty container, not containing any products\
        **2. Input rules:**\
        Must be 4 characters long, all are numbers. Must not contain spaces
      </td>
    </tr>
  </tbody>
</Table>

* If the drivers incorrectly input any of the above information, he will not be able to submit the **LIFT ON (1)** events
* If the ***Container Number*** is input correctly length wise, but fails to comply with ISO standard, there will be a pop-up to warn the driver, showing exactly which container was inputted incorrectly. The driver can choose to check the container number again, or continue to submit the event

<Image title="Mobile - Send lift on 1.gif" alt={270} className="border" border={true} src="https://files.readme.io/e098153-Mobile_-_Send_lift_on_1.gif" />

* Once the task is successfully submitted, the mobile screen will automatically redirect back to the task list screen so that the driver can follow up the next tasks
* The time icon next to the completed tasks will turn green, while the incomplete tasks still appear white

<Image title="2019-08-01 15_18_58-Window.png" alt={149} className="border" border={true} src="https://files.readme.io/8d904fd-2019-08-01_15_18_58-Window.png" />

* When the shipment has been completed, with all the tasks turn green, the shipment will be moved to **History** tab

## View planned and actual delivery routes

During the delivery trip, the driver can view the optimized route and check against the actual route he's been travelling.

## View planned route

* On the task list screen, tap on **Map** icon on the top right of the screen. The driver will be directed to the map view screen
* The driver can use two fingers to zoom in the map (Swipe the two fingers closer to each other) or zoom out the map (Swipe the two fingers further from each other) 

<Image title="view map.gif" alt={544} className="border" border={true} src="https://files.readme.io/1a1871e-view_map.gif" />

* Tap on **Plan** tab. On the screen, there will be the original planned route of the shipments, with all the stops the driver has to visit

<Image title="2019-07-08 21_43_30-Window.png" alt={449} className="border" border={true} src="https://files.readme.io/bc9063f-2019-07-08_21_43_30-Window.png" />

## View actual route

* Tap on **Actual** tab. The map will display the route that the driver has actually been travelling.
* To play back the actual delivery route, the driver can tap on :fa-eye: icon on the bottom left corner of the screen. The actual delivery route will be played back

<Image title="view map.gif" alt={608} className="border" border={true} src="https://files.readme.io/0831e84-view_map.gif" />

## Request Non-freight related stop (NFR)

* After completing the shipment, the truck tractor driver might need to travel from the end location of the recently completed shipment to:
* The start location of the next shipment, or
* A location not related to the next shipment
* He can do so by actively requesting a Non-freight related stop (NFR), a stop point not tied to any specific shipment
* To do that, the driver needs to tap on **History** tab, then tap on the recently completed shipment
* On the task list screen, tap on :fa-plus-circle: icon, then tap on the icon that reads **Add NFR**
* On the **Add NFR** screen, tap on **Location** field, then choose the desired location on the **Location list**, or search for the location in the **Search** field, then click **Save**. The NFR request will be submitted to the dispatcher, waiting for approval

<Image title="Mobile - Send NFR.gif" alt={608} className="border" border={true} src="https://files.readme.io/5d02711-Mobile_-_Send_NFR.gif" />

* The driver can simply swipe the Mobile app screen to refresh and update the approval status of the NFR
* If the NFR request has been approved, the shipment will be moved back to the **Shipments** tab. The task list of the recently completed shipment will be updated. There will be additional tasks the driver need to perform, in order to get to the desired location, such as: GATE OUT (from the current port), GATE IN (to the desired port) etc. Only when completing these additional tasks, the shipment is finally deemed completed

<Image title="Mobile - NFR Approved.gif" alt={608} className="border" border={true} src="https://files.readme.io/5a4b8c7-Mobile_-_NFR_Approved.gif" />

> 🚧 If there has been a NFR request sent from the mobile associated with the truck tractor earlier, which is still waiting for the dispatcher decision, the driver will not be able to submit another NFR from that mobile

## Submit shipment charge requests to dispatchers

## Submit charge requests

* On the task list screen, tap on the yellow :fa-plus-circle: button. 
* Two other buttons will reveal. Tap on the **New charge fee** :fa-pencil: button, the driver will then be able to submit the fee he has just been charged.
* The driver could choose the type of fee (**Fee type**) from the drop down menu, the amount of that fee (**Fee price**), a short description of that fee (**Note**). The driver could also take pictures of the fee bill.
* If the driver doesn't want to submit charge request, he can tap on the :fa-times-circle: icon.
* The charge request will then be submitted to server, waiting for the dispatcher's approval.

<Image title="Mobile - Send charge.gif" alt={270} className="border" border={true} src="https://files.readme.io/9885204-Mobile_-_Send_charge.gif" />

## View list of submitted charge requests

* By tapping on the :fa-history: icon on the top right of the task list screen (Next to the **Map** icon), the driver can see a list of charge requests associated with the shipment he's currently operating, along with the status of the request (pending or has been approved).
* To update that status of pending charge requests, the driver can simply swipe the mobile screen down to refresh the list. When the status of the pending charge requests changes from **Waiting** to **Approved**, that means the request has been approved by the dispatcher on Web app

<Image title="Mobile - Charge approved.gif" alt={608} className="border" border={true} src="https://files.readme.io/fd40f44-Mobile_-_Charge_approved.gif" />

## View container note

* Each container of a shipment might container a short note. To view a container's note, you have to navigate to the Shipment detail screen. Next, tap on **Container** tab, then tap on the note of a container under **Note** column

<Image title="52df85a-Image_7.png" alt={1760} className="border" border={true} src="https://files.readme.io/2ef7fec-52df85a-Image_7.png" />

## Send And Receive Shipment Notes

* During the Shipment performing process, you can send as well as receive shipment related notes on the Mobile app
* First, tap on the **Shipments** tab
* Notice the Shipment note section at the bottom of the Shipment. This section will display the latest note sent by the dispatcher from the Web app

<Image title="APT3TcCSM7.png" alt={860} className="border" border={true} src="https://files.readme.io/6fbd26f-APT3TcCSM7.png" />

* To view the full note history, tap on that section. The Mobile app will redirect to the **Shipment Note** screen
* To send a new note, tap on the **Note from Driver** section then input the note. You can input a maximum of ***500 characters*** (letters; numbers; special characters including spaces) per note.
* After that, tap on the **Send** icon :fa-send: to send the note to the dispatcher

<Image title="1FFCR5u3Ty.png" alt={429} className="border" border={true} src="https://files.readme.io/7713e3a-1FFCR5u3Ty.png" />

* There are some notes: 
* 1 - Once a note is created and sent, you can not edit it
* 2 - For each Shipment, you can send and receive a maximum of ***50 notes***
* To go back to the Shipment tab, tap on the **Back** icon :fa-mail-reply:

<Image title="1FFCR5u3Tsy.png" alt={429} className="border" border={true} src="https://files.readme.io/ae90a6b-1FFCR5u3Tsy.png" />
