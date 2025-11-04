---
title: Configurations by Organization type
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
> ❗️ The configurations mentioned below are compulsory for this Model

## Configurations for Manufacturer

## API Key

* **API** stands for **Application Programming Interface**. In layman's terms, these interfaces are what allow software solutions to communicate with each other
* Since Abivin vRoute very frequently needs to work with other external ERP systems, this configuration provides an easy way to help the users set up the connection between these systems
* This configuration is present on tab **More Configurations** of the Manufacturer
* To generate an API key, click on the plus icon :fa-plus:. A random API key will be generated

<Image title="AvTc2lp9vH.png" alt={787} className="border" border={true} src="https://files.readme.io/d464518-AvTc2lp9vH.png" />

* You can copy that API key and paste into to the API of your external system (Usually in the header ***X-API-Key***). From then on, the API key will authenticate the API calls between your external system and Abivin vRoute system

<Image title="kDhWop6e5c.png" alt={364} className="border" border={true} src="https://files.readme.io/5074d2b-kDhWop6e5c.png" />

* After a while, if you decide to change the API key, you can click on the refresh icon :fa-undo: to generate a new API key

## Configurations for Transporter

### Shipment Type

* Section: **Mobile**
* Specify the Mode of transport for the shipments. With this model, you have to select the following mode: ***By Terminal Tractor***

![749](https://files.readme.io/85c7d44-Image_1.png "Image 1.png")

### Shipment Device ID Type

* Section: **Mobile**
* In this model, each terminal tractor is equipped with a mobile. The terminal tractor drivers will use the equipped mobiles to submit delivery tasks, instead of their own mobiles. The shipments, therefore, will need to be tracked by the vehicles (Terminal tractors), not by the users (Terminal tractor drivers). This configuration will help the dispatchers manage the shipments by vehicles and track the location of the vehicles.
* There are two options to track the device of each vehicle:
* Option 1: IMEI. The tablets equipped on the Terminal Tractors will be managed by their IMEIs
* Option 2: MAC Address. The tablets equipped on the Terminal Tractors will be managed by their MAC Addresses
* For detailed instruction, refer to the following article: [**Manage Terminal Tractors**](https://docs.abivin.com/docs/freight-transport-road-manage-truck-tractors)

![747](https://files.readme.io/a3f281e-image_2.png "image 2.png")
