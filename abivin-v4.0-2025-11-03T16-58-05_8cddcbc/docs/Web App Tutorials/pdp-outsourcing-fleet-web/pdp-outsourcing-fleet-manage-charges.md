---
title: Manage Charges
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
## Charge Definition

* During the delivery process, there may happen scenarios in which as the Transporters' vehicles arrive at the construction sites (Depots), some expenses related to the Orders (Not Transport Service price) may incurre. These expenses are defined as ***Incurred Charges***
* An incurred Charge will specify the following information:
* 1 - What Order to which that incurred Charge relates
* 2 - The price of that incurred Charge
* 3 - The reason why that Charge incurred
* 4 - The Organization (Of Depot type) which will bear that incured charge. It could be the Origin Depot (where the products are picked up), or the Destination Depot (where the products are dropped off)
* In actual operation, there can be various Charges, therefore each management Branch can classify those Charges into separated categories called **Charge Types** to manage easier

## Compulsory Configurations

* In order to use this function, first you need to enable the module **Charge** for the User group your user accounts belongs in

<Image title="Selection_026.png" alt={817} className="border" border={true} src="https://files.readme.io/7e49773-Selection_026.png" />

## Manage Charge Types

### Locate Charge Type list

* Charge Types are listed on **Charges > Charge Type** tab

### Create Charge Type

* Charge Types can only be created using Web form
* Below are the information fields and input rules of a Charge Type 

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Description & Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Charge Type Code
      </td>

      <td>
        **1. Description:**\
        The management code of the Charge Type being created\
        **2. Input Rules:**\
        Format: Text and numbers. Must not contain spaces\
        For example: "Charge Type 01" is invalid; "Charge\_Type\_01" is valid
      </td>
    </tr>

    <tr>
      <td>
        Organization Code
      </td>

      <td>
        **1. Description:**\
        The Organization which directly manages the Charge Type being created\
        In this model, the management Organization is the Branch\
        **2. Input Rules:**\
        Click on this field. On the drop down list, select the appropriate Branch
      </td>
    </tr>

    <tr>
      <td>
        Charge Type Name
      </td>

      <td>
        **1. Description:**\
        Name of the Charge Type being created\
        **2. Input Rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

## Manage Charges

* After the Charge Types are created, you can proceed to create Charges

### Locate Charge list

* Charges are listed on **Charges > Charge List** tab

### Create Charge

* Charges can be created using Web form or Excel template
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using Web form
* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template
* **Note**: On Web app, you can directly create Charges for a particular Order over at the tab **PDP Orders > Current Orders**. On this tab, click on the icon **Charge** (Under column **Edit**) of the Order for which you want to create Charge. The form **Create Charge** will appear, similarly to the tab **Charges > Charge List**. After creating, the Charge will also appear on the tab **Charges > Charge List**

<Image title="ehh22OOQAf.png" alt={1686} className="border" border={true} src="https://files.readme.io/8e37e4d-ehh22OOQAf.png" />

### Charge information

* Below are the information fields and input rules of a Charge

> 🚧 The information of a Charge must be input exactly in the sequence below

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Description & Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Charge Code
        (Web form + Excel template)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code of the Charge being created\
        **2. Input Rules:**\
        Format: Text and numbers. Must not contain spaces\
        The default format is: ***CH-yymmdd-xxxx***\
        in which:\
        CH stands for Charge\
        yy is the last two digits of the year when the Charge was created\
        mm is the month when the Charge was created\
        dd is the date when the Charge was created\
        xxxx is the numerical order of the Charge on the date it was created\
        You can change the Charge Code to any format you want
      </td>
    </tr>

    <tr>
      <td>
        Organization (Web form); Organization Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Organization which directly manages the Order to which the Charge being created relates\
        In this model, the management Organization is the Branch\
        **2. Input Rules:**\
        **Web form:**\
        Click on this field. Select the appropriate Branch from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the appropriate Branch on Web app, then paste into this cell\
        **Note:**\
        The Organization Code can be found under the column of the same name in the tab "Organizations > Organization List"
      </td>
    </tr>

    <tr>
      <td>
        Order Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Order to which the Charge being created relates\
        **2. Input Rules:**\
        **Web form:**\
        Click on this field. The drop down menu will show all Orders managed by the selected Branch (Both Current Orders and Past Orders) created during the last 30 days. Click on the search bar, input the appropriate Order Code then select the returned value\
        **Excel template:**\
        Copy the appropriate Order Code on Web app, then paste into this cell\
        **Note:**\
        The Order Code can be found under the column of the same name in the tab "PDP Orders > Current Order"
      </td>
    </tr>

    <tr>
      <td>
        Charge Price\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The price of the Charge being created\
        **2. Input Rules:**\
        Format: Numbers\
        Input the value in numbers only. Do not input the unit\
        **Notes:**\
        You can input a negative Charge price (For instance: -100). This is because in certain scenarios, the Transport service price might be partly deducted, but hasn't been formulated. The negative charge price thus helps the dispatchers know how much the deducted amount is\
        When using Excel template, if the Charge is a decimal number, the decimal point could be a full stop (.) or a comma (,) based on the setting of your computer
      </td>
    </tr>

    <tr>
      <td>
        Charge Type (Web form); Charge Type Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Charge Type of the Charge being created\
        **2. Input Rules:**\
        **Web form:**\
        Click on this field. The drop down menu will show the Charge Types created by the selected Branch. Select the appropriate Charge Type\
        **Excel template:**\
        Copy the appropriate Charge Type Code on Web app, then paste into this cell\
        **Note:**\
        The Charge Type Code can be found under the column of the same name in the tab "Charges > Charge Type"
      </td>
    </tr>

    <tr>
      <td>
        Charge By (Web form); Charge By Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Organization which bears the Charge being created\
        In this model, the Organization which bears the Charges is the Depot\
        **2. Input Rules:**\
        **Web form:**\
        Click on this field. The drop down menu will only show the Origin and Destination Depots of the selected Order. Select the appropriate Depot\
        **Excel template:**\
        Copy the Organization Code of the appropriate Depot on Web app, then paste into this cell\
        **Note:**\
        The Organization Code can be found under the column of the same name in the tab "Organizations > Organization List"
      </td>
    </tr>

    <tr>
      <td>
        Comment\
        (Web form + Excel template)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Short description about the Charge being created\
        **2. Input Rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

## Export Charges

* You can export Charges of a particular Branch across a specific Date range by following the steps below
* First, click on the field **Organization**. Select the Branch which you want to export Charges
* Then, click on the calendar field. On the drop down calendars, select the appropriate date range
* Finally, hover over the icon :fa-plus-circle:, then click on the icon **Export** :fa-download:
* The Charges will be exported immediately

<Image title="nfsZYEOnp7.png" alt={1357} className="border" border={true} src="https://files.readme.io/66a266e-nfsZYEOnp7.png" />
