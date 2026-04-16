# Nested Lists

Cho tên và điểm số của từng sinh viên trong một lớp học gồm $N$ sinh viên, hãy lưu trữ chúng trong một danh sách lồng
nhau (nested list) và in ra tên của những sinh viên có điểm số thấp thứ hai.

**Lưu ý:** Nếu có nhiều sinh viên cùng sở hữu mức điểm thấp thứ hai này, hãy sắp xếp tên của họ theo thứ tự bảng chữ cái
và in mỗi tên trên một dòng mới.

**Example**

$records$ = [["chi", 20.0],["beta", 50.0],["alpha", 50.0]]

Giả sử danh sách điểm đã sắp xếp là $[20.0, 50.0]$, vậy mức điểm thấp thứ hai là $50.0$.
Có hai sinh viên đạt mức điểm này là ["alpha", "beta"].

Sau khi sắp xếp theo bảng chữ cái, kết quả được in ra là:

```markdown
alpha
beta
```

**Input Format**

Dòng đầu tiên chứa số nguyên $N$, biểu thị số lượng sinh viên.

$2N$ dòng tiếp theo mô tả thông tin của từng sinh viên:
- Dòng đầu tiên là tên sinh viên.
- Dòng thứ hai là điểm số của sinh viên đó.

**Constraints**

- $2 \le N \le 5$
- Luôn có ít nhất một hoặc nhiều sinh viên có mức điểm thấp thứ hai.

**Output Format**

In ra tên của những sinh viên có điểm thấp thứ hai. Nếu có nhiều sinh viên, hãy sắp xếp tên theo thứ tự bảng chữ cái và in mỗi tên trên một dòng mới.

**Sample Input 0**

```markdown
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

**Sample Output 0**

```markdown
Berry
Harry
```

**Explanation 0**

Trong lớp này có 5 sinh viên với tên và điểm số được tập hợp thành danh sách như sau:

`students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]`

- Điểm thấp nhất là 37.2 (thuộc về Tina).
- Mức điểm thấp thứ hai là 37.21 (thuộc về cả Harry và Berry).
- Chúng ta sắp xếp tên Harry và Berry theo bảng chữ cái và in mỗi tên trên một dòng.