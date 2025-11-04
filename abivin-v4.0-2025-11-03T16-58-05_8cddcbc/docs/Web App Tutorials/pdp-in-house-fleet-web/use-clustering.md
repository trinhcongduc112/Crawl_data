---
title: Use Clustering
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
Để hạn chế các xe giao chồng lấn giữa các tuyến đường, nhân viên điều phối có thể sử dụng cấu hình chia theo cụm để hạn chế tối đa chồng lấn đường đi giữa các xe, phân các khách hàng theo các cụm mà không vi phạm vượt quá sức chứa (trọng lượng/thể tích) của các xe.\
Chia theo cụm thuật toán sẽ bỏ qua phần đảm bảo tổng chi phí thấp nhất mà ưu tiên các giải quyết phần cắt nhau của lộ trình các xe. Kết quả là các xe sẽ được chia theo cụm.

## Thiết lập clustering

1. Vào tổ chức
2. Chọn loại branch, nhấn Edit
3. Tick vào config Use Clustering
4. Lưu lại

## Khởi tạo lộ trình

1. Lộ trình khi chưa chia theo cụm

![1751](https://files.readme.io/f349c12-p1.png "p1.png")

2. Lộ trình khi chia theo cụm

![1921](https://files.readme.io/9389bcf-p2.png "p2.png")

Khi chia theo cụm thì hạn chế việc lộ trình của các xe bị cắt nhau, đường đi giữa các xe không bị chồng lấn quá nhiều.\
Chia theo cụm sẽ có các dạng như sau:

1. Cụm hình cánh quạt
