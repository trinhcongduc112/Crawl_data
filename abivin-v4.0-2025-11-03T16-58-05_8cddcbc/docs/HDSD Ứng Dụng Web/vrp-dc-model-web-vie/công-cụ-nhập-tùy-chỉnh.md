---
title: Công cụ Nhập tùy chỉnh
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
* **Nhập tùy chỉnh** là một công cụ hữu ích trong ứng dụng Web của chúng tôi. Nó được phát triển để giúp người dùng chuyển đổi trực tiếp dữ liệu từ các định dạng dữ liệu độc quyền của họ sang các định dạng dữ liệu tiêu chuẩn Abivin vRoute mà không cần phải sử dụng các phương pháp tạo đối tượng thông thường (Biểu mẫu web; Mẫu Excel)
* Hiện tại, công cụ **Nhập tùy chỉnh** được phát triển để chuyển đổi các Tệp Đơn hàng (**Delivery Order**, viết tắt là **DO**, không theo định dạng Đơn hàng của hệ thống Abivin vRoute). Trong bài viết này, chúng tôi sẽ sử dụng từ viết tắt **Tệp DO** để nói đến **Tệp Đơn hàng**

## Điều kiện để sử dụng công cụ Nhập tùy chỉnh

* Để có thể sử dụng công cụ Nhập tùy chỉnh, bạn phải đảm bảo rằng bạn được cấp quyền hoặc bạn đã cấp quyền sử dụng công cụ Nhập tùy chỉnh cho các nhóm người dùng nhất định. Để cấp quyền sử dụng công cụ Nhập tùy chỉnh, vui lòng làm theo các bước sau
* Bước 1: Di chuyển đến tab **Tổ chức > Nhóm người dùng**
* Bước 2: Nhấp vào biểu tượng **Chỉnh sửa**  :fa-pencil: của Nhóm người dùng mà bạn muốn cấp quyền sử dụng công cụ Nhập tùy chỉnh\
  Bước 3: Một biểu mẫu có tên **Cập nhật nhóm** sẽ hiển thị trên màn hình. Trên tab **Thông tin chung**, cuộn xuống để tìm **Hồ sơ ánh xạ** và đánh dấu vào các ô chức năng mà bạn muốn cấp quyền sử dụng cho nhóm người dùng đã chọn. Vui lòng tham khảo liên kết này để biết thông tin chi tiết [Phần Mô-đun](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-users#modules-section)
* Bước 4: Nhấp vào **Lưu lại** để các thay đổi có hiệu lực.

<Image title="3. Mapping Profie (VIE).png" alt={1920} border={true} src="https://files.readme.io/09f1a64-3._Mapping_Profie_VIE.png">
  Illustration (Vietnamese)
</Image>

## Các bước để sử dụng công cụ Nhập tùy chỉnh

### Bước 1: Truy cập công cụ Nhập tùy chỉnh & Tải lên Tệp DO

* Để truy cập công cụ Nhập tùy chỉnh, trước tiên hãy di chuyển đến tab **Cài đặt > Nhập tùy chỉnh**. Trên tab này, di chuột vào biểu tượng dấu cộng màu cam :fa-plus-circle:, sau đó nhấp vào biểu tượng **Nhập dữ liệu**

<Image title="1. Custom Import (VIE) 2.png" alt={1920} border={true} src="https://files.readme.io/8c0c522-1._Custom_Import_VIE_2.png">
  Illustration (Vietnamese)
</Image>

* Biểu mẫu **Nhập tệp CSV/XLSX** sẽ hiện ra

<Image title="1. New CSV (VIE).png" alt={1274} border={true} src="https://files.readme.io/27e22ff-1._New_CSV_VIE.png">
  Illustration (Vietnamese)
</Image>

* Nhấn vào vùng **Kéo và thả một số tệp vào đây hoặc nhấn vào để chọn tệp**, chọn Tệp DO định dạng CSV/XLSX thích hợp từ máy tính của bạn (**Lưu ý**: Chúng tôi khuyên bạn nên sử dụng định dạng XLSX để ngăn việc giải mã chữ sai định dạng không mong muốn)

<Image title="2. Drag and Drop (VIE).png" alt={1920} border={true} src="https://files.readme.io/95ccbb8-2._Drag_and_Drop_VIE.png">
  Illustration (Vietnamese)
</Image>

### Bước 2: Khai báo Hồ sơ ánh xạ

#### Định nghĩa Hồ sơ ánh xạ

* Hồ sơ ánh xạ là các bản ghi lưu trữ cơ chế ánh xạ dữ liệu chính xác giữa các định dạng dữ liệu của người dùng và các định dạng dữ liệu Abivin vRoute

* Sau khi tải lên Tệp DO như ở Bước 1, bạn cần khai báo Hồ sơ ánh xạ cho Tệp DO đó

* Ở đây có hai trường hợp:

* **Tình huống 1**: Hồ sơ ánh xạ cho Tệp DO chưa được tạo. Trong trường hợp này, bạn cần tạo Hồ sơ ánh xạ mới

* **Tình huống 2**: Hồ sơ ánh xạ cho Tệp DO đã được tạo sẵn trước đó. Trong trường hợp này, bạn chỉ cần chọn Hồ sơ ánh xạ chính xác từ danh sách các Hồ sơ ánh xạ hiện có

* Tùy thuộc vào việc tài khoản của bạn là tài khoản định hướng Chủ hàng hay tài khoản định hướng Nhà vận tải/Nhà phân phối, quy trình khai báo Hồ sơ ánh xạ sẽ khác nhau ở một số bước nhất định

* Nếu tài khoản của bạn là định hướng Chủ hàng, khi bạn sử dụng công cụ Nhập tùy chỉnh, bạn chỉ cần thực hiện những việc sau để khai báo Hồ sơ ánh xạ mới

* 1 - Chọn Tệp DO sau đó tải tệp đó lên công cụ Nhập tùy chỉnh như ở Bước 1

* 2 - Chọn một Kho quản lý các sản phẩm được liệt kê trong Tệp DO

* 3 - Đặt tên cho Hồ sơ ánh xạ

* Nếu tài khoản của bạn là tài khoản định hướng Nhà vận tải/Nhà phân phối, khi bạn sử dụng công cụ Nhập tùy chỉnh, bạn cần thực hiện những việc sau để khai báo Hồ sơ ánh xạ mới

* 1 - Chọn Tệp DO sau đó tải tệp đó lên công cụ Nhập tùy chỉnh như ở Bước 1

* 2 - Chọn một Kho quản lý các sản phẩm được liệt kê trong Tệp DO

* 3 - Chọn một Chủ hàng (chủ sở hữu/nhà cung cấp sản phẩm được liệt kê trong Tệp DO)

* 4 - Đặt tên cho Hồ sơ ánh xạ

#### Tình huống 1: Tạo Hồ sơ ánh xạ mới

* Sau khi Tệp DO đã được tải lên, hãy nhấp vào trường **Tổ chức** để chọn **Kho** trực tiếp quản lý Đơn hàng đang được tải lên (Ở đây sẽ chọn loại tổ chức là **Kho** trên ứng dụng Web Abivin cho cả tài khoản định hướng Chủ hàng và định hướng Nhà vận tải/Nhà phân phối)

<Image title="2. Mapping (ENG).png" alt={1274} border={true} src="https://files.readme.io/8543b75-2._Mapping_ENG.png">
  Illustration (Vietnamese)
</Image>

* Nếu tài khoản của bạn là tài khoản định hướng Nhà vận tải/Nhà phân phối, bạn sẽ cần chỉ định Chủ hàng được liên kết với Khách hàng trong Tệp DO. Để thực hiện việc này, hãy nhấp vào trường **Mã Chủ hàng** và chọn Chủ hàng mong muốn trong danh sách thả xuống. Ngoài ra, bạn có thể nhập Tên tổ chức/Mã tổ chức của Chủ hàng mong muốn vào thanh tìm kiếm, sau đó chọn giá trị trả về trong danh sách.

<Image title="3. Shipper Code 1 (VIE).png" alt={1594} border={true} src="https://files.readme.io/4e2de1f-3._Shipper_Code_1_VIE.png">
  Illustration (Vietnamese)
</Image>

* Nếu tài khoản của bạn là định hướng Chủ hàng và bạn không sử dụng **Mã Chủ hàng**, bạn có thể để trống trường này
* Tiếp theo, nhấp vào trường **Thiết lập hồ sơ**, chọn tùy chọn **Tạo hồ sơ mới** để tạo **Hồ sơ ánh xạ** mới. Một trường mới có tên **Tên hồ sơ** sẽ xuất hiện ở bên phải. Nhập tên của Hồ sơ ánh xạ mới vào trường **Tên hồ sơ**

<Image title="4. Mapping a New Profile (VIE).png" alt={1588} border={true} src="https://files.readme.io/e428590-4._Mapping_a_New_Profile_VIE.png">
  Illustration (Vietnamese)
</Image>

* Tên của Hồ sơ ánh xạ có thể chứa chữ cái, con số, khoảng trắng và các ký tự đặc biệt (ví dụ: ***Test @ Depot 1***). Tên của Hồ sơ ánh xạ mới không được giống với bất kỳ tên nào của các Hồ sơ ánh xạ hiện có.
* Sau khi bạn đã tạo Hồ sơ ánh xạ mới, bấm **Tiếp theo**. Bạn sẽ được di chuyển đến tab **Kiểm tra dữ liệu**

<Image title="18. Next (VIE).png" alt={1272} border={true} src="https://files.readme.io/baaaaf9-18._Next_VIE.png">
  Illustration (Vietnamese)
</Image>

* Trên tab **Kiểm tra dữ liệu**, bạn cần chọn dòng Tiêu đề trong Tệp DO đã tải lên. Dòng Tiêu đề chứa tên của các trường thông tin trong Tệp DO mà bạn sẽ sử dụng để ghép cột với các trường thông tin theo định dạng tiêu chuẩn của Abivin vRoute. Bạn hãy di chuyển chuột vào bản xem trước, nhấp vào dòng có chứa tên các cột trong Tệp DO. Dòng bạn đã nhấp vào sẽ được đánh dấu bằng màu xanh lam. Nếu bạn chắc chắn rằng dòng bạn đã chọn là tên cột trong Tệp DO, hãy nhấn vào nút **Xác nhận**. Nút ***Xác nhận*** sẽ thay đổi thành ***Đã xác nhận***

<Image title="20. Confirmed (VIE).png" alt={1270} border={true} src="https://files.readme.io/c5f9a8f-20._Confirmed_VIE.png">
  Illustration (Vietnamese)
</Image>

* Nếu bạn chọn nhầm dòng, hãy nhấp vào chữ ***Hoàn tác*** (nằm ở bên dưới nút ***Đã xác nhận***), sau đó chọn lại dòng đúng

<Image title="21. Undo (VIE).png" alt={1273} border={true} src="https://files.readme.io/84ff02f-21._Undo_VIE.png">
  Illustration (Vietnamese)
</Image>

* Sau khi bạn đã chọn và xác nhận đúng dòng có chứa các tiêu đề, nhấp vào nút **Tiếp theo**
* Bạn sẽ được di chuyển đến tab **Ghép cột thông tin**

<Image title="22. Next (VIE).png" alt={1273} border={true} src="https://files.readme.io/b074cab-22._Next_VIE.png">
  Illustration (Vietnamese)
</Image>

#### Tình huống 2: Lựa chọn Hồ sơ ánh xạ đã có sẵn

* Nếu Hồ sơ ánh xạ cho Tệp DO đã được tạo trước đó, thì bạn chỉ cần chọn Hồ sơ ánh xạ đó mà không cần phải tạo Hồ sơ ánh xạ mới
* Bấm vào trường **Tổ chức** để chọn Kho thích hợp, sau đó chuyển sang trường thông tin **Mã Chủ hàng** để chọn mã của Chủ sở hữu/Nhà cung cấp của hàng hóa được liệt kê trong Tệp DO. Sau đó, nhấp vào trường **Tên hồ sơ**. Trên danh sách thả xuống, hãy chọn Hồ sơ ánh xạ thích hợp đã được tạo trước đó. Sau khi ba trường này đã được chọn, hãy nhấp vào nút **Tiếp theo**
* Bạn sẽ được di chuyển đến tab **Ghép cột thông tin**

<Image title="23. Select (VIE).png" alt={1752} border={true} src="https://files.readme.io/80185da-23._Select_VIE.png">
  Illustration (Vietnamese)
</Image>

### Bước 3: Ghép nối các trường dữ liệu

* Trên tab **Ghép cột thông tin**, bạn sẽ cần ghép các trường dữ liệu trong Tệp DO được tải lên với các trường dữ liệu tương ứng theo định dạng Abivin vRoute. Tại đây, nếu bạn đang tạo một Hồ sơ ánh xạ mới, bạn sẽ cần phải ghép các trường dữ liệu trong Tệp DO với các trường dữ liệu tương ứng trong cơ sở dữ liệu Abivin vRoute. Nếu bạn đang sử dụng Hồ sơ ánh xạ hiện có thì các trường dữ liệu đã được ghép trước đó
* Bạn sẽ thấy hai cột dữ liệu.
* 1 - Cột dữ liệu ở bên trái (1) là cột thông tin ở định dạng Abivin vRoute
* 2 - Cột dữ liệu ở bên phải (2) hiển thị các cột dữ liệu ở Tệp DO mà bạn đã tải lên

<Image title="17. Map Columns (VIE).png" alt={1919} border={true} src="https://files.readme.io/6e49b44-17._Map_Columns_VIE.png">
  Illustration (Vietnamese)
</Image>

* Để ghép cột thông tin, trước tiên, nhấp vào trường thông tin trong cột dữ liệu ở bên phải. Một danh sách thả xuống sẽ xuất hiện, hiển thị các trường dữ liệu trong Tệp DO mà bạn đã tải lên trước đó. Chọn trường dữ liệu thích hợp từ danh sách thả xuống, sau đó nhấp vào nút **Xác nhận ánh xạ**

<Image title="Edited.png" alt={1593} border={true} src="https://files.readme.io/718982d-Edited.png">
  Illustration (Vietnamese)
</Image>

* **Lưu ý**: Nếu loại trường dữ liệu được ghép cột là Ngày (Ngày đặt hàng; Ngày đến hạn, v.v.), thì ngay sau khi bạn chọn trường dữ liệu đó, bên dưới trường dữ liệu đó sẽ xuất hiện trường **Chọn định dạng**. Bạn cần nhấp vào trường này, chọn định dạng ngày tương tự như định dạng ngày hiện tại trong Tệp DO 

<Image title="14.ate (VIE).png" alt={1586} border={true} src="https://files.readme.io/f2cc45a-14.ate_VIE.png">
  Illustration (Vietnamese)
</Image>

* Ví dụ: Trong Tệp DO, định dạng ngày của trường thông tin **Ngày đơn hàng** là ***Ngày-Tháng-Năm (DD-MM-YYYY)*** (ví dụ, ***10-05-2021***) thì bạn cần chọn định dạng ngày (DD-MM-YYYY) trên công cụ Nhập tùy chỉnh

<Image title="15. Date (VIE) (Ex).png" alt={1586} border={true} src="https://files.readme.io/fea19f8-15._Date_VIE_Ex.png">
  Illustration (Vietnamese)
</Image>

* Nếu bạn muốn ghép lại các cột thông tin, vui lòng nhấp vào nút **Chỉnh sửa** để ghép lại cột thông tin

<Image title="14. Edit (VIE).png" alt={1427} border={true} src="https://files.readme.io/e564c71-14._Edit_VIE.png">
  Illustration (Vietnamese)
</Image>

* Nếu bạn không muốn ghép một cột thông tin cụ thể, hãy nhấp vào nút tương ứng **Bỏ qua cột này**

<Image title="13. Ignore Columns (VIE).png" alt={1432} border={true} src="https://files.readme.io/402258f-13._Ignore_Columns_VIE.png">
  Illustration (Vietnamese)
</Image>

* Trong cột bên trái (cột dữ liệu ở định dạng Abivin vRoute), một số trường thông tin không thể bị bỏ qua và yêu cầu bạn phải ghép cột, đó là
* 1. Ngày đơn hàng
* 2. Mã Đơn hàng
* 3. Mã sản phẩm
* 4. Tên sản phẩm
* 5. Số lẻ
* Trong trường hợp tài khoản của bạn là tài khoản định hướng Chủ hàng, ở cột bên trái sẽ có thêm 2 trường thông tin bắt buộc khác yêu cầu bạn phải ghép cột, đó là
* 1. Mã Khách hàng
* 2. Tên Khách hàng\
     \*Trong trường hợp tài khoản của bạn là tài khoản định hướng Nhà vận tải/Nhà phân phối, trong cột bên trái sẽ có thêm 3 trường thông tin bắt buộc khác yêu cầu ghép cột, đó là
* 1. Mã Điểm giao
* 2. Tên Điểm giao
* 3. Địa chỉ Điểm giao
* Các trường thông tin bắt buộc phải ghép cột đều có dấu hoa thị  :fa-asterisk: ở cuối tên trường.

<Image title="Asterisk (VIE).png" alt={738} border={true} src="https://files.readme.io/d43b0ac-Asterisk_VIE.png">
  Illustration (Vietnamese)
</Image>

* Sau khi bạn hoàn thành ghép cột tất cả các trường dữ liệu cần thiết, nhấn vào nút **Tiếp theo**
* Bạn sẽ được di chuyển đến tab **Kiểm tra ánh xạ**

### Bước 4: Kiểm tra ánh xạ và Nhập dữ liệu

* Trên tab **Kiểm tra ánh xạ**, bạn có thể xem bản xem trước của Kết quả ánh xạ. Dòng tiêu đề (Dòng đầu tiên) hiển thị các trường dữ liệu ở định dạng Abivin vRoute, trong khi dòng dữ liệu (hàng thứ hai) hiển thị các trường dữ liệu thực tế đã ghép nối từ Tệp DO
* Nếu bạn không thấy bất kỳ lỗi nào với Kết quả ánh xạ, nhấp vào nút **Hoàn thành**

<Image title="15. Check (VIE).png" alt={1434} border={true} src="https://files.readme.io/ec568ae-15._Check_VIE.png">
  Illustration (Vietnamese)
</Image>

* Khi nhấn vào nút này, hệ thống sẽ kiểm tra ngay dữ liệu trong Tệp DO. Nếu dữ liệu đáp ứng tất cả các quy tắc nhập và ánh xạ, Tệp DO sẽ được chuyển đổi thành công và dữ liệu trong Tệp DO sẽ được nhập vào cơ sở dữ liệu Abivin vRoute cho ba tài nguyên sau (Theo trình tự thời gian): **Sản phẩm; Khách hàng; Đơn hàng**. Đồng thời, hệ thống sẽ có thông báo chuyển đổi thành công như hình dưới

<Image title="17. Upload.png" alt={248} border={true} src="https://files.readme.io/774bf2c-17._Upload.png">
  Illustration (Vietnamese)
</Image>

* **Lưu ý**: Nếu trong Tệp DO đang tải lên có thông tin Đơn hàng/Khách hàng/Sản phẩm đã được nhập trên hệ thống Abivin vRoute thì dữ liệu trong Tệp DO sẽ không ghi đè lên dữ liệu Abivin vRoute. Thay vào đó, hệ thống sẽ hiển thị thông báo lỗi. Ví dụ, nếu một Đơn hàng đã có sẵn trong hệ thống trước đó và bạn nhập Đơn hàng đó một lần nữa bằng công cụ Nhập tùy chỉnh, hệ thống sẽ hiển thị thông báo lỗi như trong ảnh bên dưới.

<Image title="16. Error (VIE).png" alt={1431} border={true} src="https://files.readme.io/d47074b-16._Error_VIE.png">
  Illustration (Vietnamese)
</Image>

* Nếu thông tin về Đơn hàng/Khách hàng/Sản phẩm chưa có trong cơ sở dữ liệu của Abivin vRoute trước đó, hệ thống sẽ tạo ra các bản ghi. Thông tin được tạo gần đây nhất của Đơn hàng/Khách hàng/Sản phẩm sẽ được hiển thị trên đầu trang đầu tiên của tab tương ứng cho mỗi tài nguyên.
* Ví dụ: Tệp DO của bạn có hai đơn đặt hàng với hai Sản phẩm và bạn sử dụng công cụ Nhập tùy chỉnh để nhập thông tin vào hệ thống Abivin vRoute. Thông tin về Sản phẩm mới từ tệp DO của bạn sẽ được thu thập, chuyển đổi và hiển thị trên đầu trang đầu tiên trong tab **Sản phẩm** như trong bức ảnh dưới đây.

<Image title="12. Import First Page (VIE).png" alt={1690} border={true} src="https://files.readme.io/560e3cb-12._Import_First_Page_VIE.png">
  Illustration (Vietnamese)
</Image>

## Lịch sử sử dụng công cụ Nhập tùy chỉnh

* Mỗi khi bạn tải Tệp CSV/XLSX vào cơ sở dữ liệu Abivin vRoute bằng công cụ Nhập tùy chỉnh hoặc nhập trực tiếp qua máy chủ FTP, hệ thống sẽ lưu trữ lịch sử nhập của Tệp đó ngay trên tab **Cài đặt > Nhập tùy chỉnh**

<Image title="7. History (VIE).png" alt={1920} border={true} src="https://files.readme.io/919d918-7._History_VIE.png">
  Illustration (Vietnamese)
</Image>

* Để tìm kiếm một Tệp cụ thể, nhập tên chính xác của Tệp đó vào thanh Tìm kiếm

<Image title="8. Search (VIE).png" alt={1733} border={true} src="https://files.readme.io/724ac79-8._Search_VIE.png">
  Illustration (Vietnamese)
</Image>

* Để lọc Tệp tải lên theo Tổ chức, hãy nhấn vào trường **Tổ chức** và chọn Tổ chức thích hợp (Tổ chức sẽ là các Kho)
* Để lọc các Tệp theo trạng thái tải lên, hãy nhấn vào cột **Trạng thái nhập**. Trên danh sách thả xuống, tích chọn ô của các trạng thái mong muốn. Các Trạng thái nhập gồm có **Đang thực hiện; Thành công; Thất bại**

<Image title="11. Import Status (VIE).gif" alt={1728} border={true} src="https://files.readme.io/f3785ad-11._Import_Status_VIE.gif">
  Illustration (Vietnamese)
</Image>

* Để xem nguyên nhân tại sao không nhập được một Tệp cụ thể, hãy nhấp vào mục **Chi tiết** tương ứng với Tệp đó. Ở bên phải của màn hình sẽ xuất hiện tab **Chi tiết nhập**, nêu lý do không thành công

<Image title="Reason (VIE) 2 - Merged 1.png" alt={1710} border={true} src="https://files.readme.io/4ae364b-Reason_VIE_2_-_Merged_1.png">
  Illustration (Vietnamese)
</Image>

* Để tải xuống một tệp, hãy nhấn vào biểu tượng tải xuống tương ứng :fa-download: của tệp đó bên dưới cột **Hành động**

<Image title="4. Action (ENG).png" alt={1729} border={true} src="https://files.readme.io/f3f20b5-4._Action_ENG.png">
  Illustration (English)
</Image>

<Image title="6. Actions(VIE).png" alt={1704} border={true} src="https://files.readme.io/2d81677-6._ActionsVIE.png">
  Illustration (Vietnamese)
</Image>
