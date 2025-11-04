---
title: Limit Number Of Delivery Shifts/Delivery Trips
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
* In Abivin vRoute system, during the Route Plan optimization process, a Vehicle can be assigned many Delivery Shifts and Delivery Trips as long as its parameters (Weight/Volume capacity; Working time, etc.) can still meet the demand
* This article will instruct you how to set a limit on the maximum number of Delivery Shifts/Delivery Trips that the system can assign to a single Vehicle

## Compulsory Configurations

* First, you need to enable the Limit Number Of Shifts/Limit Number Of Trips configurations at the Branch by following the steps below
* Navigate to the **Organizations > Organizations** tab
* Click the **Edit** icon :fa-pencil: of the Branch you want to enable these configurations
* On the **Update Organization** form, navigate to the **More Configuration > Algorithm** sub-tab. Scroll down the form until you see the **Limit Number Of Shifts** and **Limit Number Of Trips** checkboxes 
* If you tick these configurations' respective checkboxes, you can then input into the **Number Of Shifts Limited/Number Of Trips Limited** fields. These input fields allow you to specify the maximum number of Delivery Shifts/Delivery Trips that the system can assign to each Vehicle under the management of all the Depots under this Branch during the Route Plan optimization process

<Image title="89fZQGOLet.png" alt={728} border={true} src="https://files.readme.io/4d1fa9d-89fZQGOLet.png">
  Illustration (English)
</Image>

<Image title="STyCb5AiBQ.png" alt={730} border={true} src="https://files.readme.io/d12e0fe-STyCb5AiBQ.png">
  Illustration (Vietnamese)
</Image>

* For example, if you input the value ***3*** into the **Number Of Shifts Limited** field and the value ***2*** into the **Number Of Trips Limited** field, that means during the Route Plan optimization process of a specific date, a Vehicle can be assigned up to three Delivery Shifts and up to two Delivery Trips within each Delivery Shift
* Note: These configurations are not interdependent. You can enable either one or both of them

## Route Plan Optimization Process

* Let's look at the simple examples below to understand how these configurations work

### Limit Number Of Trips

* I prepare three Orders and one active Vehicle. The volume of each Order equals the volume capacity of that Vehicle. I also don't enable the **Limit Number Of Trips** configuration.
* During the Route Plan optimization process, the system will put all three Orders into the Delivery Shift of that active Vehicle. Each of these Orders will occupy one Delivery Trip within the Vehicle's Delivery Shift.

- I then enable the **Limit Number Of Trips** configuration and set the maximum number of Delivery Trips per Delivery Shift to ***2***.

* I will then perform the Route Plan optimization process again. This time, the system will only generate two Delivery Trips for the Vehicle. One of the Orders will be treated as Unplanned Order since the maximum number of Delivery Trips per Delivery Shift of the Vehicle has been reached.

### Limit Number Of Shifts

* I prepare three Orders and one active Vehicle. I also don't enable the **Limit Number Of Shifts** configuration.
* I prepare one Order, perform the Route Plan optimization process and lock the Delivery Shift of the Vehicle.
* I then create another Order, perform the Route Plan optimization process again. The system will generate the second Delivery Shift of the Vehicle. I don't lock the second Delivery Shift just yet.
* By now, I will enable the **Limit Number Of Shifts** configuration and set the maximum number of Delivery Shifts per Vehicle to ***1***.
* I will then perform the Route Plan optimization process again. This time, the system will treat the second Order as Unplanned Order and will not generate the Delivery Shift for the second Order because the maximum number of Delivery Shifts of that Vehicle has been reached.
