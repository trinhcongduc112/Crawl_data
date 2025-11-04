---
title: Audit Log
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
* Audit Log is a set of records related to the tasks performed on the web app including **Create, Update, Import, Export, Delete**. Accurately, any action related to these tasks will be recorded and put into this Audit Log with detailed information
* This tab will record the events happening to the following resources: **Customer; Customer Group; Vehicle; Order; Route Plan**

> ❗️ This feature is currently only developed to use in conjunction with the [**Route Plan (List View)**](https://docs.abivin.com/docs/vrp-in-house-fleet-route-plan-list-view), not yet available for the Route Plan (Map View)

* Navigate to **Settings > Audit Log** tab
* In this tab, the log will be recorded with detailed information related to the actions performed

<Image title="Audit Log (English).png" alt={1898} border={true} src="https://files.readme.io/fa354ca-Audit_Log_English.png">
  Illustration (English)
</Image>

<Image title="Audit log 1.png" alt={1901} border={true} src="https://files.readme.io/60518d0-Audit_log_1.png">
  Illustration (Vietnamese)
</Image>

* Below is the interface of the audit log

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Column Title
      </th>

      <th>
        Column Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Log Time
      </td>

      <td>
        Time stamp of the event
      </td>
    </tr>

    <tr>
      <td>
        Operated By
      </td>

      <td>
        Specify the personnel who performed the event
      </td>
    </tr>

    <tr>
      <td>
        Log Operation
      </td>

      <td>
        Specify the operation being logged\
        Below is the list of operations that will be logged:

        * \*Create\*\*: Created Order Code
        * \*Delete\*\*: Deleted Order Code
        * \*Export\*\*: Export File
        * \*Import\*\*: Import File
        * \*Optimized\*\*: The Route Plan is optimized
        * \*Locked\*\*: The Route Plan is locked
        * \*Unlocked\*\*: The Route Plan is unlocked
        * \*Finalized\*\*: The Route Plan is finalized
        * \*Synced\*\*: The Route Plan is synchronized to the external Transportation Management System
        * \*Updated\*\*: Updated Information
        * \*Completed\*\*: Completed 
        * \*Deleted\*\*: Deleted Order Code
        * \*Missing Order Moved To Route\*\*: The Missing Order is moved into the Route Plan
        * \*Stop Moved From Route To Route\*\*: The Stop is moved into the Route Plan
        * \*Order Moved From Route To Route\*\*: The Order is moved within Route Plan
        * \*Coordinate Updated\*\*: The Stop's coordinate information is updated
        * \*Order Removed From Route\*\*: The Order is removed from the Route Plan
        * \*Stop Removed From Route\*\*: The Stop is removed from the Route Plan
      </td>
    </tr>

    <tr>
      <td>
        Component
      </td>

      <td>
        Specify the component being logged\
        Below is the list of components:\
        Web App\
        Mobile
      </td>
    </tr>

    <tr>
      <td>
        Module
      </td>

      <td>
        Specify the module being logged\
        Below is the list of modules:\
        Order\
        Partner\
        Vehicle\
        Planning
      </td>
    </tr>

    <tr>
      <td>
        Resource
      </td>

      <td>
        Specify the resources being logged\
        Below is the list of resources:\
        Sale Order\
        Customer\
        Customer Group\
        Vehicle\
        Route Plan
      </td>
    </tr>

    <tr>
      <td>
        Resource Code
      </td>

      <td>
        Management code of the resources being logged
      </td>
    </tr>

    <tr>
      <td>
        Log Detail
      </td>

      <td>
        Detail of the event being logged
      </td>
    </tr>
  </tbody>
</Table>

* This is an example of the log recorded:
* The first image is the action of ETD date, Delivery date and Due date change from 2020-08-19 to 2020-08-20 **(Order Code SO-200819-0002)** 

<Image title="1.png" alt={1920} className="border" border={true} src="https://files.readme.io/3da874c-1.png" />

* This image is the log recorded in the Audit Log related to the date change of **Order Code SO-200819-0002** 

<Image title="A.png" alt={1920} className="border" border={true} src="https://files.readme.io/2cb9af7-A.png" />

* If the log is too long, it will be shortened. To view the log detail, click the text **Show More**, the form **Information** will appear

<Image title="AZ3HNbsBB2.png" alt={491} className="border" border={true} src="https://files.readme.io/5a62347-AZ3HNbsBB2.png" />

## Search, Filter, Sort

<Image title="Log Att.png" alt={1920} className="border" border={true} src="https://files.readme.io/5cf31c6-Log_Att.png" />

* To search for all events happening during a specific date range, click the calendar icon :fa-calendar:\
  to the right side of the line **Log Time** then select the desired date range from the drop-down calendars. Note that the date range must not exceed ***ninety days***

<Image title="Log Time.png" alt={1900} border={true} src="https://files.readme.io/bec48b5-Log_Time.png">
  Illustration (English)
</Image>

<Image title="Log Time (Vietnamese).png" alt={1897} border={true} src="https://files.readme.io/e6b8454-Log_Time_Vietnamese.png">
  Illustration (Vietnamese)
</Image>

* By default, the logs are sorted chronologically. The latest event will be on top, and the older events will appear below
* To change the sort order based on a specific column, left-click on that column title. That column will be sorted in ascending order. Left-click again on that column title will change the sort order to descending
* To filter a column by specific values, click the down angle icon :fa-angle-down: then click the checkboxes of the desired values
* To export the log data, click on the yellow button :fa-plus-circle: then click on export data and an export file named \<Export\_Audit Log> will be downloaded to your system
* Also, the log will be deleted automatically after ***sixty days***
