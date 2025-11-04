---
title: Cut-off time for multiple shifts
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
Khi nhân viên điều phối muốn lên lộ trình nhiều lần trong 1 ngày với khoảng thời gian xuất phát từ kho giữa mỗi shfit của các xe là khác nhau, có thể sử dụng tính năng cut-off-time cho mỗi lần khởi tạo.

## Trường hợp Không chọn khoảng cut-off-time

**Khi lên lộ trình trong cùng 1 xe nhiều shift**\
Nếu không chọn cut-off-time thì thời gian shift thứ 2 trở đi cách shift đầu tiên 30 phút như hình dưới đây:

![1361](https://files.readme.io/c4d3f3f-cutofff.png "cutofff.png")

**Khi lên lộ trình với nhiều lần cho các xe khác nhau**\
Nếu không chọn cut-off-time thì lộ trình lần tiếp theo cho xe khác xe sẽ xuất phát từ Start Time của xe, không phụ thuộc vào cut-off-time

![1373](https://files.readme.io/a97083e-c122.png "c122.png")

## Trường hợp chọn khoảng cut-off-time

**Khi lên lộ trình trong cùng 1 xe nhiều shift**\
Nếu chọn khoảng cut-off-time thì thời gian shift thứ 2 trở đi sẽ nhận khoảng thời gian xuất phát là thời gian cut-off-time đã chọn

Khi lên lộ trình với nhiều lần cho các xe khác nhau\
Nếu chọn cut-off-time thì lộ trình lần tiếp theo cho xe khác xe sẽ xuất phát từ khoảng thời gian cut-off-time đã chọn

Trường hợp nếu chọn khoảng cut-off-time nằm ngoài khoảng Stop Time của xe thì sẽ không lên được lộ trình.
