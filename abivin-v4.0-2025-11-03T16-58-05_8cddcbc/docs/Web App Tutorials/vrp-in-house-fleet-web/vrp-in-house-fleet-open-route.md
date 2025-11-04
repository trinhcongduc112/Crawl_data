---
title: Open Route
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
## Open Route Definition

* By default, the delivery fleet is set to return to the manufacturing warehouses after they have completed the delivery tasks, making their Delivery Routes ***Closed Routes*** (Delivery Routes in which the vehicles start and finish at the manufacturing warehouses)
* You can set the delivery fleet to finish their Delivery Routes at the last customer location instead of traveling back to the manufacturing warehouses. These Delivery Routes are defined as ***Open Routes*** 

## Compulsory Configuration

* Navigate to the tab **Organizations > Organizations**
* Click the icon **Edit** :fa-pencil: of the **Branch**
* On the form **Update Organization**, navigate to the sub-tab **More Configuration > Algorithm**. Scroll down this section and tick the check box **Open Route**
* Click **Save** to confirm the change

<Image title="l9CeRg9nW5.png" alt={748} className="border" border={true} src="https://files.readme.io/816ace1-l9CeRg9nW5.png" />

## Route Plan Optimization

* When the configuration **Open Route** is not enabled, the delivery vehicle is planned to travel back to the manufacturing warehouse after the last customer, like so:

<Image title="closed route.png" alt={1920} src="https://files.readme.io/f21a8be-closed_route.png">
  Closed Route
</Image>

* When the configuration **Open Route** is enabled, the delivery vehicle is planned to stop at the last customer location, like so:

<Image title="open route.png" alt={1920} border={true} src="https://files.readme.io/9e8d8b2-open_route.png">
  Open Route
</Image>
