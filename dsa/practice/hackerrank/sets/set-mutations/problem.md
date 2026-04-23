# Set Mutations

Chúng ta đã thấy ứng dụng của các phép toán hợp (union), giao (intersection), hiệu (difference) và hiệu đối xứng (symmetric difference), nhưng các phép toán này không làm thay đổi hay biến đổi (mutate) tập hợp gốc.

Để thay đổi trực tiếp nội dung của một tập hợp, chúng ta có thể sử dụng các phương thức sau:

**.update() hoặc |=**

Cập nhật tập hợp bằng cách thêm các phần tử từ một đối tượng có thể lặp (iterable) hoặc một tập hợp khác.

```markdown
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
```

**.intersection_update() hoặc &=**

Cập nhật tập hợp bằng cách chỉ giữ lại các phần tử có mặt trong cả chính nó và một tập hợp khác.

```markdown
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
```

**.difference_update() hoặc -=**

Cập nhật tập hợp bằng cách loại bỏ các phần tử có mặt trong một tập hợp khác.

```markdown
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
```

**.symmetric_difference_update() hoặc ^=**

Cập nhật tập hợp bằng cách chỉ giữ lại các phần tử xuất hiện ở một trong hai tập hợp, nhưng không xuất hiện ở cả hai.

```markdown
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
```

**TASK**

Bạn được cho một tập hợp $A$ và $N$ tập hợp khác. Với $N$ tập hợp này, bạn phải thực hiện các thao tác biến đổi cụ thể lên tập hợp $A$.

Nhiệm vụ của bạn là thực thi các thao tác đó và in ra tổng các phần tử còn lại trong tập hợp $A$.

**Input Format**

Dòng 1: Chứa số lượng phần tử của tập hợp $A$.

Dòng 2: Chứa danh sách các phần tử của tập hợp $A$, cách nhau bởi dấu cách.

Dòng 3: Chứa số nguyên $N$, số lượng các tập hợp khác.

$2 \times N$ dòng tiếp theo: Chia thành $N$ phần, mỗi phần gồm 2 dòng:

- Dòng thứ nhất của mỗi phần chứa tên thao tác và độ dài của tập hợp khác, cách nhau bởi dấu cách.
- Dòng thứ hai của mỗi phần chứa danh sách các phần tử của tập hợp khác đó, cách nhau bởi dấu cách.

**Output Format**

In ra tổng các phần tử trong tập hợp $A$.

**Sample Input**

```markdown
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
```

**Sample Output**

```markdown
38
```

**Explanation**

Sau phép toán đầu tiên (intersection_update), tập hợp $A$ chỉ còn các phần tử chung với tập hợp 10 phần tử đã cho.

Sau phép toán thứ hai (update), thêm 55 và 66 vào $A$.

Sau phép toán thứ ba (symmetric_difference_update), $A$ cập nhật các phần tử chỉ có ở một trong hai bên.

Sau phép toán cuối cùng (difference_update), loại bỏ các phần tử trùng với tập hợp cuối.

Cuối cùng, tổng các số còn lại trong $A$ là 38.