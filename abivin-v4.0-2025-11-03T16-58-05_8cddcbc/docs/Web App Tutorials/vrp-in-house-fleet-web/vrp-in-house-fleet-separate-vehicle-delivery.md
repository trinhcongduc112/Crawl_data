---
title: Separate Vehicle Delivery (Split Order)
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
* By default, if a Customer places multiple Orders, the system will always assign all those Orders to a single Vehicle
* This article will instruct you on how to configure so that each Order will be delivered by a separate vehicle, by setting up the Orders as **Split Orders**

## Compulsory Preparation

* You must disable the configuration **Split Delivery**. To disable the configuration Split Delivery, follow the steps below
* * Step 1: Navigate to tab **Organization**
* * Step 2: Edit information for a Branch (the organization must be a Branch)
* * Step 3: Click the tab **More Configuration > Algorithm** 
* * Step 4: Scroll down and untick the box of **Split Delivery**
* * Step 5: Click **Save** for changes to take effects.

<Image title="1. Split Delivery (Turned Off) (ENG).png" alt={933} src="https://files.readme.io/68137d7-1._Split_Delivery_Turned_Off_ENG.png">
  Disable the configuration Split Delivery (English)
</Image>

<Image title="1. Split Delivery (Turned Off) (VIE).png" alt={931} src="https://files.readme.io/cc705d6-1._Split_Delivery_Turned_Off_VIE.png">
  Disable the configuration Split Delivery (Vietnamese)
</Image>

## Create Orders

### Create Orders using Web form

* During the Order creation process using Web form, tick the **Separate Vehicle** checkbox for *Every Order* placed by the same Customer

<Image title="uY2RTGPner.png" alt={1265} border={true} src="https://files.readme.io/5c9d40c-uY2RTGPner.png">
  Separate Vehicle (English)
</Image>

<Image title="2. Split Delivery.png" alt={1570} src="https://files.readme.io/7e27cdd-2._Split_Delivery.png">
  Separate Vehicle (Vietnamese)
</Image>

### Create Orders using Excel template

* During the Order creation process using Web form, input the value ***TRUE*** into the **Splitted** cell of *every Order* placed by the same Customer

<Image title="Splitted.png" alt={1687} border={true} src="https://files.readme.io/aaa1645-Splitted.png">
  Splitted (Excel Form) (English)
</Image>

<Image title="Splitted (VIE).png" alt={1819} src="https://files.readme.io/a9720b0-Splitted_VIE.png">
  Splitted (Excel Form) (Vietnamese)
</Image>

## Route Plan Optimization process

* During the Route Plan Optimization process, each Split Order of the same Customer will be assigned to a different Vehicle

<Image title="Seprate Vehicle (ENG).png" alt={1418} border={true} src="https://files.readme.io/7e6a6fe-Seprate_Vehicle_ENG.png">
  Separate Vehicle Comparison (English)
</Image>

<Image title="Seprate Vehicle (VIE).png" alt={1076} src="https://files.readme.io/c560ed7-Seprate_Vehicle_VIE.png">
  Separate Vehicle Comparison (Vietnamese)
</Image>
