# No Idea!

Cho một mảng gồm $n$ số nguyên. Ngoài ra còn có hai tập hợp rời nhau $A$ và $B$, mỗi tập hợp chứa $m$ số nguyên. Bạn thích tất cả các số nguyên trong tập hợp $A$ và ghét tất cả các số nguyên trong tập hợp $B$. Chỉ số hạnh phúc ban đầu của bạn là $0$. Đối với mỗi số nguyên $i$ trong mảng:

- Nếu $i$ thuộc tập hợp $A$, bạn cộng $1$ vào chỉ số hạnh phúc.
- Nếu $i$ thuộc tập hợp $B$, bạn trừ $1$ vào chỉ số hạnh phúc.
- Nếu không, chỉ số hạnh phúc của bạn không thay đổi.

Hãy in ra tổng chỉ số hạnh phúc cuối cùng của bạn.

**Lưu ý:** Vì $A$ và $B$ là các tập hợp, chúng không có các phần tử trùng lặp. Tuy nhiên, mảng có thể chứa các phần tử trùng nhau.

**Constraints**

$1 \le n \le 10^5$

$1 \le m \le 10^5$

$1 \le \text{Số nguyên bất kỳ trong input} \le 10^9$

**Input Format**

Dòng đầu tiên chứa hai số nguyên $n$ và $m$ cách nhau bởi dấu cách.

Dòng thứ hai chứa $n$ số nguyên của mảng.

Dòng thứ ba và thứ tư lần lượt chứa $m$ số nguyên của tập hợp $A$ và $B$.

**Output Format**

In ra một số nguyên duy nhất là tổng chỉ số hạnh phúc cuối cùng.

**Sample Input**

```markdown
3 2
1 5 3
3 1
5 7
```

**Sample Output**

```markdown
1
```

**Explanation**

Bạn nhận được $1$ đơn vị hạnh phúc cho mỗi phần tử $3$ và $1$ thuộc tập hợp $A$. Bạn mất $1$ đơn vị cho phần tử $5$ thuộc tập hợp $B$. Phần tử $7$ trong tập $B$ không có trong mảng nên không được tính. 

Do đó, tổng hạnh phúc là $1 + 1 - 1 = 1$.

