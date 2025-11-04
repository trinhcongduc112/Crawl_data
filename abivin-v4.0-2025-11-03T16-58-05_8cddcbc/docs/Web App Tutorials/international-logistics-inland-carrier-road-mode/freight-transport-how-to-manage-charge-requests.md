---
title: Manage Requests
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
When the drivers operate the shipments, they have to pay various related fees (or charges)

After completing a shipment, in order to be able to deliver another shipment, the driver also needs to send a non-freight related (NFR) request

Information of these requests will be submitted to Abivin vRoute, waiting for the dispatcher approval

This article will assist the dispatchers on how to manage these requests

## Manage charge types

* Navigate to **Charges > Charge type** tab
* This tab is where all the charge types are listed

## Create charge type

* Please refer to the **[CRUD](https://docs.abivin.com/docs/crud#section-create)** article to get the general steps on how to create charge type.

## Edit charge type

* Please refer to the **[CRUD](https://docs.abivin.com/docs/crud#section-edit)** article to get the general steps on how to edit charge type information

## Delete charge type

* Please refer to the **[CRUD](https://docs.abivin.com/docs/crud#section-delete)** article to get the general steps on how to delete charge type.

## Charge type information

* A charge type will have these essential information fields

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Charge Code
      </td>

      <td>
        The management code assigned to this charge type
      </td>
    </tr>

    <tr>
      <td>
        Organization Code
      </td>

      <td>
        Code of the organization which will manage this charge
      </td>
    </tr>

    <tr>
      <td>
        Charge Name
      </td>

      <td>
        Specific name of the charge
      </td>
    </tr>

    <tr>
      <td>
        Note
      </td>

      <td>
        Short description about the charge. This field will be filled in by the driver on Mobile app
      </td>
    </tr>

    <tr>
      <td>
        Price
      </td>

      <td>
        Price of the charge. This field will be filled in by the driver on Mobile app
      </td>
    </tr>
  </tbody>
</Table>

## Manage charge requests

After enabling the **Charges** tab, the dispatcher can now view and manage charge requests submitted from the drivers.

* Navigate to **Charges > Charge request** tab
* This tab is where all the charge requests are listed

## Manage charge requests

* To change the status of the charge request, the dispatcher can click on the **Edit** :fa-pencil: icon next to that charge. On the **Charge request detail** screen, the dispatcher can choose from a set of decisions (Could be *Approve* - *Disapprove*), then click **Save** to confirm the decision

<Image title="Mange charge request.gif" alt={1668} className="border" border={true} src="https://files.readme.io/79113f2-Mange_charge_request.gif" />

## Charge request information

* A charge request will have these information fields

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Shipment Code
      </td>

      <td>
        Management code of the shipment, assigned by its owner organization
      </td>
    </tr>

    <tr>
      <td>
        Origin
      </td>

      <td>
        First location of the shipment
      </td>
    </tr>

    <tr>
      <td>
        Destination
      </td>

      <td>
        Last location of the shipment
      </td>
    </tr>

    <tr>
      <td>
        Container Code
      </td>

      <td>
        Management code of the container, assigned by its owner organization (Note: This is not container serial number)
      </td>
    </tr>

    <tr>
      <td>
        Charge Name
      </td>

      <td>
        Specific name of the charge
      </td>
    </tr>

    <tr>
      <td>
        Price
      </td>

      <td>
        The amount of the charge, submitted by the driver
      </td>
    </tr>

    <tr>
      <td>
        Driver
      </td>

      <td>
        Name of the driver who's operating the shipment
      </td>
    </tr>

    <tr>
      <td>
        Note
      </td>

      <td>
        Short note about the charge
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        Approval status of the charge.
      </td>
    </tr>

    <tr>
      <td>
        Action
      </td>

      <td>
        The dispatcher will approve the charge request here, thus changing the status of the charge
      </td>
    </tr>
  </tbody>
</Table>

## Manage Non-freight related request (NFR)

* Navigate to **Tasks > Shipment List** tab
* If the truck tractor driver has just submitted a Non-freight related request (NFR) after completing a certain shipment, the dispatcher will receive a notification on Web app. The shipments which have NFR requests will also be highlighted with a mild blue color
* Clicking on the notification will lead the dispatcher to the **Shipment Details** screen of that shipment
* The dispatcher needs to scroll the horizontal scroll bar to the far right. Here, the dispatcher can decide to either **Approve** or **Decline** the NFR request by clicking on the corresponding button
* The shipment will no longer be highlighted after the NFR request has been resolved
* Similar to the shipment requests, all NFR requests will show up on the **Notification** section of all dispatcher accounts

<Image title="SNP Approve NFR.gif" alt={1920} className="border" border={true} src="https://files.readme.io/f4182bf-SNP_Approve_NFR.gif" />
