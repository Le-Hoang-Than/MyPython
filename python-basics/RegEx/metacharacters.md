| Ký tự    | Mô tả                                                                  | Ví dụ            |
|:---------|:-----------------------------------------------------------------------|:-----------------|
| **`[]`** | Một tập hợp các ký tự.                                                 | `"[a-m]"`        |
| **`\`**  | Báo hiệu một chuỗi đặc biệt (cũng dùng để "thoát" các ký tự đặc biệt). | `"\d"`           |
| **`.`**  | Bất kỳ ký tự nào (ngoại trừ ký tự dòng mới).                           | `"he..o"`        |
| **`^`**  | Bắt đầu với...                                                         | `"^hello"`       |
| **`$`**  | Kết thúc với...                                                        | `"planet$"`      |
| **`*`**  | Xuất hiện 0 hoặc nhiều lần.                                            | `"he.*o"`        |
| **`+`**  | Xuất hiện 1 hoặc nhiều lần.                                            | `"he.+o"`        |
| **`?`**  | Xuất hiện 0 hoặc 1 lần.                                                | `"he.?o"`        |
| **`{}`** | Xuất hiện chính xác số lần được chỉ định.                              | `"he.{2}o"`      |
| **`\|`** | Hoặc (Phép toán logic OR).                                             | `"falls\|stays"` |
| **`()`** | Chụp (capture) và nhóm lại.                                            |                  |