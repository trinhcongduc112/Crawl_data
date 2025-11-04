---
title: Mô hình PDP - Tạo form cho tác vụ Mobile
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
## Thao tác tạo form chung

* **Bước 1**. Di chuyển đến tab **Tác vụ > Danh sách hành động**
* **Bước 2**. Di chuột vào dòng của từng hành động, sau đó nhấn vào biểu tượng **Trình tạo biểu mẫu** :fa-cog: để vào màn hình tạo form

<Image title="Open form builder.gif" alt={1668} className="border" border={true} src="https://files.readme.io/a4b599f-Open_form_builder.gif" />

* **Bước 3**. Xóa nút **Submit** màu xanh bằng cách di chuột vào nút đó, sau đó nhấn vào biểu tượng :fa-times: màu đỏ

<Image title="form builder delete submit button.gif" alt={1668} className="border" border={true} src="https://files.readme.io/46474b3-form_builder_delete_submit_button.gif" />

* **Bước 4**. Nhấn vào một trong ba phần **Basic Components**, **Special Components** hoặc **Layout Components** ở cột bên trái để tìm thành phần thích hợp, sau đó nhấn và giữ chuột vào thành phần đã chọn rồi kéo sang khu vực bên phải màn hình
* Biểu mẫu thiết lập của thành phần sẽ hiện ra. Mỗi biểu mẫu có một số tab: **Display, Validation, API** v.v. Điền thông tin cụ thể vào biểu mẫu này. Chi tiết nội dung điền cho từng thành phần sẽ được trình bày ở phần dưới
* Có một số thành phần như **Panel**, **Table** (Ở mục **Layout Components**) hay **Container** (Ở mục **Special Components**) cho phép bạn có thể kéo thả các thành phần khác vào ***bên trong*** các thành phần này. Điều này sẽ được mô tả thực tế ở bên dưới
* Nhấn **Save** để hoàn tất thiết lập thành phần

<Image title="drag form.gif" alt={1668} className="border" border={true} src="https://files.readme.io/98b7841-drag_form.gif" />

* **Bước 5**. Di chuyển xuống cuối màn hình tạo form, nhấn nút **Save View** đề hoàn tất việc tạo form cho tác vụ

<Image title="Save view form builder.gif" alt={1668} className="border" border={true} src="https://files.readme.io/d4ab5c7-Save_view_form_builder.gif" />

## Tác vụ Soạn hàng tại kho

* Mã hành động của tác vụ là LOADING\_AT\_DEPOT

## Tạo form hiển thị Thông tin đơn hàng

### Tạo khung chứa đơn hàng

* Kéo thành phần **Panel** ở mục **Layout Components**

<Image title="drag panel component.gif" alt={1668} className="border" border={true} src="https://files.readme.io/7c893f9-drag_panel_component.gif" />

* Ở tab **Display**, điền tên hiển thị của khung chứa đơn hàng (VD: *Danh sách đơn hàng*) vào trường **Title** 

<Image title="panel component - display tab.png" alt={1085} className="border" border={true} src="https://files.readme.io/920981e-panel_component_-_display_tab.png" />

* Nhấn vào tab **API**. Điền *orderList* vào trường **Property Name**. Nhấn tiếp vào **Custom Properties**, điền *url* vào trường **Key** và */orders/list/* vào trường **Value**

<Image title="panel component - api tab.png" alt={1087} className="border" border={true} src="https://files.readme.io/4a6c613-panel_component_-_api_tab.png" />

### Tạo bảng chứa các đơn hàng

* Kéo thành phần **Table** ở mục **Layout Components** vào bên trong khung chứa đơn hàng mới tạo phía trên

<Image title="drag table into panel component.gif" alt={1668} className="border" border={true} src="https://files.readme.io/959bc21-drag_table_into_panel_component.gif" />

* Ở tab **Display**, điền *1* vào trường **Number of Rows** và *4* vào trường **Number of Columns**
* Chú thích: *1* là dòng hiện tên các trường thông tin của đơn hàng; *4* là số trường thông tin mặc định sẽ hiển thị cho từng đơn hàng: **Mã đơn hàng**, **Mã khách hàng**, **Tên khách hàng** và **Tổng giá**

<Image title="Screenshot_10.png" alt={1085} className="border" border={true} src="https://files.readme.io/8d1ebb4-Screenshot_10.png" />

* Nhấn vào tab **API**. Điền *orderList* vào trường **Property Name**. Nhấn tiếp vào **Custom Properties**, điền *url* vào trường **Key** và */orders/list/* vào trường **Value**

<Image title="Screenshot_11.png" alt={1085} className="border" border={true} src="https://files.readme.io/5436206-Screenshot_11.png" />

### Tạo các trường thông tin của đơn hàng

* Các trường thông tin của đơn hàng được tạo với thao tác tương tự nhau:
* Kéo thành phần **Text Field** ở mục **Basic Components** vào khu vực **Drag and Drop a form component** màu xanh
* Mỗi trường thông tin tương ứng với một lần kéo thả thành phần **Text Field**

<Image title="drag text field into table.gif" alt={1668} className="border" border={true} src="https://files.readme.io/0bece8d-drag_text_field_into_table.gif" />

* Điền nội dung vào trường **Label** ở tab **Display** và trường **Property Name** ở tab **API**
* Nội dung điền đối với các trường thông tin được cho trong bảng dưới

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Mã đơn hàng
      </th>

      <th>
        Mã khách hàng
      </th>

      <th>
        Tên khách hàng
      </th>

      <th>
        Tổng giá
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Ở tab Display, điền giá trị sau vào trường Label:
        *Mã đơn hàng*

        Ở tab API, điền giá trị sau vào trường Property Name:
        *orderCode*
      </td>

      <td>
        Ở tab Display, điền giá trị sau vào trường Label:\
        *Mã khách hàng*

        Ở tab API, điền giá trị sau vào trường Property Name:\
        *customerInfo.customerCode*
      </td>

      <td>
        Ở tab Display, điền giá trị sau vào trường Label:\
        *Tên khách hàng*

        Ở tab API, điền giá trị sau vào trường Property Name:\
        *customerInfo.fullName*
      </td>

      <td>
        Ở tab Display, điền giá trị sau vào trường Label:\
        *Tổng giá*

        Ở tab API, điền giá trị sau vào trường Property Name:\
        *totalPrice*
      </td>
    </tr>
  </tbody>
</Table>

## Tạo form Xác nhân đến kho (Check in)

* Kéo thành phần **File** ở mục **Special Components** vào bên dưới form Thông tin đơn hàng vừa tạo phía trên

<Image title="drag file component.gif" alt={1668} className="border" border={true} src="https://files.readme.io/c02fdd4-drag_file_component.gif" />

* Ở tab **Display**, điền *Check in* vào trường **Label**

<Image title="Screenshot_14.png" alt={1072} className="border" border={true} src="https://files.readme.io/af5946c-Screenshot_14.png" />

* Nhấn vào tab **API**. Điền *undefinedCheckIn* vào trường **Property Name**
* Tiếp tục nhấn vào **Custom Properties**, điền *isHideSelectFromLibrary* vào trường **Key** và *true* vào trường **Value**. Thiết lập này sẽ bắt buộc tài xế phải chụp ảnh xác nhận, không cho phép tài xế lấy ảnh đã chụp sẵn từ hòm ảnh của điện thoại

<Image title="Screenshot_15.png" alt={1064} className="border" border={true} src="https://files.readme.io/19d83a6-Screenshot_15.png" />

* Nhấn vào tab **Validation**. Tùy chọn nhấn vào ô **Required** :fa-square-o:, chuyển ô đó thành :fa-check-square-o: để bắt buộc tài xế phải thực hiện tác vụ này trên ứng dụng di động. Nếu không nhấn, tài xế không bắt buộc phải thực hiện tác vụ này trên ứng dụng di động

<Image title="Screenshot_18.png" alt={1085} className="border" border={true} src="https://files.readme.io/f1b5f89-Screenshot_18.png" />

## Tạo form Xác nhận rời kho (Check out)

### Tạo khung chứa form xác nhận

* Kéo thành phần **Panel** ở mục **Special Components** vào bên dưới form Xác nhận đến kho mới tạo phía trên

<Image title="drag check out container.gif" alt={1668} className="border" border={true} src="https://files.readme.io/8ce99d5-drag_check_out_container.gif" />

* Ở tab **Display**, điền *Xác nhận trạng thái* vào trường **Title**

<Image title="Screenshot_16.png" alt={1081} className="border" border={true} src="https://files.readme.io/25e7de6-Screenshot_16.png" />

* Nhấn vào tab **API**. Điền *undefinedPanel* vào trường **Property Name**

<Image title="Screenshot_17.png" alt={1087} className="border" border={true} src="https://files.readme.io/039c1be-Screenshot_17.png" />

### Tạo các mục xác nhận

* Cần tạo các mục xác nhận sau:
* Đã lấy hàng ra khỏi kệ trong kho và chất lên phương tiện vận tải
* Đã rời khỏi kho, chuẩn bị bắt đầu vận chuyển
* Để tạo các mục xác nhận này, thực hiện các thao tác sau:
* Kéo thành phần **Check Box** ở mục **Basic Components** vào bên trong Khung chứa form xác nhận vừa tạo phía trên

<Image title="drag confirmation check box.gif" alt={1668} className="border" border={true} src="https://files.readme.io/f7d5556-drag_confirmation_check_box.gif" />

* Điền các thông tin vào các trường **Label** ở tab **Display**, **Required** ở tab **Validation** và **Property Name** ở tab **API**
* Thông tin điền như ở bảng bên dưới

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Xác nhận đã lấy hàng ra khỏi kệ trong kho và chất lên phương tiện vận tải
      </th>

      <th>
        Xác nhận đã rời khỏi kho, chuẩn bị bắt đầu vận chuyển
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Ở tab Display, điền giá trị sau vào trường Label:
        *Xác nhận đã lấy hàng ra khỏi kho*
        Ở tab Validation, tích vào ô Required
        Ở tab API, điền giá trị sau vào trường Property Name:
        *undefinedPanelConfirmproductsaretakenoutofdepot*
      </td>

      <td>
        Ở tab Display, điền giá trị sau vào trường Label:\
        *Xác nhận rời kho*\
        Ở tab Validation, tích vào ô Required\
        Ở tab API, điền giá trị sau vào trường Property Name:\
        *undefinedPanelCheckoutfromdepot*
      </td>
    </tr>
  </tbody>
</Table>

## Tạo form Chữ ký điện tử

* Kéo thành phần **Signature** trong mục **Special Components** vào bên dưới Khung các mục xác nhận vừa tạo phía trên

<Image title="drag signature.gif" alt={1668} className="border" border={true} src="https://files.readme.io/3ca4c56-drag_signature.gif" />

* Ở tab **Display**, điền giá trị sau vào trường **Footer Label**: *Chữ ký điện tử*

<Image title="Screenshot_19.png" alt={1075} className="border" border={true} src="https://files.readme.io/3c5be21-Screenshot_19.png" />

* Nhấn vào tab **Validation**, tích vào ô **Required** :fa-square-o:

<Image title="Screenshot_20.png" alt={1082} className="border" border={true} src="https://files.readme.io/b961f9a-Screenshot_20.png" />

* Nhấn vào tab **API**, điền giá trị sau vào trường **Property Name**: *undefinedSignature*

<Image title="Screenshot_21.png" alt={1068} className="border" border={true} src="https://files.readme.io/9ceea42-Screenshot_21.png" />

* Giao diện tác vụ sau khi đã tạo form hoàn chỉnh như sau:

<Image title="2019-09-03 17_42_32-Window.png" alt={1098} className="border" border={true} src="https://files.readme.io/798fbea-2019-09-03_17_42_32-Window.png" />

## Tác vụ Giao hàng

* Mã hành động của tác vụ là DELIVER\_PRODUCT

## Tạo form Xác nhận đến kho của khách

* Kéo thành phần **File** ở mục **Special Components**
* Ở tab **Display**, điền giá trị sau vào trường **Label**: *Arrival Check In*
* Nhấn vào tab **Validation**, tích vào ô **Required** :fa-square-o:
* Nhấn vào tab **API**, điền *undefinedCheckIn* vào trường **Property Name**. Tiếp tục nhấn vào **Custom Properties**, điền *isHideSelectFromLibrary* vào trường **Key** và *true* vào trường **Value**

## Tạo form Xác nhận bắt đầu dỡ hàng

* Kéo thành phần **File** ở mục **Special Components** vào bên dưới form Xác nhận đến kho của khách vừa tạo phía trên
* Ở tab **Display**, điền giá trị sau vào trường **Label**: *Unloading Check in*
* Nhấn vào tab **Validation**, tích vào ô **Required** :fa-square-o:
* Nhấn vào tab **API**, điền *undefinedUnloadingCheckin* vào trường **Property Name**. Tiếp tục nhấn vào **Custom Properties**, điền *isHideSelectFromLibrary* vào trường **Key** và *true* vào trường **Value**

## Tạo form Xác nhận trạng thái giao hàng

### Tạo khung chứa form Xác nhận trạng thái giao hàng

* Kéo thành phần **Container** ở mục **Special Components** vào bên dưới form Xác nhận bắt đầu dỡ hàng vừa tạo phía trên
* Ở tab **Display**, điền giá trị sau vào trường **Label**: *Xác nhận trạng thái*
* Nhấn vào tab **API**, điền *undefinedXcnhntrngthi* vào trường **Property Name**
* Tiếp tục nhấn vào **Custom Properties**. Điền *data* vào trường **Key** và *\{}* vào trường **Value**
* Nhấn vào nút **Add Value** để thêm một dòng nữa ở mục **Custom Properties**. Điền *url* vào trường **Key** và */orders/list/* vào trường **Value**

### Tạo form Xác nhận trạng thái giao hàng

* Kéo thành phần **Check Box** ở mục **Basic Components** vào bên trong Khung chứa form xác nhận vừa tạo phía trên
* Ở tab **Display**, điền giá trị sau vào trường **Label**: *Xác nhận đã giao hàng*
* Nhấn vào tab **Validation**, tích vào ô **Required** :fa-square-o:
* Nhấn vào tab **API**, điền *undefinedXcnhntrngthiXcnhnnhnhng* vào trường **Property Name**

### Tạo form Chữ ký điện tử

* Thao tác [tương tự như trên](https://docs.abivin.com/docs/pdp-model-form-builder#section-t-o-form-ch-k-i-n-t-) 
* Giao diện tác vụ sau khi đã tạo form hoàn chỉnh như sau:

<Image title="2019-09-03 17_45_05-Window.png" alt={1070} className="border" border={true} src="https://files.readme.io/3b0e62c-2019-09-03_17_45_05-Window.png" />

## Tác vụ Lấy hàng tại kho khách hàng

* Mã hành động của tác vụ là LOADING\_AT\_STORE

## Tạo form Xác nhận tại kho của khách hàng

* Thao tác [tương tự như trên](https://docs.abivin.com/docs/pdp-model-form-builder#section-t-o-form-x-c-nh-n-n-kho-c-a-kh-ch)

## Tạo form Xác nhận trạng thái lấy hàng

### Tạo Khung chứa form xác nhận trạng thái lấy hàng

* Thao tác [tương tự như trên](https://docs.abivin.com/docs/pdp-model-form-builder#section-t-o-khung-ch-a-form-x-c-nh-n)

### Tạo form Xác nhận trạng thái lấy hàng

#### Tạo form Xác nhận đã tải xong hàng lên phương tiện

* Kéo thành phần **Check Box** ở mục **Basic Components** vào bên trong Khung chứa form xác nhận trạng thái lấy hàng vừa tạo phía trên
* Ở tab **Display**, điền giá trị sau vào trường **Label**: *Đã tải xong*
* Nhấn vào tab **Validation**, tích vào ô **Required** :fa-square-o:
* Nhấn vào tab **API**, điền *undefinedPanelProductsloaded* vào trường **Property Name**

#### Tạo form Xác nhận đã rời khỏi kho khách hàng

* Kéo thành phần **Check Box** ở mục **Basic Components** vào bên trong Khung chứa form xác nhận trạng thái lấy hàng vừa tạo phía trên, bên dưới form Xác nhận đã tải xong hàng lên phương tiện
* Ở tab **Display**, điền giá trị sau vào trường **Label**: *Rời kho khách hàng*
* Nhấn vào tab **Validation**, tích vào ô **Required** :fa-square-o:
* Nhấn vào tab **API**, điền *undefinedPanelConfirmleavingcustomerwarehouse* vào trường **Property Name**
* Giao diện tác vụ sau khi đã tạo form hoàn chỉnh như sau:

<Image title="2019-09-03 17_46_36-Window.png" alt={1073} className="border" border={true} src="https://files.readme.io/ad34754-2019-09-03_17_46_36-Window.png" />

## Tác vụ Di chuyển

* Mã hành động của tác vụ là TRANSIT

## Tạo form Xác nhận tại nơi nghỉ qua đêm

* Thao tác [tương tự như trên](https://docs.abivin.com/docs/pdp-model-form-builder#section-t-o-form-x-c-nh-n-n-kho-c-a-kh-ch)
* Giao diện tác vụ sau khi đã tạo form hoàn chỉnh như sau:

<Image title="2019-09-03 17_47_38-Window.png" alt={1069} className="border" border={true} src="https://files.readme.io/c08fba3-2019-09-03_17_47_38-Window.png" />

## Tác vụ Về kho

* Mã hành động của tác vụ là BACK\_DEPOT

## Tạo form Xác nhận tại kho

* Thao tác [tương tự như trên](https://docs.abivin.com/docs/pdp-model-form-builder#section-t-o-form-x-c-nh-n-n-kho-c-a-kh-ch)
* Giao diện tác vụ sau khi đã tạo form hoàn chỉnh như sau:

<Image title="2019-09-03 17_47_38-Window.png" alt={1069} className="border" border={true} src="https://files.readme.io/32cf3f4-2019-09-03_17_47_38-Window.png" />

## Tác vụ Hết ngày

* Mã hành động của tác vụ là END\_DAY

## Tạo form Tình trạng giao hàng

### Tạo Khung chứa form tình trạng giao các đơn hàng

* Kéo thành phần **Panel** ở mục **Layout Components**
* Ở tab **Display**, điền giá trị sau vào trường **Title**: *Tình trạng giao hàng*
* Nhấn vào tab **API**. Điền *undefinedPanel* vào trường **Property Name**. Nhấn tiếp vào **Custom Properties**, điền *url* vào trường **Key** và */orders/list/* vào trường **Value** 

### Tạo bảng chứa các đơn hàng

* Kéo thành phần **Table** ở mục **Layout Components** vào bên trong khung chứa đơn hàng mới tạo phía trên
* Ở tab **Display**, điền *1* vào trường **Number of Rows** và *4* vào trường **Number of Columns**
* Nhấn vào tab **API**. Điền *orderList* vào trường **Property Name**. Nhấn tiếp vào **Custom Properties**, điền *url* vào trường **Key** và */orders/list/* vào trường **Value**

### Tạo các trường thông tin của đơn hàng

* Các trường thông tin của đơn hàng được tạo lần lượt với thao tác tương tự nhau:
* Kéo thành phần **Text Field** ở mục **Basic Components** lần lượt vào khu vực **Drag and Drop a form component** màu xanh
* Điền nội dung vào trường **Label** ở tab **Display** và trường **Property Name** ở tab **API**
* Nội dung điền đối với các trường thông tin được cho trong bảng dưới

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Mã đơn hàng
      </th>

      <th>
        Mã khách hàng
      </th>

      <th>
        Tên khách hàng
      </th>

      <th>
        Tiền phải thu
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Ở tab Display, điền giá trị sau vào trường Label:
        *Mã đơn hàng*

        Ở tab API, điền giá trị sau vào trường Property Name:
        *orderCode*
      </td>

      <td>
        Ở tab Display, điền giá trị sau vào trường Label:\
        *Mã khách hàng*

        Ở tab API, điền giá trị sau vào trường Property Name:\
        *customerInfo.customerCode*
      </td>

      <td>
        Ở tab Display, điền giá trị sau vào trường Label:\
        *Tên khách hàng*

        Ở tab API, điền giá trị sau vào trường Property Name:\
        *customerInfo.fullName*
      </td>

      <td>
        Ở tab Display, điền giá trị sau vào trường Label:\
        *Tiền phải thu*

        Ở tab API, điền giá trị sau vào trường Property Name:\
        *totalPrice*
      </td>
    </tr>
  </tbody>
</Table>

## Tạo form Xác nhân đến kho (Check in)

* Thao tác [tương tự như trên](https://docs.abivin.com/docs/pdp-model-form-builder#section-t-o-form-x-c-nh-n-n-kho-check-in-)

## Tạo form Xác nhận trạng thái giao hàng

### Tạo Khung chứa form xác nhận trạng thái giao hàng

* Thao tác [tương tự như trên](https://docs.abivin.com/docs/pdp-model-form-builder#section-t-o-khung-ch-a-form-x-c-nh-n)

### Tạo các mục xác nhận

* Cần tạo các mục xác nhận sau:
* Đã bàn giao toàn bộ hàng trả về cho thủ kho
* Đã nộp toàn bộ tiền thu được cho kế toán
* Để tạo các mục xác nhận này, thực hiện các thao tác sau:
* Kéo thành phần **Check Box** ở mục **Basic Components** vào bên trong Khung chứa form xác nhận vừa tạo phía trên
* Điền các thông tin vào các trường **Label** ở tab **Display**, **Required** ở tab **Validation** và **Property Name** ở tab **API**
* Thông tin điền như ở bảng bên dưới:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Xác nhận đã bàn giao toàn bộ hàng trả về cho thủ kho
      </th>

      <th>
        Xác nhận đã nộp toàn bộ tiền thu được cho kế toán
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Ở tab Display, điền giá trị sau vào trường Label:
        *Xác nhận đã chuyển tiền cho kế toán*
        Ở tab Validation, tích vào ô Required
        Ở tab API, điền giá trị sau vào trường Property Name:
        *undefinedPanel2Confirmtohandallreturnedproducttowarehousekeeper*
      </td>

      <td>
        Ở tab Display, điền giá trị sau vào trường Label:\
        *Xác nhận rời kho*\
        Ở tab Validation, tích vào ô Required\
        Ở tab API, điền giá trị sau vào trường Property Name:\
        *undefinedPanelCollectedCash*
      </td>
    </tr>
  </tbody>
</Table>

* Giao diện tác vụ sau khi đã tạo form hoàn chỉnh như sau:

<Image title="2019-09-03 17_59_30-Window.png" alt={1064} className="border" border={true} src="https://files.readme.io/60cfb17-2019-09-03_17_59_30-Window.png" />
