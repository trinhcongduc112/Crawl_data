---
title: Customers' Non-working Days
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
* Customers may not work on certain days and will not receive delivered goods on those days. To inform the dispatchers, you could add the customers' non-working days in Abivin vRoute system.
* You could add information on Customers' non-working day by using either Webform or Excel Template

## Using Webform to add Customers' Non-working Day

* Step 1: Navigate to the **Partners > Customers** tab
* Step 2: Click the icon :fa-plus-circle: to create new customers. In case the customer information has already been available in the system, click the icon :fa-pencil: to the right of the Customer name.
* Step 3: The form names **Create Customer** pops up. In case you update the information of a customer, the form will name **Update Customer**
* Step 4: Click the tab **Other Settings**. On the left of the form, choose the tab **Non-working Days**

<Image title="Non-working Days (ENG).gif" alt={1900} border={true} src="https://files.readme.io/cc6d0b7-Non-working_Days_ENG.gif">
  Illustration (English)
</Image>

<Image title="Non-working Days (VIE).gif" alt={1900} border={true} src="https://files.readme.io/e3fb8e3-Non-working_Days_VIE.gif">
  Illustration (Vietnamese)
</Image>

Here in the form, there are three fields to add information on customers' non-working days.

* Step 5: Click on the drop-down list to the right of the line **By Week**. The drop-down menu will show all weekdays and the weekend. You can tick more than one day on the list.

<Image title="1. By Week (ENG).png" alt={1198} border={true} src="https://files.readme.io/16cf245-1._By_Week_ENG.png">
  Illustration (English)
</Image>

<Image title="1. By Week (VIE).png" alt={1193} border={true} src="https://files.readme.io/e518a30-1._By_Week_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 6: Click on the drop-down list to the right of the line **By Public Holidays**. The drop-down menu will show the country name. Just choose the country name in the list; the system will automatically update the public holiday based on the country name you choose.

<Image title="1. By Public Holidays (ENG).png" alt={1198} src="https://files.readme.io/89098f2-1._By_Public_Holidays_ENG.png">
  Illustration (English)
</Image>

<Image title="2. By Public Holiday (VIE).png" alt={1193} border={true} src="https://files.readme.io/9e1eb4c-2._By_Public_Holiday_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 7: If non-working days of a customer last only a few specific days, you could manually select the day by clicking the button **Add Custom Days** to the right of the line **Custom Days**

- Enter the name of non-working days in the field **Date Name**. This field cannot be left blank.
- Click the **Date Range**, then choose the Start Date and End Date of the non-working period in the calendar given.
- If the non-working period above is the same every year, click the button **Repeat Year**. If not, you could skip this button.

* Step 8: Click **Save** for information to be integrated into the system.\
  In case you want to delete the information of the non-working days that has just been entered, click the icon :fa-trash:\
  In case you want to stop adding information about non-working days, click the button **Cancel**

<Image title="Custom Day (VIE) (White 2).gif" alt={1900} src="https://files.readme.io/9668047-Custom_Day_VIE_White_2.gif">
  Illustration (Vietnamese)
</Image>

## Using Excel template to add Customers' Non-working Day

* Step 1: Navigate and click the tab **Partners** 
* Step 2: Click the icon :fa-plus-circle: On the drop-down list, click on the button **Import Data**
* Step 3: A form named **Upload Data** pops up on the screen. Click the line **Non-working Days** 

<Image title="Non-working Day.png" alt={743} border={true} src="https://files.readme.io/67c45d9-Non-working_Day.png">
  Illustration (English)
</Image>

<Image title="Non-working Day (VIE).png" alt={739} border={true} src="https://files.readme.io/0058f3e-Non-working_Day_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 4: Click the line **Overwrite Existing Records** if you want to erase all previous data and enter brand new data based on the Customer Code in the new file.\
  Click the line **Skip Existing Records** if you want to keep the previous data intact and supplement new data based on the Customer Code in the new file.

<Image title="Overwrite (ENG).png" alt={749} border={true} src="https://files.readme.io/3d1b9e4-Overwrite_ENG.png">
  Illustration (English)
</Image>

<Image title="Overwrite (VIE).png" alt={739} border={true} src="https://files.readme.io/8c0a930-Overwrite_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 5: Click the button **Download Sample**. An Excel template named *Import\_Partner\_Non-workingDay\_Template* will be downloaded to your computer.

<Image title="download (ENG).png" alt={749} src="https://files.readme.io/7a017bb-download_ENG.png">
  Illustration (English)
</Image>

<Image title="download (VIE).png" alt={742} border={true} src="https://files.readme.io/640958d-download_VIE.png">
  Illustration (Vietnamese)
</Image>

* Step 6: Open the Excel Template. You should fill in the information as follows

<Image title="1. Template (ENG 2).png" alt={1707} src="https://files.readme.io/e0b2f68-1._Template_ENG_2.png">
  Non-Working Days Excel Template (English)
</Image>

<Image title="1. Template (VIE).png" alt={1705} src="https://files.readme.io/b7157e4-1._Template_VIE.png">
  Non-Working Days Excel Template (Vietnamese)
</Image>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Customer Code
        (Required Field)
      </td>

      <td>
        **1. Description:**\
        Enter the management code of the customer whose non-working days you want to add or update.

        **2. Input rules:**\
        You could find the Customer Code on the web app in the tab **Partners > Customers** then copy and paste into this cell.
      </td>
    </tr>

    <tr>
      <td>
        Organization Code\
        (Required Field)
      </td>

      <td>
        **1. Description:**\
        Enter the organization code of the Depot whose non-working days you want to add or update.

        **2. Input rules:**\
        You could find the Organization Code on the web app in the tab **Organizations > Organizations** then copy and paste into this cell.
      </td>
    </tr>

    <tr>
      <td>
        Mon - Sun\
        (Days in a week) (Optional)
      </td>

      <td>
        **1. Description:**\
        These 7 cells represent non-working days within a week. 

        **2. Input rules:**\
        You could tick **T** in more than one column. You could either tick these cells or leave these cells blank.
      </td>
    </tr>

    <tr>
      <td>
        Public Holiday\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Fill in this field if the non-working days are public holidays. You could fill this cell or leave this cell blank.

        **2. Input rules:**\
        This field can be either left blank or filled with one of the country names as below

        * Indonesia
        * Myanmar
        * Vietnam

        Example:\
        If the customer/organization whose non-working days need updating is in Indonesia, enter "Indonesia" in this cell, or else you could leave this cell blank.
      </td>
    </tr>

    <tr>
      <td>
        Custom day-Name\
        (Required Field)
      </td>

      <td>
        **1. Description:**\
        Enter the name of the non-working days. 

        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        Custom day-Start Date\
        Custom day-End Date\
        (Required Fields)
      </td>

      <td>
        **1. Description:**

        * Enter the start date of the non-working day in the field **Custom day-Start Date**
        * Enter the end date of the non-working day in the field **Custom day-End Date**

        **2. Input rules:**

        * Input format: Date/Month/Year (dd/mm/yyyy)

        Example:\
        Your customer has a non-working period lasts from 9 December 2020 to 15 December 2020, 

        * Enter 09/12/2020 in the field **Custom day-Start Date**
        * Enter 15/12/2020 in the field **Custom day-End Date**
      </td>
    </tr>

    <tr>
      <td>
        Custom day-Repeat Year\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        This field will set the non-working days repetitive.

        **2. Input rules:**\
        If the non-working days happen every other year, enter the letter **T**.\
        If the non-working days are temporary, enter the letter **F**.\
        If you leave this cell blank, the non-working days will not be repeated
      </td>
    </tr>
  </tbody>
</Table>

* Step 7: Save the Excel File with information, then drag the file to the box **Drop import file here or click to upload**. The file information will be automatically uploaded and stored in the system database.

## Impact of Non-Working Days setting on Orders with ETA/ETD

## Orders with ETA or ETD partially coincides with non-working period at a delivery stop

Example:\
You create an order with ETA set at 14 Jan 2021 and ETD set at 15 Jan 2021

<Image title="ETA (1).png" alt={1588} border={true} src="https://files.readme.io/02dfe85-ETA_1.png">
  ETA & ETD Date Example (English)
</Image>

The customer delivery stop has a non-working day on 15 Jan 2021  and 16 Jan 2021

<Image title="Non-working Days Example.png" alt={1193} border={true} src="https://files.readme.io/dee4ccd-Non-working_Days_Example.png">
  Non-working Day Example (English)
</Image>

The Order Confirmation will automatically set the ETD Date one day earlier, which is on 14 Jan 2021 instead of on 15 Jan as initially set, to avoid the non-working day period in the customers' delivery stop

<Image title="ETD Date.png" alt={1920} className="border" border={true} src="https://files.readme.io/3277eed-ETD_Date.png" />

## Orders with ETA & ETD Date completely coincide with the Non-working Day period at a delivery stop

Example:\
You create an order that has ETA and ETD Date set on 15 Jan 2021 and 16 Jan 2021 respectively

<Image title="Coincide 1.png" alt={1593} className="border" border={true} src="https://files.readme.io/260c27b-Coincide_1.png" />

The customer delivery stop also has a non-working day on 15 Jan 2021  and 16 Jan 2021.

<Image title="Non-working Days Example.png" alt={1193} className="border" border={true} src="https://files.readme.io/82df1c7-Non-working_Days_Example.png" />

Because the ETD & ETA Date of the Order coincides with the Non-working period in the customers' delivery stop, which means the order could not be delivered on the day you want to set, the system will send you a notification as below.

<Image title="confirmation 2.png" alt={743} className="border" border={true} src="https://files.readme.io/4946667-confirmation_2.png" />

If you click **Confirm**, the system will take the order as an exception and still deliver the order on the day that you specified.\
If you click **Delete the order(s)**, the order will be deleted, and you may have to create a new order with ETA & ETD Date different from the non-working day period at customers' delivery stop.
