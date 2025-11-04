---
title: Ship-to Depot Delivery
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
> ❗️ The content in this article is only reserved for certain User accounts who use Ship-to Profiles

## Setup Non-working Days

* Navigate to **Organization > Organization** tab
* Click **Edit** :fa-pencil: icon of the **Branch**
* On the **Update Organization** form, navigate to **More Configuration > Holidays** sub-tab
* In this sub-tab, you can setup the Non-working Days
* First, you can setup the Saturday & Sunday to be Non-working Days by ticking their respective checkboxes
* You can also add the official public holidays of a country to the Non-working Days by clicking on **By Public Holidays** field and select the appropriate country from the drop-down list (Note: We currently only have public holiday data of Vietnam, not yet for other countries)
* Furthermore, you can add custom days to the Non-working Days. To do that, click **Add Holiday** button of the **By Custom Days** field. Each time you click this button, a new row will appear in the custom Non-working Day table below. You then need to fill in the information fields of the custom Non-working Days 

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Custom Non-working Day Information Field
      </th>

      <th>
        Description & Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Date Name
      </td>

      <td>
        **1. Description:**\
        A name assigned to the custom non-working day being created\
        **2. Input rules:**\
        Free-form input
      </td>
    </tr>

    <tr>
      <td>
        Date
      </td>

      <td>
        **1. Description:**\
        The specific date of the custom non-working day being created\
        **2. Input rules:**\
        Click on the calendar icon then select the appropriate date from the pop-out calendar. Alternatively, you can manually input in dd/mm/yyyy format
      </td>
    </tr>

    <tr>
      <td>
        Repeat Year
      </td>

      <td>
        **1. Description:**\
        Specify whether the custom non-working day being created will be repeated annually or not\
        **2. Input rules:**\
        If you wish to repeat the custom non-working day being created annually then tick the checkbox, otherwise leave it unticked
      </td>
    </tr>
  </tbody>
</Table>

* If you mistakenly add an incorrect custom non-working day, click the delete icon :fa-trash: under **Edit** column to remove that day

## Create Orders

## Route Plan Optimization Process

### Route Plan Optimization Process with Due Date

* The Due Date is the date on which the Order must be delivered, even if that date falls within the predefined Non-working Days
* For example: An Order has the Due Date attribute value to be ***04/25/2020***. This date is Saturday and has been defined earlier as a Non-working Day

- Despite that, on that date, the Order will still be delivered

### Route Plan Optimization Process without Due Date

* If an Order doesn’t have a Due Date, then the Order will be planned to be delivered during a Delivery Date Range. The Delivery Date Range is determined by the following formula:
* ***The Start date of the Delivery Date Range = Order Date***
* ***The End date of the Delivery Date Range = Order Date + Ship-to Expected Lead Time (Excluding Non-working Days)***
* For example:
* A Branch is configured to have the Non-working Days for all subordinate Depots to be: Saturday, Sunday and Vietnam official holidays

<Image title="DjkZMJdBwZ.png" alt={723} className="border" border={true} src="https://files.readme.io/d6c8ceb-DjkZMJdBwZ.png" />

* An Order has the Order Date to be ***04/27/2020*** and has no Due Date

- The respective Ship-to Profile of the Order has the Expected Lead Time to be ***D3 (Three days)***
- Supposedly, if there is no Non-working day, the End date of the Delivery Date Range should be ***04/27/2020 + 03 = 04/30/2020***
- However, 04/30/2020 is Vietnam Reunification Day, a Non-working Day, therefore the End Date of the Delivery Date Range will be moved forward one day to be ***04/30/2020 + 01 = 05/01/2020***
- 05/01/2020 is World Labor Day, a Non-working Day, therefore the End date of the Delivery Date Range will be moved forward one day to be ***05/01/2020 + 01 = 05/02/2020***
- 05/02/2020 is Saturday, a Non-working Day, therefore the End date of the Delivery Date Range will be moved forward one day to be ***05/02/2020 + 01 = 05/03/2020***
- 05/03/2020 is Saturday, a Non-working Day, therefore the End date of the Delivery Date Range will be moved forward one day to be ***05/03/2020 + 01 = 05/04/2020***
- 05/04/2020 is Monday, not a Non-working Day, therefore the End date of the Delivery Date Range will ultimately be set at this date
- The Delivery Date Range will be from 04/27/2020 to 05/04/2020, excluding the following dates: 04/30/2020, 05/01/2020, 05/02/2020, 05/03/2020
