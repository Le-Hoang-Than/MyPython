# Find a string

Trong thử thách này, người dùng nhập vào một chuỗi ký tự (string) và một chuỗi con (substring). Nhiệm vụ của bạn là in ra số lần chuỗi con đó xuất hiện trong chuỗi đã cho. Việc duyệt chuỗi sẽ thực hiện từ trái sang phải, không phải từ phải sang trái.

**LƯU Ý:** Các chữ cái trong chuỗi có phân biệt chữ hoa và chữ thường (case-sensitive).

**Input Format**

Dòng đầu tiên của đầu vào chứa chuỗi gốc. Dòng tiếp theo chứa chuỗi con.

**Constraints**

$1 \le \text{độ dài chuỗi gốc} \le 200$
Mỗi ký tự trong chuỗi là một ký tự ASCII.

**Output Format**

In ra một số nguyên cho biết tổng số lần chuỗi con xuất hiện trong chuỗi gốc.

**Sample Input**
```markdown
ABCDCDC
CDC
```

**Output Format**

Xuất ra số nguyên biểu thị tổng số lần xuất hiện của chuỗi con trong chuỗi gốc.

**Sample Input**

```markdown
ABCDCDC
CDC
```

**Sample Output**

```markdown
2
```

**Concept**

Có một vài khái niệm mới cần lưu ý:

Trong Python, độ dài của một chuỗi được tìm bằng hàm len(s), trong đó s là chuỗi ký tự.

Để duyệt qua toàn bộ độ dài của một chuỗi, hãy sử dụng vòng lặp for:

```markdown
for i in range(0, len(s)):
    print(s[i])
```

Hàm range được sử dụng để lặp qua một khoảng độ dài nào đó:

```markdown
range(0, 5)
```

Ở đây, vòng lặp sẽ chạy từ $0$ đến $4$. Giá trị $5$ bị loại trừ (không tính).

**Constraints**

$\text{-}$