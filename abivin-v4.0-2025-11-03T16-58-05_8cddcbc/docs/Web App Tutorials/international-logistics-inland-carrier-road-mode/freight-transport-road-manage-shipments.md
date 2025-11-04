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
> 📘 This article is being edited

## Locate shipment tab

* Shipments are listed on **Tasks > Shipment** tab

<Image title="1UgPZkCtrb.png" alt={1920} className="border" border={true} src="https://files.readme.io/08086e5-1UgPZkCtrb.png" />

## Shipment Information Fields

### **General Shipment information fields**

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
        Management code assigned to the shipment being created
      </td>
    </tr>

    <tr>
      <td>
        Itinerary Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Itinerary Code of the shipment being created
      </td>
    </tr>

    <tr>
      <td>
        Leg Index\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        The numerical order of the leg of the shipment being created

        Note: the numerical order must start from 0.
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
        In this model, the shipment mode is Terminal Tractor (Or Truckload, abbreviated as TL)
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
        In this model, there is only one shipment type: ACTUAL
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
        There are three types: Internal; External and Domestic
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
        There are two types:
      </td>
    </tr>

    <tr>
      <td>
        Vehicle\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        Vehicle Code of the terminal tractor which delivers the shipment being created
      </td>
    </tr>

    <tr>
      <td>
        Trailer\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        Code of the trailer which delivers containers of the shipment being created (If available)
      </td>
    </tr>

    <tr>
      <td>
        Stuffing Date\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        The last date to stuff goods to the containers of the shipment being created at the consolidation point
      </td>
    </tr>

    <tr>
      <td>
        Cut-off Date\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        The last date at which export containers and all related documents of the shipment being created can be received for a particular vessel
      </td>
    </tr>

    <tr>
      <td>
        Late Delivery Time\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        The last date and time at which the shipment being created will be considered late to start
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
        Code of the location where the shipment being created starts
      </td>
    </tr>

    <tr>
      <td>
        Destination Customer Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        Code of the location where the shipment being created ends
      </td>
    </tr>
  </tbody>
</Table>

### **Shipment Stops information fields**

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
        Management code assigned to the shipment being created
      </td>
    </tr>

    <tr>
      <td>
        Stop Index (Web form); Shipment Stop Index (Excel template)\
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
        Code of the task group to be performed at the shipment stop being created
      </td>
    </tr>

    <tr>
      <td>
        Stop Type (Web form); Shipment Stop Type (Excel template)\
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

### **Shipment Containers information fields**

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
        Management code assigned to the shipment being created
      </td>
    </tr>

    <tr>
      <td>
        Stop Index (Web form); Shipment Stop Index (Excel template)\
        (Required)
      </td>

      <td>
        Numerical code of the shipment stop that stores the container(s) being added
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
        Booking Number\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        Booking Number of the container (If available)
      </td>
    </tr>

    <tr>
      <td>
        Seal Number\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        Number printed on the seal lock of the container
      </td>
    </tr>

    <tr>
      <td>
        Bill of Lading\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        Bill of Lading of the container (If available)
      </td>
    </tr>

    <tr>
      <td>
        Shipping Line\
        (Web form + Excel template)\
        (Required)
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
        (Required)
      </td>

      <td>
        Code of the vessel that will transport the container
      </td>
    </tr>

    <tr>
      <td>
        Voyage ID\
        (Web form + Excel template)\
        (Required)
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
        (Required)
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
        The verified goods weight that the container can carry
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

### Create shipments using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form
* Below is the input instruction for each information field on the Web form

#### **Tab Shipments**

<Image title="Image 2.png" alt={1492} className="border" border={true} src="https://files.readme.io/61a412e-Image_2.png" />

* **Shipment Code:**
* Format: Must not contain spaces
* **Itinerary Code:**
* Format: Must not contain spaces
* **Leg Index:**
* Format: Number (The order must start from 0)
* **Shipment Mode:**
* Click on this field, choose the value ***TL*** from the drop down menu
* **Shipment Order Type:**
* Click on this field, choose the appropriate value from the drop down menu
* **Shipment Type:**
* Click on this field, choose the appropriate value from the drop down menu
* **Vehicle:**
* Click on this field, input the appropriate vehicle code of the terminal tractor into the search bar, then select from the drop down menu
* If you don't want to assign the shipment being created to any particular terminal tractor, don't input anything into this field
* **Trailer:**
* Click on this field, input the trailer code of the trailer into the search bar, then select from the drop down menu
* If you don't want to assign the shipment being created to any particular trailer, don't input anything into this field
* **Stuffing Date; Cut-off Date; Late Delivery Time:**
* You can either click on the calendar icon :fa-calendar-o: and select the appropriate dates from the drop down menu, or input directly into this field in the following format: ***mm/dd/yyyy hh:mm***
* **Shipment Note:**
* Format: Free-form

#### **Tab Stops:**

* In this tab, you would have to input the information for each stop of the shipment
* **Location:**
* Click on this field, input the appropriate location code of the stop being created into the search bar, then select from the drop-down menu
* **Stop Type:**
* Click on this field, select the appropriate stop type for the stop being created from the drop-down menu
* **Task Group:**
* Click on this field, select the appropriate code of the task group to be performed at the stop being created from the drop-down menu
* There are twelve task groups to select. The detailed tasks of each task group are listed in the below table

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Task group code
      </th>

      <th>
        List of tasks
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        T1
        (For normal shipments)
      </td>

      <td>
        Lift On (1)\
        Gate Out
      </td>
    </tr>

    <tr>
      <td>
        T2\
        (For normal shipments)
      </td>

      <td>
        Lift On (0)\
        Gate Out
      </td>
    </tr>

    <tr>
      <td>
        T3\
        (For normal shipments)
      </td>

      <td>
        Gate In\
        Lift Off
      </td>
    </tr>

    <tr>
      <td>
        T4\
        (For normal shipments)
      </td>

      <td>
        Gate In\
        Stuffing Start\
        Stuffing Finish
      </td>
    </tr>

    <tr>
      <td>
        T5\
        (For normal shipments)
      </td>

      <td>
        Gate Out
      </td>
    </tr>

    <tr>
      <td>
        T6\
        (For normal shipments)
      </td>

      <td>
        Gate In\
        Destuffing Start\
        Destuffing Finish
      </td>
    </tr>

    <tr>
      <td>
        T7\
        (For normal shipments)
      </td>

      <td>
        Gate In\
        Trailer Detach
      </td>
    </tr>

    <tr>
      <td>
        T8\
        (For normal shipments)
      </td>

      <td>
        Trailer Attach\
        Gate Out
      </td>
    </tr>

    <tr>
      <td>
        T9\
        (For normal shipments)
      </td>

      <td>
        Gate In\
        Lift Off
      </td>
    </tr>

    <tr>
      <td>
        T10\
        (For normal shipments)
      </td>

      <td>
        Gate In\
        Lift Off\
        Trailer Detach
      </td>
    </tr>

    <tr>
      <td>
        T11\
        (For normal shipments)
      </td>

      <td>
        Trailer Attach\
        Lift On (0)\
        Gate Out
      </td>
    </tr>

    <tr>
      <td>
        T12\
        (For NFR shipments)
      </td>

      <td>
        Gate In
      </td>
    </tr>

    <tr>
      <td>
        T13\
        (For NFR shipments)
      </td>

      <td>
        Gate Out
      </td>
    </tr>
  </tbody>
</Table>

* After you have filled in the three above information fields, color the **Add Stop** button will turn to blue. Now you can click on that button to add the stop. The stop will appear in the **Shipment Stops List**. You would need to input into some more information fields of the stop
* **Estimated Time Arrival; Planned Time Arrival; Estimated Time Departure; Planned Time Departure:**
* Click on the :fa-calendar-o: icon, select the appropriate dates and time from the drop down calendar/watch

### Create shipments using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form
* Below is the input instruction for each information field in the Excel template

#### **Sheet Shipment**

* **Shipment Code:**
* Format: Must not contain spaces

<Image title="2019-11-07 10_36_32-Window.png" alt={117} className="border" border={true} src="https://files.readme.io/8374b94-2019-11-07_10_36_32-Window.png" />

* **Itinerary Code:**
* Format: Must not contain spaces

<Image title="2019-11-08 15_15_06-Import_Shipment_Template (2).xlsx - Excel.png" alt={112} className="border" border={true} src="https://files.readme.io/ab8a02c-2019-11-08_15_15_06-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Leg Index:**
* Input the numerical order of the leg (in number) into this cell
* For example: ***1; 2; 3*** etc.

<Image title="2019-11-08 15_15_44-Import_Shipment_Template (2).xlsx - Excel.png" alt={110} className="border" border={true} src="https://files.readme.io/0b4e0dc-2019-11-08_15_15_44-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Shipment Mode:**
* Always input the value ***TL*** into this cell

<Image title="2019-11-08 15_16_13-Import_Shipment_Template (2).xlsx - Excel.png" alt={167} className="border" border={true} src="https://files.readme.io/7a9a4d1-2019-11-08_15_16_13-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Shipment Type:**
* Always input the following value into this cell: ***ACTUAL***

<Image title="2019-11-08 15_16_53-Import_Shipment_Template (2).xlsx - Excel.png" alt={141} className="border" border={true} src="https://files.readme.io/e5d3c25-2019-11-08_15_16_53-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Transaction Type:**
* Input the value ***I*** (Capitalization of letter ***i***) into this cell if the transaction type of the shipment being created is ***Import***
* Input the value ***E*** into this cell if the transaction type of the shipment being created is ***Export***
* Input the value ***D*** into this cell if the transaction type of the shipment being created is ***Domestic***

<Image title="2019-11-08 15_17_36-Import_Shipment_Template (2).xlsx - Excel.png" alt={186} className="border" border={true} src="https://files.readme.io/c4b01de-2019-11-08_15_17_36-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Vehicle:**
* Copy the Vehicle Code of the Truck tractor on Web app, then paste into this cell
* The Vehicle Code can be found under **Vehicle Code** column in **Transportation > Vehicle List** tab

<Image title="2019-11-08 15_34_52-I2mport_Shipment_Template (2).xlsx - Excel.png" alt={1905} className="border" border={true} src="https://files.readme.io/80430f8-2019-11-08_15_34_52-I2mport_Shipment_Template_2.xlsx_-_Excel.png" />

* **Trailer:**
* Copy the trailer code on Web app, then paste into this cell
* The trailer code can be found under **Trailer Code** column in **Freights > Trailers** tab

<Image title="2019-11-08 16_29_25-Import_Shipment_Template (2).xlsx - Excel.png" alt={1896} className="border" border={true} src="https://files.readme.io/3209a0f-2019-11-08_16_29_25-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Stuffing Date; Cut-off Date; Late Delivery Time:**
* These dates must be input in the following format: ***dd/mm/yyyy hh:mm***
* For example: ***20/11/2019 12:30***
* **Shipment Note:**
* Format: Free-form
* **Origin Customer Code; Destination Customer Code:**
* Copy the Customer Codes of the corresponding locations on Web app, then paste into these cells
* The Customer Codes can be found under **Customer Code** column in **Partners > Customer List** tab

<Image title="2019-11-08 15_51_16-Import_Shipment_2Template (2).xlsx - Excel.png" alt={1902} className="border" border={true} src="https://files.readme.io/7e31af7-2019-11-08_15_51_16-Import_Shipment_2Template_2.xlsx_-_Excel.png" />

#### **Sheet Stop**

* **Shipment Code:**
* Same as instructed above
* **Shipment Stop Index:**
* Input the corresponding numerical order of the shipment stop into this cell
* For example: ***1; 2; 3*** and so on
* **Shipment Stop Location Code:**
* Copy the Customer Codes of the corresponding locations on Web app, then paste into these cells
* The Customer Codes can be found under **Customer Code** column in **Partners > Customer List** tab

<Image title="2019-11-08 16_03_06-Import_Shipment_Template (2).xlsx - Excel.png" alt={1897} className="border" border={true} src="https://files.readme.io/0bb5415-2019-11-08_16_03_06-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Task Group Code:**
* Input the appropriate task group code into this cell
* The list of task groups can be found above

- **Shipment Stop Type:**
- If the stop is a Pick stop, input the following value into this cell: ***P***
- If the stop is a Drop stop, input the following value into this cell: ***D***

<Image title="2019-11-08 16_04_41-Import_Shipment_Template (2).xlsx - Excel.png" alt={168} className="border" border={true} src="https://files.readme.io/5b2975b-2019-11-08_16_04_41-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Estimated Time Arrival; Planned Time Arrival; Estimated Time Departure; Planned Time Departure:**
* These dates must be input in the following format: ***dd/mm/yyyy hh:mm***
* For example: ***18/11/2019 08:30***

<Image title="2019-11-08 16_05_19-Import_Shipment_Template (2).xlsx - Excel.png" alt={859} className="border" border={true} src="https://files.readme.io/3fafe6c-2019-11-08_16_05_19-Import_Shipment_Template_2.xlsx_-_Excel.png" />

#### **Sheet Container**

* **Shipment Code:**
* Same as instructed above
* **Shipment Stop Index:**
* Same as instructed above
* **Container Number:**
* Input the numbers of the container into this cell
* For example: ***TKRU426221***
* **Booking Number:**
* Input the Booking Number that comes with the container into this cell
* For example: ***403772CHLTB***
* **Bill of Lading:**
* Input the Bill of Lading numbers that comes with the container into this cell
* For example: ***403772CHLTB***
* **Seal Number:**
* Input the numbers of the seal lock of the container into this cell
* For example: ***ES2633201***
* **Shipping Line:**
* Input the code of the shipping line into this cell
* For example: ***OCL\_LN***
* **Customer; Pick Location; Drop Location:**
* Copy the Customer Codes of the corresponding locations on Web app, then paste into these cells
* The Customer Codes can be found under **Customer Code** column in **Partners > Customer List** tab

<Image title="2019-11-08 16_06_56-Import_Shipment_Template (2).xlsx - Excel.png" alt={1901} className="border" border={true} src="https://files.readme.io/b83b338-2019-11-08_16_06_56-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Container Status:**
* If the container has goods inside, input the following value into this cell: ***F***
* If the container is an empty container, doesn't have goods inside, input the following value into this cell: ***E***

<Image title="2019-11-08 16_08_57-Import_Shipment_Template (2).xlsx - Excel.png" alt={140} className="border" border={true} src="https://files.readme.io/6dd8431-2019-11-08_16_08_57-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Container Type:**
* Copy the suitable container type code on Web app, then paste into this cell
* The container type code can be found under **Container Type Code** column in **Freights > Container Types** tab

<Image title="2019-11-08 16_10_25-Import_Shipment_Template (2).xlsx - Excel.png" alt={1902} className="border" border={true} src="https://files.readme.io/48e833d-2019-11-08_16_10_25-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Vessel:**
* Input the code of the shipping vessel into this cell
* For example: ***EMPT; ATE; LGB*** etc.
* **Voyage ID:**
* Input the code of the voyage into this cell
* **IMO Class:**
* Input the following value into this cell if the container contains dangerous goods: ***FXIX***
* Input the following value into this cell if the container contains oversize goods: ***FXXO***
* If the container neither contains neither dangerous nor oversize goods, leave this cell blank

<Image title="2019-11-08 16_13_18-Import_Shipment_Template (2).xlsx - Excel.png" alt={99} className="border" border={true} src="https://files.readme.io/974b46e-2019-11-08_16_13_18-Import_Shipment_Template_2.xlsx_-_Excel.png" />

* **Temperature:**
* Input the corresponding temperature of the container (In degree Celsius)
* For example: ***2; 4; -20*** etc.
* **Tare Weight; Gross Weight; VGM:**
* Input the corresponding weights (In kilogram) into these cells
* For example: ***2500; 3000; 33000*** etc.
* **Note:**
* Format: Free-form

## Update shipment

* Click on **Edit** :fa-pencil: icon of the shipment which you want to edit

## Delete shipment

## Export shipments

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-read-objects-on-excel-file-export-) article to know the general steps about exporting shipments in Abivin vRoute

<Image title="chrome_5Z3OBKUGLx.png" alt={1920} className="border" border={true} src="https://files.readme.io/c6d6d75-chrome_5Z3OBKUGLx.png" />

## Search Shipments

* You can search a Shipment by inputting one of the following attributes of that Shipment into the search bar:
* 1 - The Shipment Code
* 2 - The Container Number of a particular Container in that Shipment
