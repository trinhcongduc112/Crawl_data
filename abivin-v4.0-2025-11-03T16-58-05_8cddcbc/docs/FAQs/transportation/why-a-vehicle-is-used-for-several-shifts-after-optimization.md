---
title: Why a vehicle is used for several shifts after optimization?
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
## Why a vehicle is used for several shifts after optimization?

**:fa-angle-right:Case:** After optimizing the route plan, it appears that a vehicle, for example vehicle Xe may 1 with plate license number 29b1-6383, is assigned to many different routes although there are available vehicles.

![1920](https://files.readme.io/fc89105-VehiclesXX.png "VehiclesXX.png")

* On the tab Vehicles, both vehicles coded AbivinVroute & Xe may 1 are Active to assign.

![1920](https://files.readme.io/a372013-VehiclesXX2.png "VehiclesXX2.png")

**:fa-angle-right:Reason:** the optimized Branch is using both "Use Familarity" config and "Rental Vehicle" which results in the above situation.

![1920](https://files.readme.io/249d778-VehiclesXX4.png "VehiclesXX4.png")

* The rental cost field of vehicle Xe may 1 is filled with a greater-than-zero value identifying this vehicle as a rental vehicle. In case there are some specific reasons causing the missing orders such as Out of working hours, Overload, Over-capacity, and more, the rental vehicle will be re-used to carry those orders whose customers have alike MDP codes. 

![1920](https://files.readme.io/a5fb45d-vehicleXX3.png "vehicleXX3.png")

**:fa-angle-right:Solution:** Please untick "Use Familirity" config or change the "Rental Cost" field of the rental vehicle to 0. Then, go to  and re-op and re-optimize the route plan.

> 📘 Notice:
>
> If you want to use both Familarity config and rental vehicle for route optimization, please follow these instructions below:

* **Step 1:** Go to ion] and select  and select o enter yo to enter your optimized route plan.
* **Step 2:** Select the cle] button on a button on a specific route and change the assigned vehicle to another one.

![1920](https://files.readme.io/78c059c-vehicleXX5.png "vehicleXX5.png")
