---
title: Shipment Operation
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
> 📘 This article is being edited

## Shipment definition

* In Freight transport - Sea barge model, there are two shipment types:
* **Dummy shipment**: Is the pre-planned shipment. This kind of shipment will have correct information about **Pick Stops** - locations where the barge picks up containers
* **Actual shipment**: Is the shipment that follows a completed Dummy shipment. An Actual shipment will hold information about **Drop Stops** - locations where the barge drops off containers, and will inherit all information from its predecessor Dummy shipment, once the two shipments [have been linked](https://docs.abivin.com/docs/freight-transport-barge-manage-shipments#section-link-shipment) 

## Update shipment note

* To update a shipment's note, the dispatcher needs to click on that shipment code
* On the **Shipment Details** screen, edit the note in the **Shipment Note** field
* Click **Update** to confirm

<Image title="shipment note.gif" alt={1912} className="border" border={true} src="https://files.readme.io/785e525-shipment_note.gif" />

## Link and unlink completed Dummy shipment and Actual shipment

### Link shipments

* After the barge has completed a Dummy shipment, an Actual shipment will be created on the External Transporation System to link with that Dummy shipment, thus update the Drop Stops for the barge captain
* The Actual shipment will have an identification information. Upon reading this identification information, the dispatcher will know what completed Dummy shipment can be linked with that Actual shipment
* To link the Dummy shipment with the corresponding Actual shipment, the dispatcher needs to follow these steps:
* Click on the *Shipment code* of the Actual shipment
* On the **Shipment Details** screen, click on **Dummy shipment** field, then select the correct Dummy shipment from the drop down menu
* Click **Update** to confirm linking the two shipments

<Image title="Link shipment.gif" alt={1908} className="border" border={true} src="https://files.readme.io/a39be19-Link_shipment.gif" />

* The system will perform verification between the Pick Stops of two shipments. Below is the information of the Pick Stops that will be verified:
* 1 - Stop No
* 2 - Location Id
* 3 - Stop Type
* If the Pick Stops information are not the same between the two shipments, the system will show a warning message and doesn't allow linking those shipments

<Image title="can' link.gif" alt={1908} className="border" border={true} src="https://files.readme.io/9389b9f-can_link.gif" />

* After the two shipments have been linked, all information of the completed Dummy shipment, except information of the Drop Stops, will be transferred to the Actual shipment
* By now, the barge captain will have been notified about the Actual shipment. By viewing the Actual shipment on his device, he will be updated with locations of the Drop Stops, and can continue to operate the Actual shipment
* The below table shows the status of Dummy and Actual shipment, before and after linking

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Shipment Type
      </th>

      <th>
        Status before linking
      </th>

      <th>
        Status after linking
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Dummy Shipment
      </td>

      <td>
        Shipping Completed
      </td>

      <td>
        None (It will be hidden from the shipment list)
      </td>
    </tr>

    <tr>
      <td>
        Actual Shipment
      </td>

      <td>
        Not Assigned
      </td>

      <td>
        Plan Received
      </td>
    </tr>
  </tbody>
</Table>

## Un-link shipment

* The dispatcher can un-link an Actual shipment from a completed Dummy shipment at anytime, by following the steps below:
* Click on the shipment code
* On the **Shipment Details** screen, click on **Reset** button

<Image title="unlink.gif" alt={1908} className="border" border={true} src="https://files.readme.io/762bae9-unlink.gif" />

* After being unlinked, the Dummy shipment will reappear on the Shipment list

## Delete shipment

* The dispatcher can delete a Dummy shipment or an un-linked Actual shipment by clicking on **Delete** :fa-times: icon of that shipment
* A message will pop out. Confirm the deletion by inputting the reason on the **Deleting Reason** field, then click **OK**

<Image title="delete shipment.gif" alt={1912} className="border" border={true} src="https://files.readme.io/d972f7f-delete_shipment.gif" />

## Warnings of late shipments

* Late shipments are shipments that have yet to be performed, even though they have passed the planned Start time. They will be highlighted with a red background to catch the dispatcher's attention

## View container list of shipment

* The container quantity being transported in each shipment is shown under the **Total Containers** column
* The dispatchers can view the containers being transported in each shipment by clicking on that quantity number
* The **Shipment Containers Details** screen will appear, outlining in details the container list

<Image title="container list.gif" alt={1672} className="border" border={true} src="https://files.readme.io/fc1d10d-container_list.gif" />

* This container list is divided into three sections:

## Section 1: The aggregated container quantity being transported

* This section specify the quantity of **Full containers** - containers that have goods inside; and **Empty containers** - containers that don't carry any goods inside

<Image title="2019-09-13 14_29_13-Window.png" alt={406} className="border" border={true} src="https://files.readme.io/a86e79c-2019-09-13_14_29_13-Window.png" />

* Full containers: Symbolized by **F** letter (Short for **Full**). The full containers combine the quantity of both non-empty Dry Containers and Refrigerated Containers. Since the Refrigerated Containers require extra care than Dry Containers, they will be listed inside parentheses, and is symbolized by **RF** letter (Short for **Reefer**), so that the dispatchers can take notice
* Empty containers: Symbolized by **E** letter (Short for **Empty**). The empty containers combine the quantity of both empty Dry Containers and Refrigerated Containers, similar to Full containers above. The empty Refrigerated containers don't carry any goods therefore it's not needed to specify the quantity of them
* Dry Containers have 3 dimensions: 20 feet, 40 feet and 45 feet. Refrigerated Containers only have 2 dimensions: 20 feet and 40 feet. The corresponding quantity of each dimension is separated by a forward slash / character, and are listed in this order: *20 feet/40 feet/45 feet*
* Take this container list for example: *15/20/25 F (5/10 RF) & 30/35/40 E*. The specific quantity of full containers by each dimension can be broken down in the table below:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Full container
      </th>

      <th>
        Quantity
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        20 feet Refrigerated Containers
      </td>

      <td>
        5
      </td>
    </tr>

    <tr>
      <td>
        20 feet Dry Containers
      </td>

      <td>
        15 - 5 = 10
      </td>
    </tr>

    <tr>
      <td>
        40 feet Refrigerated Containers
      </td>

      <td>
        10
      </td>
    </tr>

    <tr>
      <td>
        40 feet Dry Containers
      </td>

      <td>
        20 - 10 = 10
      </td>
    </tr>

    <tr>
      <td>
        45 feet Dry Containers
      </td>

      <td>
        25
      </td>
    </tr>
  </tbody>
</Table>

## Section 2: The quantity of containers to be picked up/dropped off at each Stop in the shipment route

* This section will provide more details about the containers. Besides showing the quantity of Dry Containers and Refrigerated Containers of each dimensions, this section will also specify whether any of the containers are IMO containers (containers that carry dangerous cargoes), and over-sized containers (containers that carry heavy and bulky, and/or over-width, over-height cargoes)

<Image title="2019-09-13 14_29_49-Window.png" alt={1305} className="border" border={true} src="https://files.readme.io/37862df-2019-09-13_14_29_49-Window.png" />

## Section 3: Specific information of each container

* This section will only appear for Actual shipments

<Image title="2019-09-13 14_27_54-Window.png" alt={1315} className="border" border={true} src="https://files.readme.io/50a9170-2019-09-13_14_27_54-Window.png" />

* Below are the information fields of each container:

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
        Order Release Code
      </td>

      <td>
        A special code related to the orders managed on the external general control system (If available)
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Seal Number
      </td>

      <td>
        Numbers printed on the container seal lock
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Container Number
      </td>

      <td>
        Numbers printed on the container doors
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Full
      </td>

      <td>
        Show a F letter if the container carries goods\
        Show a E letter if the container is empty
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Transport Handing Unit
      </td>

      <td>
        Type of the container
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Bill/Book
      </td>

      <td>
        Bill of lading or Booking number of the container
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Customer
      </td>

      <td>
        Organization code of the customer who will ultimately receive the containers
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Shipping Line
      </td>

      <td>
        Organization code of the shipping company in charge of transporting the containers to the Pick Location (If the shipment is of Export type), or transporting from the Drop Location (If the shipment is of Import type)
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Pick Location
      </td>

      <td>
        Organization code of the location where the containers will be picked up to the barge
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Drop Location
      </td>

      <td>
        Organization code of the location where the containers will be dropped off from the barge
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Vessel Code
      </td>

      <td>
        Code of the transport vessel
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Vessel Voyage
      </td>

      <td>
        Code of the transport voyage
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        VGM
      </td>

      <td>
        Stands for Verified Gross Mass, the Gross Weight of the container that has been verified prior to loading to a vessel
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Gross Weight
      </td>

      <td>
        Gross Weight of the container
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Tare Weight
      </td>

      <td>
        Tare Weight of the container
      </td>
    </tr>
  </tbody>
</Table>

## Refresh, search and filter shipment

## Refresh shipment status

* The dispatcher can refresh the whole shipment list to get new shipments from the general control system, as well as update the most recent status of every shipments, by clicking on :fa-refresh: **Refresh** icon on the toolbar

<Image title="refresh shipment list.gif" alt={1912} className="border" border={true} src="https://files.readme.io/8b5642e-refresh_shipment_list.gif" />

## Search shipment

* The dispatcher can search for an Actual shipment using the *ID* (Shipment code) of the linked Dummy shipment. Click on the **Dummy Shipment ID** column, then type a part or the whole Shipment code of the linked Dummy shipment into the search field
* The system will immediately filter and return the Actual shipment of which the linked Dummy shipment has that Shipment code

<Image title="search shipment.gif" alt={1908} className="border" border={true} src="https://files.readme.io/b4164fd-search_shipment.gif" />

## Filter shipment

* The dispatcher can filter shipments by their *Shipment Type*, *Assigned Barge*, and *Status*, by clicking on the **Shipment Type**, **Barge** and **Status** column correspondingly, then select from the drop down menu

<Image title="filter shipment.gif" alt={1908} className="border" border={true} src="https://files.readme.io/b3da439-filter_shipment.gif" />

## Manage requests to change Estimated Arrival Date

* During the shipment operation, the barge captain can send requests to the dispatchers on Web app, asking to change Estimated Arrival Time of a specific stop
* Upon receiving the request, the dispatchers can decide to either approve or decline the request by following the below steps:
* Click on the shipment code
* On the **Shipment details** screen, the new Estimated Arrival Date requested by the captain will display under **Estimated Arrival Date New** column. On the **Barge Request Approval** column, the dispatcher can click on **Approve** button to either give approval, or **Decline** button to reject the captain request

<Image title="accept eta time change.gif" alt={1908} className="border" border={true} src="https://files.readme.io/077f5a3-accept_eta_time_change.gif" />

## Manage Non-freight related routes

* In a perfect scenario, the last location of an Actual shipment, where the barge finishes unloading containers, is also the first location of the next assigned Dummy shipment. The barge will not have to travel to another location to start the next Dummy shipment. But more often than not, the barge will have to travel some routes in order to get to the first stop of the next assigned Dummy shipment
* This kind of route is defined as **Non-freight related route**, a special kind of route to track the movement of the barge from the last stop of a completed Actual shipment to the first stop of the next assigned Dummy shipment
* The dispatcher can create a NFR request for a barge, then send that request to the general control system
* To create the NFR request, the dispatcher needs to follow these steps:
* Navigate to **Transportation > Vehicle List** tab
* Click on **Update Vehicle Location** :fa-map-marker: icon of the barge that needs to perform NFR routes
* The **Update Location** screen will appear
* Click on the **Location** field. Type the location code of the location in the search field, then select from the drop down menu (**Note**: The location code can be viewed in the **Partners > Customer List** tab, under **Customer Code** column)
* Click on **Update**. The NFR request will be created and sent to the general control system

<Image title="Create NFR sea barge.gif" alt={1668} className="border" border={true} src="https://files.readme.io/31bd390-Create_NFR_sea_barge.gif" />

* The general control system will manage all NFR requests. If the NFR request is approved on the general control system, a NFR route will be created automatically on Abivin vRoute web app. On Mobile app, that route will display as a separate shipment, placed after the ongoing Actual shipment
* The dispatcher can assign as many NFR routes to a barge as needed. The approved NFR routes will appear chronologically on Mobile app, with the earliest approved NFR route appear right below the ongoing Actual shipment, then followed by later approved NFR routes
* The shipment code of the NFR route will be the Actual shipment code adding a **NFR \_0x** prefix, with x being the numerical order of the NFR. For example, an Actual shipment with the shipment code *Actual\_01* will have the first NFR route's shipment code as *NFR\_01\_Actual\_01*, the second NFR route's shipment code as *NFR\_02\_Actual\_01*, and so on

<Image title="2019-08-18 22_56_15-TechSmith Camtasia 2019.png" alt={1916} className="border" border={true} src="https://files.readme.io/b53709f-2019-08-18_22_56_15-TechSmith_Camtasia_2019.png" />

> ❗️ If the barge has already been assigned another Dummy shipment, the dispatcher will not be able to create NFR request. The pre-assigned Dummy shipment has to be deleted before the dispatcher can create a NFR request

## Send notifications to users

* Navigate to **Settings > Notifications** tab
* The dispatchers can send to single users or groups of users a general announcement, or an urgent warning
* To select single users, the dispatcher can click on **Users** field, then select the user code from the drop down menu. He can also type the *username* into this field to search faster
* The dispatcher can select multiple users by repeating the step above

<Image title="noti.gif" alt={1912} className="border" border={true} src="https://files.readme.io/8ef917b-noti.gif" />

* The dispatcher can remove some selected users simply by clicking on their corresponding usernames

<Image title="2019-08-12 11_23_41-Window.png" alt={1658} className="border" border={true} src="https://files.readme.io/b4a8ef6-2019-08-12_11_23_41-Window.png" />

* To select a group of user, the dispatcher nees to click on **Groups** field then select from the drop down menu. He can search similar to when searching user
* After the dispatcher has finished choosing users and/or group of user, he needs to enter the notification intended to send in the field below. The notification length can be up to 300 characters
* Finally, to send the notification, the dispatcher needs to click **Send** button
* Chosen users will receive the message on their mobile app

<Image title="2019-08-12 11_23_41-Window2.png" alt={1658} className="border" border={true} src="https://files.readme.io/adb7d72-2019-08-12_11_23_41-Window2.png" />
