---
title: Are the shift codes duplicated?
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
## Are the shift codes duplicated?

**Case**: Customers may see the shift codes/ tripcodes from different vehicles belonging to different branches have the exact digits.

<Image title="1222.png" alt={1468} src="https://files.readme.io/b19e360-1222.png">
  The XEKHO009 vehicle belongs to the "Chi Nhánh 3" Branch has the shift code: SHIFT-210203-0003 on the 04 February 2021 route plan.
</Image>

<Image title="223.png" alt={1469} src="https://files.readme.io/81db588-223.png">
  The XEKHO001 vehicle belongs to the "Chi Nhánh 1" Branch has the shift code: SHIFT-210203-0003 on the 04 February 2021 route plan.
</Image>

**Reason**: The format of the Shift/Trip code on the platform is: **SHIFT-YYMMDD-\{counter}**

![156](https://files.readme.io/210aa94-222.png "222.png")

For example:  ***SHIFT-220104-0001*** means the shift is the ***first*** shift of the vehicle, planned on ***04 January 2022***.\
The system by default allows Shift codes of vehicles from different branches can have the same digits.
