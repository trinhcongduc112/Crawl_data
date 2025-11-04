---
title: Transport Services
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
## Transport Service Definition

* Transport Services are the services provided by the third-party Transporters to fulfill the delivery tasks between different Depot groups

<Image title="transport service 1.png" alt={441} className="border" border={true} src="https://files.readme.io/a84595e-transport_service_1.png" />

## Transport Service Groups

## Transport Service Group Definition

* Transport Service Group is a group that comprises 1. A group of Depots, and 2. A Transporter who will provide the Transport Services for the Depots in that group
* **Note:** A Depot can belong in more than one Transport Service Group

<Image title="transport service group 1.png" alt={281} className="border" border={true} src="https://files.readme.io/88cab72-transport_service_group_1.png" />

## Locate Transport Service Group list

* Transport Service Groups are listed in the tab **Services > Service Groups** 

<Image title="2019-10-14 10_51_34-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/5974e59-2019-10-14_10_51_34-Window.png" />

## Create Transport service group

### Create single Transport service group using Web form

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using Web form

<Image title="2019-10-24 08_55_25-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/569e600-2019-10-24_08_55_25-Window.png" />

### Create multiple Transport service groups using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template

### Transport service group information fields

* Below is the list of information fields of a transport service group

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
        Service group code
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the transport service group being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Service Group 01" is not acceptable; "Service\_Group\_01" is acceptable
      </td>
    </tr>

    <tr>
      <td>
        Service group name\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        The management name assigned to the transport service group being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Depots (Web form); Depot Code (Excel template)
      </td>

      <td>
        **1. Description:**\
        The Depots chosen for the transport service group being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field, type the Organization Code/Organization Name of the Depot into the search bar, then choose from the drop down menu\
        Can select multiple Depots\
        **Excel template:**\
        Copy the Organization Code of the Depots on Web app, then paste into this cell\
        If there are multiple Depots, two adjacent Depots can be separated only by a comma\
        For example: Depot\_01,Depot\_02\
        Or can be separated by a comma and a space\
        For example: Depot\_01, Depot\_02\
        **Note:**\
        The Organization Code can be found under "Organization Code" column in "Organizations > Organization List" tab
      </td>
    </tr>

    <tr>
      <td>
        Transporter name (Web form); Transporter Code (Excel template)
      </td>

      <td>
        **1. Description:**\
        The transporter who will perform the transport services for the Depots in the transport service group being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field, type the Organization Code/Organization Name of the Transporter into the search bar, then choose from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the Transporter on Web app, then paste into this cell\
        **Note:**\
        The Organization Code can be found under "Organization Code" column in "Organizations > Organization List" tab
      </td>
    </tr>
  </tbody>
</Table>

#### Note when creating Transport Service Groups

* If you want to create Transport Services provided by a Tranposter between some specific Depots, you need to create two separate Transport Service Groups, one is the *original* Transport Service Group, and the other is the *counter* Transport Service Group. These two Transport Service Groups will have the same **Transporter Name** and **Depots** information, but different **Service Group Code** and **Service Group Name** information

## Manage Transport services

## Transport Service definition

* Transport services are the services provided by the Transporters to fulfill the delivery tasks betweens Depots belongings to two different groups of Depots. That means if two Transport Service Groups have the same Transporter, there can be Transport Services between those two groups

* A Transport Service will specify the following information:

* 1 - The Transporter who provides that Transport Service

* 2 - The Vehicle Type that will perform that Transport service

* 3 - The Depot Group where the Transporter's vehicles will travel to and pick up products (Defined as the ***Origin Transport\
  Service Group***), and the Depot group where the Transporter's vehicles will travel to and deliver products (Defined as the ***Destination Transport Service Group***)

* 4 - The fee for that Transport Service. There are three Transport Service fees:

* 4.1 - [**Main Transport Service fee**](https://docs.abivin.com/docs/pdp-outsourcing-fleet-transport-service#create-main-transport-services): The fee applied to the first Order of a vehicle's Delivery Trip

* Besides the Main Transport Service fee, the second Order (If available) of a vehicle will be applied the **Transport Service Surcharge** or the **Discounted Transport Service fee**

* 4.2 - [**Transport Service Surcharge**](https://docs.abivin.com/docs/pdp-outsourcing-fleet-transport-service#set-up-transport-service-surcharge): The fee applied to the second Order of a vehicle's Delivery Trip, provided that the first and second Orders share the same Origin Depot but two different Destination Depots and the distance between the two Destination Depots is smaller than a certain value. The Surcharge is independent of the Main Transport service fee and is changeable

* 4.3 - [**Discounted Transport Service fee**](https://docs.abivin.com/docs/pdp-outsourcing-fleet-transport-service#setup-discounted-transport-service-fee): The fee applied to the second Order of a vehicle's Delivery Trip, provided that: 1. the Origin Depots of the first and the second Orders are not the same, 2. The distance between the Destination Depot of the first Order and the Origin Depot of the second Order is smaller than a certain value, and 3. The distance between the Destination Depot of the second Order and the Origin Depot of the first Order is smaller than a certain value. The Discounted Transport Service fee is the Main Transport Service fee after discounting a certain percentage value

## Locate Main Transport services list

* Transport services are listed in **Service > Transport Services** tab

<Image title="2019-10-14 10_54_02-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/a0fe5e1-2019-10-14_10_54_02-Window.png" />

## Create Main Transport services

> ❗️ You need to create vehicles before being able to create Transport Services

### Main Transport Service information fields

* The Main Transport Services can be created using two methods: Webform and Excel template
* Below is the list of information fields of a Main Transport Service

> 📘 Apart from the information fields mentioned below, you do not need to input into other information fields

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
        Service Code
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        A management code assigned to the Main Transport Service being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Service 01" is not valid; "Service\_01" is valid
      </td>
    </tr>

    <tr>
      <td>
        Transporter Name (Web form); Transporter Code (Excel template)
      </td>

      <td>
        **1. Description:**\
        The Transporter that provides the Main Transport Service being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. On the search bar, input the Organization Code/Organization Name of the appropriate Transporter, then select the returned value\
        **Excel template:**\
        Copy the Organization Code of the appropriate Transporter on Web app then paste into the cell\
        **Note:**\
        The Organization Code and Organization Name can be found under columns of the same titles in the tab "Organizations > Organization"
      </td>
    </tr>

    <tr>
      <td>
        Vehicle Type (Web form); Vehicle Type Code (Excel template)
      </td>

      <td>
        **1. Description:**\
        The vehicle type of the Transporter which will perform the Main Transport Service being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. On the search bar, input the appropriate Vehicle Type Code into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the appropriate Vehicle Type Code on Web app then paste into this cell\
        **Note:**\
        The Vehicle Type Codes can be found under the column "Type Code" in the tab "Transport > Vehicle List"
      </td>
    </tr>

    <tr>
      <td>
        From\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        The Origin Transport Service group, from where the Transporter's vehicles will pick up products\
        **2. Input rules:**\
        **Web form:**\
        Click on the field, then select from the drop down menu\
        **Excel template:**\
        Copy the transport service group code on the Web app (Under "S.Group Code" column in "Services > Service Groups" tab), then paste into the cell
      </td>
    </tr>

    <tr>
      <td>
        To\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        The Destination Transport Service group, to where the Transporter's vehicles will deliver products\
        **2. Input rules:**\
        **Web form:**\
        Click on the field, then select from the drop down menu\
        **Excel template:**\
        Copy the transport service group code on the Web app (Under "S.Group Code" column in "Services > Service Groups" tab), then paste into the cell
      </td>
    </tr>

    <tr>
      <td>
        Unit\
        (Web form)
      </td>

      <td>
        **1. Description:**\
        The journey unit to which the transport service being created will apply\
        **2. Input rules:**\
        Format: Text\
        For example: Leg; Trip
      </td>
    </tr>

    <tr>
      <td>
        Service Price (Web form); Service Unit Price (Excel template)
      </td>

      <td>
        **1. Description:**\
        The Main fee of the Transport Service being created\
        **2. Input rules:**\
        Format: Numbers. Can be decimal\
        Input only the value. Do not input the currency unit\
        If the service price is a decimal number, use dot (.) to separate the whole part from the decimal part. Do not use comma (,)\
        For example: The transport unit is delivery trip. The service price per delivery trip is "One hundred and eight tenths US dollars". You need to type this value into the field/cell: 100.8. Do not type this value: 100,8
      </td>
    </tr>

    <tr>
      <td>
        Start Date; End Date\
        (Web form + Excel template)
      </td>

      <td>
        **1. Description:**\
        Start date and End date of the date range during which the service being created is effective\
        **2. Input rules:**\
        Format: dd/mm/yyyy\
        **Web form:**\
        Click on the field, then select the dates from the drop down calendar\
        **Excel template:**\
        Input the date into the cell
      </td>
    </tr>
  </tbody>
</Table>

### Create Single Transport Services via Webform

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating a single object using the Webform
* Below is an illustration gif of creating a new transport service

<Image title="create ts by transporter web.gif" alt={1668} className="border" border={true} src="https://files.readme.io/17be550-create_ts_by_transporter_web.gif" />

* **Note:** You can move on to creating a new Transport service without leaving the **Add New Service** screen simply by clicking on **Save and Continue** button after finishing creating a service

<Image title="2019-10-14 10_55_27-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/b03c8eb-2019-10-14_10_55_27-Window.png" />

### Create multiple transport services using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using the Excel template

### Note when creating Main Transport services

* When you first create a brand new Transport Service provided by a Transporter's Vehicle Type for two Depot groups (Let's call it the ***Original Transport Service***), you'll also need to create another Transport Service (Let's call it the ***Supplementary Transport Service***) which shares nearly the same information as the Original Transport Service. (Same Transporter, Vehicle Type, Price, Unit, Start Date, End Date attributes). The only difference between the Original and the Supplementary Transport Services (Besides the Service Code, obviously) is that the **Origin Transport Service Group** attribute of the Original Transport Service will be the **Destination Transport Service Group** attribute of the Supplementary Transport Service, and vice versa, the **Destination Transport Service Group** attribute of the Original Transport Service will be the **Origin Transport Service Group** attribute of the Supplementary Transport Service
* Below are the illustrations of the Original - Supplementary Transport Service pair on the Web app and in the Excel import file

<Image title="J0ek7msu8I.png" alt={429} border={true} src="https://files.readme.io/0775c50-J0ek7msu8I.png">
  Original - Supplementary Transport service pair on Web app
</Image>

<Image title="vIsrZEKHOD.png" alt={1009} border={true} src="https://files.readme.io/e69579c-vIsrZEKHOD.png">
  Original - Supplementary Transport service pair in Excel template
</Image>

## Transport Service Surcharges & Discounted Transport Service fee

### Locate Transport Service Surcharges & Discounted Transport Service fee setting section

* The Transport Service Surcharges and Discount rates can be set at the Branch. After setting, these Transport Service Surcharges and Discount rates will apply to all Transporters under the management of the Branch. However, you can also set the Transport Service Surcharges and Discount rates exclusively for each Transporter
* To set up Transport Service Surcharges and Discount rates for a Branch, perform the following
* Click the icon **Edit** :fa-pencil: of the **Branch**
* On the form **Update Organization**, navigate to the sub-tab **More Configuration > Discount**.  The section **Surcharge and Discount** is where you can set up the surcharges and discounts for all Transporters under the management of the Branch

<Image title="AIXbiAQ2YA.png" alt={740} className="border" border={true} src="https://files.readme.io/d6ce44a-AIXbiAQ2YA.png" />

* To set up the Transport Service Surcharges and Transport Service Discount Rates for each Transporter exclusively, click the icon **Edit** :fa-pencil: of each Transporter. On the form **Update Organization**, navigate to the sub-tab **More Configuration > Discount**. Here, instead of ticking the radio box **Default** (Which means the Transporter will abide by the settings of its upper-level Branch), tick the radio box **Custom**. The section **Surcharge and Discount** will appear similar to the Branch. However, the values input here will only apply to the selected Transporter

<Image title="CtrBLMTCo7.png" alt={738} className="border" border={true} src="https://files.readme.io/ce9d26b-CtrBLMTCo7.png" />

> ❗️ Compulsory Transport Service Surcharges and Transport Service Discount Rates declaration of the Transporters
>
> Even if you intend to apply the default Transport Service Surcharges and Transport Service Discount Rates of the Branch to all subordinate Transporters, you still need to declare that to the system by doing the following: Click **Edit** :fa-pencil: of each Transporter, navigate to the sub-tab **More Configuration**, tick the **Default** checkbox then click **Save**. Only after doing this will the system store the Transport Service Surcharges and Transport Service Discount Rates of the Transporter

## Set up Transport Service Surcharge

* As described above, Transport Service Surcharge is the fee applied to the second Order of a vehicle's Delivery Trip in the scenario the vehicle picks up products from one Origin Depot (Hereby referred to as the **first Depot**) then delivers to two different Destination Depots (Hereby referred to as the **second Depot** and **third Depot**), provided that the distance between the second and third Depots is smaller than a certain value. This distance value is defined as the **Surcharge Maximum Distance Level**
* You can set up two Surcharge Maximum Distance Levels, thereby set up two Surcharge Price Levels:
* Surcharge Price Level 1: Applicable when the Surcharge Maximum Distance Level is smaller than or equal to a specific value (Defined as the **Surcharge Maximum Distance Level 1**)
* Surcharge Price Level 2: Applicable when the Surcharge Maximum Distance Level is greater than the Surcharge Maximum Distance Level 1 but is smaller than or equal to another value (Defined as the **Surcharge Maximum Distance Level 2**)
* If the distance between the two Destination Depots is greater than the Surcharge Maximum Distance Level 2, then the system will apply the Main Transport Service fee to the second Order instead of the Surcharge
* To set up the Surcharge Maximum Level Distances and their respective Surcharge Price Levels, input into the four information fields shown below

<Image title="giKycm9032.png" alt={732} className="border" border={true} src="https://files.readme.io/7972c5b-giKycm9032.png" />

* Let's look at the example below to understand how Transport Service Surcharge works:
* The Surcharge Maximum Distance Level 1 and 2 are ***5*** and ***7*** kilometers respectively; the Surcharge Price Level 1 and 2 are ***500.000*** and ***1.000.000*** Vietnam Dong respectively

<Image title="aHvXATdZrL.png" alt={483} className="border" border={true} src="https://files.readme.io/26a7539-aHvXATdZrL.png" />

* This means the following:
* 1 - If the second Depot - third Depot distance is smaller than or equal to 5 kilometers, the Surcharge applied to the second Order will be 500.000 Vietnam Dong 
* 2 - If the second Depot - third Depot distance is greater than 5 kilometers but smaller than 7 kilometers, the Surcharge applied to the second Order will be 1.000.000 Vietnam Dong
* 3 - If the second Depot - third Depot distance is greater than 7 kilometers, the Main Transport Service fee will be applied to the second Order instead of the Surcharge

## Setup Discounted Transport Service fee

* As described above, Discounted Transport Service fee is the fee applied to the second Order of a vehicle's Delivery Trip when the Origin Depot of the first Order and the Origin Depot of the second Order are not the same
* There are two Delivery Trip types that will be applied the Discounted Transport Service fee: Connecting Trip and Returning Trip

### Connecting Trip

* **Connecting Trip** is the term to refer to the Delivery Trips in which after the vehicle delivers products of the first Order from the first Depot to the second Depot, it will then perform one of the two following scenarios:
* Scenario 1. Picks up products right at the second Depot (Which means the Destination Depot of the first Order is also the Origin Depot of the second Order) then delivers to a third Depot

- Scenario 2. Picks up products at a third Depot then delivers to a fourth Depot

* The Discounted Transport Service fee for the Connecting Trip is determined based on the distance between the second Depot (The Destination Depot of the first Order) and the third Depot (The Origin Depot of the second Order). If the distance is less than or equal to a certain value (Defined as the **Connecting Trip Maximum Distance**), then a Discount Rate (Defined as the **Discount Rate per Connecting Trip**) will be applied to the Main Transport Service fee. The Discounted Transport Service fee is the Main Transport Service fee after discounting the discount amount
* To set up the Connecting Trip Maximum Distance and the Discount Rate per Connecting Trip, input into the information fields with the same titles
* Let's look at the example below to understand how Discount for Connecting Trip works:
* The Connecting Trip Maximum Distance value is ***5*** kilometers and the Discount Rate per Connecting Trip is ***15*** percent

<Image title="HaaVT7dhHE.png" alt={355} className="border" border={true} src="https://files.readme.io/db59f47-HaaVT7dhHE.png" />

* That means if the Delivery Trip of the second Order qualifies to be a Connecting Trip, and the second Depot - third Depot distance is less than or equal to 5 kilometers, then the Discount Rate applied to the Main Transport Service fee will be 15 percent. The Discounted Transport Service fee for the second Order thus will be 0.85 (85 percent) of the Main Transport Service fee

### Returning Trip

* **Returning Trip** is the term to refer to the Delivery Trips in which after the vehicle delivers the first Order from a first Depot to a second Depot it will then perform one of the two following scenarios:
* Scenario 1. Picks up products right at the second Depot then delivers back to the first Depot (Which means the Origin and Destination Depots of the first and second Order are inverted)

- Scenario 2. Picks up products at a third Depot then either delivers back to the first Depot or to a fourth Depot. The fourth Depot is located on the third Depot - first Depot route

* The Discounted Transport Service fee will only be applied to the Returning Trip if the two following conditions are both met:
* Condition 1: The distance between the second Depot (The Destination Depot of the first Order) and the third Depot (The Origin Depot of the second Order) is less than or equal to a certain value. This value is defined as the **Returning Trip Maximum Distance Condition**. This is because if the second Depot - third Depot distance is relatively small the vehicles will not have to travel a long journey with an empty cargo
* Condition 2: The distance between the fourth Depot (The Destination Depot of the second Order) back to the first Depot (The Origin Depot of the first Order) is less than or equal to a certain value. This value is defined as the **Returning Trip Maximum Distance**. This is because the Transporter garage is usually located near the first Depot. If the fourth Depot - first Depot distance is relatively small, the vehicles will not have to travel a long journey with an empty cargo
* If these two conditions are met then the system will apply the Discounted Transport Service fee to the second Order. The Discounted Transport Service fee is calculated by deducting a discount amount from the Main Transport Service fee. The discount amount is calculated by multiplying the Main Transport Service fee with a rate. This rate is defined as the **Discount Rate per Returning Trip**
* To set up the Returning Trip Maximum Distance, the Returning Trip Maximum Distance Condition, and the Discount Rate per Returning Trip, input into the information fields with the same titles
* Let's look at the example below to understand how Discount for Returning Trip works:
* The Returning Trip Maximum Distance value is ***15*** kilometers. The Returning Trip Maximum Distance Condition is ***10*** kilometers. The Discount Rate per Returning Trip is ***20*** percent

- That means if 1. The second Depot - third Depot distance is less than or equal to 10 kilometers, 2. The fourth Depot - first Depot is less than or equal to 15 kilometers, then the Discount Rate applied to the Main Transport Service fee will be 20 percent. The Discounted Transport Service fee for the second Order thus will be 80 percent of the Main Transport Service fee

## Export Transport Services & Transport Service Groups

* To export Transport Services (As well as Transport Service Groups), on their respective tab, hover over the icon :fa-plus-circle:, then click the icon **Export Data** :fa-download:

<Image title="7YvdOMLSFZ.png" alt={1527} className="border" border={true} src="https://files.readme.io/3abf66f-7YvdOMLSFZ.png" />

* **Note:** In order to be able to do this, you need to enable the function **Export** for the module **Services** of the User Group to which your user account belong

<Image title="YSgOFvEkqL.png" alt={843} className="border" border={true} src="https://files.readme.io/66a2816-YSgOFvEkqL.png" />
