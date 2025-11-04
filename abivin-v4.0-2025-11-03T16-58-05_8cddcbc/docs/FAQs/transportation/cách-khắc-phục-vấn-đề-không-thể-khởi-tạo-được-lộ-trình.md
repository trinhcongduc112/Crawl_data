---
title: Cách khắc phục vấn đề không thể khởi tạo được lộ trình
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
**Lý do 1:** Trọng lượng và thể tích của xe nhỏ hơn trọng lượng và thể tích của đơn hàng

* Giải quyết: Kiểm tra lại trọng tải và thể tích của xe để đảm bảo trọng tải và thể tích của xe lớn hơn hoặc bằng trọng tải và thể tích của đơn hàng
* Các bước để kiểm tra trọng lượng và thể tích của xe

- Bước 1: Đăng nhập bằng tài khoản
- Bước 2: Chọn Vận Tải
- Bước 3: Nhấp vào nút [Chỉnh sửa] của xe cần kiểm tra

![782](https://files.readme.io/2151a96-1.png "1.png")

**Lý do 2:** Khách hàng, kho không có vĩ độ, kinh độ

* Giải quyết: Thêm vĩ độ, kinh độ cho khách hàng và kho
* Các bước thêm vĩ độ, kinh độ khi khách hàng không có vĩ độ, kinh độ

- Bước 1: Vào Đối tác
- Bước 2: Nhấp vào nút hỉnh sửa] c của khách hàng cần thêm vĩ độ, kinh độ
- Bước 3: Nhấn Thêm cấu hình ở màn hình Chỉnh sửa khách hàng và thêm kinh độ, vĩ độ của khách hàng
- Bước 4: Nhấn Lưu lại

![2870](https://files.readme.io/15e4662-3.png "3.png")

**Lí do 3:** Khoảng thời gian hoạt động của xe và Khoảng thời gian hoạt động của khách hàng trong ngày không trùng nhau\
Ví dụ: Thời gian hoạt động của xe từ 8 giờ sáng đến 8 giờ tối, thời gian hoạt động của khách hàng từ 9 giờ tối đến 11 giờ tối

* Giải quyết: Chọn xe đi đến khách hàng có khoảng thời gian hoạt động trùng nhau.\
  Ví dụ: thời gian hoạt động của xe từ 8h sáng đến 9h tối thì tương thích với khách hàng có thời gian hoạt động từ 10h sáng đến 9h tối
* Các bước để xem thời gian hoạt động của xe:

- Bước 1: Vào Vận Tải
- Bước 2: Nhập thời gian hoạt động của xe

![800](https://files.readme.io/9d91d21-4.png "4.png")

Cách xem thời gian hoạt động của Khách hàng:\
Bước 1: Vào Đối tác\
Bước 2: Nhấp vào nút  sửa] của k của khách hàng cần kiểm tra\
Bước 3: Nhấn Thêm cấu hình và kiểm tra thời gian hoạt động của khách hàng

![2876](https://files.readme.io/77a2c8c-5.png "5.png")

**Lí do 4:** Cấu hình sai thời gian bắt đầu, thời gian kết thúc, thời gian bắt đầu nghỉ trưa, thời gian kết thúc nghỉ trưa của xe\
Ví dụ Cấu hình sai thời gian bắt đầu 8, thời gian kết thúc 20:0

* Giải quyết: Cấu hình theo đúng quy định\
  Ví dụ: Thời gian bắt đầu 6:00, thời gian kết thúc 23:59

![801](https://files.readme.io/c0aa9b7-6.png "6.png")

**Lí do 5:** Chưa chọn loại xe (xe máy, xe tải, xe container) cho tài xế và xe không tích vào ô hoạt động

* Giải quyết:

- Khi upload hoặc khi tạo trực tiếp người dùng (tài xế) cần nhập loại phương tiên (xe máy, xe tải, xe container)\
  Khi kiểm tra màn hình tài xế chưa có loại phương tiện thì cần thêm vào như sau:
  * Bước 1: Vào Tổ Chức và nhấn vào người dùng
  * Bước 2: Nhấn vào nút chỉnh sửa (hình cây bút ) của tài xế cần thêm xe
  * Bước 3: Nhấn Thêm cấu hình và chọn loại xe cho tài xế
  * Bước 4: Nhấn Lưu lại

![1247](https://files.readme.io/fd687a4-7.png "7.png")

Kiểm tra tài xế đã có loại phương tiện chưa:

* Bước 1: Vào Vận tải và chọn tài xế
* Bước 2: Kiểm tra tài xế phải có kiểu xe và có nút hoạt động phải được tích

![1238](https://files.readme.io/de8f3b8-8.png "8.png")

**Lí do 6:** Nhiều đơn hàng cùng đi đến 1 khách hàng, khi lên lộ trình hệ thống sẽ tối ưu và dồn các đơn hàng đó vào 1 xe nên khối lượng xe được hệ thống chọn lên lộ trình sẽ bị nhỏ hơn trọng lượng các đơn hàng

* Giải quyết: Khi có nhiều đơn cùng đi đến 1 khách hàng thì tích vào ô đơn chẻ của tất cả các đơn cùng đi đến 1 khách hàng

![1246](https://files.readme.io/f04e995-9.png "9.png")

**Lí do 7:** Khách hàng ở xa, lộ trình giao hàng và về kho của xe phải đi hơn 1 ngày thì hệ thống sẽ báo lỗi dữ liệu

* Giải quyết: Mở thời gian hoạt động của xe  lớn hơn 24 giờ\
  Ví dụ:\
  Opening the start time of the vehicle is 7:00, the end time of the vehicle is 150:00

![801](https://files.readme.io/d4af531-10.png "10.png")

**Lí do 8:** Chưa gán xe cho đơn hàng khi lên lộ trình hệ thống sẽ thông báo: kiểm tra dữ liệu đầu vào

* Giải quyết:

- Bước 1: Vào đơn hàng
- Bước 2: Tích vào ô vuông đầu đơn hàng cần gán xe
- Bước 3: Nhấn đến phương tiện và chọn xe
- Bước 4: Nhấn Gán
- Bước 5: Vào Vận tải và lên lộ trình

![1264](https://files.readme.io/cbf5098-11.png "11.png")

**Lí do 9:** Định dạng thời gian tối thiểu, thời gian tối đa của kho xuất hàng sai (giây, giờ). Định dạng đúng là phút

* Giải quyết: Kiểm tra lại định dang thời gian tối đa, thời gian tối thiểu và đưa về đúng định dạng là phút

- Bước 1: Vào Tổ Chức
- Bước 2:Nhấn icon chỉnh sửa (hình cây bút) của kho xuất hàng và nhấn Thêm cấu hình
- Bước 3: Nhập thời gian tối đa và thời gian tối thiểu là một số nguyên và lớn hơn 0
- Bước 4: Nhấn Lưu lại

![2868](https://files.readme.io/d01373d-12.png "12.png")
