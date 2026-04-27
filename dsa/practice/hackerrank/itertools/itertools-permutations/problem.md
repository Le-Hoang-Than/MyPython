# itertools.permutations()

**itertools.permutations(iterable[, r])**

Công cụ này trả về các hoán vị có độ dài $r$ kế tiếp nhau của các phần tử trong một iterable.

Nếu $r$ không được chỉ định hoặc bằng None, thì $r$ mặc định là độ dài của iterable, và tất cả các hoán vị có độ dài đầy đủ sẽ được tạo ra.

Các hoán vị được in ra theo thứ tự từ điển (lexicographic sorted order). Do đó, nếu dữ liệu đầu vào đã được sắp xếp, các bộ hoán vị trả về cũng sẽ xuất hiện theo thứ tự sắp xếp.

**Sample Code**

```text
>>> from itertools import permutations
>>> # Hoán vị đầy đủ (không chỉ định r)
>>> print(list(permutations(['1','2','3'])))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> # Hoán vị độ dài r = 2
>>> print(list(permutations(['1','2','3'], 2)))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
```

**Task**

Bạn được cho một chuỗi $S$.

Nhiệm vụ của bạn là in ra tất cả các hoán vị có thể có với kích thước $k$ của chuỗi đó theo thứ tự từ điển.

**Input Format**

Một dòng duy nhất chứa chuỗi $S$ và giá trị nguyên $k$, cách nhau bởi dấu cách.

**Constraints**

$0 < k \le \text{độ dài của chuỗi } S$

Chuỗi $S$ chỉ chứa các ký tự IN HOA.

**Output Format**

In các hoán vị của chuỗi trên các dòng riêng biệt.

**Sample Input**

```text
HACK 2
```

**Sample Output**

```text
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
```

**Explanation**

Tất cả các hoán vị có kích thước 2 khả thi của chuỗi "HACK" đều được in ra theo thứ tự sắp xếp từ điển (lexicographic sorted order).