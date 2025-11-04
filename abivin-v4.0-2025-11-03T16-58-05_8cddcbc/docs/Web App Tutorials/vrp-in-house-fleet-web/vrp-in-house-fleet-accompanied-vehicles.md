---
title: Accompanied Vehicles
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
* When a truck is performing multiple orders, there might be some roads on the delivery route that are too narrow for the truck to drive in. In situations like that, the dispatcher will have to resort to using smaller vehicle types such as motorbikes to accompany the truck fulfill the orders
* In Abivin vRoute, this feature is referred to as **Accompanied Vehicle**. To use this feature, please follow the steps below:
* Navigate to **Transportation > Vehicle List** tab
* Click on **Organizations** field on the toolbar, input the ***Organization Name*** of the Depot that will need the Accompanied Vehicle feature enabled into the search bar, then select from the drop down menu
* Click on the **Edit** :fa-pencil: icon of the selected ***Main trucks*** - Trucks that will be accompanied by other motorbikes
* On the **Update Vehicle** form, scroll down to the bottom. Click on **Accompanied Vehicle** field
* A drop down menu will show the list of all the motorbikes also managed by the Depot (Both Active and Inactive ones), in **Vehicle Code - License Plate** format. Select one or more motorbikes that will accompany the truck by clicking on the corresponding values
* Click **Update** to confirm

<Image title="accompany vehicle.gif" alt={1672} className="border" border={true} src="https://files.readme.io/52e87ea-accompany_vehicle.gif" />

* From now on, any route generated for the main trucks will also be generated for their accompanied motorbikes

> 🚧
>
> Make sure that the main trucks and their accompanied motorbikes are **Active** before performing route optimization. If all the accompanied motorbikes are **Inactive**, the routes will be generated for the main trucks only

* On the Timeline panel, there will be dotted lines between the icons of the main truck and the motorbikes that accompany it

<Image title="2019-11-04 11_57_08-Window.png" alt={899} className="border" border={true} src="https://files.readme.io/28be888-2019-11-04_11_57_08-Window.png" />

* When the dispatcher click on **Lock Route**, the optimized route will be sent to mobile accounts of  the main truck driver as well as the accompanied motorbike drivers
* The truck and motorbike drivers can then manually divide delivery tasks between themselves

<Image title="route accompany vehicle.gif" alt={1672} className="border" border={true} src="https://files.readme.io/858e3df-route_accompany_vehicle.gif" />
