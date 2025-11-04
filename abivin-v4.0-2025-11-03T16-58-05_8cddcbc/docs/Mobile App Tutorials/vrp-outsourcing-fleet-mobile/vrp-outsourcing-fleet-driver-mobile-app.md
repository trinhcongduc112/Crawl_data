---
title: Driver (Delivery men)
excerpt: >-
  This article will guide the driver on how to perform delivery tasks on the
  Mobile app
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
* You are the driver (Delivery man) of the Transporter. Below we will guide you on how to perform your tasks on the Mobile App

## Sign in

* When you sign in on the Mobile app to get the task assigned, you will be greeted with a screen showing what vehicle you would be operating

<Image title="sign in.gif" alt={420} className="border" border={true} src="https://files.readme.io/8af839a-sign_in.gif" />

* On the **Tasks** tab will show the list of all delivery routes you need to perform
* Each route consists of several tasks: ***Load products at Depot, Deliver products to customer*** and ***Come back to Depot, end the working day***
* You can tap on the task title to move to the task screen, where you need to perform several actions and submit the task

<Image title="task title.png" alt={836} className="border" border={true} src="https://files.readme.io/37b60ec-task_title.png" />

* You need to perform the tasks in the correct sequence displayed on the app screen
* If the tasks are in a different date, you can tap on the icons :fa-chevron-left: and :fa-chevron-right: to go to the appropriate date. You can also tap directly on the date and choose the appropriate date from the pop out calendar

<Image title="mobiledate.png" alt={420} className="border" border={true} src="https://files.readme.io/0a753c3-mobiledate.png" />

<Image title="mobiledatecalendar.png" alt={830} className="border" border={true} src="https://files.readme.io/319f370-mobiledatecalendar.png" />

## 1. Perform "Loading at Depot" task

## View order information

* In this task, you come to the Depot to check in, load products on to the vehicle that you have been assigned with
* You can view the orders needed to be delivered by tapping on the icon :fa-caret-up: on **Order Information** bar

<Image title="orderinfo.png" alt={425} className="border" border={true} src="https://files.readme.io/5cb5f09-orderinfo.png" />

## Check in at Depot

* You must first perform **Check-In** task, proving that you have come to the Depot, by taking photo of the Depot
* There might be two options to perform the Check In task

### Check In by picture

* If you see a camera icon :fa-camera:, you will need to take a photo of the current location, by tapping on that icon then take picture
* The Mobile app will gather the exact time and location information as you take the Check In photo. A warning will display if the Check in location is too far from the Depot location (The default value is set to 200 meters from the Depot)

<Image title="check in photo.png" alt={413} className="border" border={true} src="https://files.readme.io/ce68f7b-check_in_photo.png" />

### Check In by location coordinate

* If you see a location mark icon :fa-map-marker:, tap on that icon. The Mobile app will gather the coordinate information of the location where you are currently standing

<Image title="check in coordinate.png" alt={417} className="border" border={true} src="https://files.readme.io/4702378-check_in_coordinate.png" />

## Confirm product loading status and check out of Depot

* Next, you need to confirm to have ***taken the products out of the Depot*** and ***checked out of the Depot***, ready to deliver, by tapping on the icon :fa-toggle-off: on the corresponding rows, turning that icon into :fa-toggle-on:

<Image title="confirm.png" alt={411} className="border" border={true} src="https://files.readme.io/b24e075-confirm.png" />

* You can then tap on **Submit** on the top right of the screen to send the task to the dispatcher on Web app

<Image title="submit task.png" alt={420} className="border" border={true} src="https://files.readme.io/9473721-submit_task.png" />

* Below is an animated illustration of the whole task

<Image title="Loading at depot.gif" alt={420} className="border" border={true} src="https://files.readme.io/ef0dfed-Loading_at_depot.gif" />

## 2. Perform "Deliver products" task

* In this task, you will travel to the customer warehouse/store to deliver products
* Before traveling to the customer warehouse/store, you can call the customer to ensure they are opening by tapping on the icon :fa-phone: on the **Phone number** row
* You can tap on the icon :fa-share-square: on the **Address row** to view the direction from your current location to the customer warehouse/store

<Image title="customerphone.png" alt={413} className="border" border={true} src="https://files.readme.io/359167f-customerphone.png" />

<Image title="2019-08-27 23_25_18-Window.png" alt={419} className="border" border={true} src="https://files.readme.io/b02893b-2019-08-27_23_25_18-Window.png" />

## Check in at customer warehouse/store

* Upon arriving at the customer warehouse/store, you need to Check-In by taking photo of the customer store/warehouse
* [The instruction is similar as when you check in at your Depot](https://docs.abivin.com/docs/vrp-in-house-fleet-driver-mobile-app#section-check-in-at-depot)

## Select delivery result

* There are three possible results for the delivery status of an order: 
* **Completed**: The order is completed, all product cases/items have been delivered to customer successfully
* **Partly Delivered**: Some, not all product cases/items have been delivered to customer
* **Not Completed**: None of the product cases/items have been delivered to customer

<Image title="reason.png" alt={398} className="border" border={true} src="https://files.readme.io/d3c52d9-reason.png" />

### Completed result

* If the Delivery result is **Completed**, you can specify the actual amount of money received from the customer by tapping on the money value on **Collected** row, input the correct value on the numerical keyboard, then tap on **Done**

<Image title="completedamount.png" alt={419} className="border" border={true} src="https://files.readme.io/facb76f-completedamount.png" />

### Partly Delivered result

* If the Delivery result is **Partly Delivered**, you will need to specify the quantity of product cases/items that have actually been delivered, as well as the actual amount of money received from the customer
* To specify the quantity of product cases/items that have actually been delivered, tap on the number value next to the text **Actual** in **Product Detail** section

<Image title="partlyamount.png" alt={422} className="border" border={true} src="https://files.readme.io/3418ffe-partlyamount.png" />

* A form will appear. On this form, on the left side is where you select the quantity of product cases actual delivered; on the right side is where you select the quantity of product items actually delivered . To select, swipe the product cases/product items number up or down until the appropriate values are selected on the screen. After you have selected the correct value(s), tap on **Confirm**

<Image title="actualcaseitem.png" alt={422} className="border" border={true} src="https://files.readme.io/002d9bf-actualcaseitem.png" />

* If the product you deliver comes from multiple product lots, repeat the steps above for all product lots

<Image title="product lot.png" alt={416} className="border" border={true} src="https://files.readme.io/c964475-product_lot.png" />

* Next, specify the actual amount of money that you have received from the customer by tapping on the money value on **Collected** row, input the correct value on the numerical keyboard, then tap on **Done**, similar to when you select **Completed** result above

### Not Completed result

* If the delivery result is **Not Completed**,  you need to select a reason as to why the order was not delivered from a list of available reasons by tapping on the text **Select Reason** below the **Not Completed** option. You will be directed to a screen, listing the reasons. Tap on the appropriate reason to select it

<Image title="select reason.png" alt={866} className="border" border={true} src="https://files.readme.io/303050a-select_reason.png" />

* If there are multiple reasons, you can tap on the search icon :fa-search:, input a part of the reason you want to find into the search bar in order to filter faster 

<Image title="find reason.png" alt={422} className="border" border={true} src="https://files.readme.io/a609f90-find_reason.png" />

## Confirm to have received the commercial bill

* Next, you need to confirm to have ***received the commercial bill from the customer*** , by tapping on the icon :fa-toggle-off: on the corresponding row, turning that icon into :fa-toggle-on:

<Image title="bill.png" alt={407} className="border" border={true} src="https://files.readme.io/ac87688-bill.png" />

## (Optional) Get customer signature for Delivery notes

* You might have to get the customer signature, confirming that they have received the products
* The signature can be had in a digital form by tapping on **Signature** :fa-pencil: icon
* The customer can sign directly on the Mobile screen using his finger. He can reset the signature to sign again by tapping on **Reset** on the signature screen. When the signature is correct, he can tap on **Save**

<Image title="deliver product.gif" alt={420} className="border" border={true} src="https://files.readme.io/b5def14-deliver_product.gif" />

* Finally, you can tap on **Submit** on the top right of the screen to submit this task

## 3. Comes back to the Depot, perform "End of Day" task

* In this task, you come back to the Depot after completing the deliveries to return undelivered products as well as perform other necessary procedures

## Check in at Depot

* You need to **Check in** upon your come back to the Depot
* [The instruction is similar as when you check in at your Depot](https://docs.abivin.com/docs/vrp-in-house-fleet-driver-mobile-app#section-check-in-at-depot)

## Confirm to have handed over returned products and submitted collected cash

* You need to confirm to have ***handed all returned products to the warehouse manager/keeper*** and ***submitted all collected cash to the accountant*** by tapping on :fa-toggle-off: icon on the corresponding rows

- Finally, you can tap on **Submit** on the top right of the screen to submit this task
- Below is an animated illustration of the whole task

<Image title="end of day.gif" alt={420} className="border" border={true} src="https://files.readme.io/be22844-end_of_day.gif" />

## Optional functions

## Get notified when the route dispatcher makes changes to the delivery route

* In the scenario the route dispatcher makes some changes to your delivery route, you will be notified on the Mobile app

## View order note (remark)

* If the dispatcher input a short note for the order you are delivering, you can view the note of that order in the **Remark** section of the **Delivery products** task

<Image title="remark.png" alt={420} className="border" border={true} src="https://files.readme.io/1246f44-remark.png" />
