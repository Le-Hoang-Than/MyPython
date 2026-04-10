# Python If-Else

**Task**

Cho một số nguyên dương $n$, hãy thực hiện các hành động điều kiện sau:

- Nếu $n$ là số lẻ: In ra `Weird` (Kỳ lạ).
- Nếu $n$ là số chẵn và nằm trong khoảng từ 2 đến 5 (bao gồm cả 2 và 5): In ra `Not Weird` (Không kỳ lạ).
- Nếu $n$ là số chẵn và nằm trong khoảng từ 6 đến 20 (bao gồm cả 6 và 20): In ra `Weird`.
- Nếu $n$ là số chẵn và lớn hơn 20: In ra `Not Weird`.

**Input Format**

Một dòng duy nhất chứa một số nguyên dương $n$.

**Constraints**

- 1 ≤ $n$ ≤ 100

**Output Format**

In ra `Weird` nếu số đó thỏa mãn điều kiện "kỳ lạ". Ngược lại, in ra `Not Weird`.

**Sample Input 0**

```markdown
3
```

**Sample Output 0**

```markdown
Weird
```

**Explanation 0**

$n$ = 3

$n$ là số lẻ mà số lẻ là "kỳ lạ", nên in `Weird`.

**Sample Input 1**

```markdown
24
```

**Sample Outphut 1**

```markdown
Not Weird
```

**Explanation 1**

$n$ = 24

$n$ > 20 và là số chẵn, nên nó không "kỳ lạ".
