---
title: Hướng dẫn cách viết Hướng dẫn sử dụng
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
## Quy trình viết doc tổng quát

**Bước 1**: Đọc tài liệu BA đính kèm trong task ClickUp để hiểu tổng quan tính năng. Có thể lăng xăng chạy đi hỏi để nắm rõ hơn. Mặt cần dày 1 chút\
**Bước 2**: Nghiên cứu xem nội dung HDSD tính năng nên để trong 1 doc đã có sẵn hay sẽ tách riêng 1 doc mới hoàn toàn. Kinh nghiệm xử lý như sau:\
1 - Nếu tính năng là 1 tính năng nhỏ đối với 1 tài nguyên cụ thể, các thao tác diễn ra trên 1 màn hình, ví dụ như: Lock route trên Map View; Master Filter => Sẽ để nội dung tính năng vào doc tổng của tài nguyên đó, cụ thể là doc Route Plan Optimization (Map View) và Manage Sales Orders\
2 - Nếu tính năng có nội dung khá lớn, nhiều thao tác trên nhiều màn hình, ví dụ 3D Loading (Bật config, nhập số liệu tài nguyên Sản phẩm, Xe; khởi tạo 3D loading) => Viết riêng 1 doc. Trong doc sẽ có link về các doc quản lý tài nguyên gốc để người đọc tham chiếu quy cách nhập từ doc gốc\
**Bước 3**: Liên hệ tester trực tiếp test tính năng để lấy thông tin môi trường nơi dev sẽ đẩy tính năng lên (d mấy, vd vroute.d8.abivin.vn)\
**Bước 4**: (Sau khi front, back end và algo đã đẩy hòm hòm code lên môi trường) Vào môi trường test tính năng, dịch giao diện. thử thao tác sau đó draft vào doc tính năng đó\
Trong bước này sẽ chưa thể viết được hoàn chỉnh doc vì thường sẽ có rất nhiều thay đổi, chưa ổn định. Để chắc chắn, hãy định hình sẵn khung nội dung trong đầu và trên doc, chờ tới khi tính năng được đẩy lên cotest thì mới tiến hành viết chi tiết hơn\
**Bước 5**: Xem bản preview của doc và dịch doc. Đối với những doc hoàn toàn mới, chưa publish vội mà chờ tới đợt deploy tính năng thì mới publish\
**Bước 6**: Nghe chửi, ngồi khóc xong cười rồi sửa doc

## Kết cấu doc

**Phần 1**: Đoạn giới thiệu ngắn về vấn đề phát sinh trong nghiệp vụ logistics thực tế và tính năng tương ứng trong Abivin vRoute để hỗ trợ giải quyết vấn đề đó\
**Phần 2**: Các thiết lập cần thực hiện: Bật tắt cái gì ở đâu, bổ sung thông tin gì cho những tài nguyên nào v.v\
**Phần 3**: Quá trình thao tác và kết quả thực tế của tính năng. Trong phần này, nếu như có nhiều tình huống thì cần mô tả cách để tái hiện từng tình huống\
Tip: Sử dụng header để tách các phân đoạn trong doc, gọi là header-ception
