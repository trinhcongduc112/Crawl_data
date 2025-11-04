---
title: Manage Sales Orders
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
## PDP Order Types

* In this model, there are two PDP Order Types:
* **Less than Truckload (LTL)**: This Order Type is used when a single Vehicle will pickup Products at multiple locations (Defined as the **Origin Customer**) then deliver to one or more locations (Defined as the **Destination Customer**)
* **Full Truckload (FTL)**: This Order Type is used when a single Vehicle will pickup Products at only one Origin Customer then deliver to only one Destination Customer

## Locate PDP Order List

* The PDP Orders can be classified into two groups based on their active status. The active status of a PDP Order is determined by comparing the current date on your computer with the **Date** attribute of that PDP Order. If the current date on your computer lies within the Date range of the PDP Order, that PDP Order is deemed as *Active*. On the other hand, if the current date on your computer is in the past in comparison with the Date range of the PDP Order, that PDP Order is deemed as *Inactive*
* The Active PDP Orders are listed on the **PDP Orders > Current Orders** tab
* This tab is where you can also create new PDP Orders

<Image title="1. Order List (ENG).png" alt={1920} border={true} src="https://files.readme.io/176dba7-1._Order_List_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Order List.png" alt={1920} border={true} src="https://files.readme.io/394c2c2-1._Order_List.png">
  Illustration (Vietnamese)
</Image>

* The past, inactive PDP Orders are listed on the **PDP Orders > Past Orders** tab

<Image title="2. Order List (ENG).png" alt={1920} border={true} src="https://files.readme.io/0be5a04-2._Order_List_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Order List (VIE).png" alt={1920} border={true} src="https://files.readme.io/fa4bcf8-2._Order_List_VIE.png">
  Illustration (Vietnamese)
</Image>

## Create PDP orders

### PDP Order Information Fields

* Below is the list of all information fields of a PDP Order

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organization
        (Webform)
        (Required)
      </td>

      <td>
        The Depot that directly manages the PDP Order being created. It is actually the parking garage of the Vehicles. The Vehicles will start their very first Delivery Shifts in a day at the parking garage
      </td>
    </tr>

    <tr>
      <td>
        Order Code\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        The management code assigned to the PDP Order being created\
        Format: Can contain letters, numbers, special characters. Must not contain spaces\
        For example: "Order Code 01" is invalid; "Order\_Code\_01" is valid
      </td>
    </tr>

    <tr>
      <td>
        Order Type\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        The Order Type of the PDP Order being created\
        There are two PDP Order Types, Full Truckload - FTL, and Less than Truckload - LTL, which have been mentioned at the beginning of this article
      </td>
    </tr>

    <tr>
      <td>
        Date\
        (Webform)\
        (Required)
      </td>

      <td>
        The date or date range during which the PDP Order being created can be performed
      </td>
    </tr>

    <tr>
      <td>
        Start Date; End Date\
        (Excel import file)\
        (Required)
      </td>

      <td>
        Start Date: The first date of the date range during which the order being created can be performed\
        End Date: The last date of the date range during which the order being created can be performed
      </td>
    </tr>

    <tr>
      <td>
        Origin Customer (Webform); Origin Pickup Code (Excel import file)\
        (Required)
      </td>

      <td>
        The Customer(s) where the Vehicles will travel to and pick up Products
      </td>
    </tr>

    <tr>
      <td>
        Destination Customer (Webform); Destination Delivery Code (Excel import file)\
        (Required)
      </td>

      <td>
        The Customer(s) where the Vehicles will travel to and deliver Products
      </td>
    </tr>

    <tr>
      <td>
        Origin Time Window\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        The time window during which the Vehicles can pick up Products at the Origin Customer location\
        This attribute will only be effective if the following configuration is enabled at the Branch: **Hard Time Windows**\
        Format: hh:mm-hh:mm\
        The time point must never exceed the 23:59\
        For example: 06:00-10:30 is valid; 06:00-24:30 is invalid
      </td>
    </tr>

    <tr>
      <td>
        Destination Time Window\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        The time window during which the Vehicles can deliver Products at the Destination Customer location\
        This attribute will only be effective if the following configuration is enabled at the Branch: **Hard Time Windows**\
        Format: hh:mm-hh:mm\
        The time point must never exceed 23:59\
        For example: 06:00-10:30 is valid; 06:00-24:30 is invalid
      </td>
    </tr>

    <tr>
      <td>
        Type of Vehicle (Webform); Vehicle Type (Excel import file)\
        (Optional)
      </td>

      <td>
        The Vehicle Type chosen to perform the PDP Order being created
      </td>
    </tr>

    <tr>
      <td>
        Sub-contractor (Webform); Use Subcontractor (Excel import file)\
        (Optional)
      </td>

      <td>
        This field specifies whether the PDP Order being created might/will be performed by the Vehicles of the sub-contractors or not\
        There are three options:

        * **No\***: The PDP Order being created will not be performed by the Vehicles of the sub-contractors
        * **Use if Needed\***: The PDP Order being created might be performed by the Vehicles of a sub-contractor should the managing Depot does not have any suitable active Vehicle available
        * **Always\***: The PDP Order being created will always be performed by the Vehicles of the sub-contractors
      </td>
    </tr>

    <tr>
      <td>
        Sub-contractor Name\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        Name of the sub-contractor whose Vehicles might/will perform the PDP Order being created
      </td>
    </tr>

    <tr>
      <td>
        Palletized\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        Specify whether the Products in the PDP Order being created will be placed on the pallets or not
      </td>
    </tr>

    <tr>
      <td>
        Product (Webform); Product Code (Excel import file)\
        (Required)
      </td>

      <td>
        The Product(s) in the PDP Order being created
      </td>
    </tr>

    <tr>
      <td>
        Expired Date\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        The date on which the Product in the PDP Order being created is deemed expired, no longer suitable for delivery
      </td>
    </tr>

    <tr>
      <td>
        Lot Number\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        The number of the Product Lot from where the whole cases/single items of the Product in the PDP Order being created are picked up
      </td>
    </tr>

    <tr>
      <td>
        Total Weight (kg)\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        The total weight value of the PDP Order being created, in kilogram (kg)
      </td>
    </tr>

    <tr>
      <td>
        Total Volume\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        The total volume value of the PDP Order being created, in cubic meter (m3)
      </td>
    </tr>

    <tr>
      <td>
        Self-calculated Stats\
        (Webform)\
        (Optional)
      </td>

      <td>
        Let the system automatically calculate the Total Weight, Total Volume, and Total Price attributes of the PDP Order instead of having the users manually input those values
      </td>
    </tr>

    <tr>
      <td>
        Pallet (Webform); Number Of Pallets (Excel import file)\
        (Required)
      </td>

      <td>
        The number of pallets of a specific Product in the PDP Order being created
      </td>
    </tr>

    <tr>
      <td>
        Number Of Cases\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        The number of whole cases of a specific Product in the PDP Order being created
      </td>
    </tr>

    <tr>
      <td>
        Number Of Items\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        The number of single items of a specific Product in the PDP Order being created
      </td>
    </tr>

    <tr>
      <td>
        Total Pallet\
        (Webform)\
        (Required)
      </td>

      <td>
        The total number of Product pallets in the PDP Order being created
      </td>
    </tr>

    <tr>
      <td>
        Total Price\
        (Webform + Excel import file)\
        (Required)
      </td>

      <td>
        The total price of the PDP Order being created
      </td>
    </tr>

    <tr>
      <td>
        Customer Reference Number\
        (Webform + Excel import file)\
        (Optional)
      </td>

      <td>
        The reference phone number of the Destination Customer location
      </td>
    </tr>

    <tr>
      <td>
        Check by\
        (Webform)\
        (Optional)
      </td>

      <td>
        The name of the staff who checks the accuracy of the PDP Order being created
      </td>
    </tr>
  </tbody>
</Table>

### Create PDP Orders Using The Webform

* When you use the Webform to create the PDP Orders, you ought to input the below information fields first to ensure there are no mistakes:
* Organization
* Order Code
* Order Type
* Date
* Origin Customer; Origin Time Window
* Destination Customer; Destination Time Window
* Below we will guide you on how to input each of the information fields on the Webform

#### 1.1. Organization

* Click on this field. Input the Organization Code/Organization Name of the desired Depot into the search bar then select it from the drop-down menu

<Image title="dwgOUc2fli.png" alt={566} border={true} src="https://files.readme.io/a4e7361-dwgOUc2fli.png">
  Illustration
</Image>

#### 1.2. Order Code

* The Order Code of the PDP Order is automatically generated in the following format: ***SO-yymmdd-xxxxx***, in which:
* ***SO*** is the acronym for ***Sales Order***
* ***yy*** is the last two digits of the current year. For example, if the current year is ***2021*** then the ***yy*** value would be ***21***
* ***mm*** is the current month. For example, if the current month is ***May*** then the ***mm*** value would be ***05***
* ***dd*** is the current date. For example, if the current date is ***Fifth*** then the ***dd*** value would be ***05***
* ***xxxxx*** is the numerical order of the PDP Order being created. This numerical order will automatically increase each time you open the **Create New Order** screen. For example, ***00001; 00002; 00003***, and so on
* You can also change the Order Code to the format that you normally use. However, please note that the Order Code must not contain spaces

<Image title="3. Order Code (ENG).png" alt={398} border={true} src="https://files.readme.io/560e0d3-3._Order_Code_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Order Code (VIE).png" alt={413} border={true} src="https://files.readme.io/2816985-3._Order_Code_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 1.3. Order Type

* Click on this field. Select the appropriate Order Type from the drop-down menu
* FTL (Full Truckload): Select this Order Type if you wish to generate the Route Plans in which:
* 1 - Each Order will have only one Origin Customer and only one Destination Customer 
* 2 - If a Vehicle is assigned multiple FTL Orders, that Vehicle will perform the Orders in a sequential manner
* For example, a Vehicle is assigned a Delivery Shift which consists of three FTL Orders, Order A, Order B, and Order C. In this scenario, the stop sequence on the Delivery Shift of the Vehicle might look like so: 
* Stop 1: Order A's Origin Customer
* Stop 2: Order A's Destination Customer
* Stop 3: Order B's Origin Customer
* Stop 4: Order B's Destination Customer
* Stop 5: Order C's Origin Customer
* Stop 6: Order C's Destination Customer
* LTL (Less than Truckload): Select this Order Type if you wish to generate the Route Plans in which:
* 1 - One Order can have more than one Origin Customer.
* 2 - If a Vehicle is assigned multiple LTL Orders, that Vehicle *might* travel to all the Origin Customer locations of the Orders to pick up Products first then deliver to all the Destination Customer locations
* Note: Notice that we say *might* instead of *always* because, in order to attain this, you need to set up the Origin and Destination Customers of those LTL Orders so that the Origin Customers share the same **City/Province** attribute, and so do the Destination Customers
* For example, a Vehicle is assigned a Delivery Shift which consists of three LTL Orders, Order A, Order B, and Order C. The Origin Customers of these three Orders are set up to have the same City/Province, and so do the Destination Customers. In this scenario, the stop sequence on the Delivery Shift of the Vehicle will look like so:
* Stop 1: Order A's Origin Customer
* Stop 2: Order B's Origin Customer
* Stop 3: Order C's Origin Customer
* Stop 4: Order A's Destination Customer
* Stop 5: Order B's Destination Customer
* Stop 6: Order C's Destination Customer

#### 1.4. Date

* Click on this field. Select the Start Date and End Date from the drop-down calendar then click the **Apply** button to finish creating the date range
* If the Origin and Destination Customer locations of the Order being created are located far away from each other, you should select a long date range that spans across several days to ensure the Order has enough time to be performed

<Image title="Date (ENG).gif" alt={1152} border={true} src="https://files.readme.io/10c72a7-Date_ENG.gif">
  Illustration (English)
</Image>

<Image title="Date (VIE).gif" alt={1152} border={true} src="https://files.readme.io/dea0d58-Date_VIE.gif">
  Illustration (Vietnamese)
</Image>

#### 1.5. Origin Customer & Destination Customer

* To select the Origin Customer, click on that field. Scroll the drop-down menu down until you see the desired Customer and select it. Alternatively, you can input the Customer Name/Customer Code into the search bar then select the returned result

<Image title="4. Customers (ENG).png" alt={1711} border={true} src="https://files.readme.io/548e22c-4._Customers_ENG.png">
  Illustration (English)
</Image>

<Image title="4. Customers (VIE) 2.png" alt={1709} border={true} src="https://files.readme.io/9b68fef-4._Customers_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* Note: If the Order Type is LTL then you can add multiple Origin Customers. To do that, click on the plus icon :fa-plus: to the right of the **New Customer** tab. Each time you click the plus icon, a new tab will appear. Each tab will allow you to select an Origin Customer as well as the Products to be picked up at that Origin Customer's location

<Image title="5. New Customer (ENg).png" alt={1707} border={true} src="https://files.readme.io/d0ac2e6-5._New_Customer_ENg.png">
  Illustration (English)
</Image>

<Image title="5. New Customer (VIE).png" alt={1704} border={true} src="https://files.readme.io/0b64bf0-5._New_Customer_VIE.png">
  Illustration (Vietnamese)
</Image>

* To select the Destination Customer, click on that field then follow the exact steps above

#### 1.6. Origin Time Window & Destination Time Window

> ❗️
>
> These attributes will only be effective if the following configuration is enabled at the Branch: **Hard Time Windows**

* Input the time window exactly in the ***hh:mm-hh:mm*** format. For example, ***08:00-12:30***
* If none of the Customers in the Order being created has time windows, leave these fields blank

<Image title="6. Time Window (ENG).png" alt={1707} border={true} src="https://files.readme.io/7fde208-6._Time_Window_ENG.png">
  Illustration (English)
</Image>

<Image title="6. Time Window (VIE).png" alt={1704} border={true} src="https://files.readme.io/98eda04-6._Time_Window_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 1.7. Type of Vehicle

* Click on this field. Select the appropriate Vehicle Type from the drop-down menu. Alternatively, you can input the Vehicle Type Code/Vehicle Type Name of the desired Vehicle Type into the search bar to filter out the result faster

<Image title="7. Vehicle Type (ENG).png" alt={1704} border={true} src="https://files.readme.io/28fec61-7._Vehicle_Type_ENG.png">
  Illustration (English)
</Image>

<Image title="7. Vehicle Type (VIE).png" alt={1700} border={true} src="https://files.readme.io/8bf7574-7._Vehicle_Type_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 1.8. Use Sub-contractor & Sub-contractor Name

* Click on this field. On the drop-down menu, select the appropriate option from the following three options: ***Always; Use if Needed; No***

<Image title="edit 7.png" alt={589} border={true} src="https://files.readme.io/daf6d95-edit_7.png">
  Illustration (English)
</Image>

<Image title="edit 6.png" alt={589} border={true} src="https://files.readme.io/3cce76a-edit_6.png">
  Illustration (Vietnamese)
</Image>

* If you select the ***Use if Needed*** or ***Always*** option, you have to specify the sub-contractor whose Vehicles might/will perform the Order being created. To do that, click on the **Sub-contractor Name** field then select the appropriate sub-contractor from the drop-down menu

<Image title="9. Subcontractor Name (ENG).png" alt={551} border={true} src="https://files.readme.io/f841e3b-9._Subcontractor_Name_ENG.png">
  Illustration (English)
</Image>

<Image title="9. Subcontractor Name (VIE).png" alt={562} border={true} src="https://files.readme.io/2873638-9._Subcontractor_Name_VIE.png">
  Illustration (Vietnamese)
</Image>

* Note: Prior to this, you need to set up the Vehicles as Sub-contractor Vehicles. Please refer to the main article for instruction: [**Manage Vehicles**]()

#### 1.9. Product

* Click on this field. Input the Product Name/Product Code of the desired Product into the search bar then select it from the drop-down menu. Next, click the **Add** button to add that Product to the Order being created. The selected Product will appear on the Product table

<Image title="10. Product Code (ENG).png" alt={1680} border={true} src="https://files.readme.io/06857b7-10._Product_Code_ENG.png">
  Illustration (English)
</Image>

<Image title="10. Product Code (VIE).png" alt={1687} border={true} src="https://files.readme.io/b9ff08e-10._Product_Code_VIE.png">
  Illustration (Vietnamese)
</Image>

* You can select multiple Products by repeating these steps
* If you accidentally added the wrong Product, click the **Remove** icon :fa-remove: of that Product to remove it from the Product table

<Image title="11. Remove (ENG).png" alt={1653} border={true} src="https://files.readme.io/7ce70a5-11._Remove_ENG.png">
  Illustration (English)
</Image>

<Image title="11. Remove (VIE).png" alt={1679} border={true} src="https://files.readme.io/715d92d-11._Remove_VIE.png">
  Illustration (Vietnamese)
</Image>

* After you have added the Products, you need to specify whether the Products will be placed on pallets or not

##### 1.9.1. Products Are Not Placed On Pallets

* Input the number of whole cases/single items of each Product into the corresponding **Number Of Cases/Number Of Items** fields
*  Product in the If there are zero single items of a specific Product in the Order being created, you must input the value ***0*** into the **Number Of Items** field of that Product

<Image title="12. Product not on Pallets (ENG).png" alt={1653} border={true} src="https://files.readme.io/5dd70df-12._Product_not_on_Pallets_ENG.png">
  Illustration (English)
</Image>

<Image title="12. Product not on Pallets (VIE).png" alt={1679} border={true} src="https://files.readme.io/4200107-12._Product_not_on_Pallets_VIE.png">
  Illustration (Vietnamese)
</Image>

* Similarly, If there are zero whole cases of a specific Product in the Order being created, you must input the value ***0*** into the **Number Of Cases** field

##### 1.9.2. Products Are Placed On Pallets

* If the Products will be placed on pallets, click the **Palletized** check box then input the number of pallets of each Product into its corresponding **Pallet** field

<Image title="13. Product on Pallets (ENG).png" alt={1706} border={true} src="https://files.readme.io/f226627-13._Product_on_Pallets_ENG.png">
  Illustration (English)
</Image>

<Image title="13. Product on Pallets (VIE).png" alt={1706} border={true} src="https://files.readme.io/76a824c-13._Product_on_Pallets_VIE.png">
  Illustration (Vietnamese)
</Image>

##### 1.9.3. Product Lot Number; Product Expired Date

* The **Expired date** and **Lot Number** fields are optional. If you don't have the information, you can safely leave these fields blank

<Image title="13. Expired (ENG).png" alt={1706} border={true} src="https://files.readme.io/c6b99d1-13._Expired_ENG.png">
  Illustration (English)
</Image>

<Image title="13. Expired (VIE).png" alt={1706} border={true} src="https://files.readme.io/f2ffb49-13._Expired_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 1.10. Total Weight; Total Volume and Total Price

##### 1.10.1. Manually Input Total Weight, Total Volume, And Total Price

* By default, these information fields **must be** input manually
* Only input the value (in number), do not input the unit

<Image title="14. Total (ENG).png" alt={580} border={true} src="https://files.readme.io/2caa303-14._Total_ENG.png">
  Illustration (English)
</Image>

<Image title="14. Total (VIE).png" alt={590} border={true} src="https://files.readme.io/5a97d02-14._Total_VIE.png">
  Illustration (Vietnamese)
</Image>

##### 1.10.2. Automatically Calculate Total Weight; Total Volume And Total Price

* If you wish to let the system automatically calculate this information, tick the **Self-calculated Stats** checkbox. These fields will be greyed out

<Image title="15. Self-calculated (ENG).png" alt={1693} border={true} src="https://files.readme.io/eaeacb4-15._Self-calculated_ENG.png">
  Illustration (English)
</Image>

<Image title="15. Self-calculated (VIE).png" alt={1700} border={true} src="https://files.readme.io/3d83e46-15._Self-calculated_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 1.11. Other optional information (Customer Reference Number; Check By)

* These information fields are optional. If you don't have information, just leave these fields blank
* After you have input all the necessary information, click on the blue **Save** button to finish creating the Order

<Image title="16. SAVE (ENG) 2.png" alt={1702} border={true} src="https://files.readme.io/44b4f0d-16._SAVE_ENG_2.png">
  Illustration (English)
</Image>

<Image title="16. SAVE (ENG).png" alt={1695} border={true} src="https://files.readme.io/0e6e908-16._SAVE_ENG.png">
  Illustration (Vietnamese)
</Image>

### Create PDP Orders Using The Excel Import File

* Below is the instruction to input in the information fields of the Excel import file

#### 2.1. Start Date; End Date

* Input in either the ***dd/mm/yyyy*** or ***mm/dd/yyyy*** format based on the current Date format of your computer

<Image title="2019-10-16 13_51_52-.png" alt={1673} border={true} src="https://files.readme.io/eb06e27-2019-10-16_13_51_52-.png">
  Illustration (English)
</Image>

<Image title="17. Date (VIE).png" alt={1920} border={true} src="https://files.readme.io/137a314-17._Date_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 2.2. Order Code

* As mentioned above, the Order Code must not contain spaces

<Image title="18. Order Code (ENG).png" alt={1920} border={true} src="https://files.readme.io/ab03141-18._Order_Code_ENG.png">
  Illustration (English)
</Image>

<Image title="18. Order Code (VIE).png" alt={1920} border={true} src="https://files.readme.io/88c92da-18._Order_Code_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 2.3. Order Type

* If the order being created is of ***Full Truckload*** type, input the following value into this cell: ***FTL***
* If the order being created is of ***Less than Truckload*** type, input the following value into this cell: ***LTL***

<Image title="19. Order Type (ENG).png" alt={1920} border={true} src="https://files.readme.io/43f313d-19._Order_Type_ENG.png">
  Illustration (English)
</Image>

<Image title="19. Order Type (VIE).png" alt={1920} border={true} src="https://files.readme.io/1ae815d-19._Order_Type_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 2.4. Origin Pickup Code & Destination Delivery Code

* Copy the Customer Codes of the desired Origin and Destination Customers on the Web app then paste them into the suitable cells in the Excel import file
* The Customer Codes can be found under the **Customer Code** column in the **Partners > Customers** tab

<Image title="2. Order Code (EDITED) (ENG).png" alt={1920} border={true} src="https://files.readme.io/90674e9-2._Order_Code_EDITED_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Order Code (EDITED) (VIE).png" alt={1920} border={true} src="https://files.readme.io/a26d720-2._Order_Code_EDITED_VIE.png">
  Illustration (Vietnamese)
</Image>

* If the Order being created is an LTL Order which has multiple Origin Customers and one Destination Customer, be sure to copy and paste the Customer Code of the Destination Customer into the **Destination Delivery Code** cells of each Origin Customer row

#### 2.5. Origin Time Window & Destination Time Window

* The time window format must be ***hh:mm-hh:mm***. Note that the timepoint must not exceed ***23:59***

<Image title="20. Time Window (ENG).png" alt={1920} border={true} src="https://files.readme.io/7aaa1fe-20._Time_Window_ENG.png">
  Illustration (English)
</Image>

<Image title="20. Time Window (VIE).png" alt={1920} border={true} src="https://files.readme.io/a1210cb-20._Time_Window_VIE.png">
  Illustration (Vietnamese)
</Image>

* If the Order being created is an LTL Order which has multiple Origin Customers and one Destination Customer, be sure to copy and paste the Time Window of the Destination Customer into the respective **Destination Time Window** cells of all Origin Customer rows

#### 2.6. Product

##### 2.6.1. Product Code

* Copy the Product Code of the appropriate product on the Web app, then paste it into this cell
* The Product Code can be found under the **Product Code** column in the **Products > Products** tab

<Image title="21. Product Code (ENG).png" alt={1920} border={true} src="https://files.readme.io/16c79a1-21._Product_Code_ENG.png">
  Illustration (English)
</Image>

<Image title="21. Product Code (VIE).png" alt={1920} border={true} src="https://files.readme.io/fe52c28-21._Product_Code_VIE.png">
  Illustration (Vietnamese)
</Image>

* If the Order being created has multiple Products, put each Product on a separate row. Note that you also have to copy and paste all the common information of the Order on each Product row
* Next, you need to specify whether the Products of an Order will be placed on pallets or not. An important thing to note is that in an Order, all Products can only be either placed on pallets or without pallets. You CANNOT mix these two product placement methods in one Order

##### 2.6.2. Products Are Not Placed On Pallets

* If the Products will not be placed on pallets, input the following value into all the **Palletized** cells of all Product rows: ***FALSE***
* Next, input the number of whole cases and/or single items of each Product into their respective **Number of Cases** and **Number of Items** cells. Don't forget to leave the **Number of Pallets** cells blank

<Image title="22.Palletized (ENG).png" alt={1920} border={true} src="https://files.readme.io/ab7b614-22.Palletized_ENG.png">
  Illustration (English)
</Image>

<Image title="22.Palletized (VIE).png" alt={1920} border={true} src="https://files.readme.io/5985623-22.Palletized_VIE.png">
  Illustration (Vietnamese)
</Image>

* *0*** into that If the Order being created contains zero whole cases of a particular Product, input the value ***0*** into that Product's **Number of Cases** cell. Similarly, if the Order being created contains zero single items of a particular Product, input the value ***0*** into that Product's **Number of Items** cell. DO NOT leave these cells blank

<Image title="2019-10-16 14_29_16-Window.png" alt={693} border={true} src="https://files.readme.io/0f629a9-2019-10-16_14_29_16-Window.png">
  Illustration (English)
</Image>

<Image title="edit 5.png" alt={621} border={true} src="https://files.readme.io/d3d9525-edit_5.png">
  Illustration (Vietnamese)
</Image>

##### 2.6.3. Products Are Placed On Pallets

* If the Products will be placed on pallets, input the following value into all the **Palletized** cells of all the Product rows: ***TRUE***
* Next, input the number of pallets of each Product into its corresponding **Number Of Pallets** cells. Do not forget to leave the **Number of Cases** and **Number of Items** cells of that Product blank

<Image title="2019-10-16 14_29_57-Window.png" alt={694} border={true} src="https://files.readme.io/8ade448-2019-10-16_14_29_57-Window.png">
  Illustration (English)
</Image>

<Image title="edit 4.png" alt={621} src="https://files.readme.io/acba130-edit_4.png">
  Illustration (Vietnamese)
</Image>

##### 2.6.4. Lot Number; Expired Date

* Input the lot number and expiry date of the product into these cells
* These information fields are optional. You can safely leave them blank

<Image title="23. Lot + Expired (ENG).png" alt={1920} border={true} src="https://files.readme.io/e53407c-23._Lot__Expired_ENG.png">
  Illustration (English)
</Image>

<Image title="23. Lot + Expired (VIE).png" alt={1920} border={true} src="https://files.readme.io/c6ca0b3-23._Lot__Expired_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 2.7. Total Price; Total Weight; Total Volume

* In the Excel import file, the Total Price. Total Weight. Total Volume values are of the whole Order, not of each separate Product. Therefore if the Order contains multiple Products, make sure to input the same Total Weight, Total Volume, Total Price values of the Order into all the respective cells of all Product rows

<Image title="24. Total (VIE).png" alt={1920} border={true} src="https://files.readme.io/90a4308-24._Total_VIE.png">
  Illustration (English)
</Image>

<Image title="24. Total (VIE).png" alt={1920} border={true} src="https://files.readme.io/1f8211e-24._Total_VIE.png">
  Illustration (Vietnamese)
</Image>

* If a value is a decimal number, the separator between the whole part and the decimal part can either be a dot (.) or a comma (,) based on the setting of your computer and the Excel software. Do check to see what is the correct input method

#### 2.8. Use Subcontractor; Subcontractor Name

* If the Order being created will not be performed by the Sub-contractor Vehicles, input the following value into the **Use Subcontractor** cell: ***NO***
* If the Order being created might be performed by the Sub-contractor Vehicles (In case your organization doesn't have any Vehicle left that can perform this Order), input the following value into the **Use Subcontractor** cell: ***USEIFNEEDED***
* If the order being created will be performed by the Sub-contractor Vehicles, input the following value into the **Use Subcontractor** cell: ***ALWAYS***
* If the **Use Subcontractor** cell value is either ***USEIFNEEDED*** or ***ALWAYS***, input the Sub-contractor name in the **Subcontractor Name** cell

<Image title="25. Use Subcontractor (ENG).png" alt={1920} border={true} src="https://files.readme.io/a3494b9-25._Use_Subcontractor_ENG.png">
  Illustration (English)
</Image>

<Image title="25. Use Subcontractor (VIE).png" alt={1920} border={true} src="https://files.readme.io/1784d59-25._Use_Subcontractor_VIE.png">
  Illustration (Vietnamese)
</Image>

* Note that you need to set up some of the available Vehicles to belong to the Sub-contractors first. After the Vehicles have been set up as Sub-contractor Vehicles, you can copy the name of the Sub-contractor in the Vehicle information on Web app then paste that value into the **Subcontractor Name** cell of the Order being created

<Image title="26. Add Sub (ENG).png" alt={897} border={true} src="https://files.readme.io/ab088d1-26._Add_Sub_ENG.png">
  Illustration (English)
</Image>

<Image title="26. Add Sub (VIE).png" alt={893} border={true} src="https://files.readme.io/61bc7bc-26._Add_Sub_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 2.9. Vehicle Type

* Copy the Vehicle Type Code of the desired Vehicle Type which will perform the Order being created on the Web app then paste it into this cell
* Vehicle Type Code can be found under the **Type Code** column in the **Transportation > Vehicle Type** tab

<Image title="27. Vehicle Type Code (ENG).png" alt={1920} border={true} src="https://files.readme.io/8332e3d-27._Vehicle_Type_Code_ENG.png">
  Illustration (English)
</Image>

<Image title="27. Vehicle Type Code (VIE).png" alt={1920} border={true} src="https://files.readme.io/915017d-27._Vehicle_Type_Code_VIE.png">
  Illustration (Vietnamese)
</Image>

#### 2.10. Customer Reference Number; Order Note

* These information fields are optional. If you don't have information, you can safely leave these cells blank

<Image title="28. Optional (ENG).png" alt={1920} border={true} src="https://files.readme.io/0ec7743-28._Optional_ENG.png">
  Illustration (English)
</Image>

<Image title="28. Optional (VIE).png" alt={1920} border={true} src="https://files.readme.io/b89eee4-28._Optional_VIE.png">
  Illustration (Vietnamese)
</Image>
