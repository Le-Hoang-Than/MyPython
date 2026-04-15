# List Comprehensions

Hãy cùng tìm hiểu về List Comprehensions! 
Bạn được cho ba số nguyên $x, y, z$ đại diện cho kích thước của 
một hình hộp chữ nhật và một số nguyên $n$.

Hãy in ra một danh sách tất cả các tọa độ $(i, j, k)$ có thể có 
trên lưới 3D, trong đó tổng của $i + j + k$ không được bằng $n$.

Các giá trị nằm trong khoảng:

- $0 \le i \le x$
- $0 \le j \le y$
- $0 \le k \le z$

Hãy sử dụng list comprehensions thay vì dùng nhiều vòng lặp 
lồng nhau để luyện tập kỹ năng này.

**Example**

- $x = 1$
- $y = 1$
- $z = 1$
- $n = 3$

Tất cả các hoán vị của $[i, j, k]$ là:

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]].

In ra danh sách các phần tử có tổng khác 3:

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0]].

**Input Format**

Bốn số nguyên $x, y, z$ và $n$, mỗi số nằm trên một dòng riêng biệt.

**Constraints**

In danh sách theo thứ tự tăng dần (thứ tự từ điển - lexicographic).

**Sample Input 0**

```markdown
1
1
1
2
```

**Sample Output 0**

```text
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

**Explanation 0**

Mỗi biến $i, j, k$ sẽ nhận giá trị $0$ hoặc $1$. Tất cả các hoán vị
có dạng 

$[i, j, k] = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]$.

Loại bỏ tất cả các mảng có tổng bằng $n = 2$, chỉ để lại các hoán vị hợp lệ.

**Sample Input 1**

```markdown
2
2
2
2
```

**Sample Output 1**

```markdown
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
```
