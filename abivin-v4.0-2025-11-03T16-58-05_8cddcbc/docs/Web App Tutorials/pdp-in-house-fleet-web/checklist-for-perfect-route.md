---
title: Checklist for perfect route
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
Khi nhân viên điều phối khởi tạo lộ trình, trong trường hợp không sử dụng cấu hình thuật toán nào trong hệ thống thì 1 lộ trình hoàn hảo cần đảm bảo các tiêu chí dưới đây:

## Check Assignments

**Vehicle - Customer: Kiểm tra phương tiện liên kết với khách hàng thông qua MDP**

* Mỗi khách hàng được gán cho mỗi xe thông qua mã MDP, mã MDP của xe và khách hàng trùng khớp thì xe đó sẽ nhận biết được khách hàng thân thuộc thông qua mã MDP được khai báo.

**Vehicle - Driver: Kiểm tra xe được gán với tài xê trong mỗi ca** 

* Một ca được gán cho một driver. Xe và tài xế trong ca làm việc phải tương thích
* Chỉ có 1 driver được chỉ định cho mỗi ca làm việc của xe. 1 tài xế có thể chỉ định cho 1 xe có nhiều ca làm việc thông qua gán mặc định tài xế cho mỗi xe.

## Check Time

**Thời gian giữa phương tiện - Tài xế** 

* Thời gian làm việc của mỗi tài xế được xác định bằng mỗi ca làm việc.
* Trong mỗi ca được thực hiện bởi mỗi tài xế, thời gian giao hàng của mỗi xe bằng tổng thời gian di chuyển bắt đầu từ kho đến các điểm giao hàng và quay lại kho
* Thời gian giao hàng của mỗi xe không được dài hơn thời gian lái xe tối đa được cho phép của mỗi tài xế ( \<= Stop Time của mỗi xe)

**Thời gian giữa Phương tiện - Khách hàng - Đơn hàng - Tài xế** 

* Hoạt động giao hàng được thực hiện trong giờ mở/đóng cửa của khách hàng.
* Đối với tất cả các hoạt động, khoảng thời gian đến và đi (Reaching Time) của mỗi khách hàng phải nằm trong khoảng thời gian mở/đóng cửa của khách hàng.
* Khung thời gian của đơn hàng được giao cho mỗi khách hàng  phải nằm trong khoảng thời gian mở/đóng cửa của khách hàng đó
* Khoảng thời gian giữa 2 ca làm việc liên tiếp của mỗi xe phải cách nhau ít nhất 30 phút

## Các điều kiện lộ trình hoàn hảo

![1919](https://files.readme.io/6820873-img1.png "img1.png")

1. Các đơn hàng đảm bảo đều vào được lộ trình, không bị rớt
2. Tỉ lệ đầy xe: Các xe đảm bảo giao các đơn hàng hết thời gian làm việc, đầy về mặt khối lượng/thể tích ( tỉ lệ đầy: 90-100%).\
   Lộ trình đang ưu tiên giao cho các xe có capacity nhỏ trước, nếu 1 xe đã giao đầy đơn mà hết thời gian làm việc thì lượng đơn còn lại sẽ được phân chia cho các xe còn lại.
3. Thứ tự giao hàng: Xe ưu tiên giao đến các điểm gần kho trước, sau đó đi đến các điểm tiếp theo thỏa mãn quãng đường giữa 2 điểm liên tiếp là gần nhau
4. Các xe giao hàng đảm bảo giao các đơn hàng không vượt quá sức chứa về trọng lượng, thể tích (tỉ lệ đầy tối đa là 100%)
5. Nếu trọng lượng/thể tích của các đơn hàng vượt quá sức chứa của xe nhưng trong trường vẫn đủ thời gian thì có thể quay về kho để lấy hàng và tiếp tục giao hàng.
6. Đường đi giữa các xe: Đường đi giữa các xe hạn chế chồng lấn nhau, trong trường hợp chồng lấn 1 số điểm thì điều phối viên cần phải kéo đơn thủ công để hạn chế.
7. Thời gian giao hàng của xe: Trong phạm vi thời gian làm việc của xe đã khai báo.

## Độ thân thuộc

Khi người điều phối muốn gán các cụm khách hàng cho 1 xe giao trong khu vực thân thuộc  thì sử dụng cấu hình Độ thân thuộc.\
Độ thân thuộc luôn ưu tiên các xe giao đến các khách hàng thân thuộc trước, trong trường hợp còn thời gian thì sẽ giao các khách hàng khác không thân thuộc để đảm bảo tỉ lệ đầy xe.\
Độ thân thuộc hoàn hảo từ 90-100% cho mỗi xe

![1918](https://files.readme.io/d5adfd7-dtt.png "dtt.png")

## Cụm địa lý

Để hạn chế các xe giao chồng lấn giữa các tuyến đường, nhân viên điều phối có thể sử dụng cấu hình chia theo cụm để hạn chế tối đa chồng lấn đường đi giữa các xe, phân các khách hàng theo các cụm mà không vi phạm vượt quá sức chứa (trọng lượng/thể tích) của các xe.\
Chia theo cụm thuật toán sẽ bỏ qua phần đảm bảo tổng chi phí thấp nhất mà ưu tiên các giải quyết phần cắt nhau của lộ trình các xe. Kết quả là các xe sẽ được chia theo cụm.

![1918](https://files.readme.io/7eca32d-clustering.png "clustering.png")

Khi chia theo cụm thì các đơn vào lộ trình vẫn thỏa mãn tỉ lệ đầy xe.\
\* *Lưu ý: Không thể kết hợp chia theo cụm và độ thân thuộc.*
