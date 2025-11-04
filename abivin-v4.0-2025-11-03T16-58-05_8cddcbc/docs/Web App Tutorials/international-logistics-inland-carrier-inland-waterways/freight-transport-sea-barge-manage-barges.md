---
title: Manage Barges
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
* In Freight Transport - Sea Barge Model, the barges are under direct management of the ***Transporter***

## Locate barge list

* Navigate to **Transportation > Vehicle List** tab
* This tab lists all barges under the management of your organization

<Image title="2019-10-22 15_03_44-Window.png" alt={1671} className="border" border={true} src="https://files.readme.io/f03839a-2019-10-22_15_03_44-Window.png" />

## Create barges

### Barge information fields

* Below is the list of all information fields of a barge

> 📘 Apart from the information fields mentioned below, other information fields can be left blank during the creation/editing process

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
        Organization (Web form); Organization Code (Excel template)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Transporter which will manage the barge being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field, input the Organization Name/Organization Code of the management Transporter into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the Transporter which manages the barge being created on Web app, then paste into this cell\
        **Note:**\
        The Organization Name and Organization Code can be found under "Organization Name" and "Organization Code" columns in "Organizations > Organization List" tab\
        This information can not be changed once the barge has been created. Therefore, please pay extra attention
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Type\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Vehicle type of the barge being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field then choose the following value from the drop down menu: barge\
        **Excel template:**\
        Input the following value into the cell: barge
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Name\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A name assigned to the barge being created for easier management\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        License Plate\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        License Plate number of the barge being created\
        **2. Input rules:**\
        Format: Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Management code assigned to the barge being created\
        **2. Input rules:**\
        Maximum 15 characters\
        Letters and numbers are inputtable. Special characters (Not letters and numbers) will not be inputtable\
        Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        Temperature\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The product temperature levels supported by the barge being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field, tick on check boxes of all temperature levels: Frozen, Ambient, Chilled\
        **Excel template:**\
        Input the following value into the cell: ***FAC***
      </td>
    </tr>

    <tr>
      <td>
        Temp Zone\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The number of temperature zones available on the barge being created\
        **2. Input rules:**\
        Input the following value into the field/cell: ***3***
      </td>
    </tr>

    <tr>
      <td>
        Volume (Web form); Capacity Volume (m3) (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum product capacity in cubic meter (m3) that the barge being created can carry\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example, if the barge can carry maximum twelve cubic meters, input the following value into the field/cell: 12
      </td>
    </tr>

    <tr>
      <td>
        Weight (Web form); Capacity Weight (kg) (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The maximum product capacity in kilograms (kg) that the barge being created can carry\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: If the barge being created can carry maximum three thousand kilograms, input the following value into the field/cell: 3000
      </td>
    </tr>

    <tr>
      <td>
        Gross weight\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The total weight of the barge, including all the components of the barge, the weight of the captain, product, fuel, and other things\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: If the barge gross weight is three thousand kilograms, input the following value into the field/cell: 3000
      </td>
    </tr>

    <tr>
      <td>
        Real weight\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The actual weight the barge being created can carry\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: The barge is registered to have the real weight information at three thousand kilograms, input the following value into the field/cell: 3000
      </td>
    </tr>

    <tr>
      <td>
        Start time; Stop time\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **Note: Even though being required, this information field is only effective in VRP model**\
        **1. Description:**\
        The official times of day when the barge being created starts and stops working\
        **2. Input rules:**\
        Format: hh:mm (24 hour)\
        Input only the value into this field, do not input the unit\
        For example: The barge starts working at 7:30 A.M and stops working at 8:30 P.M. Input the following values into the "Start time" and "Stop time" fields/cells correspondingly: 07:30 and 20:30
      </td>
    </tr>

    <tr>
      <td>
        Lunch start time; Lunch stop time\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **Note: Even though being required, this information field is only effective in VRP model**\
        **1. Description:**\
        The official times of day when the captain of the barge being created starts and stops the lunch break\
        **2. Input rules:**\
        Format: hh:mm (24 hour)\
        Input only the value into this field, do not input the unit\
        For example: The lunch break starts at 12:30 A.M and stops at 1:30 P.M. Input the following values into the "Lunch start time" and "Lunch stop time" fields/cells correspondingly: 12:30 and 13:30
      </td>
    </tr>

    <tr>
      <td>
        Speed\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Movement speed of the barge being created\
        Unit: Kilometer per hour (km/h)\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: The barge runs at thirty kilometers per hour. Input the following value into the field/cell: 30
      </td>
    </tr>

    <tr>
      <td>
        Cost per km\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The cost for the barge being created per one kilometer during a delivery route\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: The barge costs two thousand dollars to operate per one kilometer. Input the following value into the field/cell: 2000
      </td>
    </tr>

    <tr>
      <td>
        Fixed Cost\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The fixed cost of the barge being created during a delivery route, not depending on the route length\
        **2. Input rules:**\
        Input only the value into this field, do not input the unit\
        For example: The Fixed cost of the barge is two thousand dollars. Input the following value into the field/cell: 2000
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Identification Number\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The unique identification code of the barge being created, usually printed on the driver's side of the dashboard\
        **2. Input rules:**\
        Maximum 17 characters\
        All letters and numbers are inputtable, except for the following: Special characters and spaces; letters I (i), O (o), and Q (q) (These three letters can cause confusion with the numbers 1 and 0).
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Engine Number\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The number printed on the engine of the barge being created\
        **2. Input rules:**\
        Maximum 15 characters\
        Letters and numbers are inputtable. Special characters (Not letters and numbers) and spaces will not be inputtable
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Internal Code\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A code assigned by the management organization and can be printed out and pasted onto the barge being created. This code is similar to the Vehicle code in Abivin vRoute system, but is used by the organization for external management\
        **2. Input rules:**\
        Maximum 15 characters\
        Spaces will not be inputtable\
        All letters, numbers and special characters will be inputtable. Spaces will not be inputtable
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Description\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Short description about the barge being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Default driver\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The default driver of the barge being created\
        **2. Input rules:**\
        **Web form:**\
        Click on the field, choose the default driver from the drop down menu\
        **Excel template:**\
        Copy the username of the driver on Web app, then paste into this cell\
        **Note:**\
        Username of the driver can be found under "Username" column in "Organizations > Organization List" tab
      </td>
    </tr>

    <tr>
      <td>
        Location\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The current location of the barge being created\
        **2. Input rules:**\
        If you want to change location of the barge, click on this field, input the Organization code of the location in the search bar and select from the drop down menu\
        The location codes can be found under "Customer Code" column in "Partners > Customer List" tab
      </td>
    </tr>

    <tr>
      <td>
        Device ID (IMEI)\
        (Web form)\
        (Required in order to receive Shipments on Mobile App)
      </td>

      <td>
        **1. Description:**\
        The IMEI or MAC Address of the mobile device equipped for the barge being created. This information will help the dispatcher track the current location of the barge during the delivery process\
        **2. Input rules:**\
        Refer to the following section: [**Store IMEI/MAC address of the barge's equipped mobile device**](https://docs.abivin.com/docs/freight-transport-sea-barge-manage-barges#store-imeimac-address-of-the-barges-equipped-mobile-device)
      </td>
    </tr>

    <tr>
      <td>
        Registration Date\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The date when the registration certificate of the barge being created is deemed expired\
        **2. Input rules:**\
        Click on the field, choose the suitable date from the drop down calendar
      </td>
    </tr>

    <tr>
      <td>
        Active\
        (Web form)
      </td>

      <td>
        **1. Description:**\
        The active status of the barge being created\
        **2. Input rules:**\
        By default, the status of the barge is Active, represented by this icon: :fa-check-square:\
        To turn the status into Inactive, click on that icon
      </td>
    </tr>

    <tr>
      <td>
        Draught\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The draught level (In meter - m) of the barge being created\
        **2. Input rules:**\
        Information in this field will be forwarded from the external transportation management system
      </td>
    </tr>
  </tbody>
</Table>

### Create single barge using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form
* **Note:** 
* During the creation process, the **Organization** and **Vehicle Type** fields must be input first

<Image title="2019-10-22 15_09_37-Window.png" alt={790} className="border" border={true} src="https://files.readme.io/11c78e8-2019-10-22_15_09_37-Window.png" />

### Create multiple barges using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template

## Store IMEI/MAC address of the barge's equipped mobile device

* As have been mentioned, in this model, each barge will be equipped a mobile device (A tablet to be specific). The barge captains will receive and submit shipment tasks on the equipped tablet instead of their smartphones. On Web app, the dispatcher can track the current location of the barges via the GPS information of the equipped tablets. The Web dispatcher first need to store the IMEI/MAC address of each barge's equipped tablet
* First, the Web dispatcher needs to decide whether to manage the barge's tablet by IMEI or MAC Address by doing the following:
* Navigate to the tab **Organizations > Organizations**
* Click **Edit** :fa-pencil: icon of the **Transporter**
* On the form **More Configurations**, navigate to the sub-tab **Mobile**. In the section **Shipment Device ID Type**, select between the two values **IMEI** or **MAC Address**. Click **Save** to confirm the change
* Next, navigate to the tab **Transportation > Vehicle**
* Click **Edit** :fa-pencil: icon of each barge
* On the form **Update Vehicle**, scroll down until you see the field **Device ID (IMEI or MAC Address)**. Input either the IMEI or MAC Address of the barge's equipped tablet into this field accordingly to the setting you chose earlier at the Transporter. Click **Save** to confirm the change
* Repeat the above step for the remaining barges
* **IMPORTANT NOTE** Always take the device MAC Address
* If the barges are managed by MAC Addresses, then you must store the default device MAC Addresses for the barges, as well as set the MAC Address setting of the mobile devices to **device MAC** instead of **randomized MAC**. During the input process, please note that the letters in the MAC Address must be input in uppercase
* The instruction on how to setup the mobile devices and get the MAC Address can be found in this article: [**Freight transport - Sea Barge Model - Mobile app**](https://docs.abivin.com/docs/freight-transport-sea-barge-mobile#setup-mobile-device-with-mac-address)

## Update barge information

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

<Image title="2019-10-22 22_11_14-Window.png" alt={1915} className="border" border={true} src="https://files.readme.io/dfe5a85-2019-10-22_22_11_14-Window.png" />

## Delete barges

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

<Image title="2019-10-22 22_11_37-Window.png" alt={1915} className="border" border={true} src="https://files.readme.io/54a6a34-2019-10-22_22_11_37-Window.png" />

## Change Barge Active Status

* By default, all barges will have their status as ***Active*** right after being created, represented by the icon :fa-check-square-o: under the column **Active**
* To change the status of a barge into inactive, you can click on that :fa-check-square-o: icon. That icon will change into :fa-square-o:, meaning that barge status has changed to **Inactive**

<Image title="2019-10-15 11_03_02-Window.png" alt={1671} className="border" border={true} src="https://files.readme.io/49f7a85-2019-10-15_11_03_02-Window.png" />

* **Note**: Inactive barge will not be visible on the Barge Plan Dashboard

## View current locations of barges on map

* Right after the Shipment has been assigned to a barge, the mobile device equipped with that barge will be tracked. The GPS information of the mobile device will be sent to the system, enabling the dispatchers to know the current locations of the barges
* The tracking session will only stop after the barge has completed the Shipment and has not been assigned new shipments
* To view the current location of all active barges, follow the steps below:
* Navigate to **Transportation > Vehicle List** tab
* Click on the **Organization** filter and select the appropriate ***Transporter*** which manages the barges

<Image title="9a7ec39-fsfsdgadf.png" alt={1676} className="border" border={true} src="https://files.readme.io/c8ec8aa-9a7ec39-fsfsdgadf.png" />

* Click on the **View map** icon on the toolbar

<Image title="d499c64-mb3-setup-consumer-3.5.1.2522-1.0.374-1.0.5434.exe.png" alt={1677} className="border" border={true} src="https://files.readme.io/a2951a2-d499c64-mb3-setup-consumer-3.5.1.2522-1.0.374-1.0.5434.exe.png" />

* You will be directed to the Map screen
* The Map screen will show the current location of all barges under the management of the selected Transporter, along with their status
* Click on a barge's icon will reveal all barges currently at that location. There will be black lines connecting these barges

<Image title="2b1ae2e-sadfasdgsagd.png" alt={1677} className="border" border={true} src="https://files.readme.io/90dd905-2b1ae2e-sadfasdgsagd.png" />

<Image title="956ab53-safsdfsdf.png" alt={1677} className="border" border={true} src="https://files.readme.io/385921f-956ab53-safsdfsdf.png" />

### Search for barge

* You can search a specific barge by inputting its ***Vehicle code*** into the search bar

<Image title="da2a379-2019-10-17_15_20_22-Window.png" alt={1204} className="border" border={true} src="https://files.readme.io/70a0531-da2a379-2019-10-17_15_20_22-Window.png" />

### Filter barges by status

* You can filter to show barges based on their respective statuses by following the steps below
* Click on the blue **Select All** button on the top left of the Map screen

<Image title="211a371-sdfsdfs.png" alt={1677} className="border" border={true} src="https://files.readme.io/cc30ce2-211a371-sdfsdfs.png" />

* The barge statuses will be grouped into four groups. Each group will have a distinct color to easily differentiate

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Status group title
      </th>

      <th>
        Status group color
      </th>

      <th>
        List of barge statuses
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Status Group 1
      </td>

      <td>
        Green color
      </td>

      <td>
        Plan Awaiting
      </td>
    </tr>

    <tr>
      <td>
        Status Group 2
      </td>

      <td>
        Red color
      </td>

      <td>
        Plan Exists\
        Plan Received
      </td>
    </tr>

    <tr>
      <td>
        Status Group 3
      </td>

      <td>
        Orange color
      </td>

      <td>
        In Transit
      </td>
    </tr>

    <tr>
      <td>
        Status Group 4
      </td>

      <td>
        Blue color
      </td>

      <td>
        Line Up Awaiting\
        Unload Awaiting\
        In Wharves Line Up Awaiting\
        In Wharves Unload Awaiting\
        Line Up Started\
        Line Up Completed\
        Unload Started\
        Unload Completed
      </td>
    </tr>
  </tbody>
</Table>

* You can filter the barges whose current statuses fall into a specific Status group by clicking on that Status group title on the menu
* You can click on a barge's icon on the Map screen to view the detail information of that barge

<Image title="c8a58a5-fsadfsdf.png" alt={1677} className="border" border={true} src="https://files.readme.io/4c1b957-c8a58a5-fsadfsdf.png" />

* You can click on **Details** button to view the container list of the shipment the barge is currently performing

<Image title="f1ac7a5-2019-10-17_14_21_33-Window.png" alt={1222} className="border" border={true} src="https://files.readme.io/8ec0bb3-f1ac7a5-2019-10-17_14_21_33-Window.png" />

* You can click on the **History** tab to view the shipments that the barge has performed in the past. The history is divided by dates. You have to click on the date field, choose a date from the drop down calendar

<Image title="48419c9-2019-10-17_14_25_16-Window.png" alt={340} className="border" border={true} src="https://files.readme.io/57d7fbf-48419c9-2019-10-17_14_25_16-Window.png" />

## Update Barge Location

* After a barge captain has submitted the task **Shipping Started** at the first Drop Stop of the Actual shipment on Mobile app, you can update that barge's location. The indicator of such barges is that they have the icon **Update Vehicle Location** :fa-map-marker: under the column **Action**

<Image title="bargeloc.png" alt={1625} className="border" border={true} src="https://files.readme.io/e01f438-bargeloc.png" />

* To update the barge location, you need to click on the icon **Update Vehicle Location**. Upon clicking, the form **Update Location** will appear. On this form, the field **Vehicle Current Location** shows the current location of the barge

<Image title="ubarge.png" alt={1492} className="border" border={true} src="https://files.readme.io/cba2648-ubarge.png" />

* To change the location, click on the field **Location**, input the code/name of the desired location into the search bar then select the returned value (The location codes/location names are the same as the Customer Codes/Customer Names and can be found under the columns with the same titels in the tab **Partners > Customers**)
* After the desired location has been selected, you then need to click the button **Update**. Upon clicking, a confirmation form will appear. Here you can decide whether to: 1. send a request to create NFR shipment to the external TMS by clicking the button **Create NFR**; or 2. just simply update the barge location on Abivin vRoute Web app by clicking the button **Update Vehicle Location Only**

<Image title="ubarge2.png" alt={892} className="border" border={true} src="https://files.readme.io/8a9a163-ubarge2.png" />

* If you click **Update Vehicle Location Only**, the barge location will be updated right away. If you click **Create NFR**, a request to create NFR Shipment for the barge will be sent to the external TMS system. If the dispatcher on the external TMS system creates the NFR Shipment, then the barge captain can submit the NFR Shipment on the Mobile app. Two minutes after the NFR request has been sent, if the dispatcher on the external TMS system hasn't created the NFR Shipment, there will be a notification on the top right of the Web app to remind you to contact the TMS dispatcher
