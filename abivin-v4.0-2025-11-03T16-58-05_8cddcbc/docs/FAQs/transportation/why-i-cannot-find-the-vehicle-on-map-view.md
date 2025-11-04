---
title: Why I cannot find the vehicle on Map View?
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
## Why I cannot find the vehicle on Map View?

**:fa-angle-right:Case:** After optimizing the route, the system pop up a notification "Cannot find the solution" and no result of route planning. You go to ransportation] a and check on the availability of your wanted vehicle - 29C-01946 and it appears that eventhough the **Active Box** is unticked, the vehicle status displays **Planned** status.

<Image title="trans2.png" alt={1920} src="https://files.readme.io/ae6b7fc-trans2.png">
  "Cannot find the solution" when optimizing the route
</Image>

<Image title="trans1.png" alt={1920} src="https://files.readme.io/59b2a04-trans1.png">
  The vehicle remains "Planned status" despite being inactive.
</Image>

**:fa-angle-right:Reason:** This situation means that the vehicle was planned for a route in the past and the driver has not submitted the **End Day** task on the Mobile App. That is the reason why the **Vehicle Status** does not change to Open.

**:fa-angle-right:Solution:** Don't be worry, the Vehicle Status does not affect the action of route optimizing. The root cause here is the **Active Box** which was left unticked. You just need to tick the **Active Box** and the route can be planned normally. For the **Vehicle Status**, please inform the driver submit the **End day** task so that the Planned status will change to Open status.

![1920](https://files.readme.io/fdf64d6-trans6.png "trans6.png")

> 📘 Notice
>
> You can also track the Vehicle Status following by date via using Gantt View to see on which day was your vehicle planned.

* Please click on the w] button to button to switch to Gantt View. 

![1920](https://files.readme.io/ef03a58-trans3.png "trans3.png")

* On the Gantt View, the vehicle status of the vehicle is devided into 02 types which are Locked and Planned, marked respectively with 02 colors blue and yellow. If you do not know how to turn on the  configurati configuration and how to use it, please find more information [here](https://docs.abivin.com/docs/vrp-dc-vehicle-gantt-view). 

![1920](https://files.readme.io/5d1cb6a-trans4.png "trans4.png")
