| Set              | Mô tả                                                                                                 | Ví dụ        |
|:-----------------|:------------------------------------------------------------------------------------------------------|:-------------|
| **`[arn]`**      | Trả về kết quả khớp nếu một trong các ký tự (a, r, hoặc n) xuất hiện.                                 | `[arn]`      |
| **`[a-n]`**      | Khớp với bất kỳ ký tự thường nào từ a đến n.                                                          | `[a-n]`      |
| **`[^arn]`**     | Khớp với bất kỳ ký tự nào NGOẠI TRỪ a, r, và n.                                                       | `[^arn]`     |
| **`[0123]`**     | Khớp với bất kỳ chữ số nào trong bộ {0, 1, 2, 3}.                                                     | `[0123]`     |
| **`[0-9]`**      | Khớp với bất kỳ chữ số nào từ 0 đến 9.                                                                | `[0-9]`      |
| **`[0-5][0-9]`** | Khớp với các số có hai chữ số từ 00 đến 59.                                                           | `[0-5][0-9]` |
| **`[a-zA-Z]`**   | Khớp với bất kỳ chữ cái nào (không phân biệt hoa thường).                                             | `[a-zA-Z]`   |
| **`[+]`**        | Trong ngoặc vuông, các ký tự đặc biệt mất đi ý nghĩa của chúng. `[+]` chỉ đơn giản là tìm ký tự cộng. | `[+]`        |