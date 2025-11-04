---
title: Pickup Orders
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
Đối với mô hình VRP trong phân phối hàng, các đơn hàng luôn được lấy từ kho và giao đi tới các khách hàng khác nhau. Trong trường hợp nhân viên giao hàng đến lấy hàng kết hợp với đi giao hàng tại các điểm cửa hàng thì áp dụng tính năng Pickup Orders trong hệ thống. Để thiết lập các đơn nhặt này theo dõi các bước sau:

## Thiết lập đơn pickup ở đơn hàng bán

1. Vào Orders/Sales Order, tạo mới/cập nhật đơn hàng bằng cách nhấn vào ô Pickup Order
2. Lưu lại\
   Với trường hợp import order:

* Nếu đơn pick up thì điền 1
* Nếu không phải đơn pickup thì điền 0 hoặc để trống\
  Sau khi thiết lập xong, các đơn hàng là pickup sẽ hiển thị Yes trên danh sách đơn hàng

![1359](https://files.readme.io/1193527-pickup.png "pickup.png")

## Khởi tạo lộ trình

Sau khi lên lộ trình, các đơn pickup sẽ không được tính capacity của xe. Các đơn này sẽ ko tính weight/volume theo fill rate khi lên lộ trình.

![1359](https://files.readme.io/777444d-lotrinh.png "lotrinh.png")

Các đơn pickup không có ưu tiên khi lên lộ trình, vẫn track điều kiện cùng các đơn bán hàng khác và vẫn ưu tiên theo quãng đường ngắn nhất
