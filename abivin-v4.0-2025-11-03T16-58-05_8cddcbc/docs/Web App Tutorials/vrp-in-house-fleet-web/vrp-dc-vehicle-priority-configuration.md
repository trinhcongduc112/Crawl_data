---
title: Vehicle Priority Configuration
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
* This article will explain how you can flexibly set up the vehicle priority based on the weight/volume capacity of the vehicles when you optimize Route Plan.

## Precondition to use the Vehicle Priority Configuration

### Requirement for Manufacturer

* To be able to use the Vehicle Priority configuration, please make sure the Business Model of the Manufacturer is **1PL**. The **Vehicle Priority** configuration is not available in the business model **3PL**
* To check this, please follow these steps
* Step 1: Navigate to **Organizations > Organizations** tab
* Step 2: Click the **Edit** icon :fa-pencil: of the **Manufacturer** you want to update information. You could refer to the **Organization Categories** column to see what type of organization you selected is.

<Image title="1. Business Model 1 (ENG).png" alt={1902} border={true} src="https://files.readme.io/43909c1-1._Business_Model_1_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Business Model 2 (VIE).png" alt={1899} border={true} src="https://files.readme.io/53f150e-1._Business_Model_2_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 3: A form named **Update Organization** will show up on the screen. Click the **More Configuration** tab, then select the sub-tab named **Model** on the left of the form. In the form **Model Settings**, look at the section named **Business** then tick the box **1PL**.

<Image title="1. Business Model 2 (ENG).png" alt={932} border={true} src="https://files.readme.io/414796d-1._Business_Model_2_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Business Model (VIE).png" alt={931} border={true} src="https://files.readme.io/cfa47a0-1._Business_Model_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 4: Click **Save** for changes to take effect.

### Requirement for Branch

* To be able to use the Vehicle Priority configuration, please make sure the Branch does not use the **PDP Order** configuration. The **Vehicle Priority** configuration is not available for **Branch** using PDP Orders.
* To check this, please follow these steps
* Step 1: Navigate to **Organizations > Organizations** tab
* Step 2: Click the **Edit** icon :fa-pencil: of the **Branch** you want to update information. You could refer to the **Organization Categories** column to see what type of organization you selected is.

<Image title="1. PDP Order 1 (ENG).png" alt={1902} border={true} src="https://files.readme.io/4e35d8b-1._PDP_Order_1_ENG.png">
  Illustration (English)
</Image>

<Image title="1. PDP Order 1 (VIE).png" alt={1899} border={true} src="https://files.readme.io/1cd374f-1._PDP_Order_1_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 3: A form named **Update Organization** will show up on the screen. Click the **More Configuration** tab, then select the sub-tab named **Route** on the left of the form. In the form named **Route Settings**, please untick the box **PDP Order**.

<Image title="2. PDP Order (ENG).png" alt={931} border={true} src="https://files.readme.io/5befbe7-2._PDP_Order_ENG.png">
  Illustration (English)
</Image>

<Image title="2. PDP Order (VIE).png" alt={930} border={true} src="https://files.readme.io/4700fd2-2._PDP_Order_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 4: Click **Save** for changes to take effect.

## Set Up Vehicle Priority

* To set up Vehicle Priority, please follow these steps below
* Step 1: Navigate to **Organizations > Organizations** tab
* Step 2: Click the **Edit** icon :fa-pencil: of the **Branch** you want to update information. You could refer to the **Organization Categories** column to see what type of organization you selected is.

<Image title="1. PDP Order 1 (ENG).png" alt={1902} border={true} src="https://files.readme.io/114ccbe-1._PDP_Order_1_ENG.png">
  Illustration (English)
</Image>

<Image title="1. PDP Order 1 (VIE).png" alt={1899} border={true} src="https://files.readme.io/0bc4b80-1._PDP_Order_1_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 3: A form named **Update Organization** will show up on the screen. Click the **More Configuration** tab, then select the sub-tab named **Algorithm** on the left of the form. In the form named **Algorithms Settings**, please scroll down until you see the **Vehicle Priority** section

<Image title="3. Vehicle Prio (ENG).png" alt={930} border={true} src="https://files.readme.io/f178a47-3._Vehicle_Prio_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Vehicle Prio (VIE).png" alt={930} border={true} src="https://files.readme.io/7e40714-3._Vehicle_Prio_VIE.png">
  Illustration (Vietnamese)
</Image>

* By clicking the icon descending arrow  :fa-sort-desc:  in two fields within the line ***Prioritize vehicles***, you can adjust the priority criteria of the vehicle selection that will be applied during the Route Plan Optimization process. There are four priority settings:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Priority Setting
      </th>

      <th>
        Priority Setting Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Prioritize vehicles **Ascending** by **Weight** to optimize route
      </td>

      <td>
        Prioritize the vehicle with the smallest weight capacity first, then move on to vehicles with larger weight capacity
      </td>
    </tr>

    <tr>
      <td>
        Prioritize vehicles **Descending** by **Weight** to optimize route
      </td>

      <td>
        Prioritize the vehicle with the largest weight capacity first, then move on to vehicles with smaller weight capacity
      </td>
    </tr>

    <tr>
      <td>
        Prioritize vehicles **Ascending** by **Volume** to optimize route
      </td>

      <td>
        Prioritize the vehicle with the smallest volume capacity first, then move on to vehicles with larger volume capacity
      </td>
    </tr>

    <tr>
      <td>
        Prioritize vehicles **Descending** by **Volume** to optimize route
      </td>

      <td>
        Prioritize the vehicle with the largest volume capacity, then move on to vehicles with smaller volume capacity
      </td>
    </tr>
  </tbody>
</Table>

* Step 4: Click **Save** for changes to take effect.
* By default, during the Route Plan Optimization process, the system will select vehicles with criteria ***Ascending by Weight capacity***, in which the system chooses the vehicles with the smallest weight capacity to deliver orders first during the Route Plan Optimization process

<Image title="4. Asc (ENG).png" alt={932} border={true} src="https://files.readme.io/8838a1f-4._Asc_ENG.png">
  Illustration (English)
</Image>

<Image title="4. Asc (VIE).png" alt={930} border={true} src="https://files.readme.io/8792744-4._Asc_VIE.png">
  Illustration (Vietnamese)
</Image>

* If you have Delivery Orders with large weight/large volume and you want to choose the vehicles with the largest capacity to fulfill these orders, please select 
* 1 - ***Prioritize vehicles Descending by Weight to optimize route*** if you want to choose Vehicles with the largest Weight capacity first to deliver Orders or, 
* 2 - ***Prioritize vehicles Descending by Volume to optimize route*** if you want to choose Vehicles with the largest Volume capacity first to deliver Orders
* After you select, the **Order Priority** checkbox will appear below. When you tick this checkbox, the **Prioritize Orders load bigger than ... Kg or ... m3** sub-setting will appear.

<Image title="1. Volume Order (ENG).png" alt={932} border={true} src="https://files.readme.io/d3897c7-1._Volume_Order_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Volume Order (VIE).png" alt={929} border={true} src="https://files.readme.io/e9ae0be-1._Volume_Order_VIE.png">
  Illustration (Vietnamese)
</Image>

* This sub-setting allows you to prioritize Orders load either by Weight (Kg) or by Volume (m3), regardless of your **Vehicle Priority** is by Weight or by Volume. This means, for example, when you choose to prioritize Vehicles by Weight,  you need not necessarily to prioritize Orders in Weight in the **Order Priority**; you can certainly choose to prioritize Orders in Volume. 

* When you enter a value into the fields, this sub-setting will let the system prioritize Orders with Volume/Weight bigger than a specific value entered in the fields, then the system will select the vehicles with the largest capacity first for orders exceeding the entered value. The value entered must be larger than 0 and can be decimal number.

* For example: If you want orders exceeding ***200 m3*** to be fulfilled by the vehicles with the largest ***Weight*** capacity,

* Step 1: Choose **Prioritize vehicles Descending by Weight**, 

* Step 2: Tick the checkbox **Order Priority**; 

* Step 3: In the line **Prioritize Orders load bigger than...Kg or m3**, please enter the value **200** into the field **...m3** and leave the field **... Kg** blank, 

* Step 4: Click **Save** for changes to take effect. 

* The system will gather all orders with Volume exceeding 200 m3 and select vehicles with the largest Weight capacity available to fulfill those orders in the Route Plan.

<Image title="1. Volume Order Priority (ENG).png" alt={930} border={true} src="https://files.readme.io/a47fdcc-1._Volume_Order_Priority_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Volume Order Priority 2 (VIE).png" alt={933} border={true} src="https://files.readme.io/288512f-1._Volume_Order_Priority_2_VIE.png">
  Illustration (Vietnamese)
</Image>

## Vehicle Priority Settings Explanation

* These priority settings are quite self-explanatory. Let's take the simple example below:
* The Depot has two active vehicles A and B. Vehicle A has the maximum carrying capacity to be ***120 kg; 1.2 m3***; while vehicle B has the maximum carrying capacity to be ***100 kg; 1 m3***
* A Customer places a ***60 kg; 0.6 m3*** Order 
* If the vehicle priority setting is ***Prioritize vehicles Descending by Weight/Volume to optimize route*** then vehicle A will be selected because it has higher weight and volume capacity compare to vehicle B. Vice versa, If the vehicle priority setting is ***Prioritize vehicles Ascending by Weight/Volume to optimize route*** then vehicle B will be selected because it has lower weight and volume capacity compare to vehicle A

## Configurations can be used with Vehicle Priority Configuration

* In the **Algorithms Settings**, there are configurations that can be used along with **Vehicle Priority** configuration
* Use Clustering
* Partner Clustering
* Hard Time Window
* Split Delivery
* Limit Number of Trips
* Limit Number of Shifts
* Time Balancing
* Auto Reduce Driver
* Use Split Route
* Use Cold Chain

<Image title="7. Config (ENG).png" alt={932} border={true} src="https://files.readme.io/8341a4d-7._Config_ENG.png">
  Illustration (English)
</Image>

<Image title="7. Config (VIE).png" alt={931} border={true} src="https://files.readme.io/5eb5de6-7._Config_VIE.png">
  Illustration (Vietnamese)
</Image>

* **Note**: **Vehicle Priority** configuration **CANNOT** be used with **Use Familiarity** configuration at the same time. If you tick the box **Use Familiarity**, the **Vehicle Priority** configuration will be disabled; users cannot enter any value or select options in the two grayed fields.

<Image title="6. Familiarity (ENG).png" alt={933} border={true} src="https://files.readme.io/46b55e8-6._Familiarity_ENG.png">
  Illustration (English)
</Image>

<Image title="6. Familiarity (VIE).png" alt={933} border={true} src="https://files.readme.io/057a2c0-6._Familiarity_VIE.png">
  Illustration (Vietnamese)
</Image>
