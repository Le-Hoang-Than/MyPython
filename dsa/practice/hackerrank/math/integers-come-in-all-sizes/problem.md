# Integers Come In All Sizes

Số nguyên trong Python có thể lớn bằng dung lượng bộ nhớ (RAM) của máy tính. Không có giới hạn cụ thể về kích thước như các kiểu dữ liệu: $2^{31}-1$ (kiểu `int` trong C++) hay $2^{63}-1$ (kiểu `long long int` trong C++).

Như chúng ta đã biết, kết quả của phép toán $a^b$ tăng lên rất nhanh khi $b$ tăng dần. Hãy cùng thực hiện một số phép tính với các số nguyên cực kỳ lớn.

**Task**

Đọc vào bốn số nguyên $a, b, c,$ và $d$, sau đó in ra kết quả của phép tính: $a^b + c^d$.

**Input Format**

Bốn số nguyên $a, b, c,$ và $d$ lần lượt được cho trên bốn dòng riêng biệt.

**Constraints**

* $1 \le a \le 1000$
* $1 \le b \le 1000$
* $1 \le c \le 1000$
* $1 \le d \le 1000$

**Output Format**

In kết quả của $a^b + c^d$ trên một dòng duy nhất.

**Sample Input**

```markdown
9
29
7
27
```

**Sample Output**

```markdown
4710194409608608369201743232  
```

Ghi chú: Kết quả này lớn hơn $2^{63}-1$. Do đó, nó sẽ không thể lưu trữ vừa trong kiểu long long int của C++ hoặc một số nguyên 64-bit thông thường.
