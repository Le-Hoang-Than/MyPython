# itertools.combinations()

**itertools.combinations(iterable, r)**

Công cụ này trả về các dãy con (subsequences) có độ dài $r$ từ các phần tử của iterable đầu vào.

Các tổ hợp được đưa ra theo thứ tự từ điển. Do đó, nếu dữ liệu đầu vào đã được sắp xếp, các bộ tổ hợp trả về cũng sẽ xuất hiện theo thứ tự sắp xếp.

Khác với hoán vị, tổ hợp không quan tâm đến thứ tự các phần tử trong bộ (ví dụ: nếu đã có ('a', 'b') thì sẽ không có ('b', 'a')).

**Sample Code**

```text
>>> from itertools import combinations
>>> 
>>> # Tạo tổ hợp chập 2 của chuỗi '12345'
>>> print(list(combinations('12345', 2)))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> # Ví dụ với các phần tử trùng lặp
>>> A = [1, 1, 3, 3, 3]
>>> print(list(combinations(A, 4)))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
```

**Task**

Bạn được cho một chuỗi $S$.

Nhiệm vụ của bạn là in ra tất cả các tổ hợp có thể có, từ kích thước 1 cho đến kích thước $k$, của chuỗi đó theo thứ tự từ điển.

**Input Format**

Một dòng duy nhất chứa chuỗi $S$ và giá trị nguyên $k$, cách nhau bởi dấu cách.

**Constraints**

$0 < k \le \text{độ dài của chuỗi } S$

Chuỗi $S$ chỉ chứa các ký tự IN HOA.
 **Output Format**

In các tổ hợp khác nhau của chuỗi $S$ trên các dòng riêng biệt. Lưu ý: In các tổ hợp kích thước 1 trước, sau đó đến kích thước 2, và tiếp tục cho đến $k$.

**Sample Input**

```text
HACK 2
```

**Sample Output**

```text
A
C
H
K
AC
AH
AK
CH
CK
HK
```