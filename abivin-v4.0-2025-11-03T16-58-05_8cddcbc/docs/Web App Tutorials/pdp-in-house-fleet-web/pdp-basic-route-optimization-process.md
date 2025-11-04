---
title: PDP - Basic route optimization process
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
* Navigate to **Transportation > Vehicle List** tab
* Click on the **View Map** icon on the toolbar
* The route optimization screen will appear
* On the form that appears, click on the **Branch** field and choose the ***Branch*** that manages the PDP depots. Next, click on the :fa-calendar: icon of the **Date** field and select the ***current date*** from the drop down calendar

> 🚧 Unlike VRP model, you can only select the ***current date*** in PDP model

* The routes for all orders will be pre-generated on the Timeline panel
* Click on **Optimize** button
* A form that reads **Optimize Route** will appear. Here you will choose the **Cut-off time** for all orders being optimized. The Cut-off time is the time period (In hours) to be added to the current time on your computer. The start time for all orders will be calculated by this formula: ***Estimated Start time = Current time + Cut-off time***
* For example, the Current time on your computer is *17:57 19/09*. You choose the Cut-off time for the orders being optimized to be *01* hours. Therefore, after clicking **Optimize**, the Estimated Start time for the orders will be around *18:57 19/09*

<Image title="PDP optimize cutoff.gif" alt={1672} className="border" border={true} src="https://files.readme.io/3ba0e19-PDP_optimize_cutoff.gif" />
