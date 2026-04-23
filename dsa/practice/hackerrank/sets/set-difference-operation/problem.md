# Set .difference() Operation

![](https://s3.amazonaws.com/hr-challenge-images/9420/1437904659-11e4bef847-A-B.png)

**.difference()**

Công cụ .difference() trả về một tập hợp chứa tất cả các phần tử có trong tập hợp gốc nhưng không xuất hiện trong một đối tượng có thể lặp (iterable) khác.

Đôi khi toán tử - được sử dụng thay thế cho .difference(), nhưng nó chỉ hoạt động khi cả hai đối tượng đều là tập hợp (set).

Tập hợp gốc sẽ không bị thay đổi (immutable) sau phép toán .difference() (hoặc toán tử -).

```markdown
>>> s = set("Hacker")
>>> # Hiệu với một chuỗi (string)
>>> print s.difference("Rank")
set(['c', 'r', 'e', 'H'])

>>> # Hiệu với một tập hợp (set)
>>> print s.difference(set(['R', 'a', 'n', 'k']))
set(['c', 'r', 'e', 'H'])

>>> # Hiệu với một danh sách (list)
>>> print s.difference(['R', 'a', 'n', 'k'])
set(['c', 'r', 'e', 'H'])

>>> # Sử dụng toán tử - (bắt buộc cả hai phải là set)
>>> s - set("Rank")
set(['H', 'c', 'r', 'e'])
```

**Task**

Sinh viên của trường Quận đăng ký mua báo tiếng Anh và báo tiếng Pháp. Một số sinh viên chỉ đăng ký báo tiếng Anh, một số chỉ đăng ký báo tiếng Pháp, và một số đăng ký cả hai loại báo.

Bạn được cho hai tập hợp chứa mã số sinh viên (roll numbers). Một tập hợp là những sinh viên đăng ký báo tiếng Anh, tập còn lại là những sinh viên đăng ký báo tiếng Pháp. Nhiệm vụ của bạn là tìm tổng số sinh viên chỉ đăng ký báo tiếng Anh.

**Input Format**

Dòng 1: Số lượng sinh viên đăng ký báo tiếng Anh.

Dòng 2: Danh sách mã số sinh viên đăng ký báo tiếng Anh (cách nhau bởi khoảng trắng).

Dòng 3: Số lượng sinh viên đăng ký báo tiếng Pháp.

Dòng 4: Danh sách mã số sinh viên đăng ký báo tiếng Pháp (cách nhau bởi khoảng trắng).

**Output Format**

In ra tổng số sinh viên chỉ đăng ký báo tiếng Anh.

**Sample Input**

```markdown
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

**Sample Output**

```markdown
4
```

**Explanation**

Các mã số sinh viên chỉ đăng ký báo tiếng Anh (có trong tập Anh nhưng không có trong tập Pháp) là:

4, 5, 7 và 9.

Vì vậy, tổng cộng là 4 sinh viên.