---
title: Customer Non-working Days
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
> 🚧 At the moment, this feature only works with the Open Delivery Routes

* It is unlikely of your Customers to work every single day throughout the year. They will probably have some days off not working, which could either be weekend days, national public holidays, or random days that they actively schedule on their own. Those days are called **Customer Non-working Days**. On Customer Non-working Days, the Customers will stop receiving any deliveries until they resume working. As the Route Planner, you have to make sure the Non-working Days of each Customer have been taken into account during the Route Plan optimization process
* This article will show you how to set up and use the Customer Non-working Days during the Route Plan optimization process on the Abivin vRoute system

## Create Customer Non-working Days

* You can create the Customer Non-working Days using two methods: The Webform and the Excel import file

### Create Customer Non-working Days Using The Webform

* To create the Non-working Days of a particular Customer using the Webform, follow the steps below
* Open the creation/editing Webform of the desired Customer
* On the Webform, navigate to the **Other Settings > Non-working Days** section
* Here you will see three sub-sections: **By Week; By Public Holidays; Custom Days**. These sub-sections allow you to set up the Non-working Days of the Customer being created/edited by weekdays, by national public holidays, and by custom day ranges

<Image title="czc2IfNlOC.png" alt={955} border={true} src="https://files.readme.io/445c235-czc2IfNlOC.png">
  Illustration (English)
</Image>

<Image title="F8dJz7FGLD.png" alt={951} border={true} src="https://files.readme.io/2d34770-F8dJz7FGLD.png">
  Illustration (Vietnamese)
</Image>

#### Create Customer Non-working Days By Weekdays Using The Webform

* To create the Customer Non-working Days by weekdays, click on the **Non-working Days** field. A drop-down list will appear showing the days in a week. Tick the checkboxes of the weekdays that you want to mark as the Non-working Days of the Customer
* For example, if you tick the Monday, Thursday, and Sunday checkboxes, that means the Customer will not be working every Monday, Thursday, and Sunday throughout the year

<Image title="ZYSkY4UPSU.png" alt={755} border={true} src="https://files.readme.io/d3632ec-ZYSkY4UPSU.png">
  Illustration (English)
</Image>

<Image title="fR3OYOSgTs.png" alt={755} border={true} src="https://files.readme.io/07c0ba4-fR3OYOSgTs.png">
  Illustration (Vietnamese)
</Image>

#### Create Customer Non-working Days By National Public Holidays Using The Webform

* To create the Customer Non-working Days by National Public Holidays, click on the **Country** field. A drop-down list will appear showing the list of supported countries. Click on the appropriate country

<Image title="1xomZT4WuR.png" alt={751} border={true} src="https://files.readme.io/1358199-1xomZT4WuR.png">
  Illustration (English)
</Image>

<Image title="GQdxl05ePb.png" alt={760} border={true} src="https://files.readme.io/bcb8d5a-GQdxl05ePb.png">
  Illustration (Vietnamese)
</Image>

#### Create Customer Non-working Days By Custom Day Ranges Using The Webform

* To create the Customer Non-working Days by custom day ranges, follow the steps below:
* Step 1: Click the **Add Custom Day** button. Upon clicking, a row will appear in the **Custom Days** table below

<Image title="C6VBqJWGfr.png" alt={771} border={true} src="https://files.readme.io/b8b3e31-C6VBqJWGfr.png">
  Illustration (English)
</Image>

<Image title="eVgo0aj63L.png" alt={771} border={true} src="https://files.readme.io/3c6d64d-eVgo0aj63L.png">
  Illustration (Vietnamese)
</Image>

* Step 2: Input the name of the custom Non-working Day range into the input field under the **Date Name** column. The date name value can consist of letters, numbers, special characters, and spaces
* Step 3: Click on the calendar icon :fa-calendar-o: under the **Date Range** column. On the drop-down calendar, select the appropriate day range then click **Apply**
* Step 4: If you wish to repeat this custom Non-working Day range on a yearly basis, click on the toggle button :fa-toggle-off: under the **Repeat Year** column. When the toggle button changes to :fa-toggle-on:, that means the day range will be repeated on a yearly basis
* Below is an example of a custom Non-working Day range, which has the name ***Custom Day 1***, starts on ***11/06/2021***, ends on ***14/06/2021***, and is repeated on a yearly basis

<Image title="YwqZ8MlDp0.png" alt={743} border={true} src="https://files.readme.io/670821a-YwqZ8MlDp0.png">
  Illustration (English)
</Image>

<Image title="qLlsgi8rgF.png" alt={739} border={true} src="https://files.readme.io/1cfa918-qLlsgi8rgF.png">
  Illustration (Vietnamese)
</Image>

* To add more Custom Day ranges, repeat the steps above
* If you mistakenly add an unwanted custom Non-working Day range, you can remove that range by clicking its respective **Remove** icon :fa-trash: under the **Edit** column

### Create Customer Non-working Days Using The Excel Import File

* To create the Customer Non-working Days using the Excel import file, follow the steps below
* Step 1: On the **Partners > Customers** tab, hover over the orange plus-circle icon :fa-plus-circle: then click the **Import Data** :fa-long-arrow-up: icon
* Step 2: The **Upload Data** form will appear. On this form, tick the **Non-working Days** radio box (Important) then click on the **Download Sample** area to save the Customer Non-working Day Excel import file, ***Import\_Partner\_Non-workingDay\_Template.xlsx***, to your computer

<Image title="QYaeGacuNg.png" alt={591} border={true} src="https://files.readme.io/965355d-QYaeGacuNg.png">
  Illustration (English)
</Image>

<Image title="BK8E3m8ihY.png" alt={588} border={true} src="https://files.readme.io/3c110be-BK8E3m8ihY.png">
  Illustration (Vietnamese)
</Image>

* Step 3: Open the file and input the Non-working Days of the Customers
* Below are the information fields in the Excel file and the input rules for each filed

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Description & Input Rules
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        "Customer Code"
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Customer Code of the Customer for which the Non-working Days being input will apply\
        **2. Input rules:**\
        Copy the Customer Code of the desired Customer on the Web app then paste it into this cell\
        The Customer Code can be found under the column with the same title in the "Partners > Customers" tab
      </td>
    </tr>

    <tr>
      <td>
        "Organization Code"\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The Organization Code of the Depot which directly manages the Customer for which the Non-working Days being input will apply\
        **2. Input rules:**\
        Copy the Organization Code of the desired Depot on the Web app then paste it into this cell\
        The Organization Code can be found under the column with the same title in the "Organizations > Organizations" tab
      </td>
    </tr>

    <tr>
      <td>
        "Weekdays (Including Mon; Tue; Wed; Thu; Fri; Sat; Sun cells)"\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        List of the weekdays. You can specify which weekdays will be the Non-working Days of the Customer\
        **2. Input rules:**\
        If a weekday is a Non-working Day, input the following value into that weekday cell: ***T***\
        If the weekday is not a Non-working day, leave its cell blank
      </td>
    </tr>

    <tr>
      <td>
        "Public Holiday"\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        This cell lets the user specify the country in which the national public holidays are followed by the Customer\
        Note: At the moment, the Abivin vRoute system only has the national public holiday data of Vietnam, not yet for other countries\
        **2. Input rules:**\
        If the Customer follows Vietnam national public holidays, input the following value into this cell (Note: The value is case-sensitive, you must input the exact value in upper-case and lower-case letters): ***Vietnam***\
        If the Customer doesn't follow Vietnam national public holidays, leave this cell blank
      </td>
    </tr>

    <tr>
      <td>
        "Custom day-Name"\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Name of the non-working day range that the Customer schedules on their own\
        **2. Input rules:**\
        Format: Free-format input (Text, numbers, special characters, and spaces are all accepted)
      </td>
    </tr>

    <tr>
      <td>
        "Custom day-Start Date"\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        This cell specifies the date on which the custom non-working day range starts\
        **2. Input rules:**\
        Format: ***Date/Month/Year dd/mm/yyyy***\
        For example, ***30/04/2020***\
        Note:\
        You need to format the cell in Text format before inputting the value to preserve the date value exactly in the above format. If you don't do this, the value in this cell might be affected by the date format setting of your computer
      </td>
    </tr>

    <tr>
      <td>
        "Custom day-End Date"\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        This cell specifies the date on which the custom non-working day range ends\
        **2. Input rules:**\
        Format: ***Date/Month/Year dd/mm/yyyy***\
        For example, ***30/05/2020***\
        Note:\
        You need to format the cell in Text format before inputting the value to preserve the date value exactly in the above format. If you don't do this, the value in this cell might be affected by the date format setting of your computer
      </td>
    </tr>

    <tr>
      <td>
        "Custom day-Repeat Year"\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        This cell specifies whether the custom non-working days range will repeat on a yearly basis or not\
        **2. Input rules:**\
        If the custom non-working days range will repeat on a yearly basis, input the following value into this cell (Note: The value is case-sensitive, you must input the exact value in upper-case and lower-case letters): ***T***\
        If the custom non-working days range will not repeat on a yearly basis, input the following value into this cell (Note: The value is case-sensitive, you must input the exact value in upper-case and lower-case letters): ***F***
      </td>
    </tr>
  </tbody>
</Table>

* **Important**: If the Customer schedules more than one custom non-working day range, you need to place each custom non-working day range on a separate row. Furthermore, you need to copy and paste other common information of that Customer (**Customer Code; Organization Code; Weekdays; Public Holiday** cells) across all rows of all custom Non-working Day ranges
* Here is a sample data set to illustrate how you should input into the Excel file:
* A Customer, ***Customer\_01***, directly managed by the Depot ***Depot\_01***, will not work every Thursday, Saturday, and Sunday. That Customer will also not work on every public holiday in Vietnam. That Customer also schedules two non-working day ranges, the first one from April 20th, 2021 to May 02nd, 2021, the second one from July 04th, 2021 to July 08th, 2021. Only the second non-working day range will repeat on a yearly basis
* For this Customer, you will need to input the data in the Excel file as follows:
* 1 - Input the Customer Code of that Customer into the **Customer Code** cell. Input the Organization Code of that Customer's managing Depot into the **Organization Code** cell
* 2 - Input the value ***T*** into the ***Thu; Sat; Sun*** cells to specify that the Customer will not work on Thursday, Saturday, and Sunday
* 3 - Input the value ***Vietnam*** into the **Public Holiday** cell to specify that the Customer will follow the national public holidays of Vietnam
* 4 - Input the name of the Customer's first custom non-working day range into the **Custom day-Name** cell. For this example, I will go with the value ***First custom range***. Next, input the start date of the Customer's first custom non-working day range, ***20/04/2021***, into the **Custom day-Start Date** cell. Continue to input the end date of the Customer's first custom non-working day range, ***02/05/2021***, into the **Custom day-End Date** cell
* 5 - Move on to the next row in the Excel file, right under the row of the first custom non-working day range of the Customer. On this row, input the name of the Customer's second custom non-working day range into the **Custom day-Name** cell. I will go with the value ***Second custom range***. Next, input the start date of the Customer's second custom non-working day range, ***04/07/2021***, into the **Custom day-Start Date** cell. Continue to input the end date of the Customer's second custom non-working day range, ***08/07/2021***, into the **Custom day-End Date** cell
* 6 - Copy the values from the following cells of the Customer's first custom non-working day range row: **Customer Code; Organization Code; Weekdays (Which are the Thu; Sat; Sun cells); Public Holiday**. Paste the copied values into the corresponding cells on the Customer's second custom non-working day range row
* That's it. Here is how the file should look now

<Image title="RUcbwIS4Di.png" alt={1008} border={true} src="https://files.readme.io/db0de93-RUcbwIS4Di.png">
  Illustration (English)
</Image>

<Image title="sMaKm4YmJh.png" alt={1056} border={true} src="https://files.readme.io/f73f84b-sMaKm4YmJh.png">
  Illustration (Vietnamese)
</Image>

* Step 4: After you have input the necessary information and saved the Excel file, you can now import that file onto the system
* Here there are two scenarios: 1. The Customers in the Excel file have not had any Non-working Days on the Web app, and 2. The Customers in the Excel file have already had Non-working Days on the Web app
* Scenario 1. The Excel file contains the Non-working Day data of Customers who have not had any Non-working Days on the Web app, you can simply just import the file as usual. Make sure that on the **Upload Data** form, the **Non-working Days** radio box is still ticked. It doesn't matter which of the **Overwrite Existing Records** and **Skip Existing Records** radio boxes is ticked

<Image title="vqkiNyPB3b.png" alt={587} border={true} src="https://files.readme.io/19357ae-vqkiNyPB3b.png">
  Illustration (English)
</Image>

<Image title="paqp6XPs2I.png" alt={592} border={true} src="https://files.readme.io/378f95a-paqp6XPs2I.png">
  Illustration (Vietnamese)
</Image>

* Scenario 2. The Excel file contains the Non-working Day data of Customers who have already had the Non-working Days on the Web app. In this scenario, you need to decide whether to keep the existing Non-working Days of those Customers and only add the new Non-working Days or completely remove the existing Non-working Days and replace them with the new Non-working Day data in the file
* If you wish to keep the existing Non-working Days of the Customers and create additional Non-working Day data, then on the **Upload Data** form, make sure you tick the **Skip Existing Records** radio box before importing the file

<Image title="Hdya2gMZ0z.png" alt={589} border={true} src="https://files.readme.io/6237b04-Hdya2gMZ0z.png">
  Illustration (English)
</Image>

<Image title="xY1f0eoI7F.png" alt={594} border={true} src="https://files.readme.io/aef92fa-xY1f0eoI7F.png">
  Illustration (Vietnamese)
</Image>

* If you wish to replace all the existing Non-working Days of the Customers with the new data in the file, then on the **Upload Data** form, make sure you tick the **Overwrite Existing Records** radio box before importing the file

<Image title="AjCPUh4Vp9.png" alt={592} border={true} src="https://files.readme.io/c6fbbdd-AjCPUh4Vp9.png">
  Illustration (English)
</Image>

<Image title="w9z9Q97pE4.png" alt={589} border={true} src="https://files.readme.io/4f872cb-w9z9Q97pE4.png">
  Illustration (Vietnamese)
</Image>

## Export Customer Non-working Days

* You can export the Customer Non-working Days into the Excel file. The Import and Export files have the same data columns, therefore you can conveniently edit the Export file then import the edited file back to the system, which can save time if you need to edit the Non-working Days of many Customers at once
* To export the Non-working Day data of some particular Customers, follow the steps below:
* Step 1: On the Customer list, tick the checkboxes of the desired Customers to select them
* Step 2: Hover your mouse over the orange plus-circle icon :fa-plus-circle:, then click the **Export Data** icon :fa-long-arrow-down:
* On the **Export Data** form, click the **Export Non-working Days** box, then click the **Export** button

<Image title="y1Tu6475AD.png" alt={464} border={true} src="https://files.readme.io/21d9523-y1Tu6475AD.png">
  Illustration (English)
</Image>

<Image title="cIAc3CKChM.png" alt={464} border={true} src="https://files.readme.io/e98367d-cIAc3CKChM.png">
  Illustration (Vietnamese)
</Image>

* The Non-working Day data of the selected Customers will be exported to the Excel file
