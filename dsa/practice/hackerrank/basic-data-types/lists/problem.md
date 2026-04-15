# Lists

Cho một danh sách ban đầu là danh sách rỗng (list = []).
Bạn có thể thực hiện các lệnh sau:

1. insert i e: Chèn số nguyên $e$ vào vị trí (chỉ số) $i$.
2. print: In danh sách ra màn hình.
3. remove e: Xóa lần xuất hiện đầu tiên của số nguyên $e$.
4. append e: Thêm số nguyên $e$ vào cuối danh sách.
5. sort: Sắp xếp danh sách (tăng dần).
6. pop: Loại bỏ phần tử cuối cùng khỏi danh sách.
7. reverse: Đảo ngược thứ tự danh sách.

Hãy khởi tạo danh sách của bạn và đọc giá trị $n$ (số lượng lệnh),

sau đó đọc tiếp $n$ dòng lệnh, trong đó mỗi dòng chứa một trong các

loại lệnh được liệt kê ở trên. Duyệt qua từng lệnh theo thứ tự và

thực hiện thao tác tương ứng trên danh sách của bạn.

**Example**

$N = 4$

$append$ 1

$append$ 2

$insert$ 1 3

$print$

- append 1: Thêm $1$ vào danh sách, $\text{arr} = [1]$.
- append 2: Thêm $2$ vào danh sách, $\text{arr} = [1, 2]$.
- insert 1 3: Chèn $3$ vào vị trí chỉ số $1$, $\text{arr} = [1, 3, 2]$
- .print: In mảng.

Output:

```markdown
[1, 3, 2]
````

**Input Format**

Dòng đầu tiên chứa một số nguyên $n$, biểu thị số lượng lệnh.

Mỗi dòng trong số $n$ dòng tiếp theo chứa một trong các lệnh được mô tả ở trên.

**Constraints**

- Các phần tử được thêm vào danh sách phải là số nguyên.

**Output Format**

Đối với mỗi lệnh loại `print`, hãy in danh sách trên một dòng mới.

**Sample Input 0**

```markdown
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```

**Sample Output 0**

```text
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```