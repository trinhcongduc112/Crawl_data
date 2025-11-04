---
title: Big Orders
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
## Definition of Big order

* If your customers has a constant demand for some particular products, you can plan the delivery schedule for your customer in advance by using **Big orders**

## Big order fulfillment process

* First, the Corporation Administrator will gather customer demand and create Big orders accordingly
* After the Big orders have been created, they will be forwarded to the account of the Order Inspector. The Big orders need to be inspected and approved by the Order Inspector
* When the Order Inspector has approved the Big orders, the Big orders will be forwarded to the Transporter Administrator. The Transporter Administrator will deliberately decide how to split the Big orders into smaller Sales orders and assigns the split Sales order to the available delivery fleet

## Create Big Orders

* You are the Corporation Administrator. You can create a Big order by following the steps below
* Navigate to **Orders > Big Orders** tab
* Hover your mouse over the icon :fa-plus-circle:, then click on the icon **Create Big Order** :fa-pencil:

<Image title="Image 3.png" alt={1912} className="border" border={true} src="https://files.readme.io/dbe1cf6-Image_3.png" />

* The screen **Create Big Order** will show up. Here you will need to input the information of the Big order

<Image title="Image 10.png" alt={1913} className="border" border={true} src="https://files.readme.io/443b3e7-Image_10.png" />

## Big order information fields

* Below are the information fields of a Big order

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
        Order Code
      </td>

      <td>
        **1. Description:**\
        The management code of the big order being created\
        **2. Input rules:**\
        [Click on this link](https://docs.abivin.com/docs/vrp-outsourcing-fleet-big-orders#section-1-order-code)
      </td>
    </tr>

    <tr>
      <td>
        Filter by Start-End Date
      </td>

      <td>
        **1. Description:**\
        The date range during which the big order can be split into smaller Sales orders  and performed\
        **2. Input rules:**\
        [Click on this link](https://docs.abivin.com/docs/vrp-outsourcing-fleet-big-orders#section-2-filter-by-start-end-date)
      </td>
    </tr>

    <tr>
      <td>
        Type Way
      </td>

      <td>
        **1. Description:**\
        The order type of the order being created\
        **2. Input rules:**\
        [Click on this link](https://docs.abivin.com/docs/vrp-outsourcing-fleet-big-orders#section-3-type-way)
      </td>
    </tr>

    <tr>
      <td>
        Customer Code
      </td>

      <td>
        **1. Description:**\
        The customer who places the big order being created\
        **2. Input rules:**\
        [Click on this link](https://docs.abivin.com/docs/vrp-outsourcing-fleet-big-orders#section-4-customer-code)
      </td>
    </tr>

    <tr>
      <td>
        Warehouse Code
      </td>

      <td>
        **1. Description:**\
        The Depot from where the products will be loaded\
        **2. Input rules:**\
        [Click on this link](https://docs.abivin.com/docs/vrp-outsourcing-fleet-big-orders#section-5-warehouse-code)
      </td>
    </tr>

    <tr>
      <td>
        Product
      </td>

      <td>
        **1. Description:**\
        The products to be loaded in the order being created\
        **2. Input rules:**\
        [Click on this link](https://docs.abivin.com/docs/vrp-outsourcing-fleet-big-orders#section-6-product)
      </td>
    </tr>

    <tr>
      <td>
        Transporter Code
      </td>

      <td>
        **1. Description:**\
        The Transporter who will perform the big order being created\
        **2. Input rules:**\
        [Click on this link](https://docs.abivin.com/docs/vrp-outsourcing-fleet-big-orders#section-7-transporter-code)
      </td>
    </tr>
  </tbody>
</Table>

## Information fields input rules

### 1. Order Code

* The Order Code is automatically created in the following format: ***BO-yymmdd-xxxx***, in which ***BO*** stands for ***Big Order***; ***yy*** is the last two digits of the current year; ***mm*** is the current month; **dd** is the current date; ***xxxx*** is the numerical order of the attempt you click on the icon **Create Big Order** :fa-pencil: on the current day
* For example: ***BO-200217-0002*** means that you have clicked on the the icon **Create Big Order** :fa-pencil: the second time. The current date is ***February 17th 2020***
* You can also change the order code to a different one

<Image title="Image 11.png" alt={206} className="border" border={true} src="https://files.readme.io/7c43c01-Image_11.png" />

### 2. Filter by Start - End date

* Click on this field. Select the appropriate date range from the drop down calendars

<Image title="Image 12.png" alt={674} className="border" border={true} src="https://files.readme.io/be79346-Image_12.png" />

### 3. Type Way

* Always click on the following radio box: **First Way**

<Image title="Image 13.png" alt={240} className="border" border={true} src="https://files.readme.io/fe1635e-Image_13.png" />

### 4. Customer Code

* Click on this field. Input the ***Customer Name/Customer Code*** of the appropriate customer into the search bar. The system will filter out the wanted customer on the drop down menu. Click on that customer to select it

### 5. Warehouse Code

* Click on this field. Input the ***Organization Name/Organization Code*** of the appropriate Depot into the search bar. The system will filter out the wanted Depot on the drop down menu. Click on that Depot to select it

### 6. Product

#### 6.1. Select product

* Click on this field, input the ***Product Name/Product Code*** of the appropriate product into the search bar. Select that product from the drop down menu, then click on the **Add** button to add that product into the order
* You can add multiple products to the order by repeating these steps

<Image title="Image 14.png" alt={1721} className="border" border={true} src="https://files.readme.io/f40c256-Image_14.png" />

#### 6.2. Specify quantity of product cases/single items

* Next, you have to input the quantity of cases and/or single items of the products into two fields **Number Of Cases** and **Number Of Items**

<Image title="Image 15.png" alt={1720} className="border" border={true} src="https://files.readme.io/140eafa-Image_15.png" />

* **Note:** If there is zero single item of a specific product in the order being created, you must input the value ***0*** into the field **Number Of Items**. Similarly, If there is zero case of a specific product in the order being created, you must input the value ***0*** into the field **Number Of Cases**
* If you accidentally added the wrong product, click on the **Remove** icon :fa-remove: of that product to remove it from the order

<Image title="Selection_009.png" alt={1718} className="border" border={true} src="https://files.readme.io/c2361a8-Selection_009.png" />

### 7. Transporter Code

* The appropriate Transporter will be automatically selected if that Transporter has transport services between the selected Customer and the selected Depot

## Inspect and Approve Big Order

* You are the Order Inspector. After the Corporation Administrator has created Big orders, you will have to inspect then approve those orders
* Login to your account
* Navigate to **Orders > Big Orders** tab
* You can click on the icon **Edit** :fa-pencil: to view more information of the order
* To approve a Big order, click on the double check mark icon :fa-check: of that order

<Image title="Image 5.png" alt={1915} className="border" border={true} src="https://files.readme.io/123d723-Image_5.png" />

* You can also approve multiple Big orders at once by clicking on the corresponding check box icon :fa-square-o: of each order. When that icon turns to :fa-check-square-o:, that means the orders have been selected. Now click on the button **Approve** on the top toolbar to approve those orders

<Image title="Image 6.png" alt={1913} className="border" border={true} src="https://files.readme.io/e39d651-Image_6.png" />

* After you have approved a Big order, that order will be forwarded to the account of the Transporter Administrator

## Perform Big order

* You are the Transporter Administrator. After the Order Inspector has approved a Big order, you will receive that Big order in your account
* You will need to split that Big order into smaller Sales orders, assign the split Sales order to the vehicles based on the actual availability of your delivery fleet, then perform route optimization for those orders

## Split Big order into smaller Sales order

* To split a Big order, follow the steps below
* Navigate to **Orders > Big Orders** tab
* Click on the icon :fa-plus-circle: of the Big order you want to split

<Image title="Image 7.png" alt={1912} className="border" border={true} src="https://files.readme.io/8da6ffd-Image_7.png" />

* The form **Split Big Order** will appear. Here you will split the Big order into smaller split Sales orders
* Click on the field **Order Date**. On the drop down calendar, select the date on which you want to perform the split Sales order being created

<Image title="Image 9.png" alt={992} className="border" border={true} src="https://files.readme.io/f09d76e-Image_9.png" />

* Then, on two fields **Cases Splitted** and **Items Splitted**, input the quantity of product cases/single items you want to be loaded in the split Sales order being created

<Image title="Image 9.png" alt={992} className="border" border={true} src="https://files.readme.io/81ff8d0-Image_9.png" />

* After you have input the above information, click on the button **Split**. The recently created split Sales order will appear on the **List Order Splitted** area

<Image title="Image 8.png" alt={988} className="border" border={true} src="https://files.readme.io/c6d9831-Image_8.png" />

* At the same time, the value in two fields **Remain Cases** and **Remain Items** will update each time you create a split Sales order, to reflect the remaining quantity of cases/single items of the Big order

<Image title="Image 8.png" alt={988} className="border" border={true} src="https://files.readme.io/8baa699-Image_8.png" />

* If you want to remove a split Sales order, click on the corresponding remove icon :fa-remove: of that order under the **List Order Splitted** area

<Image title="Image 8.png" alt={988} className="border" border={true} src="https://files.readme.io/bde6910-Image_8.png" />

* After a split Sales order has been successfully created, it will automatically appear at the **Orders > Sales Orders** tab, on the selected Order Date
* To save the current state of the Big order, click on the button **Save**

- (Optional) If you find that the Big order can not be completed in the date range assigned, you can deliberately change the date range of that Big order, by clicking on the icon **Edit** :fa-pencil:, then change the **Start - End Date** attribute of that order

> 👍 Big order can be split multiple times
>
> You don't have to split the whole Big order at one time. As long as the current date doesn't doesn't exceed the attribute **End date** of the Big order, you will still be able to see and split that Big order

## Assign split Sales order to vehicle and Perform route optimization

* After you have split the Big order into smaller split Sales orders, you can continue to assign the split Sales order to vehicles and perform route optimization for those orders like with every other normal Sales order
* To assign a Sales order to a vehicle, follow [**this instruction**](https://docs.abivin.com/docs/vrp-outsourcing-fleet-route-optimization#section-accept-the-forwarded-order-and-assign-to-a-vehicle) 
* To perform route optimization, follow [**this instruction**](https://docs.abivin.com/docs/vrp-outsourcing-fleet-route-optimization#section-perform-route-optimization)
