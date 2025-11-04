---
title: Driver Assignment
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
* A vehicle needs to be assigned one driver to operate it
* There are certain conditions when assigning driver for vehicle:
* The drivers and the vehicles must be under the management of the **same Depot/Sun**
* One driver can be assigned to be the default driver for multiple vehicles
* The drivers and the vehicles must have the same Vehicle type attribute

<Embed url="http://g.recordit.co/tdl4T644oe.gif" title="null" favicon="null" image="http://g.recordit.co/tdl4T644oe.gif" iframe="true" provider="g.recordit.co" href="http://g.recordit.co/tdl4T644oe.gif" />

## Driver assignment before route optimization

## Assign default driver on Web form

* When you create or update vehicle on Web form, you can assign a default driver to that vehicle by clicking on **Default driver** field of the **Create vehicle/Update vehicle** form, then select a suitable driver code from the drop down menu
* Click **Update** to confirm the change
* The assigned driver will be automatically selected by default to operate that vehicle for every delivery tasks

<Image title="2019-10-15 11_15_12-Window.png" alt={712} className="border" border={true} src="https://files.readme.io/b8ca663-2019-10-15_11_15_12-Window.png" />

## Assign default driver on Excel template

* During the creation process of vehicles, you can assign default driver to a vehicle, provided that the user account of the driver has already existed on Web app
* To assign a default driver to a vehicle being created, copy the Username of the appropriate driver on Web app, then paste into **Default Driver** cell in the Excel template
* The Username can be found under **Username** column in **Organizations > User List** tab

<Image title="default driver.png" alt={1910} className="border" border={true} src="https://files.readme.io/badf739-default_driver.png" />

## Special case: Assign one default driver to multiple vehicles

* You can assign one default driver to multiple vehicles. In the scenario these vehicles are utilized at the same time during the route optimization process, the default driver will operate only one of these vehicles. You will have to manually assign other drivers to the rest of these vehicles

## Driver assignment during route optimization

## Vehicle has not been assigned default driver

* If a vehicle has not been assigned default driver, during route optimization, that vehicle will be assigned a random available driver, provided that the driver shares the same Vehicle type attribute with that vehicle
* After the route optimization process, if you want to assign a different driver to a vehicle, you can do so by:
* Click on the driver icon :fa-user: of that vehicle's route on the Timeline panel
* The **Assign to Driver** form will appear. Click on the **Driver** field, then select a suitable driver on the drop down menu
* Click **Assign** to confirm

<Image title="p5.png" alt={1361} className="border" border={true} src="https://files.readme.io/70f3557-p5.png" />

> ❗️ If the vehicle route has been locked, you will not be able to assign another driver for that vehicle

## Vehicle has been assigned default driver

* If a vehicle has been assigned a default driver, then all delivery tasks assigned to that vehicle will be operated by that default driver

<Image title="p7.png" alt={1918} className="border" border={true} src="https://files.readme.io/7ef80d4-p7.png" />

* If multiple vehicles have been assigned the same default driver, then during the route optimization process, only one of those vehicle will be operated by that default driver. Other vehicles will be assigned other available drivers
