---
title: Use Lunch Time
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
Mỗi phương tiện giao hàng sẽ có khoảng thời gian nghỉ trưa hoặc không nghỉ trưa.\
Để lên kế hoạch nghỉ trưa cho mỗi xe, theo dõi các bước thiết lập trong hệ thống dưới đây:

## Bật cấu hình sử dụng nghỉ trưa

1. Vào tổ chức, chọn loại Branch\
   2.Nhấn vào More config, tick vào config Use Lunch Time
2. Lưu lại

## Khai báo thời gian nghỉ trưa ở xe

1. Vào Vehicle
2. Update/Tạo mới 1 phương tiện
3. Nhập Lunch Start Time/ Lunch Stop Time\
   Định dạng nhập: HH:MM
4. Lưu

## Khởi tạo lộ trình

Sau khi khai báo khoảng thời gian nghỉ trưa, bắt đầu khởi tạo lộ trình. Lộ trình sẽ có khoảng nghỉ trưa trên timeline ( tính từ thời gian bắt đầu nghỉ trưa đến thời gian kết thúc nghỉ trưa)

![1371](https://files.readme.io/b4e7cc2-lunchtime.png "lunchtime.png")

Hệ thống sẽ tính toán thời gian nghỉ trưa dựa trên dữ liệu người dùng đã khai báo, thời gian giao hàng tới điểm tiếp theo sẽ tính toán dựa trên quãng đường từ điểm trước đó có tính cả thời gian nghỉ trưa cho mỗi xe

Trong trường hợp người dùng khởi tạo lộ trình nhiều lần, nếu chọn khoảng cut-off-time trùng với khoảng thời gian nghỉ trưa thì thời gian của chuyến đó sẽ bắt đầu qua khoảng nghỉ trưa (không trùng với time nghỉ trưa)
