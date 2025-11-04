---
title: Configurations by Organization type
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
* After you have created the Organizations, you'll also have to enable certain configurations to make this model functional

## Process to Enable/Disable Configurations

* Navigate to **Organizations > Organization List** tab
* Click on the icon **Edit** :fa-pencil: of the appropriate Organization
* The Webform **Edit Organization** will appear. Please navigate to the tab **More Configuration** by clicking on its title
* The More Configuration tab is categorized into sections listed on the left side panel. Clicking on a section's title will navigate you to the configurations of that section. There are several methods to enable a configuration: clicking on the check box/radio button, input in the information fields, or sometimes a combination of both methods. After you have enabled the necessary configurations, click **Save** on the form to confirm the changes
* **Note**: After you have enabled the configurations, you should log out then log in to your account  in order for the configurations to become effective

<Image title="Ip3Vn6Uc9K.png" alt={1486} className="border" border={true} src="https://files.readme.io/33e238f-Ip3Vn6Uc9K.png" />

## Configurations for Manufacturer

## Model

* Setup exactly as in the image below

<Image title="bsBKVuUri6.png" alt={1472} className="border" border={true} src="https://files.readme.io/cea6da0-bsBKVuUri6.png" />

## Systems

### Approve Depot Order Config

<Image title="JU9jQRdwNN.png" alt={1450} className="border" border={true} src="https://files.readme.io/ef76d1b-JU9jQRdwNN.png" />

* This configuration will enable the Branch to allocate the following duties to separated User Groups: 
* 1 - Order Creating. This duty will be performed by the Order Creator User Group
* 2 - Order Inspecting and Approving. This duty will be performed by the Order Inspector User Group
* 3 - Route Planning. This duty will be performed by the Route Planner User Group

## Route

### Oversized Goods Restriction

* Requiredness: Optional
* This configuration will make the system check the Order's measurements (Length, Width, Height) during the Route Plan Optimization process to ensure that the vehicle's cargo space has enough space to carry the products

<Image title="AEJkPqJ28s.png" alt={744} className="border" border={true} src="https://files.readme.io/b448d4c-AEJkPqJ28s.png" />

## Transport

* Requiredness: Required
* This section lists the possible Depot type pair in which each Depot type (Of the three Depot types Internal Depot; Supplier Depot; Customer Depot) acts as the Origin and Destination end of a Sales Order. You can set up the Depot type that has to bear the Transport Service Price for Orders between each pair

<Image title="EtxBN5fpqr.png" alt={728} className="border" border={true} src="https://files.readme.io/3fdf97c-EtxBN5fpqr.png" />

* For example: The value under the **Origin** column is ***Supplier***, the value under the **Destination** column is ***Internal***, the value under the **Service Payer** column is ***Internal***. That means for Orders that have the products picked up at a Supplier Depot and dropped off at an Internal Depot, the Internal Depot will have to pay the Transport Service prices of those Orders

## Configurations for Branch

## Route

### PDP Order

* Requiredness: Required
* This configuration will enable the PDP model for the Branch

### Split Delivery

* Requiredness: Optional
* This configuration will allow over-capacity Orders to be automatically split during the Route Plan Optimization process

## Algorithm

### Hard Time Windows

* Requiredness: Optional
* This configuration Hard time windows constraint for all Depots under the direct management of the Branch
* Read more about this configuration in the following article:

## Configurations for Depot

## Mobile

### Prevent Assign Task for Depot

* Requiredness: Optional
* This configuration should be enabled for Depots that belong to the Supplier (The Depot Type is ***Supplier Depot***). Upon enabling, the system will stop generating tasks on the Mobile app of those Depots' warehousemen
