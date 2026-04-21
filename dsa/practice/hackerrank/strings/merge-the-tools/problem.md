# Merge the Tools!

Cho các dữ kiện sau:
1. Một chuỗi $s$ có độ dài $n$ (trong đó $s = c_0c_1...c_{n-1}$).
2. Một số nguyên $k$, và $k$ là một ước số của $n$.

Chúng ta có thể chia $s$ thành $n/k$ chuỗi con, mỗi chuỗi con $t_i$ gồm một khối liên tiếp $k$ ký tự trong $s$. Sau đó, sử dụng mỗi $t_i$ để tạo ra chuỗi $u_i$ sao cho:
* Các ký tự trong $u_i$ là một dãy con của các ký tự trong $t_i$.
* Bất kỳ lần xuất hiện lặp lại nào của một ký tự đều bị loại bỏ khỏi chuỗi, sao cho mỗi ký tự trong $u_i$ chỉ xuất hiện đúng một lần. Nói cách khác, nếu một ký tự tại vị trí $j$ trong $t_i$ đã xuất hiện tại một vị trí trước đó $l < j$ trong $t_i$, thì không đưa ký tự đó vào chuỗi $u_i$.

Cho $s$ và $k$, hãy in ra $n/k$ dòng, trong đó mỗi dòng thứ $i$ biểu thị chuỗi $u_i$.

**Example**

$s = \text{'AAABCADDE'}$

$k = 3$

Có 3 chuỗi con độ dài $k=3$ cần xem xét: 'AAA', 'BCA' và 'DDE'.
1. Chuỗi con thứ nhất là 'AAA': tất cả là ký tự 'A', nên $u_1 = \text{'A'}$.
2. Chuỗi con thứ hai là 'BCA': tất cả các ký tự đều riêng biệt, nên $u_2 = \text{'BCA'}$.
3. Chuỗi con thứ ba là 'DDE': có hai ký tự khác nhau, nên $u_3 = \text{'DE'}$.

**Lưu ý:** Một dãy con phải giữ nguyên thứ tự xuất hiện ban đầu của các ký tự. Thứ tự các ký tự trong mỗi dãy con được hiển thị là rất quan trọng.

**Function Description**

Hoàn thành hàm `merge_the_tools` trong trình chỉnh sửa.

`merge_the_tools` có các tham số sau:
* **string s**: chuỗi cần phân tích.
* **int k**: kích thước của mỗi chuỗi con.

**Prints**

In mỗi dãy con $u_i$ trên một dòng mới. Sẽ có tổng cộng $n/k$ dòng. Hàm không cần giá trị trả về.

**Input Format**

Dòng đầu tiên chứa một chuỗi đơn, $s$.

Dòng thứ hai chứa một số nguyên, $k$, là độ dài của mỗi chuỗi con.

**Constraints**

* $1 \le n \le 10^4$ (trong đó $n$ là độ dài của $s$).
* $1 \le k \le n$.
* Đảm bảo rằng $n$ là bội số của $k$.

**Sample Input**

```markdown
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
```

**Sample Output**

```markdown
AB
CA
AD
```

**Explanation**

Chia $s$ thành $n/k = 9/3 = 3$ phần bằng nhau, mỗi phần có độ dài $k = 3$. Chuyển đổi mỗi $t_i$ thành $u_i$ bằng cách loại bỏ các lần xuất hiện lặp lại của các ký tự:
1. $t_0 = \text{'AAB'}$ $\rightarrow$ $u_0 = \text{'AB'}$
2. $t_1 = \text{'CAA'}$ $\rightarrow$ $u_1 = \text{'CA'}$
3. $t_2 = \text{'ADA'}$ $\rightarrow$ $u_2 = \text{'AD'}$

In mỗi $u_i$ trên một dòng mới.