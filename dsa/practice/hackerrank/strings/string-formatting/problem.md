# String Formatting

Cho một số nguyên $n$, hãy in ra các giá trị sau cho mỗi số nguyên $i$ chạy từ $1$ đến $n$:
1. Thập phân (Decimal)
2. Bát phân (Octal)
2. Thập lục phân (Hexadecimal - viết hoa)
3. Nhị phân (Binary)

**Function Description**

Hãy hoàn thành hàm print_formatted trong trình soạn thảo. 

print_formatted có tham số sau:
- int number: Giá trị tối đa cần in ($n$).

**Prints**

Bốn giá trị trên phải được in trên cùng một dòng theo đúng thứ tự nêu trên cho mỗi số từ $1$ đến $n$. Mỗi giá trị phải được đệm khoảng trắng (space-padded) sao cho độ rộng của nó khớp với độ rộng của giá trị nhị phân của số $n$.Các giá trị trên cùng một dòng được phân tách với nhau bằng một khoảng trắng đơn.

**Input Format**

Một số nguyên duy nhất biểu thị giá trị $n$.

**Constraints**

$1 \le n \le 99$

**Sample Input**

```markdown
17
```

**Sample Output**
```markdown
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
```