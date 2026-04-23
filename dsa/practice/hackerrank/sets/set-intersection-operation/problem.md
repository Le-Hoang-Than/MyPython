# Set .intersection() Operation

![](https://s3.amazonaws.com/hr-challenge-images/9419/1437830945-a56a63892c-AB.png)

**.intersection()**

Toán tử .intersection() trả về tập giao của một tập hợp (set) và các phần tử trong một đối tượng có thể lặp (iterable).

Đôi khi, toán tử & được dùng thay thế cho .intersection(), nhưng nó chỉ hoạt động khi cả hai đối tượng đều là tập hợp (set).

Tập hợp gốc sẽ không bị thay đổi (immutable) sau phép toán .intersection() (hoặc toán tử &).

```markdown
>>> s = set("Hacker")
>>> print s.intersection("Rank")
set(['a', 'k'])

>>> print s.intersection(set(['R', 'a', 'n', 'k']))
set(['a', 'k'])

>>> print s.intersection(['R', 'a', 'n', 'k'])
set(['a', 'k'])

>>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
set([])

>>> print s.intersection({"Rank":1})
set([])

>>> s & set("Rank")
set(['a', 'k'])
```

**Task**

Sinh viên của trường Quận có đăng ký dài hạn báo tiếng Anh và báo tiếng Pháp. Một số sinh viên chỉ đăng ký báo tiếng Anh, một số chỉ đăng ký báo tiếng Pháp, và một số đăng ký cả hai loại báo.

Bạn được cho hai tập hợp chứa mã số sinh viên (roll numbers). Một tập hợp đăng ký báo tiếng Anh, tập hợp còn lại đăng ký báo tiếng Pháp. Nhiệm vụ của bạn là tìm tổng số sinh viên đăng ký cả hai loại báo.

**Input Format**

Dòng 1: Chứa $n$, số lượng sinh viên đăng ký báo tiếng Anh.

Dòng 2: Chứa $n$ mã số sinh viên đăng ký báo tiếng Anh, cách nhau bởi khoảng trắng.

Dòng 3: Chứa $m$, số lượng sinh viên đăng ký báo tiếng Pháp.

Dòng 4: Chứa $m$ mã số sinh viên đăng ký báo tiếng Pháp, cách nhau bởi khoảng trắng.

**Constraints**

$ 0 < \text{Total number of students in college} < 1000$

**Output Format**

In ra tổng số sinh viên có đăng ký cả hai loại báo tiếng Anh và tiếng Pháp.

**Sample Input**

```markdown
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

**Sample Output**

```markdown
5
```

**Explanation**

Các mã số sinh viên đăng ký cả hai loại báo là: 1, 2, 3, 6, 8.

Vì vậy, tổng cộng có 5 sinh viên.