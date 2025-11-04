---
title: Assign consecutive orders to one driver
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
* If you want to assign one single driver to operate multiple consecutive orders, delivered by multiple different vehicles, you can do so by:
* Create the first order, perform route optimization
* Take note of the complete time and the driver code of the first order
* Go back to the **Transportation > Vehicle List** tab, find the vehicle which operates this order
* Click **Edit** :fa-pencil: for that vehicle
* Change the **Stop time** of that vehicle to a time point shortly after the time point when the first order is completed. For example, if the first order is completed at 11:00, then the **Stop time** of the vehicle can be set to around 11:10
* Click **Update** to confirm the change
* Perform route optimization for the first order again, this time also **Lock route** to send the order tasks to the driver's mobile app

<Image title="838cdfb-Driver.png" alt={1677} className="border" border={true} src="https://files.readme.io/19593e1-838cdfb-Driver.png" />

* Copy the *Driver Code* of the driver who performs that order
* Create the second order
* Perform route optimization for the second order, choose the *Cut-off time* of the second order at a time point later than the *Complete time* of the first order

<Image title="27569b8-driver_2.png" alt={1677} className="border" border={true} src="https://files.readme.io/ae97ae5-27569b8-driver_2.png" />

* Go back to the **Transportation > Vehicle List** tab, find the vehicle which operates the second order
* Click **Edit** :fa-pencil: for that vehicle
* Paste the *Driver Code* of the first order into the **Default driver** field of that vehicle
* Change the **Start time** of this vehicle to a suitable time point after the complete time of the first order. The **Stop time** of this vehicle can be calculated by the sum of the recently configured **Start time** and the optimized time period to perform the order. For example, if the first order completes at 11:00, the dispatcher can set the **Start time** of the vehicle which will operate the second order to 12:00 (which allows the driver to rest for 1 hour). The second order, from the route optimization result, will take around 05 hours to operate. Therefore, the **Stop time** of the vehicle should be set to 12:00 + 05:00 = 17:00 
* Click **Update** to confirm

![1677](https://files.readme.io/34822dc-936671a-driver_3.png "936671a-driver_3.png")

* Go back to the route optimization map screen, perform route optimization again
* Lock route for the second order
* By doing this, the task of these two consecutive orders will be sent to only one driver's Mobile app
* You can continue to assign other consecutive orders to the same driver using this method

![1677](https://files.readme.io/ce9ca6a-2d3b4ce-driver_4.png "2d3b4ce-driver_4.png")
