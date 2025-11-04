---
title: Abivin vRoute System Resources
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
This article will introduce and explain the functions of the main objects in Abivin vrRoute.

## Organizations

Organization is an important concept in Abivin vRoute. Throughout the history of human civilizations, businesses and government departments have been arranged into organizations to concentrate common resources and manage shared-goal people.

In Abivin vRoute, an Organization can be a business, a government ministry, a region or a warehouse. Each organization, except the top organization, will have a direct upper organization. This makes the relationship between organizations a tree-like structure.

Each level of this structure will have different level of visibility rights. To be specific, an upper organization can view the resources of all its lower organizations. A lower organization cannot view any resource of its upper level organizations.

Below is a diagram to illustrate the tree-like structure of organizations in Abivin vRoute.

![1169](https://files.readme.io/da87503-Orgs_resources.png "Orgs resources.png")

## Users & User Groups

In every organization, its personnel will be grouped into separate departments. Each department is specialized in different function, such as: accounting, marketing, planning and so on. Generally each department will have its own managers and regular employees.

Similarly, vRoute organization will have its own **Users**. In the User base of an organization, individual users who share the same characteristics (Permissions; rights; duties etc.) can be put into functional **User Groups** such as Administrator User group; Driver User group; Salesmen User group and so on. A *User* can belong to more than one *User Group*.

To restrict the rights and functions of each *User Group*, we implement the *CRUDLIE* permission concept.

## Partners

Parners are entities with which your own organization has some forms of business relationships. There are two types of Partners:

* **Customers** - Individuals or organizations who have interest of the products your organization is providing
* **Suppliers** - Who you buy materials from

## Products & Product Categories

Products are the result of the manufacturing process that your organization offer for sale to your customers, or. If there are many related products, they can be grouped into particular **Product Categories**

## Orders

Orders are the requests to supply products from the organization that produces those products, to the organization who has demand for those products

If the products are to be sold by your organization to your customers, then the request is defined as a **Sales Order**

On the other hand, If the products are to be sold by your suppliers to your organization, then the request is defined as a **Purchase Order**

## Vehicles

After the customers place orders to your organization, the products can not travel to the customer locations by themselves, obviously. They have to be moved by some kinds of delivery **Vehicles**.

A fleet of delivery can be comprised of various **Vehicle Types**, such as: Motorbike, Light duty truck; Heavy duty truck; Trailer truck; Barges.

If the delivery fleet is under the sole management of your organization, then it is referred to as **In-house delivery fleet**. On the other hand, if your organization have the delivery tasks fulfilled by third party logistic service providers (3PL), then the delivery fleet is called **Outsourcing delivery fleet**

## Tasks & Actions

We are big fans of SMART goals (Specific, Measurable, Assignable, Realistic, Time Based). Without a specific description of the duties, a person will not know what he needs to do. Even if he knows what to do, he still needs to be aware of the measurements based on which his work will be evaluated.

Therefore, we want to implement the SMART goals into Abivin vRoute's **Task** system. A Task is the central core of vRoute system. The requirements for a Task to exist are the objects we have defined above: Organization, User; Customer; Product; Order; and Vehicle. To be specific, we require:

* A **User** has to complete a series of **Tasks** in order to finish an **Order**
* Each **Task** can be broken down into sub activities, called **Actions**
