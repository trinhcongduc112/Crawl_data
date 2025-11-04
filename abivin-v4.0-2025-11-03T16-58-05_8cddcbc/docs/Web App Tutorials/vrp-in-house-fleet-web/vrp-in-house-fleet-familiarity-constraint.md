---
title: Familiarity Constraint
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
* In real operation, a company may allocate the customers to their vehicle fleet based on the familiarity relationship between each vehicle with the customers. The vehicle will prioritize delivering to the customers that have familiarity relationships with them first. After delivering to the customers that have familiarity relationships with them, the vehicles will continue delivering to other non-familiar customers if they still have enough working time and capacity
* This routing plan is defined as **Master Delivery Plan** (Abbreviated as **MDP**)
* To optimize the routes with the above constraint, in Abivin vRoute, we introduce the **Familiarity** configuration
* To use this configuration, please follow the steps below:

## Compulsory Configuration

* Navigate to **Organizations > Organization List** tab
* Click **Edit** :fa-pencil: icon of the **Branch**
* On the **Update Organization** form, navigate to the **More Configurations > Algorithm** sub-tab and tick the **Use Familiarity** checkbox to enable the Familiarity Constraint routing algorithm
* Click **Save** to confirm the change

<Image title="3Pvyce3UHr.png" alt={743} className="border" border={true} src="https://files.readme.io/7319292-3Pvyce3UHr.png" />

* After you have enabled this algorithm configuration, you'll then need to:
* 1 - Assign MDP codes to the Customers
* 2 - Assign Customers' MDP codes to the Vehicles

## Assign MDP code to the customer

* There are two methods to assign MDP codes to Customers: Web form and Excel template

### Assign MDP codes to Customers on Web form

* Navigate to **Partners > Customers** tab
* Click **Edit** :fa-pencil: icon of the desired customers
* On the **Update Customer** form, navigate to **Sales Area** sub-tab. Insert a unique MDP code for the Customer. You should copy this MDP code to use later on
* Click **Save** to confirm the change

<Image title="TP2QjvpfyU.png" alt={949} className="border" border={true} src="https://files.readme.io/580cdac-TP2QjvpfyU.png" />

### Assign MDP codes to Customers on Excel template

* On the Excel template, input the MDPs code into **MDP** cells

<Image title="JjNNb9KrBT.png" alt={77} className="border" border={true} src="https://files.readme.io/75f45cc-JjNNb9KrBT.png" />

### MDP code format

* MDP codes can only consist of letters, numbers and dash symbols. For example: ***MDP\_code\_01*** is valid, ***MDP\@code!01*** is invalid
* The MDP codes of Customers must be unique. No two Customers can have the same MDP code
* One customer can only have ***one MDP code***

## Assign MDP codes to the vehicles

* You can assign the MDP codes of multiple customers to a single vehicle, or assign the MDP code of a single customer to multiple vehicles
* There are two methods to assign MDP codes to vehicles: Web form and Excel template

### Assign MDP codes to vehicles on Web form

* Navigate to **Transportation > Vehicle List** tab
* Click **Edit** :fa-pencil: icon of the desired vehicle
* On the **Update Vehicle** form, scroll down until you see the **MDP** field. Input the MDP code of the Customer into this field.  If a vehicle is assigned multiple MDP codes, separate two adjacent MDP codes by a comma, for example: ***MDP\_code\_1,MDP\_code\_2***
* Click **Save** to confirm the change. Repeat these steps for other vehicles

<Image title="A3SbO7hlX6.png" alt={778} className="border" border={true} src="https://files.readme.io/58fbc55-A3SbO7hlX6.png" />

* Alternatively, you can directly assign MDP codes to vehicles right on the Vehicle List screen
* First, you need to display the MDP column. To do that, click the **Columns** button on the top right corner of the vehicle list then select this column from the drop-down list

<Image title="xca1xkbTTp.png" alt={1703} className="border" border={true} src="https://files.readme.io/c421fed-xca1xkbTTp.png" />

* After the MDP column is displayed, click on the MDP field of each vehicle. Input the MDP code into the pop-out form.  If a vehicle is assigned multiple MDP codes, separate two adjacent MDP codes by a comma, for example: ***MDP\_code\_1,MDP\_code\_2***. After that, click the :fa-check-square: icon on the form to confirm assigning the MDP code(s) to that vehicle

<Image title="X2lK9iGNCA.png" alt={1165} className="border" border={true} src="https://files.readme.io/de03a0c-X2lK9iGNCA.png" />

### Assign MDP codes to vehicles on Excel template

* Input the MDP code to the **MDP** cell of each vehicle
* If a vehicle is assigned multiple MDP codes, separate two adjacent MDP codes by a comma and a space. For example: ***MDP\_code\_1, MDP\_code\_2***

<Image title="2019-11-01 22_08_12-Window.png" alt={191} className="border" border={true} src="https://files.readme.io/cb378b7-2019-11-01_22_08_12-Window.png" />

## Route Plan Optimization Process with Familiarity Constraint

* After setting all the above, you can perform Route Plan Optimization as usual
* The optimization process will return the most optimized routes, satisfying the MDP configuration set up earlier
* In the scenario a customer has a familiarity relationship with a vehicle, but that vehicle doesn't have enough capacity and/or working time to deliver orders of that customer, the system will automatically assign these orders to other vehicles that have enough capacity and working time, regardless of whether or not those vehicles have familiarity relationship with this customer (As described at the beginning of this article)
* To see whether a customer has the familiarity relationship with the vehicle that delivers to that customer, click on the block of that customer on the vehicle timeline. On the panel that appears right side of the screen, see the value of the **Familiarity** field:
* The value is ***Yes***: The vehicle has a familiarity relationship with the customer

<Image title="2019-11-01 18_13_54-Abivin vApp.png" alt={1907} className="border" border={true} src="https://files.readme.io/2ed413c-2019-11-01_18_13_54-Abivin_vApp.png" />

* The value is ***No***: The vehicle doesn't have a familiarity relationship with the customer

<Image title="2019-11-01 18_15_03-Abivin vApp.png" alt={1907} className="border" border={true} src="https://files.readme.io/569aef5-2019-11-01_18_15_03-Abivin_vApp.png" />

## Calculate Familiarity ratio

### Calculate Familiarity ratio of a single vehicle

* The Familiarity ratio of a vehicle is calculated by the following formula
* ***The number of customers who have familiar relationships with the selected vehicle/The total number of customers assigned to the selected vehicle***
* For example: A vehicle delivers to four customers, three of whom have familiar relationships with that vehicle
* The Familiarity ratio of that vehicle will be ***3/4 x 100% = 75%***

<Image title="2019-11-01 21_17_02-Window.png" alt={1914} className="border" border={true} src="https://files.readme.io/e30822f-2019-11-01_21_17_02-Window.png" />

### Calculate Familiarity ratio of a whole Route Plan

* The Familiarity ratio of a whole Route Plan is calculated by the following formula
* ***The number of customers who have familiar relationships with the vehicles utilized in that Route Plan/The total quantity of customers whose orders are successfully optimized in that Route Plan***
* For example: The Route Plan consists of two vehicles delivering to five customers, among whom three customers have familiarity relationships with one vehicle
* The Familiarity ratio of that routing plan will be ***3/5 x 100% = 60%***

<Image title="2019-11-01 22_00_33-Window.png" alt={1914} className="border" border={true} src="https://files.readme.io/86f14be-2019-11-01_22_00_33-Window.png" />
