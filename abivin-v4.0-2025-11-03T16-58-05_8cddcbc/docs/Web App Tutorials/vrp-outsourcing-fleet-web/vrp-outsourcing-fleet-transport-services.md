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
## Select Transport Service option

## Enable Transport Service module

* Login with the top administrator account
* Navigate to **Organizations > Group List** tab
* Click on **Edit** :fa-pencil: icon of the Administrator User group of the ***Manufacturer***

<Image title="2019-10-17 08_55_15-Window.png" alt={1654} className="border" border={true} src="https://files.readme.io/e3f00a0-2019-10-17_08_55_15-Window.png" />

* Enable the **Services** module as shown below, then click on **Save** button to confirm the change

<Image title="2019-10-17 08_42_44-Window.png" alt={687} className="border" border={true} src="https://files.readme.io/5a3498e-2019-10-17_08_42_44-Window.png" />

## Select Transport Service option

* To select the appropriate Transport Service option, perform the steps below:
* Navigate to **Organizations > Organization List** tab
* Click on **Edit** :fa-pencil: icon of the ***Manufacturer***

<Image title="2019-10-14 09_55_32-Window.png" alt={1672} className="border" border={true} src="https://files.readme.io/42f8458-2019-10-14_09_55_32-Window.png" />

* On the **Organization Information** screen, click on **Transport Service By** field, select **2. Product** 
* Click **Save** to confirm the change

<Image title="ts product.png" alt={1897} className="border" border={true} src="https://files.readme.io/2db97f6-ts_product.png" />

## Transport service by Product

### Definition

* Transport services by Product is the action of a Transporter delivering a product from a warehouse of your organization to a warehouse of your customer (Defined as **Depart way**), and also delivering empty product cases/returned product items from the warehouse of your customer back to the warehouse of your organization (Defined as **Return way**)

### Locate Transport Service list

* The Transport Services are listed on the tab **Services > Transport Services**

### Information fields of a Transport service by Product

* **Important Note**: For each product, it is compulsory that you create both ***First way*** and ***Second way*** transport services. Those Transport Services will have the same Transporter, origin Depot and destination Customer , Service Price, Price Unit, Product Code. The differences are the Service Codes and the Types

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
        (Required)
      </td>

      <td>
        **1. Description:**\
        A management code assigned to the transport service being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Service 01" is not acceptable; "Service\_01" is acceptable
      </td>
    </tr>

    <tr>
      <td>
        Organization Code (Web form); Transporter Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Transporter who will perform the transport service being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Type the Organization Name/Organization Code of the transporter into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the transporter on Web app, then paste into this cell\
        **Note:**\
        The Organization Name/Organization Code of the Transporter can be found under "Organization Name" and "Organization Code" columns in "Organizations > Organization List" tab
      </td>
    </tr>

    <tr>
      <td>
        From\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Depot from where the product in the transport service being created will be picked up\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Type the Organization Name/Organization Code of the appropriate Depot into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the appropriate Depot on Web app, then paste into this cell\
        **Note:**\
        The Organization Code of the Depot can be found under "Organization Code" column in "Organizations > Organization List" tab
      </td>
    </tr>

    <tr>
      <td>
        To Customer (Web form); To (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The customer to where the product in the transport service being created will be delivered\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Type the Organization Name/Organization Code of the appropriate customer into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Customer Code of the appropriate customer on Web app, then paste into this cell\
        **Note:**\
        The Customer Code of the Customer can be found under "Customer Code" column in "Partners > Customer List" tab
      </td>
    </tr>

    <tr>
      <td>
        Type\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Type of the transport service being created (First way or Second way)\
        **2. Input rules:**\
        **Web form:**\
        Click on this field, select the suitable type from the drop down menu\
        **Excel template:**\
        If the transport service being created is Depart way type, input the following value into the cell: 1 way\
        If the transport service being created is Return way type, input the following value into the cell: 2 ways
      </td>
    </tr>

    <tr>
      <td>
        Product Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The product to be delivered from the origin location to the destination location by the transport service being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Type the product code of the product into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the product code on Web app, then paste into this cell\
        **Note:**\
        The product code can be found under "Product Code" column in "Products > Products" tab\
        The product has to be created for both the origin location and the destination location prior to creating this service
      </td>
    </tr>

    <tr>
      <td>
        Price Unit\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        The unit of the product in the transport service being created\
        For example: "Pack; Case; Item" etc.\
        **2. Input rules:**\
        This field automatically takes the value of the "Form/Unit" field of the selected product
      </td>
    </tr>

    <tr>
      <td>
        Service Price (Web form); Service Unit Price (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The price of the transport service being created\
        **2. Input rules:**\
        Input only the value. Do not input the unit\
        For example: Price of the transport service being created is: One hundred dollars. Input this value into the field/cell: 100
      </td>
    </tr>

    <tr>
      <td>
        Start Date; End Date; Vehicle Type Code\
        (Excel template)
      </td>

      <td>
        These information fields are used for Transport service by Transporter. You do not need to input anything. Just leave the cells blank
      </td>
    </tr>
  </tbody>
</Table>

### Create Transport service using Web form

* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) to know the general steps about creating single object using Web form
* Below is an illustration gif demonstrating the creation process of a Transport service by product on Web form

<Image title="create ts web product.gif" alt={1668} className="border" border={true} src="https://files.readme.io/fef3dd1-create_ts_web_product.gif" />

* You can move on to create a new transport service without leaving the **Add New Service** screen simply by clicking on the **Save and Continue** button

<Image title="2019-10-18 13_52_23-Window.png" alt={1675} className="border" border={true} src="https://files.readme.io/c1c5d76-2019-10-18_13_52_23-Window.png" />

### Create multiple Transport services using Excel template

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template

<Image title="2019-10-29 20_30_54-Window.png" alt={1380} className="border" border={true} src="https://files.readme.io/83e595c-2019-10-29_20_30_54-Window.png" />
