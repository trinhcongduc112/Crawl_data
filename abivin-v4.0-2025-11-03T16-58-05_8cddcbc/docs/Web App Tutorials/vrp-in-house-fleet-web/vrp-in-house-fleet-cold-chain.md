---
title: Cold Chain
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
## Activate Cold Chain configuration

* Navigate to **Organizations > Organization List** tab
* Click on **Edit** :fa-pencil: icon of the ***Branch*** which you want to activate the Cold Chain configuration
* On the **Update Organization** form, navigate to the sub-tab **More configuration > Algorithm**, then tick the **Use Cold Chain** checkbox
* Click **Save** to confirm the change

## Configure Temperature level for Products

* In Abivin vRoute, the Products can be classified into three following temperature levels:
* **Ambient**: Represented by the color **Orange** on the Timeline panel

<Image title="ambient product.png" alt={116} className="border" border={true} src="https://files.readme.io/7dde978-ambient_product.png" />

* **Chilled**: Represented by the color **Green** on the Timeline panel

<Image title="chill products.png" alt={116} className="border" border={true} src="https://files.readme.io/4bb4872-chill_products.png" />

* **Frozen**: Represented by the color **Blue** on the Timeline panel

<Image title="blue products.png" alt={116} className="border" border={true} src="https://files.readme.io/9d1f8dd-blue_products.png" />

### **Update Temperature level for existing products**

* If you haven't classified the temperature levels for the existing products correctly, you would have to do so by following these steps:
* Navigate to **Products > Products** tab
* Click on **Edit** :fa-pencil: icon of each product

<Image title="2019-10-30 11_15_18-Window.png" alt={1908} className="border" border={true} src="https://files.readme.io/d9a4633-2019-10-30_11_15_18-Window.png" />

* On the **Update Product** form, click on the **Temperature** field, then choose the appropriate temperature level for that product from the drop down menu
* Click **Update** to confirm the change

<Image title="2019-10-30 11_17_01-Window.png" alt={896} className="border" border={true} src="https://files.readme.io/80b6654-2019-10-30_11_17_01-Window.png" />

### **Update Temperature level for new products**

* For new products that have not been uploaded to the system, you can classify the temperature level for each product on both Web form and Excel template during the creation process
* The input rules are as below:

#### **Input rules on Web form**

* Click on the field then choose the appropriate Temperature level from the drop down menu

#### **Input rules on Excel template**

* Type either ***F, A*** or ***C*** into this cell. These letters represent ***Frozen, Ambient*** and ***Chilled*** respectively

<Image title="2019-10-30 11_18_11-Window.png" alt={157} className="border" border={true} src="https://files.readme.io/936c8eb-2019-10-30_11_18_11-Window.png" />

> ❗️ NOTE: One product can only have one Temperature level!

## Configure Temperature levels for Vehicles

* Next, we would have to configure the vehicles so that they can support specific temperature levels 
* A vehicle can support the products of the above three temperature levels and thus can have up to ***three*** temperature zones in its container. Each temperature zone is specially designed to carry products of one specific temperature level

<Image title="ITP_Bulkheads.png" alt={1060} border={true} src="https://files.readme.io/9f09d18-ITP_Bulkheads.png">
  A truck with three temperature zones
</Image>

* In case a vehicle doesn't have enough built-in temperature zones in its container for all the temperature levels it supports, products the temperature levels that account for the lowest volume of the total volume will be stored in portable ***temperature boxes***

<Image title="51a+AZZeihL._SX425_.jpg" alt={425} border={true} src="https://files.readme.io/ca25b1a-51aAZZeihL._SX425_.jpg">
  A temperature box
</Image>

### **Configure existing vehicles**

* Navigate to **Transportation > Vehicle List** tab
* Click on **Edit** :fa-pencil: icon of the vehicles you want to configure

<Image title="2019-10-30 11_21_37-Window.png" alt={1908} className="border" border={true} src="https://files.readme.io/65396f5-2019-10-30_11_21_37-Window.png" />

* On the **Update Vehicle** form, input the ***Temperature levels*** supported by the vehicles at the **Temperature** field by clicking on the field and click on the corresponding values in the drop down menu. Next, input the number of ***Temperature zones*** available in the vehicle container by inputting the value ***1, 2*** or ***3*** into the **Temp Zone** field

<Image title="2019-10-30 11_22_42-Window.png" alt={793} className="border" border={true} src="https://files.readme.io/a865d93-2019-10-30_11_22_42-Window.png" />

### **Configure new vehicles**

* For new vehicles that have not been uploaded to the system, you can specify the temperature levels and temperature zones of each vehicle on both Web form and Excel template during the creation process
* The input rules are as below:

#### **Input rules on Web form**

* Follow the instruction described above for existing vehicle

#### **Input rules on Excel template**

##### **Input rules for Temperature levels**

* If the vehicle being created supports products of ***Frozen*** temperature level, input the following value into the cell: ***F***
* If the vehicle being created supports products of ***Ambient*** temperature level, input the following value into the cell: ***A***
* If the vehicle being created supports products of ***Chilled*** temperature level, input the following value into the cell: ***C***
* If the vehicle being created supports products of ***Frozen*** and ***Ambient*** temperature levels, input the following value into the cell: ***FA***
* If the vehicle being created supports products of ***Frozen*** and ***Chilled*** temperature levels, input the following value into the cell: ***FC***
* If the vehicle being created supports products of ***Frozen***, ***Ambient*** and ***Chilled*** temperature levels, input the following value into the cell: ***FAC***

##### **Input rules for Temperature zones**

* Type the number of temperature zones available in the vehicle being created in the cell

> ❗️ The values above are case sensitive. You must write these exact values in the Excel template

<Image title="2019-10-30 11_27_13-Window.png" alt={255} className="border" border={true} src="https://files.readme.io/c0f6191-2019-10-30_11_27_13-Window.png" />

## Create orders and Optimize routes

* After you have configured the products and vehicles, you can proceed to create orders and optimize routes like usual

### **Temperature zones reservation rules**

* The available temperature zones will be used to store products of the the temperature levels that account for more percentage of the total volume of all products being delivered
* Other temperature levels not stored in the temperature zones will be stored in the temperature boxes. In Abivin vRoute, the temperature box is represented by this icon on the Timeline panel:

<Image title="temp box.png" alt={100} className="border" border={true} src="https://files.readme.io/306b4dd-temp_box.png" />

* For example, in the screenshot below, the vehicle supports all three temperature levels, but only has one temperature zone in its container. This only temperature zone is used to store products of ***Chilled*** temperature level because these products account for the largest percentage of the total volume. The products of ***Ambient*** and ***Frozen*** temperature levels will thus be stored in two temperature boxes

<Image title="2019-09-17 14_56_01-Window.png" alt={202} className="border" border={true} src="https://files.readme.io/188c2f3-2019-09-17_14_56_01-Window.png" />

### **Volume limit rules**

* During the route optimization process, the system will calculate the volume of products in each temperature level and compare with the volume capacity of the vehicle, using a set of ***Volume limit rules***. Below are the specific rules:

#### **For products stored in temperature zones**

* The total volume of temperature zones used to store ***Chilled*** and ***Frozen*** products must never exceed ***75%*** the volume capacity of the vehicle

#### **For products stored in temperature boxes**

* The volume of one temperature box must never exceed ***25%*** the volume capacity of the vehicle. This rule applies to all three temperature levels
* The volume of ***Chilled*** and ***Frozen*** products must never exceed ***75%*** the volume of the temperature boxes that store them. Combine with the 25% rule above, if the ***Chilled*** and/or ***Frozen*** products are put into temperature boxes, their volume must not exceed ***18.75%*** the volume capacity of the vehicle. If you run into this situation, you need to increase the number of temperature zones in the vehicle's container
* If any of the above rules is violated, the route optimization process would not be able to run
