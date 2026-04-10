# Notes

---

## Python If-Else

**Mục tiêu bài toán**

Cho một số nguyên dương $n$ (1 ≤ $n$ ≤ 100), in ra:

- `Weird` nếu:
    - $n$ là số lẻ.
    - $n$ là số chẵn và nằm trong [6, 20]
- `Not Weird` nếu:
    - $n$ là số chẵn và nằm trong [2, 5].
    - $n$ là số chẵn và lớn hơn 20

**Ý tưởng**

- Xác định chẵn / lẻ bằng `n % 2`.
- Chia bài toán thành 2 nhóm:
    - Số lẻ, luôn `Weird`.
    - Số chẵn, xét các khoảng giá trị.

**Cách giải**

Nếu $n$ là số lẻ, return `Weird`.

Nếu $n$ là số chẵn:

- 2 ≤ $n$ ≤ 5, return `Not Weird`.
- 6 ≤ $n$ ≤ 20, return `Weird`.
- n > 20, return `Not Weird`.

**Test case**

| TC |                 Loại | $n$ | Kết quả mong đợi |             Giải thích |
|---:|---------------------:|----:|-----------------:|-----------------------:|
|  1 |     Giá trị cực tiểu |   1 |            Weird |           $n$ là số lẻ |
|  2 |                Số lẻ |   3 |            Weird |           $n$ là số lẻ |
|  3 |      Biên dưới [2,5] |   2 |        Not Weird |   Số chẵn, thuộc [2,5] |
|  4 | Giá trị khoảng [2,5] |   4 |        Not Weird |   Số chẵn, thuộc [2,5] |
|  5 |      Biên trên [2,5] |   5 |            Weird |     Số lẻ, thuộc [2,5] |
|  6 |     Biên dưới [6,20] |   6 |            Weird | Số chẵn, thuộc [6, 20] |
|  7 |       Giá trị [6,20] |  14 |            Weird | Số chẵn, thuộc [6, 20] |
|  8 |     Biên trên [6,20] |  20 |            Weird | Số chẵn, thuộc [6, 20] |
|  9 |                Số lẻ |  21 |            Weird | $n$ là số lẻ (dù > 20) |
| 10 |       Biên dưới > 20 |  22 |        Not Weird |      Số chẵn, $n$ > 20 |
| 11 |   Giá trị trong > 20 |  24 |        Not Weird |      Số chẵn, $n$ > 20 |
| 12 |      Giá trị cực đại | 100 |        Not Weird |      Số chẵn, $n$ > 20 |

