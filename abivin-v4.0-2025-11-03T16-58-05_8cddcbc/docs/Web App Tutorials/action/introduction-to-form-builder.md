---
title: Introduction to Form Builder
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
* An Action after being created is just like an empty container, having nothing inside. The Mobile users will still not be able to perform anything
* On Web app, you would have to integrate *Forms* into the actions, to make them *actionable* on Mobile app
* In Abivin vRoute, we have equipped a very powerful Form builder tool, enabling our clients to quickly create just about any web form they want, in order to cover all the physical tasks of the drivers or sales staffs just on one Mobile screen
* Below are the basic steps to integrate forms into the actions
* **Step 1**. Navigate to **Tasks > Action List** tab
* **Step 2**. Click on **Form Builder** :fa-cog: icon of the selected action to get to the **Form Builder** setup screen

<Image title="Open form builder.gif" alt={1668} className="border" border={true} src="https://files.readme.io/a4b599f-Open_form_builder.gif" />

* **Step 3**. Remove the blue **Submit** button by hovering your mouse over that button, then click on the red :fa-times: icon

<Image title="form builder delete submit button.gif" alt={1668} className="border" border={true} src="https://files.readme.io/46474b3-form_builder_delete_submit_button.gif" />

* **Step 4**. Click on either of these three sections: **Basic Components**, **Special Components** or **Layout Components** on the left column to find the suitable component, then click and drag the component to the right side of the screen, then release the mouse
* The setup form of the component will show up. Each setup form has several tab: **Display, Validation, API** etc. Input relevant information of the component in this setup form
* You can use multiple components to build the form of an action. The way you arrange the components will be how they will be displayed on the Mobile app
* Most of the components can be arranged next to, above or below other components. There are several components such as **Panel**, **Table** (Under **Layout Components** section) or **Container** (Under **Special Components** section) that allows you to click and drag other components ***inside*** them
* After you have input all necessary information in the component setup form, click on the green **Save** button to finish configuring that component

<Image title="drag form.gif" alt={1668} className="border" border={true} src="https://files.readme.io/98b7841-drag_form.gif" />

* **Step 5**. Scroll down to the **View form design** area to view an illustration of the form you have just set up. This is how the form will appear on the Mobile app

<Image title="2019-09-03 17_59_30-Window.png" alt={1064} src="https://files.readme.io/c513db0-2019-09-03_17_59_30-Window.png">
  Example of a form
</Image>

* **Step 6**. If you feels that the form is good enough, click on the green **Save view** button to finish setting up the form for the action

> ❗️ This step is very important! If you forget to do this, you will lose every configurations you have just setup

<Image title="Save view form builder.gif" alt={1668} className="border" border={true} src="https://files.readme.io/d4ab5c7-Save_view_form_builder.gif" />

* Your form is now successfully integrated into the Action. The drivers/sales staffs can now perform the action on their Mobile apps
* Due to the vast configuration options and specific requirements of the forms, we will have a series of article to guide you on how to create forms for each model or specific tasks
