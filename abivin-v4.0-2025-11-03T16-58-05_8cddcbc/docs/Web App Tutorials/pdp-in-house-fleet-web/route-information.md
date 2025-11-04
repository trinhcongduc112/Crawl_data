---
title: Route information
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
Để xem các thông tin về đơn hàng, quãng đường, doanh thu, ... cho mỗi xe trên lộ trình:

1. Vào Vận tải, chọn chi nhánh
2. Xem thông tin tổng quát lộ trình

## Xem thông tin lộ trình tổng quát các xe

Khi chưa bật từng xe để xem chi tiết lộ trình, các thông số sẽ hiển thị tổng số của tất cả các xe trên lộ trình. Trường hợp các đơn bị rớt trên timeline sẽ không tính vào tổng số các thông số trong lộ trình.

![1915](https://files.readme.io/b9190cd-routeinfo.png "routeinfo.png")

Giải thích các thông số:

* Orders: Tổng số đơn hàng của tất cả các xe
* Distance: Tổng quãng đường của tất cả các xe theo kế hoạch
* Costs: = SUM(fixed cost của xe + quãng đường x cost per km)
* Revenues: Tổng giá của tất cả các đơn hàng trên các xe
* Revenues/Distance: Doanh thu/Quãng đường
* Familiarity: Số khách hàng thân thuộc của các xe so với tổng số các khách hàng đang có trên lộ trình\
  % thân thuộc = số khách hàng thân thuộc / tổng số khách hàng \* 100
* Hiệu suất: = Doanh thu - Chi phí

## Xem thông tin lộ trình của từng xe

Để xem thông tin lộ trình của mỗi xe, enable vào từng xe sẽ hiển thị thông tin của mỗi xe đó

1. Vào Vận tải
2. Bật vào icon xe để xem thông tin của mỗi xe

## Thông tin lộ trình x-Dock

![1355](https://files.readme.io/5a60179-p3.png "p3.png")

* Xe đi từ kho đến x-Dock:\
  Các thông số = tổng thông số các xe đi từ x-Dock đến các cửa hàng\
  Như hình trên, thông số của xe Truck\_005 bằng tổng thông số của  xe Truck\_004
