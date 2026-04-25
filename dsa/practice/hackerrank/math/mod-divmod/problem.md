# Mod Divmod

Một trong những hàm tích hợp sẵn của Python là `divmod`, hàm này nhận vào hai đối số $a$ và $b$ và trả về một **tuple** chứa thương số ($a // b$) trước, sau đó là số dư ($a \% b$).

**Ví dụ:**

```markdown
>>> print divmod(177,10)
(17, 7)
```

Ở đây:
- Phép chia số nguyên là: 177 // 10 => 17
- Phép chia lấy dư (modulo) là: 177 % 10 => 7

**Task**

Đọc vào hai số nguyên $a$ và $b$, sau đó in ra ba dòng:

Dòng thứ nhất là kết quả của phép chia số nguyên $a // b$.

Dòng thứ hai là kết quả của phép chia lấy dư $a \% b$.

Dòng thứ ba in ra kết quả của hàm divmod(a, b).

**Input Format**

Dòng đầu tiên chứa số nguyên thứ nhất $a$.

Dòng thứ hai chứa số nguyên thứ hai $b$.

**Output Format**

In ra kết quả theo mô tả ở trên.

**Sample Input**

```markdown
177
10
```

**Sample Output**

```markdown
17
7
(17, 7)
```