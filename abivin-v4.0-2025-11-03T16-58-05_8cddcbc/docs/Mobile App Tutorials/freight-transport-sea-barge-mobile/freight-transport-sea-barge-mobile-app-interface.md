---
title: Mobile app user interface
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
## Main screen

* The screen of the app is divided into two main tabs:
* **Shipments**: List of shipments being performed or assigned. This is the default tab when the captain first logs in

<Image title="2019-08-18 15_29_02-BlueStacks.png" alt={1772} className="border" border={true} src="https://files.readme.io/94dae4d-2019-08-18_15_29_02-BlueStacks.png" />

* If the stop list of a shipment exceeds the screen, the captain can touch on the stop list then swipe left and right to see the whole stop list

<Image title="swipe left right.gif" alt={1705} className="border" border={true} src="https://files.readme.io/3552bcf-swipe_left_right.gif" />

* **History**: List of completed shipments, sorted in chronological order (Most recently completed shipment on top of the list)

<Image title="2019-08-18 15_29_20-BlueStacks.png" alt={1773} className="border" border={true} src="https://files.readme.io/fefe91b-2019-08-18_15_29_20-BlueStacks.png" />

## Shipment detail screen

* On **Shipments** tab, tap on **Detail >** of a specific shipment will lead to the details of that shipment

<Image title="Screenshot_10.png" alt={1018} className="border" border={true} src="https://files.readme.io/495f397-Screenshot_10.png" />

* The shipment detail screen is divided into four sections

<Image title="Screenshot_2019-08-01-17-47-40 v2.png" alt={1210} className="border" border={true} src="https://files.readme.io/698888f-Screenshot_2019-08-01-17-47-40_v2.png" />

## Section 1

* This is the top bar, consists of the following information and functions:
* Shipment Name
* Shipment Type: **Internal** or **External**
* Symbol :fa-arrow-left:: Go back to the shipment list screen
* **Map** symbol: Show the **Planned route** and the **Actual route** of the barge when operating that specific shipment

<Image title="2019-08-01 16_46_58-Window 2.png" alt={1222} className="border" border={true} src="https://files.readme.io/3d756fe-2019-08-01_16_46_58-Window_2.png" />

## Section 2

* This is the list of Stops in the shipment route, along with their basic information
* The list of stops will be ordered from left to right. If the stop list exceeds the screen, the captain can touch on the stop list then swipe left and right to see the whole stop list

<Image title="2019-08-18 17_47_05-BlueStacks.png" alt={1766} className="border" border={true} src="https://files.readme.io/691f3ae-2019-08-18_17_47_05-BlueStacks.png" />

* Each stop will have these information: 
* Name of the stop
* Type of the stop: 
* **Pick Stop** (Symbolized by :fa-download: icon and blue text): Stop where containers are picked up onto the barge
* **Drop Stop** (Symbolized by :fa-upload: icon and red text): Stop where containers are dropped off from the barge
* Type of the containers needed to be picked up or dropped off at each stop: Non-empty containers (Of both General Cargo Dry Container and Refrigerated Container; labeled by the letter **F** - short for **Full**); Non-empty Refrigerated Container (Labeled by the letter **RF** - short for **Reefer**); and Empty containers (Of both General Cargo Dry Container and Refrigerated Container; labeled by the letter **E** - short for **Empty**). Each type of container will have the quantities corresponding to these dimensions: **20 feet, 40 feet** and **45 feet** (Except for **RF** type which doesn't have 45 feet dimension)
* Estimated Arrival Date of the shipment
* Phone number of the person in charge at each stop

## Section 3

* This section contains a short note about the Shipment, filled by the dispatcher

<Image title="2019-08-18 17_49_41-.png" alt={1755} className="border" border={true} src="https://files.readme.io/32727e1-2019-08-18_17_49_41-.png" />

## Section 4

* This section consists of three sub tabs:

### Sub tab 1. Task list

* This is the list of tasks needed to be performed at each stop
* The captain can tap on :fa-chevron-circle-down: symbol to hide the task list of a stop, or :fa-chevron-circle-up: to show the task list

<Image title="task list.gif" alt={1705} className="border" border={true} src="https://files.readme.io/7d16f8e-task_list.gif" />

### Sub tab 2. Container

* Detail information of the containers needed to be picked/dropped at each stop. These information will be summarized and show at **Section 2** above
* The **Container Detail** information for each container will be hidden for Dummy shipment, and will be enabled for Actual shipment

<Image title="2019-09-13 13_52_46-Window.png" alt={1625} className="border" border={true} src="https://files.readme.io/b78ffdf-2019-09-13_13_52_46-Window.png" />

### Sub tab 3. BAY map

* Photo of the [**BAY map**](https://en.wikipedia.org/wiki/Stowage_plan_for_container_ships) (Actual photo or diagram)

<Image title="2019-08-01 18_04_33-Window.png" alt={1120} className="border" border={true} src="https://files.readme.io/a8bf56c-2019-08-01_18_04_33-Window.png" />

> 🚧
>
> The mobile app is currently optimized for tablet devices. Users can have some difficulties when using this app on devices with small screens
