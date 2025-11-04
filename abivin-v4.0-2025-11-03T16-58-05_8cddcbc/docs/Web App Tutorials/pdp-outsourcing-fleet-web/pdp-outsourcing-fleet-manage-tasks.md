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
* Throughout the delivery process of the order, you can keep track of the status of the mobile tasks on Web app, using the **Task** function
* As you lock a Delivery Route during the Route Plan Optimization process, the tasks of all Orders on that Delivery Route will be generated automatically over at the tab **Tasks > Task List**

## Search and filter tasks

## Search tasks based on Order Date

* On this tab, to search for the tasks of a specific Order, first click on the first date range field (On the right of the search bar). On the drop down calendars, select the date range which contains the attribute **Order Date** of the Order you're finding

<Image title="Selection_024.png" alt={1907} className="border" border={true} src="https://files.readme.io/ecf2aac-Selection_024.png" />

## Search tasks based on task creation date

* You can search tasks by their creation dates by clicking on the second date range field (The one that reads ***Filter By Created At***), select the appropriate date range from the drop down calendars

<Image title="Jst9Eolq0N.png" alt={1660} className="border" border={true} src="https://files.readme.io/15427b9-Jst9Eolq0N.png" />

## Search task based on Task Code

* To search for a particular task, you can input the specific **Task Code** of that task into the search bar

<Image title="Selection_023.png" alt={1701} className="border" border={true} src="https://files.readme.io/41a7beb-Selection_023.png" />

## Filter tasks

* You can filter tasks based on the following attributes: **Order Code, Organizations; Driver; Status, Action**
* The steps to filter are described below:
* 1 - Click on the column title of the attribute you want to use as filter
* 2 - On the drop down list, click on the check box :fa-square-o: of the attribute value by which you want to filter tasks
* In the images below, we have illustrated the process to filter tasks based on Order Code

<Image title="task order.png" alt={1908} className="border" border={true} src="https://files.readme.io/5bfee52-task_order.png" />

*

<Image title="task order 1.png" alt={208} className="border" border={true} src="https://files.readme.io/cffa362-task_order_1.png" />

<Image title="task order 3.png" alt={1908} className="border" border={true} src="https://files.readme.io/04f206c-task_order_3.png" />

## Task details

* Below are the information of a task

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Column title
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Task Code
      </td>

      <td>
        Management code of the task
      </td>
    </tr>

    <tr>
      <td>
        Order Code
      </td>

      <td>
        The Order to which the task is associated
      </td>
    </tr>

    <tr>
      <td>
        Task Name
      </td>

      <td>
        Name of the task
      </td>
    </tr>

    <tr>
      <td>
        Organizations
      </td>

      <td>
        The Depot from where the Order originated
      </td>
    </tr>

    <tr>
      <td>
        Assigned to
      </td>

      <td>
        The Driver who delivered the Order
      </td>
    </tr>

    <tr>
      <td>
        Customer
      </td>

      <td>
        The customer who placed the Order
      </td>
    </tr>

    <tr>
      <td>
        Created At
      </td>

      <td>
        The time point when the Order was created
      </td>
    </tr>

    <tr>
      <td>
        Start Date
      </td>

      <td>
        The time point when the task should have been started as planned
      </td>
    </tr>

    <tr>
      <td>
        Due date
      </td>

      <td>
        The time point when the task should have been finished as planned
      </td>
    </tr>

    <tr>
      <td>
        Completion Date
      </td>

      <td>
        The time point when the task was actually finished\
        This time point is the time point when the tasks was successfully submitted from the Mobile app to the Web app
      </td>
    </tr>

    <tr>
      <td>
        Results
      </td>

      <td>
        Result of the task
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        Status of the task\
        Below are the possible statuses:
      </td>
    </tr>

    <tr>
      <td>
        Action
      </td>

      <td>
        The action associated with the task
      </td>
    </tr>
  </tbody>
</Table>

* To view the details of submitted tasks (Tasks which have the status value to be ***Completed***), click on the icon **Submit** :fa-gear: under the column **Edit**

<Image title="1Gw3Y2oAfH.png" alt={1671} className="border" border={true} src="https://files.readme.io/5eb678b-1Gw3Y2oAfH.png" />

* Upon clicking on the icon **Submit** :fa-gear:, you will be directed to the task detail screen. On this screen, you can view the documents (Check-in, Check-out photos, Electronic Proof of Delivery, Customer signature etc.) that have been submitted from the Mobile app

<Image title="NGePopnbbm.png" alt={1712} className="border" border={true} src="https://files.readme.io/5b15cb5-NGePopnbbm.png" />

## Note when searching/filtering tasks

* You can combine the search/filter functions to increase result accuracy. Note that when you combine two date ranges (Order Date and Order creation date), those two date ranges must have overlapping range, else there would be no result
* Selecting date range exceed ***07 days*** is discouraged, because that could very likely cause system unstability due to too many tasks
