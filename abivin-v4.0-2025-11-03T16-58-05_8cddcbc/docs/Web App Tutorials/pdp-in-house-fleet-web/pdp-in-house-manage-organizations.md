---
title: Manage Organizations
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
## Organization Definition

* **Organization** in PDP Model are defined and served exactly the same way as in VRP/DC Model. For more information on **Organization**, please refer to this article: [**Organization Definition**](https://docs.abivin.com/docs/vrp-dc-manage-organizations-eng#organization-definition)

## Organization Types and Hierarchy Chart

* **Organization Types and Hierarchy Chart** in PDP Model are defined and served exactly the same way as in VRP/DC Model. For more information on **Organization Types and Hierarchy Chart**, please refer to this article: [**Organization Types and Hierarchy Chart**](https://docs.abivin.com/docs/vrp-dc-manage-organizations-eng#organization-types-and-hierarchy-chart)

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Organization Type
      </th>

      <th>
        Direct Upper-level Organization type
      </th>

      <th>
        Functions and Resources
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Manufacturer
        (Required)
      </td>

      <td>
        Manufacturer (Itself)
      </td>

      <td>
        Have the management rights over all resources
      </td>
    </tr>

    <tr>
      <td>
        Branch\
        (Required)
      </td>

      <td>
        Manufacturer
      </td>

      <td>
        Directly manages the routing plan
      </td>
    </tr>

    <tr>
      <td>
        Depot\
        (Required)
      </td>

      <td>
        Branch
      </td>

      <td>
        Directly manages the customers; products inventory; vehicles; drivers; orders
      </td>
    </tr>
  </tbody>
</Table>

## Account Setup Orientation

* **Account Setup Orientation** in PDP Model are defined and served exactly the same way as in VRP/DC Model. For more information on **Account Setup Orientation**, please refer to this article: [**Account Setup Orientation**](https://docs.abivin.com/docs/vrp-dc-manage-organizations-eng#account-setup-orientation)

## Locate Organizations list

* Navigate to **Organizations > Organizations** tab
* This tab lists all the organizations you belong in or have the management rights over

<Image title="1. Org (ENG).png" alt={1920} border={true} src="https://files.readme.io/9ec297a-1._Org_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Org (VIE).png" alt={1920} border={true} src="https://files.readme.io/fa4c0eb-1._Org_VIE.png">
  Illustration (Vietnamese)
</Image>

## Create Organizations

* You have two methods to create the Organizations: Webform and Excel import file

### Create the Manufacturer

* The **Manufacturer** is the first Organization you have to create. This Organization can only be created using the Webform
* On the Webform, input the Organization Code and the Organization Name of the Manufacturer into the **Organization Code** and **Organization Name** fields, then click **Save**

<Image title="2. Create (ENG).png" alt={834} border={true} src="https://files.readme.io/46ed271-2._Create_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Create (VIE).png" alt={837} border={true} src="https://files.readme.io/598ca91-2._Create_VIE.png">
  Illustration (Vietnamese)
</Image>

* After the Manufacturer has been created, click its **Edit** icon :fa-pencil: On the **Update Organization** form, click on the **Parent Organization** field and select itself as its own **Parent Organization**. Next, click on the **Organization Categories** field, select the ***Manufacturer*** Organization Type from the drop-down menu. Click **Save** to confirm the change

<Image title="3. Parent 2 (ENG) Merge.png" alt={1699} border={true} src="https://files.readme.io/8695d40-3._Parent_2_ENG_Merge.png">
  Illustration (English)
</Image>

<Image title="3. Parent 2 (VIE) Merge.png" alt={1598} border={true} src="https://files.readme.io/8a704bc-3._Parent_2_VIE_Merge.png">
  Illustration (Vietnamese)
</Image>

* Now the Manufacturer has been fully set up. You can move on to create other lower-level Organizations using either the Webform or the Excel import file

### Create Lower-level Organizations

* After the Manufacturer has been created, you can create other lower-level Organizations using either the Webform or the Excel import file
* If you create the Organizations using the Excel import file, there are some notes that you should be aware of:
* 1 - When you create the direct lower-level Organizations of the Manufacturer - The Distributor or the Branch, you must copy the exact Organization Code of the Manufacturer on the Web app then paste it into the **Parent Organization Code** cell of the Distributor/Branch in the Excel import file

<Image title="2019-10-23 13_54_14-Window.png" alt={1674} border={true} src="https://files.readme.io/e5161e8-2019-10-23_13_54_14-Window.png">
  Illustration (English)
</Image>

<Image title="4. Create Org (VIE).png" alt={1920} border={true} src="https://files.readme.io/0f9884e-4._Create_Org_VIE.png">
  Illustration (Vietnamese)
</Image>

2 - When you create the Organizations that have yet to exist on the Web app, follow this step to create the parent-child relationship between an upper-level Organization and its direct lower-level Organizations (For example, a Branch and its Depot) in the Excel import file: Copy the Organization Code of the upper-level Organization from its **Organization Code** cell then paste that value into the **Parent Organization Code** cells of its direct lower-level Organizations

<Image title="2019-09-08 22_48_58-Window.png" alt={1917} border={true} src="https://files.readme.io/d22f800-2019-09-08_22_48_58-Window.png">
  Illustration (English)
</Image>

<Image title="4. Create Org (VIE) 2.png" alt={1919} border={true} src="https://files.readme.io/2535b94-4._Create_Org_VIE_2.png">
  Illustration (Vietnamese)
</Image>

### Organization information fields

* Below is the list of information fields of organizations of this model

> 📘 You don't necessarily need to input into every information fields
>
> Apart from the information fields mentioned below, other information fields can be left blank during the creation process

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
        Parent Organization (Web form);
        Parent Organization Code (Excel template)
        (Required)
      </td>

      <td>
        **1. Description:**\
        The direct upper level organization of the organization being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Input the Organization Name/Organization Code of the upper level organization of the organization being created into the search bar, then select from the drop down menu\
        **Excel template:**\
        Copy the Organization Code of the upper level organization of the organization being created on Web app, then paste into this cell\
        **Note:**\
        The Organization Name and Organization Code of organizations can be found under "Organization Name" and "Organization Code" columns in "Organizations > Organization List" tab
      </td>
    </tr>

    <tr>
      <td>
        Organization Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Organization Code assigned to the organization being created\
        **2. Input rules:**\
        Format: Must not contain spaces\
        For example: "Org 01" is not acceptable; "Org\_01" is acceptable\
        **Note:**\
        When you use the Web form, the organization code will automatically be capitalized\
        For example: If you input "Sample\_Organization\_Code", it will automatically be converted into "SAMPLE\_ORGANIZATION\_CODE"\
        This code is case sensitive\
        For example: "Sample\_Organization\_Code" is different than "SAMPLE\_ORGANIZATION\_CODE". Please pay attention when copying the code
      </td>
    </tr>

    <tr>
      <td>
        Organization Name\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Name of the organization being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Organization Category (Web form);\
        Organization Category Code (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Specify the Organization Type of the Shipper being created

        **2. Input rules:**\
        Webform:\
        Click on this field. Select the appropriate Organization Type from the drop-down menu\
        **Excel import file:**\
        If the Organization being created is a Distributor, input the following value into this cell (Remove the quotation marks when inputting): **"DISTRIBUTOR"**\
        If the Organization being created is a Branch, input the following value into this cell (Remove the quotation marks when inputting): **"BRANCH"**\
        If the Organization being created is a Depot, input the following value into this cell (Remove the quotation marks when inputting): **"DEPOT"**\
        If the Organization being created is a Sun, input the following value into this cell (Remove the quotation marks when inputting): **"SUN"**\
        If the Organization being created is a Crossdock, input the following value into this cell (Remove the quotation marks when inputting): **"CROSSDOCK"**\
        If the Organization being created is a Shipper, input the following value into this cell (Remove the quotation marks when inputting): **"SHIPPER"**

        **Notes when using the Excel import file:**\
        You must input the values exactly in English and in uppercase letters, as shown above. Do not input in any other language and lowercase letters
      </td>
    </tr>

    <tr>
      <td>
        Latitude, Longitude\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Coordinate information of the organization being created\
        **2. Input rules:**\
        Format: Decimal Degrees\
        For example: 41.40338 and 2.17403\
        Read this article for instruction: [**Get coordinate information of places**](https://docs.abivin.com/docs/how-to-get-coordinates-of-places)
      </td>
    </tr>

    <tr>
      <td>
        Open Time; Close Time\
        (Web form + Excel template)\
        (Required for organizations of Depot/Sun/Crossdock type)
      </td>

      <td>
        **1. Description:**\
        The regular time of day at which the organization being created officially starts working and closes\
        **2. Input rules:**\
        Format: hh:mm (24 hour format)\
        For example: The organization being created regularly starts working at 8:30 A.M and closes at 5:30 P.M everyday. You need to input the following values in the Open Time and Close Time fields/cells respectively: 08:30 and 17:30
      </td>
    </tr>

    <tr>
      <td>
        Min Time; Max Time\
        (Web form + Excel template)\
        (Required for organizations of Depot/Sun/Crossdock type)
      </td>

      <td>
        **1. Description:**\
        The minimum and maximum time period (In minutes) the Depot/Sun/Crossdock being created requires each vehicle to load products\
        **2. Input rules:**\
        On Web form, you need to click on "More Configurations" to see this information field\
        Input only the value in number. Do not input the unit\
        For example: The Depot/Sun/Crossdock being created requires each vehicle to load products no less than fifteen minutes and no more than thirty minutes. Input the following values into the Min Time and Max Time fields/cells respectively: 15; 30\
        Read more about this configuration at this article:
      </td>
    </tr>

    <tr>
      <td>
        Phone Number\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Phone contact of the organization being created\
        **2. Input rules:**\
        Format: Numbers only. Must not contain spaces\
        For example: "090 181 0800" or "090.181.0800" is not acceptable; "0901810800" is acceptable
      </td>
    </tr>

    <tr>
      <td>
        Address\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Official address where the organization being created is located\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

#### Organization Information On Webform

* On the Webform, the information of an Organization is present on two tabs: **Main Information** and **More Configuration**
* The **Main Information** tab holds the basic information of the Organization
* The **More Configuration** tab holds the specific information for each Organization Type. As you select the attribute **Organization Category** on the **Main Information** tab, this tab will update accordingly and gray out the information fields not related to the selected Organization Type
* For example, if the **Organization Category** is **Manufacture**, on the **More Configuration > Algorithm** tab, there would be a tooltip specifying which type of Organization for the grayed-out information fields not related to the selected Organization Type.

<Image title="5. Grayed (ENG) Merge.png" alt={1674} border={true} src="https://files.readme.io/482e705-5._Grayed_ENG_Merge.png">
  Illustration (English)
</Image>

<Image title="5. Grayed (VIE) Merge.png" alt={1676} border={true} src="https://files.readme.io/0ff9e79-5._Grayed_VIE_Merge.png">
  Illustration (Vietnamese)
</Image>

* We have a dedicated article for the configurations on the **More Configuration** tab: [**Configurations by Organization Type**](https://docs.abivin.com/docs/vrp-in-house-fleet-configurations-by-organization-type)

## Update Organization

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Delete Organization

* Please refer to the [**CRUD functions**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute

> 📘 BE VERY CAREFUL WHEN DELETING ORGANIZATIONS
>
> If you delete an organization, all resources of that organization as well as the resources of all organizations beneath it will be deleted\
> For example: If you delete a Branch, the resources of that Branch as well as of all Depots directly under that Branch will be deleted

## Search and Filter Organization

### Search Organization

* Enter either the **Organization Code** or the **Organization Name** of the organization you want to search in the search box :fa-search: 
* The system will filter and return result shortly

<Image title="6. Search (ENG).png" alt={1702} border={true} src="https://files.readme.io/e5f9cfd-6._Search_ENG.png">
  Illustration (English)
</Image>

<Image title="6. Search (VIE).png" alt={1711} border={true} src="https://files.readme.io/0408ec2-6._Search_VIE.png">
  Illustration (Vietnamese)
</Image>

## Filter Organization

* You can filter Organization that are the same **Organization Type** or share the same **Parent Organization** by clicking on the **Organization Categories** and **Parent Organization** columns then ticking on boxes in the drop down menus

<Image title="7. Filter (ENG).png" alt={1726} border={true} src="https://files.readme.io/5ae7de7-7._Filter_ENG.png">
  Illustration (English)
</Image>

<Image title="7. Filter (VIE).png" alt={1705} border={true} src="https://files.readme.io/41d93c6-7._Filter_VIE.png">
  Illustration (Vietnamese)
</Image>

* You can also search an organization quicker by typing the ***Organization Name*** or ***Organization Code*** of its upper level organization in the search bar of **Parent Organization** column; or the ***Organization Type*** in the search bar **Organization Categories** column

<Image title="8. Search (ENG) 2.png" alt={1729} border={true} src="https://files.readme.io/467ff22-8._Search_ENG_2.png">
  Illustration (English)
</Image>

<Image title="8. Search (VIE) 2.png" alt={1729} border={true} src="https://files.readme.io/1c95c0b-8._Search_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* You can combine these two filters for more accurate search results

## Locate Organizations on the map

* To view locations of organizations on the map, click on **View Map** icon (Next to the **Search** :fa-search: field)

<Image title="9. Map (ENG).png" alt={1703} border={true} src="https://files.readme.io/e71a630-9._Map_ENG.png">
  Illustration (English)
</Image>

<Image title="9. Map (VIE).png" alt={1710} border={true} src="https://files.readme.io/d8d4a91-9._Map_VIE.png">
  Illustration (Vietnamese)
</Image>

* On the map, each organization is marked by a :fa-map-marker: symbol
* Click on each :fa-map-marker: symbol to show the label of the organization
* Click on **View data table** :fa-table: icon to get back to the organization list screen

<Image title="10. View (ENG) 2.png" alt={1709} border={true} src="https://files.readme.io/9644cc3-10._View_ENG_2.png">
  Illustration (English)
</Image>

<Image title="10. View (VIE) 2.png" alt={1705} src="https://files.readme.io/4b11f49-10._View_VIE_2.png">
  Illustration (Vietnamese)
</Image>
