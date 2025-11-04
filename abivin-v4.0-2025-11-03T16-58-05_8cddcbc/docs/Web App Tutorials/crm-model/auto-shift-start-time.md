---
title: Auto Shift Start Time
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
\*\*note: người sau bổ sung Manual của Pana trước khi publish nha ^^

## Overview

* This configuration will allow the system to suggest Shift Start Time that will minimize driver's waiting time at stops. 
* Go to **Branch > More Configurations > Route > Shift Start Time** .  Select **Auto** to turn on Auto Shift Start Time 

<Image title="autoshift.PNG" alt={753} src="https://files.readme.io/49a2ac8-autoshift.PNG">
  Illustration
</Image>

* This configuration is not compatible with PDP Model. 

## Setting up for Auto Shift Start Time

* This configuration must be combined with [Hard Time Window](https://docs.abivin.com/docs/vrp-in-house-fleet-hard-time-window-constraint).  

* Depot's Working Time and Vehicle's Working Time must be overlapping (Vehicle's Working Time must start no later than Depot's Close Time). 

* During Route Optimization, The Shift Start Time for each vehicle will be computed in order to have an optimal waiting time for the trip. If the optimal Shift Start Time does not satisfy Depot's Close Time, the system will suggest the vehicle to start Shift at the time to ensure the vehicle has departed when the Depot closes. 

* Refer to this article about [Route Plan Optimization](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-map-view)
