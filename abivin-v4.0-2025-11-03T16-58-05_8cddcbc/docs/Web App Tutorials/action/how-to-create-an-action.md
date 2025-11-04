---
title: Manage Actions
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: link
      title: Introduction to Form Builder
      url: https://docs.abivin.com/docs/introduction-to-form-builder
---
* Actions in Abivin vRoute would help simulate on the Mobile app the real life practices of the drivers during their performance of the delivery routes

## Create Actions

## Option 1: Create single action using Web form

* Please refer to the [**CRUD**](https://docs.abivin.com/docs/crud#section-option-1-create-single-objects-using-abivin-vroute-web-form) article to know the general steps about creating single object using web form
* **Note**: This option is used when creating actions for Optimal Routing Plan business model

## Create multiple actions using Excel template

* Please refer to the [**CRUD**](https://docs.abivin.com/docs/crud#section-option-2-create-multiple-objects-using-excel-templates) article to know the general steps about creating multiple objects using Excel template
* **Note**: This option is used when creating actions for Customer Relationship Management (CRM) business model

## Information fields of an action

* Below is the list of all information fields of an action

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description & Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Organizations
        (Required)
      </td>

      <td>
        **1. Description:**\
        Organization Name of the Manufacturer\
        **2. Input rules:**\
        Click on the field, type the Organization Name of the Manufacturer into the search bar, then select from the drop down menu
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Organization Code\
        (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        Organization Code of the Manufacturer\
        **2. Input rules:**\
        Copy the Organization Code of the Manufacturer on Web app and paste into this cell
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Action Code\
        (Web form + Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The code assigned to the action being created\
        **2. Input rules:**\
        Click on the field and choose the code from the drop down menu\
        The list of Action codes and their meaning are listed in the section: [***List of Action codes***](https://docs.abivin.com/docs/how-to-create-an-action#section-list-of-action-codes-for-optimal-routing-plan-business-model)
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Tasks action Name (Web form); Action Name (Excel template)\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The name assigned to the action being created\
        This name will show up on the Mobile app\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Groups able\
        (Required)
      </td>

      <td>
        **1. Description:**\
        The User groups within the Organization, by whom the action being created will be performed\
        **2. Input rules:**\
        Click on that field, type the
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Description\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        Short description to explain purpose of the action being created
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Checkin in task\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        **2. Input rules:**
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Checkout in task\
        (Web form)\
        (Optional)
      </td>

      <td>
        **1. Description:**\
        **2. Input rules:**
      </td>
    </tr>
  </tbody>
</Table>

## List of Action codes for Optimal Routing Plan business model

* Below is the default set of action codes used only for Optimal Routing Plan business models (VRP and PDP). Due to the differences in operation process between these two models, some action codes are only available for one model or the other
* Based on the description of the Action Code, you can type the corresponding Action Name so that the drivers can understand

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action Code
      </th>

      <th>
        Description
      </th>

      <th>
        Action Name (Suggestion)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        LOADING\_AT\_DEPOT
        (VRP model + PDP model)
        (Required)
      </td>

      <td>
        The driver loads products onto the vehicle at the Depot
      </td>

      <td>
        Load Products at Depot
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        DELIVER\_PRODUCT\
        (VRP model + PDP model)\
        (Required)
      </td>

      <td>
        The driver arrives at customer's location and delivers product to the customer
      </td>

      <td>
        Deliver Products
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        LOADING\_AT\_STORE\
        (PDP model)\
        (Required)
      </td>

      <td>
        The driver picks up products from the customer's warehouse onto the vehicle to continue the delivery to other customer
      </td>

      <td>
        Load Products at Customer Warehouse
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        TRANSIT\
        (PDP model)\
        (Required)
      </td>

      <td>
        The driver rests at the end of a working day, before continuing the delivery route on the next day
      </td>

      <td>
        Transit
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        BACK\_DEPOT\
        (VRP model + PDP model)\
        (Required)
      </td>

      <td>
        The driver has come back to the Depot after performing a delivery route\
        Note: This action will only show up if the driver is assigned consecutive delivery routes. It will show up on the task list of the former delivery route
      </td>

      <td>
        Travel Back to Depot
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        END\_DAY\
        (VRP model + PDP model)\
        (Required)
      </td>

      <td>
        The driver finishes his working day
      </td>

      <td>
        End of Day
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        EXTRA\_TASK\
        (VRP model + PDP model)\
        (Optional)
      </td>

      <td>
        Additional tasks that the driver might perform during the delivery route
      </td>

      <td>
        Extra Task
      </td>
    </tr>
  </tbody>
</Table>

## Update action

* Please refer to the [**CRUD**](https://docs.abivin.com/docs/crud#section-update-objects) article to know the general steps about updating objects in Abivin vRoute

## Delete action

* Please refer to the [**CRUD**](https://docs.abivin.com/docs/crud#section-delete-objects) article to know the general steps about deleting objects in Abivin vRoute
