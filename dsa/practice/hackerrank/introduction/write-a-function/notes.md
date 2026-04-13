# Notes

---

## Write a function

**Mục tiêu bài toán**

Cho một năm là số nguyên dương ($1900 \le \text{year} \le 10^5$)

- `True` là năm nhuận, khi:
    - Chia hết cho 400.
    - Chia hết cho 4 nhưng không chia hết cho 100.

- `False` là năm không nhuận:
    - Chia hết cho 100 nhưng không chia hết cho 400.
    - Các trường hợp còn lại không chia hết cho 4.

**Ý tưởng**

- Chỉ xét điều kiện là `năm nhuận` khi và chỉ khi:
  - Năm chia hết cho 400 hoặc chia hết cho 4 và không chia hết cho 100

Hoặc:

- Sử dụng phương pháp Loại trừ dần dựa trên cấp độ ưu tiên của các điều kiện 
  - Chia hết cho 400. Là năm nhuận
  - Chia hết cho 100 nhưng không chia hết cho 400. Là năm không nhuận
  - Chia hết cho 4 nhưng khong chia hết cho 100. Là năm nhuận
  - Các trường hợp còn lại không chia hết cho 4. Là năm không nhuận
**Cách giải**

- Nếu năm chia hết 400 thì là năm nhuận
- Còn không, nếu năm chia hết cho 100 thì là không nhuận
- Còn không, nếu năm chia hết cho 4 thì là năm nhuận
- còn không, các năm còn lại là năm không nhuận

**Decision Table**

| Điều kiện        | R1 | R2 | `R3` | R4 | `R5` | `R6` | `R7` | R8 |
|:-----------------|:--:|:--:|:----:|:--:|:----:|:----:|:----:|:--:|
| Chia hết cho 4   | 0  | 1  |  0   | 1  |  0   |  1   |  0   | 1  |
| Chia hết cho 100 | 0  | 0  |  1   | 1  |  0   |  0   |  1   | 1  |
| Chia hết cho 400 | 0  | 0  |  0   | 0  |  1   |  1   |  1   | 1  |
| Leap Year        | F  | T  |  -   | F  |  -   |  -   |  -   | T  |

Xuất hiện mâu thuẫn:

- R3 (0-1-0): Vô lý vì số chia hết cho 100 thì bắt buộc phải chia hết cho 4.
- R5 (0-0-1): Vô lý vì số chia hết cho 400 thì bắt buộc phải chia hết cho 4 và 100.
- R6 (1-0-1): Vô lý vì số chia hết cho 400 thì bắt buộc phải chia hết cho 100.
- R7 (0-1-1): Vô lý vì số chia hết cho 400 thì bắt buộc phải chia hết cho 4.

| Điều kiện        | R1 | R2 | R4 | R8 |
|:-----------------|:--:|:--:|:--:|:--:|
| Chia hết cho 4   | 0  | 1  | 1  | 1  |
| Chia hết cho 100 | 0  | 0  | 1  | 1  |
| Chia hết cho 400 | 0  | 0  | 0  | 1  |
| Leap Year        | F  | T  | F  | T  |

Ta có:

- R1: year % 4 != 0 $\rightarrow$ False.
- R2: year % 4 == 0 AND year % 100 != 0 $\rightarrow$ True.
- R4: year % 100 == 0 AND year % 400 != 0 $\rightarrow$ False.
- R8: year % 400 == 0 $\rightarrow$ True.

**Hoặc**

Dựa vào mục tiêu bài toán:

| Năm chia hết cho:                              | 4 | 100 | 400 | Leap year |
|:-----------------------------------------------|:-:|:---:|:---:|:---------:|
| Không chia hết cho 4                           | 0 |  -  |  -  |     F     |
| Chia hết cho 4 nhưng không chia hết cho 100.   | 1 |  0  |  _  |     T     |
| Chia hết cho 100 nhưng không chia hết cho 400. | 1 |  1  |  0  |     F     |
| Chia hết cho 400.                              | 1 |  1  |  1  |     T     |

**Test Case**

| TC   | TC Name                                   | Year | Expected Result |
|:-----|:------------------------------------------|:----:|----------------:|
| TC01 | not_divisible_by_4                        | 2023 |           False |
| TC02 | divisible_by_4_but_not_divisible_by_100   | 2024 |            True |
| TC03 | divisible_by_100_but_not_divisible_by_400 | 1900 |           False |
| TC04 | divisible_by_400                          | 2000 |            True |