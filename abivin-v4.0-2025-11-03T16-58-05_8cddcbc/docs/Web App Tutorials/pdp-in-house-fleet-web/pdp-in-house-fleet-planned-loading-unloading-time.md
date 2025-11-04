---
title: Planned Loading/Unloading time calculation
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
* In PDP model, the Planned Loading/Unloading time will be fixed numbers, regardless of the total number of pallets or total weight/volume of the orders. It will be based on the time configuration of the vehicle types for Palletized or Non-Palletized orders

## The order is configured as Palletized

* If the Order is configured as ***Palletized***, then both the Planned Loading time at the Origin Customer and the Planned Unloading time at the Destination Customer would take the value of the **Palletized Time** field of the vehicle type that performs that order
* For example: An order is performed by a vehicle of the vehicle type ***Truck 4000***. This vehicle type is configured to have the **Palletized Time** to be ***100 minutes*** and the **Non-Palletized Time** to be ***120 minutes***

<Image title="2019-10-02 17_20_00-Window.png" alt={1105} className="border" border={true} src="https://files.readme.io/e583af9-2019-10-02_17_20_00-Window.png" />

* The order assigned to a vehicle of this vehicle type is configured as ***Palletized***

<Image title="2019-10-02 17_23_51-Window.png" alt={1659} className="border" border={true} src="https://files.readme.io/d1a61f8-2019-10-02_17_23_51-Window.png" />

* During the route optimization process, the **Planned Loading time** at the Origin Customer and the **Planned Unloading time** at the Destination Customer would therefore take the **Palletized Time** value of the vehicle: ***100 minutes***

<Image title="2019-10-02 17_26_46-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/9be195f-2019-10-02_17_26_46-Window.png" />

## The order is configured as Non-Palletized

* If the Order is configured as ***Non-Palletized***, then both the Planned Loading time at the Origin Customer and the Planned Unloading time at the Destination Customer would take the value of the **Non-Palletized Time** field of the vehicle type that performs that order
* For example: An order is performed by a vehicle of the vehicle type ***Truck 4000***. This vehicle type is configured to have the **Palletized Time** to be ***100 minutes*** and the **Non-Palletized Time** to be ***120 minutes***

<Image title="2019-10-02 17_20_00-Window.png" alt={1105} className="border" border={true} src="https://files.readme.io/0405b5b-2019-10-02_17_20_00-Window.png" />

* The order assigned to a vehicle of this vehicle type is configured as ***Non-Palletized***

<Image title="2019-10-02 17_37_42-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/134c5b9-2019-10-02_17_37_42-Window.png" />

* During the route optimization process, the **Planned Loading time** at the Origin Customer and the **Planned Unloading time** at the Destination Customer would therefore take the **Non-Palletized Time** value of the vehicle: ***120 minutes***

<Image title="2019-10-02 17_36_23-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/a605e4a-2019-10-02_17_36_23-Window.png" />

<Image title="2019-10-02 17_28_46-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/57d1625-2019-10-02_17_28_46-Window.png" />
