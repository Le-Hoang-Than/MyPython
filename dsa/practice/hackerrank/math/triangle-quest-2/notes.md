# Notes

---

## Triangle Quest 2

**Mục tiêu bài toán:**

- In ra một tam giác đối xứng (palindromic triangle) có kích thước $N$.

**Ý tưởng:**

Nhìn vào dòng 4:
- 1234321, có thể phân tích như sau:
- 1234567 
- -246

Nhìn vào dòng 5:
- 123454321, có thể phân tích như sau:
- 123456789
-    -2468

`(1)` Có thể suy ra in một dãy số biến thiên từ 1 đến i + (i - 1)

Nhìn vào dòng 9:
- 12345678987654321
- 123456789????????

Do $1 \le N \le 9$ nên ý tưởng `(1)` sai

Tương tự bài 1 cần in ra hằng số const:
- 1
- 11
- 111
- 1111
- 11111

Nhìn vào dòng 3:
- 12321, có thể diễn giải như sau:
- 111 thực hiện một phép toán chưa biết để cho ra kết quả 12321
- 12321 là một số lẻ có thể chia cho 111
$\frac{12321}{111} = 111$

Suy ra 12321 = 111*111