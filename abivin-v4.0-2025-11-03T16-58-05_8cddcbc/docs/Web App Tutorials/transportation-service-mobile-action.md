---
title: Transportation service Mobile action
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
## Create actions

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Action Name (Changeable)
      </th>

      <th style={{ textAlign: "left" }}>
        Action Code (Compulsory)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Start Day at Depot
      </td>

      <td style={{ textAlign: "left" }}>
        DEPOT\_START\_DAY
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Deliver at Depot
      </td>

      <td style={{ textAlign: "left" }}>
        DEPOT\_DELIVERY
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Receive at Depot
      </td>

      <td style={{ textAlign: "left" }}>
        DEPOT\_RECEIVING
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        End of Day at Depot
      </td>

      <td style={{ textAlign: "left" }}>
        DEPOT\_END\_DAY
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Loading at Depot
      </td>

      <td style={{ textAlign: "left" }}>
        LOADING\_AT\_DEPOT
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Back to Depot
      </td>

      <td style={{ textAlign: "left" }}>
        BACK\_DEPOT
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        End of Day
      </td>

      <td style={{ textAlign: "left" }}>
        END\_DAY
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Deliver Products
      </td>

      <td style={{ textAlign: "left" }}>
        DELIVER\_PRODUCT
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Loading at Store
      </td>

      <td style={{ textAlign: "left" }}>
        LOADING\_AT\_STORE
      </td>
    </tr>
  </tbody>
</Table>

## Drag forms for action codes

## DEPOT\_START\_DAY

**1. Panel component:**\
**Position:** On top\
**Input rules:**\
***Display > Title:*** Order Information *(Can be customized)*

**2. Table component:**\
**Position:** Inside **Panel component**\
**Input rules:**\
***Display > Number of Rows:*** 1\
***Display > Number of Columns:*** 2\
***API > Custom Properties:*** ***Key:*** url; ***Value:*** /orders/list/

**3. Text Field component 1:**\
**Position:** Inside **Table component**\
**Input rules:**\
***Display > Label:*** Order Code *(Can be customized)*\
***Data > Default Value:*** orderCode

**4. Text Field component 2:**\
**Position:** Inside **Table component**, to the right of **Text Field component 1**\
**Input rules:**\
***Display > Label:*** Order Code *(Can be customized)*\
***Data > Default Value:*** totalWeight

**5. File component:**\
**Position:** Below **Panel component**\
***Display > Label:*** Check-In *(Can be customized)*\
***Validation:*** Required *(Optional)*\
***API > Custom Properties:*** ***Key:*** isHideSelectFromLibrary; ***Value:*** true

## DEPOT\_DELIVERY

**1. Panel component:**\
**Position:** On top\
**Input rules:**\
***Display > Title:*** Shipping Information

**2. Text Field component:**\
**Position:** Inside **Panel component**\
***Display > Label:*** Warehouse *(Can be customized)*\
***API > Property Name:*** depotName
