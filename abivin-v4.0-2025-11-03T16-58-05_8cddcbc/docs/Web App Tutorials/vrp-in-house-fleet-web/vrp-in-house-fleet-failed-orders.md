---
title: Failed Orders
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
## Failed Orders Definition

* Failed Orders are Orders that were successfully put into the optimized Delivery route during the Route Optimization process. However, during the Delivery process, the drivers could not deliver them to the customers for various reasons. On Order list, their Fulfillment Status are ***Unfulfilled***

## Compulsory Configurations

* You need to enable the following configuration at the **Branch**: **Allow Re-delivery Order** (Can be found in **More Configuration > System** sub-tab)
* The CRUD rights of the Administrator User group also needs to be updated. For module **Orders**, the check box under the column **Integration – Input** must be ticked

<Image title="2.png" alt={848} border={true} src="https://files.readme.io/2d63ffe-2.png">
  Illustration Image (English)
</Image>

<Image title="1.png" alt={848} src="https://files.readme.io/db7ada7-1.png">
  Illustration Image (Vietnamese)
</Image>

* You can set a list of reasons why an Order was failed to be delivered to the customer, so that the drivers can select on their Mobile app if they face that situation
* To configure the reasons for Failed Orders, follow the steps below:
* Navigate to **Organizations > Organization List** tab
* Click on **Edit** :fa-pencil: icon of the ***Branch*** you want configure the reasons

<Image title="TAKd62YsJO.png" alt={1920} border={true} src="https://files.readme.io/aa3fc98-TAKd62YsJO.png">
  Illustration Image (English)
</Image>

<Image title="5.png" alt={1920} src="https://files.readme.io/5582267-5.png">
  Illustration Image (Vietnamese)
</Image>

* On **Edit Organization** form, click on **More Configurations** tab. On that tab, scroll on the way down until you see **Reason settings** section
* Click on the button **Add Reason** :fa-plus:. As you click on this button, a new row will appear on the list below. This is where you input the information of the reason
* The section [**Failed Order reason information**](https://docs.abivin.com/docs/vrp-in-house-fleet-failed-orders#section-failed-order-reason-information) will help you specify the information of a reason
* You can repeat the steps above to add more reasons

<Image title="2.png" alt={749} border={true} src="https://files.readme.io/65207c8-2.png">
  Illustration Image (English)
</Image>

<Image title="1.png" alt={751} src="https://files.readme.io/e9e7b48-1.png">
  Illustration Image (Vietnamese)
</Image>

* After you have created all reasons, click **Save** to save the changes

## Failed Order reason information

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description & Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        REASON CODE
      </td>

      <td>
        **1. Description:**\
        Management code assigned to the reason being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Reason 1" is invalid; "Reason\_1" is valid
      </td>
    </tr>

    <tr>
      <td>
        REASON NAME
      </td>

      <td>
        **1. Description:**\
        Content of the reason. The value input into this field will display on the Mobile app for the driver to select\
        **2. Input rules:**\
        Format: Free-form\
        For example: "The store has closed"
      </td>
    </tr>

    <tr>
      <td>
        ALLOW RE-DELIVERY
      </td>

      <td>
        **1. Description:**\
        Specify whether the orders that were failed to deliver due to the reason being created can be retrieved and planned on a future date or not\
        **2. Input rules:**\
        Choose the following option to allow the failed orders linked with the reason being created to be retrieved from the past date and planned on a future date: **YES**\
        Choose the following option to not allow failed orders linked with the reason being created to be retrieved from the past date and planned on a future date: **NO**
      </td>
    </tr>
  </tbody>
</Table>

## Retrieve Failed Orders from past dates

* Navigate to **Orders > Sales Orders** tab
* Hover your mouse over the icon :fa-plus-circle:, then click on the icon **Fetch old order** :fa-refresh:
* The form **Get Past Order** will appear
* On this form, click on the field **Branch**. From the drop down menu, select the Branch from which you want to retrieve Failed Orders
* Next, click on the calendar icon :fa-calendar-o: under the text **Get Failed Orders Date**. On the drop down calendar, select the date on which there were Failed Orders
* Then, click on the calendar icon :fa-calendar-o: under the text **Delivery Date**. On the drop down calendar, select the date on which you want to replan the Failed Orders
* **(Important)** Click on the check box **Not completed delivery** to specify that you want to retrieve Failed Orders
* (Optional) You can also click on the check box **Missing orders** to also retrieve Missing Orders from the same selected date as the Failed Orders
* If you want to assign the Failed Orders to the same drivers who delivered them in the past date, click on the check box **Re-assigned**. If you want to assign these Failed Orders to other drivers, don't click on that check box
* Finally, click on the button **Fetch Order**
* The system will immediately find the Failed Orders from the selected past date, then create ***new Orders*** that retain the same ***Order Codes*** attribute as those Failed Orders, and put them to the Order list of the selected future date
* On the Order list, Orders that were created based on Failed Orders will be highlighted with green color

<Image title="download.png" alt={1888} border={true} src="https://files.readme.io/333d4df-download.png">
  Illustration Image (English)
</Image>

<Image title="3.png" alt={1919} src="https://files.readme.io/fdb7b41-3.png">
  Illustration Image (Vietnamese)
</Image>

* See the illustration below to have a better understanding of this function

<Image title="retrieve failed orders.gif" alt={1904} border={true} src="https://files.readme.io/623f1ff-retrieve_failed_orders.gif">
  Illustration GIF (English)
</Image>

<Image title="6661515151.gif" alt={1920} src="https://files.readme.io/77bbffd-6661515151.gif">
  Illustration GIF (Vietnamese)
</Image>

## Route Plan Optimization Process

* During the Route Plan Optimization Process, the failed Orders from past dates will always be prioritized to be put into the optimized Delivery Route before the remaining Orders
* On the Timeline panel, the time blocks of the Stops (Customers) whose Order also contain failed Orders from past dates will have an inner mild green color

<Image title="cs3bbjf8T6.png" alt={933} className="border" border={true} src="https://files.readme.io/3537cfe-cs3bbjf8T6.png" />
