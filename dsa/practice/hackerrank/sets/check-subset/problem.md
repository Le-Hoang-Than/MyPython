# Check Subset

Bạn được cho hai tập hợp, $A$ và $B$.

Nhiệm vụ của bạn là xác định xem tập hợp $A$ có phải là tập hợp con của tập hợp $B$ hay không.

Nếu tập hợp $A$ là tập hợp con của tập hợp $B$, in ra True.

Nếu tập hợp $A$ không phải là tập hợp con của tập hợp $B$, in ra False.

**Input Format**

Dòng đầu tiên chứa số lượng các trường hợp kiểm tra (test cases), $T$.

Với mỗi trường hợp kiểm tra:

Dòng 1: Chứa số lượng phần tử của tập hợp $A$.

Dòng 2: Chứa các phần tử của tập hợp $A$, cách nhau bởi dấu cách.

Dòng 3: Chứa số lượng phần tử của tập hợp $B$.

Dòng 4: Chứa các phần tử của tập hợp $B$, cách nhau bởi dấu cách.

**Constraints**

- $0 < T < 20$

- $0 < \text{Số phần tử của mỗi tập hợp} < 1000$

**Output Format**

In ra True hoặc False cho mỗi trường hợp kiểm tra trên từng dòng riêng biệt.

```markdown
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
```

**Sample Output**

```markdown
True 
False
False
```

**Explanation**

Trường hợp 01:

- Tập hợp $A = \{1, 2, 3, 5, 6\}$
- Tập hợp $B = \{9, 8, 5, 6, 3, 2, 1, 4, 7\}$
- Tất cả các phần tử của $A$ đều nằm trong $B$. 

Do đó, $A$ là tập hợp con của $B \rightarrow$ True.