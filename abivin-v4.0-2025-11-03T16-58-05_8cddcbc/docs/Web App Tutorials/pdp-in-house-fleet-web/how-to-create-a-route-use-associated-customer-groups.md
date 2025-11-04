---
title: Associated customer group
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
Các đơn hàng được giao từ các khách hàng khác nhau giao có thể/không thể giao trong cùng 1 chuyến. Để các khách hàng đó không giao trong cùng 1 chuyến, áp dụng tính năng phân chia nhóm khách hàng của hệ thống bằng cách theo dõi các bước thiết lập dưới đây:

## Step 1: Create the customer group

Read more at the link: [https://docs.abivin.com/docs/manage-customer-groups](https://docs.abivin.com/docs/manage-customer-groups) to create/import the customer groups\
Có 3 loại nhóm liên kết:\
Loại 1: Liên kết với chính nhóm đó\
Loại 2: Liên kết giữa nhóm này với nhóm khác\
Loại 3: Không liên kết với nhóm nào

## Step 2: Upload the customer list assigned  the group created in Step 1

* Download the data sample file
* Fill the information into the excel file

![1355](https://files.readme.io/d293369-N4.png "N4.png")

## Step 3: Go to the Transportation tab, select the branch and optimize the route

Loại 1: Nếu các khách hàng thuộc nhóm liên kết với chính nó, sau khi khởi tạo lộ trình thì các khách hàng thuộc nhóm này sẽ được giao riêng cho 1 xe bất kỳ, đảm bảo không giao tới các khách hàng thuộc loại nhóm liên kết khác

![1363](https://files.readme.io/873c5bd-N5.png "N5.png")

The delivery plan will only include orders to Customers in this Group.\
Loại 2: Nếu các khách hàng thuộc nhóm liên kết giữa các nhóm với nhau, sau khi khởi tạo lộ trình thì các khách hàng thuộc nhóm này sẽ được giao riêng cho 1 xe bất kỳ, đảm bảo không giao tới các khách hàng thuộc loại nhóm liên kết khác.

![1364](https://files.readme.io/4f8ea84-N6.png "N6.png")

The delivery plan will include Customers in the associated Groups.\
Loại 3: Nếu các khách hàng thuộc nhóm không liên kết với nhóm nào, thì khi lên lộ trình sẽ giao cho các khách hàng mà không thuộc nhóm nào hoặc các nhóm khác cũng không có liên kết và cho các xe riêng với 2 loại trên

![1366](https://files.readme.io/9c0760f-N7.png "N7.png")

The shipment to customers in this Group will be optimized and assign to drivers normally.
