---
title: Form Builder - Create forms for VRP model actions - backup
excerpt: >-
  In this article, we will be guiding you on creating some essential forms for
  the Actions of VRP model
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
* Based on the actual operation of each action, we will create the suitable forms for each action
* To avoid too many duplicate steps, please read the basic steps to integrate forms into actions at the **[Manage Actions](https://docs.abivin.com/docs/how-to-create-an-action#section-integrate-forms-into-actions-using-form-builder-tool)** article. Below we will just mention what components will be used, and what information will be input into those components
* We will have a demonstration GIF for each action to help you understand easier

## Create form for LOADING\_AT\_DEPOT action code

## Actual operation

* The action Loading products at Depot is the first action in a Delivery route
* The driver needs to see the list of orders he's going to deliver, details of each order (Order Code, Customer Code, Customer Name, Price of each order and Total Price of all orders that he needs to receive from the customer)
* The driver needs to perform a Check-In task upon his arrival at the Depot, by taking photo at the time of checking in
* The driver needs to confirm to have: 1. Taken out the products for the orders from the Depot onto the delivery vehicle; and 2. Checked out of the Depot to start the Delivery route

## Step 1: Create the display area for all orders

### Component

* Layout Components > Panel

### Input

* **Display** tab - **Title** field: Title of the form on Mobile app. Suggestion title: *Order list*
* **API** tab - **Property Name** field: Type *orderList*
* **API** tab - **Field Tags > Custom Properties** field: Type *url* in *Key* and */orders/list/ * in *Value*

## Step 2: Create table to contain information fields for each order

## Step 3: Create text fields

<Image title="4.png" alt={1358} src="https://files.readme.io/32cbf4e-4.png">
  Image 1: Click the images": [
      button
</Image>

Step 2: Drag the component in the left panel to the right area you want to create\
2.1 Order information form component\
2.1.1 Drag Panel component at the out Components] but button and drop into the right area

<Image title="h2.png" alt={1332} src="https://files.readme.io/5bf7650-h2.png">
  Image 2: Drag and drop a form component
</Image>

Input the component information as the picture below, then click the  butto button

<Image title="2.1.png" alt={1557} src="https://files.readme.io/bc2cdda-2.1.png">
  Image 3: Input the component information
</Image>

2.1.2 Drag Table component at the Components] button  button and drop into the Panel component created at 2.1.1

<Image title="2.1.2.png" alt={1331} src="https://files.readme.io/f80e736-2.1.2.png">
  Image 4: Drag and drops the Panel component
</Image>

Input the component information as the picture below, then click the ton:
[ button:

<Image title="h8.png" alt={1115} src="https://files.readme.io/e8b0547-h8.png">
  Image 5: Input the Table component information
</Image>

2.1.3 Drag Text Field component at the nents] button and  button and drop into the Table component created at 2.1.2 includes:

<Image title="2.1.3.png" alt={1335} src="https://files.readme.io/f63ee69-2.1.3.png">
  Image 6: Drag and drop the Text Field component
</Image>

Order Code: You input the component information as the picture below, then click the 
[bloc button:

<Image title="h11.png" alt={1678} src="https://files.readme.io/98f09c9-h11.png">
  Image 7: Input the Order Code component information
</Image>

Step 3: Create a delivery note: Drag the component in the left panel to the right area you want to create\
3.1 Product information form component\
3.1.1 Drag Panel component at the ts] button and drop button and drop into the right area

<Image title="2018-11-23_15-02-20.png" alt={1347} src="https://files.readme.io/33582fd-2018-11-23_15-02-20.png">
  Image 8: Drag and drop a form component
</Image>

Input the component information as the picture below, then click the ck:ima button

<Image title="2018-11-23_15-04-44.png" alt={879} src="https://files.readme.io/f1848e9-2018-11-23_15-04-44.png">
  Image 9: Input the component information
</Image>

3.1.2 Drag Well component at the button and drop int button and drop into the Panel component created at 3.1.1

<Image title="2018-11-23_15-12-49.png" alt={1347} src="https://files.readme.io/36d4c34-2018-11-23_15-12-49.png">
  Image 10: Drag and drops the Panel component
</Image>

Click the mage]
 button

![877](https://files.readme.io/439840d-2018-11-23_15-14-36.png "2018-11-23_15-14-36.png")

Step 4: Creat Check In: Drag the component in the left panel to the right area you want to create\
4.1 Check in information form component

![1323](https://files.readme.io/b31f75f-2019-01-29_11-46-01.jpg "2019-01-29_11-46-01.jpg")

Input the component information as the picture below, then click the 

![1618](https://files.readme.io/487c2bc-2019-01-29_12-01-06.jpg "2019-01-29_12-01-06.jpg")

Then click re form
[bl to save the entire form

## Create a component for the 'GIAO\_HANG' task action

## Create a component for the 'VE\_KHO' task action

## Create a component for the 'HET\_NGAY' task action

Step 1: Go to the lder] button , click the nents as the p button to add components as the picture below:

<Image title="2018-12-28_11-29-10.png" alt={1196} src="https://files.readme.io/5de9e64-2018-12-28_11-29-10.png">
  Image 1: Click the 
          "http button
</Image>

Step 2: Create a Goods receipt note: Drag the component in the left panel to the right area you want to create\
2.1 Product information form component\
2.1.1 Drag Panel component at the into the right area button and drop into the right area

<Image title="2018-12-28_12-04-16.png" alt={1347} src="https://files.readme.io/944cae1-2018-12-28_12-04-16.png">
  Image 2: Drag and drop a form component
</Image>

Input the component information as the picture below, then click the s": [
 button

<Image title="2018-12-28_12-06-50.png" alt={875} src="https://files.readme.io/e61d54c-2018-12-28_12-06-50.png">
  Image 3: Input the component information
</Image>

2.1.2 Drag Well component at the  the Panel componen button and drop into the Panel component created at 2.1.1

<Image title="2018-12-28_13-44-55.png" alt={1336} src="https://files.readme.io/230780b-2018-12-28_13-44-55.png">
  Image 4: Drag and drops the Panel component
</Image>

Click the [
     button

![877](https://files.readme.io/ed16ecc-439840d-2018-11-23_15-14-36.png "439840d-2018-11-23_15-14-36.png")

Step 3: Drag the component in the left panel to the right area you want to create\
3.1 Order information form component\
3.1.1 Drag Panel component at the  right area
[block: button and drop into the right area

<Image title="2018-12-28_14-09-13.png" alt={1337} src="https://files.readme.io/765cbce-2018-12-28_14-09-13.png">
  Image 5: Drag and drop a form component
</Image>

Input the component information as the picture below, then click the  
   button

<Image title="2018-12-28_14-22-30.png" alt={1743} src="https://files.readme.io/34e8f4c-2018-12-28_14-22-30.png">
  Image 6: Input the component information
</Image>

3.1.2 Drag Table component at the el component create button and drop into the Panel component created at 3.1.1

<Image title="2018-12-28_15-50-41.png" alt={1328} src="https://files.readme.io/cf54f67-2018-12-28_15-50-41.png">
  Image 7: Drag and drops the Panel component
</Image>

Input the component information as the picture below, then click the 
      button:

<Image title="2018-12-28_15-33-04.png" alt={1301} src="https://files.readme.io/2ff306a-2018-12-28_15-33-04.png">
  Image 8:  Input the Table component information
</Image>

3.1.3 Drag Text Field component at the mponent created at button and drop into the Table component created at 3.1.2 includes:

<Image title="2018-12-28_16-26-26.png" alt={1333} src="https://files.readme.io/d5fb77e-2018-12-28_16-26-26.png">
  Image 9: Drag and drop the Text Field component
</Image>

Order Code: You input the component information as the picture below, then click the    "im button:

<Image title="98f09c9-h11.png" alt={1678} src="https://files.readme.io/7616152-98f09c9-h11.png">
  Image 10: Input the Order Code component information
</Image>

## Create a component for the 'EXTRA TASK' task action

Step 1: Go to the onents as the, click the ow:
[block:ima button to add components as the picture below:

<Image title="2019-02-15_09-36-37.jpg" alt={1185} src="https://files.readme.io/2915f22-2019-02-15_09-36-37.jpg">
  Image 1: Click the readme.io/2915 button
</Image>

Step 2: Create Check in: Drag the component in the left File to the right area you want to create\
2.1  Composition of photos

<Image title="2019-02-15_16-19-50.jpg" alt={1882} src="https://files.readme.io/d1241aa-2019-02-15_16-19-50.jpg">
  Image 2: Drag and drop a form component
</Image>

Input the component information as the picture below, then click the ": [
  button

<Image title="2019-02-15_17-33-05.jpg" alt={2330} src="https://files.readme.io/b11d0e4-2019-02-15_17-33-05.jpg">
  Image 3: Input the component information
</Image>

Step 3: Create Extra type: Drag the component in the left Radio to the right area you want to create\
3.1  Extra type form component

<Image title="2019-02-15_17-45-00.jpg" alt={1877} src="https://files.readme.io/58e834a-2019-02-15_17-45-00.jpg">
  Image 4: Drag and drop a form component
</Image>

Input the component information as the picture below, then click the [
     button:

<Image title="2019-02-15_17-53-21.jpg" alt={2183} src="https://files.readme.io/4018cee-2019-02-15_17-53-21.jpg">
  Image 5: Input the component information
</Image>

Step 4: Create Description: Drag the component in the left Text Field to the right area you want to create\
4.1  Description form component

<Image title="2019-02-15_18-00-51.jpg" alt={1316} src="https://files.readme.io/ece98db-2019-02-15_18-00-51.jpg">
  Image 6: Drag and drop a form component
</Image>

Input the component information as the picture below, then click the        button:

<Image title="2b970df-2019-02-19_17-36-45.jpg" alt={1313} src="https://files.readme.io/dda049e-2b970df-2019-02-19_17-36-45.jpg">
  Image 7: Input the component information
</Image>

Step 5: Create Cost: Drag the component in the left Number to the right area you want to create\
5.1  Cost form component

<Image title="2019-02-18_09-45-20.jpg" alt={1892} src="https://files.readme.io/cc8e5a8-2019-02-18_09-45-20.jpg">
  Image 8: Drag and drop a form component
</Image>

Input the component information as the picture below, then click the   "htt button:

<Image title="2019-02-18_09-51-34.jpg" alt={2455} src="https://files.readme.io/5f45b6b-2019-02-18_09-51-34.jpg">
  Image 9: Input the component information
</Image>