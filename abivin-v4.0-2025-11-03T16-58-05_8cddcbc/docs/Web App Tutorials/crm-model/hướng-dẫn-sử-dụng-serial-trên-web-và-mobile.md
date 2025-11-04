---
title: Hướng dẫn sử dụng serial trên web và mobile
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
## 1. Số Serial ở màn hình Tạo mới liên hệ

* Áp dụng với trường hợp Xóa Khách hàng đã được gán số serial, Người dùng có thể tạo lại khách hàng và gán lại số serial.

## 2. Số Serial ở màn hình Chỉnh sửa khách hàng

* Hệ thống cho phép Chỉnh sửa/thêm số serial ở màn hình Chỉnh sửa khách hàng.\
  Đăng nhập vào hệ thống => Chọn Đối tác => Chọn Khách hàng cần chỉnh sửa => Chọn Icon Chỉnh sửa => Nhập các thông tin cần chỉnh sửa, Nhập thêm/chỉnh sửa số Serial => Chọn Lưu lại\
  \=> Hệ thống Lưu lại toàn bộ thông tin chỉnh sửa vừa nhập.
* **Điều kiện nhập thêm/chỉnh sửa số Serial:** Số serial chưa tồn tại trong hệ thống, nếu muốn nhập nhiều số serial thì các số serial sẽ được ngăn cách nhau bởi dấu phẩy. 
* **Lưu ý:** chỉ dùng để thêm số serial cũ của khách hàng mà trước đây chưa được cập nhật trên hệ thống.

## 3. Số Serial ở màn hình Tạo mới tác vụ

Khi tạo mới tác vụ, trình tự nhập thông tin như sau:\
B1: Chọn Action\
B2: Nhập các thông tin khác trên form tạo mới\
B3: Nhấn nút Lưu\
**\* Đối với Action Lắp đặt**

* Khi tạo mới tác vụ bằng tay, trong form Tạo mới tác vụ action Lắp mới sẽ không có trường số Serial.\
  **\* Đối với các Action khác**
* Khi tạo mới tác vụ bằng tay, trong form Tạo mới tác vụ các action khác sẽ có trường số Serial. Người dùng chọn số serial có sẵn trong hệ thống của khách hàng đó gán cho tác vụ. Số serial được gán sẽ hiển thị trong tác vụ đó trên mobile. 

## 4. Số Serial khi Import tác vụ

Người dùng có thể import số serial theo tác vụ\
**\* Đối với tác vụ Lắp đặt:** 

* Tác vụ ở trạng thái “Mở”: Số serial sẽ chỉ gán cho tác vụ và chưa được gán cho khách hàng. Khi người dùng mobile hoàn thành trên mobile số Serial mới được gán cho khách hàng.
* Tác vụ ở trạng thái “Hoàn thành”: Số serial sẽ được gán cho tác vụ và được gán luôn cho khách hàng đó, Số serial bắt buộc phải nhập.

- Điều kiện import số Serial: số Serial chưa tồn tại trên hệ thống, không import hơn 1 tác vụ lắp mới cùng số serial trong cùng 1 file import.\
  **\* Đối với các tác vụ khác:** Số serial sẽ được gán cho tác vụ.
- Điều kiện import số Serial: Số Serial đã tồn tại trên hệ thống và số serial gán cho tác vụ đã được gán cho khách hàng của tác vụ đó.

## 5. Số Serial khi Gửi trên mobile

**\* Đối với tác vụ Lắp đặt**

* Để hoàn thành tác vụ Lắp đặt, người dùng phải nhập các trường bắt buộc bao gồm phải nhập cả số Serial
* Điều kiện nhập số Serial: Là số Serial chưa tồn tại trên hệ thống.
* Các trường hợp sai: Người dùng nhập số serial đã được gán cho khách hàng khác trên hệ thống, hoặc không nhập số serial đã gửi tác vụ.\
  **\* Đối với các tác vụ khác**
* Để hoàn thành các task vụ khác, người dùng phải nhập các trường bắt buộc trên form, ở các tác vụ khác thường đã có số serial khi Tạo tác vụ người dùng web đã gán số serial của khách hàng cho task vụ đó.
* Điều kiện nhập số Serial: Người dùng mobile phải nhập số Serial đúng với số Serial đã được gán cho khách hàng đó trên web.
* Các trường hợp sai: Tác vụ đó chưa được gán số Serial, người dùng mobile nhập số serial chưa tồn tại trên web, hoặc số serial không thuộc khách hàng của tác vụ đó.
