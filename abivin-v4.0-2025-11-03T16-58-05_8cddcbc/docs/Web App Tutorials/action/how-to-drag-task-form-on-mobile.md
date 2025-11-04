---
title: How to drag task form on Mobile
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
There are four types of actions :

1. Product loading at main depot
2. Delivery
3. Go back to the warehouse
4. End of day.

![1317](https://files.readme.io/aaae69c-1.png "1.png")

## 1. Product loading at main depot

**Step 1 : Panel Setting**

* The first, select *Layout Component* - select *Panel*.
* At the *Display* tab, name the *Panel* in the *Title* section
* At the *API* tab, select *property name: orderList*\
  Custom Property section, follow the picture below 

![324](https://files.readme.io/87e2897-2.PNG "2.PNG")

Then click *Save* 

**Step 2 : Set up a table containing "Order Information"** 

* The first, select *Layout Components*, chọn *Table* 
* Select the information indexes (including line numbers and column numbers) of the table.
* In section *Basic Companents*, select *Text Field*, dragged into the newly created *Table*.
* For the newly created *Text Field*, name the *Text Fields* in the *Label* : Optional name according to customer requirements (eg Order code, Customer code, Customer name, Receipt, ...)

**Step 3 : Fill in the details of the items (Order Code, Customer Code, Customer Name, Receipt, ...)**

* For order code :\
  API tag : In the *Property Name*, insert *orderCode*. section *Custom Properties* , doing nothing.
* For Customer code:\
  API tag : In the *Property Name* , insert *customerInfo.customerCode* in the *Custom Properties* , doing nothing
* For Customer Name:\
  API tag: In the *Property Name* , insert *customerInfo.fullName*. section *Custom Properties* , doing nothing
* For Receivables:\
  API tag: In the *Property Name* , insert *totalPrice*. section  *Custom Properties* , doing nothing
* Then click *Save*.

**Step 4 : Create in the Check in and insert images via phone** 

* In the *Special Components* section , drag and drop file to the Panel. In Dispaly tab, named to the customer's preferences. For example, "Check In".
* In the *Validation* section, click on "Required"\
  The result will have a red star next to Check In (see illustration below).
* API tag: In the *Property Name* field, insert *undefinedCheckIn* (usually available - depending on the customer's choice)
* In the Custom Properties section (as shown below):\
  Key field, insert: *isHideSelectFromLibrary*\
  Value field, insert: *true*\
  The result: the shipper is required to take a photo in real time at the store for check-in, unable to obtain the photo available from the photo library.
* Then click Save

![617](https://files.readme.io/dea1188-3.png "3.png")

**Step 5: Creates the confirmation status of the goods.** 

* In the Layout Components section, select and drag the *Panel*
* At the Display tab, name the panel: "Confirm Status"
* At the API tab, stay the same.
* Then click Save.
* In the Basic Components section, select and drag the Check Box into the "Validate Status"
* At the Display tab, name each Checkbox.
* At the Validation tab, click the " Required" button.\
  The result will be a red star next to the checkboxes - illustrated below
* At the API tab, stay the same.

![608](https://files.readme.io/2fee294-4.png "4.png")

Finally, Click  SAVE VIEW at the bottom of the screen to complete the form creation process.

## 2. Delivery

 **Step 1 : Create the "Check in delivery"**       

* Select *Special Components* - drag and drop files into.
* At the *Display* tab,\
  Name "Check in Delivery" in the Label section. (Name depending on customer choice)\
  Click *Display as Images*,\
  At this point, the *Image Size* frame will appear 200. (image below)\
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

![622](https://files.readme.io/5774fba-5.PNG "5.PNG")

* At the *Validation* tab, click " Required"
* At the " API" tab, *Customer Properties*, follow the picture below\
  Key field, insert: isHideSelectFromLibrary\
  Value field, insert: true\
  The result: the shipper is required to take a photo in real time at the store for check-in, unable to obtain the photo available from the photo library.

![628](https://files.readme.io/bef979f-6.png "6.png")

Then click Save.

Step 2 : Update delivery status

* In the *Special Components* section, drag the container inside
* At the *Display* tab of the container, name the container in the *Label* (Example: "Update delivery status").
* At the *API* tab, in the *Custom Properties* section, follow the picture below:\
  The first key, insert: url.\
  The second key, insert: data\
  Value first, insert: orders / list. The second value, insert: \{}\
  Results: In the mobile application, the delivery section shows delivery status, including: Partial delivery, Full delivery and Not delivered together with order details and details of the amount entered.\
  (iIllustrated below)
* Then click SAVE VIEW

![623](https://files.readme.io/413260c-7.png "7.png")

![308](https://files.readme.io/fb8aa85-8.png "8.png")

![294](https://files.readme.io/341f2f8-9.png "9.png")

## 3. Go back to the warehouse

* The first, select *Special Components* , drag and drop the file into.
* In the *File Component*, at the *Display* tab:\
  Name "Check in warehouse" in the Label section. (Name depending on customer choice)\
  Click on \* *Display*as Images *,*&#x49;mage Size\* box will appear 200. (image below)
* At the Validation tab, click on Required
* At the API tab, Custom Properties, follow the image below\
  Key field, insert : isHideSelectFromLibrary\
  Value field, insert : true\
  The result: the shipper is required to take a photo in real time at the store for check-in, unable to obtain the photo available from the photo library.

![628](https://files.readme.io/6ecc611-10.png "10.png")

Finally, click SAVE VIEW at the bottom of the screen to complete the form creation process.

## 4. End of day

**Step 1: Create Check in finishes work day** 

* The first, select *Special Components* , drag and drop the file into.
* In the *File Component*, at the *Display* tab:\
  Name "Check in End of Day" in the Label section. (Name depending on customer choice)\
  Click **Display as Images**, at this point, the **Image Size** will appear 200. (image below)
* At the Validation tab, click Required.
* At the API tab, Custom Properties, follow the image below\
  Key field, insert: isHideSelectFromLibrary\
  Value field, insert: true\
  The result: the shipper is required to take a photo in real time at the store for check-in, unable to obtain the photo available from the photo library.

![630](https://files.readme.io/280eae4-11.png "11.png")

Step 2 : Set table confirm the status of the end of the working day

* In the Layout Components section, select and drag the panel
* At the Display tab, name the panel: "Update end date status"
* Then click Save
* In the Basic Components section, select and drag the Check Box into the "Date End Status Update"
* At the Display tab, name each Checkbox
* At the Validation tab, click the "Required" button.\
  The result will be a red star next to the checkboxes - illustrated below

![630](https://files.readme.io/7fdcbeb-12.png "12.png")

Finally, click SAVE VIEW at the bottom of the screen to complete the form creation process.
