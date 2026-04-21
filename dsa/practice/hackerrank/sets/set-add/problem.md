# Set .add()

Nếu chúng ta muốn thêm một phần tử đơn lẻ vào một tập hợp đã có, chúng ta có thể sử dụng toán tử .add().

Nó sẽ thêm phần tử vào tập hợp và trả về 'None'.

**Example**

```markdown
>>> s = set('HackerRank')
>>> s.add('H')
>>> print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
>>> print s.add('HackerRank')
None
>>> print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])
```

**Task**

Hãy vận dụng kiến thức của bạn về toán tử .add() để giúp người bạn Rupal.

Rupal có một bộ sưu tập tem quốc gia khổng lồ. Cô ấy quyết định đếm tổng số tem quốc gia riêng biệt trong bộ sưu tập của mình và nhờ bạn giúp đỡ. Bạn lấy từng con tem một từ một chồng gồm N con tem quốc gia.

Hãy tìm tổng số lượng tem quốc gia riêng biệt.

**Input Format**

Dòng đầu tiên chứa một số nguyên $N$, tổng số tem quốc gia.

$N$ dòng tiếp theo chứa tên của quốc gia nơi con tem đó xuất xứ.

**Constraints**

$0 < N < 1000$

**Output Format**

In ra tổng số tem quốc gia riêng biệt trên một dòng duy nhất.

**Sample Input**

```markdown
7
UK
China
USA
France
New Zealand
UK
France 
```

**Sample Output**

```markdown
5
```

**Explanation**

UK và France lặp lại hai lần. Do đó, tổng số tem quốc gia riêng biệt là 5 (năm).