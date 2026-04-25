# Power - Mod Power

Cho đến nay, chúng ta mới chỉ nghe nói về sức mạnh của Python. Bây giờ, chúng ta sẽ thực sự chứng kiến chúng!

Lũy thừa (số mũ) trong Python có thể được tính toán bằng hàm tích hợp sẵn hoặc toán tử. Bạn có thể gọi hàm lũy thừa như sau:

```markdown
>>> pow(a,b)
```

hoặc

```markdown
>>> a**b
```

Ngoài ra, Python còn cho phép tính lũy thừa kết hợp với phép chia lấy dư: $a^b \pmod m$

```markdown
>>> pow(a,b,m)
```

Điều này cực kỳ hữu ích trong các phép toán cần in ra kết quả sau khi thực hiện % mod.

**Lưu ý:**

- Ở đây, $a$ và $b$ có thể là số thực hoặc số âm. Tuy nhiên, nếu có đối số thứ ba ($m$), thì $b$ không được là số âm.
- Python có một module math cũng sở hữu hàm pow(). Hàm math.pow() này nhận hai đối số và luôn trả về một số thực (float). Tuy nhiên, người ta rất ít khi sử dụng math.pow().

**Task**

Bạn được cho ba số nguyên: $a$, $b$, và $m$. Hãy in ra hai dòng:

Dòng thứ nhất in ra kết quả của pow(a, b).

Dòng thứ hai in ra kết quả của pow(a, b, m).

**Input Format**

Dòng đầu tiên chứa $a$.

Dòng thứ hai chứa $b$.

Dòng thứ ba chứa $m$.

**Constraints**

$1 \le a \le 10$

$1 \le b \le 10$

$2 \le m \le 1000$

**Sample Input**

```markdown
3
4
5
```

**Sample Output**

```markdown
81
1
```