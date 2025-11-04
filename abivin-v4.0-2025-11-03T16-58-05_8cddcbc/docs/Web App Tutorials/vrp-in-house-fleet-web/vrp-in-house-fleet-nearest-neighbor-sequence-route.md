---
title: Nearest Neighbor Sequence Route
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
* The default routing algorithm of Abivin vRoute is configured so that the vehicles will deliver for the farthest customer from the Depot first, and the closest customer last
* However, there might be situations in which the vehicles need to deliver fragile and bulky products. The vehicles, therefore, need to deliver to the closest customer first and the farthest customer last. This article will how to achieve that using the **Nearest Neighbor Sequence Route** algorithm configuration
* First, you need to enable this configuration at the Branch (In the sub-tab **More Configuration > Algorithm**). Then you can proceed to create orders and optimize routes as usual

<Image title="uCuSDGeqbQ.png" alt={736} className="border" border={true} src="https://files.readme.io/569a99e-uCuSDGeqbQ.png" />

* Below is the example of a Delivery Route when this configuration is enabled and disabled. As you can see, on the left side (This configuration is enabled), the vehicle will deliver to the closest customer first, while on the right side (This configuration is not enabled), the vehicle will deliver to the closest customer last

<Image title="2bibPVvknA.png" alt={857} className="border" border={true} src="https://files.readme.io/4131e51-2bibPVvknA.png" />
