---
title: 'Hướng dẫn Habeco: Nhà vận tải Xử lý đơn hàng'
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
## Các điều kiện cần trước khi tạo đơn hàng

## Thiết lập tải trọng của xe

* Cần kiểm tra 

## Gán nhiều đơn hàng tới cùng một khách hàng cho một xe

Nhà vận tải cần chốt lộ trình lần lượt cho từng đơn hàng. 

* Bước 1. Vào tab **Đơn hàng bán**, chọn đơn hàng sẽ đi đầu tiên, sau đó chọn xe sẽ giao đơn hàng đó

- Bước 2. Di chuyển đến tab **Vận tải** để tối ưu lộ trình cho đơn hàng này

* Bước 3. Sau khi tối ưu lộ trình, cần nhấn nút **Chốt lộ trình** cho đơn hàng này. Đây là bước cực kỳ quan trọng

- Bước 4. Quay trở lại tab **Đơn hàng bán**, gán đơn hàng thứ hai cho cùng xe đã giao đơn hàng đầu tiên

* Bước 5. Di chuyển đến tab **Vận tải** để tối ưu lộ trình cho đơn hàng thứ hai.\
  Bắt đầu từ đơn hàng thứ hai, sẽ xuất hiện thêm trường **Thời gian xuất phát** ở biểu mẫu tối ưu lộ trình.\
  Nhà vận tải cần tự chọn Thời gian xuất phát cho đơn hàng thứ hai này vào thời điểm muộn hơn thời điểm kết thúc được tối ưu hóa của đơn hàng đầu tiên.\
  VD: Đơn hàng đầu tiên có Thời gian kết thúc tối ưu là 09:30. Nhà vận tải cần chọn Thời gian xuất phát của đơn hàng thứ hai sau đó, có thể là 10:00 hoặc 10:30\
  Nếu người điều phối không chọn Thời gian xuất phát, Abivin vRoute sẽ tự động đặt Thời gian xuất phát vào thời điểm 30 phút sau thời gian kết thúc được tối ưu hóa của đơn hàng đầu tiên

- Bước 6. Chốt lộ trình cho đơn hàng thứ hai

Tiếp tục thực hiện các bước từ Bước 4 đến Bước 6 cho các đơn hàng còn lại trong nhóm đơn hàng gán cho xe này
