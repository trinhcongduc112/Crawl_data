---
title: Form builder - Create forms for PDP model actions
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

Navigate to **Tasks > Action List** tab\
We will be configuring the following actions for drivers on mobile app 

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Action Code
      </th>

      <th style={{ textAlign: "left" }}>
        Action Name
      </th>

      <th style={{ textAlign: "left" }}>
        Required
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        LOADING\_AT\_DEPOT
      </td>

      <td style={{ textAlign: "left" }}>
        Product Loading at Depot
      </td>

      <td style={{ textAlign: "left" }}>
        x
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        LOADING\_AT\_STORE
      </td>

      <td style={{ textAlign: "left" }}>
        Loading at customer (Pickup point)
      </td>

      <td style={{ textAlign: "left" }}>
        x
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        DELIVER\_PRODUCT
      </td>

      <td style={{ textAlign: "left" }}>
        Delivery
      </td>

      <td style={{ textAlign: "left" }}>
        x
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        TRANSIT
      </td>

      <td style={{ textAlign: "left" }}>
        Rest ponit
      </td>

      <td style={{ textAlign: "left" }}>
        x
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        EXTRA\_TASK
      </td>

      <td style={{ textAlign: "left" }}>
        Extra task
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        BACK\_DEPOT
      </td>

      <td style={{ textAlign: "left" }}>
        Back to depot
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        END\_DAY
      </td>

      <td style={{ textAlign: "left" }}>
        End of day
      </td>

      <td style={{ textAlign: "left" }}>
        x
      </td>
    </tr>
  </tbody>
</Table>

## Create a component for the 'LOADING\_AT\_DEPOT' task action

Step 1: Go to the n List], clic, click on the Builder] butto button to add components as the picture below:

![1362](https://files.readme.io/843e038-L1.png "L1.png")

Step 2: Drag the component in the left panel to the right area you want to create\
2.1 Drag "File" component at the Components] button  button and drop into the right area

![1344](https://files.readme.io/d11a85c-2.1.png "2.1.png")

2.2 Input the component information as the picture below, then click the ton:
[ button:

![1347](https://files.readme.io/18f8d2c-2.2.png "2.2.png")

## Create a component for the 'LOADING\_AT\_STORE' task action

Step 1: Go to the  click on the, click on the  button to add button to add components as the picture below:

![1355](https://files.readme.io/2e90d3c-l2.png "l2.png")

Step 2: Drag the component in the left panel to the right area you want to create\
2.1 Drag "File" component at the ts] button and drop button and drop into the right area

![1334](https://files.readme.io/3b1aed6-l3.png "l3.png")

2.2 Drag "Panel" component at the ] button and drop i button and drop into the right area

![1342](https://files.readme.io/f220803-l4.png "l4.png")

2.3 Input the component information as the picture below, then click the k:imag button:

![1332](https://files.readme.io/ea7db0f-l5.png "l5.png")

## Create a component for the 'DELIVER\_PRODUCT' task action

Step 1: Go to the the [Form Bui, click on the  add component button to add components as the picture below:

![1363](https://files.readme.io/9d701d7-l6.png "l6.png")

Step 2: Drag the component in the left panel to the right area you want to create\
2.1 Drag "File" component at the  and drop into the  button and drop into the right area, name of component is "Arrival Check In"

![1341](https://files.readme.io/21d0100-l7.png "l7.png")

2.2 Drag "File" component at the nd drop into the ri button and drop into the right area, name of component is "Unloading Check In"

![1339](https://files.readme.io/96b540a-l8.png "l8.png")

## Create a component for the 'TRANSIT' task action

Step 1: Go to the m Builder] bu, click on the ponents as the button to add components as the picture below:

![1365](https://files.readme.io/bc298cb-l9.png "l9.png")

Step 2: Drag the component in the left panel to the right area you want to create\
2.1 Drag "File" component at the p into the right ar button and drop into the right area, name of component is "Check In"

![1331](https://files.readme.io/7e7d37b-l10.png "l10.png")

## Create a component for the 'END\_DAY' task action

Step 1: Go to the der] button t, click on the s as the pictu button to add components as the picture below:

![1361](https://files.readme.io/c91d728-l11.png "l11.png")

Step 2: Drag the component in the left panel to the right area you want to create\
2.1 Drag "File" component at the  the right area, na button and drop into the right area, name of component is "Check In"
