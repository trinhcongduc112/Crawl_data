---
title: Service Time Calculation
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
* In Abivin vRoute system, the Service Time is a time concept that refers to the following two time periods that you see during the Route Plan optimization process:
* 1 - The time period to load Products at the Depot at the beginning of a Delivery Trip, and
* 2 - The time period to unload Products at a Customer's receiving location
* There are several Service Times determination mechanisms in Abivin vRoute system:
* Mechanism 1 - Automatic Service Time. This is the default Service Time mechanism of the system
* Mechanism 2 - Manual Customer Service Time. This mechanism is used for the Customers who regularly change their Service Times
* Mechanism 3 - Specialised Service Time. This is a set of several custom Service Time mechanisms that are optimized for certain User accounts

## Service Time Related Concepts

* Firstly, there are some time-related concepts that we need you to get familiar with:
* 1 - **Base Service Time**. This is a time configuration at the **Branch**. This configuration defines a fixed time period to load/unload a fixed amount of products. The amount could either be weight or volume
* 2 - **Service Time Window**. The Service Time Window refers to the time window constraints that the manufacturing Depots and the Customers' receiving locations impose on every Vehicle when loading/unloading Products. The Vehicles must always load/unload products within the imposed time window constraints, no more and no less
* 3 - **Service Time**. As mentioned at the beginning of this article, this is the loading/unloading time period that the system applies to the Vehicles during the Route Plan optimization process, the ones you see on the optimized Route Plan. The Service Time is determined by comparing the following two numbers:
* 3.1 - The result of the multiplication between the Base Service Time and the amount of Products that a Vehicle is assigned to load/unload at a location (The manufacturing Depot or the Customer's receiving location) during the Route Plan optimization process, and
* 3.2 - The Service Time Window imposed by that location
* Now that you've understood these time concepts, let's move on to configure them

## Automatic Service Time

* The Automatic Service Time mechanism is the default Service Time mechanism of the Abivin vRoute system
* To use this Service Time mechanism, you will need to perform the following setup before proceeding to the Route Plan optimization process:
* 1 - Set up the Base Service Time at the Branch
* 2 - Set up the Service Time Window at the Depot
* 3 - Set up the Service Time Window at the Customers

### Set Up The Base Service Time At The Branch

* To set up the Base Service Time at the Branch, please follow the steps below:
* Navigate to the **Organizations > Organizations** tab
* Click the **Edit** icon :fa-pencil: of the Branch you want to set up
* On the **Update Organization** form, navigate to the **More Configuration > Un(loading) Time** sub-tab
* At the top of this sub-tab, you will see the **Service Times** section. In this section, there is a phrase that reads: ***Need\[ ] minutes for loading and unloading of packages weighting \[ ] kg***. This is where you can set up the Base Service Time based on weight (kilogram, kg)

<Image title="deN4ClBiHT.png" alt={745} border={true} src="https://files.readme.io/2f425e3-deN4ClBiHT.png">
  Illustration (English)
</Image>

<Image title="ccjd9F8BAN.png" alt={745} border={true} src="https://files.readme.io/f645feb-ccjd9F8BAN.png">
  Illustration (Vietnamese)
</Image>

* If you tick the **Use Volume** checkbox, this phrase will change to ***Need\[ ] minutes for loading and unloading of packages volume \[ ] m3***. This will allow you to set up the Base Service Time based on volume (cubic meter, m3)

<Image title="DkobrL8XeO.png" alt={745} border={true} src="https://files.readme.io/c52ab46-DkobrL8XeO.png">
  Illustration (English)
</Image>

<Image title="mf08lf47e1.png" alt={745} border={true} src="https://files.readme.io/ec0475f-mf08lf47e1.png">
  Illustration (Vietnamese)
</Image>

### Set Up The Service Time Window at the Depot

> 📘 The Service Time Window can also be set up at the Sun and the Crossdock

* The Service Time Window of a Depot consists of the Minimum Loading Time and the Maximum Loading Time (In minutes)
* To configure the Service Time Window of a Depot, please follow the steps below
* Navigate to the **Organizations > Organizations** tab
* Click the **Edit** icon :fa-pencil: of the Depot you want to set up
* On the **Update Organization** form, navigate to the **More Configuration > Loading Time** sub-tab
* Input the Minimum Loading Time into the **Loading Min Time** field and the Maximum Loading Time into the **Loading Max Time** field
* Click **Save** to confirm the change

<Image title="b7wBrv9ysc.png" alt={744} border={true} src="https://files.readme.io/3c8cdc1-b7wBrv9ysc.png">
  Illustration (English)
</Image>

<Image title="3iYD441hkL.png" alt={743} border={true} src="https://files.readme.io/690b75b-3iYD441hkL.png">
  Illustration (Vietnamese)
</Image>

* If you use the Excel import file to create the Depot, input the Minimum Loading Time and the Maximum Loading Time into the **Min Time (minute)** and **Max Time (minute)** cells of the Depots being created, respectively

### Set Up The Service Time Window At The Customers

* The Service Time Window of a Customer consists of the Minimum Unloading Time and the Maximum Unloading Time (In minutes) 
* To configure the Service Time Window of a Customer, please follow the steps below
* Navigate to the **Partners > Customers** tab
* Click the **Edit** icon :fa-pencil: of the Customer you want to set up
* On the **Update Customer** form, input the Minimum Unloading Time and the Maximum Loading Time of the Customer into the **MinTime Unloading** and the **MaxTime Unloading** fields, respectively
* Click **Save** to confirm the change

<Image title="7Nd5JRNdlU.png" alt={955} border={true} src="https://files.readme.io/599ec80-7Nd5JRNdlU.png">
  Illustration (English)
</Image>

<Image title="crviDKn2dz.png" alt={952} border={true} src="https://files.readme.io/8079f07-crviDKn2dz.png">
  Illustration (Vietnamese)
</Image>

* If you use the Excel import file to import new Customers or update existing Customers, input the Minimum Unloading Time and the Maximum Loading Time of the Customer into the **Min Time** and the **Max Time** cells, respectively
* We will use the following example throughout the content of this article: 
* Three Customers John; Jane and Michael all have the same Service Time Window: ***10 to 30 minutes***
* Now that you have set up the necessary configurations, you can move on to the Route Plan optimization process. Below we will describe how the system will determine the Service Time using these configurations

### Automatic Service Time Determination Method

* As mentioned above, during the Route Plan optimization, the Service Time of a Vehicle at the Depot and a Customer's receiving location will be determined by comparing the following two values:
* 1 - The result of the multiplication between the Base Service Time and the amount of Products to be loaded/unloaded, and
* 2 - The Service Time Window
* There can be three possible scenarios:
* Scenario 1: The multiplication result is less than the Minimum Loading/Unloading Time of the Service Time Window => The Service Time will equal the Minimum Loading/Unloading Time
* Scenario 2: The multiplication result is larger than the Maximum Loading/Unloading Time of the Service Time Window => The Service Time will equal the Maximum Loading/Unloading Time
* Scenario 3: The multiplication result is within the Service Time Window => The Service Time will equal that multiplication result
* We will use the following example to demonstrate this mechanism:
* The Base Service Time at the Branch is set up as follows: ***Need 0.05 minutes for loading and unloading of packages weighting 1 kg***
* The Depot's Service Time Window is: ***From 10 minutes to 30 minutes***
* Three Customers John, Jane, and Michael have the same Service Time Window: ***From 10 minutes to 30 minutes***
* Customer John places a total of ***100 kilograms*** of Products 
* Customer Jane places a total of ***1000 kilograms*** of Products 
* Customer Michael places a total of ***500 kilograms*** of Products
* During the Route Plan optimization process, three Vehicles are utilized. Vehicle A is assigned to deliver to Customer John; Vehicle B is assigned to deliver to Customer Jane; Vehicle C is assigned to deliver to Customer Michael
* We will now see how the system determine the Service Time of these Vehicles at the Depot and at the three Customers' receiving locations
* First, let's start with Vehicle A
* The Service Time of Vehicle A at the Depot will be determined by comparing the following two values:
* 1 - The result of the multiplication between the Base Service Time and the amount of Products to be loaded onto Vehicle A at the Depot, which is ***0.05 x 100 / 1 = 5 minutes***, and 
* 2 - The Service Time Window of the Depot, which is ***From 10 minutes to 30 minutes***
* According to the above mechanism, the multiplication result is less than the Depot's Minimum Loading Time, 10 minutes, therefore the Service Time of Vehicle A at the Depot will be the Depot's Minimum Loading Time, ***10 minutes***
* In the same manner, the Service Time of Vehicle A at Customer John's receiving location will ultimately be ***10 minutes***
* Next is Vehicle B
* The result of the multiplication between the Base Service Time and the amount of Products to be loaded onto Vehicle B at the Depot is ***0.05 x 1000 / 1 = 50 minutes*** 
* According to the above mechanism, the multiplication result is larger than the Depot's Maximum Loading Time, 30 minutes, therefore the Service Time of Vehicle B at the Depot will be the Depot's Maximum Loading Time, ***30 minutes***
* In the same manner, the Service Time of Vehicle B at Customer Jane's receiving location will ultimately be ***30 minutes***
* Last is Vehicle C
* The result of the multiplication between the Base Service Time and the amount of Products to be loaded onto Vehicle C at the Depot is ***0.05 x 500 / 1 = 25 minutes*** 
* According to the above mechanism, the multiplication result is within the Depot's Service Time Window, from 10 to 30 minutes, therefore the Service Time of Vehicle C at the Depot will be the multiplication result, ***25 minutes***
* In the same manner, the Service Time of Vehicle C at Customer Michael's receiving location will ultimately be ***25 minutes***

## Manual Customer Service Time

* The Manual Customer Service Time mechanism is used for Customers whose Service Time tend to change regularly
* To use this Service Time mechanism, you would need to do the following things:
* 1 - Enable the **Use Service Time** configuration at the Branch
* 2 - Input the Manual Service Time for the Customers during the Order creation process

### Enable Use Service Time Configuration

* To enable the **User Service Time** configuration at the Branch, please follow the steps below:
* Navigate to the **Organizations > Organizations** tab
* Click the **Edit** icon :fa-pencil: of the Branch you want to set up
* On the **Update Organization** form, navigate to the **More Configuration > Algorithm** sub-tab
* Tick the **Use Service Time** checkbox
* Click **Save** to confirm the change

<Image title="K9nwk4suxt.png" alt={743} border={true} src="https://files.readme.io/9130539-K9nwk4suxt.png">
  Illustration (English)
</Image>

<Image title="3Ocrjbnmlv.png" alt={742} border={true} src="https://files.readme.io/f936150-3Ocrjbnmlv.png">
  Illustration (Vietnamese)
</Image>

### Input Customer Manual Service Time

> ❗️ Only Use The Order Excel Import File!
>
> For the Customers who use this Service Time mechanism, you need to create their Orders using the Order Excel import file, since the Order creation Webform doesn't have the Service Time input field

* In the Order Excel import file, input the Service Time of the Customer into the **Service Time (minutes)** cell
* If the Customer places multiple Orders with the same Order Date attribute, the value input into this cell must be the same for all of those Orders
* For example, in the illustration image below, the Customer places three Orders with the same Order Date attribute. The Service Time of the Order must be the same across all these Orders

<Image title="a2IVPHcQlA.png" alt={714} className="border" border={true} src="https://files.readme.io/1f305fa-a2IVPHcQlA.png" />

### Manual Service Time Determination Method

* During the Route Plan optimization process, the system will compare the Service Time that you have input in the Order Excel import file against the Service Time Window of the Customer to determine the Service Time of that Customer
* The comparison method is similar to the Automatic Service Time determination method. According to that, there will be three possible scenarios:
* Scenario 1: The Manual Service Time is less than the Minimum Unloading Time of the Customer's Service Time Window => The Service Time will equal the Customer's Minimum Unloading Time
* Scenario 2: The Manual Service Time is larger than the Maximum Unloading Time of the Customer's Service Time Window => The Service Time will equal the Customer's Maximum Unloading Time
* Scenario 3: The Manual Service Time is within the Customer's Service Time Window => The Service Time will equal the Manual Service Time

## Multi-Depot Carrier Service Time

> ❗️ The Service Time formulas in this section are specialized for certain User accounts

* The Service Time formulas in this section are specialized for certain User accounts. They will define the following parameters:
* **Travel Time**: For some organizations, the delivery vehicles might need to pick up products at different Depots before delivering the products to the customers. The travel time between the Depots therefore will need to be taken into account when calculating the Loading Time
* **Lunch Break Time**: The time window during which the Depots take lunch break. During the lunch break time, the vehicles are not allowed to load products at the Depots
* **Loading Time Per Product Unit**: The time period to load a product item at the manufacturing Depots. This time period is independent of the product category
* **Unload Time per Unit**: The time period to unload a product item at the customer destination. This time period is dependent on the product category
* The Loading Time of any delivery vehicle at the manufacturing warehouses will be determined by comparing the Pre-adjusted Loading Time against the Loading Time Window of the warehouse\
  Pre-adjusted Loading Time = Travel Time + Loading Time (per product unit) x Product unit quantity + Remaining Lunch Time

## Custom Loading Time at Depot

* **Purpose of this configuration:** Loading time among depots can vary, hence, making time window constraint sometimes inappropriate when it comes to loading goods on vehicles. Therefore, you may need to customize the loading time for specific depots.

* To enable this configuration, please follow these steps below

* Step 1: You have to enable the configuration **Enable Loading time at Depot** in the branch that the Depot being changed is subject to before moving on. To see how to enable this configuration at Branch, click here for more instruction [Configuration Un(loading) Time](doc:configuration-unloading-time) ]

* Step 2:  Navigate to tab **Organizations**. In the list of organizations, choose a Depot for which you want to enable this configuration.

* Step 3: A form names **Update Organization** will pop up on the screen. Click the tab **More Configurations**

* Step 4: On the left side of the form, choose **Loading Time**

* Step 5: If you have already enabled the configuration **Enable Loading time at Depot** in the Branch, you could see the section **Custom Loading Time at Depot** is now ready to be filled out. The section **Use Services Time at Branch**  and **Dynamic Loading Time** are all disabled to fully use the **Custom Loading Time at Depot**.

* The sections of **Loading Min Time** and **Loading Max Time** are still kept the same as in the Branch. These sections are used as a standard benchmark to determine Loading Time at Depot.

* You could establish the loading time for a specific depot by adjusting the **Processing Time** and **Loading Time of Vehicles**

* You could change the Processing Time by entering the field **Processing Time** the number of minutes it takes to process at Depot. The legit number of minutes must be more than 0 and can be decimal if the time it takes is measured in seconds.

<Image title="Loading Time.png" alt={934} border={true} src="https://files.readme.io/144ccce-Loading_Time.png">
  Illustration (English)
</Image>

<Image title="Soanj hang.png" alt={934} border={true} src="https://files.readme.io/1e87cfb-Soanj_hang.png">
  Illustration (Vietnamese)
</Image>

* You could change the Loading Time of Vehicles by entering the field **Loading Time of Vehicles** the number of minutes it takes to load goods at Depot. The legit number of minutes must be more than 0 and can be decimal if the time it takes is measured in seconds.

<Image title="weight (ENG).png" alt={933} border={true} src="https://files.readme.io/bf8bf4f-weight_ENG.png">
  Illustration (English)
</Image>

* When you enable the configuration **Loading Time** at Depot, you could establish whether the depot uses Volume or Weight to load goods. 
* If you want the depot to use the volume of goods to establish the time it takes to load goods, remember to tick the box Use Volume below. The unit will be automatically changed from "kg" to "m3."

<Image title="Volume.png" alt={930} border={true} src="https://files.readme.io/4bac592-Volume.png">
  Illustration (Vietnamese)
</Image>

* In case you want to use the weight of goods to establish the time it takes to load goods, please untick the box **Use Volume**. The unit that will be used is "kg"

<Image title="weight (VIE).png" alt={933} border={true} src="https://files.readme.io/9fcb136-weight_VIE.png">
  Illustration (English)
</Image>

After entering all information to establish the loading time, click **Save** for changes to take effect.

## Rules to Calculate Loading Time at Depot

* Loading Time at Depot is calculated as follows\
  Loading Time = Processing Time +  Loading Time per Product Unit (can be either per kg or per m3)
* If the Depot has established the Loading Min Time and Loading Max Time, these timeframes will be used as a standard benchmark to determine the loading time at a specific depot.

### Scenario 1. The calculated loading time at depot is lower than the Loading Min Time

* In this scenario, the Loading time at depot will be the Min time
* For example: 
* The calculated loading time at depot is ***10 minutes***
* The Min Loading Time and Max Loading Time are respectively ***15 minutes - 30 minutes***
* The Loading time at depot thus will be ***15 minutes***

### Scenario 2. The calculated loading time at depot is higher than the Loading Max Time

* In this scenario, the Loading time at depot will be the Max time
* The calculated loading time at depot is ***35 minutes***
* The Min Loading Time and Max Loading Time are respectively ***15 minutes - 30 minutes***
* The Loading time at depot thus will be ***30 minutes***

### Scenario 3. The calculated loading time at depot is within the Loading/Unloading time window

* In this scenario, the Loading time at depot will be the calculated one. 
* The calculated loading time at depot is ***20 minutes***
* The Min Loading Time and Max Loading Time are respectively ***15 minutes - 30 minutes***
* The Loading time at depot thus will be ***20 minutes***

## Unloading Time at Customer

* Purpose of this configuration: Unloading time at customers' places can vary, hence, making time window constraint sometimes inappropriate when it comes to unloading goods. Therefore, you may need to customize and add more information on the unloading time of some specific delivery stops.

* To enable this configuration, please follow these steps below

* Step 1: You have to enable the configuration **Enable Unloading time at Customer** in the Branch that the Customer being changed is subject to before moving on. To see how to enable this configuration at Branch, click here for more instruction. [Configuration Un(loading) Time](doc:configuration-unloading-time) 

* Step 2:  Navigate to tab **Partners**. In the list of Customers, choose a Customer for which you want to enable this configuration.

* Step 3: A form names **Update Customer** will pop up on the screen. Click the tab **Other Settings**

* Step 4: On the left side of the form, choose **Unloading Time**

<Image title="customer.png" alt={1192} border={true} src="https://files.readme.io/667091d-customer.png">
  Illustration (English)
</Image>

<Image title="khách.png" alt={1195} border={true} src="https://files.readme.io/c8672dd-khch.png">
  Illustration (Vietnamese)
</Image>

* Step 5: If you have already enabled the configuration **Enable Unloading time at Customer** in the Branch, you could see the section **Unloading Time Settings** is now ready to be filled out.

* You could establish the loading time for a specific depot by adjusting the **Processing Time** and **Unloading Time per CBM**

* You could change the Processing Time and the Unloading time by entering the fields **Processing Time**  and **Unloading Time per CBM** the number of minutes it takes to process and unload at customers' delivery stop. The legit number of minutes must be more than 0 and can be decimal if the time it takes is measured in seconds.

<Image title="dỡ hàng 2.png" alt={1194} border={true} src="https://files.readme.io/c945444-d_hng_2.png">
  Illustration (English)
</Image>

<Image title="dỡ hàng.png" alt={1195} border={true} src="https://files.readme.io/01e108c-d_hng.png">
  Illustration (Vietnamese)
</Image>

After entering all information, click **Save** for changes to take effect.

## Rules to Calculate Unloading Time at Customer

* Unloading Time at Customer is calculated as follows\
  Unloading Time at Customer = Processing Time +  (Unloading Time per CBM \* Quantity of CBM of total orders in a stop)

* For example:

* The Processing Time is 3 minutes

* The Unloading time per CBM is 1 minute

* The quantity of CBM of total orders in a stop is 30 m3\
  The Unloading time is 3 min + (1 min \* 30 m3) = 33 min

* If the delivery stop has no established Loading Min Time and Loading Max Time, the Unloading Time at Customer will be the result of the formula mentioned above

* If the delivery stop has established the Loading Min Time and Loading Max Time, these timeframes will be used as a standard benchmark to determine the unloading time at a specific stop.

### Scenario 1. The calculated unloading time at delivery stop is lower than the Loading Min Time

* In this scenario, the Loading time at delivery stop will be the Min time
* For example: 
* The calculated unloading time at delivery stop is ***10 minutes***
* The Min Loading Time and Max Loading Time are respectively ***15 minutes - 30 minutes***
* The Unloading time at delivery stop thus will be ***15 minutes***

### Scenario 2. The calculated unloading time at delivery stop is higher than the Loading Max Time

* In this scenario, the Loading time at delivery stop will be the Max time
* The calculated unloading time at delivery stop is ***35 minutes***
* The Min Loading Time and Max Loading Time are respectively ***15 minutes - 30 minutes***
* The Unloading time at delivery stop thus will be ***30 minutes***

### Scenario 3. The calculated unloading time at delivery stop is within the Loading/Unloading time window

* In this scenario, the Unloading time at delivery stop will be the calculated one. 
* The calculated unloading time at a delivery stop is ***20 minutes***
* The Min Loading Time and Max Loading Time are respectively ***15 minutes - 30 minutes***
* The Unloading time at delivery stop thus will be ***20 minutes***

## Adding Unloading Time at Customer by Excel Template

* When you create multiple customers by Excel Template, you will see two fields **Processing Time** and **Unloading Time per CBM** as below. 
* These two fields are optional. If you would like to add information about Unloading Time at Customer, you could fill in these two fields with input rules mentioned above, or else you could leave them blank.

<Image title="template.png" alt={1896} border={true} src="https://files.readme.io/214c55c-template.png">
  Illustration (English)
</Image>

<Image title="template 2.png" alt={1892} border={true} src="https://files.readme.io/26ea8fb-template_2.png">
  Illustration (Vietnamese)
</Image>

* Filling in those two fields does not mean that you could use Unloading Time at Customer if you have not enabled the configuration **Enable Unloading Time at Customer** in the Branch that the Customer is subjected to. To enable the configuration for Branch, click here [Configuration Un(loading) Time](doc:configuration-unloading-time)
