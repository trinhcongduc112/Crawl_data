---
title: ERP System
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
* In Abivin vRoute, we have set up an API to enable our partners to connect to other Enterprise Resource Planning (ERP) or Distributor Management System (DMS) systems and fetch the customer and orders data into Abivin vRoute database

## Activate ERP configuration

* To get data from external ERP system using the API, please follow the steps below:
* Log in with the ***top administrator account***
* Navigate to **Organizations > Organization List** tab
* Click on **Edit** :fa-pencil: icon of the top organization - The ***Manufacturer***

<Image title="0229788-2019-11-04_09_38_23-Window.png" alt={1913} className="border" border={true} src="https://files.readme.io/fdce6d4-0229788-2019-11-04_09_38_23-Window.png" />

* On the **Organization Information** screen, click on the **ERP** check box to activate the ERP API
* Click **Save** to confirm the change

<Image title="2019-11-05 16_36_58-Window.png" alt={1893} className="border" border={true} src="https://files.readme.io/02191eb-2019-11-05_16_36_58-Window.png" />

> ❗️ The **ERP** configuration is proprietary for only one of our clients

## Pull customer list data

* Navigate to **Partners > Customer List** tab
* You will notice there's a new :fa-download: button on the toolbar. That's the **Sync from ERP** button

<Image title="2019-11-05 16_48_38-Window.png" alt={1907} className="border" border={true} src="https://files.readme.io/0d6264d-2019-11-05_16_48_38-Window.png" />

* Click on that button, the **Sync from ERP** form will appear
* Click on the **Branch** field and select the Branch to which you want to pull the customer data 
* Next, input the IP/Domain address, the Username, Password of the ERP system into **IP/Domain, Username** and **Password** fields
* Next, click on the **ERP/DMS Date** field to select the date when you want to pull the customer data
* The **Check warehouse code (parent\_ID)** check box is optional. If you enable it, the system will compare the ***parent\_ID*** field of the customer data on ERP system against the available customer data on Abivin vRoute and will announce if there are unmatched parent IDs. If you don't enable it, the pulling process will always complete without checking the data accuracy
* Finally, click on **Pull** to start pulling customer data from the ERP system into Abivin vRoute

<Image title="2019-11-05 16_58_21-Window.png" alt={786} className="border" border={true} src="https://files.readme.io/4be238c-2019-11-05_16_58_21-Window.png" />

## Pull orders

* Navigate to **Orders > Sales Order** tab
* Similarly to **Partners > Customer List** tab, you will notice there's a new :fa-download: button on the toolbar to sync order data from the ERP system

<Image title="2019-11-05 17_33_38-Window.png" alt={1896} className="border" border={true} src="https://files.readme.io/a60bb89-2019-11-05_17_33_38-Window.png" />

* Click on that button, the **Sync from ERP** form will appear
* Click on the **Branch** field and select the Branch for which you want to pull the order data 
* Next, input the IP/Domain address, the Username, Password of the ERP system into **IP/Domain, Username** and **Password** fields
* Next, you have two options: Pull failed orders - Orders that have been pulled to Abivin vRoute from previous days, but were failed to deliver, or Pull new orders - Orders that have just been recently created on ERP system and have not been pulled to Abivin vRoute

<Image title="2019-11-05 17_37_10-Window.png" alt={793} className="border" border={true} src="https://files.readme.io/678c7bc-2019-11-05_17_37_10-Window.png" />

## Pull failed orders from previous days

* If you want to pull failed orders, first click on **Get Failed Orders Date** field, select a previous date from the drop down calendar. Next, click on **Delivery Date (vRoute)** field, select a new date to redeliver those orders. Then click on **Get Failed Order** button to start retrieving the failed orders
* Abivin vRoute will scan the orders delivered on the selected previous date, and retrieve orders that were failed to deliver on that date, and plan to the selected new date
* You can gather failed to deliver orders from multiple previous days

<Image title="2019-11-05 17_58_00-Window.png" alt={1903} className="border" border={true} src="https://files.readme.io/57269cb-2019-11-05_17_58_00-Window.png" />

## Pull new orders

* If you want to pull new orders, first click on **ERP/DMS Date** field, select the date when the orders were created on the ERP system from the drop down calendar. Next, click on **Delivery Date (vRoute)** field, select a date to delivery those orders. Then click on **Pull** button to start pulling the new orders
* Abivin vRoute will pull orders from the ERP system and plan to the selected delivery date

<Image title="2019-11-05 18_05_46-Window.png" alt={1892} className="border" border={true} src="https://files.readme.io/615767a-2019-11-05_18_05_46-Window.png" />
