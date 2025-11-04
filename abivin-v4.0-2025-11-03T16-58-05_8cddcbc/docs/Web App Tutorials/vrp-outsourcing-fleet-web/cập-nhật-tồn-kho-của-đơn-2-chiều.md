---
title: Cập nhật tồn kho của đơn 2 chiều
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
Ban đầu, mã sản phẩm SP001 của tổ chức KSXOUT còn 1000 đơn vị

![1366](https://files.readme.io/869e666-4.0.png "4.0.png")

Bước 1: Tạo đơn hàng bán mã sản phẩm SP001 với số lượng là 300

![1366](https://files.readme.io/e5616a4-4.1.png "4.1.png")

300 đơn vị tồn kho của KSXOUT sẽ hiển thị ở cột Trên đơn về

![1366](https://files.readme.io/16d0399-4.2.png "4.2.png")

Bước 3: Nhà vận tải chuyển trạng thái của đơn hàng sang Picked and Packed khi tài xế đến lấy hàng tại điểm giao\
\--> 300 đơn vị tồn kho sẽ hiển thị ở cột Đang nhận lại và ở cột Trên đơn về.

![1366](https://files.readme.io/bb8b902-3.3.png "3.3.png")

Bước 3: Tài xế lấy hàng về kho thì tài khoản Kho chuyển trạng thái của đơn hàng sang Shipped\
\--> 300 đơn vị tồn kho hiển thị ở cột Trên đơn về và Đang nhận lại chuyển sang cột Trên kệ. Số lượng tăng từ 1000 lên 1300 thùng.

![1366](https://files.readme.io/520f60f-4.4.png "4.4.png")

* Nếu đơn hàng chiều về không thực hiện được thì tài khoản nhà vận tải chuyển tình trạng đặt hàng sang Canceled. Khi đó cột Trong đơn về của đơn hàng sẽ giảm đi một số lượng bằng số lượng thùng chiều về đã đặt trong đơn bán
