---
title: Quản lý Người dùng
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
## Định nghĩa Người dùng và Nhóm người dùng

Người dùng là một cá nhân được cấp tài khoản để sử dụng ứng dụng Web hoặc ứng dụng di động Abivin vRoute.\
Nhóm người dùng là tập hợp những tài khoản Người dùng trực thuộc cùng một Tổ chức, được phân những quyền giống nhau.

## Loại Nhóm người dùng

Tương tự như tài nguyên Tổ chức, trong mô hình này cũng tồn tại hai loại Nhóm người dùng dựa trên tính bắt buộc: **Nhóm người dùng bắt buộc** và **Nhóm người dùng tuỳ chọn (Không bắt buộc)**.

### Nhóm người dùng bắt buộc

Trong mô hình này, có hai Nhóm người dùng bắt buộc: **Quản trị viên** và **Tài xế (Nhân viên giao hàng)**.

#### Nhóm người dùng Quản trị viên

Quản trị viên là những Người dùng sẽ sử dụng ứng dụng Web để quản lý các tài nguyên trong hệ thống.\
Mỗi Tổ chức sẽ có Nhóm người dùng Quản trị viên riêng.

#### Nhóm người dùng Tài xế (Nhân viên giao hàng)

Tài xế là những người sẽ trực tiếp điều khiển Phương tiện giao hàng để giao những Đơn hàng tới cho Khách hàng. Trong quá trình giao hàng, họ sẽ sử dụng ứng dụng di động để gửi kết quả của tác vụ mà họ được phân công thực hiện về ứng dụng Web để Quản trị viên có thể theo dõi.\
Mỗi Tổ chức thuộc loại Kho cấp 1/Kho Sun sẽ có Nhóm người dùng Tài xế riêng.\
Hướng dẫn sử dụng ứng dụng di động cho Tài xế được trình bày tại bài viết sau: [**Tài xế (Nhân viên giao hàng)**]().

### Nhóm người dùng tuỳ chọn

Trong mô hình này, có hai Nhóm người dùng tuỳ chọn: **Nhân viên bán hàng** và **Người tiêu dùng**.

#### Nhóm người dùng Nhân viên bán hàng

Các công ty sản xuất luôn duy trì một lực lượng các nhân viên bán hàng. Nhân viên bán hàng là những người được giao trách nhiệm khai phá thị trường, tìm kiếm và thiết lập mối quan hệ kinh doanh với những đối tác mới.\
Trong hệ thống Abivin vRoute, các tài khoản Nhân viên bán hàng sẽ có thể theo dõi trạng thái thực hiện của những Đơn hàng được giao cho những Khách hàng mà họ có liên kết. Họ cũng có thể chủ động tạo Đơn hàng theo yêu cầu từ các Khách hàng của họ.\
Mỗi Tổ chức thuộc loại Kho cấp 1/Kho Sun sẽ có Nhóm người dùng Nhân viên bán hàng riêng.\
Cách thiết lập Nhóm người dùng này trên ứng dụng Web được trình bày tại bài viết sau: [**Nhân viên bán hàng**]().\
Hướng dẫn sử dụng ứng dụng di động cho Nhân viên bán hàng được trình bày tại bài viết sau: [**Nhân viên bán hàng**]().

#### Nhóm người dùng Người tiêu dùng

Người tiêu dùng là là những người dùng cuối, trực tiếp tiêu thụ các Sản phẩm được sản xuất bởi tổ chức của bạn. Trong một số lĩnh vực, ví dụ bán lẻ, Người tiêu dùng có thể chủ động đặt Đơn hàng khi họ có nhu cầu.\
Cách thiết lập Nhóm người dùng này trên ứng dụng Web được trình bày tại bài viết sau: [**Người tiêu dùng**]().\
Hướng dẫn sử dụng ứng dụng di động cho Người tiêu dùng được trình bày tại bài viết sau: [**Người tiêu dùng**]().

## Quản lý Nhóm người dùng

### Định vị danh sách Nhóm người dùng

Các bản ghi Nhóm người dùng được liệt kê tại tab **Tổ chức > Nhóm người dùng**

### Tạo Nhóm người dùng

Trong hệ thống Abivin vRoute, mỗi khi một Tổ chức được tạo mới, Nhóm người dùng Quản trị viên của Tổ chức đó cũng sẽ được tạo tự động.\
Nhóm người dùng Quản trị viên được tạo tự động sẽ có các đặc điểm sau:

1. Thuộc tính **Mã Nhóm người dùng** sẽ là giá trị thuộc tính **Mã tổ chức** của Tổ chức mà Nhóm người dùng Quản trị viên đó trực thuộc cộng thêm tiền tố ***AD-***.
2. Thuộc tính **Tên Nhóm người dùng** sẽ là giá trị thuộc tính **Têntổ chức** của Tổ chức mà Nhóm người dùng Quản trị viên đó trực thuộc cộng thêm tiền tố ***Admin\_***.\
   Ví dụ, đối với một Chi nhánh có Mã tổ chức là ***Chi\_nhanh\_Hanoi*** và Tên tổ chức là **\*Chi nhánh Hà Nội** thì Nhóm người dùng Quản trị viên của Chi nhánh đó sẽ có Mã Nhóm người dùng là ***AD-Chi\_nhanh\_Hanoi*** và Tên Nhóm người dùng là ***Admin\_Chi nhánh Hà Nội***.

Ngoài ra, nếu như bạn tạo Tổ chức thuộc loại **Kho cấp 1** thì Nhóm người dùng Tài xế của Kho cấp 1 đó cũng sẽ được tạo tự động với Mã Nhóm người dùng ***DELIVERER*** và Tên nhóm người dùng là ***Nhóm giao hàng***.

<Image title="delv.png" alt={879} border={true} src="https://files.readme.io/a987003-delv.png">
  Illustration Image (English)
</Image>

Nếu như bạn muốn tạo thêm Nhóm người dùng cho một Tổ chức nào đó, bạn phải sử dụng Biểu mẫu Web.

#### Thông tin Nhóm người dùng

Thông thường, thông tin của Nhóm người dùng sẽ được nhập vào hai phần:

1. [**Phần Thông tin cơ bản**](). Phần này sẽ chứa những thông tin cơ bản nhất của Nhóm người dùng như Mã nhóm người dùng, Tên nhóm người dùng.
2. [**Phần Mô-đun phân quyền**](). Phần này cho phép Quản trị viên có thể phân quyền các Mô-đun trong hệ thống mà từng Nhóm người dùng sẽ có quyền truy cập.

Ngoài ra, đối với Nhóm người dùng Quản trị viên, sẽ có thêm phần [**Quyền Kế hoạch lộ trình**](). Phần này cho phép bạn thiết lập những quyền liên quan đến Kế hoạch lộ trình.

#### Phần Thông tin cơ bản

Bên dưới là danh sách các trường thông tin cơ bản của một Nhóm người dùng:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Trường thông tin
      </th>

      <th>
        Mô tả & Cách nhập
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Tổ chức
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        Tổ chức quản lý Nhóm người dùng đang được tạo.\
        **Quy tắc nhập:**\
        Nhấn vào trường này. Trên trình đơn xổ xuống, nhập **Tên tổ chức/Mã tổ chức** của Tổ chức cần tìm, sau đó chọn giá trị trả ra.\
        **Ghi chú:**\
        Nếu nhóm người dùng đang được tạo là Nhóm người dùng **Tài xế/Nhân viên bán hàng**, Tổ chức quản lý phải thuộc các loại sau: **Kho cấp 1/Kho Sun**\
        Nếu nhóm người dùng được tạo là Nhóm người dùng **Người tiêu dùng**, Tổ chức quản lý phải thuộc loại sau: **Nhà sản xuất**
      </td>
    </tr>

    <tr>
      <td>
        Mã Nhóm\
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        Mã quản lý được gán cho Nhóm người dùng đang được tạo.\
        **Quy tắc nhập:**\
        Định dạng: Chỉ chứa chữ số, chữ cái, ký tự đặc biệt. Không được chứa khoảng trắng (dấu cách).\
        Nếu Nhóm người dùng đang được tạo là Nhóm người dùng **Tài xế**, bạn cần nhập chính xác giá trị sau vào trường này (Tất cả các chữ cái phải viết hoa): ***DELIVERER***.\
        Nếu Nhóm người dùng đang được tạo là Nhóm người dùng **Nhân viên bán hàng**, bạn cần nhập chính xác giá trị sau vào trường này (Tất cả các chữ cái phải viết hoa): ***SALESMAN***.\
        Nếu Nhóm người dùng đang được tạo là Nhóm người dùng **Người tiêu dùng**, bạn cần nhập chính xác giá trị sau vào trường này (Tất cả các chữ cái phải viết hoa): ***CONSUMER***.\
        **Ghi chú:**\
        Khi bạn tạo Nhóm người dùng bằng biểu mẫu Web, tất cả các ký tự của Mã nhóm người dùng sẽ được tự động viết hoa. Ngoài ra, tất cả các khoảng trắng sẽ được chuyển thành dấu gạch ngang (-).
      </td>
    </tr>

    <tr>
      <td>
        Tên Nhóm\
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        Tên của Nhóm người dùng đang được tạo.\
        **Quy tắc nhập:**\
        Định dạng: Nhập tự do.
      </td>
    </tr>

    <tr>
      <td>
        Mô tả\
        (Tùy chọn)
      </td>

      <td>
        **Mô tả:**\
        Mô tả ngắn về Nhóm người dùng đang được tạo.\
        **Quy tắc nhập:**\
        Định dạng: Nhập tự do
      </td>
    </tr>
  </tbody>
</Table>

#### Phần Mô-đun phân quyền

Phần này là nơi bạn có thể thiết lập các Mô-đun mà Nhóm người dùng đang được tạo được quyền truy cập và những quyền cụ thể của Nhóm người dùng đối với các Mô-đun đó.\
**Lưu ý**: Có một số quyền chưa khả dụng cho một số Mô-đun.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Quyền Mô-đun
      </th>

      <th>
        Mô tả quyền
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Tạo mới
      </td>

      <td>
        Có thể tạo các bản ghi của Mô-đun đó
      </td>
    </tr>

    <tr>
      <td>
        Đọc
      </td>

      <td>
        Có thể đọc các bản ghi của Mô-đun đó
      </td>
    </tr>

    <tr>
      <td>
        Cập nhật
      </td>

      <td>
        Có thể cập nhật/chỉnh sửa các bản ghi của Mô-đun đó
      </td>
    </tr>

    <tr>
      <td>
        Xóa
      </td>

      <td>
        Có thể xóa các bản ghi của Mô-đun đó
      </td>
    </tr>

    <tr>
      <td>
        Xem tất cả
      </td>

      <td>
        Có thể xem các tài nguyên của mô-đun đó từ các Tổ chức khác cùng cấp
      </td>
    </tr>

    <tr>
      <td>
        Xuất tệp tin
      </td>

      <td>
        Có thể xuất các bản ghi của Mô-đun đó ra tệp Excel
      </td>
    </tr>

    <tr>
      <td>
        Tất cả
      </td>

      <td>
        Tất cả các quyền trên
      </td>
    </tr>

    <tr>
      <td>
        Tích hợp-Đầu vào
      </td>

      <td>
        Tích hợp với cơ sở dữ liệu của các hệ thống bên ngoài (TMS; ERP, v.v.) và kéo dữ liệu của Mô-đun đó về cơ sở dữ liệu Abivin vRoute
      </td>
    </tr>

    <tr>
      <td>
        Tích hợp-Đầu ra
      </td>

      <td>
        Tích hợp với cơ sở dữ liệu của các hệ thống bên ngoài (TMS; ERP, v.v.) và đẩy dữ liệu của Mô-đun đó từ cơ sở dữ liệu Abivin vRoute sang các hệ thống tích hợp
      </td>
    </tr>
  </tbody>
</Table>

Ngoài ra, để Nhóm người dùng của một Tổ chức cấp trên có thể xem tài nguyên của tất cả các Tổ chức cấp dưới trực thuộc Tổ chức cấp trên đó, bạn cần đánh dấu vào ô chọn **Có thể xem Tổ chức con**.\
**Lưu ý**: Những Người dùng thuộc Nhóm người dùng Quản trị viên được tạo tự động của một Tổ chức sẽ luôn có thể xem tất cả các tài nguyên của mọi Tổ chức cấp thấp hơn trực thuộc Tổ chức đó, bất kể ô chọn **Có thể xem Tổ chức con** có được tích hay không. Ví dụ: Người dùng thuộc Nhóm người dùng Quản trị viên được tạo tự động của một Chi nhánh sẽ luôn có thể xem tài nguyên của tất cả các Kho trực thuộc Chi nhánh đó.

#### Phần quyền Kế hoạch lộ trình

Đối với Nhóm người dùng Điều phối viên (Trực thuộc các Tổ chức Nhà sản xuất; Nhà phân phối; Chi nhánh), có nhiều chức năng liên quan đến việc thao tác Kế hoạch lộ trình. Do đó, có một phần riêng để thiết lập các quyền Kế hoạch lộ trình ngoài phần Mô-đun đã mô tả ở trên.\
Trước khi đi vào chi tiết, có một số lưu ý:

1. Nhóm người dùng Quản trị viên của Nhà sản xuất sẽ luôn có đầy đủ quyền Kế hoạch lộ trình bất kể các chức năng trong phần này có được bật cho Nhóm người dùng đó hay không.
2. Một số chức năng trong phần này sẽ có tác dụng tương tự như một số thiết lập tại một số Loại tổ chức (Chủ yếu là tại Chi nhánh). Tuy nhiên, các thiết lập tại Tổ chức sẽ luôn được ưu tiên hơn các chức năng được mô tả trong phần này. Ví dụ: nếu bạn không bật chức năng trong phần này nhưng bật thiết lập có cùng tác dụng tại Tổ chức, thì Người dùng vẫn có thể sử dụng chức năng đó.
3. Một số chức năng trong phần này có thể chỉ khả dụng trên màn hình Kế hoạch lộ trình (Dạng bản đồ) hoặc màn hình Kế hoạch lộ trình (Dạng danh sách), chưa khả dụng đồng thời trên cả hai màn hình.

Để truy cập phần thiết lập Quyền Kế hoạch lộ trình, trên biểu mẫu **Cập nhật nhóm**, hãy di chuyển đến tab phụ **Các quyền khác**.\
Để bật một chức năng, chỉ cần tích ô chọn tương ứng của chức năng ấy.\
Để nhanh chóng bật tất cả các chức năng, tích ô chọn **Kế hoạch lộ trình**.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Quyền Kế hoạch lộ trình
      </th>

      <th>
        Mô tả chức năng
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Tạo mới
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép khởi tạo Kế hoạch lộ trình.
      </td>
    </tr>

    <tr>
      <td>
        Đọc
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép xem chi tiết của một Kế hoạch lộ trình đã được khởi tạo.\
        **Lưu ý quan trọng:**\
        Quyền này là quyền cơ bản nhất, cần được bật trước khi bật các quyền khác.
      </td>
    </tr>

    <tr>
      <td>
        Xoá
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép xóa/loại bỏ một Chuyển giao hàng khỏi Kế hoạch lộ trình.\
        Quyền này tương tự như thiết lập sau tại Chi nhánh: **Cho phép gỡ chốt và xóa lộ trình**.
      </td>
    </tr>

    <tr>
      <td>
        Xuất tệp tin
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép xuất Kế hoạch lộ trình ra tệp tin Excel.
      </td>
    </tr>

    <tr>
      <td>
        Khởi tạo
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép khởi tạo quá trình tối ưu Kế hoạch lộ trình.
      </td>
    </tr>

    <tr>
      <td>
        Chốt lộ trình
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép chốt các Lộ trình giao hàng trong Kế hoạch lộ trình.
      </td>
    </tr>

    <tr>
      <td>
        Gỡ chốt lộ trình
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép gỡ chốt các Lộ trình giao hàng đã chốt trong Kế hoạch lộ trình.\
        Tương tự như thiết lập sau tại Chi nhánh: **Cho phép gỡ chốt và xóa lộ trình**.
      </td>
    </tr>

    <tr>
      <td>
        Khóa lộ trình
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép khoá các Lộ trình giao hàng đã chốt trong Kế hoạch lộ trình.
      </td>
    </tr>

    <tr>
      <td>
        Tích hợp-Đầu ra
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép đồng bộ hoá Kế hoạch lộ trình đã khóa từ hệ thống Abivin vRoute tới Hệ thống quản lý vận tải bên ngoài.
      </td>
    </tr>

    <tr>
      <td>
        Đóng chuyến
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép đóng các Chuyến giao hàng đã được đồng bộ hoá từ hệ thống Abivin vRoute tới Hệ thống quản lý vận tải bên ngoài, qua đó xác nhận các Đơn hàng trong Lộ trình giao hàng đã được hoàn thành đồng thời giải phóng các Phương tiện đã được sử dụng trong Lộ trình giao hàng đó.
      </td>
    </tr>

    <tr>
      <td>
        Chuyển tài xế
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép thay đổi Tài xế thực hiện Ca giao hàng trong Kế hoạch lộ trình.
      </td>
    </tr>

    <tr>
      <td>
        Chuyển phương tiện
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép thay đổi Phương tiện thực hiện Ca giao hàng trong Kế hoạch lộ trình.
      </td>
    </tr>

    <tr>
      <td>
        Di chuyển Đơn hàng/Điểm dừng
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép 1. di chuyển các Đơn hàng trong một Điểm dừng hoặc toàn bộ một Điểm dừng sang một vị trí khác trong Kế hoạch lộ trình, hoặc 2. di chuyển các Đơn hàng rớt vào Kế hoạch lộ trình.\
        **Lưu ý:**\
        Tính năng di chuyển Đơn hàng hiện không khả dụng cho Kế hoạch lộ trình (Dạng bản đồ).
      </td>
    </tr>

    <tr>
      <td>
        Cập nhật vị trí Điểm dừng
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ).\
        Quyền cho phép cập nhật thông tin tọa độ của Điểm dừng trong Kế hoạch lộ trình.
      </td>
    </tr>

    <tr>
      <td>
        Xóa Đơn hàng/Điểm dừng
      </td>

      <td>
        Khả dụng trên: Kế hoạch lộ trình (Dạng bản đồ) và Kế hoạch lộ trình (Dạng danh sách).\
        Quyền cho phép xoá các Đơn hàng trong một Điểm dừng hoặc toàn bộ Điểm dừng ra khỏi Kế hoạch lộ trình.\
        **Lưu ý:**\
        Tính năng xóa Đơn hàng hiện không khả dụng cho Kế hoạch lộ trình (Dạng bản đồ).
      </td>
    </tr>
  </tbody>
</Table>

Dưới đây là các quyền cần thiết mà bạn nên gán cho các Nhóm người dùng bắt buộc của mô hình này (Nhấn vào chữ để chuyển luôn đến nội dung):\
[Nhóm người dùng Quản trị viên của Nhà sản xuất]().\
[Nhóm người dùng Tài xế của Kho cấp 1/Kho Sun]().\
Đối với các Nhóm người dùng tuỳ chọn (Nhân viên bán hàng, Người tiêu dùng), nội dung phân quyền sẽ được trình bày tại bài viết riêng của Nhóm người dùng đó.

##### Nhóm người dùng Quản trị viên Nhà sản xuất

Bảng dưới đây liệt kê các Mô-đun và quyền cần thiết của từng Mô-đun mà bạn cần gán cho Nhóm người dùng Quản trị viên Nhà sản xuất của mô hình này:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Mô-đun
      </th>

      <th>
        Quyền Mô-đun
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Tổ chức
      </td>

      <td>
        Tất cả
      </td>
    </tr>

    <tr>
      <td>
        Báo cáo
      </td>

      <td>
        Tất cả
      </td>
    </tr>

    <tr>
      <td>
        Phân quyền
      </td>

      <td>
        Tất cả
      </td>
    </tr>

    <tr>
      <td>
        Người dùng
      </td>

      <td>
        Tất cả
      </td>
    </tr>

    <tr>
      <td>
        Khách hàng
      </td>

      <td>
        Tất cả
      </td>
    </tr>

    <tr>
      <td>
        Đơn hàng
      </td>

      <td>
        Tất cả
      </td>
    </tr>

    <tr>
      <td>
        Phương tiện
      </td>

      <td>
        Tất cả
      </td>
    </tr>

    <tr>
      <td>
        Tác vụ
      </td>

      <td>
        Tất cả
      </td>
    </tr>

    <tr>
      <td>
        Hành động tác vụ
      </td>

      <td>
        Tất cả
      </td>
    </tr>
  </tbody>
</Table>

Dưới đây là các quyền tùy chọn có thể được bật tùy thuộc vào nhu cầu của bạn:\
Nếu bạn muốn sử dụng chức năng truy xuất và lấy những [**Đơn hàng rớt**]() và [**Đơn hàng không giao được**]() từ các ngày quá khứ vào ngày hiện tại, bạn cần tích ô chọn **Tích hợp - Đầu vào** của Mô-đun **Đơn hàng**.\
Nếu như bạn có áp dụng các chương trình [**Giảm giá và Khuyến mãi**]() cho Sản phẩm của mình, hãy tích ô chọn **Tất cả** của Mô-đun **Khuyến mãi**.\
Nếu bạn muốn sử dụng [**Công cụ nhập tuỳ chỉnh**]() để nhập trực tiếp các tệp Đơn hàng theo định dạng mà tổ chức của bạn sử dụng lên hệ thống Abivin vRoute, hãy tích ô chọn **Tất cả** của Mô-đun **Hồ sơ ánh xạ**.

##### Nhóm người dùng Tài xế Kho cấp 1/Kho Sun

Bảng dưới đây liệt kê các Mô-đun và quyền cần thiết bạn mà bạn cần gán cho Nhóm người dùng Tài xế Kho cấp 1/Kho Sun của mô hình này:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Mô-đun
      </th>

      <th>
        Quyền Mô-đun
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Tổ chức
      </td>

      <td>
        Đọc
      </td>
    </tr>

    <tr>
      <td>
        Tác vụ
      </td>

      <td>
        Đọc\
        Cập nhật
      </td>
    </tr>

    <tr>
      <td>
        Khách hàng
      </td>

      <td>
        Đọc
      </td>
    </tr>

    <tr>
      <td>
        Sản phẩm
      </td>

      <td>
        Đọc
      </td>
    </tr>

    <tr>
      <td>
        Đơn hàng
      </td>

      <td>
        Đọc
      </td>
    </tr>
  </tbody>
</Table>

Nếu bạn muốn cho phép các Người dùng Tài xế có thể [chủ động sắp xếp lại trình tự các Điểm dừng]() trên Lộ trình giao hàng mà họ được phân công ngay trên ứng dụng di động giao hàng, thì bạn sẽ cần di chuyển đến tab phụ **Các quyền khác** và tích chọn quyền **Di chuyển Đơn hàng/Điểm dừng** cho Nhóm người dùng này.

## Quản lý Người dùng

Sau khi bạn đã hoàn thành thiết lập các Nhóm người dùng, bạn có thể chuyển sang tạo và quản lý các Người dùng trực thuộc các Nhóm người dùng.

### Định vị danh sách Người dùng

Các bản ghi Người dùng được liệt kê tại tab **Tổ chức > Người dùng**

### Tạo Người dùng

Bạn có thể tạo Người dùng bằng hai phương phép: Biểu mẫu Web và Tệp nhập Excel.

#### Tạo Người dùng bằng Biểu mẫu Web

Khi bạn sử dụng Biểu mẫu Web để tạo Người dùng, bạn cần nhập các thông tin cơ bản của Người dùng theo trình tự sau để đảm bảo không có lỗi:

1. Tên tổ chức (Trong mô hình này, một tài khoản Người dùng có thể thuộc nhiều Tổ chức khác nhau).
2. Các nhóm (Trong mô hình này, một tài khoản Người dùng có thể thuộc nhiều Nhóm người dùng khác nhau).
3. Tên đăng nhập.
4. Mật khẩu; Nhập lại mật khẩu.
5. Email (Hãy nhập địa chỉ email thật (Gmail, Outlook, Yahoo Mail v.v.) đối với những Người dùng quan trọng, cần quan tâm tới vấn đề bảo mật, ví dụ Quản trị viên hệ thống. Đối với những Người dùng thông thường, ví dụ Tài xế, bạn có thể sử dụng các dịch vụ email tạm thời (disposable email), ví dụ như YOPmail, MailDrop, Mailinator, v.v.).
6. Số điện thoại.
7. Họ tên.

Vừa rồi mới chỉ là các thông tin cơ bản của tất cả Người dùng. Nếu như Người dùng đang được tạo thuộc Nhóm người dùng Tài xế, bạn sẽ cần nhập thêm một số thông tin khác của Người dùng ấy ở phần **Các thiết lập khác**.

Mô tả và quy tắc nhập liệu các trường thông tin của Người dùng được trình bày ở phần sau: [**Trường thông tin Người dùng**]().

#### Tạo Người dùng bằng Tệp nhập Excel

Bạn nên sử dụng phương pháp này nếu muốn tạo nhiều bản ghi Người dùng cùng một lúc.\
Lưu ý rằng trong Tệp nhập Excel không có các trường thông tin **Mật khẩu; Nhập lại mật khẩu** như trên Biểu mẫu Web. Sau khi tệp được tải thành công lên hệ thống, mỗi tài khoản Người dùng trong tệp sẽ được tạo tự động một mật khẩu ngẫu nhiên. Mật khẩu ngẫu nhiên sẽ được gửi về địa chỉ email của từng Người dùng. Người dùng sẽ cần sử dụng mật khẩu ngẫu nhiên để đăng nhập vào tài khoản của họ. Sau khi đã đăng nhập thành công lần đầu, Người dùng có thể tuỳ ý thay đổi mật khẩu 

* You will notice that in the Excel file, there are no **Password/Re-password** fields like on the Webform. This is because upon uploading the Excel file onto the Web app, the system will automatically generate random passwords for each user and send the password to the Users' email addresses input in the Excel file. The Users have to use those random passwords to login to their accounts for the first time. After logging in, they can change their passwords to new ones (Note that the new passwords must adhere to the [**Strong Password rules**](https://docs.abivin.com/docs/web-app-account#section-password-rules))

> 📘 Hướng dẫn thay đổi mật khẩu (Nhấn vào chữ để chuyến tới nội dung)
>
> [Thay đổi mật khẩu trên ứng dụng Web]()\
> [Thay đổi mật khẩu trên ứng dụng di động]()

#### Thông tin Người dùng

Dưới đây là các thông tin của Người dùng

> 📘 Có một số trường thông tin không sử dụng cho mô hình này, do đó không được đề cập

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Trường thông tin
      </th>

      <th>
        Mô tả & Cách nhập
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Tên tổ chức (Biểu mẫu Web); Mã tổ chức (Tệp nhập Excel)
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        (Các) Tổ chức mà Người dùng đang được tạo trực thuộc.\
        **Quy tắc nhập:**\
        **Biểu mẫu Web:**\
        Nhấn vào trường này. Trên thanh tìm kiếm của trình đơn xổ xuống, nhập **Tên tổ chức/Mã tổ chức** của Tổ chức cần tìm, sau đó tích ô chọn của giá trị trả về.\
        **Tệp nhập Exce:**\
        Sao chép Mã tổ chức của Tổ chức phù hợp trên ứng dụng Web, sau đó dán vào ô này.\
        **Lưu ý:**\
        Khi bạn sử dụng Biểu mẫu Web, bạn có thể lựa chọn nhiều Tổ chức. Tuy nhiên, trên Tệp nhập Excel, bạn chỉ có thể điền một Mã tổ chức duy nhất.\
        Mã tổ chức và Tên tổ chức có thể được tìm thấy trong các cột cùng tên ở tab **Tổ chức > Tổ chức**.\
        Nếu Người dùng đang được tạo là Tài xế, Tổ chức quản lý phải thuộc loại **Kho cấp 1** hoặc **Kho Sun**.
      </td>
    </tr>

    <tr>
      <td>
        Các nhóm (Biểu mẫu Web); Mã nhóm người dùng (Tệp nhập Excel)\
        (Tuỳ chọn)
      </td>

      <td>
        **Mô tả:**\
        (Các) Nhóm người dùng thuộc (các) Tổ chức đã chọn.\
        **Quy tắc nhập:**\
        **Biểu mẫu Web:**\
        Nhấn vào trường này. Trên thanh tìm kiếm của trình đơn xổ xuống, nhập **Tên Nhóm/Mã Nhóm** của Nhóm người dùng cần tìm, sau đó tích ô chọn của giá trị trả về.\
        **Tệp nhập Excel:**\
        Sao chép Mã Nhóm của Nhóm người dùng phù hợp trên ứng dụng Web, sau đó dán vào ô này.\
        **Lưu ý:**\
        Khi bạn sử dụng Biểu mẫu Web, bạn có thể lựa chọn nhiều Nhóm người dùng. Tuy nhiên, trên Tệp nhập Excel, bạn chỉ có thể điền một Mã Nhóm người dùng duy nhất.\
        Mã Nhóm người dùng và Tên Nhóm người dùng có thể được tìm thấy ở các cột **Mã Nhóm** và **Tên Nhóm** ở tab **Tổ chức > Nhóm người dùng**.
      </td>
    </tr>

    <tr>
      <td>
        Tên đăng nhập\
        (Biểu mẫu Web + Tệp nhập Excel)\
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        Tên đăng nhập của Người dùng đang được tạo. Người dùng sẽ sử dụng tên đăng nhập để đăng nhập vào ứng dụng Web và ứng dụng di động.\
        **Quy tắc nhập:**\
        Định dạng: Có thể chứa chữ cái, số, ký tự đặc biệt (bao gồm cả dấu cách)
      </td>
    </tr>

    <tr>
      <td>
        Mật khẩu; Nhập lại mật khẩu\
        (Biểu mẫu Web)\
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        Mật khẩu của Người dùng đang được tạo. Người dùng sẽ sử dụng mật khẩu để đăng nhập vào ứng dụng Web và ứng dụng di động.\
        **Quy tắc nhập:**\
        Mật khẩu phải tuân theo các [**Nguyên tắc mật khẩu mạnh**]().\
        Phải nhập chung giá trị mật khẩu vào cả hai trường **Mật khẩu** và **Nhập lại mật khẩu**.\
        **Lưu ý:**\
        Các  trường này không có trong Tệp nhập Excel. Nếu như bạn tạo Người dùng bằng Tệp nhập Excel, hệ thống sẽ tự động tạo các mật khẩu ngẫu nhiên cho từng Người dùng và sẽ gửi email chứa mật khẩu ngẫu nhiên tới địa chỉ email của từng Người dùng.
      </td>
    </tr>

    <tr>
      <td>
        Email\
        (Biểu mẫu Web + Tệp nhập Excel)\
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        Địa chỉ email của Người dùng đang được tạo.\
        **Quy tắc nhập:**\
        Hãy nhập địa chỉ email chính xác, có thể truy cập\
        **Lưu ý khi sử dụng Tệp nhập Excel:**\
        Bạn phải xoá hết các siêu liên kết khỏi các địa chỉ email trước khi tải tệp lên. Hướng dẫn xoá siêu liên kết được trình bày tại bài viết sau: [**Các chức năng hệ thống**]()
      </td>
    </tr>

    <tr>
      <td>
        Số điện thoại\
        (Biểu mẫu Web + Tệp nhập Excel)\
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        Số điện thoại của Người dùng đang được tạo.\
        **Quy tắc nhập:**\
        Định dạng: Chỉ chứa chữ số.\
        Ví dụ: ***0901810800*** hợp lệ. ***090 181 0800*** hoặc ***090.181.0800*** không hợp lệ.
      </td>
    </tr>

    <tr>
      <td>
        Họ tên\
        (Biểu mẫu Web + Tệp nhập Excel)\
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        Tên đầy đủ của Người dùng đang được tạo.\
        **Quy tắc nhập:**\
        Định dạng: Có thể chứa chữ cái, số, ký tự đặc biệt (bao gồm cả dấu cách).
      </td>
    </tr>

    <tr>
      <td>
        Loại phương tiện (Biểu mẫu Web); Kiểu phương tiện (Tệp nhập Excel)\
        (Tuỳ chọn)\
        Trên Biểu mẫu Web, trường này nằm ở phần **Các thiết lập khác**
      </td>

      <td>
        **Mô tả:**\
        Loại phương tiện mà Người dùng đang được tạo sẽ điều khiển.\
        **Quy tắc nhập:**\
        Nếu như bạn sử dụng các Loại phương tiện mặc định của hệ thống, hãy thực hiện như sau:\
        **Biểu mẫu Web:**\
        Nhấn vào trường này. Trên trình đơn xổ xuống, tích chọn một trong các Loại phương tiện sau: **Xe tải; Xe bán tải; Xe máy**.\
        **Tệp nhập Excel:**\
        Nếu Người dùng đang được tạo sẽ điều khiển **Xe tải**, hãy nhập giá trị sau vào ô này: ***truck***.\
        Nếu Người dùng đang được tạo sẽ điều khiển **Xe bán tải**, hãy nhập giá trị sau vào ô này: ***semi-truck***.\
        Nếu Người dùng đang được tạo sẽ điều khiển **Xe máy**, hãy nhập giá trị sau vào ô này: ***bike***.\
        Nếu như bạn sử dụng các Loại phương tiện tuỳ chỉnh, hãy thực hiện như sau:
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

#### Driver-specific information

* Apart from the basic information fields above, there will be some additional information fields for Users who are Drivers (Deliverymen). These fields are optional, however
* On the Webform, these information fields will be visible when you click on the ***MORE CONFIGURATIONS*** text

<Image title="Selection_003.png" alt={1898} className="border" border={true} src="https://files.readme.io/ad552bc-Selection_003.png" />

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Information field
      </th>

      <th>
        Description & Input
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Vehicle Type (Webform); Type Of Vehicle (Excel File)
        (Optional Field)
      </td>

      <td>
        **1. Description:**\
        The Vehicle Type that the Driver being created will operate\
        One Driver can only operate one Vehicle Type\
        **2. Input rules:**\
        **Webform:**\
        Click on this field. Select the appropriate Vehicle Type from the drop-down menu\
        **Excel file:**\
        If you use the default Vehicle Types of this model (Truck; Semi-truck and Motorbike), then input as follows:\
        If the User being created operates trucks, input the following value: ***"truck"***. Omit the quotation marks when inputting\
        If the User being created operates semi-trucks, input the following value: ***"semi-truck"***. Omit the quotation marks when inputting\
        If the User being created operates motorbikes, input the following value: ***"bike"***. Omit the quotation marks when inputting\
        If you use custom Vehicle Types, copy the appropriate Vehicle Type Code from the Web app then paste it into this cell\
        **Notes:**\
        The Vehicle Type Code can be found under the "Type Code" column in the "Transportation > Vehicle Types" tab\
        In the Excel file, this value is case sensitive. Do not input values such as: ***Truck; BIKE***\
        With the default Vehicle Types, this value must always be input in English as shown above. Do not input in any other language, for example, ***Xemay; Xetai***
      </td>
    </tr>

    <tr>
      <td>
        Position\
        (Webform + Excel File)\
        (Optional Field)
      </td>

      <td>
        **1. Description:**\
        Position of the driver being created in the driver user group\
        **2. Input rules:**\
        **Web form:**\
        Click on this field then choose from the drop down menu\
        **Excel template:**\
        Input the following value into the cell if the driver being created is a Light duty truck driver: ***"LDD"***. Omit the quotation marks when inputting\
        Input the following value into the cell if the driver being created is a Heavy duty truck driver: ***"HDD"***. Omit  the quotation marks when inputting\
        Input the following value into the cell if the driver being created is the leader of the driver group: ***"Driver Leader"***. Omit the quotation marks when inputting\
        Input the following value into the cell if the driver being created is a driver who normally operates motorbikes: ***"Delivery Man"***. Omit the quotation marks when inputting\
        **Note when using Excel template:**\
        This value is case-sensitive. You must input one of the values as shown above into the cell
      </td>
    </tr>

    <tr>
      <td>
        Driver License Number\
        (Webform + Excel File)\
        (Optional Field)
      </td>

      <td>
        **1. Description:**\
        Driver license number of the driver being created\
        **2. Input rules:**\
        Format: Must not contain spaces
      </td>
    </tr>

    <tr>
      <td>
        License Class\
        (Webform + Excel File)\
        (Optional Field)
      </td>

      <td>
        **1. Description:**\
        License class of the driver being created\
        **2. Input rules:**\
        **Web form:**\
        Click on this field. Select the appropriate license class from the drop down menu\
        You can select more than one value, meaning the driver being created has more than one license class\
        **Excel template:**\
        Input license class like on Web form into the cell\
        If the driver being created has more than one license class, separate two adjacent license classes only by commas. Do not add spaces\
        For example: The driver being created has two driver licenses of class A and class B. Input the following value into this cell: ***A,B***
      </td>
    </tr>

    <tr>
      <td>
        Medically Cleared\
        (Webform + Excel File)\
        (Optional Field)
      </td>

      <td>
        **1. Description:**\
        Specify whether the driver being created has passed the required medical examination of your organization or not\
        **2. Input rules:**\
        **Web form:**\
        Click on the check box if the user being created has passed required medical exams\
        **Excel template:**\
        Input the following value into the cell if the driver being created has passed required medical examination: TRUE\
        Input the following value into the cell if the driver being created has not passed required medical examination: FALSE\
        **Note when using Excel template:**\
        This field is case sensitive. You must input one of the exact values above into this cell
      </td>
    </tr>

    <tr>
      <td>
        Secret\
        (Webform)\
        (Optional Field)
      </td>

      <td>
        **1. Description:**\
        Secret of the driver being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        sub scription Code\
        (Webform)\
        (Optional Field)
      </td>

      <td>
        **1. Description:**\
        Subscription Code of the driver being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>

    <tr>
      <td>
        sub scription Expiry\
        (Webform)\
        (Optional Field)
      </td>

      <td>
        **1. Description:**\
        Subscription Expiry date of the driver being created\
        **2. Input rules:**\
        Format: Free-form
      </td>
    </tr>
  </tbody>
</Table>

## Change Active Status of Driver Users

* Besides the **Organizations > Users** tab, the driver users also have a dedicated tab, **Transportation > Drivers**. On this tab, you can change their Active Status

<Image title="Image 1.png" alt={1908} border={true} src="https://files.readme.io/034a67e-Image_1.png">
  Illustration Image (English)
</Image>

<Image title="TbbLskRJah.png" alt={1920} border={true} src="https://files.readme.io/18eeff8-TbbLskRJah.png">
  Illustration Image (Vietnamese)
</Image>

* By default, after being created, all drivers will have the Active Status ***Active***, represented by the icon :fa-check-square-o: under the column **Active**. This means the drivers can be selected to operate the vehicles during the Route Plan optimization process

<Image title="ALrvcwY47H.png" alt={1309} className="border" border={true} src="https://files.readme.io/3bf144c-ALrvcwY47H.png" />

* To change the active status of a driver, click on that icon. When that icon turns to :fa-square-o:, that means the Active Status of the driver has been switched to ***Inactive***, which means that driver will not appear anymore in the Route Plan optimization process, unless prior to this you have locked a Delivery Shift with that driver

## Beginner's Guide

After creating an organizational chart (you can see the tutorial for beginners [here](https://docs.abivin.com/docs/vrp-in-house-fleet-manage-organizations#beginners-guide)), you can proceed to the next step in the Route Optimization Process: Creating users. In this tutorial, we will determine users as drivers.

### Create a User Group

* Below are the simple steps on how to create a Driver user group using Web form:

* Step 1: Navigate to **Organizations > User Group** tab.

* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Create** (the :fa-pencil: symbol).

![2876](https://files.readme.io/bc1d34a-Screen_Shot_2021-01-22_at_10.56.59.png "Screen Shot 2021-01-22 at 10.56.59.png")

* Step 3: Input information to complete the **Group Information** section. There are 3 required fields:
* **Group Code:** Input the following value: ***SAMPLE-DELIVERER***
* **Organization:** The organization type must be Depot/Sun: ***Sample Depot***
* **Group Name:** Input the name of the Driver user group: ***Sample Deliverers***
* *Example*: 

![2880](https://files.readme.io/27785d5-Screen_Shot_2021-01-22_at_11.07.35.png "Screen Shot 2021-01-22 at 11.07.35.png")

* Step 4: In the **Configurations** section, set up the modules that the  Driver User Group can get access to, and the corresponding level of authority over those modules by ticking the boxes:

![1220](https://files.readme.io/0c484aa-Screen_Shot_2021-01-22_at_13.47.12.png "Screen Shot 2021-01-22 at 13.47.12.png")

* Step 5: Click **SAVE**
* Beside Web form, Excel files can be used to create a Driver user group. Here are the steps to import an Excel file into the system:
* Step 1: Navigate to **Organizations > User Group** tab.
* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Import**.
* Step 3: Choose the Excel you want to import by dropping it to the area or clicking the area.
* **Note:** The chosen file must be in the right format and contain required fields (Group Code, Organization, Group Name). You can also download a sample with a correct format provided by us. To do this, click **DOWNLOAD SAMPLE**. Then you can paste your data onto the sample file.

### Create a User

Next, here are the steps you should follow to create a user (driver)

* Step 1: Navigate to **Organizations > Users** tab.
* Step 2: Click on the :fa-plus-circle: symbol :fa-arrow-right: **Create** (the :fa-pencil: symbol).

![2880](https://files.readme.io/75f57f3-Screen_Shot_2021-01-22_at_13.49.18.png "Screen Shot 2021-01-22 at 13.49.18.png")

* Step 3: Fill in information to complete the User information section. These are the required fields:
* **Organization Name:** Input the organization in which the user being created belongs: ***Sample Depot***
* **Username:** Input the username the driver will use to login to  the Web app/Mobile app
* **Phone Number:** Input the phone number of the driver being created
* **Full Name:** Input the full name of the driver being created
* **Password/Re-password:** Input the password the driver will use to login to Web app/Mobile app. The password must follow [password rules](https://docs.abivin.com/docs/web-app-account#password-rules)
* **E-mail:** Input the e-mail address of the driver being created. After being created, each new user will receive a email attached with a random password. The user must use that password to log in their account on the first time. After successfully logging in, they can freely change the password as instructed in the following article: [Change login password](https://docs.abivin.com/docs/web-app-account#change-login-password)

![2880](https://files.readme.io/4f7420a-Screen_Shot_2021-01-22_at_13.59.56.png "Screen Shot 2021-01-22 at 13.59.56.png")

* **Vehicle:** Click **MORE CONFIGURATIONS:fa-caret-down:** for the **Vehicle** field to be shown, then click on vehicle assigned to the driver. 

![2880](https://files.readme.io/18513ca-Screen_Shot_2021-01-22_at_14.03.20.png "Screen Shot 2021-01-22 at 14.03.20.png")

* Step 4: Click **SAVE**
