---
title: Delivery Trip Limitations
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
* During the Route Plan optimization process, you can put some limitations on the Delivery Trips of the Vehicles, including:
* 1 - The maximum number of Stops on a Delivery Trip
* 2 - The furthest distance possible between any two Stops on a Delivery Trip
* 3 - The minimum total volume of all the Orders on a Delivery Trip
* Note: The number of limitations that you can set up is likely to increase in the future
* This article will guide you on how to set up the limitations in the Abivin vRoute system

## Set Up Delivery Trip Limitations

* To set up the Delivery Trip limitations, follow the steps below
* Navigate to the **Organizations > Organizations** tab
* Click the **Edit** icon :fa-pencil: of the Branch
* On the **Update Organization** form, navigate to the **More Configurations > Algorithm** sub-tab
* Here, you will see two checkboxes, **Limit For Each Trip** and **Minimum Order Quantity**. These two checkboxes will allow you to set up the above-aforementioned limitations for the Delivery Trips

### Limit For Each Trip

* When you tick the **Limit For Each Trip** checkbox, a couple of radio boxes and input fields will appear below to let you set up some limitations that are related to the Stops on the Delivery Trip
* The **Default** radio box is the box that is ticked by default. When this radio box is ticked, the effect of this configuration will be applied to ***all*** Customers of the Depots under the Branch. There will be two input fields below this radio box:
* 1 - **Maximum Distance between Nearest and Furthest Stops**: This field lets you specify the maximum distance, in kilometer (km), between two Stops on a Delivery Trip
* You can input a positive integer or decimal value into this field. If you leave this field blank, it means you don't set any limitation regarding this
* For example, if you input the value ***15.3***, it means you want to set the maximum distance between any two Stops on a Delivery Trip at ***fifteen point three kilometers***
* 2 - **Maximum Number of Stops**: This field lets you specify the maximum number of Stops on a Delivery Trip
* You can input a positive integer value into this field. If you leave this field blank, it means you don't set any limitation regarding this
* For example, if you input the value ***10***, it means you want to set the maximum number of Stops on a Delivery Trip at ***ten Stops***

<Image title="FAiIzAFeze.png" alt={741} border={true} src="https://files.readme.io/8e97b16-FAiIzAFeze.png">
  Illustration (English)
</Image>

<Image title="Cn6vQgEhPN.png" alt={741} border={true} src="https://files.readme.io/8ebf5bf-Cn6vQgEhPN.png">
  Illustration (Vietnamese)
</Image>

* If you tick the **Custom On Each Customer Group** radio box, the two input fields above will disappear on this form. Instead, they will appear on the setup form of the Customer Groups of the Depots under the Branch. To set up these limitations for the Customer Groups, you need to navigate to the **Partners > Customer Groups** tab
* You need to open the update form of each Customer Group to access these fields. These input fields will be present in the **Other Settings** tab

<Image title="hw9YYiefMl.png" alt={951} border={true} src="https://files.readme.io/0b0b563-hw9YYiefMl.png">
  Illustration (English)
</Image>

<Image title="0jE4czovFM.png" alt={956} border={true} src="https://files.readme.io/905969e-0jE4czovFM.png">
  Illustration (Vietnamese)
</Image>

### Minimum Order Quantity

* When you tick the **Minimum Order Quantity** checkbox, a couple of radio boxes and input fields will appear below to let you set up some limitations that are related to the Orders on the Delivery Trip
* The **Default** radio box is the box that is ticked by default. When this radio box is ticked, the effect of this configuration will be applied to ***all*** Customers of the Depots under the Branch. There will be one input field below this radio box:
* **Minimum Volume - CBM**: This field lets you specify the minimum volume, in cubic meter (m3), of all Orders on a Delivery Trip. If you leave this field blank, it means you don't set any limitation regarding this 
* You can input a positive integer or decimal value into this field. If you leave this field blank, it means you don't set any limitation regarding this
* For example, if you input the value ***2.5***, it means you want to set the minimum total volume of all Orders on a Delivery Trip at ***two point five cubic meters***

<Image title="PPACWd5YbL.png" alt={739} border={true} src="https://files.readme.io/f477a87-PPACWd5YbL.png">
  Illustration (English)
</Image>

<Image title="F7DWnNL5xY.png" alt={738} border={true} src="https://files.readme.io/05976fa-F7DWnNL5xY.png">
  Illustration (Vietnamese)
</Image>

* If you tick the **Custom On Each Customer Group** radio box, the input field above will disappear on this form. Instead, it will appear on the setup form of the Customer Groups of the Depots under the Branch. To set up this limitation for the Customer Groups, you need to navigate to the **Partners > Customer Groups** tab
* You need to open the update form of each Customer Group to access this field. This input field will be present in the **Other Settings** tab

<Image title="vh0479euV5.png" alt={951} border={true} src="https://files.readme.io/c075ffb-vh0479euV5.png">
  Illustration (English)
</Image>

<Image title="275RIe7pGp.png" alt={955} border={true} src="https://files.readme.io/361678f-275RIe7pGp.png">
  Illustration (Vietnamese)
</Image>
