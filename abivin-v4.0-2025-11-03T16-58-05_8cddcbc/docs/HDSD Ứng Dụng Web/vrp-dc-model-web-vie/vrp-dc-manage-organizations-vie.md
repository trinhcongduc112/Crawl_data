---
title: Quản lý Tổ chức
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
## Định nghĩa Tổ chức

Trong hệ thống Abivin vRoute, chúng tôi cố gắng mô phỏng sơ đồ tổ chức thực tế của doanh nghiệp để người dùng có thể quản lý tài nguyên một cách trực quan và hiệu quả.\
Tài nguyên **Tổ chức** được tạo ra để phục vụ mục tiêu đó. Sau khi bạn đã đăng ký tài khoản chính trên hệ thống của chúng tôi, bạn có thể bắt đầu xây dựng sơ đồ tổ chức của bạn.

## Loại tổ chức

Trong hệ thống Abivin vRoute nói chung và trong mô hình này nói riêng, các Tổ chức có thể được phân thành hai Loại tổ chức dựa trên tính bắt buộc của chúng: **Loại tổ chức bắt buộc** và **Loại tổ chức tuỳ chọn (Không bắt buộc)**.

### Loại tổ chức bắt buộc

Loại tổ chức bắt buộc là những Loại tổ chức mà nếu không được tạo thì tài khoản của bạn sẽ không thể hoạt động được.\
Dưới đây là những Loại tổ chức bắt buộc của mô hình này:

#### Nhà sản xuất

Nhà sản xuất là Loại tổ chức đại diện cho trụ sở chính của doanh nghiệp của bạn. Loại tổ chức này sẽ quản lý tất cả các tài nguyên trong toàn bộ hệ thống của bạn.\
Nhà sản xuất là Tổ chức cấp cao nhất trong cây tổ chức trên tài khoản của bạn. Lưu ý rằng một tài khoản chính chỉ có thể có ***duy nhất một*** Tổ chức thuộc loại Nhà sản xuất.

#### Chi nhánh

Chi nhánh là một Loại tổ chức đại diện cho Phòng kế hoạch hay Bộ phận điều phối. Tại Loại tổ chức này, bạn sẽ xây dựng các thiết lập và quản lý qá trình tối ưu Kế hoạch lộ trình.\
Chi nhánh là Tổ chức cấp dưới trực tiếp của Nhà sản xuất hoặc của một Loại tổ chức không bắt buộc là Nhà phân phối (Được mô tả bên dưới). Trên một tài khoản bạn có thể tạo nhiều Chi nhánh.

#### Kho

Kho (Hay còn gọi là Kho cấp một để phân biệt với các Loại tổ chức Kho cấp hai là Kho Sun và Kho trung chuyển) là Loại tổ chức đại diện cho Kho hàng. Loại tổ chức này sẽ trực tiếp quản lý các tài nguyên của hoạt động giao hàng như Sản phẩm, Khách hàng; Phương tiện và Đơn hàng.\
Kho là Tổ chức cấp dưới trực tiếp của Chi nhánh. Mỗi Chi nhánh có thể có nhiều Kho trực thuộc.

### Loại tổ chức tùy chọn

Loại tổ chức tùy chọn là những Loại tổ chức không bắt buộc cần phải tạo. Bạn có thể tạo chúng sau dựa trên nhu cầu cụ thể của mình.\
Dưới đây là những Loại tổ chức tuỳ chọn của mô hình này:

#### Nhà phân phối

Nhà phân phối là Loại tổ chức đại diện cho Bộ phận quản lý vùng, quản lý các chi nhánh thuộc các khu vực địa lý nhỏ hơn (Tỉnh, thành phố, v.v.).\
Nhà phân phối là Tổ chức cấp dưới trực tiếp của Nhà sản xuất và là Tổ chức cấp trên trực tiếp của Chi nhánh. Một tài khoản có thể có nhiều Nhà phân phối. Một Nhà phân phối có thể có nhiều Chi nhánh trực thuộc.

#### Kho Sun

Kho Sun là một Loại tổ chức Kho cấp hai, là cấp dưới trực tiếp của Kho cấp một. Kho Sun sẽ nhận Sản phẩm từ Kho cấp một cấp trên trực tiếp, sau đó phân phối đến tập Khách hàng của Kho Sun đó.\
Đọc thêm về Loại tổ chức này trong bài viết sau: [**Kho Sun**]().

#### Kho trung chuyển

Kho trung chuyển là một Loại tổ chức Kho cấp hai, là cấp dưới trực tiếp của Kho cấp một. Kho trung chuyển sẽ tạm thời lưu trữ Sản phẩm từ Kho cấp một cấp trên trực tiếp, sau đó phân phối đến tập Khách hàng của Kho trung chuyển đó.\
Đọc thêm về Loại tổ chức này trong bài viết sau: [**Kho trung chuyển**]().

#### Chủ hàng

Chủ hàng là một Loại tổ chức đặc biệt. Loại tổ chức này được sử dụng khi bạn thiết lập tài khoản của mình với tư cách là Nhà vận tải hoặc Nhà phân phối, những đơn vị cung cấp dịch vụ hậu cần bên thứ ba cho các Nhà cung cấp/Chủ sở hữu Sản phẩm. Loại tổ chức này đại diện cho các Nhà cung cấp/Chủ sở hữu Sản phẩm đó.\
Chủ hàng là Tổ chức cấp dưới trực tiếp của Nhà sản xuất hoặc Nhà phân phối.\
Đọc thêm về Loại tổ chức này trong bài viết sau: [**Chủ hàng**]().

## Định hướng thiết lập tài khoản

Trong mô hình này, bạn có thể thiết lập tài khoản của mình theo một trong hai định hướng sau tuỳ thuộc vào hoạt động kinh doanh thực tế của bạn: **Định hướng Chủ hàng** và **Định hướng Nhà vận tải/Nhà phân phối**.

### Thiết lập tài khoản Định hướng Chủ hàng

Bạn sẽ thiết lập tài khoản của mình theo định hướng này nếu bạn chính là Chủ hàng, là Nhà cung cấp/Chủ sở hữu trực tiếp của Sản phẩm. Bạn sở hữu đội Phương tiện giao hàng riêng và bạn sử dụng đội Phương tiện của mình để phân phối Sản phẩm đến các Kênh phân phối hoặc tới Người tiêu dùng.\
Định hướng thiết lập tài khoản này có một số đặc điểm sau:\
**Sơ đồ tổ chức**: Trong cây sơ đồ tổ chức của bạn, bạn không cần phải tạo Loại tổ chức Chủ hàng.\
**Cơ chế quản lý sản phẩm**: Bạn cần thiết lập Cơ chế quản lý Sản phẩm Định hướng Chủ hàng. Hướng dẫn chi tiết được mô tả trong các bài viết sau (Nhấn vào tên bài để chuyển tới nội dung bài): [**Quản lý Danh mục sản phẩm**]() và [**Quản lý Sản phẩm**]().

### Thiết lập tài khoản Định hướng Nhà vận tải/Nhà phân phối

Bạn sẽ thiết lập tài khoản của mình theo định hướng này nếu bạn là Nhà vận tải và/hoặc Nhà phân phối. Bạn cung cấp dịch vụ logistics (vận chuyển, kho bãi) cho các Chủ hàng. Bạn có đội Phương tiện riêng và có thể là cả Kho hàng riêng. Bạn sử dụng đội Phương tiện của mình để phân phối Sản phẩm của Chủ hàng đến các Khách hàng của các Chủ hàng đó.\
Định hướng thiết lập tài khoản này có một số đặc điểm sau:\
**Sơ đồ tổ chức**: Trong cây sơ đồ tổ chức của bạn, bạn cần tạo Loại tổ chức Chủ hàng. Mỗi Tổ chức Chủ hàng sẽ đại diện cho một đơn vị sản xuất sản phẩm mà tổ chức của bạn có mối quan hệ kinh doanh trong hoạt động thực tế.\
**Cơ chế quản lý sản phẩm**: Bạn cần thiết lập Cơ chế quản lý Sản phẩm Định hướng Nhà vận tải/Nhà phân phối. Hướng dẫn chi tiết được mô tả trong các bài viết sau (Nhấn vào tên bài để chuyển tới nội dung bài): [**Quản lý Danh mục sản phẩm**]() và [**Quản lý Sản phẩm**]().

## Định vị Danh sách Tổ chức

Bản ghi các Tổ chức được liệt kê ở tab **Tổ chức > Tổ chức**.

## Tạo Tổ chức

Bạn có hai phương pháp để tạo Tổ chức: **Biểu mẫu Web** và **Tệp nhập Excel**.\
Mô tả và cách nhập liệu của các trường thông tin cụ thể của Tổ chức được mô tả ở phần sau trong bài viết này: [**Trường thông tin Tổ chức**]().

### Tạo Nhà sản xuất

Nhà sản xuất là Tổ chức đầu tiên bạn phải tạo trên tài khoản của bạn. Lưu ý rằng Tổ chức này chỉ có thể được tạo bằng cách sử dụng Biểu mẫu Web.\
Trên Biểu mẫu Web, hãy nhập thông tin của Nhà sản xuất vào các trường thông tin sau: **Mã tổ chức** và **Tên tổ chức**. Sau khi đã nhập thông tin, hãy nhấn nút **Lưu lại** để tạo Nhà sản xuất đó trong cơ sở dữ liệu.\
Tiếp theo, hãy nhấn vào biểu tượng **Chỉnh sửa** :fa-pencil: của chính Nhà sản xuất mà bạn vừa tạo. Biểu mẫu **Thông tin Tổ chức** sẽ hiện ra. Trên biểu mẫu này, hãy nhấn vào trường **Tổ chức cha** và chọn chính Nhà sản xuất vừa tạo làm Tổ chức cha của chính nó. Kế tiếp, hãy nhấn vào trường **Danh mục Tổ chức**, chọn loại tổ chức **Nhà sản xuất** từ trình đơn xổ xuống. Cuối cùng nhấn **Lưu lại** để xác nhận thay đổi.\
Như vậy là bạn đã tạo xong Tổ chức Nhà sản xuất. Bạn có thể tiếp tục tạo các Tổ chức cấp thấp hơn bằng cách sử dụng Biểu mẫu Web hoặc Tệp nhập Excel.

### Tạo các Tổ chức cấp thấp

Nếu bạn sử dụng Tệp nhập Excel để tạo các Tổ chức cấp thấp, có một số lưu ý sau:

1. Khi bạn tạo các Tổ chức cấp dưới trực tiếp của Nhà sản xuất - Nhà phân phối hoặc Chi nhánh, thì bạn phải sao chép chính xác giá trị Mã tổ chức của Nhà sản xuất trên ứng dụng Web sau đó dán vào ô **Mã tổ chức cha** của các Nhà phân phối/Chi nhánh mà bạn muốn tạo trong Tệp nhập Excel.

2) Khi bạn tạo những Tổ chức chưa tồn tại trên ứng dụng Web, hãy làm theo bước sau để tạo mối quan hệ Cha-Con giữa một Tổ chức cấp trên và một Tổ chức cấp dưới trực tiếp (Ví dụ: Giữa một Chi nhánh và một Kho trực thuộc Chi nhánh đó) trong Tệp nhập Excel:\
   Bước 1: Sao chép Mã tổ chức của Tổ chức cấp trên từ ô **Mã tổ chức** của Tổ chức cấp trên đó.\
   Bước 2: Dán giá trị Mã tổ chức vừa sao chép vào ô **Mã tổ chức cha** của Tổ chức cấp dưới trực tiếp của Tổ chức cấp trên đó.

### Trường thông tin Tổ chức

Dưới đây là các trường thông tin và quy tắc nhập liệu cho tài nguyên Tổ chức của mô hình này.\
**Lưu ý**: 

1. Có thể có một số trường thông tin không sử dụng cho mô hình này và do đó sẽ không được đề cập trong bảng dưới.
2. Có hai loại trường thông tin: **Bắt buộc** - Những trường thông tin bắt buộc phải nhập, không được để trống, và **Tuỳ chọn** -  Những trường thông tin không bắt buộc phải nhập, có thể để trống. Chúng tôi sẽ chỉ rõ tính chất bắt buộc của từng trường thông tin
3. Trên Biểu mẫu Web, thông tin của một Tổ chức được liệt kê ở hai tab **Thông tin chung** và **Các thiết lập khác**. Tab Thông tin chung sẽ chứa những thông tin cơ bản nhất của Tổ chức. Tab Các thiết lập khác sẽ chứa những thông tin, những thiết lập chuyên sâu hơn, được sử dụng cho nhiều chức năng có liên quan tới Tổ chức đó.\
   Chúng tôi có một bài viết riêng để liệt kê danh sach các thiết lập của các Loại tổ chức trên tab Các thiết lập khác: [**Thiết lập theo Loại tổ chức**]().

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Trường thông tin
      </th>

      <th>
        Mô tả & Quy tắc nhập
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Mã Tổ chức
        (Biểu mẫu Web + Tệp nhập Excel)
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        Mã tổ chức được gán cho Tổ chức đang được tạo.\
        **Quy tắc nhập:**\
        Định dạng: Có thể chứa chữ cái, chữ số, ký tự đặc biệt. Không được chứa dấu cách và dấu thanh (Dấu huyền, dấu sắc, dấu ngã v.v.).\
        Ví dụ: ***To\_chuc\_01*** hợp lệ. ***Tổ chức 01*** không hợp lệ.\
        **Ghi chú:**\
        Khi bạn sử dụng Biểu mẫu Web, tất cả các ký tự của giá trị nhập vào sẽ tự động được viết hoa. Ngoài ra các dấu cách sẽ được tự động chuyển thành dấu gạch ngang (-)\
        Ví dụ: Nếu bạn nhập giá trị ***Ma to chuc mau***, giá trị này sẽ tự động được chuyển thành ***MA\_TO\_CHUC\_MAU***.\
        Khi bạn sử dụng Tệp nhập Excel, giá trị nhập vào sẽ không được viết hoa tự động sau khi tải lên như với Biểu mẫu Web.\
        Mã này phân biệt chữ viết hoa và chữ viết thường.\
        Ví dụ: ***Ma\_To\_Chuc*** khác với ***MA\_TO\_CHUC***. Bạn hãy lưu ý điều này khi sao chép Mã tổ chức.
      </td>
    </tr>

    <tr>
      <td>
        Tên Tổ chức\
        (Biểu mẫu Web + Tệp nhập Excel)\
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        Tên của Tổ chức đang được tạo.\
        **Quy tắc nhập:**\
        Định dạng: Nhập tự do (Có thể chứa chữ cái, chữ số, ký tự đặc biệt và dấu cách).
      </td>
    </tr>

    <tr>
      <td>
        Tổ chức cha (Biểu mẫu Web); Mã tổ chức cha (Tệp nhập Excel)\
        (Bắt buộc)
      </td>

      <td>
        **Mô tả:**\
        Tổ chức cấp trên trực tiếp của Tổ chức đang được tạo.\
        **Quy tắc nhập:**\
        **Biểu mẫu Web:**\
        Nhấn vào trường này. Nhập **Tên tổ chức/Mã tổ chức** của Tổ chức cấp trên của Tổ chức đang được tạo vào thanh tìm kiếm của trình đơn xổ xuống sau đó chọn giá trị trả về.\
        **Tệp nhập Excel:**\
        Sao chép giá trị **Mã tổ chức** của Tổ chức cấp trên của Tổ chức đang được tạo trên ứng dụng Web, sau đó dán vào ô này trong tệp.\
        **Ghi chú:**\
        Có thể tìm Tên tổ chức và Mã tổ chức ở các cột cùng tên trong tab **Tổ chức > Tổ chức**
      </td>
    </tr>

    <tr>
      <td>
        Loại tổ chức (Biểu mẫu Web); Mã loại tổ chức (Tệp nhập Excel)\
        (Tùy chọn)
      </td>

      <td>
        **Mô tả:**\
        Xác định Tổ chức đang được tạo thuộc Loại tổ chức cụ thể nào.\
        **Quy tắc nhập:**\
        **Biểu mẫu Web:**\
        Nhấn vào trường này. Chọn Loại tổ chức thích hợp từ trình đơn thả xuống.\
        **Tệp nhập Excel:**\
        Nếu Tổ chức đang được tạo thuộc loại **Nhà phân phối**, hãy nhập giá trị sau vào ô này: ***DISTRIBUTOR***\
        Nếu Tổ chức đang được tạo thuộc loại **Chi nhánh**, hãy nhập giá trị sau vào ô này: ***BRANCH***\
        Nếu Tổ chức đang được tạo thuộc loại **Kho cấp 1**, hãy nhập giá trị sau vào ô này (Bỏ dấu ngoặc kép khi nhập): ***DEPOT***\
        Nếu Tổ chức đang được tạo thuộc loại **Kho Sun**, hãy nhập giá trị sau vào ô này (Bỏ dấu ngoặc kép khi nhập): ***SUN***\
        Nếu Tổ chức đang được tạo thuộc loại **Kho trung chuyển**, hãy nhập giá trị sau vào ô này: ***CROSSDOCK***\
        Nếu Tổ chức đang được tạo thuộc loại **Chủ hàng**, hãy nhập giá trị sau vào ô này: ***SHIPPER***\
        **Lưu ý khi sử dụng Tệp nhập Excel:**\
        Bạn phải nhập các giá trị chính xác bằng tiếng Anh và bằng chữ in hoa như trên. Bạn không được nhập bất cứ giá trị nào khác.
      </td>
    </tr>

    <tr>
      <td>
        Vĩ độ, Kinh độ\
        (Biểu mẫu Web + Tệp nhập Excel)\
        (Tùy chọn)
      </td>

      <td>
        **Mô tả:**\
        Thông tin tọa độ của Tổ chức đang được tạo.\
        **Quy tắc nhập:**\
        Định dạng: Độ thập phân\
        Ví dụ: ***41.40338*** và ***2.17403***\
        **Ghi chú:**\
        Các trường thông tin này rất quan trọng đối với các Tổ chức thuộc loại **Kho cấp 1 (Kho); Kho Sun; Kho trung chuyển** vì sẽ được sử dụng trong quá trình tối ưu Kế hoạch lộ trình.
      </td>
    </tr>

    <tr>
      <td>
        Giờ mở cửa; Giờ đóng cửa\
        (Biểu mẫu Web + Tệp nhập Excel)\
        (Tùy chọn)
      </td>

      <td>
        **Mô tả:**\
        Thời gian làm việc chính thức của Tổ chức đang được tạo.\
        **Quy tắc nhập:**\
        Định dạng: HH:mm (Giờ:Phút; định dạng 24 giờ)\
        Ví dụ: Tổ chức đang được tạo bắt đầu hoạt động lúc tám giờ ba mưới sáng và đóng cửa lúc năm giờ ba mươi chiều hàng ngày. Bạn cần nhập giá trị ***08:30*** vào trường/ô **Giờ mở cửa** và giá trị ***17:30*** vào trường/ô **Giờ đóng cửa**.\
        **Ghi chú:**\
        Trường **Giờ mở cửa** rất quan trọng đối với Tổ chức thuộc loại **Kho cấp 1; Kho Sun; Kho trung chuyển** vì sẽ được sử dụng trong quá trình tối ưu Kế hoạch lộ trình.
      </td>
    </tr>

    <tr>
      <td>
        Địa chỉ\
        (Biểu mẫu Web + Tệp nhập Excel)\
        (Tùy chọn)
      </td>

      <td>
        **Mô tả:**\
        Địa chỉ địa lý của Tổ chức đang được tạo.\
        **Quy tắc nhập:**\
        Định dạng: Nhập tự do.
      </td>
    </tr>

    <tr>
      <td>
        Quốc Gia\
        (Biểu mẫu Web)\
        (Tùy chọn)
      </td>

      <td>
        **Mô tả:**\
        Thiết lập quốc gia nơi doanh nghiệp của bạn đặt trụ sở.\
        **Quy tắc nhập:**\
        Nhấn vào trường này. Chọn quốc gia thích hợp từ danh sách xổ xuống.
      </td>
    </tr>

    <tr>
      <td>
        Đơn vị tiền tệ\
        (Biểu mẫu Web)\
        (Tùy chọn)
      </td>

      <td>
        **Mô tả:**\
        Thiết lập đơn vị tiền tệ trên toàn hệ thống.\
        **Quy tắc nhập:**\
        Đơn vị tiền tệ sẽ tự động cập nhật khi bạn chọn thông tin Quốc gia ở trên.\
        Bạn có thể thiết lập đơn vị tiền tệ theo cách thủ công bằng cách nhấn vào trường này và chọn đơn vị tiền tệ phù hợp từ danh sách xổ xuống.
      </td>
    </tr>

    <tr>
      <td>
        Ngày đầu tuần\
        (Biểu mẫu Web)\
        (Tùy chọn)
      </td>

      <td>
        **Trường thông tin này chỉ yêu cầu đối với một số tài khoản cụ thể.**\
        **Mô tả:**\
        Thiết lập ngày làm việc đầu tiên trong một tuần.\
        Giá trị này sẽ ảnh hưởng đến một báo cáo cụ thể.\
        **Quy tắc nhập:**\
        Nhấn vào trường này. Chọn ngày thích hợp từ danh sách xổ xuống.
      </td>
    </tr>

    <tr>
      <td>
        Ngày làm việc\
        (Biểu mẫu Web)\
        (Tùy chọn)
      </td>

      <td>
        **Trường thông tin này chỉ yêu cầu đối với một số tài khoản cụ thể.**\
        **Mô tả:**\
        Thiết lập các ngày làm việc trong một tuần.\
        Giá trị này sẽ ảnh hưởng đến một báo cáo cụ thể.\
        **Quy tắc nhập:**\
        Nhấn vào trường này. Chọn ngày thích hợp từ danh sách xổ xuống.
      </td>
    </tr>

    <tr>
      <td>
        Múi giờ\
        (Biểu mẫu Web)\
        (Tùy chọn)\
        (Chỉ có tác dụng đối với Tổ chức **Nhà sản xuất**)
      </td>

      <td>
        **Mô tả:**\
        Múi giờ của vị trí địa lý của Tổ chức của bạn.\
        **Quy tắc nhập:**\
        Nhấn vào trường này. Chọn múi giờ thích hợp từ danh sách xổ xuống.
      </td>
    </tr>

    <tr>
      <td>
        Ngày thành lập\
        (Biểu mẫu Web)\
        (Tùy chọn)
      </td>

      <td>
        **Mô tả:**\
        Ngày mà Tổ chức của bạn chính thức được thành lập.\
        **Quy tắc nhập:**\
        Nhấn vào biểu tượng lịch :fa-calendar:. Chọn ngày thích hợp từ lịch thả xuống.
      </td>
    </tr>

    <tr>
      <td>
        Mô tả\
        (Biểu mẫu Web)\
        (Tùy chọn)
      </td>

      <td>
        **Mô tả:**\
        Mô tả ngắn gọn về Tổ chức đang được tạo.\
        **Quy tắc nhập:**\
        Định dạng: Nhập tự do.
      </td>
    </tr>

    <tr>
      <td>
        Thời gian nghỉ\
        (Biểu mẫu Web)\
        (Tùy chọn)
      </td>

      <td>
        **Trường thông tin này chỉ được yêu cầu cho một số tài khoản cụ thể và chỉ cần nhập đối với Tổ chức thuộc loại Kho cấp 1.**\
        **Mô tả:**\
        Khoảng thời gian mà Kho cấp một đang được tạo sẽ không cho phép các Phương tiện di chuyển vào và lấy Sản phẩm.\
        **Quy tắc nhập:**\
        Định dạng: HH:mm (Giờ:Phút; định dạng 24 giờ)\
        Nếu có nhiều khoảng thời gian nghỉ, chia hai khoảng thời gian cạnh nhau bằng dấu chấm phấy (;).\
        Ví dụ: Kho cấp một có hai khoảng thời gian nghỉ: Từ tám giờ sáng đến chín giờ ba mươi sáng và từ mười một giờ ba mươi sáng đến một giờ ba mươi chiều. Nhập giá trị sau vào trường này:

        * **08:00-09:30;11:30-13:30\***.
      </td>
    </tr>
  </tbody>
</Table>

## Cập nhật Tổ chức

Vui lòng tham khảo bài viết [**Các chức năng hệ thống**]() để biết các bước chung để cập nhật tài nguyên trong hệ thống Abivin vRoute.

## Xóa Tổ chức

Vui lòng tham khảo bài viết [**Các chức năng hệ thống**]() để biết các bước chung để xoá tài nguyên trong hệ thống Abivin vRoute.

> ❗️ THẬN TRỌNG KHI XÓA TỔ CHỨC!
>
> Nếu bạn xóa một bản ghi Tổ chức, tất cả bản ghi của các tài nguyên của Tổ chức đó cũng như của tất cả các tổ chức cấp thấp hơn trực thuộc Tổ chức đó sẽ bị xóa khỏi cơ sở dữ liệu hệ thống.\
> Ví dụ: Nếu bạn xóa một Chi nhánh, các tài nguyên của Chi nhánh đó cũng như của tất cả các Kho trực thuộc Chi nhánh đó sẽ bị xóa.

## Tìm kiếm và lọc Tổ Chức

### Tìm kiếm Tổ chức

Để tìm kiếm một Tổ chức nào đó, hãy nhập **Mã tổ chức** hoặc **Tên tổ chức** của Tổ chức đó vào ô tìm kiếm.

### Lọc Tổ chức

Bạn có thể lọc các Tổ chức có cùng thuộc tính **Loại tổ chức** hoặc có chung một **Tổ chức cấp trên** bằng cách nhấn vào cột **Loại tổ chức** và **Tổ chức cấp trên** sau đó tích vào các ô chọn mong muốn trong trình đơn xổ xuống.\
Ở cột Tổ chức cấp trên, bạn cũng có thể nhanh chóng tìm kiếm một Tổ chức cụ thể bằng cách nhập **Tên tổ chức** hoặc **Mã tổ chức** của Tổ chức cần tìm vào thanh tìm kiếm.\
Bạn có thể kết hợp cả hai bộ lọc này.

## Chế độ bản đồ

Để xem vị trí của các Tổ chức trên bản đồ, nhấn vào biểu tượng **Xem Bản đồ** (Bên cạnh trường Tìm kiếm).

**Lưu ý**: Để một Tổ chức có thể xuất hiện trên bản đồ, Tổ chức đó cần có thông tin toạ độ (Kinh độ, Vĩ độ).\
Trên bản đồ, mỗi Tổ chức được đánh dấu bởi một biểu tượng điểm đánh dấu bản đồ :fa-map-marker:.\
Nhấn vào từng biểu tượng điểm đánh dấu bản đồ :fa-map-marker: của Tổ chức mong muốn để hiển thị nhãn của Tổ chức đó.\
Để quay trở lại Danh sách Tổ chức, hãy nhấn vào biểu tượng **Xem bảng dữ liệu** :fa-table:.

## Hướng dẫn cho người mới bắt đầu

Phần này dành cho những người dùng mới bắt đầu sử dụng hệ thống. Chúng tôi sẽ hướng dẫn bạn thiết lập một sơ đồ tổ chức ở mức độ đơn giản nhất.\
Về cơ bản, trong tài khoản của bạn, bạn sẽ cần một hệ thống phân cấp Tổ chức bao gồm: 

* Một Nhà sản xuất
* Một Chi nhánh
* Và một Kho cấp 1

### Tạo Nhà sản xuất

Để bắt đầu, hãy tạo một Tổ chức thuộc loại **Nhà sản xuất** bằng Biểu mẫu Web.\
Thao tác tạo Nhà sản xuất khá đơn giản và [đã được mô tả phía trên](https://docs.abivin.com/docs/vrp-dc-manage-organizations-vie#t%E1%BA%A1o-nh%C3%A0-s%E1%BA%A3n-xu%E1%BA%A5t).

### Tạo Chi nhánh và Kho

Sau khi đã tạo Nhà sản xuất, bạn cần tạo một Chi nhánh và một Kho cấp 1 trực thuộc Chi nhánh đó.\
Bạn có thể tạo hai Tổ chức này bằng Biểu mẫu Web hoặc Tệp nhập Excel.\
Đối với Chi nhánh, bạn chỉ cần nhập các thông tin sau: **Mã tổ chức, Tên tổ chức, Tổ chức cha, Loại tổ chức**.\
Đối với Kho cấp 1, bạn cần nhập các thông tin sau: **Mã tổ chức, Tên tổ chức, Tổ chức cha, Loại tổ chức, Giờ mở cửa, Giờ đóng cửa, Vĩ độ, Kinh độ**.
