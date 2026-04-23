# Set .symmetric_difference() Operation

![](https://s3.amazonaws.com/hr-challenge-images/9421/1437912471-534f33cf60-AB.png)

**.symmetric_difference()**

Toán tử .symmetric_difference() trả về một tập hợp chứa tất cả các phần tử thuộc về một trong hai tập hợp (tập hợp gốc hoặc đối tượng có thể lặp), nhưng không thuộc về cả hai.

Nói cách khác, nó loại bỏ các phần tử chung (phần giao) và giữ lại những phần tử riêng biệt của mỗi bên.

Đôi khi, toán tử ^ được dùng thay thế cho phương thức .symmetric_difference(), nhưng nó chỉ hoạt động khi cả hai đối tượng đều là tập hợp (set).

Tập hợp gốc sẽ không bị thay đổi (immutable) sau phép toán này.

```markdown
>>> s = set("Hacker")
>>> # Hiệu đối xứng với một chuỗi (iterable)
>>> print s.symmetric_difference("Rank")
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> # Sử dụng toán tử ^ (bắt buộc cả hai là set)
>>> s ^ set("Rank")
set(['c', 'e', 'H', 'n', 'R', 'r'])
```

**Task**

Sinh viên của trường Quận có đăng ký báo tiếng Anh và báo tiếng Pháp. Một số sinh viên chỉ đăng ký báo tiếng Anh, một số chỉ đăng ký báo tiếng Pháp, và một số đăng ký cả hai.

Bạn được cho hai tập hợp mã số sinh viên. Một tập đăng ký báo tiếng Anh, tập còn lại đăng ký báo tiếng Pháp. Nhiệm vụ của bạn là tìm tổng số sinh viên chỉ đăng ký duy nhất một loại báo (đăng ký báo Anh hoặc báo Pháp nhưng không phải cả hai).

**Input Format**

Dòng 1: Số lượng sinh viên đăng ký báo tiếng Anh.

Dòng 2: Danh sách mã số sinh viên đăng ký báo tiếng Anh (cách nhau bởi khoảng trắng).

Dòng 3: Số lượng sinh viên đăng ký báo tiếng Pháp.

Dòng 4: Danh sách mã số sinh viên đăng ký báo tiếng Pháp (cách nhau bởi khoảng trắng).

**Output Format**

In ra tổng số sinh viên có đăng ký báo tiếng Anh hoặc tiếng Pháp nhưng không đăng ký cả hai.

**Sample Input**

```markdown
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

**Sample Output**

```markdown
8
```

**Explanation**

Các mã số sinh viên có đăng ký báo Anh hoặc Pháp nhưng không phải cả hai là:

4, 5, 7, 9 (từ tập tiếng Anh) và 10, 11, 21, 55 (từ tập tiếng Pháp).

Tổng cộng có 8 sinh viên.