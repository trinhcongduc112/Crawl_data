---
title: Why I cannot find a solution when optimize the route planning?
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: basic
      slug: how-to-check-reason-for-missing-order
      title: Missing order reasons and how to resolve them?
---
When you cannot find a solution to optimize your route planning, please remember to check the [Order] tab beforehand to make sure the orders of the planning date were existed on the system.

* To check the orders, please go to [Orders] and change the Date to your Date of planning. 

![1920](https://files.readme.io/045452f-solution_1.png "solution 1.png")

* If the orders of that date have not been existed, please create new orders by using Web form or Excel file before re-optimizing the route. In case you do not know how to create new Order, please find more information [here](https://docs.abivin.com/docs/pdp-outsourcing-fleet-manage-sales-orders).

![1920](https://files.readme.io/e41f7c0-solution_2.png "solution 2.png")

In case your orders of the date planning existed but you still could not find the solution to optimize the route, please check these common circumstances below to find which your situation belong to.

## 1. The coordinate of the warehouse and the customer are empty.

:fa-angle-right: Solution: Add coordinate of the warehouse and the customer.

**1.1. Check the coordanite of the customer.**\
**Step 1:** Go to ers] and c and choose Tab Customers\
**Step 2:** Click on the  butto button :fa-pencil:.\
**Step 3:** Check the coordinate of the Customer and add latitude & longitude if the coordinate is left empty. Then click .
[blo.

![1920](https://files.readme.io/85a4d3b-pic_1.2.1.png "pic 1.2.1.png")

**1.2. Check the coordinates of the warehouse.**\
**Step 1:** Go to the ations].
**Step.\
**Step 2:** Click on the utton  button :fa-pencil: for each warehouse.\
**Step 3:** Check the coordinate of the Warehouse and add latitude & longitude if the coordinate is left empty. Then click [block.

![1920](https://files.readme.io/bfc108d-pic_1.2.2.png "pic 1.2.2.png")

## 2. The operating time of the vehicle doesn't match the customers'.

> ❗️ Wrong example
>
> The operating time of the vehicle is from 8 am to 8 pm, while the customer's is from 9 pm to 11 pm.

:fa-angle-right: Solution: Choose a vehicle has the same operating time with the customer.

> 👍 Correct example
>
> The vehicle with operating hours from 8 am to 9 pm is compatible with customers with operating hours between 10 am and 9 pm.

* Follow these steps to check the operating time of the vehicle:\
  **Step 1:** Click "Transportation".\
  **Step 2:** Fill the start time and stop time of the vehicle.

![800](https://files.readme.io/75a462f-tWojnRbFWeyaSZmXTMSZWhCfZIU1X8ywZQ.png "tWojnRbFWeyaSZmXTMSZWhCfZIU1X8ywZQ.png")

## 3. Wrong format of Start & End time, Lunch Break Start & End time.

> ❗️ Wrong example
>
> The start time is 6, the stop time is 20:0.

:fa-angle-right: Solution: Reconfigure the correct format.

> 👍 Correct example
>
> The start time is 6:00, the stop time is 23:59.

![1920](https://files.readme.io/3f18fda-pic_4.png "pic 4.png")

## 4. Min time, Max time of the depot in wrong format (seconds, hour).

:fa-angle-right: Solution: As the correct format is minutes, re-check and fix Min time & Max time to the correct format as stated in these steps below:\
**Step 1:** Go to "Organizations".\
**Step 2:** Click the  depot button :fa-pencil: of depot.\
**Step 3:** Choose "More Configuration".\
**Step 4:** Click on t the Min .\
**Step 5:** Input the Min time and Max time (An integer and greater than 0).

![1920](https://files.readme.io/8265b0e-pic_9.png "pic 9.png")

## 5. Minumum Vehicle Fill Rate is set up equal to 0% when using config Cluster by Drawing.

:fa-angle-right: Solution: When you use the config "Clustering by Drawing", the "Minimum Vehicle Fill Rate" must be greater than 0%. If not, the system cannot find solution to optimize the route. Follow these instructions below to modify the above data:\
**Step 1:** Go to the k on the [Edit.\
**Step 2:** Click on the r Bran button :fa-pencil: of your Branch.\
**Step 3:** Choose on [Algorithm] on the and click on f the table on the left column of the table.\
**Step 4:** Scroll down until you see "Use Clustering", then fill a number except 0 in the "Minimum Vehicle Fill Rate" and s": [
.

![1920](https://files.readme.io/d5341d7-solution.png "solution.png")

## 6. No Drawings created when using config Cluster By Drawings

:fa-angle-right: Case: After optimizing the route plan, the system displays a notification of "When using Cluster By Drawing, Customers must be located in a user-drawn cluster".

<Image title="Doc2.png" alt={1920} src="https://files.readme.io/15006cc-Doc2.png">
  Popular situation when using config "Cluster By Drawing"
</Image>

<Image title="Doc1.png" alt={1920} src="https://files.readme.io/ea77309-Doc1.png">
  Popular situation when using config "Cluster By Drawing"
</Image>

:fa-angle-right: Solution: Despite using config Cluster By Drawing in Branch, no drawings were created in the geographic clusters for the wanted customer group which belonged customers have need-to-plan orders. 

![1920](https://files.readme.io/bd7ec85-doc3.png "doc3.png")

:fa-angle-right: Solution: Please follow these instructions to re-check whether your customer group has area drawings and add new drawings if that group does not have any before re-optimizing the route plan.\
**Step 1:** Go to p].
**Step and navigate tab Depot in the Dro.\
**Step 2:** Select your Depot in the Drop down list before click on the  clusters. button to view the geographical clusters.\
**Step 3:** Navigate the Group Cluster and your Customer Group code to check whether its drawing exists.\
**Step 4:** In case no drawing exists, create new ones before re-optimizing. If you don't know how to manage user-drawn geographical clusters, please read more \[here]\(Manage User-drawn Geographical Clusters).

![1920](https://files.readme.io/b351f14-doc4.png "doc4.png")

## 7. Customers' Open and Close time are not input when using config Hard Time Window

:fa-angle-right: Reason: When using config Hard Time Window, Customers' Open and Close time fields are required for successful optimization. Therefore, if these fields are empty, no results are returned after optimizing the route plan. In order to re-check the case, please follow the below instructions:

* Step 1: Go to rders that and select your Depots which have orders that need to be planned and Export the Data as followed.

![1920](https://files.readme.io/c00e68e-pic1.png "pic1.png")

* Step 2: In the exported file, navigate columns Open & Close time to check whose are missing these fields. Please input the missing data before re-uploading the file to the Website. 

![1920](https://files.readme.io/405a14b-pic2.png "pic2.png")

* Step 3: Optimize the route plan after updating Partners 'data.

## 8. There is no order available on the date of the route plan.

:fa-angle-right: Case: Customers see the notice showing that ***"There is no order available"***.

![1920](https://files.readme.io/04be75c-1111.png "1111.png")

:fa-angle-right: Reason: There is no order available on the date of the route plan.

![1917](https://files.readme.io/f73e481-121.png "121.png")

:fa-angle-right: Resolution: Input the orders information to plan the route. You can learn how to create an order on our system [here](https://docs.abivin.com/docs/vrp-outsourcing-fleet-manage-sales-orders).
