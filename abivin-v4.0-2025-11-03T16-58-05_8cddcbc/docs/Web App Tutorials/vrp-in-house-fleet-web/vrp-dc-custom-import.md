---
title: Custom Import Tool
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: link
      title: FAQ with Custom Import
      url: https://docs.abivin.com/docs/faq-with-custom-import
---
* **Custom Import** is a useful tool in our Web app. It is developed to help our users directly convert data from their proprietary data formats into Abivin vRoute standard data formats without having to use the usual object creation methods (Web form; Excel templates)
* At the moment, this **Custom Import** tool is developed for converting Delivery Order files (**Delivery Order**, shortened as **DO**). In this article, we will use the acronym **DO file** to refer to the **Delivery Order file** 

## Precondition to Use Custom Import

* To be able to use the Custom Import tool, you must make sure you are given permission or you have given permission to the Custom Import tool to the intended user groups. To grant permission to the  Custom Import tool, please follow these steps below
* Step 1: Navigate to tab **Organizations > User Groups**
* Step 2: Click the **Edit** icon :fa-pencil: of the User Groups that you would like to grant the permission to use the Custom Import tool
* Step 3: A form named **Update Group** will show up on the screen. On the tab **Main Information**, scroll down to find the **Mapping Profile** and tick the boxes of permissions you want to grant access to the selected user group. Please refer to this link to get detailed information on types of permission [Modules Sections](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#modules-section)
* Step 4: Click **Save** for changes to take effect.

<Image title="3. Mapping Profie (ENG).png" alt={1920} border={true} src="https://files.readme.io/48170e0-3._Mapping_Profie_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Mapping Profie (VIE).png" alt={1920} border={true} src="https://files.readme.io/09f1a64-3._Mapping_Profie_VIE.png">
  Illustration (Vietnamese)
</Image>

## General Steps to Use Custom Import tool

### Step 1: Access Custom Import tool & Upload DO file

* To access the Custom Import tool, first navigate to the tab **Settings > Custom Import**. On this tab, hover your mouse on the orange plus circle icon :fa-plus-circle:, then click on the icon **Import Data** 

<Image title="1. Custom Import (ENG).png" alt={1920} border={true} src="https://files.readme.io/de462d7-1._Custom_Import_ENG.png">
  Illustration (English)
</Image>

<Image title="1. Custom Import (VIE) 2.png" alt={1920} border={true} src="https://files.readme.io/8c0c522-1._Custom_Import_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* The form **Import From CSV/XLSX** will appear 

<Image title="1. New CSV (ENG).png" alt={1275} border={true} src="https://files.readme.io/361ea7e-1._New_CSV_ENG.png">
  Illustration (English)
</Image>

<Image title="1. New CSV (VIE).png" alt={1274} border={true} src="https://files.readme.io/27e22ff-1._New_CSV_VIE.png">
  Illustration (Vietnamese)
</Image>

* Click on the area **Drag and drop some files here or click to files**, select the appropriate CSV/XLSX DO file from your computer (**Note**: We strongly suggest using XLSX format to prevent unwanted inaccurate text decode)

<Image title="2. Drag and Drop (ENG).png" alt={1920} border={true} src="https://files.readme.io/650070e-2._Drag_and_Drop_ENG.png">
  Illustration (English)
</Image>

<Image title="2. Drag and Drop (VIE).png" alt={1920} border={true} src="https://files.readme.io/95ccbb8-2._Drag_and_Drop_VIE.png">
  Illustration (Vietnamese)
</Image>

### Step 2: Declare Mapping Profile

#### Mapping Profile definition

* Mapping Profiles are records that store the correct data mapping mechanism between user proprietary data formats and Abivin vRoute data formats

* After uploading a DO file as in Step 1, you need to declare the Mapping Profile for that DO file

* Here there are two scenarios: 

* **Scenario 1**: The Mapping Profile for the DO file hasn’t been created yet. In this scenario, you need to create a new Mapping Profile

* **Scenario 2**: The Mapping Profile for the DO file has already been created. In this scenario, you only need to select the correct Mapping Profile from the list of existing Mapping Profiles

* Depends on whether your account is Shipper-oriented or Carrier/Distributor oriented, the Mapping Profile declaration process will differ in certain steps

* If your account is Shipper-oriented, when you use the Custom Import tool, you only need to do the following to declare a new Mapping Profile

* 1 - Select a DO file then upload it to the Custom Import tool as in Step 1

* 2 - Select a Depot that manages the products listed in the DO file

* 3 - Name a Mapping Profile

* If your account is Carrier/Distributor-oriented, when you use the Custom Import tool, you need to do the following to declare a new Mapping Profile

* 1 - Select a DO file then upload it to the Custom Import tool as in Step 1

* 2 - Select a Depot that manages the products listed in the DO file

* 3 - Select a Shipper (owner/supplier of the products listed in the DO file)

* 4 - Name a Mapping Profile

#### Scenario 1: Create a new Mapping Profile

* After the DO file has been uploaded, click on the field **Organization** to select the **Depot** that will directly manage the Order being uploaded (The organizations of **Depot** type on Abivin Web app for both Shipper-oriented and Carrier/Distributor-oriented accounts)

<Image title="2. Mapping (VIE).png" alt={1275} border={true} src="https://files.readme.io/6e3ada7-2._Mapping_VIE.png">
  Illustration (English)
</Image>

<Image title="2. Mapping (ENG).png" alt={1274} border={true} src="https://files.readme.io/8543b75-2._Mapping_ENG.png">
  Illustration (Vietnamese)
</Image>

* If your account is Carrier/Distributor-oriented, you will need to specify the Shipper that is associated with the Customer in the DO file. To do this, then click on the field **Shipper Code** and select the intended Shipper on the drop-down list. Alternatively, you could enter the Organization Name/Organization Code of the desired Shipper into the search bar then select the returned value.

<Image title="3. Shipper Code 1 (ENG).png" alt={1593} border={true} src="https://files.readme.io/af71c6a-3._Shipper_Code_1_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Shipper Code 1 (VIE).png" alt={1594} border={true} src="https://files.readme.io/4e2de1f-3._Shipper_Code_1_VIE.png">
  Illustration (Vietnamese)
</Image>

* If your account is Shipper-oriented and you don't use **Shipper Code**, you could leave this field blank
* Next, click on the field **Profile Settings**, select the option **Create New Profile** to create a new Mapping Profile. A new field named **Profile Name** will appear on the right. Enter the name of the new Mapping Profile into the field **Profile Name** 

<Image title="4. Mapping a New Profile (ENG).png" alt={1593} border={true} src="https://files.readme.io/8393d7a-4._Mapping_a_New_Profile_ENG.png">
  Illustration (English)
</Image>

<Image title="4. Mapping a New Profile (VIE).png" alt={1588} border={true} src="https://files.readme.io/e428590-4._Mapping_a_New_Profile_VIE.png">
  Illustration (Vietnamese)
</Image>

* Mapping Profile Name format can contain letters, text, numbers, spaces and special characters (for example: ***Test @ Depot 1***). The name of the new Mapping Profile should not be the same as any of the existing Mapping Profiles'. 
* After you have created a new Mapping Profile, click **Next**. You will be navigated to the tab **Review Data**

<Image title="18. Next (ENG).png" alt={1270} border={true} src="https://files.readme.io/a91f4e3-18._Next_ENG.png">
  Illustration (English)
</Image>

<Image title="18. Next (VIE).png" alt={1272} border={true} src="https://files.readme.io/baaaaf9-18._Next_VIE.png">
  Illustration (Vietnamese)
</Image>

* On the tab **Review Data**, you need to select the Header row in the uploaded DO file. The Header row contains the name of the data fields in the DO file, which you will use to map with the Abivin vRoute standard data fields later. You need to move your mouse onto the preview, click on the row that contains the columns' name in the DO file. The row you clicked on will be highlighted in blue. If you are sure that the row you selected is the column name in the Abivin vRoute DO file, then click **Confirm**. The button ***Confirm*** will change to ***Confirmed***

<Image title="20. Confirmed (ENG).png" alt={1272} border={true} src="https://files.readme.io/614d74f-20._Confirmed_ENG.png">
  Illustration (English)
</Image>

<Image title="20. Confirmed (VIE).png" alt={1270} border={true} src="https://files.readme.io/c5f9a8f-20._Confirmed_VIE.png">
  Illustration (Vietnamese)
</Image>

* If you mistakenly selected the incorrect row, click on the text ***Undo*** (Below the text ***Confirmed***), then reselect the correct row

<Image title="21. Undo (ENG).png" alt={1273} border={true} src="https://files.readme.io/41d4a8f-21._Undo_ENG.png">
  Illustration (English)
</Image>

<Image title="21. Undo (VIE).png" alt={1273} border={true} src="https://files.readme.io/84ff02f-21._Undo_VIE.png">
  Illustration (Vietnamese)
</Image>

* After you have selected and confirmed the correct row that contains the headers, click **Next**
* You will be navigated to the tab **Match Columns**

<Image title="22. Next (ENG).png" alt={1273} border={true} src="https://files.readme.io/0071f28-22._Next_ENG.png">
  Illustration (English)
</Image>

<Image title="22. Next (VIE).png" alt={1273} border={true} src="https://files.readme.io/b074cab-22._Next_VIE.png">
  Illustration (Vietnamese)
</Image>

#### Scenario 2: Select existing Mapping Profile

* If the Mapping Profile for the DO file has been created earlier, then you only need to select that Mapping Profile instead of having to create a new Mapping Profile
* Click on the field **Organization** to select the appropriate Depot, then move on to the field **Shipper Code** to select the Owner/Supplier of the goods listed in the DO file. Then, click on the field **Profile Name**. On the drop-down list, select the appropriate Mapping Profile which has been created earlier. After these three fields have been selected, click **Next**
* You will be navigated to the tab **Match Columns**

<Image title="23. Select (ENG).png" alt={1752} border={true} src="https://files.readme.io/220df99-23._Select_ENG.png">
  Illustration (English)
</Image>

<Image title="23. Select (VIE).png" alt={1752} border={true} src="https://files.readme.io/80185da-23._Select_VIE.png">
  Illustration (Vietnamese)
</Image>

### Step 3: Map data fields

* On the tab **Match Columns**, you will need to map the data fields in the DO file uploaded to the corresponding data fields in the Abivin vRoute formats. Here, if you are creating a new Mapping Profile, you will need to match the data fields in the DO file with the corresponding data fields in Abivin vRoute database. If you’re using an existing Mapping Profile, then the data fields have already been mapped before
* You will see two data field columns.
* 1 - Data fields column on the left (1) is in Abivin vRoute format
* 2 - Data field column on the right (2) shows the data fields in your proprietary DO format

<Image title="17. Map Columns (ENG).png" alt={1885} border={true} src="https://files.readme.io/62e8eee-17._Map_Columns_ENG.png">
  Illustration (English)
</Image>

<Image title="17. Map Columns (VIE).png" alt={1919} border={true} src="https://files.readme.io/6e49b44-17._Map_Columns_VIE.png">
  Illustration (Vietnamese)
</Image>

* To map a data field, first click on that field on the data field column on the right. A drop down list will appear, showing the data fields in the DO file that you have uploaded earlier. Select the appropriate data field from the drop down list, then click on the button **Confirm Mapping**

<Image title="12. Confirm Mapping (ENG).png" alt={1434} border={true} src="https://files.readme.io/980b53a-12._Confirm_Mapping_ENG.png">
  Illustration (English)
</Image>

<Image title="Edited.png" alt={1593} border={true} src="https://files.readme.io/718982d-Edited.png">
  Illustration (Vietnamese)
</Image>

* **Note**: If the type of data field being mapped is Date (Order Date; Due Date, etc.), then right after you select that data field, below that data field will appear the field **Choose format**. To do this, you need to click on this field, select the date format similar to the current date format in the DO file 

<Image title="14.ate (ENG).png" alt={1588} border={true} src="https://files.readme.io/ecf1d21-14.ate_ENG.png">
  Illustration (English)
</Image>

<Image title="14.ate (VIE).png" alt={1586} border={true} src="https://files.readme.io/f2cc45a-14.ate_VIE.png">
  Illustration (Vietnamese)
</Image>

* For example: In the DO file, the date format of the field **Order Date** is ***date/month/year (dd/mm/yyyy)*** (for instance, ***10/05/2021***) then you need to select this date format on the Custom Import tool

<Image title="15. Date (ENG) (Ex).png" alt={1588} border={true} src="https://files.readme.io/7145b11-15._Date_ENG_Ex.png">
  Illustration (English)
</Image>

<Image title="15. Date (VIE) (Ex).png" alt={1586} border={true} src="https://files.readme.io/fea19f8-15._Date_VIE_Ex.png">
  Illustration (Vietnamese)
</Image>

* If you mistakenly mapped the wrong data fields, please click on the button **Edit** to remap them

<Image title="14. Edit (English).png" alt={1434} border={true} src="https://files.readme.io/dca2ec9-14._Edit_English.png">
  Illustration (English)
</Image>

<Image title="14. Edit (VIE).png" alt={1427} border={true} src="https://files.readme.io/e564c71-14._Edit_VIE.png">
  Illustration (Vietnamese)
</Image>

* If you do not wish to map a particular data field, click on the corresponding button **Ignore this column**

<Image title="13. Ignore Columns (ENG).png" alt={1434} border={true} src="https://files.readme.io/1af7a5a-13._Ignore_Columns_ENG.png">
  Illustration (English)
</Image>

<Image title="13. Ignore Columns (VIE).png" alt={1432} border={true} src="https://files.readme.io/402258f-13._Ignore_Columns_VIE.png">
  Illustration (Vietnamese)
</Image>

* In the left column (the column of data in Abivin vRoute format), some data fields cannot be ignored and require you to map information, which are
* 1. Order Date
* 2. Order Code
* 3. Product Code
* 4. Product Name
* 5. Number of Items
* In case your account is Shipper-oriented, in the left column, there are also other 2 compulsory data fields that require mapping, which are 
* 1. Customer Code
* 2. Customer Name
* In case your account is Carrier/Distributor-oriented, in the left column, there are other 3 compulsory data fields that require mapping, which are
* 1. Ship-to Code
* 2. Ship-to Name
* 3. Ship-to Address
* All the compulsory data fields that require mapping have the asterisk :fa-asterisk: at the end of their field name.

<Image title="Asterisk (ENG).png" alt={740} border={true} src="https://files.readme.io/f9ff627-Asterisk_ENG.png">
  Illustration (English)
</Image>

<Image title="Asterisk (VIE).png" alt={738} border={true} src="https://files.readme.io/d43b0ac-Asterisk_VIE.png">
  Illustration (Vietnamese)
</Image>

* After you have completed mapping all the necessary data fields, click on the button **Next**
* You will be navigated to the tab **Review Mapping**

### Step 4: Review and import data

* On this tab **Review Mapping**, you could see a preview of the mapping result. The header row (first row) shows the data fields in Abivin vRoute format, while the data row (second row) shows the actual data fields from the DO file
* If you don’t see any error with the mapping, click on the button **Finish**

<Image title="15. Check (ENG).png" alt={1434} border={true} src="https://files.readme.io/3f64f29-15._Check_ENG.png">
  Illustration (English)
</Image>

<Image title="15. Check (VIE).png" alt={1434} border={true} src="https://files.readme.io/ec568ae-15._Check_VIE.png">
  Illustration (Vietnamese)
</Image>

* Upon clicking on this button, the system will immediately check the data in the DO file. If the data satisfies all import rules, then the DO file will be successfully converted, and the data in the DO file will be imported into Abivin vRoute database for the following three resources (In chronological sequence): **Products; Customers; Orders**. There will be a popup to announce the successful conversion

<Image title="17. Upload (ENG).png" alt={258} border={true} src="https://files.readme.io/3c9d4ee-17._Upload_ENG.png">
  Illustration (English)
</Image>

<Image title="17. Upload.png" alt={248} border={true} src="https://files.readme.io/774bf2c-17._Upload.png">
  Illustration (Vietnamese)
</Image>

* **Note**: If in the DO file being uploaded, there are Orders/Customers/Products that have already existed on Abivin vRoute system, then the data in the DO file will not overwrite Abivin vRoute data. Instead, the system will display the error message notifying the errors. For example, if an Order has been available in the system before and you mistakenly import it with the Custom Import tool once again, the system will display the error message as in the photos below. 

<Image title="16. Error (ENG).png" alt={1431} border={true} src="https://files.readme.io/aabfd67-16._Error_ENG.png">
  Illustration (English)
</Image>

<Image title="16. Error (VIE).png" alt={1431} border={true} src="https://files.readme.io/d47074b-16._Error_VIE.png">
  Illustration (Vietnamese)
</Image>

* If the information on Orders/Customers/Products has not been available in the database of Abivin vRoute before, the system will generate records. The most recently generated information of the new Orders/Customers/Products will be displayed on top of the first page of the corresponding tab for each resource. 
* For example: Your DO file has two orders with two Products and you use the Custom Import tool to import information to Abivin vRoute. The information on Products from your DO file will be gathered, converted and displayed on the top of the first page in tab **Products** as in the photo below.

<Image title="12. Import First Page (ENG).png" alt={1678} border={true} src="https://files.readme.io/46ac726-12._Import_First_Page_ENG.png">
  Illustration (English)
</Image>

<Image title="12. Import First Page (VIE).png" alt={1690} border={true} src="https://files.readme.io/560e3cb-12._Import_First_Page_VIE.png">
  Illustration (Vietnamese)
</Image>

## Custom Import Tool History

* Each time you import a CSV/XLSX file into Abivin vRoute database using the Custom Import tool or directly import via FTP server, the system will store the import history of that file right on the tab **Settings > Custom Import**

<Image title="7. History (ENG).png" alt={1920} border={true} src="https://files.readme.io/23529c9-7._History_ENG.png">
  Illustration (English)
</Image>

<Image title="7. History (VIE).png" alt={1920} border={true} src="https://files.readme.io/919d918-7._History_VIE.png">
  Illustration (Vietnamese)
</Image>

* To search for a specific import file, import the correct Import File Name into the search bar

<Image title="8. Search (ENG).png" alt={1697} border={true} src="https://files.readme.io/234d0a6-8._Search_ENG.png">
  Illustration (English)
</Image>

<Image title="8. Search (VIE).png" alt={1733} border={true} src="https://files.readme.io/724ac79-8._Search_VIE.png">
  Illustration (Vietnamese)
</Image>

* To filter import files by organizations, click on the field **Organization** and select the appropriate organization (Of Depot type)
* To filter the files by their import status, click on the column **Import Status**. On the drop-down menu, tick the checkboxes of the wanted statuses (***Progressing; Success; Failed***)

<Image title="11. IMport Status (ENG).gif" alt={1728} border={true} src="https://files.readme.io/11a1f29-11._IMport_Status_ENG.gif">
  Illustration (English)
</Image>

<Image title="11. Import Status (VIE).gif" alt={1728} border={true} src="https://files.readme.io/f3785ad-11._Import_Status_VIE.gif">
  Illustration (Vietnamese)
</Image>

* To see the reason why a specific file was failed to be imported, click the respective text ***Details*** of that file. On the right side of the screen will appear the tab **Import Detail**, citing the fail reason

<Image title="Reason (ENG) 2 - Merged 1.png" alt={1711} border={true} src="https://files.readme.io/f224457-Reason_ENG_2_-_Merged_1.png">
  Illustration (English)
</Image>

<Image title="Reason (VIE) 2 - Merged 1.png" alt={1710} border={true} src="https://files.readme.io/4ae364b-Reason_VIE_2_-_Merged_1.png">
  Illustration (Vietnamese)
</Image>

* To download a file, click the respective download icon :fa-download: of that file under the column **Action**

<Image title="4. Action (ENG).png" alt={1729} border={true} src="https://files.readme.io/f3f20b5-4._Action_ENG.png">
  Illustration (English)
</Image>

<Image title="6. Actions(VIE).png" alt={1704} border={true} src="https://files.readme.io/2d81677-6._ActionsVIE.png">
  Illustration (Vietnamese)
</Image>
