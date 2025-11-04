---
title: Manage Shipments
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
## Locate Shipment list

* Barge Shipments are listed on **Tasks > Shipment** tab

<Image title="ced8c81-2019-08-18_22_56_15-TechSmith_Camtasia_2019.png" alt={1916} className="border" border={true} src="https://files.readme.io/1b1780d-ced8c81-2019-08-18_22_56_15-TechSmith_Camtasia_2019.png" />

## Shipment Information Fields

### General Shipment information fields

* The general information of a Shipment is present on the tab **Shipments** (Web form) and the sheet **Shipments** (Excel template)

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
        (Web form + Excel template)
        (Required)
      </td>

      <td>
        Management code assigned to the Shipment being created\
        Format: Must not contain spaces\
        For example: "Shipment 01" is not acceptable; "Shipment\_01" is acceptable
      </td>
    </tr>

    <tr>
      <td>
        Itinerary Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Itinerary Code of the Shipment being created\
        Format: Must not contain spaces\
        For example: "Itinerary 01" is invalid; "Itinerary\_01" is valid
      </td>
    </tr>

    <tr>
      <td>
        Leg Position\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Numerical order of the itinerary leg of the Shipment being created\
        Format: Number only. The minimum value is 0. The maximum value is 9\
        Note: For a shipments will all new containers (Containers that have never been in any previous shipment), the leg position of all containers must be 0 in order for them to display on the Mobile app, so that the driver can see and request
      </td>
    </tr>

    <tr>
      <td>
        Shipment Mode\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Mode of transport used for the shipment being created\
        For shipments of Sea barge model, the shipment mode is Barge
      </td>
    </tr>

    <tr>
      <td>
        Shipment Order Type\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Order type of the shipment being created\
        There are two types:\
        INTERNAL: Shipments between your organization's Inland Container Depots (ICD)\
        EXTERNAL: Shipments from your organization's Inland Container Depots to external locations
      </td>
    </tr>

    <tr>
      <td>
        Shipment Type\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Type of the shipment being created\
        If the Order Type of the Shipment being created is INTERNAL, there are three shipment type options:\
        DUMMY: The shipment type in which the barge will pick up containers at one or more locations\
        ACTUAL: The shipment type in which the barge will drop off containers at one or more locations\
        NFR (Non-freight related): The shipment type in which the barge will travel from one location to another location without loading any container\
        If the Order Type of the Shipment being created is EXTERNAL, there are two shipment type options:\
        ACTUAL: The shipment type in which the barge will both pick up containers at one or more locations and then drop off containers at one or more other locations\
        NFR (Non-freight related): Same as above
      </td>
    </tr>

    <tr>
      <td>
        Transaction Type\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Transaction Type of the shipment being created\
        There are seven transaction types:\
        IMPORT\
        EXPORT\
        DOMESTIC\
        EXPORT - IMPORT\
        DOMESTIC - EXPORT\
        DOMESTIC - IMPORT\
        DOMESTIC - EXPORT - IMPORT
      </td>
    </tr>

    <tr>
      <td>
        Vehicle\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Vehicle Code of the barge that will perform the shipment being created
      </td>
    </tr>

    <tr>
      <td>
        Stuffing Date\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        The official due date to stuff goods to the containers of the shipment being created
      </td>
    </tr>

    <tr>
      <td>
        Cut-off Date\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        The latest possible date the containers of the shipment may be delivered to a terminal for loading to a ship
      </td>
    </tr>

    <tr>
      <td>
        Late Delivery Time\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        The date and time at which the shipment being created will be considered late to start
      </td>
    </tr>

    <tr>
      <td>
        Shipment Note\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        A specific note about the shipment being created
      </td>
    </tr>

    <tr>
      <td>
        Origin Customer Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Code of the location where the shipment being created originally departs
      </td>
    </tr>

    <tr>
      <td>
        Destination Customer Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Code of the location where the shipment being created ultimately arrives
      </td>
    </tr>
  </tbody>
</Table>

### Shipment Stops information fields

* These information fields are present on the tab **Stops** (Web form) and the sheet **Stops** (Excel template)

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
        (Web form + Excel template)
        (Required)
      </td>

      <td>
        Management code assigned to the Shipment being created
      </td>
    </tr>

    <tr>
      <td>
        Shipment Stop Index\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Numerical code of the shipment stop being created
      </td>
    </tr>

    <tr>
      <td>
        Location (Web form); Shipment Stop Location Code (Excel template)\
        (Required)
      </td>

      <td>
        Location code of the shipment stop being created
      </td>
    </tr>

    <tr>
      <td>
        Task Group (Web form); Task Group Code (Excel template)\
        (Required)
      </td>

      <td>
        **This information fields is used only for Freight transport - Road model**\
        The task group to be performed at the shipment stop being created
      </td>
    </tr>

    <tr>
      <td>
        Shipment Stop Type\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Type of the shipment stop being created\
        There are two types: Pick stop and Drop stop
      </td>
    </tr>

    <tr>
      <td>
        Estimated Time Arrival\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Estimated Time of Arrival at the shipment stop being created
      </td>
    </tr>

    <tr>
      <td>
        Planned Time Arrival\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Planned Time of Arrival at the shipment stop being created
      </td>
    </tr>

    <tr>
      <td>
        Estimated Time Departure\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Estimated Time of Departure from the shipment stop being created
      </td>
    </tr>

    <tr>
      <td>
        Planned Time Departure\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Planned Time of Departure from the shipment stop being created
      </td>
    </tr>
  </tbody>
</Table>

### Shipment Containers information fields

* These information fields are present on the tab **Containers** (Web form) and the sheet **Containers** (Excel template)

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
        (Excel template)
        (Required)
      </td>

      <td>
        Management code assigned to the Shipment being created
      </td>
    </tr>

    <tr>
      <td>
        Stop Index (Web form); Shipment Stop Index (Excel template)\
        (Required)
      </td>

      <td>
        Numerical code of the shipment stop
      </td>
    </tr>

    <tr>
      <td>
        Container Number\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Numbers printed on the door of the container
      </td>
    </tr>

    <tr>
      <td>
        Seal Number\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        The numbers printed on the seal lock of the container
      </td>
    </tr>

    <tr>
      <td>
        Leg Position
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Booking Number\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Booking Number of the container included in the shipment being created
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
        Shipping Line\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        Code of the shipping line company that will transport the container
      </td>
    </tr>

    <tr>
      <td>
        Customer\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Ultimate customer of the container
      </td>
    </tr>

    <tr>
      <td>
        Container Status\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Most recent status of the container at the time the shipment is created
      </td>
    </tr>

    <tr>
      <td>
        Container Type\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Type of the container
      </td>
    </tr>

    <tr>
      <td>
        Vessel\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        Code of the vessel that will transport the container
      </td>
    </tr>

    <tr>
      <td>
        Voyage ID\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        Code of the voyage that will transport the container
      </td>
    </tr>

    <tr>
      <td>
        Pick Location\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Code of the location from where the container is picked up
      </td>
    </tr>

    <tr>
      <td>
        Drop Location\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Code of the location to where the container will be dropped off
      </td>
    </tr>

    <tr>
      <td>
        IMO Class\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        IMO Class of the container\
        There are two classes:\
        Dangerous goods:  FXIX\
        Oversize goods: FXXO
      </td>
    </tr>

    <tr>
      <td>
        Temperature\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        Temperature of the container
      </td>
    </tr>

    <tr>
      <td>
        Tare Weight\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Weight of the container without loading any goods
      </td>
    </tr>

    <tr>
      <td>
        Gross Weight\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Maximum goods weight that the container can carry
      </td>
    </tr>

    <tr>
      <td>
        VGM\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Short for Verified Gross Mass - The verified weight of the cargo plus the tare weight of the container
      </td>
    </tr>

    <tr>
      <td>
        Note\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        A short note about the container
      </td>
    </tr>
  </tbody>
</Table>

## Create shipments

* There are two methods to create shipment: Using Web form and using Excel template

### **Create shipments using Web form**

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using Web form
* Below is the input instruction for each information field on Web form

#### **1. Tab Shipments**

* First, you have to click on **Shipment Mode** field, select the value ***BARGE*** from the drop down menu

<Image title="Image 5.png" alt={1494} className="border" border={true} src="https://files.readme.io/f0c08ad-Image_5.png" />

* Then, input in other information fields
* Below are some notes when creating/assign Shipments

##### Barge assignment rules

* When the dispatchers try to assign a Shipment to a particular barge, the system will validate some rules
* The general rules are:
* 1 - With nonempty Shipments (Dummy, Internal and External Actual Shipments), at any particular time point, the barge can only be assigned a maximum of one ongoing Shipment (Shipment currently being performed) and one pending Shipment (Shipment waiting to be performed)
* 2 - With empty Shipments (Non-freight Related, or NFR Shipments), you can assign a NFR Shipment to a barge right after its corresponding Actual Shipment has been assigned to that barge

###### Dummy Shipments

* If the barge is currently not performing any Shipment, then you can assign a new Dummy Shipment to that barge
* You can not assign a new Dummy Shipment to a barge if that barge is still performing another Dummy Shipment. Only after the preceding Dummy Shipment has been completed the new one can be assigned
* You can not assign a new Dummy Shipment to a barge if that barge has already been assigned an External Actual Shipment, and the barge captain has yet to submit tasks of that External Actual Shipment on Mobile app

###### Internal Actual Shipments

* You can assign a new Internal Actual Shipment to a barge even if the barge is still performing, hasn't yet completed an External Actual Shipment

###### External Actual Shipments

* You can not assign a new External Actual Shipment to a barge if that barge has a completed Dummy Shipment that has not been linked with an Internal Actual Shipment
* You can not assign a new External Actual Shipment to a barge if that barge has already been assigned an External Actual Shipment, and the barge captain has yet to submit tasks of the preceding External Actual Shipment on Mobile app

###### Non-freight Related (NFR) Shipments

* At any particular time point, a barge can be concurrently assigned one Internal NFR Shipment and one Eternal NFR Shipment 

#### **2. Tab Stops**

* After you have input all necessary information on tab **Shipments**, navigate to tab **Stops**
* On this tab, you have to add the Shipment Stops to the Shipment being created. Start by clicking on **Location** field, input either the name or code of the appropriate location into the search bar, then select from the drop down menu
* The names and codes of the locations can be found under **Customer Code** and **Customer Name** columns in **Partners > Customer List** tab
* Next, click on **Stop Type** field, select the appropriate stop type from the drop down menu
* Then, click on **Add Stop** button to add the stop to the shipment
* The stop will appear in the stop list below
* Repeat these steps for other stops

<Image title="add shipment stop.gif" alt={1912} className="border" border={true} src="https://files.readme.io/a466a43-add_shipment_stop.gif" />

* In the stop list, you have to specify the Estimated Time Arrival; Planned Time Arrival; Estimated Time Departure; Planned Time Departure for each stop. To do that, click on the calendar icon :fa-calendar-o: of each corresponding information field, then select the appropriate date/hour/minute/second from the drop down calendars

<Image title="Image 6.png" alt={1518} className="border" border={true} src="https://files.readme.io/15df4c6-Image_6.png" />

* If you accidentally add the wrong stop, you can remove it by clicking on trash bin icon :fa-trash: under **Action** column

<Image title="Image 7.png" alt={1480} className="border" border={true} src="https://files.readme.io/d94af23-Image_7.png" />

#### **3. Tab Containers**

* After you have added all stops of the shipment in tab **Stops**, let's navigate to tab **Containers** to add containers to the shipment
* First, click on **Stop Index** field. The drop down menu will list all available **Pick Stops** that you have added earlier, along with their numerical order. Select the appropriate Pick Stop from the list
* Next, input container number into **Container Number** field. Then, click on **Add Container** button. Repeat these steps for other containers
* The containers will appear in the container list below. You then need to input information for each container

> 🚧 Container number format
>
> * You can input freely into **Container Number** field. However, only containers that have their numbers written correctly in [**ISO standard**](https://en.wikipedia.org/wiki/ISO_6346) (for example ***CSQU3054383***) will show up on Mobile app

<Image title="add container.gif" alt={1912} border={true} src="https://files.readme.io/2c197c8-add_container.gif">
  Adding container to Shipment
</Image>

* If you accidentally add the wrong container, you can remove it by clicking on trash bin icon :fa-trash: under **Action** column

<Image title="Image 8.png" alt={1494} className="border" border={true} src="https://files.readme.io/c844a64-Image_8.png" />

* Finally, click on the button **Create** to finish creating the shipment

<Image title="Image 9.png" alt={1495} className="border" border={true} src="https://files.readme.io/64204e5-Image_9.png" />

### **Create shipments using Excel template**

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form
* Below is the input instruction for each information field in the Excel template

#### **Sheet Shipments**

##### **2.1. Shipment Mode**

* First, you have to input the following value into **Shipment Mode** cell (Note: All letters must be uppercase): ***BARGE*** 

##### **2.2. Shipment Type**

* Input only one appropriate value from the following three values into this cell (Note: All letters must be uppercase): ***ACTUAL; DUMMY; NFR***

##### **2.3. Transaction Type**

* Input only one appropriate value from the following seven values in the table below into this cell

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Value on Web form
      </th>

      <th>
        Corresponding value in Excel template
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        IMPORT
      </td>

      <td>
        I
      </td>
    </tr>

    <tr>
      <td>
        EXPORT
      </td>

      <td>
        E
      </td>
    </tr>

    <tr>
      <td>
        DOMESTIC
      </td>

      <td>
        D
      </td>
    </tr>

    <tr>
      <td>
        EXPORT - IMPORT
      </td>

      <td>
        E,I
      </td>
    </tr>

    <tr>
      <td>
        DOMESTIC - IMPORT
      </td>

      <td>
        D,I
      </td>
    </tr>

    <tr>
      <td>
        DOMESTIC - EXPORT
      </td>

      <td>
        D,E
      </td>
    </tr>

    <tr>
      <td>
        DOMESTIC - EXPORT - IMPORT
      </td>

      <td>
        D,E,I
      </td>
    </tr>
  </tbody>
</Table>

##### **2.4. Shipment Order Type**

* If the shipment order type of the shipment is internal, input the following value into this cell (Note: All letters must be uppercase): ***INTERNAL***
* If the shipment order type of the shipment is external, input the following value into this cell (Note: All letters must be uppercase): ***EXTERNAL***

##### **2.5. Vehicle**

* Copy the Vehicle Code of the appropriate barge on Web app, then paste into this cell
* The Vehicle Code can be found under **Vehicle Code** column in **Transportation > Vehicle List** tab

##### **2.6. Origin Customer Code; Destination Customer Code**

* Copy the Customer Codes of the appropriate customers on Web app, then paste into these cells
* The Customer Codes can be found under **Customer Code** column in **Partners > Customer List** tab

<Image title="2019-11-08 15_51_16-Import_Shipment_2Template (2).xlsx - Excel.png" alt={1902} className="border" border={true} src="https://files.readme.io/7e31af7-2019-11-08_15_51_16-Import_Shipment_2Template_2.xlsx_-_Excel.png" />

##### **2.7. Itinerary Code**

* Input the corresponding itinerary code of the shipment into this cell

<Image title="2019-11-08 15_15_06-Import_Shipment_Template (2).xlsx - Excel.png" alt={112} className="border" border={true} src="https://files.readme.io/ab8a02c-2019-11-08_15_15_06-Import_Shipment_Template_2.xlsx_-_Excel.png" />

##### **2.8. Leg Index**

* Input the corresponding Leg index of the shipment into this cell

<Image title="2019-11-08 15_15_44-Import_Shipment_Template (2).xlsx - Excel.png" alt={110} className="border" border={true} src="https://files.readme.io/0b4e0dc-2019-11-08_15_15_44-Import_Shipment_Template_2.xlsx_-_Excel.png" />

##### **2.9. Shipment Mode**

* Always input the following value into this cell: ***BARGE***

##### **2.10. Shipment Type**

* Input the following value into this cell if the shipment being created is a Dummy shipment: ***DUMMY*** 
* Input the following value into this cell if the shipment being created is an Actual shipment: ***ACTUAL***

<Image title="2019-11-08 15_16_53-Import_Shipment_Template (2).xlsx - Excel.png" alt={141} className="border" border={true} src="https://files.readme.io/e5d3c25-2019-11-08_15_16_53-Import_Shipment_Template_2.xlsx_-_Excel.png" />

##### **2.11. Transaction Type**

* Input only one of the following six values from the below table into this cell

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Value on Web form
      </th>

      <th>
        Corresponding value in Excel template
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        IMPORT
      </td>

      <td>
        I
      </td>
    </tr>

    <tr>
      <td>
        EXPORT
      </td>

      <td>
        E
      </td>
    </tr>

    <tr>
      <td>
        DOMESTIC
      </td>

      <td>
        D
      </td>
    </tr>

    <tr>
      <td>
        EXPORT - IMPORT
      </td>

      <td>
        E,I
      </td>
    </tr>

    <tr>
      <td>
        DOMESTIC - IMPORT
      </td>

      <td>
        D,I
      </td>
    </tr>

    <tr>
      <td>
        DOMESTIC - EXPORT
      </td>

      <td>
        D,E
      </td>
    </tr>

    <tr>
      <td>
        DOMESTIC - EXPORT - IMPORT
      </td>

      <td>
        D,E,I
      </td>
    </tr>
  </tbody>
</Table>

##### **2.12. Vehicle**

* Copy the Vehicle Code of the barge on Web app, then paste into this cell
* The Vehicle Code can be found under **Vehicle Code** column in **Transportation > Vehicle List** tab

<Image title="2019-11-08 15_34_52-I2mport_Shipment_Template (2).xlsx - Excel.png" alt={1905} className="border" border={true} src="https://files.readme.io/80430f8-2019-11-08_15_34_52-I2mport_Shipment_Template_2.xlsx_-_Excel.png" />

##### **2.13. Trailer**

* This information field is only used for Freight transport - Road model. Just leave this cell blank

##### **2.14. Stuffing Date; Cut-off Date; Late Delivery Time**

* These dates must be input in the following format: ***dd/mm/yyyy hh:mm***
* For example: ***20/11/2019 12:30***

##### **2.15. Shipment Note**

* Format: Free-form

#### **Sheet Stop**

##### **2.16. Shipment Code**

* Same as instructed above

##### **2.17. Shipment Stop Index**

* Input the corresponding numerical order of the shipment stop into this cell
* For example: ***1; 2; 3*** and so on

##### **2.18. Shipment Stop Location Code**

* Copy the Customer Codes of the corresponding locations on Web app, then paste into these cells
* The Customer Codes can be found under **Customer Code** column in **Partners > Customer List** tab

<Image title="2019-11-08 16_03_06-Import_Shipment_Template (2).xlsx - Excel.png" alt={1897} className="border" border={true} src="https://files.readme.io/0bb5415-2019-11-08_16_03_06-Import_Shipment_Template_2.xlsx_-_Excel.png" />

##### **2.19. Task Group Code**

* This information field is only used for Freight transport - Road model. Just leave this cell blank

##### **2.20. Shipment Stop Type**

* If the stop is a Pick stop, input the following value into this cell: ***P***
* If the stop is a Drop stop, input the following value into this cell: ***D***

<Image title="2019-11-08 16_04_41-Import_Shipment_Template (2).xlsx - Excel.png" alt={168} className="border" border={true} src="https://files.readme.io/5b2975b-2019-11-08_16_04_41-Import_Shipment_Template_2.xlsx_-_Excel.png" />

##### **2.21. Estimated Time Arrival; Planned Time Arrival; Estimated Time Departure; Planned Time Departure**

* These dates must be input in the following format: ***dd/mm/yyyy hh:mm***
* For example: ***18/11/2019 08:30***

<Image title="2019-11-08 16_05_19-Import_Shipment_Template (2).xlsx - Excel.png" alt={859} className="border" border={true} src="https://files.readme.io/3fafe6c-2019-11-08_16_05_19-Import_Shipment_Template_2.xlsx_-_Excel.png" />

#### **Sheet Container**

##### **2.22. Shipment Code**

* Same as instructed above

##### **2.23. Shipment Stop Index**

* Same as instructed above

##### **2.24. Container Number**

* Input the numbers of the container into this cell
* For example: ***TKRU426221***

##### **2.25. Booking Number**

* Input the Booking Number that comes with the container into this cell
* For example: ***403772CHLTB***

##### **2.26. Seal Number**

* Input the numbers of the seal lock of the container into this cell
* For example: ***ES2633201***

##### **2.27. Shipping Line**

* Input the code of the shipping line into this cell
* For example: ***OCL\_LN***

##### **2.28. Customer; Pick Location; Drop Location**

* Copy the Customer Codes of the corresponding locations on Web app, then paste into these cells
* The Customer Codes can be found under **Customer Code** column in **Partners > Customer List** tab

<Image title="2019-11-08 16_06_56-Import_Shipment_Template (2).xlsx - Excel.png" alt={1901} className="border" border={true} src="https://files.readme.io/b83b338-2019-11-08_16_06_56-Import_Shipment_Template_2.xlsx_-_Excel.png" />

##### **2.29. Container Status**

* If the container has goods inside, input the following value into this cell: ***F***
* If the container is an empty container, doesn't have goods inside, input the following value into this cell: ***E***

<Image title="2019-11-08 16_08_57-Import_Shipment_Template (2).xlsx - Excel.png" alt={140} className="border" border={true} src="https://files.readme.io/6dd8431-2019-11-08_16_08_57-Import_Shipment_Template_2.xlsx_-_Excel.png" />

##### **2.30. Container Type**

* Copy the suitable container type code on Web app, then paste into this cell
* The container type code can be found under **Container Type Code** column in **Freights > Container Types** tab

<Image title="2019-11-08 16_10_25-Import_Shipment_Template (2).xlsx - Excel.png" alt={1902} className="border" border={true} src="https://files.readme.io/48e833d-2019-11-08_16_10_25-Import_Shipment_Template_2.xlsx_-_Excel.png" />

##### **2.31. Vessel**

* Input the code of the shipping vessel into this cell
* For example: ***EMPT; ATE; LGB*** etc.

##### **2.32. Voyage ID**

* Input the code of the voyage into this cell

##### **2.33. IMO Class**

* Input the following value into this cell if the container contains dangerous goods: ***FXIX***
* Input the following value into this cell if the container contains oversize goods: ***FXXO***
* If the container neither contains neither dangerous nor oversize goods, leave this cell blank

<Image title="2019-11-08 16_13_18-Import_Shipment_Template (2).xlsx - Excel.png" alt={99} className="border" border={true} src="https://files.readme.io/974b46e-2019-11-08_16_13_18-Import_Shipment_Template_2.xlsx_-_Excel.png" />

##### **2.34. Temperature**

* Input the corresponding temperature of the container (In degree Celsius)
* For example: ***2; 4; -20*** etc.

##### **2.35. Tare Weight; Gross Weight; VGM**

* Input the corresponding weights (In kilogram) into these cells
* For example: ***2500; 3000; 33000*** etc.

##### **2.36. Note**

* Format: Free-form

> 🚧 Rule about creating Dummy shipment
>
> For a barge, the previous assigned Dummy shipment has to be completed before the next assigned Dummy shipment can be created

## Edit shipments

* To edit a Shipment, click on **Edit** icon :fa-pencil: of that Shipment. You might need to use the horizontal scrollbar to scroll to the end of the Shipment list to see this icon

<Image title="Image 2.png" alt={1694} className="border" border={true} src="https://files.readme.io/c6ae220-Image_2.png" />

## Delete shipments

* To delete a Shipment, click on **Delete** icon :fa-remove: of that Shipment. You might need to use the horizontal scrollbar to scroll to the end of the Shipment list to see this icon

<Image title="Image 2.png" alt={1694} className="border" border={true} src="https://files.readme.io/dd88633-Image_2.png" />
