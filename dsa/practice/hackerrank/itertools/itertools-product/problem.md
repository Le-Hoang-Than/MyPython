# itertools.product()

Công cụ này dùng để tính tích Cartesian (tích đề-các) của các dữ liệu đầu vào có thể lặp lại (iterables).

Nó có tác dụng tương đương với các vòng lặp for lồng nhau.

Ví dụ: product(A, B) sẽ trả về kết quả giống như ((x,y) for x in A for y in B).

**Sample code**
```text
>>> from itertools import product
>>>
>>> print list(product([1,2,3],repeat = 2))
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
>>>
>>> print list(product([1,2,3],[3,4]))
[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
>>>
>>> A = [[1,2,3],[3,4,5]]
>>> print list(product(*A))
[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
>>>
>>> B = [[1,2,3],[3,4,5],[7,8]]
>>> print list(product(*B))
[(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]
```

**Task**

Bạn được cho hai danh sách $A$ và $B$. Nhiệm vụ của bạn là tính tích Cartesian $A \times B$.

**Example**

```text
A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
```

**Lưu ý:** $A$ và $B$ là các danh sách đã được sắp xếp, và các bộ (tuples) kết quả của tích Cartesian cũng phải được in ra theo thứ tự đã sắp xếp.

**Input Format**

Dòng thứ nhất chứa các phần tử của danh sách $A$, cách nhau bởi dấu cách.

Dòng thứ hai chứa các phần tử của danh sách $B$, cách nhau bởi dấu cách.

Cả hai danh sách đều không có các phần tử số nguyên trùng lặp.

**Constraints**

$0 < A < 30$

$0 < B < 30$

**Output Format**

In ra các bộ (tuples) của tích Cartesian, mỗi bộ cách nhau bởi một dấu cách.

**Sample Input**

```text
1 2
3 4
```

**Sample Output**

```text
(1, 3) (1, 4) (2, 3) (2, 4)
```