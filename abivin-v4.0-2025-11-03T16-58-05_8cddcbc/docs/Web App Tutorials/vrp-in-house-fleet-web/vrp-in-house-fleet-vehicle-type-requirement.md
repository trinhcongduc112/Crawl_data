---
title: Default Vehicle Types
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
* As has been mentioned in the [**Manage Vehicles**]() article, in VRP/DC model by default there are three Vehicle Types: Motorbike, Truck, and Semi-truck
* When you carry out the Route Plan optimization process on the Route Plan (Map View), on the Timeline panel, the Vehicles of the Motorbike type will be represented by the motorcycle icon :fa-motorcycle:, and the Vehicles of the Trucks/Semi-trucks type will be represented by the truck icon :fa-truck:

<Image title="7.png" alt={215} border={true} src="https://files.readme.io/e4b92a0-7.png">
  Illustration (English)
</Image>

<Image title="8.png" alt={215} src="https://files.readme.io/f8ac14b-8.png">
  Illustration (Vietnamese)
</Image>

* This article will explain how you can specify the allowed Vehicle Types among the above three for each Customer

## Configure customers

* You need to specify the delivery medium(s) accepted by each customer

### Configure existing customers

* Navigate to **Partners > Customer List** tab
* Click on **Edit** :fa-pencil: icon of the customers who you want to configure

<Image title="2019-10-30 11_05_28-Window.png" alt={1908} border={true} src="https://files.readme.io/d6a4c06-2019-10-30_11_05_28-Window.png">
  Illustration Image (English)
</Image>

<Image title="1.png" alt={1920} src="https://files.readme.io/bb887f9-1.png">
  Illustration Image (Vietnamese)
</Image>

* On the **Edit Customer** screen, scroll down and click on **More Configurations** :fa-caret-down: to open the algorithm configuration section
* Specify the delivery medium required by that customer by inputting in both the **Bike Only** and **Truck Only** fields. There are two possible values to input: **TRUE** - that customer ***accepts*** that delivery medium to deliver to them; and **FALSE** - that customer ***does not accept*** that delivery medium to deliver to them
* Click **Save** to confirm the changes

<Image title="3.png" alt={958} border={true} src="https://files.readme.io/ac4cd99-3.png">
  Illustration Image (English)
</Image>

<Image title="2.png" alt={958} src="https://files.readme.io/7a81410-2.png">
  Illustration Image (Vietnamese)
</Image>

* There are three input options:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Input Option
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        * \*Bike only\*\*: TRUE
        * \*Truck only\*\*: FALSE
      </td>

      <td>
        That Customer only allows motorbikes and does not allow trucks/semi-trucks
      </td>
    </tr>

    <tr>
      <td>
        * \*Bike only\*\*: FALSE
        * \*Truck only\*\*: TRUE
      </td>

      <td>
        That Customer only allows Trucks/Semi-trucks and does not allow Motorbikes
      </td>
    </tr>

    <tr>
      <td>
        * \*Bike only\*\*: FALSE
        * \*Truck only\*\*: FALSE
      </td>

      <td>
        That Customer allows both Trucks/Semi-trucks and Motorbikes
      </td>
    </tr>
  </tbody>
</Table>

> ❗️ WARNING!
>
> **DO NOT** input the **TRUE** value in both of these fields! That will cause a confusion to the system and the route optimization process will not be able to start

<Image title="2019-10-30 10_32_42-Window.png" alt={1709} border={true} src="https://files.readme.io/bce2fb5-2019-10-30_10_32_42-Window.png">
  The customer only accepts Trucks
</Image>

<Image title="2019-10-30 10_32_34-Window.png" alt={1709} border={true} src="https://files.readme.io/bdf90cb-2019-10-30_10_32_34-Window.png">
  The customer only accepts Motorbikes
</Image>

<Image title="2019-10-30 10_32_10-Window.png" alt={1709} border={true} src="https://files.readme.io/d4001f4-2019-10-30_10_32_10-Window.png">
  The customer accepts both Motorbikes and Trucks
</Image>

<Image title="2019-10-30 10_32_25-Window.png" alt={1709} border={true} src="https://files.readme.io/0fa2d25-2019-10-30_10_32_25-Window.png">
  DO NOT input like this
</Image>

## Configure new customers

* If you create new customers using Web form, follow the instruction described above
* If you create new customers using Excel template, there are also **Truck Only** and **Bike Only** fields. Input similarly like on Web form

<Image title="2019-10-30 10_40_17-Window.png" alt={229} border={true} src="https://files.readme.io/f5120a1-2019-10-30_10_40_17-Window.png">
  Input either of the three green options. DO NOT input the red option
</Image>

<Image title="4.png" alt={158} src="https://files.readme.io/6f0804c-4.png">
  Input either of the three green options. DO NOT input the red option
</Image>

## Route Plan Optimization

* The Route optimization process will take into account the configurations you have made for each customer, and will allocate delivery vehicles correspondingly
* Make sure that there are active vehicles accepted by those customers, otherwise the Route optimization process can not generate results

<Image title="bikeonly.png" alt={1368} border={true} src="https://files.readme.io/9c82d13-bikeonly.png">
  The customer only accepts Motorbikes
</Image>

<Image title="5.png" alt={1753} src="https://files.readme.io/a86cc6d-5.png">
  The customer only accepts Motorbikes
</Image>

<Image title="truckonly.png" alt={1349} border={true} src="https://files.readme.io/df27519-truckonly.png">
  The customer only accepts Trucks
</Image>

<Image title="6.png" alt={1920} src="https://files.readme.io/204cb9e-6.png">
  The customer only accepts Trucks
</Image>
