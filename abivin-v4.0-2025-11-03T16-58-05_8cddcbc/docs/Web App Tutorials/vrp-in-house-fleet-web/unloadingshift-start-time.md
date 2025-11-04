---
title: Unloading Time/Shift Start Time
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
This relates to Algorithms that we are using\
Shift start time: relative or absolute (backend truyền lên cho algo dữ liệu thời gian bắt đầu chạy của mỗi xe)\
Loading & unloading time: đọc dữ liệu backend gửi. Nếu check Enable loading time at each Depot = Y -> sử dụng loading time tại depot; nếu check Enable unloading time at customer = Y -> sử dụng unloading time tại mỗi customer\
Đọc min/max time of loading/unloading at depot/customer. Nếu sau khi tính loading/unloading time theo công thức (*) mà bị vượt min/max loading/unloading time -> Algo lấy theo min/max\
(*) Công thức:\
Loading time (tại depot) = Processing time + loading time per kg (hoặc m3) *quantity - Xem thêm tại phần 2:[https://docs.google.com/document/d/1iQ-MjzQe4Hq2hGZjEHWoPIktZW8ro3ybfO7ezxhTFmM/edit#heading=h.c32bgmn4tptb](https://docs.google.com/document/d/1iQ-MjzQe4Hq2hGZjEHWoPIktZW8ro3ybfO7ezxhTFmM/edit#heading=h.c32bgmn4tptb)\
Unloading time (tại customer) = Processing time + unloading time per CBM* quantity of CBM of total orders in a stop  - Xem thêm tại phần 2: [https://docs.google.com/document/d/1XRHg379v6R\_dJCzX4Ke\_z4pp1MNv\_8EDIiwV9IuFLM4/edit](https://docs.google.com/document/d/1XRHg379v6R_dJCzX4Ke_z4pp1MNv_8EDIiwV9IuFLM4/edit)\
Associated product: nếu bật tại manu, check các sp thuộc cùng product category có associated product = Y (để xử lý ở bước chia đơn)
