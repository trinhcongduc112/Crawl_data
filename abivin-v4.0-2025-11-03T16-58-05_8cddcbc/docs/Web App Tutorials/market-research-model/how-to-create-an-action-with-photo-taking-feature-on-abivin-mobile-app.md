---
title: Form Builder - Create a Photo-taking form
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
Many customers of ours require the Abivin Mobile app to have function to take photos, so that the mobile users can perform related tasks. Using the built in Form Builder tool, we could create a function with this feature on Abivin Mobile app.

* Navigate to **Tasks > Action List** tab
* The list of all actions that you have created will be presented there.
* On the rows of the actions that require taking photos, click on the gear icon that reads **Form Builder**. We will be directed to the Form Builder tool. 

- On the Form builder page, click **Special components** to reveal the sub menu.
- Click and drag the **File** field onto the white area on the right, below the orange bar. This **File** field is the photo taking feature on Abivin vRoute Mobile app.
- A **File component** field will automatically appear. Now you can create the function to take photos.
- First, on **Display** tab.
- In the **Label** field, write a name that will represent the photo function on Abivin vRoute Mobile app. For example, I will name this task **Take photos**
- Next, click on **API** tab.
- In the **Property Name** field, write **hinhAnh1**. This string will let Abivin server know that this function is for taking photos.
- Next, click on **Custom Properties**.
- In the **Key** field, write **distanceFilter**. The string will let Abivin server know that this function is for creating distance constraint.
- In the **Value** field, write the radius you constraint required for this task. For example, if you write **500**, this will let the server know that the mobile user will only be able to perform this task within the radius of 500 meters from the required location.
- Click **Save**, then scroll to the bottom of the page and click **Save View**. The mobile form for this action has been successfully created. It will now be present on the Abivin vRoute mobile app of the user.

<Image title="Form builder take photos.gif" alt={1197} className="border" border={true} src="https://files.readme.io/153803e-Form_builder_take_photos.gif" />
