# Alphabet Rangoli

Bạn được cho một số nguyên $N$. Nhiệm vụ của bạn là in ra một hình **Alphabet Rangoli** có kích thước $N$. (Rangoli là một dạng nghệ thuật dân gian Ấn Độ dựa trên việc tạo ra các hoa văn).

Dưới đây là ví dụ về Alphabet Rangoli với các kích thước khác nhau:

**Kích thước 3 (Size 3):**
```markdown
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
```

**Kích thước 5 (Size 5):**

```markdown
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

Tâm của hình rangoli là chữ cái đầu tiên trong bảng chữ cái (a), và ranh giới ngoài cùng là chữ cái thứ $N$ (theo thứ tự bảng chữ cái).

**Function Description**

Hãy hoàn thành hàm print_rangoli trong trình soạn thảo.

Hàm print_rangoli có tham số sau:
- int size: kích thước của hình rangoli.

**Returns**

- string: Một chuỗi duy nhất bao gồm các dòng của hình rangoli, ngăn cách nhau bởi ký tự xuống dòng (\n).

**Input Format**

Một dòng duy nhất chứa số nguyên $N$, đại diện cho kích thước của hình rangoli.

**Constraints**

$0 < N < 27$

**Sample Input**

```markdown
5
```

**Sample Output**

```markdown
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```
