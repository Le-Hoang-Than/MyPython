# DefaultDict Tutorial

Công cụ defaultdict là một vùng chứa (container) thuộc lớp collections trong Python. Nó tương tự như từ điển (dict) thông thường, nhưng điểm khác biệt duy nhất là defaultdict sẽ có một giá trị mặc định nếu khóa (key) đó chưa được thiết lập. Nếu bạn không sử dụng defaultdict, bạn sẽ phải kiểm tra xem khóa đó có tồn tại hay không, và nếu không, hãy đặt nó thành giá trị bạn muốn.

**Ví dụ:**
```text
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
```

**Kết quả in ra:**

```text
('python', ['awesome', 'language'])
('something-else', ['not relevant'])
```

Trong thử thách này, bạn sẽ được cho hai số nguyên $n$ và $m$. Có $n$ từ (có thể lặp lại) trong nhóm từ $A$. Có $m$ từ thuộc nhóm từ $B$. Đối với mỗi từ trong $m$ từ đó, hãy kiểm tra xem từ đó đã xuất hiện trong nhóm $A$ hay chưa. In ra các chỉ số (vị trí) của mỗi lần xuất hiện của từ đó trong nhóm $A$. Nếu nó không xuất hiện, in ra $-1$.

**Example**

Nhóm A chứa 'a', 'b', 'a'

Nhóm B chứa 'a', 'c'

Đối với từ đầu tiên trong nhóm B là 'a', nó xuất hiện tại vị trí $1$ và $3$ trong nhóm A. Từ thứ hai là 'c' không xuất hiện trong nhóm A, vì vậy in ra $-1$.

Kết quả mong đợi:

```text
1 3
-1
```

**Input Format**

Dòng đầu tiên chứa các số nguyên $n$ và $m$ cách nhau bởi dấu cách.

$n$ dòng tiếp theo chứa các từ thuộc nhóm $A$.

$m$ dòng tiếp theo chứa các từ thuộc nhóm $B$.

**Constraints**

$1 \le n \le 10000$

$1 \le m \le 100$

$1 \le \text{độ dài mỗi từ} \le 100$

**Output Format**

In ra $m$ dòng.

Dòng thứ $i$ nên chứa các vị trí (bắt đầu từ chỉ số 1) của các lần xuất hiện của từ thứ $i$ trong nhóm $B$, cách nhau bởi dấu cách.

**Sample Input**

```text
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
```

**Sample Output**

```text
1 2 4
3 5
```

**Explanation**

'a' xuất hiện 3 lần tại các vị trí $1, 2$ và $4$.

'b' xuất hiện 2 lần tại các vị trí $3$ và $5$.

Trong bài toán mẫu, nếu 'c' cũng xuất hiện trong nhóm từ $B$, bạn sẽ in ra $-1$.

