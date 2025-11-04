---
title: Vehicle Usage History
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
* Abivin vRoute system will keep track of how the Vehicles are utilized in the Route Plan optimization process. This article will show you how to view the Vehicle usage history.
* The Vehicle usage history can be accessed through two viewing modes:
* 1 - The default List View mode
* 2 - A more visual viewing mode called Gantt View

## Vehicle Usage History (List View)

* The **Transportation > Vehicles** tab is displayed in the List View mode by default.

<Image title="1. Default (ENG).png" alt={1920} border={true} src="https://files.readme.io/0c804d8-1._Default_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Default (VIE).png" alt={1920} border={true} src="https://files.readme.io/ebc5771-1._Default_VIE.png">
  Illustration (Vietnamese)
</Image>

* In this viewing mode, you can see the usage history of a particular Vehicle by clicking its corresponding **Vehicle History** icon under the **Actions** column.
* As you click this icon, the **Vehicle History** panel will appear on the right side of the screen.

<Image title="1. List View (ENG) 2.gif" alt={1728} border={true} src="https://files.readme.io/2e4dba3-1._List_View_ENG_2.gif">
  Illustration (English)
</Image>

<Image title="1. List View (VIE) 2.gif" alt={1728} border={true} src="https://files.readme.io/3b98af7-1._List_View_VIE_2.gif">
  Illustration (Vietnamese)
</Image>

* By default, this panel will show the usage history of the Vehicle during the most recent 30 days
* To change the date range, click on the date field. On the drop-down calendar, select the new date range (**Note:** You can only select a maximum of 30 days).

<Image title="2. Vehicle List (ENG).png" alt={1920} border={true} src="https://files.readme.io/743d3b3-2._Vehicle_List_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Vehicle List (VIE).png" alt={1920} border={true} src="https://files.readme.io/214d192-2._Vehicle_List_VIE.png">
  Illustration (Vietnamese)
</Image>

* If during the selected date range, the Vehicle is utilized in some Route Plans, then its assigned Delivery Shifts will appear below.
* Three information of the Delivery Shifts are displayed: 
* 1 - Their Planned Start and Stop Time.
* 2 - Their names in the Route Plan.
* 3 - Their current Planning Status in the Route Plan.

<Image title="3. Vehicle Info (ENG).png" alt={504} border={true} src="https://files.readme.io/a6c7f26-3._Vehicle_Info_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Vehicle Info (VIE).png" alt={502} border={true} src="https://files.readme.io/55a034d-3._Vehicle_Info_VIE.png">
  Illustration (Vietnamese)
</Image>

* If you click on a Delivery Shift name, you will be directed to a new web browser tab showing the Route Plan (Map View). The Delivery Shift will be selected on the Map View.

<Image title="6. Vehicle List Map (VIE).gif" alt={1728} border={true} src="https://files.readme.io/996d9fe-6._Vehicle_List_Map_VIE.gif">
  Illustration (English)
</Image>

<Image title="6. Vehicle List Map (VIE) 2.gif" alt={1728} border={true} src="https://files.readme.io/176336b-6._Vehicle_List_Map_VIE_2.gif">
  Illustration (Vietnamese)
</Image>

## Vehicle Usage History (Gantt View)

* Apart from the default list view, you can also view the usage history of the Vehicles in a more visual mode called **Gantt View**.
* To access the Gantt View mode, click the **Show History** icon :fa-align-justify: on the toolbar.

<Image title="Use Gantt View 2.png" alt={1919} border={true} src="https://files.readme.io/0f61d74-Use_Gantt_View_2.png">
  Illustration (English)
</Image>

<Image title="Use Gantt View.png" alt={1909} border={true} src="https://files.readme.io/da9a533-Use_Gantt_View.png">
  Illustration (Vietnamese)
</Image>

* To get back to the List View mode, click the **Show List** icon :fa-list-ul: on the toolbar.

<Image title="11. List (ENG).png" alt={1920} border={true} src="https://files.readme.io/e521cd1-11._List_ENG.png">
  Illustration (English)
</Image>

<Image title="11. List (VIE).png" alt={1920} border={true} src="https://files.readme.io/545bd43-11._List_VIE.png">
  Illustration (Vietnamese)
</Image>

* Generally, the Gantt View mode consists of three sections:
* 1 - The Vehicle Planning Status Bar.
* 2 - The Vehicle Information Table.
* 3 - The Vehicle Usage History Gantt Chart.

<Image title="1. New Board (ENG).png" alt={1920} border={true} src="https://files.readme.io/b81ffa3-1._New_Board_ENG.png">
  Illustration (English)
</Image>

<Image title="1. New Board (VIE).png" alt={1920} border={true} src="https://files.readme.io/6e77586-1._New_Board_VIE.png">
  Illustration (Vietnamese)
</Image>

### Vehicle Planning Status Bar

* The Vehicle Planning Status Bar explains the color codes of the Vehicles' Delivery Shifts on the Gantt chart according to their current Planning Status. There are three colors:
* Blue color means the Planning Status of the Delivery Shift is ***Locked***.

<Image title="Locked (Color).png" alt={219} className="border" border={true} src="https://files.readme.io/701360b-Locked_Color.png" />

* Yellow color means the Planning Status of the Delivery Shift is ***Planned***.

![218](https://files.readme.io/bf71818-Planned_Color.png "Planned (Color).png")

* Green color means the Planning Status of the Delivery Shift is ***Finalized***.

![219](https://files.readme.io/2a80c45-Finalized_Color.png "Finalized (Color).png")

### Vehicle Information Table

* The Vehicle Information Table comprises of three following columns:
* 1 - Vehicle Code
* 2 - Vehicle Type
* 3 - License Plate
* After a new Vehicle is created, it will be listed on top of the table.
* On this table, you are able to perform certain operations like on the List View mode:
* Bulk update multiple Vehicles.

<Image title="8. Bulk Update (ENG).png" alt={1920} border={true} src="https://files.readme.io/2800f3d-8._Bulk_Update_ENG.png">
  Illustration (English)
</Image>

<Image title="8. Bulk Update (VIE).png" alt={1920} border={true} src="https://files.readme.io/6c4faaf-8._Bulk_Update_VIE.png">
  Illustration (Vietnamese)
</Image>

* Edit Vehicle; Show Vehicle history panel; Delete Vehicle. These three functions are grouped into the three vertical dots icon :fa-ellipsis-v: at the right end of the Vehicle row on the table.

<Image title="4. Dot (ENG).png" alt={1732} border={true} src="https://files.readme.io/cc59f41-4._Dot_ENG.png">
  Illustration (English)
</Image>

<Image title="4. Dot (VIE).png" alt={1729} border={true} src="https://files.readme.io/80565b8-4._Dot_VIE.png">
  Illustration (Vietnamese)
</Image>

### Vehicle Usage History Gantt Chart

* The Gantt chart will visually depict the usage history of the Vehicles during a certain date range
* By default, the Gantt chart will only show the current date. To select another date range, please click on the date field on the toolbar then select an appropriate date range (Note: You cannot select more than 30 days).

<Image title="2. Date Range (ENG).png" alt={1920} border={true} src="https://files.readme.io/c68899c-2._Date_Range_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Date Range (VIE).png" alt={1920} border={true} src="https://files.readme.io/3fa4810-2._Date_Range_VIE.png">
  Illustration (Vietnamese)
</Image>

* The length and the height of the Gantt chart might exceed the length and height of your screen. If that happens, you can use the horizontal and vertical scrollbar

- If during the selected date range, the Vehicles are used in the Route Plans, then their Delivery Shifts will appear in the chart in the form of the horizontal colored bars. The colors of the bar are explained in the [Vehicle Planning Status Bar](https://docs.abivin.com/docs/vrp-dc-vehicle-usage-history#vehicle-planning-status-bar) section.
- The length of the bar equals the length of the corresponding Delivery Shift on the Plan Timeline panel (Not the Execution Timeline panel) The beginning and the end of the bar mark the beginning and the end timestamps of the Delivery Shift.
- When you hover the mouse onto a bar, you will see the following information of the Delivery Shift:
- 1 - Its Code on the Route Plan.
- 2 - Its current Planning Status.
- 3 - Its Start Time and Stop Time as planned by the system.

<Image title="4. Shift Block (ENG).png" alt={1920} border={true} src="https://files.readme.io/2328d88-4._Shift_Block_ENG.png">
  Illustration (English)
</Image>

<Image title="4. Shift Block (VIE).png" alt={1920} border={true} src="https://files.readme.io/f3893ee-4._Shift_Block_VIE.png">
  Illustration (Vietnamese)
</Image>

* One Vehicle can have multiple horizontal bars on the Gantt chart. This means the Vehicle is assigned multiple Delivery Shifts.

<Image title="Locked and Planned (ENG).png" alt={1920} border={true} src="https://files.readme.io/2147109-Locked_and_Planned_ENG.png">
  Illustration (English)
</Image>

<Image title="Locked and Planned (VIE).png" alt={1920} src="https://files.readme.io/05b3e8d-Locked_and_Planned_VIE.png">
  Illustration (Vietnamese)
</Image>

* If you click on a horizontal bar, you will be directed to the Map View Screen of the Route Plan that stores the corresponding Delivery Shift. 

<Image title="9. Block Shift (ENG).gif" alt={1920} border={true} src="https://files.readme.io/eaaac24-9._Block_Shift_ENG.gif">
  Illustration (English)
</Image>

<Image title="10. Block SHift (ENG).gif" alt={1920} border={true} src="https://files.readme.io/d7899af-10._Block_SHift_ENG.gif">
  Illustration (Vietnamese)
</Image>

* Everything you do to the Delivery Shift in the Route Plan screen will reflect on the Gantt chart, for example: 
* You change the Planning Status of a Vehicle's Delivery Shift from ***Locked*** to ***Planned***. The color and the Planning Status information of the Delivery Shift's corresponding horizontal bar on the Gantt chart will also change.

<Image title="Merged 1.png" alt={1920} border={true} src="https://files.readme.io/588dbb5-Merged_1.png">
  Illustration (English)
</Image>

<Image title="Merged 2.png" alt={1920} border={true} src="https://files.readme.io/f5c14a9-Merged_2.png">
  Illustration (Vietnamese)
</Image>

* You assign the Delivery Shift from one Vehicle to another. The Delivery Shift's horizontal bar will move from the past Vehicle to the new one.

- If you use two browser tabs, one for the Route Plan and one for the Gantt View, you can click the **Refresh** button on the Gantt View toolbar to update the latest changes to the Delivery Shifts on the Gantt chart.

<Image title="5. refresh (ENG).png" alt={1733} border={true} src="https://files.readme.io/a7221dc-5._refresh_ENG.png">
  Illustration (English)
</Image>

<Image title="5. refresh (VIE).png" alt={1733} border={true} src="https://files.readme.io/c7c3f16-5._refresh_VIE.png">
  Illustration (Vietnamese)
</Image>
