# Introduction to Sets

Một tập hợp (set) là một tập hợp các phần tử không có thứ tự và không chứa các giá trị trùng lặp.

Khi được in ra, lặp qua (iterate) hoặc chuyển đổi thành một dãy, các phần tử của nó sẽ xuất hiện theo một thứ tự ngẫu nhiên (không định trước).

**Example**

```markdown
>>> print set()
set([])

>>> print set('HackerRank')
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print set((1,2,3,4,5,5))
set([1, 2, 3, 4, 5])

>>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
set(['Hacker', 'Rank'])

>>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
```

Về cơ bản, tập hợp (sets) được sử dụng để kiểm tra tư cách thành viên (phần tử có nằm trong tập hay không) và loại bỏ các giá trị trùng lặp.

**Task**

Bây giờ, hãy sử dụng kiến thức về tập hợp để giúp Mickey.

Cô Gabriel Williams là giáo sư thực vật học tại trường Cao đẳng Quận. Một ngày nọ, cô yêu cầu sinh viên của mình là Mickey tính trung bình cộng chiều cao của tất cả các loài cây có chiều cao khác nhau (distinct heights) trong nhà kính.

Công thức sử dụng:

$$\text{Average} = \frac{\text{Tổng các giá trị khác nhau}}{\text{Tổng số lượng các giá trị khác nhau}}$$

**Function Description**

Hãy hoàn thành hàm `average` trong trình chỉnh sửa bên dưới.

`average` trung bình có các tham số sau:
- int arr: một mảng các số nguyên đại diện cho chiều cao của cây.

**Returns**
- float: giá trị số thực thu được, được làm tròn đến 3 chữ số thập phân.

**Input Format**

Dòng đầu tiên chứa số nguyên $N$, là kích thước của mảng arr.

Dòng thứ hai chứa $N$ số nguyên cách nhau bởi khoảng trắng, đại diện cho các giá trị trong arr.

**Sample Input**

```markdown
STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
```

**Sample Output**

```markdown
169.375
```

**Explanation**

Tại đây, set ([154, 161, 167, 170, 171, 174, 176, 182]) là tập hợp chứa các chiều cao riêng biệt. Bằng cách sử dụng các hàm sum() và len(), chúng ta có thể tính toán được giá trị trung bình.

$$\text{Average} = \frac{\text{1355}}{\text{8}} = \text{169.375}$$
