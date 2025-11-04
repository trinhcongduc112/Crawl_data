---
title: Salesmen
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: basic
      slug: mobile-interaction-with-orders
      title: Salesmen interaction with Orders
---
* In many companies, there exists a group consists of employees who are sales people (Salesmen). These sales people will explore new markets, find and build rapport with new customers. When the business relationships with the customers have been established, the sales people might be required to track the status of orders delivered to their associated customers, or even deliberately create orders for their customers
* In this article we will find out how to:
* Create Salesmen User group
* Allocate Users into Salesmen User group
* Associate Customers and Salesmen

## Create Salesmen User group

* Navigate to **Organizations > Group List** tab
* Please refer to the [**CRUD functions article**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) to know the general steps about creating single object using web form

## Salesmen User group information field

* Below is the list of all information fields of a Salesmen User group 

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
        Organization
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Depot or Sun which manages the Salesmen  User group being created\
        **2. Input rules:**\
        Click on this field. Type the Organization Name or Organization Code of the Depot/Sun into the search bar, then select from the drop down menu
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Group Code\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The management code assigned to the Salesmen User group being created\
        **2. Input rules:**\
        Always input this value: **SALESMAN**
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Group Name\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The name assigned to the Salesmen User group being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Description\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        A short description of the Salesmen User group being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

## Assign CRUD rights

* Depending on your business model, you could allow the Salesmen Users to only be able to view orders, or also create orders:

### Allow salesmen to view orders only

* With this configuration, the salesmen users can only view the status of his customer's orders on Mobile app

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Module
      </th>

      <th>
        Rights assigned
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organizations
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Customers
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Products
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Orders
      </td>

      <td>
        Read
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2019-10-01 21_10_14-Window.png" alt={821} className="border" border={true} src="https://files.readme.io/e17a9f4-2019-10-01_21_10_14-Window.png" />

### Allow salesmen to view and create orders

* With this configuration, the salesmen users can also create orders to their customers on Mobile app

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Module
      </th>

      <th>
        Rights assigned
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organizations
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Customers
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Products
      </td>

      <td>
        Read
      </td>
    </tr>

    <tr>
      <td>
        Orders
      </td>

      <td>
        Create; Read
      </td>
    </tr>
  </tbody>
</Table>

<Image title="2019-10-01 22_25_08-Window.png" alt={816} className="border" border={true} src="https://files.readme.io/6fe4067-2019-10-01_22_25_08-Window.png" />

## Allocate Users into Salesmen User group

## Allocate existing users

* You could allocate existing users of a ***Depot*** or ***Sun*** into the Salesmen User group recently created by doing the following steps:
* Navigate to **Organizations > User List** tab
* Filter out the users of the Depot or Sun which you want to allocate, then click on **Edit** :fa-pencil: icon of those users
* On the **User Information** screen, click on the **Groups** field. Type the text ***Sales*** in the search bar to filter the Salesmen User group, then select that group from the drop down menu
* Next, on the **Sales Code** field, input the a code assigned to the salesman being created. This code will help the system map the Salesman with his associated Customers
* There are some criteria for the Sales code:
* All letters must be uppercase and must not contain spaces. For example: ***salescode001*** or ***SALES CODE 001*** is not acceptable; ***SALES\_CODE\_001*** is acceptable
* A salesman can have multiple sales codes. Two adjacent sales codes are separated by a comma. For example: ***SALES\_CODE\_01,SALES\_CODE\_02***
* Click **Save** to confirm the change

<Image title="2019-10-02 09_16_19-Window.png" alt={1676} className="border" border={true} src="https://files.readme.io/ae18ac6-2019-10-02_09_16_19-Window.png" />

## Allocate new users

* If you create new salesmen users using Web form, follow the steps described above
* If you create new salesmen users using Excel template, you need to pay attention to the following things:
* Make sure the value in the **Organization Code** cell is the Organization Code of the ***Depot*** or ***Sun*** in which the salesmen being created belong
* Input the text ***SALESMAN*** into the **User Group Code** cell
* Input the Sales Code of the salesman being created into the **Sales Code** cell. The criteria described above also applies here
* Repeat these steps for other salesmen users

<Image title="2019-10-01 23_27_33-Window.png" alt={1808} className="border" border={true} src="https://files.readme.io/4f42afa-2019-10-01_23_27_33-Window.png" />

## Associate Salesmen and Customers

## Associate existing customers

* Navigate to **Partners > Customer List** tab
* Click on **Edit** :fa-pencil: icon of the customers which you want to associate with Salesmen
* On the **Edit Customer** screen, scroll down and click on **More Configurations**
* Type the Sales Code of the salesman associated with this customer in the **Sales Code** field
* Click **Save** to confirm the change

<Image title="2019-10-01 22_38_34-Window.png" alt={1900} className="border" border={true} src="https://files.readme.io/aefbfce-2019-10-01_22_38_34-Window.png" />

## Associate new customers

* If you create new customers using Web form, follow the steps described above
* If you create new customers using Excel template, input the sales code of the Salesman you want to associate with the customer being created in the **Sales Code** cell. The criteria of the code described above also applies when using this method
* **Note:** Multiple customers can have the same sales code, which means they are associated with the same salesman

<Image title="2019-10-01 22_41_07-Window.png" alt={1631} className="border" border={true} src="https://files.readme.io/0e1ed4b-2019-10-01_22_41_07-Window.png" />
