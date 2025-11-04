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
* This article will act as a handbook, listing all configurations that can be enabled to provide you with additional functions beside the default functions provided by this model

> 🚧 Except for the configurations mentioned below, other configurations are not meant for this model even if they can be enabled

## Process to enable/disable configurations

* Navigate to **Organizations > Organization List** tab
* Click on the icon **Edit** :fa-pencil: of the appropriate Organization
* The Web form **Edit Organization** will appear. Navigate to the tab **More Configuration** by clicking on its title
* The configurations are categorized by sections such as **Model; Systems** etc. Click on the section title to open that section

<Image title="orgmoreconfig.gif" alt={744} border={true} src="https://files.readme.io/1325fd4-orgmoreconfig.gif">
  Illustration GIF (English)
</Image>

<Image title="Update Org (VIE) 2.gif" alt={944} src="https://files.readme.io/05e25fe-Update_Org_VIE_2.gif">
  Illustration GIF (Vietnamese)
</Image>

* To enable a configuration, click on its respective checkbox :fa-square-o: or radio button :fa-circle-thin:, or inputting in its information fields. Then, click **Save** to save the changes
* **Note**: For the configuration to take effect (Especially configurations of the **Manufacturer** Organization type), you might have to log out of your account then log in again
* Below are the list of configurations used by each Organization type of this Model. Configurations not mentioned are used in other Models

## Configurations for Manufacturer

## Transportation

## Warehouse

* Section: **Model**
* For this model, always select the radio button ***Inhouse***. Do not select ***Outsourcing***
* Section: **Model**
* For this model, always select the radio button ***Inhouse***. Do not select ***Outsourcing***

## Services

* Section: **Model**
* This configuration is currently not used for this Model. It is used for VRP - Transporters to Create Routes and PDP - Manufacturers to Select Transporters Models

## Business

* Section: **Model**
* This configuration will determine the Organization Type which will directly manage the Product Categories and Product general information. There are two options

### 1PL

* Product Categories and Product general information will be directly managed solely by the **Manufacturer**

### 3PL

* Product Categories and Product general information will be directly managed by each Organization, instead of uniting at the Manufacturer
* Read more about this at the following article: [**Manage Product Categories**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-product-categories) and [**Manage Products**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-products)

## Integrated ERP

> 🚧
>
> This configuration is only required for certain user accounts, and is used in conjunction with the following configuration: [**Order Consolidation**](https://docs.abivin.com/docs/vrp-in-house-fleet-configurations-by-organization-type#section-order-consolidation)

* Section: **Systems**
* Enable the integration between Abivin vRoute with the external FTP server
* Read more about this configuration at the following article: [**FTP Server**](https://docs.abivin.com/docs/vrp-in-house-fleet-ftp-server)

## Flexible Vehicle Type

* Section: **Route**
* Enable the customers to accept more vehicle types, not only limited to the default vehicle types of this model (Truck; Semi-truck; Motorbike)
* Read more about this configuration at the following article: [**Site-Dependent Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-site-dependent-constraint)

## Allow Approve Order

* Section: **Systems**
* Enable the function to let the Dispatchers approve orders submitted from the Delivery Mobile app (By the Salesmen) and Consumer Mobile app (By the Consumers) on Web app
* Read more about this configuration at the following article: [**Salesmen & Consumers Orders Approval**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#section-salesmen-consumers-orders-approval)

## Allow Manual Split Order

* Section: **Systems**
* Enable the function to let the dispatchers manually split Sales Order
* Read more at the following article: [**Manage Sales Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#manually-split-orders)

## Show Route List View

* Section: **Route**
* Enable the Route Plan (List View) feature, besides the default Route Plan (Map View). The Route Plan will be presented in a list form. Read more about this configuration at the following article: [**Route Plan (List View)**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-list-view)

## Reports

* Section: **Algorithm**
* Enable the **Reports > Reports** and **Reports > Dashboard** tabs
* Read more about this configuration at the following articles: [**Reports**](https://docs.abivin.com/docs/vrp-in-house-fleet-reports) and [**Dashboards**](https://docs.abivin.com/docs/vrp-in-house-fleet-dashboard)

## API Key

* Section: **API Key**
* Generate API keys to enable the connection between Abivin vRoute with external systems

## Use FTP

* Section: **Systems**
* Enable the connection between Abivin vRoute database with the external FTP server
* Read more about this configuration at the following article: [**FTP Server**](https://docs.abivin.com/docs/vrp-in-house-fleet-ftp-server)

## Configurations for Distributor

## Consolidate Order

> 🚧
>
> This configuration is only required for certain user accounts, and is used in conjunction with [**Use FTP**](https://docs.abivin.com/docs/vrp-in-house-fleet-configurations-by-organization-type#section-use-ftp) configuration

* Section: **Systems**
* This configuration will consolidate orders from second-level Branches and pull to the first-level Distributor
* Read more about this configuration at the following article: [**FTP Server**](https://docs.abivin.com/docs/vrp-in-house-fleet-ftp-server)

## Configurations for Branch

## Allow Send Email

* Section: **Systems**
* Enable the function to send emails enclosed with Electornic Proof of Delivery (ePOD) to the customers
* Read more about this configuration at the following article: [**Electronic Proof of Delivery**](https://docs.abivin.com/docs/vrp-in-house-fleet-electronic-proof-of-delivery)

## Avoid Creating Driver Task

* Section: **Systems**
* Stop generating tasks on the Mobile app of the drivers after the Delivery Routes are locked

## Required Driver

* Section: **Systems**
* If enabled, during the Route Plan Optimization process, the system will inspect all vehicles which have been assigned Delivery Routes. If there exists vehicles which has not been assigned default drivers, the system will prevent you from locking the Delivery Routes
* The relationship between the configurations **Avoid Creating Driver Task** and **Required Driver** are 

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Configuration
      </th>

      <th>
        Scenario 1
      </th>

      <th>
        Scenario 2
      </th>

      <th>
        Scenario 3
      </th>

      <th>
        Scenario 4
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Required Driver
      </td>

      <td>
        Ticked
      </td>

      <td>
        Unticked
      </td>

      <td>
        Ticked
      </td>

      <td>
        Unticked
      </td>
    </tr>

    <tr>
      <td>
        Avoid Creating Driver Task
      </td>

      <td>
        Ticked
      </td>

      <td>
        Unticked
      </td>

      <td>
        Unticked
      </td>

      <td>
        Ticked
      </td>
    </tr>

    <tr>
      <td>
        Scenario Result
      </td>

      <td>
        Prevent locking Delivery Routes if there are vehicles which have not been assigned drivers\
        Stop generating tasks on the Mobile app of the drivers after the Delivery Routes are locked
      </td>

      <td>
        Allow locking Delivery Routes even if there are vehicles which have not been assigned drivers\
        Don't generate tasks on the Mobile app of all drivers after the Delivery Routes are locked
      </td>

      <td>
        Prevent locking Delivery Routes if there are vehicles which have not been assigned drivers\
        Don't generate tasks on the Mobile app of all drivers after the Delivery Routes are locked
      </td>

      <td>
        Allow locking Delivery Routes even if there are vehicles which have not been assigned drivers\
        Don't generate tasks on the Mobile app of all drivers after the Delivery Routes are locked
      </td>
    </tr>
  </tbody>
</Table>

## 3D Loading

> 🚧 This configuration is currently a subfeature of the configuration **Show Route List View**

* Section: **Systems**
* This configuration will generate a 3D projection of the products inside the delivery vehicle's storage space (container) during the Route Plan Optimization process
* Read more at the following article: [**3D Loading**](https://docs.abivin.com/docs/vrp-in-house-fleet-3d-loading)

## Integrated Telematics

> ❗️
>
> This configuration is only used for certain user accounts, and requires tokens in order to establish connections with the telematics devices

* Section: **Systems**
* Record information taken from the telematics devices equipped on the Delivery vehicles

<Image title="temp tele.png" alt={1917} className="border" border={true} src="https://files.readme.io/ec05d87-temp_tele.png" />

## Allow Re-delivery Order

* Section: **Systems**
* Enable the function to retrieve [**Missing orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-missing-orders) (Orders that could not be put into the optimal Delivery routes in their original Order dates) and [**Failed orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-failed-orders) (Orders that were successfully put into the optimal Delivery routes but were failed to be delivered to the customers) from selected past dates, then attemp to put them into the Route optimization process on selected future dates
* Read more about this configuration at the following article: [**Retrieve Missing Orders & Failed Orders from past dates**](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-sales-orders#section-retrieve-missing-orders-failed-orders-from-past-dates)

## Show Driver On Route

> 🚧 This configuration is only effective for certain user accounts

* Section: **Display**
* Display usernames of drivers (Instead of vehicle codes) on route map screen during the route optimization process

<Image title="ddriver route.png" alt={1916} className="border" border={true} src="https://files.readme.io/61ff20e-ddriver_route.png" />

## Show Driver On Vehicle Table

> 🚧 This configuration is only effective for certain user accounts

* Section: **Display**
* Display usernames of drivers on **Transportation > Vehicle List** tab

<Image title="ddriver.png" alt={1913} className="border" border={true} src="https://files.readme.io/83bc584-ddriver.png" />

## Show Customer on Order List

* Section: **Display**
* Display Customer Name & Customer Code on **Orders > Sales Orders** tab

<Image title="customer.png" alt={1904} className="border" border={true} src="https://files.readme.io/87e58d1-customer.png" />

## Dynamic Loading Time

> ❗️ At the moment, this configuration is only usable for certain user accounts\
> This configuration is used in conjunction with the following configurations:

* Section: **Algorithm**
* Enable a specific loading/unloading time calculation algorithm, instead of using the default loading/unloading time calculation algorithm
* Read more at the following article:

## Use Due Date For VRP

> ❗️ This configuration is only required for certain User accounts

* Section: **Route**
* When enabled, the system will force the vehicles to deliver Orders to the customers exactly on the Due Dates mentioned in the Orders

## Allow Driver Create Extra Task

* Section: **Mobile**
* Allow the Drivers (Deliverymen) to actively create extra tasks on the Delivery Mobile app

<Image title="extra task.png" alt={523} className="border" border={true} src="https://files.readme.io/aa5fd48-extra_task.png" />

## Shift Start Time

* Section: **Route** 

![774](https://files.readme.io/de3ae4f-image_7.png "image (7).png")

* Allow users to configure the Shift Start Time of Vehicles with the following options: 
* Default: The system will compare the Open time of the Depot and Working time of the Vehicle to suggest the Shift Start Time during the Route Optimization process.
* Manual: Before the Route Optimization process, a pop-up will appear for users to manually input the Shift Start Time.
* Auto: The system will suggest the Shift Start Time that minimizes the waiting time of Driver during the Route Optimization process. 

## Hide Number Collected

* Section: **Mobile**
* Hide the field to input the money amount collected from the customers on the Delivery Mobile app

<Image title="hide collect.png" alt={1034} className="border" border={true} src="https://files.readme.io/94d87c2-hide_collect.png" />

## Hide Partially Delivery

* Section: **Mobile**
* Hide the option ***Partly Delivered*** from the Delivery results on the Delivery Mobile app

<Image title="hide partly.png" alt={1032} className="border" border={true} src="https://files.readme.io/30e6cf3-hide_partly.png" />

## Prevent Re-Submit Task

* Section: **Mobile**
* Prevent the Drivers (Deliverymen) from resubmitting tasks that have already been submitted on the Delivery Mobile app

## Allow Submit Task Over Date

* Section: **Mobile**
* Allow the Drivers (Deliverymen) to submit overdue tasks (By date) on the Delivery Mobile app
* For example: A task is planned to be performed no later than ***10:00 on 10/04/2020***. With this configuration enabled, the Drivers (Deliverymen) will still be able to submit that task at a later time point than that time point

## Prevent submit task over

> 📘 This configuration will not be visible if the configuration **Allow Submit Task Over Date** is enabled

* Section: **Mobile**
* Prevent the Drivers (Deliverymen) from submitting overdue tasks on the Delivery Mobile app. There are two options:

### Date and time

* Tasks that are overdue by the planned time point will not be submittable
* For example: A task is planned to be performed no later than ***10:00 on 10/04/2020***. The Drivers (Deliverymen) will not be able to submit that task after ***10:00 on 10/04/2020***

### Date

* Tasks that are overdue by the planned date will not be submittable
* For example: A task is planned to be performed no later than ***10:00 on 10/04/2020***. The Drivers (Deliverymen) will still be able to submit that task as long as the current date is earlier or equals to ***10/04/2020***, but will not be able to submit if the current date is a later date (For example ***11/04/2020***)

## Enable Unlock And Remove Route

* Section: **Route**
* Enable the function to unlock all locked Delivery Shifts on the current Route Plan at once
* Read more about this configuration at the following article: [**Unlock most recently locked Delivery shifts of all vehicles**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-adjustment#unlock-most-recently-locked-delivery-shifts-of-all-vehicles)

## Allow Unlock One Route

* Section: **Route**
* Enable the function to unlock only some selected locked Delivery Shifts on the current Route Plan
* Read more about this configuration at the following article: [**Unlock locked Delivery routes of only selected vehicles**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-adjustment#section-unlock-locked-delivery-routes-of-only-selected-vehicles)

## Random Vehicle Seed

* Section: **Route**
* By default, during the Route optimization process, the system will select the vehicles from a static vehicle list. Over time, this will lead to the situation in which certain vehicles will likely get selected more than other vehicles
* When enabled, this configuration will generate a random vehicle list for each Route optimization attempt, which will prevent the above phenomenon from happening

## Services Time

* Section: **Algorithm**
* Specify the Base Service time of the Branch, in order to automatically calculate the Service time (Loading and Unloading time) of all Depots and Customers under that Branch
* Read more about this configuration at the following article: [**Planned Service Time Calculation**](https://docs.abivin.com/docs/vrp-in-house-fleet-planned-service-time-calculation)

## Use Familiarity

* Section: **Algorithm**
* Enable the Familiarity Constraint
* Read more about this configuration at the following article: [**Familiarity Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-familiarity-constraint)

## Use Clustering

* Section: **Algorithm**
* Enable the Geographic Clustering routing algorithm
* Read more about this configuration at the following article: [**Geographic Clustering**](https://docs.abivin.com/docs/vrp-in-house-fleet-geographic-clustering)

## Clustering By District

* Enable the Geographic Clustering (By District) routing algorithm
* Read more about this configuration at the following article: 

## Lunch Time

* Enable the delivery vehicle to have lunch break time
* Read more about this configuration at the following article: [**Vehicle Lunch Break**](https://docs.abivin.com/docs/vrp-in-house-fleet-vehicle-lunch-break)

## Odd Even Policy

* Enable traffic policy by odd and even vehicle license plate numbers
* Read more about this configuration at the following article: [**Road constraint based on Vehicle license plate number**](https://docs.abivin.com/docs/vrp-in-house-fleet-road-constraints#section-road-constraint-based-on-vehicle-license-plate-number)

## Time Balancing

* Make the working time of the delivery vehicles to be as balanced as possible
* Read more about this configuration at the following article:

## Use Cold Chain

* Enable temperature-controlled supply chain feature
* Read more about this configuration at the following article: [**Cold Chain**](https://docs.abivin.com/docs/vrp-in-house-fleet-cold-chain)

## Split Delivery

* Enable the function to automatically assign multiple Sales Orders that are placed by the same customer to multiple vehicles, without having to enable the configuration **Separate Vehicle** for each of those Orders during the Order creation process
* Read more about this configuration at the following article:

## Use Service Time

* Use the service time of the orders  (Unloading time at the customers' warehouses/stores) that have been manually input in the Order Excel template instead of the automatically calculated service time during the route optimization process
* Read more about this configuration at the following article: [**Manual Customer Service time**](https://docs.abivin.com/docs/vrp-in-house-fleet-planned-service-time-calculation#section-manual-customer-service-time)

## Use WMS

> 🚧
>
> This configuration is only used for some user accounts

* Enable the integration between Abivin vRoute with the external Warehouse management system, in order to pull data (Orders, Customers etc.) to Abivin vRoute
* Read more about this configuration at the following article:

## Hard Time Windows

* Enable the Hard time windows constraint
* Read more about this configuration at the following article: [**Hard Time Window Constraint**](https://docs.abivin.com/docs/vrp-in-house-fleet-hard-time-window-constraint)

## Open Route

* Allow the delivery vehicles to not travel back to the manufacturing warehouses after completing all assigned delivery tasks
* Read more about this configuration at the following article: [**Open Route**](https://docs.abivin.com/docs/vrp-in-house-fleet-open-route)

<Image title="ba open route.png" alt={1488} className="border" border={true} src="https://files.readme.io/959fe57-ba_open_route.png" />

## Reason settings

* Specify the reasons for Failed orders, so that the Drivers (Deliverymen) can select on the Delivery Mobile app
* Read more about this configuration at the following article: [**Failed Orders**](https://docs.abivin.com/docs/vrp-in-house-fleet-failed-orders)

## Un(loading) Time

* When you enable this configuration, you could use these two configurations: Loading Time at Depot and Customer Unloading Time. The only organization type that could enable this configuration is Branch.

## Configurations for Depot

> 📘 The configurations for Depot will also apply to Sun & Crossdock if mentioned

## Loading Min Time & Loading Max Time

> 📘
>
> On Excel template, these fields are called Min Time and Max Time\
> Also applies to Sun & Crossdock

* The minimum and maximum loading time period (In minutes) that the Depot/Sun/Crossdock being created imposes on every vehicle when loading products
* Read more about this configuration at the following article: [**Planned Service Time Calculation**](https://docs.abivin.com/docs/vrp-in-house-fleet-planned-service-time-calculation)

## Global Customer

* Section: **Systems**

* This configuration allows the user to create a global customer. A global customer is a customer that can be used in any branch and depot in the organization.

* When enabling this configuration:

* Customer's organization must be Manufacture when creating customer (by manual or import files)

* Old customer maybe update or not

* When disabling this configuration:

* User checks if there is any customer that its organization is Manufacture. Then, the user must update the organization of those customers as Depot

* When the user disables this configuration, the system will warn and list all the customers that have not updated yet

* Steps to use this configuration:

* **Step 1**: Enable the configuration: The user edits the Manufacture org and then selects **MORE CONFIGURATIONS** tab, in the **System** section

<Image title="Screenshot from 2023-03-01 09-34-53.png" alt={1249} src="https://files.readme.io/5feba62-Screenshot_from_2023-03-01_09-34-53.png">
  Global customer config
</Image>

* **Step 2**: In the **Organizations > User Groups** tab, create new User Group.
* New User Group must have *View All* permission for **Organizations** resource, and *All* permission for **Customer** resource. The group should contain permissions as below:

<Image title="Screenshot from 2023-03-01 09-44-37.png" alt={849} src="https://files.readme.io/46a47a2-Screenshot_from_2023-03-01_09-44-37.png">
  New User Group
</Image>

* **Step 3**: Assign a new User Group to a specific User
* In the **Organizations > User** tab, edit the User you want to have permission to manage Global Customer
* Add the Manufacture to the user's *Organization*
* Add a new User Group to user's *Groups*

<Image title="Screenshot from 2023-03-01 10-28-06.png" alt={947} src="https://files.readme.io/a3c832a-Screenshot_from_2023-03-01_10-28-06.png">
  User's fields need to update
</Image>

* **Step 4**: Create Orders: The user can select Global Customer when creating Order
* *Note*: In each route plan, all orders delivered to the same customer should be created from the same depot

<Image title="Screenshot from 2023-03-01 10-33-17.png" alt={314} src="https://files.readme.io/6b2879b-Screenshot_from_2023-03-01_10-33-17.png">
  Global Customer will be listed
</Image>
