---
title: Cập nhật tồn kho của đơn hàng 1 chiều
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
Ban đầu, mã sản phẩm SP005 của tổ chức KSXOUT còn 1000 đơn vị

![1366](https://files.readme.io/c2cf7b7-2.0.png "2.0.png")

Bước 1: Tạo đơn hàng bán mã sản phẩm SP005 với số lượng là 200

![1366](https://files.readme.io/2c69bf7-2.1.png "2.1.png")

Bước 2: Sau khi tổng công ty chọn điểm đầu thì 200 đơn vị tồn kho của KSXOUT sẽ hiển thị ở cột Trong Đơn bán

![1366](https://files.readme.io/b9a1f84-2.2.png "2.2.png")

Bước 3: KSXOUT chuyển trạng thái của đơn hàng sang Picked and Packed khi tài xế đến lấy hàng đi giao

![1366](https://files.readme.io/b40fc51-2.3.png "2.3.png")

200 thùng được chuyển từ cột On-hand sang Picked (từ 1000 xuống 800 thùng)

![1366](https://files.readme.io/30ab381-2.4.png "2.4.png")

Bước 4: Khi tài xế đem hàng đến Điểm giao xong thì tài khoản nhà vận tải chuyển trạng thái đơn hàng sang Shipped  

![1366](https://files.readme.io/0ee3b8a-2.5.png "2.5.png")

Số lượng tồn kho hiển thị ở cột On-SOrder và Picked mất đi, cột On-hand hiển thị số lượng đã giảm là 800 thùng

![1366](https://files.readme.io/081bdfd-2.6.png "2.6.png")

* Nếu đơn hàng không thực hiện được thì tài khoản kho chuyển trạng thái đơn hàng sang Canceled. Khi đó cột On-SOrder sẽ giảm đi một số lượng bằng số thùng chiều đi đặt trong đơn bán
