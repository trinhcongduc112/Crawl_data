---
title: Split Delivery (Automatic)
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
## Over-capacity Scenarios

* During the Route Plan Optimization Process, there are two scenarios which will lead to ***Over-capacity*** - The situation in which the weight and/or volume of the Orders that the system is trying to assign to a vehicle exceed that vehicle's weight and/or volume capacity
* Scenario 1. A Customer places multiple Orders. Each Order's weight and volume doesn't exceed the weight/volume capacity of the vehicles but the total weight/volume of the Orders exceeds the weight/volume capacity of the active vehicles
* Scenario 2. A Customer places only one Order. The Order's weight/volume exceeds the weight/volume capacity of the active vehicles 
* In both scenarios, by default, that Customer's Order(s) can not be assigned to a single vehicle, the system will therefore treat that Customer's Order(s) as Unplanned (Missing) Orders
* This article will present a solution that can help you automatically split the over-capacity Order(s) of a Customer into smaller Orders to fit the capacity of the vehicles

## Compulsory Configurations

### Enable Split Delivery Configuration

* Navigate to **Organizations > Organizations** tab
* Click **Edit** :fa-pencil: of the **Branch**
* On the **Update Organization** form, navigate to **More Configurations > Algorithm** sub-tab
* Tick the **Split Delivery** checkbox
* The Split Delivery Configuration has been enabled. From now on, on each Route Plan Optimization attempt, the system will compare the total Weight/Volume of all Orders placed by a Customer against the weight/volume capacity of all ***active vehicles*** from the same Depot that directly manages that Customer, regardless of whether those active vehicles have been assigned Delivery Routes or not

<Image title="vAbn4GtfH1.png" alt={742} className="border" border={true} src="https://files.readme.io/1aa9727-vAbn4GtfH1.png" />

* In addition to that, upon checking the Split Delivery checkbox, several sub-configurations will appear below:

#### Use Inactive vehicles for comparison

* If you enable this sub-configuration, then asides the active vehicles, the system will also take the ***inactive vehicles*** of the managing Depot into comparison

<Image title="vAbn4GtfH1.png" alt={742} className="border" border={true} src="https://files.readme.io/e724ce5-vAbn4GtfH1.png" />

## How Does This Configuration Work?

## With "Use Inactive vehicles for comparison" sub-configuration disabled

* During the Route Plan Optimization process, the system will compare the weight and volume of the Orders against the weight and volume capacity of the active vehicles. Two splitting mechanisms will be utilized depending on which over-capacity scenario happens:

### Order-level Order Splitting

* This splitting mechanism will be utilized if Scenario 1 happens. The system will assign the Customer's Orders to several vehicles instead of a single vehicle, starting from the vehicle with the highest volume capacity

### Product-level Order Splitting

* This splitting mechanism will be utilized if Scenario 2 happens. The system will split the Customer's single Order into several smaller Orders then assign those smaller Orders to several vehicles instead of a single vehicle, starting from the vehicle with the highest volume capacity
* If one Order of a Customer is over-capacity compare to both active vehicles and inactive vehicles, then the system will split that Order into some smaller Orders that fit the capacity of the active vehicles and will treat the rest of the original Order as an Unplanned (Missing) Order
* **Note**: The system will only utilize this splitting mechanism for the furthest Stop on a Delivery Route

## With "Use Inactive vehicles for comparison" sub-configuration enabled

* During the Route Plan Optimization process, the system will compare the weight and volume of the Orders against the weight and volume capacity of both the active and inactive vehicles
* If one Order of a Customer is over-capacity compare to all active vehicles, but is still within the capacity of some of the inactive vehicles, then even if the system can still split that Order into smaller Orders to fit the capacity of the active vehicles, the system will simply treat that Order as an Unplanned (Missing) Order. Here you can simply switch the inactive vehicle(s) which have enough capacity into the active state and perform the Route Plan Optimization process again
* Below is the reason the system will give out when this scenario happens

<Image title="j6Jy41Y0gk.png" alt={371} className="border" border={true} src="https://files.readme.io/17e831d-j6Jy41Y0gk.png" />

* If one Order of a Customer is over-capacity compare to both active vehicles and inactive vehicles, then the system will split that Order into some smaller Orders that fit the capacity of the active vehicles and will treat the rest of the original Order as an Unplanned (Missing) Order
