---
title: Manual Split Orders
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
Trong trường hợp các đơn hàng được đặt giao đến cùng 1 khách hàng có capacity( weight/volume) lớn hơn sức chứa của xe, mà xe đó không thể chở được, nhân viên điều phối có thể chia đơn hàng thủ công để thỏa mãn capacity của đơn \<= sức chứa của xe để chở được.

Giả sử đơn hàng ban đầu có mã SO-0001 có capacity là 100kg, 10 m3., các xe hiện tại có capacity là 90kg, 10m3. Đơn này sẽ không giao được vì lớn hơn capacity của xe.\
Lúc này, nhân viên điều phối cần chia thủ công đơn đó thành 2 mã đơn khác nhau: SO-0001.1 và SO-0001.2 thỏa mãn capacity của mỗi đơn \< trọng lượng của xe để giao.

Các bước thiết lập trên hệ thống:

## Thiết lập đơn hàng

1. Vào đơn hàng bán, tạo/cập nhật đơn
2. Tick vào nút Splitted Order
3. Lưu lại\
   Với trường hợp import đơn hàng:

* Nếu đơn chẻ thì điền 1
* Nếu không phải đơn chẻ thì điền 0 hoặc để trống

## Khởi tạo lộ trình

Các đơn chẻ luôn giao cho 2 xe khác nhau, đảm bảo các đơn chẻ không được giao trong cùng 1 xe

![1364](https://files.readme.io/eecfbd1-split.png "split.png")

Trường hợp các đơn chẻ giao đến 1 khách hàng đã tách giao cho các xe khác nhau, nếu move đơn chẻ gộp lại để giao trong cùng 1 xe, hệ thống sẽ đưa ra thông báo không cho phép kéo như hình dưới đây:

![1363](https://files.readme.io/3375bf6-move.png "move.png")
