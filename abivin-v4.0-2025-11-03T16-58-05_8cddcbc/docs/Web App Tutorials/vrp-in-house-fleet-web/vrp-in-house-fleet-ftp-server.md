---
title: FTP Server
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
> 🚧 At the moment, configurations described in this article are proprietary for one of our clients

## Activate FTP server connection

* Navigate to **Organizations > Organization List** tab
* Click on **Edit** :fa-pencil: icon of the top organization - The ***Manufacturer***

<Image title="erIkbeTIMd.png" alt={1920} className="border" border={true} src="https://files.readme.io/663054d-erIkbeTIMd.png" />

* On the **Organization Information** screen, click on **Use FTP** check box
* Click **Save** to confirm the change

<Image title="YCUySFf65r.png" alt={1920} className="border" border={true} src="https://files.readme.io/177f1cf-YCUySFf65r.png" />

## Pull orders from FTP server to second level branches

* Login with the administrator account of each branch
* Navigate to **Orders > Sales Orders** tab
* Click on :fa-download: icon on the toolbar
* On the **Sync from ERP** form, click on **Branch** field, select the appropriate branch from the drop down menu

<Image title="dsfd.png" alt={798} className="border" border={true} src="https://files.readme.io/e8d3e8d-dsfd.png" />

* Next, input data into **IP/Domain; Port; Username** and **Password** fields
* Click on **ERP/DMS Date** field, select the date the orders have been created on the FTP server from the drop down calendar. Then, click on **Delivery Date (vRoute)** field, select a date to execute these orders from the drop down calendar
* Click on **Pull**. The system will start pulling orders of all depot under the selected branch from FTP server to Abivin vRoute

<Image title="fsafđg.png" alt={1911} className="border" border={true} src="https://files.readme.io/760e691-fsafg.png" />

## Optimize routes for orders of second level branches

* After you have pulled the orders for the second level branches from FTP server to Abivin vRoute, you can proceed to optimize routes for those orders

<Image title="b3CAGbsGfV.png" alt={1920} className="border" border={true} src="https://files.readme.io/6979db5-b3CAGbsGfV.png" />

* After you have optimized routes, as you click on **Lock Route**, the **Push Data to ERP** form will appear. Input the FTP server information into the fields **IP or Domain; Port; Username; Password**, then click **Push** to push the route data to FTP server

<Image title="gla7o2sq0p.png" alt={1920} className="border" border={true} src="https://files.readme.io/dd71e06-gla7o2sq0p.png" />

## Consolidate optimized orders of second level branches

* After you have optimized and locked routes for the orders of all second level branches as described above, you can now consolidate those orders into one big order and pull to the first level distributor

## Enable Order Consolidation configuration

* Navigate to **Organizations > Organization List** tab
* Click on **Edit** :fa-pencil: icon of the ***Distributor*** that you want to set as the first level distributor

<Image title="SnnjjOQg1R.png" alt={1920} className="border" border={true} src="https://files.readme.io/f9ccb3d-SnnjjOQg1R.png" />

* On the **Organization Information** screen, click on **Order Consolidation** check box
* Click **Save** to confirm the change

<Image title="PuQ8cWQaEl.png" alt={1920} className="border" border={true} src="https://files.readme.io/253a472-PuQ8cWQaEl.png" />

## Setup Branch as Customer

* In order for the first level distributor to be able to pull data from the second level branches, you have to create customers whose ***Customer Code*** attributes are the same as ***Organization Code*** attributes of those branches. They will be under direct management of the first level depot

> ❗️ We currently support only ***nine*** branches

<Image title="cYQpIfpcbh.png" alt={1887} className="border" border={true} src="https://files.readme.io/a07f6dd-cYQpIfpcbh.png" />

## Setup first level Depot

* You have to create a first level depot under the direct management of the first level distributor. This depot will store products that will later be delivered to the second level branches

<Image title="HUweNeIxjk.png" alt={1920} className="border" border={true} src="https://files.readme.io/623ca8c-HUweNeIxjk.png" />

## Consolidate optimized orders of second level branches

* Navigate to **Orders > Sales Orders** tab
* Click on :fa-download: icon on the toolbar
* On **Sync from ERP** form, click on the **Branch** field, input the Organization Name of the ***First Level Distributor*** into the search bar, then select from the drop down menu

<Image title="k49Xy6jxN03.png" alt={1920} className="border" border={true} src="https://files.readme.io/96c1653-k49Xy6jxN03.png" />

* The **Sync from ERP** form will change to **Fetch orders from Branches** form
* Next, click on the :fa-calendar-o: icon under **Delivery Date (vRoute)** text. On the drop down calendar, you need to select the date on which the orders have been optimized and locked
* Next, click on the :fa-calendar-o: icon under **ERP/DMS Date** text. On the drop down calendar, you need to select the date on which the orders have been created on the FTP server
* Finally, click on **Pull** to begin consolidating orders from the second level branches into one big order and pull to the first level depot

> 📘 Even the ***missing orders*** - orders of the second level branches that were unable to be optimized, will also be consolidated into the big order pulled to the first level depot. This is to ensure that the first level depot supplies enough products for the second level branches

## Optimize routes for first level depot

* After the orders from second level branches have been consolidated and pulled to the first level depot, you can proceed to optimize routes for these orders
* **Note:** During the optimization process, you have to select the ***First level Distributor*** to optimize routes, instead of branches like usual

<Image title="1k6QJCsNoa.png" alt={1920} border={true} src="https://files.readme.io/2ad3265-1k6QJCsNoa.png">
  Choose the first level Distributor
</Image>

* After you have optimized routes, as you click on **Lock Route**, the **Push Data to ERP** form will appear. Input the FTP server information into the fields **IP or Domain; Port; Username; Password**, then click **Push** to push the route data to FTP server

## Rules when allocating orders

* The orders are allocated based on ***Volume*** attribute. If the volume of a big order exceeds the volume capacity of every available vehicles of the first level depot, it will automatically be split into smaller orders. The volume attribute of the split orders will be based on the volume capacity of the available vehicles, starting from the vehicle with the largest volume capacity
* One vehicle of the first level depot can deliver orders of multiple second level depot vehicles. On the other hand, orders of one vehicle of a second level depot can only be delivered by one single vehicle of the first level depot
