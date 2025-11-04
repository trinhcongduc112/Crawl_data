---
title: Organizations
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
## Definition

* <Glossary>Organization</Glossary> is an important concept in Abivin vRoute. Throughout the history of human civilizations, businesses and government departments have been arranged into organizations to concentrate common resources and manage shared-goal people.
* In Abivin vRoute, an Organization can be a business, a government ministry, a region or a warehouse branch. Each organization, except the top organization, will have a single superior organization. This makes the relationship a tree-like structure. 

## Level of visibility rights

* Each level of this structure will have different level of visibility rights. 
* To be specific, a parent organization can view the union of all resources in its subordinate organizations. A subordinate organization cannot view any resources from its superior organization.
* Resources in a organization include its **Users, Partners, Products, Orders, Vehicles** and **Tasks**. 

<Image title="Luồng vApp - Organization structure.png" alt={1725} width="100%" src="https://files.readme.io/7edfa53-Luong_vApp_-_Organization_structure.png">
  A diagram illustrates the tree relationship of organizations. Each organization has its own resources of Users, Partners, Products, Orders, Vehicles and Tasks. A parent organization may have the visibility on the resources of their children organizations but not vice versa.
</Image>

## Organization structure in Abivin vRoute

* In Abivin vRoute, we have defined some common organizations and basic organization structures in order to manage the database logically. Please note that we can customize to support your existing organization structure.

## In-In Model

* In this model, the vehicle fleet is managed in-house.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Level of Organization
      </th>

      <th>
        Name of Organization
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        First level
      </td>

      <td>
        Manufacturer
      </td>

      <td>
        Manufacturer of the products. This is the top organization
      </td>
    </tr>

    <tr>
      <td>
        Second level
      </td>

      <td>
        Distributor
      </td>

      <td>
        Distribution channels of the manufacturer
      </td>
    </tr>

    <tr>
      <td>
        Third level
      </td>

      <td>
        Branch
      </td>

      <td>
        The agents selling the products
      </td>
    </tr>

    <tr>
      <td>
        Fourth level
      </td>

      <td>
        Depot
      </td>

      <td>
        The first level warehouse, where products are stored before being distributed to agents and retail stores for sales
      </td>
    </tr>

    <tr>
      <td>
        Fifth level\
        (Optional)
      </td>

      <td>
        Sun; Crossdock
      </td>

      <td>
        The second level warehouse
      </td>
    </tr>
  </tbody>
</Table>

## Out-Out Model

* In this model, the vehicle fleet is out-sourced to third party transporter organizations. 

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Level of Organization
      </th>

      <th>
        Name of Organization
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        First level
      </td>

      <td>
        Manufacturer
      </td>

      <td>
        Manufacturer of the products. This is the top organization
      </td>
    </tr>

    <tr>
      <td>
        Second level
      </td>

      <td>
        Distributor
      </td>

      <td>
        Distribution channels of the manufacturer
      </td>
    </tr>

    <tr>
      <td>
        Third level
      </td>

      <td>
        Branch
      </td>

      <td>
        The agents selling the products
      </td>
    </tr>

    <tr>
      <td>
        Fourth level
      </td>

      <td>
        Transporter
      </td>

      <td>
        Third party transporter organizations that the manufacturer hires to deliver products to customers
      </td>
    </tr>
  </tbody>
</Table>

## User group

* Each organization is structured differently. They may be a group by function: Group of decision makers, Group of marketing, sales, engineering or accounting. They may also be grouped into project teams: Project Manager, Product Owner, Designer, Software Engineer, Software Tester. Therefore, the purpose of User groups is to categorize a group of Users who share the same characteristics. A User group will have the same permission to access data in the system.
* Within each organization, there are 2 types of User groups: Administrator user group and Normal user group. These User groups have different level of rights:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Type of User Group
      </th>

      <th>
        Rights of user
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Administrator group**
      </td>

      <td>
        When originally created, users of these groups are allowed to perform [**CRUD**](https://docs.abivin.com/docs/crud) operations to the organizations they manage

        The Administrator user of the upper organization can edit rights assigned to the Administrator groups of the lower organizations
      </td>
    </tr>

    <tr>
      <td>
        **Normal group**
      </td>

      <td>
        Only allowed to perform certain [**CRUD**](https://docs.abivin.com/docs/crud) operations as granted by the Administrators user of the organizations they belong in
      </td>
    </tr>
  </tbody>
</Table>
