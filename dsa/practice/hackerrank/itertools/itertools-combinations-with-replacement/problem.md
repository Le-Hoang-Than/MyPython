# itertools.combinations_with_replacement()

**itertools.combinations_with_replacement(iterable, r)**

Công cụ này trả về các dãy con có độ dài $r$ từ các phần tử của iterable đầu vào, cho phép các phần tử riêng lẻ được lặp lại nhiều hơn một lần.

Các tổ hợp được đưa ra theo thứ tự từ điển. Do đó, nếu dữ liệu đầu vào đã được sắp xếp, các bộ tổ hợp trả về cũng sẽ xuất hiện theo thứ tự sắp xếp.

Điểm khác biệt so với combinations thông thường là một phần tử có thể tự kết hợp với chính nó (ví dụ: có thể có ('1', '1')).

**Sample Code**

```text
>>> from itertools import combinations_with_replacement
>>> 
>>> # Tổ hợp lặp chập 2 của chuỗi '12345'
>>> print list(combinations_with_replacement('12345',2))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
```

**Task**

Bạn được cho một chuỗi $S$.

Nhiệm vụ của bạn là in ra tất cả các tổ hợp lặp có kích thước $k$ của chuỗi đó theo thứ tự từ điển.

**Input Format**

Một dòng duy nhất chứa chuỗi $S$ và giá trị nguyên $k$, cách nhau bởi một dấu cách.

**Constraints**

$0 < k \le \text{độ dài của chuỗi } S$

Chuỗi $S$ chỉ chứa các ký tự IN HOA.

**Output Format**

In các tổ hợp lặp của chuỗi $S$ trên các dòng riêng biệt.

**Sample Input**

```text
HACK 2
```

**Sample Output**

```text
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
```