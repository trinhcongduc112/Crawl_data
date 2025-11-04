---
title: Multimodal transport
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
* Multimodal transport is the transportation of freights that are performed with at least two different modes of transport. In Abivin vRoute Freight transport models, multimodal transport is the combination of two modes of transport: ***Truck tractor*** and ***Barge***
* The External Transportation Management system will create orders. An order will have a distinct Order Release Code, which applies to all containers that belong to that order so that the dispatcher can track the movement of the containers
* To get to the ultimate customer, a container might need to be carried by multiple consecutive shipments. In each shipment, the container will be assigned a ***Leg Position*** - a number (From ***0*** to ***9***) to indicate the chronological order by which the shipments must be executed
* After the shipments have been created from the External Transportation Management system and pushed to Abivin vRoute, the dispatcher can check the chronological order of the shipments by following the below steps:
* First, look at the number under **Leg Index** column. The shipment with the lower leg index must be performed before the shipments with greater leg indexes

<Image title="shipment leg index.png" alt={1912} className="border" border={true} src="https://files.readme.io/126544b-shipment_leg_index.png" />

* Next, click on the container number under **Total Containers** column

<Image title="container number.png" alt={1912} className="border" border={true} src="https://files.readme.io/8846f38-container_number.png" />

* The **Shipment Details** screen will appear. Here you can view in details all containers carried in a particular shipment

<Image title="shipment container.png" alt={1492} className="border" border={true} src="https://files.readme.io/93a1c18-shipment_container.png" />

* You can filter the containers which have the same Booking Number by clicking on a specific Booking Number under **Booking Number** column

<Image title="bol cont.png" alt={1488} className="border" border={true} src="https://files.readme.io/6474d91-bol_cont.png" />

* You can download the list of booking numbers of that shipment to an Excel template to view offline by clicking on **Download** button

<Image title="bol cont.png" alt={1488} className="border" border={true} src="https://files.readme.io/57fe027-bol_cont.png" />
