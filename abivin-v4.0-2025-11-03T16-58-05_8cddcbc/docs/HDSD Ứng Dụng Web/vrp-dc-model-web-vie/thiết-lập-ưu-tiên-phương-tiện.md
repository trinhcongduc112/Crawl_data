---
title: Thiết lập Ưu tiên Phương tiện
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
* Bài viết này sẽ giải thích cách bạn có thể linh hoạt thiết lập mức độ Ưu tiên Phương tiện dựa trên sức chứa theo Thể tích/sức chứa theo Khối lượng của Phương tiện khi bạn khởi tạo Kế hoạch lộ trình.

## Điều kiện để sử dụng thiết lập Ưu tiên Phương tiện

### Yêu cầu đối với Nhà sản xuất

* Để có thể sử dụng thiết lập Ưu tiên phương tiện, vui lòng đảm bảo Mô hình kinh doanh của Nhà sản xuất là **1PL**. Thiết lập **Ưu tiên phương tiện** không khả dụng với mô hình kinh doanh **3PL**
* Để kiểm tra điều này, vui lòng làm theo các bước sau
* Bước 1: Di chuyển đến tab **Tổ chức > Tổ chức**
* Bước 2: Nhấp vào biểu tượng **Chỉnh sửa** :fa-pencil: của **Nhà sản xuất** bạn muốn cập nhật thông tin. Bạn có thể tham khảo cột **Loại Tổ chức** để xem Tổ chức bạn chọn thuộc loại Tổ chức nào.

<Image title="1. Business Model 2 (VIE).png" alt={1899} border={true} src="https://files.readme.io/53f150e-1._Business_Model_2_VIE.png">
  Illustration (Vietnamese)
</Image>

* Bước 3: Một biểu mẫu có tên **Cập nhật tổ chức** sẽ hiển thị trên màn hình. Nhấn vào tab **Các thiết lập khác**, sau đó chọn tab phụ có tên **Mô hình** ở bên trái của biểu mẫu. Trong biểu mẫu có tên **Thiết lập mô hình**, hãy nhìn vào phần có tên **Kinh doanh** sau đó tích chọn ô **1PL**

<Image title="1. Business Model (VIE).png" alt={931} border={true} src="https://files.readme.io/cfa47a0-1._Business_Model_VIE.png">
  Illustration (Vietnamese)
</Image>

* Bước 4: Nhấp vào **Lưu lại** để các thay đổi có hiệu lực.

### Yêu cầu đối với Chi nhánh

* Để có thể sử dụng thiết lập Ưu tiên phương tiện, vui lòng đảm bảo Chi nhánh không sử dụng **Đơn hàng PDP**. Thiết lập **Ưu tiên phương tiện** không khả dụng cho **Chi nhánh** sử dụng thiết lập Đơn hàng PDP.
* Để kiểm tra điều này, vui lòng làm theo các bước sau
* Bước 1: Di chuyển đến tab **Tổ chức > Tổ chức**
* Bước 2: Nhấp vào biểu tượng **Chỉnh sửa** :fa-pencil: của **Chi nhánh** bạn muốn cập nhật thông tin. Bạn có thể tham khảo cột **Loại Tổ chức** để xem Tổ chức bạn chọn thuộc loại Tổ chức nào.

<Image title="1. PDP Order 1 (VIE).png" alt={1899} border={true} src="https://files.readme.io/1cd374f-1._PDP_Order_1_VIE.png">
  Illustration (Vietnamese)
</Image>

* Bước 3: Một biểu mẫu có tên **Cập nhật tổ chức** sẽ hiển thị trên màn hình. Nhấn vào tab **Các thiết lập khác**, sau đó chọn tab phụ có tên **Lộ trình** ở bên trái của biểu mẫu. Trong biểu mẫu có tên **Thiết lập lộ trình**, vui lòng bỏ chọn ô **Đơn hàng PDP**

<Image title="2. PDP Order (VIE).png" alt={930} border={true} src="https://files.readme.io/4700fd2-2._PDP_Order_VIE.png">
  Illustration (Vietnamese)
</Image>

* Bước 4: Nhấp vào **Lưu lại** để các thay đổi có hiệu lực.

## Thiết lập mức độ Ưu tiên Phương tiện

* Để thiết lập mức độ Ưu tiên cho Phương tiện, vui lòng làm theo các bước sau
* Bước 1: Di chuyển đến tab **Tổ chức > Tổ chức**
* Bước 2: Nhấp vào biểu tượng **Chỉnh sửa** :fa-pencil: của **Chi nhánh** bạn muốn cập nhật thông tin. Bạn có thể tham khảo cột **Loại Tổ chức** để xem Tổ chức bạn chọn thuộc loại Tổ chức nào.

<Image title="1. PDP Order 1 (VIE).png" alt={1899} border={true} src="https://files.readme.io/0bc4b80-1._PDP_Order_1_VIE.png">
  Illustration (Vietnamese)
</Image>

* Bước 3: Một biểu mẫu có tên **Cập nhật tổ chức** sẽ hiển thị trên màn hình. Nhấn vào tab **Các thiết lập khác**, sau đó chọn tab phụ có tên **Thuật toán** ở bên trái của biểu mẫu. Trong biểu mẫu có tên **Thiết lập thuật toán**, vui lòng cuộn xuống cho đến khi bạn thấy phần **Ưu tiên phương tiện**

<Image title="3. Vehicle Prio (VIE).png" alt={930} border={true} src="https://files.readme.io/7e40714-3._Vehicle_Prio_VIE.png">
  Illustration (Vietnamese)
</Image>

* Bằng cách nhấp vào biểu tượng mũi tên hướng xuống :fa-sort-desc: bên cạnh hai trường thông tin nằm trong dòng ***Ưu tiên các phương tiện***, bạn có thể điều chỉnh các tiêu chí ưu tiên của thuật toán lựa chọn Phương tiện sẽ được áp dụng trong quá trình khởi tạo Kế hoạch lộ trình. Có bốn thiết lập ưu tiên:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Thiết lập ưu tiên
      </th>

      <th>
        Mô tả thiết lập ưu tiên
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Ưu tiên các phương tiện **Tăng dần** theo **Khối lượng** để tối ưu lộ trình
      </td>

      <td>
        Ưu tiên chọn Phương tiện có sức chứa theo Khối lượng nhỏ nhất trước, sau đó chuyển sang chọn Phương tiện có sức chứa theo Khối lượng lớn hơn.
      </td>
    </tr>

    <tr>
      <td>
        Ưu tiên các phương tiện **Giảm dần** theo **Khối lượng** để tối ưu lộ trình
      </td>

      <td>
        Ưu tiên chọn Phương tiện có sức chứa theo Khối lượng lớn nhất trước, sau đó chuyển sang chọn Phương tiện có sức chứa theo Khối lượng nhỏ hơn.
      </td>
    </tr>

    <tr>
      <td>
        Ưu tiên các phương tiện **Tăng dần** theo **Thể tích** để tối ưu lộ trình
      </td>

      <td>
        Ưu tiên chọn Phương tiện có sức chứa theo Thể tích nhỏ nhất trước, sau đó chuyển sang chọn Phương tiện có sức chứa theo Thể tích lớn hơn.
      </td>
    </tr>

    <tr>
      <td>
        Ưu tiên các phương tiện **Giảm dần** theo **Thể tích** để tối ưu lộ trình
      </td>

      <td>
        Ưu tiên chọn Phương tiện có sức chứa theo Thể tích lớn nhất, sau đó chuyển sang chọn Phương tiện có sức chứa theo Thể tích nhỏ hơn.
      </td>
    </tr>
  </tbody>
</Table>

* Bước 4: Nhấp vào **Lưu lại** để các thay đổi có hiệu lực.
* Theo mặc định, trong quá trình khởi tạo Kế hoạch lộ trình, hệ thống sẽ chọn các Phương tiện có tiêu chí ***Tăng dần theo Khối lượng để tối ưu lộ trình***, trong đó hệ thống chọn Phương tiện có khối lượng nhỏ nhất để giao Đơn hàng trước trong quá trình khởi tạo Kế hoạch lộ trình

<Image title="4. Asc (VIE).png" alt={930} border={true} src="https://files.readme.io/8792744-4._Asc_VIE.png">
  Illustration (Vietnamese)
</Image>

* Nếu bạn có Đơn hàng có khối lượng lớn/thể tích lớn và muốn chọn xe có sức chứa lớn nhất để thực hiện các Đơn hàng này, vui lòng chọn
* 1 - ***Ưu tiên các phương tiện Giảm dần theo Khối lượng để tối ưu lộ trình*** nếu bạn muốn chọn Phương tiện có sức chứa theo Khối lượng lớn nhất trước để giao Đơn hàng HOẶC,
* 2 - ***Ưu tiên các phương tiện Giảm dần theo Thể tích để tối ưu lộ trình*** nếu bạn muốn chọn Phương tiện có sức chứa Thể tích lớn nhất trước để giao Đơn hàng
* Sau khi bạn chọn, ô chọn **Ưu tiên đơn hàng** sẽ xuất hiện bên dưới. Khi bạn tích chọn ô này, thiết lập phụ **Ưu tiên các đơn hàng lớn hơn ... Kg hoặc ... m3** sẽ xuất hiện.

<Image title="1. Volume Order (VIE).png" alt={929} border={true} src="https://files.readme.io/e9ae0be-1._Volume_Order_VIE.png">
  Illustration (Vietnamese)
</Image>

* Thiết lập phụ này cho phép bạn ưu tiên các Đơn hàng theo Khối lượng (Kg) hoặc theo Thể tích (m3), bất kể **Ưu tiên phương tiện** đã chọn là Khối lượng hoặc Thể tích. Điều này có nghĩa là, ví dụ, khi bạn chọn ưu tiên Phương tiện theo Khối lượng, bạn không nhất thiết phải ưu tiên Đơn hàng theo Khối lượng trong thiết lập phụ **Ưu tiên đơn hàng**; bạn chắc chắn có thể chọn ưu tiên các Đơn hàng theo Thể tích và ngược lại.

* Khi bạn nhập giá trị vào các trường, thiết lập phụ này sẽ cho phép hệ thống ưu tiên các Đơn hàng có Khối lượng/Thể tích lớn hơn giá trị cụ thể đã nhập trong các trường, sau đó hệ thống sẽ chọn xe có sức chứa lớn nhất trước cho các Đơn hàng vượt quá giá trị đã nhập. Giá trị được nhập phải lớn hơn 0 và có thể là số thập phân.

* Ví dụ: Nếu bạn muốn các Đơn hàng vượt quá ***200 m3*** được thực hiện bởi các Phương tiện có sức chứa theo ***Khối lượng*** lớn nhất,

* Bước 1: Chọn **Ưu tiên phương tiện Giảm dần theo Khối lượng,**

* Bước 2: Tích chọn ô **Ưu tiên đơn hàng**;

* Bước 3: Trong dòng **Ưu tiên các Đơn hàng lớn hơn ... Kg hoặc m3**, vui lòng nhập giá trị **200** ở trong trường thông tin **... m3** và bỏ trống trường thông tin **... Kg**

* Bước 4: Nhấp vào **Lưu lại** để các thay đổi có hiệu lực.

* Hệ thống sẽ tập hợp tất cả các Đơn hàng có Thể tích vượt quá 200 m3 và chọn ra các Phương tiện có sức chứa theo Khối lượng lớn nhất hiện có để thực hiện các Đơn hàng đó trong Kế hoạch lộ trình.

<Image title="1. Volume Order Priority 2 (VIE).png" alt={933} border={true} src="https://files.readme.io/288512f-1._Volume_Order_Priority_2_VIE.png">
  Illustration (Vietnamese)
</Image>

## Giải thích Thiết lập Ưu tiên Phương tiện

* Các thiết lập ưu tiên này khá dễ hiểu. Hãy lấy ví dụ đơn giản dưới đây:
* Kho có hai phương tiện đang hoạt động là A và B. Phương tiện A có sức chứa tối đa là ***120 kg; 1,2 m3***; còn phương tiện B có sức chứa tối đa là ***100 kg; 1 m3***
* Một Khách hàng đặt một Đơn hàng ***60 kg; 0.6 m3*** 
* Nếu thiết lập mức độ ưu tiên của phương tiện là ***Ưu tiên các phương tiện Giảm dần theo Khối lượng/Thể tích để tối ưu lộ trình*** thì phương tiện A sẽ được chọn vì phương tiện đó có sức chứa theo khối lượng và thể tích cao hơn so với phương tiện A. Ngược lại, nếu cài đặt mức độ ưu tiên của phương tiện là ***Ưu tiên các phương tiện Tăng dần theo Khối lượng/Thể tích để tối ưu lộ trình*** thì phương tiện B sẽ được chọn vì phương tiện đó có sức chứa theo khối lượng và thể tích thấp hơn so với phương tiện A

## Các thiết lập có thể cùng sử dụng với thiết lập Ưu tiên Phương tiện

* Trong phần **Thiết lập thuật toán**, một số thiết lập có thể được sử dụng cùng với thiết lập **Ưu tiên phương tiện** như
* Sử dụng Phân cụm địa lý
* Phân cụm Khách Hàng
* Khung thời gian cố định
* Chia Đơn hàng
* Giới hạn số lượng Chuyến
* Giới hạn số lượng Ca
* Cân bằng thời gian hoạt động
* Tự động giảm người giao hàng
* Chia lộ trình
* Sử dụng Chuỗi cung ứng lạnh

<Image title="7. Config (VIE).png" alt={931} border={true} src="https://files.readme.io/5eb5de6-7._Config_VIE.png">
  Illustration (Vietnamese)
</Image>

* **Chú ý**: Thiết lập **Ưu tiên phương tiện KHÔNG THỂ** sử dụng cùng lúc với thiết lập **Sử dụng độ thân thuộc**. Nếu bạn đánh dấu vào ô **Sử dụng độ thân thuộc**, thiết lập **Ưu tiên phương tiện** sẽ bị vô hiệu hóa; người dùng không thể nhập bất kỳ giá trị nào hoặc chọn các tùy chọn trong hai trường thông tin.

<Image title="6. Familiarity (VIE).png" alt={933} border={true} src="https://files.readme.io/057a2c0-6._Familiarity_VIE.png">
  Illustration (Vietnamese)
</Image>
