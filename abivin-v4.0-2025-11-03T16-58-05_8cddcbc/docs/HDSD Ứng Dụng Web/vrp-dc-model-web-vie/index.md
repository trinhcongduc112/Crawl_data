---
title: '[Nội thành] Mô hình VRP/DC'
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
Mô hình VRP/DC là mô hình định tuyến (Vehicle Routing) trong đó tổ chức của bạn sở hữu một số kho hàng (Warehouse) hoặc trung tâm phân phối (Distribution Center, viết tắt là DC). Mỗi kho hàng/trung tâm phân phối sẽ sở hữu đội phương tiện riêng và có tập khách hàng riêng. Đội phương tiện sẽ lấy hàng tại Kho, di chuyển đi giao hàng theo Đơn hàng của các Khách hàng, sau đó trở về Kho và kết thúc Lộ trình giao hàng. Trong quá trình khởi tạo Kế hoạch lộ trình, người điều phối có thể áp dụng một số điều kiện ràng buộc, các thuật toán lộ trình để tạo ra Kế hoạch lộ trình tối ưu nhất.\
Mô hình này hiện nay được xây dựng để phục vụ hai chủ thể sau trong chuỗi cung ứng:\
**Chủ hàng**: Chủ hàng là các doanh nghiệp sản xuất hàng hoá. Họ sẽ trực tiếp phân phối hàng hoá của họ tới các kênh phân phối hoặc tới người tiêu dùng bằng đội phương tiện giao hàng của họ.\
**Nhà vận tải**: Nhà vận tải là các đơn vị cung cấp dịch vụ vận tải bên thứ ba. Họ sẽ ký hợp đồng cung ứng dịch vụ kho vận với các Chủ hàng và điều phối đội phương tiện giao hàng của họ theo yêu cầu của các Chủ hàng.

> 👍 Tương thích với mô hình PDP
>
> Bạn có thể chạy mô hình này đồng thời với Mô hình PDP trên cùng một tài khoản, miễn là bạn tạo các Tổ chức thuộc loại **Chi nhánh** riêng biệt cho từng mô hình.\
> Ngoài mô hình PDP, không mô hình nào khác có thể được sử dụng đồng thời với mô hình này trên cùng một tài khoản.
