---
title: Request trailers and shipments
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
* To request a shipment, the driver needs to tap on the **Freight** tab.
* On the screen, there will be two sub tabs:

- **Container**: List of shipments need to be delivered
- **Trailer**: List of ready to use trailers

* The driver can swipe the mobile screen left or right to switch between these two sub tabs

<Image title="Untitled-1.png" alt={2160} className="border" border={true} src="https://files.readme.io/d570c38-Untitled-1.png" />

## Request trailer

* If the driver is operating a truck tractor without an attached trailer, he needs to request a trailer
* On **Trailer** sub tab, tapping directly on each trailer will lead the driver to the **Trailer Detail** screen.
* Here the driver can see essential information of the trailer, including:
* License Plate number of the trailer
* Trailer type
* Weight Level
* Location of the trailer
* The driver can swipe the list up and down to view all the available trailers 
* By checking the information of each trailer, the driver can then decide what trailer he wants to use, by tapping on **Request trailer** button at the bottom of the screen.

<Image title="request trailer.gif" alt={608} className="border" border={true} src="https://files.readme.io/9b6d5cb-request_trailer.gif" />

## Detach trailer

* After a trailer has been attached (or hooked) to the truck tractor, on **Shipments** tab, the trailer code will be displayed under the vehicle code. There will also be a yellow icon on the trailer row
* The driver can detach that trailer from the truck tractor by tapping on the yellow icon and tap **OK** on the pop-up message
* If there are containers on the trailer, the driver will not be able to detach the trailer

<Image title="Mobile - Detach trailer.gif" alt={608} className="border" border={true} src="https://files.readme.io/857c99c-Mobile_-_Detach_trailer.gif" />

## Request shipment

* The **Container** sub tab consists of the first containers appear in all available shipments.
* Tapping directly on each container will lead the driver to the **Container Detail** screen. 
* Here the driver can see essential information of the shipment, including:
* Seal number, Type, Length, Gross weight, Tare weight, Net weight (Unit: Tons)
* Start and End points of the shipment
* The driver can swipe the list up and down to view all the available containers
* By checking the information of each shipment, the driver can then decide what shipment he wants to deliver, by tapping on **Request container** button at the bottom of the screen.

<Image title="request cont.gif" alt={608} className="border" border={true} src="https://files.readme.io/243df0d-request_cont.gif" />

* During viewing and requesting shipment, the driver might encounter these alerts:
* ***Request failed. You are currently delivering another shipment, or are waiting for approval of another shipment.***: This announcement means that the driver is currently delivering/requesting, or has already been assigned a shipment, therefore he would be unable to request another shipment.
* ***Invalid location information!***: Some stop points of the shipment routes don't have coordinates (Latitude, Longitude) information. If the driver encounters this message, the driver should call the dispatcher to update these information.
* ***The truck tractor doesn't have an attached trailer, therefore is not eligible to request this container***: This means there isn't a TRAILER ATTACH event in the shipment being requested, and the truck tractor doesn't have an attached trailer. The driver needs to request a trailer first, or choose another shipment that has TRAILER ATTACH event

## Search shipment and trailer

* On the respective sub tabs, the driver can search for a specific shipment/trailer
* The driver can either type part of the shipment/trailer name onto the search field :fa-search:. The shipments/trailers with that name will appear

<Image title="search trailer.gif" alt={608} className="border" border={true} src="https://files.readme.io/6556b15-search_trailer.gif" />

## View shipments/trailers at a specific location

* To view all shipments/trailers at a specific location, the driver can tap on the **Map** icon next to the search field on the respective sub tabs. The driver will be directed to the location list, where he can choose a specific location. Upon choosing the location, the app will display all shipments/trailers at that location
* The driver can request trailer/shipment at a location by doing the steps described above

<Image title="trailer location.gif" alt={608} className="border" border={true} src="https://files.readme.io/77a12f6-trailer_location.gif" />
