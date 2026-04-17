# Các Kiểu Định Dạng (Formatting Types) trong Python

Sử dụng bên trong các dấu ngoặc nhọn `{}` của f-string hoặc phương thức `.format()` để tùy chỉnh kết quả hiển thị.

| Ký hiệu                                 | Mô tả                                                              |
|:----------------------------------------|:-------------------------------------------------------------------|
| **Căn lề (Alignment)**                  |                                                                    |
| `:<`                                    | **Căn lề trái** kết quả (trong khoảng trống khả dụng).             |
| `:>`                                    | **Căn lề phải** kết quả (trong khoảng trống khả dụng).             |
| `:^`                                    | **Căn giữa** kết quả (trong khoảng trống khả dụng).                |
| **Dấu (Signs)**                         |                                                                    |
| `:=`                                    | Đặt dấu (âm/dương) ở vị trí **ngoài cùng bên trái**.               |
| `:+`                                    | Sử dụng **dấu cộng** để hiển thị cả số dương và số âm.             |
| `:-`                                    | Chỉ sử dụng **dấu trừ** cho các giá trị âm (mặc định).             |
| `: `                                    | Thêm một **khoảng trắng** trước số dương (và dấu trừ trước số âm). |
| **Dấu phân cách (Separators)**          |                                                                    |
| `:,`                                    | Sử dụng **dấu phẩy** làm dấu phân cách hàng nghìn.                 |
| `:_`                                    | Sử dụng **dấu gạch dưới** làm dấu phân cách hàng nghìn.            |
| **Hệ cơ số (Number Bases)**             |                                                                    |
| `:b`                                    | Định dạng hệ **Nhị phân** (Binary).                                |
| `:d`                                    | Định dạng hệ **Thập phân** (Decimal).                              |
| `:o`                                    | Định dạng hệ **Bát phân** (Octal).                                 |
| `:x`                                    | Định dạng hệ **Thập lục phân** (Hex), viết thường.                 |
| `:X`                                    | Định dạng hệ **Thập lục phân** (Hex), viết hoa.                    |
| **Số thực & Khoa học (Floating Point)** |                                                                    |
| `:e`                                    | Định dạng **Số mũ/Khoa học** (chữ "e" thường).                     |
| `:E`                                    | Định dạng **Số mũ/Khoa học** (chữ "E" hoa).                        |
| `:f`                                    | Định dạng **Số thực dấu phẩy tĩnh** (Fix point).                   |
| `:F`                                    | Định dạng **Số thực dấu phẩy tĩnh** (viết hoa `INF` và `NAN`).     |
| `:g`                                    | Định dạng chung (General format).                                  |
| `:G`                                    | Định dạng chung (sử dụng `E` hoa cho ký hiệu khoa học).            |
| **Khác**                                |                                                                    |
| `:c`                                    | Chuyển đổi giá trị thành ký tự **Unicode** tương ứng.              |
| `:n`                                    | Định dạng số (tùy theo ngôn ngữ hệ thống).                         |
| `:%`                                    | Định dạng **Phần trăm** (Percentage).                              |