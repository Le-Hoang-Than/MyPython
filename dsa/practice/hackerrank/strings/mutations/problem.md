### Mutations

Chúng ta đã biết rằng `list` (danh sách) có thể thay đổi (**mutable**), còn `tuple` thì không thể thay đổi (**immutable**).

Hãy cùng tìm hiểu điều này qua một ví dụ. Giả sử bạn có một chuỗi ký tự (string) - vốn là một đối tượng không thể thay
đổi - và bạn muốn chỉnh sửa nó.

**Example**

```markdown
> > > string = "abracadabra"
```

Bạn có thể truy cập một vị trí (index) bằng cách:

```markdown
> > > print string[5]
a
```

Nhưng chuyện gì sẽ xảy ra nếu bạn muốn gán một giá trị mới vào vị trí đó?

```markdown
> > > string[5] = 'k'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

Làm thế nào để giải quyết vấn đề này?

- Cách 1: Chuyển đổi chuỗi thành một danh sách (list), sau đó thay đổi giá trị và nối lại thành chuỗi.

**Example**

```markdown
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
```

- Cách 2: Sử dụng kỹ thuật cắt chuỗi (slicing) và nối chúng lại với nhau.

**Example**

```markdown
>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
```

**Task**

Đọc một chuỗi cho trước, thay đổi ký tự tại một vị trí (index) xác định và sau đó in ra chuỗi đã được sửa đổi.

**Function Description**

Hãy hoàn thành hàm `mutate_string` trong trình soạn thảo.

Hàm mutate_string có các tham số sau:
- string string: chuỗi ký tự cần thay đổi.
- int position: vị trí (index) để chèn ký tự mới.
- string character: ký tự cần chèn vào.

**Returns**

- string: chuỗi ký tự sau khi đã thay đổi.

**Input Format**

- Dòng đầu tiên chứa một chuỗi ký tự $S$.
- Dòng tiếp theo chứa số nguyên $position$ (vị trí index) và một ký tự $character$, cách nhau bởi một khoảng trắng.

**Sample Input**

```markdown
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
```

**Sample Output**

```markdown
abrackdabra
```