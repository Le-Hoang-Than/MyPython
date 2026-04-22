# Symmetric Difference

**Objective**

Hôm nay, chúng ta sẽ tìm hiểu về một kiểu dữ liệu mới: tập hợp (sets).

**Concept**

Nếu các đầu vào được đưa ra trên cùng một dòng và cách nhau bởi một ký tự (dấu phân cách), hãy sử dụng split() để lấy các giá trị riêng biệt dưới dạng một danh sách (list). Dấu phân cách mặc định là khoảng trắng (ascii 32). Để chỉ định dấu phẩy là dấu phân cách, hãy sử dụng string.split(','). Trong thử thách này, và thông thường trên HackerRank, khoảng trắng sẽ là dấu phân cách.

Cách dùng:

```markdown
>> a = raw_input()
5 4 3 2
>> lis = a.split()
>> print (lis)
['5', '4', '3', '2']
```

Nếu các giá trị trong danh sách đều là kiểu số nguyên, hãy sử dụng phương thức map() để chuyển đổi tất cả các chuỗi thành số nguyên.

```markdown
>> newlis = list(map(int, lis))
>> print (newlis)
[5, 4, 3, 2]
```

Tập hợp là một bộ sưu tập không có thứ tự của các giá trị duy nhất. Một tập hợp đơn lẻ có thể chứa các giá trị thuộc bất kỳ kiểu dữ liệu bất biến (immutable) nào.

**CREATING SETS**

```markdown
>> myset = {1, 2} # Directly assigning values to a set
>> myset = set()  # Initializing a set
>> myset = set(['a', 'b']) # Creating a set from a list
>> myset
{'a', 'b'}
```

**MODIFYING SETS**

Sử dụng hàm add():

```markdown
>> myset.add('c')
>> myset
{'a', 'c', 'b'}
>> myset.add('a') # As 'a' already exists in the set, nothing happens
>> myset.add((5, 4))
>> myset
{'a', 'c', 'b', (5, 4)}
```

Sử dụng hàm update():

```markdown
>> myset.update([1, 2, 3, 4]) # update() only works for iterable objects
>> myset
{'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
>> myset.update({1, 7, 8})
>> myset
{'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
>> myset.update({1, 6}, [5, 13])
>> myset
{'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}
```

**REMOVING ITEMS**

Cả hai hàm discard() và remove() đều nhận một giá trị duy nhất làm đối số và xóa giá trị đó khỏi tập hợp. Nếu giá trị đó không tồn tại, discard() sẽ không làm gì cả, nhưng remove() sẽ báo lỗi KeyError.

```markdown
>> myset.discard(10)
>> myset
{'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
>> myset.remove(13)
>> myset
{'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}
```

**COMMON SET OPERATIONS**

Sử dụng các hàm union() (hợp), intersection() (giao) và difference() (hiệu).

![](https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSH37mEPm33_o-IDteM-Q3dd97uh1CM47-fOfWXOhoL8_Sbrr9tnlkHSu1bL6fMgYIOIG2t8SXY5jprVBReNGLVRlaNRXn21BBR0sN2aoNueG_0wVs)

```markdown
>> a = {2, 4, 5, 9}
>> b = {2, 4, 11, 12}
>> a.union(b) # Values which exist in a or b
{2, 4, 5, 9, 11, 12}
>> a.intersection(b) # Values which exist in a and b
{2, 4}
>> a.difference(b) # Values which exist in a but not in b
{9, 5}
```

Các hàm union() và intersection() có tính đối xứng:

```markdown
>> a.union(b) == b.union(a)
True
>> a.intersection(b) == b.intersection(a)
True
>> a.difference(b) == b.difference(a)
False
```

**Task**

Cho hai tập hợp số nguyên, $M$ và $N$, hãy in ra hiệu đối xứng (symmetric difference) của chúng theo thứ tự tăng dần. Thuật ngữ "hiệu đối xứng" chỉ những giá trị tồn tại trong tập hợp $M$ hoặc $N$ nhưng không tồn tại trong cả hai.

**Input Format**

Dòng đầu tiên chứa số nguyên $M$.

Dòng thứ hai chứa $M$ số nguyên cách nhau bởi khoảng trắng.

Dòng thứ ba chứa số nguyên $N$.

Dòng thứ tư chứa $N$ số nguyên cách nhau bởi khoảng trắng.

**Output Format**

In các số nguyên thuộc hiệu đối xứng theo thứ tự tăng dần, mỗi số trên một dòng.

**Sample Input**

```markdown
STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
```

**Sample Output**

```markdown
5
9
11
12
```