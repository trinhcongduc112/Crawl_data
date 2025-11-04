---
title: Rental Vehicles
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
* In some days, one or more vehicles of the in-house fleet are not able deliver orders due to unexpected reasons. In this situation, the dispatchers might have to resort to temporarily renting external vehicles
* The rental vehicles are supposed to have the exact same properties as the in-house vehicles they temporarily replace
* In Abivin vRoute, we have introduced a work-around for this problem, using **Rental vehicles** configuration. In this article, we will be going through the steps of setting up rental vehicles, and optimizing routes for those vehicles

## Configure rental cost

* Navigate to **Transportation > Vehicle List** tab
* Click **Edit** :fa-pencil: icon of the vehicles you want to configure as rental vehicles
* Scroll down the **Update Vehicle** form, input the rental cost of the vehicle in the **Rental Cost** field
* Make sure that the **Active** check boxes of those vehicles are ticked
* Click **Update** to confirm the change
* Now, these vehicles would be identified as rental vehicles in Abivin vRoute system

<Image title="rental vehicle update.png" alt={791} className="border" border={true} src="https://files.readme.io/3617670-rental_vehicle_update.png" />

## Optimize routes with rental vehicles

* Perform route optimization as usual
* The rental vehicles will have additional suffixes in their vehicle codes: ***#1, #2*** etc. For example, an in-house vehicle with the vehicle code ***Truck\_01*** will be identified as ***Truck\_01 #1*** or ***Truck\_01 #2*** etc. (Depends on the delivery order) after being configured as rental vehicle

<Image title="rental vehicle.png" alt={1677} className="border" border={true} src="https://files.readme.io/11ef50f-rental_vehicle.png" />
