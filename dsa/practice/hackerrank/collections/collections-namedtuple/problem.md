# Collections.namedtuple()

**collections.namedtuple()**

Về cơ bản, namedtuples là các loại đối tượng nhẹ, dễ dàng tạo lập.

Chúng biến các bộ dữ liệu (tuples) thành những vùng chứa tiện lợi cho các tác vụ đơn giản.

Với namedtuples, bạn không cần phải sử dụng các chỉ số nguyên (index) để truy cập các thành phần của một tuple.

**Example**

**Code 01**

```text
>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
```

**Code 02**

```text
>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y
```

**Task**

Tiến sĩ John Wesley có một bảng tính chứa danh sách sinh viên gồm ID, MARKS (Điểm số), CLASS (Lớp) và NAME (Tên).

Nhiệm vụ của bạn là giúp Tiến sĩ Wesley tính điểm trung bình của các sinh viên.$$\text{Average} = \frac{\text{Tổng tất cả điểm số}}{\text{Tổng số sinh viên}}$$

**Lưu ý:**

1. Các cột có thể ở bất kỳ thứ tự nào. ID, MARKS, CLASS và NAME có thể được viết theo bất kỳ thứ tự nào trong bảng tính.
2. Tên các cột là ID, MARKS, CLASS và NAME. (Cách đánh vần và định dạng chữ hoa/thường của các tên này sẽ không thay đổi.)

**Input Format**

Dòng đầu tiên chứa một số nguyên $N$, tổng số sinh viên.

Dòng thứ hai chứa tên của các cột theo thứ tự bất kỳ.

$N$ dòng tiếp theo chứa các giá trị ID, MARKS, CLASS và NAME tương ứng dưới tên cột của chúng.

**Constraints**

$0 < N \le 100$

**Output Format**

In ra điểm trung bình của danh sách, làm tròn đến 2 chữ số thập phân.

**Sample Input**

**TESTCASE 01**

```text
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
```

**TESTCASE 02**

```text
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
```

**Sample Output**

**TESTCASE 01**

```text
78.00
```

**TESTCASE 02**

```text
81.00
```

**Explanation**

**TESTCASE 01**

Điểm trung bình = $(97 + 50 + 91 + 72 + 80) / 5 = 78.00$

Bạn có thể giải thử thách này trong 4 dòng code hoặc ít hơn không?

LƯU Ý: Không có hình phạt nào cho các giải pháp đúng nhưng có nhiều hơn 4 dòng code.