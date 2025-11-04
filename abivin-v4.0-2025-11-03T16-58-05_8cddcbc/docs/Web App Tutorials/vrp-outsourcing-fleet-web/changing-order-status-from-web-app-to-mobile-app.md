---
title: Chuyển tình trạng đơn hàng giữa Web app và Mobile app
excerpt: >-
  Đơn hàng sau khi lên lộ trình sẽ ở tình trạng đặt hàng là: Mở. Kho và tài xế
  chuyển tình trạng đặt hàng sau khi nhà vận tải lên lộ trình và chốt lộ trình.
  Các Kho Và Nhà vận tải bắt buộc phải thực hiện việc chuyển tình trạng đặt hàng
  theo quy trình hướng dẫn bên dưới.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
\*\*\* TRƯỜNG HỢP ĐƠN HÀNG CÓ CẢ CHIỀU ĐI VÀ CHIỀU VỀ\
1> Tài xế đến kho lấy hàng thành phẩm đi giao cho khách hàng thì Kho lấy hàng có nhiệm vụ chuyển tình trạng đặt hàng trên web từ Mở sang đã nhặt và sắp hàng và tài xế có nhiệm vụ gửi tác vụ Soạn hàng thực hiện trên mobile

* Kho thực hiện trên web\
  Nếu số lượng thùng hàng thành phẩm thực tế ở chiều đi lớn hơn hoặc nhỏ hơn số lượng thùng kế hoạch ở trong đơn hàng thì kho xuất hàng sẽ nhập vào ô số lượng thùng thực tế  và nhấn Lưu lại

![1334](https://files.readme.io/352c33e-Screenshot_7.png "Screenshot_7.png")

Bước 1: Đăng nhập bằng tài khoản Kho\
Bước 2: Vào Đơn hàng và nhấn vào icon chỉnh sửa ( hình cây bút) của đơn hàng\
Bước 3: Nhấn vào gạch ngang phía dưới tình trạng đặt hàng và chọn Đã nhặt và sắp hàng ở Chiều đi\
Bước 4: Nhấn Lưu

![1354](https://files.readme.io/9f08371-Screenshot_1.png "Screenshot_1.png")

* Tài xế thực hiện trên app điện thoại

![388](https://files.readme.io/334e6e9-Screenshot_1.png "Screenshot_1.png")

2> Đến khách hàng tài xế thực hiện tác vụ Giao hàng trên app điện thoại.\
2.1 Chiều đi

* Nếu giao cho khách đủ số lượng hàng số lượng mang đi thì tích vào Hoàn thành
* Nếu giao cho khách hàng số lượng ít hơn số lượng mang đi thì tích vào Giao 1 phần
* Nếu vì lí do nào đó mà không giao được cho khách hàng thì tích vào Không hoàn thành và chọn lí do

![348](https://files.readme.io/2d91aee-Screenshot_2.png "Screenshot_2.png")

* Sau khi tài xế Gửi tác vụ giao hàng trên app điện thoại thì trên web sẽ tự động cập nhật tình trạng giao hàng

- TH1: Tài xế chọn trạng thái giao hàng là hoàn thành và gửi tác vụ giao hàng thì ở trên web sẽ tự động cập nhật tình trạng đặt hàng từ đã nhặt và sắp sang đã chuyển hàng với tình trạng hoàn thành là hoàn thành

![1332](https://files.readme.io/efc711c-Screenshot_3.png "Screenshot_3.png")

+TH2: Tài xế chọn trạng thái giao hàng là giao 1 phần  và gửi tác vụ giao hàng thì ở trên web sẽ tự động cập nhật tình trạng đặt hàng từ đã nhặt và sắp sang đã chuyển hàng với tình trạng hoàn thành là hoàn thành 1 phần 

![1330](https://files.readme.io/23a2e2f-Screenshot_4.png "Screenshot_4.png")

* TH3: Tài xế chọn trạng thái giao hàng là không hoàn thành và gửi tác vụ giao hàng thì ở trên web sẽ tự động cập nhật tình trạng đặt hàng từ đã nhặt và sắp sang đã chuyển hàng với tình trạng hoàn thành là chưa hoàn thành

![1344](https://files.readme.io/02b7ca8-Screenshot_8.png "Screenshot_8.png")

2.2 Chiều về

* Sau khi tài xế gửi tác vụ giao hàng trên mobile thì trên web sẽ tự động cập nhật tình trạng giao hàng của chiều về từ mở sang đã nhặt và sắp

- TH1: tài xế gửi tác vụ giao hàng chiều về với tình trạng giao hàng là hoàn thành hoặc không hoàn thành thì trên web sẽ hiển thị tình trạng đặt hàng là đã nhặt và sắp với tình trạng hoàn thành là không hoàn thành và số lượng ở cột số lượng thùng thực tế sẽ bằng với số lượng thùng kế hoạch

![1331](https://files.readme.io/8b5757f-Screenshot_9.png "Screenshot_9.png")

* TH2:  tài xế gửi tác vụ giao hàng chiều về với tình trạng giao hàng là giao 1 phần thì trên web sẽ hiển thị tình trạng đặt hàng là đã nhặt và sắp với tình trạng hoàn thành là không hoàn thành và số lượng ở cột số lượng thùng thực tế sẽ là số lượng thùng mà tài xế đã chọn trên mobile

![1339](https://files.readme.io/4d916cc-Screenshot_10.png "Screenshot_10.png")

* Sau khi tài xế đem hàng vỏ về kho thì kho sẽ có nhiệm vụ chuyển tình trạng đặt hàng từ đã nhặt và sắp sang đã chuyển hàng

- TH1: Kho nhận đủ số thùng hàng vỏ theo kế hoạch thì kho sẽ chuyển tình trạng đặt hàng sang đã chuyển hàng với tình trạng hoàn thành là hoàn thành

![1334](https://files.readme.io/9509313-Screenshot_11.png "Screenshot_11.png")

* TH2: Kho nhận lớn hơn hay nhỏ hơn số thùng vỏ so với kế hoạch thì kho sẽ chuyển tình trạng đơn hàng sang đã nhặt và sắp với tình trạng hoàn thành là hoàn thành 1 phần và kho sẽ nhập số lượng thùng vỏ mà kho nhận thực tế vào ô số lượng thùng được giao

![1332](https://files.readme.io/468f150-Screenshot_12.png "Screenshot_12.png")

* TH3: Khách hàng không có vỏ cho tài xế mang về, kho sẽ chuyển tình trạng đơn hàng thành đã chuyển hàng với tình trạng hoàn thành là chưa hoàn thành 

![1333](https://files.readme.io/9ca0e6b-Screenshot_13.png "Screenshot_13.png")

\*\*\* TRƯỜNG HỢP ĐƠN HÀNG CHỈ CÓ CHIỀU ĐI\
1> Khi tài xế đến kho lấy hàng thành phẩm đi giao cho khách hàng kho sẽ nhập số lượng hàng thực tế xuất đi vào ô số lượng thùng thực tế và chuyển tình trạng đặt hàng sang đã nhặt và sắp 

* Tài xế có nhiệm vụ gửi tác vụ giao hàng trên mobile

![1326](https://files.readme.io/0ae1e96-Screenshot_14.png "Screenshot_14.png")

2> Đến khách hàng tài xế có nhiệm vụ gửi tác vụ giao hàng trên mobile 

* Sau khi tài xế gửi tác vụ giao hàng trên mobile thì trên web sẽ tự động cập nhật tình trạng đặt hàng từ đã nhặt và sắp sang đã chuyển hàng với tình trạng hoàn thành hiển thị theo tài xế gửi tác vụ là hoàn thành, giao 1 phần, chưa hoàn thành 

![1340](https://files.readme.io/5556d05-Screenshot_15.png "Screenshot_15.png")

\*\*\* TRƯỜNG HỢP ĐƠN HÀNG CÓ CHIỀU VỀ\
1> Tài xế đến khách hàng lấy hàng vỏ chiều về thì tài xế sẽ có nhiệm vụ gửi tác vụ soạn hàng và giao hàng trên mobile\
2> Sau khi tài xế gửi tác vụ giao hàng thì trên web sẽ tự động cập nhật tình trạng đặt hàng từ mở sang đã nhặt và sắp 

![1347](https://files.readme.io/b2ae52a-Screenshot_16.png "Screenshot_16.png")

3> Tài xế mang hàng vỏ từ khách hàng về kho thì kho sẽ có nhiệm vụ chuyển tình trạng đặt hàng từ đã nhặt và sắp sang đã chuyển hàng 

* TH1: Nếu kho nhận đủ số thùng vỏ so với kế hoạch thì kho sẽ chuyển tình trạng đặt hàng sang đã chuyển hàng và chọn tình trạng hoàn thành là hoàn thành
* TH2: Khách hàng không có hàng vỏ trả cho kho thì kho sẽ chuyển tình trạng đặt hàng sang đã chuyển hàng và chọn tình trạng hoàn thành là chưa hoàn thành
* TH3: Kho nhận lớn hơn hoặc nhỏ hơn số thùng vỏ so với kế hoạch thì kho sẽ chuyển tình trạng đơn hàng sang đã chuyển hàng, chọn tình trạng hoàn thành là hoàn thành 1 phần và nhập số lượng thùng thực tế nhận được vào ô số lượng thùng được giao

![1350](https://files.readme.io/0287b6d-Screenshot_17.png "Screenshot_17.png")
