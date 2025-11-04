---
title: Vehicle Lunch Break
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
* During the performing of deliveries, the drivers might need to take a quick lunch break time before continuing the tasks assigned. In Abivin vRoute, you can allocate the lunch time period for the vehicles by using the **Lunch time** configuration

## Enable Lunch Break Configuration

* Navigate to **Organizations > Organization List** tab
* Click on **Edit** :fa-pencil: of the ***Branch*** which you want to activate this configuration

<Image title="2019-10-29 17_56_26-Window.png" alt={1914} className="border" border={true} src="https://files.readme.io/4cdfefd-2019-10-29_17_56_26-Window.png" />

* On the **Organization Information** screen, scroll down and click on **More Configurations** :fa-caret-down: to open the algorithm configuration section
* Click on the **Lunch time** check box
* Click **Save** to confirm the change

<Image title="2019-10-29 17_57_28-Window.png" alt={1914} className="border" border={true} src="https://files.readme.io/324525a-2019-10-29_17_57_28-Window.png" />

## Configure Lunch break time for vehicles

* Next, you need to configure the exact Lunch break time period for each vehicle managed by the Depots/Suns under the Branch configured above

## Configure for existing vehicles

* Navigate to **Transportation > Vehicle List** tab
* Click on **Edit** :fa-pencil: icon of the vehicles which you want to configure the lunch break time period
* On the **Update Vehicle** form, input the time point when the Lunch break starts and ends in the **Lunch start time (hh:mm)** and **Lunch stop time (hh:mm)** fields. Note that the time format must be **hh:mm (24 hours)** and must not exceed ***23:59***
* For example, the vehicle starts the lunch break at ***11:30 A.M*** and ends the lunch break at ***1:00 P.M***. You should input ***11:30*** into the **Lunch start time** field and ***13:00*** into the **Lunch stop time** field
* Click **Update** to confirm the change
* Repeat the steps above for other vehicles
* **Note:** If you don't input any value into the **Lunch start time** and **Lunch stop time** fields, the system will suppose that those vehicles do not have lunch break time

<Image title="2019-09-23 15_44_53-Window.png" alt={794} className="border" border={true} src="https://files.readme.io/dfdcc28-2019-09-23_15_44_53-Window.png" />

## Configure for new vehicles

* If you create new vehicles using the Web form, follow the steps above
* If you create new vehicles using Excel template, input the lunch break time in the **Lunch start time** and **Lunch stop time** fields. The time format must also be **hh:mm (24 hours)**

<Image title="2019-09-23 15_43_46-Window.png" alt={1633} className="border" border={true} src="https://files.readme.io/3e4942b-2019-09-23_15_43_46-Window.png" />

## Perform route optimization

* After configuring the lunch break time for the vehicles, you can perform route optimization process as usual
* The process will take into account the lunch break time of the vehicles. During the lunch break time, the vehicles will not perform any tasks. Any load/unload tasks will be moved to after the vehicle has finished the lunch break
* For example: A vehicle is configured to have the lunch break time from ***12:00*** to ***13:30***

<Image title="2019-09-23 15_55_55-Window.png" alt={795} className="border" border={true} src="https://files.readme.io/d728462-2019-09-23_15_55_55-Window.png" />

* If the Lunch break time configuration is not enabled, the load/unload tasks can be performed during this lunch break time period

<Image title="2019-09-23 16_14_04-Window.png" alt={1673} className="border" border={true} src="https://files.readme.io/48670ba-2019-09-23_16_14_04-Window.png" />

* If the Lunch break time configuration is enabled, the load/unload tasks will be moved to after the lunch break time period has ended

<Image title="2019-09-23 15_54_53-Window.png" alt={1677} className="border" border={true} src="https://files.readme.io/c7dfa65-2019-09-23_15_54_53-Window.png" />
