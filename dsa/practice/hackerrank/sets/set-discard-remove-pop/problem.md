# Set .discard(), .remove() & .pop()

**.remove(x)**

Toán tử này xóa phần tử $x$ khỏi tập hợp.

Nếu phần tử $x$ không tồn tại, nó sẽ gây ra lỗi KeyError.

Toán tử `.remove(x)` trả về giá trị None.

**Example**

```markdown
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0
```

**.discard(x)**

Toán tử này cũng xóa phần tử $x$ khỏi tập hợp.

Nếu phần tử $x$ không tồn tại, nó không gây ra lỗi KeyError.

Toán tử .discard(x) trả về giá trị None.

**Example**

```markdown
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
```

**.pop()**

Toán tử này xóa và trả về một phần tử bất kỳ từ tập hợp.

Nếu tập hợp không có phần tử nào để xóa, nó sẽ gây ra lỗi KeyError.

**Example**

```markdown
>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set
```

**Task**

Bạn có một tập hợp $s$ không rỗng, và bạn phải thực thi $N$ lệnh được đưa ra trong $N$ dòng tiếp theo.

Các lệnh sẽ bao gồm: pop, remove và discard.

**Input Format**

Dòng đầu tiên chứa số nguyên $n$, số lượng phần tử trong tập hợp $s$.

Dòng thứ hai chứa $n$ phần tử của tập hợp $s$, cách nhau bởi khoảng trắng. Tất cả các phần tử đều là số nguyên không âm, nhỏ hơn hoặc bằng 9.

Dòng thứ ba chứa số nguyên $N$, số lượng lệnh thực thi.

$N$ dòng tiếp theo chứa các lệnh pop, remove và/hoặc discard, theo sau là giá trị tương ứng (nếu có).

**Constraints**

$0 < n < 20$
$0 < N < 20$

**Output Format**

In ra tổng các phần tử còn lại của tập hợp $s$ trên một dòng duy nhất.

**Sample Input**

```markdown
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
```

**Sample Output**

```markdown
4
```

**Explanation**

Sau khi hoàn thành 10 thao tác trên, tập hợp $s$ còn lại các phần tử mà tổng của chúng là 4.

Lưu ý: Hãy chuyển đổi các phần tử của tập hợp $s$ sang kiểu số nguyên (integer) khi gán chúng. Để đảm bảo việc nhập dữ liệu cho tập hợp chính xác, chúng tôi đã thêm hai dòng mã đầu tiên vào trình chỉnh sửa.