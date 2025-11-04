---
title: Associated Products
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
* A Product is usually made up of various smaller components. Take a mobile phone for instance. A mobile phone can be broken down into smaller discrete parts such as the screen, the frame, etc.
* The Shippers, the manufacturers of the Products will usually demand their own delivery fleet or the Carriers, the third-party transportation service providers, to deliver all parts of a finished Products on the same Delivery Trips so that when the parts arrive at the assembly plant, the workers can put together those parts into finished Products right away, which greatly decreases unwanted standby time
* This article will guide you on how you can set up the associated Products in the Abivin vRoute system

## Enable Associated Product Configuration

* The first thing that you need to do is to enable the **Associated Product** configuration
* To do this, follow the steps below
* Navigate to the **Organizations > Organizations** tab
* Click the **Edit** icon :fa-pencil: of the Manufacturer
* On the **Update Organization** form, navigate to the **More Configurations > Product Management** section. On this section, tick the **Enable Associated Product** checkbox

<Image title="9vxYdqWp4s.png" alt={737} border={true} src="https://files.readme.io/5c78fcf-9vxYdqWp4s.png">
  Illustration (English)
</Image>

<Image title="aKAH1qP3M5.png" alt={737} border={true} src="https://files.readme.io/6ec3f4c-aKAH1qP3M5.png">
  Illustration (Vietnamese)
</Image>

* Click **Save** to confirm the change
* **Note**: This configuration can be used for both of the Product management mechanisms, [**Shipper-oriented mechanism**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-product-categories#mechanism-1-shipper-oriented-product-management-mechanism) and [**Carrier/Distributor-oriented mechanism**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-product-categories#mechanism-2-carrierdistributor-oriented-product-management-mechanism)

## Create Association-Enabled Product Categories

* The next thing that you need to do is to create the Product Categories in which the associated Products belong

### Create Association-Enabled Product Categories Using The Webform

* On the Webform, input the basic information of the Product Categories following the rules in the main article [**Manage Product Categories**]()
* Then, click on the **Associated Products** field. On the drop-down menu, select the ***Yes (Do not allow to Split by Order with Products in this Product Category)*** option if you want the Product Category being created to contain the associated Products. Otherwise, if you don't want the Product Category being created to contain the associated Products, select the ***No (Allow to Split by Order with Products in this Product Category)*** option instead

<Image title="zRC26yi59m.png" alt={593} border={true} src="https://files.readme.io/06dd1dc-zRC26yi59m.png">
  Illustration (English)
</Image>

<Image title="xmTFrJiUpI.png" alt={707} border={true} src="https://files.readme.io/1f9bcb7-xmTFrJiUpI.png">
  Illustration (Vietnamese)
</Image>

### Create Association-Enabled Product Categories Using The Excel Import File

* In the Excel import file, input the basic information of the Product Categories following the rules in the main article [**Manage Product Categories**]()
* Then, for the **Associated Products** cell, input the value ***T*** (Acronym for ***True***)  if you want the Product Category being created to contain the associated Products. Otherwise, if you don't want the Product Category being created to contain the associated Products, input the value ***F*** (Acronym for ***False***) instead

## Create Products Of Association-Enabled Product Category

* After you have created the Association-enabled Product Categories, you can proceed to create the Products belonging to the Association-enabled Product Categories

### Create Associated Products Using The Webform

* When you use the Webform to create the Associated Products, make sure to select the appropriate Association-enabled Product Categories

### Create Associated Products Using The Excel Import File

* When you use the Excel import file to create the Associated Products, make sure to copy the Product Category Codes of the appropriate Association-enabled Product Categories on the Web app, then paste the copied Product Category Codes into the **Product Category Codes** cells in the file

## Create Orders Containing Associated Products

* Now you can proceed to create Orders that contain the Associated Products

### Create Orders Containing Associated Products Using The Webform

* When you use the Webform to create the Orders, as you select a Product that belongs to an Association-enabled Product Category, the system will automatically add the other Products that also belong to that Association-enabled Product Category into the Product table of the Order being created

### Create Orders Containing Associated Products Using The Excel Import File

* When you use the Excel import file to create the Orders containing Associated Products, you have to make sure to copy and paste the Product Codes of ***all*** the Associated Products in an Association-enabled Product Category into the **Product Code** cells in the file. The system will prevent importing the file if there are missing Associated Products
