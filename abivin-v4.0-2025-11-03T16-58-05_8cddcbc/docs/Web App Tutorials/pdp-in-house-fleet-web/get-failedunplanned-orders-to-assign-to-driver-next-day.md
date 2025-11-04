---
title: Get Failed/Unplanned Orders to assign to Driver next day
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
## Get failed orders

Đọc thêm ở docs sau cách lấy đơn giao lại: [https://docs.abivin.com/docs/how-to-get-failed-orders-from-a-past-day-for-re-delivery](https://docs.abivin.com/docs/how-to-get-failed-orders-from-a-past-day-for-re-delivery)\
Với trường hợp của Mesa thì đơn giao lại sẽ do chính tài xế hôm trước giao lại đơn đó\
Với VTI: Đơn giao lại có thể giao cho tài xế mới hoặc giao cho tài xế cũ

## Get Unplanned Orders

Unplanned Orders là những đơn rớt không thể vào được lộ trình vì 1 số lý do nào đó. Để lấy lại những đơn này, theo dõi các bước sau:

1. Vào tổ chức loại Manufacture
2. Bật config Allow Re-delivery Order
3. Lưu
4. Vào Orders, hover vào dấu + màu vàng và nhấn nút Fetch old order

![1347](https://files.readme.io/9f86524-failed-orders.png "failed-orders.png")

Delivery Date: Ngày sẽ giao lại đơn rớt\
Get Failed Orders Date: Ngày mà các đơn đó bị rớt\
Nếu tick vào nút Re-assigned: Các đơn không giao được hôm trước sẽ được giao lại cho đúng tài xế đó hoặc cho tài xế khác vào ngày delivery date đã chọn\
Nếu không tick  vào nút Re-assigned: Các đơn không giao được hôm trước sẽ được giao lại cho đúng tài xế đó vào ngày delivery date đã chọn

Nếu tick vào nút Not completed delivery: Lấy đơn không giao được\
Tick vào nút Missing orders: Lấy đơn rớt\
5\. Sau khi lấy đơn xong, các đơn giao lại/đơn rớt sẽ đánh dấu màu xanh trên danh sách đơn

Chú thích:\
Trường hợp lấy nhiều lần thì không bị duplicate và đè lên dữ liệu đã lấy lần đầu

## Khởi tạo lộ trình với đơn giao lại/đơn rớt

Khi khởi tạo lộ trình với cả đơn giao lại/đơn rớt và đơn hàng bán thì lộ trình không ưu tiên cho đơn nào trước, vẫn thỏa mãn giao cho tài xế cũ/mới , thỏa mãn quãng đường đến các cửa hàng là ngắn nhất.\
Các đơn giao lại/đơn rớt đánh dấu marker xanh trên lộ trình

Với các đơn giao lại/đơn rớt thì vẫn thực hiện kéo đơn bình thường như các đơn hàng bán
