| Ký tự    | Mô tả                                                                | Ví dụ                  |
|:---------|:---------------------------------------------------------------------|:-----------------------|
| **`\A`** | Trả về kết quả khớp nếu các ký tự được chỉ định nằm ở đầu chuỗi.     | `"\AThe"`              |
| **`\b`** | Trả về kết quả khớp nếu các ký tự nằm ở đầu hoặc cuối của một từ.    | `r"\bain"`, `r"ain\b"` |
| **`\B`** | Trả về kết quả khớp nếu các ký tự có mặt, nhưng KHÔNG ở đầu/cuối từ. | `r"\Bain"`, `r"ain\B"` |
| **`\d`** | Trả về kết quả khớp khi chuỗi có chứa chữ số (0-9).                  | `"\d"`                 |
| **`\D`** | Trả về kết quả khớp khi chuỗi KHÔNG chứa chữ số.                     | `"\D"`                 |
| **`\s`** | Trả về kết quả khớp khi chuỗi có chứa ký tự khoảng trắng.            | `"\s"`                 |
| **`\S`** | Trả về kết quả khớp khi chuỗi KHÔNG chứa ký tự khoảng trắng.         | `"\S"`                 |
| **`\w`** | Trả về kết quả khớp khi chuỗi chứa ký tự chữ, số hoặc gạch dưới.     | `"\w"`                 |
| **`\W`** | Trả về kết quả khớp khi chuỗi KHÔNG chứa ký tự chữ, số, gạch dưới.   | `"\W"`                 |
| **`\Z`** | Trả về kết quả khớp nếu các ký tự được chỉ định nằm ở cuối chuỗi.    | `"Spain\Z"`            |