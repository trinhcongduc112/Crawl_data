---
title: Đơn hàng lớn
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
Đơn hàng lớn là loại đơn được lên kế hoạch để thực hiện trong một khoảng thời gian nhiều hơn một ngày, có thể chia thành nhiều đơn hàng nhỏ hơn

## Tạo đơn hàng lớn

* Di chuyển đến tab **Đơn hàng > Đơn hàng lớn**
* Di chuột vào biểu tượng :fa-plus-circle:, nhấn vào nút **Tạo đơn hàng lớn:fa-pencil:**

<Image title="DHL1.png" alt={1674} className="border" border={true} src="https://files.readme.io/ae4f6dc-DHL1.png" />

* Ở cửa sổ **Tạo đơn hàng lớn**, điền thông tin đơn hàng vào các trường như sau
* **Mã đơn hàng**: Hệ thống sẽ tự động sinh mã đơn hàng. Người tạo đơn có thể điền mã đơn hàng theo cấu trúc thường sử dụng vào đây
* **Ngày bắt đầu và kết thúc**: Nhấn vào trường này, nhấn chọn hoặc gõ *Ngày bắt đầu* ở lịch bên trái, sau đó nhấn chọn hoặc gõ *Ngày kết thúc* ở lịch bên phải. Nhấn **Đồng ý** để hoàn tất tạo thời gian thực hiện đơn hàng lớn
* **Mã khách hàng**: Gõ *Mã tổ chức* của chính Kho MTV đang tạo đơn, hoặc *Mã đại lý* của đại lý sẽ  trực tiếp nhận sản phẩm từ Kho sản xuất

> 📘 Mã tổ chức của có thể tìm ở tab **Tổ chức > Danh sách tổ chức**\
> Mã đại lý khách hàng có thể tìm ở tab **Đối tác > Danh sách khách hàng**

* **Loại chiều**: Chọn *1 chiều* nếu đơn hàng chỉ có chiều đi (Chiều đi là chiều vận chuyển thành phẩm từ kho sản xuất tới kho một thành viên hoặc kho đại lý khách hàng); hoặc *2 chiều* nếu đơn hàng có cả chiều đi và chiều về (Chiều về là chiều vận chuyển vỏ chai, bao bì từ kho đại lý về kho sản xuất)
* **Đơn hàng nhận**: Nhấn chọn ô này nếu như đơn hàng là loại đơn một chiều chỉ có chiều về
* **Sản phẩm**: Nhấn vào trường tìm kiếm sản phẩm (Nằm bên dưới tab **Chiều đi | Chiều về**, gõ *Mã sản phẩm* của sản phẩm cần tạo đơn, sau đó nhấn **Thêm**. Tiếp tục điền các thông tin cần thiết của sản phẩm vào các ô bên cạnh: *Số lượng thùng trong đơn, Số lượng sản phẩm lẻ, Số lượng sản phẩm/thùng, Giá thùng, Giá sản phẩm lẻ, Thành tiền, Ngày hết hạn, Số lô*

> 📘 Mã sản phẩm có thể tìm ở tab **Sản phẩm > Sản phẩm**

* Sau khi đã nhập đầy đủ thông tin của đơn hàng, nhấn **Lưu lại** để hoàn tất tạo đơn hàng lớn. Nếu không muốn tạo đơn hàng lớn, nhấn **Hủy**

## Phê duyệt đơn hàng lớn

**Tài khoản thực hiện: Công ty MTV duyệt đơn**

* Di chuyển đến tab **Đơn hàng > Đơn hàng lớn**
* Danh sách các đơn hàng lớn mới tạo, chưa được phê duyệt sẽ hiện ra và được làm nổi bật bằng màu xám
* Duyệt một đơn: Admin Công ty MTV có thể phê duyệt đơn bằng cách nhấn vào nút **Phê duyệt:fa-check:** ở cuối mỗi đơn

<Image title="DHL2.png" alt={1673} className="border" border={true} src="https://files.readme.io/f27bc00-DHL2.png" />

* Duyệt nhiều đơn: Admin có thể duyệt nhiều đơn bằng cách nhấn vào ô :fa-square-o: bên cạnh các đơn hàng muốn duyệt. Các đơn hàng được chọn sẽ chuyển sang ô :fa-check-square-o:. Sau đó admin có thể nhấn vào nút **Phê duyệt** ở thanh công cụ phía trên

<Image title="DHL3.png" alt={1666} className="border" border={true} src="https://files.readme.io/ef927d9-DHL3.png" />

* Sau đó admin cần nhấn vào nút **OK** ở thông báo **Are you sure to approve order...** hiện ra
* Các đơn hàng được phê duyệt thành công sẽ có thông báo

![314](https://files.readme.io/7b3ef9c-DHL4.png "DHL4.png")

## Gán kho sản xuất và nhà vận tải

**Tài khoản thực hiện: Tổng công ty**

* Di chuyển đến tab **Đơn hàng > Đơn hàng lớn**
* Nhấn vào đơn hàng lớn cần gán kho và nhà vận tải
* Nhấn vào trường **Mã kho** và **Mã Nhà vận tải**, lần lượt chọn Kho sản xuất và Nhà vận tải từ danh sách xổ xuống
* Nhấn **Lưu lại** để hoàn tất việc gán kho sản xuất và nhà vận tải

> ❗️ Sau khi đã chọn **Mã kho**, **Mã Nhà vận tải** và nhấn **Lưu lại**, hệ thống sẽ khóa và không cho phép thay đổi giá trị sản phẩm trong đơn hàng, trên bất kỳ tài khoản nào

## Chia đơn hàng lớn và gán xe vận chuyển

**Tài khoản thực hiện: Nhà vận tải được tổng công ty gán thực hiện đơn**

* Di chuyển đến tab **Đơn hàng > Đơn hàng lớn**
* Nhấn vào nút **Chia đơn ⊕**
* Ở màn hình **Chia đơn hàng lớn**: 
* Nhấn vào trường **Ngày đơn hàng**, chọn ngày thực hiện đơn nhỏ được chia ra từ đơn hàng lớn. Có thể chọn một ngày trong tương lai, miễn là trong phạm vi những ngày thực hiện đơn hàng lớn
* Gõ số lượng thùng nguyên và sản phẩm lẻ muốn chia cho đơn nhỏ vào các trường **Chia số thùng** và **Chia số lẻ**. Giá trị ở các trường **Sô thùng còn lại** và **Số lẻ còn lại** sẽ giảm tương ứng theo giá trị đã chia cho đơn nhỏ

> 📘 Nhà vận tải không cần phải chia hết đơn hàng lớn trong một lần chia. Việc chia đơn hàng lớn có thể thực hiện trong nhiều lần, miễn là chưa hết ngày thực hiện đơn hàng lớn

* Nhấn **Chia** để hoàn tất việc chia đơn hàng lớn. Đơn hàng nhỏ vừa được chia sẽ xuất hiện ở dưới cột **Danh sách đơn chia**. Định dạng Mã Đơn hàng nhỏ = Mã đơn hàng lớn + # + số thứ tự của đơn hàng nhỏ được chia. VD: Đơn hàng lớn có mã BO\_v1, thì các đơn hàng nhỏ sẽ có mã BO\_v1#1, BO\_v1#2 
* Nếu đơn hàng lớn có cả chiều đi và chiều về thì cần nhấn vào tab tương ứng để chia đơn trước khi nhấn **Chia**
* Nếu muốn xóa đơn hàng nhỏ vừa chia, có thể nhấn vào nút :fa-times-circle: ở cạnh mã đơn đó
* Nhấn **Lưu** để hoàn tất lần chia đơn hàng. Các đơn hàng nhỏ đã được chia sẽ xuất hiện ở tab **Đơn hàng > Đơn hàng bán** vào ngày đã chia tương ứng
* Nhà vận tải có thể tiến hành gán xe cho các đơn hàng nhỏ đã chia tương tự như với đơn hàng bán thông thường

## Thay đổi ngày thực hiện đơn hàng lớn

* Nếu nhận thấy ngày thực hiện đơn hàng lớn ban đầu không phù hợp, nhà vận tải (hoặc tổng công ty) có thể thay đổi ngày thực hiện đơn hàng lớn bằng cách nhấn vào nút **Chỉnh sửa:fa-pencil:** tương ứng của đơn đó. Sau đó, thay đổi *Ngày bắt đầu* và *Ngày kết thúc* bằng ngày phù hợp hơn

> ❗️ Sau khi nhà vận tải đã chia đơn, Tổng công ty sẽ không thể chọn lại **Mã kho** và **Mã Nhà vận tải** của đơn hàng lớn

## Xem tuyến vận tải của đơn hàng

* Sau khi nhà vận tải đã lên lộ trình cho đơn hàng, các tài khoản liên quan đến đơn có thể theo dõi tuyến vận tải của đơn hàng bằng cách nhấn vào nút **Xem tuyến vận tải:fa-eye:** tương ứng của đơn hàng

<Image title="DHL6.png" alt={1672} className="border" border={true} src="https://files.readme.io/86ba217-DHL6.png" />

* Một tab khác trên trình duyệt web sẽ mở ra, hiển thị bản đồ vận tải cùng tuyến vận tải của đơn hàng

<Image title="DHL5.png" alt={1680} className="border" border={true} src="https://files.readme.io/39c9c9a-DHL5.png" />

## Xóa đơn hàng nhỏ

* Sau khi đơn hàng lớn đã chia và lưu lại, nhà vận tải vẫn có thể xóa đơn hàng nhỏ đã được chia bằng cách di chuyển đến tab **Đơn hàng > Đơn hàng bán**, chọn ngày đã lên lịch thực hiện đơn hàng nhỏ, nhấn vào nút **Xóa:fa-times:** tương ứng của đơn hàng nhỏ đó
* Giá trị đã chia cho đơn hàng vừa xóa sẽ được cộng trở lại giá trị còn lại của đơn hàng lớn trước khi chia, cho phép nhà vận tải chia lại
