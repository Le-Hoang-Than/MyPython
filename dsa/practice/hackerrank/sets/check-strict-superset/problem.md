# Check Strict Superset

Bạn được cho một tập hợp $A$ và $n$ tập hợp khác.

Nhiệm vụ của bạn là xác định liệu tập hợp $A$ có phải là tập hợp siêu cấp nghiêm ngặt (strict superset) của mỗi tập hợp trong $n$ tập hợp đó hay không.

In ra True nếu $A$ là tập hợp siêu cấp nghiêm ngặt của tất cả các tập hợp còn lại. Ngược lại, in ra False.

Một tập hợp siêu cấp nghiêm ngặt phải có ít nhất một phần tử không tồn tại trong tập hợp con của nó.

**Example**

Tập $\{1, 2, 3\}$ là tập hợp siêu cấp nghiêm ngặt của tập $\{1, 2\}$.

Tập $\{1, 2, 3\}$ không phải là tập hợp siêu cấp nghiêm ngặt của tập $\{1, 2, 3\}$.

Tập $\{1, 2, 3\}$ không phải là tập hợp siêu cấp nghiêm ngặt của tập $\{1, 2, 4\}$.

**Input Format**

Dòng đầu tiên chứa các phần tử của tập hợp $A$, cách nhau bởi dấu cách.

Dòng thứ hai chứa số nguyên $n$, số lượng các tập hợp khác.

$n$ dòng tiếp theo chứa các phần tử của các tập hợp khác, cách nhau bởi dấu cách.

**Constraints**
- $0 < \text{len(set(A)) < 501}$
- $0 < n < 21$.
- $0 < \text{len(other Sets) < 101}$

**Output Format**

In ra True nếu tập hợp $A$ là tập hợp siêu cấp nghiêm ngặt của tất cả $n$ tập hợp còn lại. Ngược lại, in ra False.

**Sample Input 0**

```markdown
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
```

**Sample Output 0**

```markdown
False
```

**Explanation  0**

Tập hợp $A$ là tập hợp siêu cấp nghiêm ngặt của tập hợp thứ nhất nhưng không phải của tập hợp thứ hai vì giá trị 100 không có trong tập $A$. Do đó, kết quả là False.
