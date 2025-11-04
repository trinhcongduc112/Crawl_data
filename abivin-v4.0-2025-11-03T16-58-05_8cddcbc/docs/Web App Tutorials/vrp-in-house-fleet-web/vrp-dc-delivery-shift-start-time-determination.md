---
title: Delivery Shift Start Time Determination
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
* In Abivin vRoute system, during the Route Plan optimization process, you have two methods to determine the Start Time point of a Delivery Shift: 
* Method 1: Relative Shift Start Time
* Method 2: Absolute Shift Start Time

## Delivery Shift Start Time Determination Method Configuration

* To select the Delivery Shift Start Time determination method, follow the steps below
* Navigate to the **Organizations > Organizations** tab
* Click the **Edit** icon :fa-pencil: of the Branch
* On the **Update Organization** form, navigate to the **More Configurations > Route** sub-tab
* Look at the **Shift Settings** section. In this section, click the respective radio box of the Shift Start Time determination method that you want to use. By default, the **Relative (default)** radio box is ticked for all new user accounts

<Image title="7jlsWWFgEj.png" alt={742} border={true} src="https://files.readme.io/cf71b3a-7jlsWWFgEj.png">
  Illustration (English)
</Image>

<Image title="xtJhiKhMzc.png" alt={742} border={true} src="https://files.readme.io/dec9f22-xtJhiKhMzc.png">
  Illustration (Vietnamese)
</Image>

* Click **Save** to confirm the change

## Relative Shift Start Time Determination Method

* If you use this Delivery Shift Start Time determination method, the Start time point of the very first Delivery Shifts of the Vehicles on a specific Route Plan date will be determined by comparing the **Start Time** of the Vehicles against the **Open Time** of the Depot. Whichever time point is later will be used as the Start time point of the Delivery Shift
* For example, the Open Time of the Depot is set at ***07:00***. Two Vehicles, A and B, are utilized in the Route Plan. The Start Time of Vehicle A is set at ***08:00***, later than the Open Time of the Depot, while the Start Time of Vehicle B is set at ***06:35***, earlier than the Open Time of the Depot
* When you first run the Route Optimization process, the system will set the start time points of the first Delivery Shifts of these Vehicles as follow:
* Vehicle A: The start time point of this Vehicle's first Delivery Shift will be set at ***08:00*** since that time point is later than the Open Time of the Depot
* Vehicle B: The start time point of this Vehicle's first Delivery Shift will be set at ***07:00*** since the Open Time of the Depot is later than the Start Time of this Vehicle
* After you have locked the very first Delivery Shifts of the Vehicles on the Route Plan date, then, as you click the **Optimize** button again, the system will prompt you to select the **Cut-off Time**. The Cut-off Time is the start time point of the next Delivery Shifts of ***all*** the Vehicles on the Route Plan
* When you click on the Cut-off Time field, the drop-down list will display the possible time points, in HH:mm (hour:minute, 24 hours) format, for you to choose. The time point has an increment of ***30 minutes***. For example, if you select the value ***01:00***, that means you want to start the next Delivery Shifts of all the Vehicles at ***one A.M***, while if you select the value ***17:30***, that means you want to start the next Delivery Shifts of all the Vehicles at ***five-thirty P.M***

<Image title="u64UHPEVJq.png" alt={388} border={true} src="https://files.readme.io/ff9f0aa-u64UHPEVJq.png">
  Illustration (English)
</Image>

<Image title="lz5kK4hyam.png" alt={392} border={true} src="https://files.readme.io/47abf8f-lz5kK4hyam.png">
  Illustration (Vietnamese)
</Image>

## Absolute Shift Start Time Determination Method

* If you use this Delivery Shift Start Time determination method, you can proactively select a specific time point to start the Delivery Shift, even for the very first Delivery Shift of a Vehicle on a Route Plan date
* For this method, the **Optimize Route** form will appear different than the Relative Shift Start Time determination method. To specify the Start time point of the Delivery Shift, input the desired time point, in HH:mm (hour:minute, 24 hours) format, into the **Shift-start time (HH:mm)** field. For example, if you input the value ***13:25***, that means you want to start the Delivery Shift at ***one twenty-five P.M***

<Image title="FqyzxieJnS.png" alt={394} border={true} src="https://files.readme.io/66acd23-FqyzxieJnS.png">
  Illustration (English)
</Image>

<Image title="jrCZiHyEZo.png" alt={393} border={true} src="https://files.readme.io/631b8b9-jrCZiHyEZo.png">
  Illustration (Vietnamese)
</Image>
