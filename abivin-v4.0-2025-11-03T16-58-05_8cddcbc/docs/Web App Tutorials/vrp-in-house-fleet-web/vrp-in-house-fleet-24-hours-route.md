---
title: Optimize Longer Than 24 Hours Routes
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
* The VRP model is mostly optimized for routes that require less than 24 hours (One working day) to complete
* You could, however, workaround to optimize routes that might require more than 24 hours to complete, by:
* Changing the **Close time** of the customers who will receive these orders
* Changing the **Stop time** of the vehicles which will deliver these orders

## Configure the customer

* Navigate to **Partners > Customer List** tab
* Click on **Edit** :fa-pencil: icon of the customers you want to configure
* On the **Edit customer** screen, scroll down and click on **More configurations** :fa-caret-down:
* In the **Close time** field, input a value larger than the sum of: 1. The time period usually taken for the vehicles to deliver products from the Depot to the customer warehouse and 2. The value of the **Open time** field of this customer
* For example: Customer A opens at ***08:00*** everyday. Orders to the customer A usually take around ***72*** hours to complete, starting from the Depot. Therefore, you should type a value greater than ***80:00*** into the **Close time** field of this customer
* Click **Save** to confirm the change

<Image title="Screenshot_1.png" alt={1834} className="border" border={true} src="https://files.readme.io/c9b225f-Screenshot_1.png" />

## Configure the vehicle

* Navigate to **Transportation > Vehicle List** tab
* Filter the Depot that will deliver to the customer configured above
* Click on **Edit** :fa-pencil: icon of the vehicles which you want to configure
* On the **Update Vehicle** form, input into the **Stop time** field a value larger than the sum of: 1. The time period these vehicles usually take to deliver from the Depot to the customer warehouse, and 2. The value of the **Start time** field
* For example: A vehicle usually starts at ***08:00*** everyday. Orders to the customer A usually takes around ***72*** hours for this vehicle to complete, starting from the Depot. Therefore, you should input a value greater than ***80:00*** into the **Stop time** field of this vehicle
* Click **Update** to confirm the change

<Image title="Screenshot_2.png" alt={1905} className="border" border={true} src="https://files.readme.io/7ef1e14-Screenshot_2.png" />

## Perform route optimization

* Now you can proceed to perform route optimization for these orders normally
* On the Timeline panel, the optimized routes for these orders will span across a time period of more than 24 hours

<Image title="24h opti.gif" alt={1672} className="border" border={true} src="https://files.readme.io/f36d7db-24h_opti.gif" />
