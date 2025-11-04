---
title: FAQ with Custom Import
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
### Lacking Buttons on Mapping Profile Screen

* Lacking buttons on Mapping Profile Screen is closely related to which permissions you have been given to use Custom Import Tool. Please refer to this detailed instruction on giving permissions to Custom Import Tool [**Precondition to use Custom Import Tool**](https://docs.abivin.com/docs/vrp-dc-custom-import#precondition-to-use-custom-import)
* When you are not given certain permissions, you will see some buttons corresponding with those permissions unavailable in your Mapping Profile screen. 
* If the box **Create** is not ticked in the Mapping Profile, the button **Create New Profile** will not be available on the screen.

<Image title="1. Lack Button Create (ENG) - Merge 1.png" alt={1434} border={true} src="https://files.readme.io/da30c11-1._Lack_Button_Create_ENG_-_Merge_1.png">
  Illustration (English)
</Image>

<Image title="1. Lack Button Create (VIE) - Merge 1.png" alt={1590} border={true} src="https://files.readme.io/5af9515-1._Lack_Button_Create_VIE_-_Merge_1.png">
  Illustration (Vietnamese)
</Image>

* If the box **Delete** is not ticked in the Mapping Profile, the trashbin icon :fa-trash: will not be available to the right of the existing mapping profile, hence you are not able to delete existing mapping profiles.

<Image title="1. Lack Button Delete (ENG) - Merge 2.png" alt={1435} border={true} src="https://files.readme.io/8bc56fd-1._Lack_Button_Delete_ENG_-_Merge_2.png">
  Illustration (English)
</Image>

<Image title="1. Lack Button Delete (VIE) - Merge 2.png" alt={1594} border={true} src="https://files.readme.io/2e94a3b-1._Lack_Button_Delete_VIE_-_Merge_2.png">
  Illustration (Vietnamese)
</Image>

* If the box **Update** is not ticked, in the Match Columns screen, the **Edit** button will not show up. You could not edit the selected mapping profile.

<Image title="1. Lack Button Edit (ENG) - Merge 2.png" alt={1433} border={true} src="https://files.readme.io/8d650f2-1._Lack_Button_Edit_ENG_-_Merge_2.png">
  Illustration (English)
</Image>

<Image title="1. Lack Button Edit (VIE) - Merge 2.png" alt={1594} border={true} src="https://files.readme.io/3ee2bc0-1._Lack_Button_Edit_VIE_-_Merge_2.png">
  Illustration (Vietnamese)
</Image>

* If the box **Read** is not ticked, you could not see the existing mapping profile. In case the you are not given the access to **Create**, the **Next** button in the Mapping Profile Screen will be disabled as in the photo below. 

<Image title="3. Disabled Next Button (ENG).png" alt={1434} border={true} src="https://files.readme.io/d61789e-3._Disabled_Next_Button_ENG.png">
  Illustration (English)
</Image>

<Image title="3. Disabled Next Button (VIE) 3.png" alt={1591} border={true} src="https://files.readme.io/0163097-3._Disabled_Next_Button_VIE_3.png">
  Illustration (Vietnamese)
</Image>

### Required Product Categories when importing orders

* When you import orders with Custom Import, if the products in the order file have not been input in the system yet, an error message will show up on the screen as in the photo below

<Image title="7. Other categories.png" alt={1846} className="border" border={true} src="https://files.readme.io/e12d1e4-7._Other_categories.png" />

* In this case, please create a product category named **Other**. After you create a new product category, please return to Custom Import and upload the order file again; the new products will be added to the newly created product category **Other** and will be imported successfully. 

<Image title="Other Categories.png" alt={1698} className="border" border={true} src="https://files.readme.io/cad2fb9-Other_Categories.png" />

For detailed instruction on creating product categories, please refer to this link [Manage Product Categories](doc:vrp-in-house-fleet-manage-product-categories)
