# Set .union() Operation

![](https://s3.amazonaws.com/hr-challenge-images/9417/1437829708-707212e33e-AuB.png)

**.union()**

**Example**

```markdown
>>> s = set("Hacker")
>>> print s.union("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(set(['R', 'a', 'n', 'k']))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(['R', 'a', 'n', 'k'])
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

>>> print s.union({"Rank":1})
set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

>>> s | set("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])
```


Toán tử .union() trả về hợp của một tập hợp và một nhóm các phần tử trong một đối tượng có thể lặp lại (iterable).

Đôi khi, toán tử | được sử dụng thay cho toán tử .union(), nhưng nó chỉ hoạt động giữa các tập hợp (set) với nhau.

Tập hợp là đối tượng không thay đổi (immutable) đối với phép toán .union() (hoặc toán tử |).

**Task**

Sinh viên của trường Cao đẳng Quận đăng ký mua báo tiếng Anh và tiếng Pháp. Một số sinh viên chỉ đăng ký báo tiếng Anh, một số chỉ đăng ký báo tiếng Pháp và một số đăng ký cả hai loại báo.

Bạn được cho hai tập hợp chứa số thứ tự (roll numbers) của sinh viên. Một tập hợp đã đăng ký báo tiếng Anh và tập hợp còn lại đăng ký báo tiếng Pháp. Một sinh viên có thể nằm trong cả hai tập hợp. Nhiệm vụ của bạn là tìm tổng số sinh viên đã đăng ký ít nhất một loại báo.

**Input Format**

Dòng đầu tiên chứa một số nguyên $n$, số lượng sinh viên đã đăng ký báo tiếng Anh.

Dòng thứ hai chứa $n$ số thứ tự của các sinh viên đó, cách nhau bởi khoảng trắng.

Dòng thứ ba chứa $m$, số lượng sinh viên đã đăng ký báo tiếng Pháp.

Dòng thứ tư chứa $m$ số thứ tự của các sinh viên đó, cách nhau bởi khoảng trắng.

**Constraints**

$0 < \text{Số lượng phần tử trong mỗi tập hợp} < 1000$

**Output Format**

In ra tổng số sinh viên có ít nhất một đăng ký.

**Sample Input**

```markdown
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

**Sample Output**

```markdown
13
```

**Explanation**

Số thứ tự của các sinh viên có ít nhất một đăng ký:

`1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 55`

Là hợp của tập hợp báo tiếng Anh và báo tiếng Pháp. Các số thứ tự: $1, 2, 3, 6$ và $8$ xuất hiện trong cả hai tập hợp nên chúng chỉ được đếm một lần.

Do đó, tổng cộng có 13 sinh viên.