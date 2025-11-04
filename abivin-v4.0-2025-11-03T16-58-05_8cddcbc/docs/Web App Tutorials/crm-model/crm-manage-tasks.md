---
title: Manage Tasks
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
## Locate Task List

* The tasks are listed on **Tasks > Tasks** tab

## Create Tasks

* You have two methods to create tasks: Web form and Excel template

## Create Tasks using Web form

* Hover over the :fa-plus-circle: icon, then click **Create**. The **Tasks action information** screen will appear
* Click on **Customer** field. Select the appropriate Customer from the dropdown list. You can also input the Customer Code/Full Name/Mobile Number attributes of the desired Customer into the search bar to filter faster
* If the Customer of the task being created is totally new, not yet available in the database, you can create that Customer right on this screen by clicking on the blue plus icon :fa-plus-square: then create the customer on the pop-out **Contact Information** form. On this form, you only need to input into the information fields that end with asterisks
* Always leave the **Assign Type** field value as ***Users*** (In this model, each staff has different tasks, unlike Retail Operation Model)
* Click on **Assigned To** field. On the search bar, select the staff to whom you want to assign the task being created. If the wanted staff is not present, you can input the Username/Full Name/Email/Phone Number attribute of that staff into the search bar to filter out that staff
* Click on **Actions** field. Select the appropriate task from the dropdown list
* After selecting the action, the **Products** and **Serial** fields will appear (The Serial field will not appear if the selected action is ***Lắp đặt*** because, with this action, the product is to be installed for the very first time so the product serial has not been retrieved yet)
* Click on **Product** field. Select the appropriate product from the dropdown list. You can also input the Product Name/Product Code of the wanted product into the search bar to filter out faster
* Click on **Serial** field. Select the appropriate serial of the selected product from the dropdown list
* Click on the calendar icon :fa-calendar: of the **Start Date** field. Select the start of the date range during which the task can be performed. Similarly, click on the calendar icon :fa-calendar: of the **End Date** field. Select the start of the date range during which the task can be performed

## Search & Filter Tasks

### Filter Tasks

* Click on the Filter icon on the top right corner of the task list (It looks similar to the wifi symbol :fa-wifi:) to open the filter table

<Image title="123123123.png" alt={1920} className="border" border={true} src="https://files.readme.io/8535739-123123123.png" />

* On the filter table, choose the appropriate attribute from the drop-down menu: **Task Status; Completed Time; Created At; Start Date; Due Date; Customer; Assign To; Organizations; Actions**

<Image title="2.png" alt={655} className="border" border={true} src="https://files.readme.io/aa60a4a-2.png" />

* You could add more attributes to the filter by clicking the **Add Filter** :fa-plus: button
* After choosing the attributes, you need to specify the attribute value by which the tasks will be filtered, details below:
* 1 - With date-type attributes (Completed Time; Created At; Start Date; Due Date), you need to click on the calendar icon :fa-calendar:, then select the appropriate date range from the drop-down calendars

<Image title="GHHLthBoui.png" alt={566} className="border" border={true} src="https://files.readme.io/bc275a1-GHHLthBoui.png" />

* 2 - With string-type attributes (Organization; Customer; Task Status; Assign To; Actions), you need to click on the caret down icon :fa-caret-down:. A dropdown list will appear. On this list, tick the checkbox of the desired value. You could tick multiple checkboxes

<Image title="HJcJQCWa6L.png" alt={566} className="border" border={true} src="https://files.readme.io/83444e0-HJcJQCWa6L.png" />

* Note that if an attribute has too many values, the dropdown list will only show several sample values. If the value you want to search is not present on the list, you could enter certain information related to that value into the search bar to filter faster. Below is the list of searchable information for each attribute

<Embed url="https://www.youtube.com/watch?v=YSiGMM3m9MU&feature=youtu.be" title="Search Task Attribute by Value" favicon="https://www.youtube.com/s/desktop/dc82f5e2/img/favicon.ico" image="https://i.ytimg.com/vi/YSiGMM3m9MU/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=YSiGMM3m9MU&feature=youtu.be" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FYSiGMM3m9MU%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DYSiGMM3m9MU%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FYSiGMM3m9MU%252Fhqdefault.jpg%26key%3Df2aa6fc3595946d0afc3d76cbbd25dc3%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22640%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

#### Appendix: Searchable Information by Attribute

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Task Attribute
      </th>

      <th>
        Searchable Information
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Customer
      </td>

      <td>
        Customer Code\
        Full Name\
        Mobile Number\
        Home Number\
        Street Address\
        Address\
        Town\
        District\
        Province/City\
        Serial Number\
        Email
      </td>
    </tr>

    <tr>
      <td>
        Assign To
      </td>

      <td>
        Username\
        Phone Number\
        Full Name\
        Email
      </td>
    </tr>

    <tr>
      <td>
        Organizations
      </td>

      <td>
        Organization Code\
        Organization Name
      </td>
    </tr>

    <tr>
      <td>
        Action
      </td>

      <td>
        Action Code\
        Action Name
      </td>
    </tr>
  </tbody>
</Table>

* To add another filter to the tasks, click on **Add Filter** and repeat the same steps above

<Image title="4.png" alt={573} className="border" border={true} src="https://files.readme.io/d11a97c-4.png" />

* If you accidentally added an unwanted filter, click the respective remove icon :fa-remove: at the end of the filter

<Image title="ApS6KoVIu1.png" alt={558} className="border" border={true} src="https://files.readme.io/457c5e7-ApS6KoVIu1.png" />

* After you have created the filters, click **Apply** to save the information
* The task list will automatically refresh and display the tasks that meet your filters
