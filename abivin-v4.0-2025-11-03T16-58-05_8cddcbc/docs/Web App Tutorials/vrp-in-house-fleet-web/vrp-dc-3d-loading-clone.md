---
title: 3D Loading
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
* During the Route Plan optimization process, you can see how the products are placed inside the vehicle cargo using the product 3D loading feature

## Compulsory Configurations

### Enable 3D Loading Configuration

* First, enable the **Use 3D Loading** configuration at the Branch (Located in the **More Configurations > 3D Loading** section)
* After enabling, several sub-configurations will appear below

#### Sub-configuration 1: Algorithm Activation Mechanism

* This sub-configuration specifies whether the system will run the 3D loading algorithms simultaneously with the routing algorithms or will only run after the routing algorithms have completed
* To enable this sub-configuration, tick the **During Routing** checkbox
* With this  
* Upon ticking, an input field that reads ***Initialize 3D loading only when vehicle fill rate reaches ... % of volume***. This field specifies the vehicle volume capacity threshold at which the system will run the 3D loading algorithms
* For example, if you input the value ***80*** in this field, then the system will run the 3D loading algorithms once the product volume reaches eighty percents of the vehicle cargo's volume capacity

#### Sub-configuration 2: Product Placement Priority By Product Case Attributes

* This sub-configuration will specify the priority when placing the products inside the vehicle cargo by the three following attributes of the product case: Density; Weight; and Volume

#### Sub-configuration 3: Delivery Stop Priority

* This sub-configuration will specify how the products of each delivery stop should be placed inside the vehicle cargo
* If you tick the **Follow FILO rule** radio box, the system will place the products according to the FILO rule, which is the abbreviation of ***First In Last Out***. By this rule, products of the last Delivery Stop on the vehicle's optimized Delivery Route will be placed at the innermost space of the vehicle cargo, while products of the first Delivery Stop on the vehicle's optimized Delivery Route will be placed at the outermost space of the vehicle cargo, near the cargo doors
* If you tick the **No priority** radio box, the system will not apply the FILO rule, which means the products of a Delivery Stop might be placed at random positions inside the vehicle cargo
* If you tick the **Follow FILO Rule** radio box, the system will apply the FILO rule. Furthermore, an input field that reads: ***Product proximity: Maximum distance between products of the same stop is ... cm*** will appear. This field specifies the maximum distance (Calculated in centimeter - cm) between any two product cases of the same Delivery Stop when loading inside the vehicle cargo
* For example, if you input the value ***80*** in this field, then the system will generate the 3D loading projection so that any two product cases of the same Delivery Stop will be placed no further than eighty centimeters from each other

#### Sub-configuration 4: Product Placement Priority By Vehicle Cargo Axes

* This sub-configuration specifies how the product cases should be placed along the axes of the vehicle cargo
* The default dimension is Width and cannot be changed. With the other two dimensions, Length and Height, you can swap their priority
* If the priority sequence is Width > Length > Height, then the product cases will be placed in the following mechanism:
* 1 - Place the product cases at the innermost space, along the width of the vehicle cargo, from left to right

- 2 - After the product cases have filled a row by width, move forward toward the vehicle cargo doors, then continue to place the other product cases along the width from left to right

* 3 - After the product cases have covered the placeable surface, the system will continue placing the remaining product cases on top of the existing product cases, starting from the left innermost case

### Setup Products

* You must set up the following attributes for the Products:
* 1 - **Items per Case**: This attribute specifies the number of single product items inside a whole product case
* For example, one battery case consists of one hundred single batteries, In this scenario, input the following value into this field: ***100***
* 2 - **Length; Width; Height**: This attribute specifies the length, the width, and the height of the whole product case (Calculated in meter - m)
* For example, the dimensions of one refrigerator case are one meter in length; one meter in width; and two meters in height. In this scenario, input the following values into the **Length; Width; Height** fields, respectively: ***1; 1; 2***
* 3 - **Weight; Volume**: This attribute specifies the weight (Calculated in kilogram - kg) and the volume (Calculated in cubic meter - m3) of the whole product case
* For example, the weight and volume of one refrigerator case are two hundred kilograms and two cubic meters. Input the following values into the **Weight; Volume** fields, respectively: ***200; 2***
* 4 - **Number of Layers**: This attribute specifies the maximum number of whole product cases of the same product that can be stacked inside the vehicle cargo
* For example, it is required that with the refrigerator, only two cases can be stacked on top of each other. In this scenario, input the following value into this field: ***2***
* 5 - **Facets**: This attribute specifies which facets of a whole product case can face the vehicle cargo floor or face other product cases that are placed beneath it when loading inside the vehicle cargo. There are seven options: 
* Option 1. The front and the back facets
* Option 2. The left and the right facets
* Option 3. The top and the bottom facets
* Option 4: The front, the back, the left, and the right facets. This option equals Option 1 pluses Option 2
* Option 5: The front, the back, the top, and the bottom facets. This option equals Option 1 pluses Option 3
* Option 6: The left, the right, the top, and the bottom facets. This option equals Option 2 pluses Option 3
* Option 7: All six facets. This option equals all three Option 1, Option 2, and Option 3
* On the Webform, tick the checkbox(es) of the options to select them. The checkbox(s) you tick corresponds with one of the seven options mentioned above
* In the Excel file, for each Product row, input one of the following seven digits into the **Facets** cell: ***1; 2; 3; 12; 13; 23; 123***. Each of these digits corresponds with one of the seven options mentioned above. For example, the digit ***23*** equals Option 5 

### Setup Vehicles

* You must set up the following attributes for the Vehicles:
* 1 - **Weight; Volume**: The maximum weight-capacity (Calculated in kilogram - kg) and volume-capacity (Calculated in cubic meter - m3) that the vehicle cargo can carry
* 2 - **Cargo Area Length; Cargo Area Width; Cargo Area Height**: The length, the width, and the height (Calculated in meter - m) of the vehicle cargo

## Access 3D Loading

* You can access the 3D Loading simulation from both the Route Plan Map View and List View modes

### Access 3D Loading From Route Plan (Map View)

* On the Timeline panel, click on the warehouse icon at the start of a Vehicle's Delivery Shift
* The warehouse information panel will appear on the right side
* Click the **3D Loading Plan** text at the bottom of the panel
* Upon clicking, a new browser tab will automatically open, showing the 3D loading simulation

- First, navigate to the tab **Transportation > Route Plan** 
- Click on the text **Detail** (Under the column **Edit**) of the Route Plan
- On the screen **Route Plan Details**, click on the right angle icon :fa-angle-right: on the row containing the Vehicle Code to display the Delivery Routes assigned to that vehicle. Continue to click on the right angle icon :fa-angle-right: on the row containing the Delivery Route code to display the Delivery Trips inside those Delivery Routes
- Next, scroll the horizontal scrollbar to the far right of the screen until you see the column **Edit**. Click on the text **3D Loading** of a Delivery Trip
- You will be directed to the tab **Transportation > 3D Loading**
- On this tab, you can view how the products of the Delivery Trip are loaded in the vehicle container in a simulated three-dimensional environment
- On the right side of the screen, you can select four viewpoints: ***3D view, Top view, Side view; Front view***
- You can also left click on a random point on the screen and, with the left mouse button still pressed, move around to see the 3D view from multiple angles. You can also use the middle scroll button on your mouse to zoom in and out the 3D view

<Image title="3d loading.gif" alt={1676} className="border" border={true} src="https://files.readme.io/93368de-3d_loading.gif" />

* To view the details of a particular Order, click on the respective Order Code on the panel. Details of that Order will appear. The 3D projection will also show only the products of that Order (1)
* You can collapse the Order panel by clicking on the left angle button :fa-angle-left: on the top left corner of the 3d projection (2)
* To download the current 3D loading plan of the vehicle, click on the Download button :fa-download: at the bottom right of the screen. After a few moments, an Excel spreadsheet will be generated (3)

<Image title="kJZPwTpiJ3.png" alt={1680} className="border" border={true} src="https://files.readme.io/ff884ba-kJZPwTpiJ3.png" />

* Below are the axes of the vehicle container: The blue line represents the X-axis; the red line represents the Y-axis; and the green line represents the Z-axis

<Image title="eVEAxS7fML.png" alt={768} className="border" border={true} src="https://files.readme.io/4b4256a-eVEAxS7fML.png" />

### 3D loading plan Excel spreadsheet

* Below are the information fields in the 3D loading plan Excel spreadsheet

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
        "No"
      </td>

      <td>
        Numerical index
      </td>
    </tr>

    <tr>
      <td>
        "Order Code"
      </td>

      <td>
        Order Code
      </td>
    </tr>

    <tr>
      <td>
        "Product Code"
      </td>

      <td>
        Product Code
      </td>
    </tr>

    <tr>
      <td>
        "Length"
      </td>

      <td>
        The length attribute of the product
      </td>
    </tr>

    <tr>
      <td>
        "Width"
      </td>

      <td>
        The width attribute of the product
      </td>
    </tr>

    <tr>
      <td>
        "Height"
      </td>

      <td>
        The height attribute of the product
      </td>
    </tr>

    <tr>
      <td>
        "Ox"
      </td>

      <td>
        The placement position of the product along the X-axis
      </td>
    </tr>

    <tr>
      <td>
        "Oy"
      </td>

      <td>
        The placement position of the product along the Y-axis
      </td>
    </tr>

    <tr>
      <td>
        "Oz"
      </td>

      <td>
        The placement position of the product along the Z-axis
      </td>
    </tr>

    <tr>
      <td>
        "X"
      </td>

      <td>
        Indicates how much the product fills the X-axis
      </td>
    </tr>

    <tr>
      <td>
        "Y"
      </td>

      <td>
        Indicates how much the product fills the Y-axis
      </td>
    </tr>

    <tr>
      <td>
        "Z"
      </td>

      <td>
        Indicates how much the product fills the Z-axis
      </td>
    </tr>
  </tbody>
</Table>

## Notes when using 3D Loading

* It should be mentioned that during the Route Plan optimization process, the system will not check the attributes **Length, Width, Height, Number of Layers, Facets** of the Products against the attributes **Length, Width, Height** of the Vehicles’ container. These attributes would only be checked when generating 3D Loading projection
* Therefore, there may happen two scenarios when the item dimensions exceed the vehicle container's dimensions

### Scenario 1. Single product item's dimensions exceeds vehicle container's dimensions

* For example: A single item of a product has the (Length, Width, Height) dimensions to be ***(10, 3, 3) meter***
* The vehicle's container has the (Length, Width, Height) dimensions to be ***(6, 3, 3) meter***
* In this scenario, that product item is oversized in comparison with the vehicle's container. On the 3D projection, the oversized product items will be placed *on the left side* of the vehicle's container. On the Order panel, the Order code containing the oversized product items will have an orange warning sign :fa-exclamation-circle:

<Image title="e6X1e55PY0.png" alt={1214} className="border" border={true} src="https://files.readme.io/6fc233a-e6X1e55PY0.png" />

### Scenario 2: Total product items' dimensions exceeds vehicle container's dimensions

* For example: A single item of a product has the (Length, Width, Height) dimensions to be ***(4, 3, 3) meter***
* The vehicle's container has the (Length, Width, Height) dimensions to be ***(6, 3, 3) meter***
* In this scenario, the vehicle can carry only one single item of the above product. If the vehicle is assigned to carry multiple single items of that product, the remaining items will be placed into *fake* containers, located to the right of the vehicle’s real container on the 3D projection. This will help you see the size of the exceeding product items, so that you can make appropriate adjustments to the Orders and/or the vehicle's container dimensions in order to successfully load all items

<Image title="jG37Gi5WdZ.png" alt={1205} className="border" border={true} src="https://files.readme.io/2af4420-jG37Gi5WdZ.png" />
