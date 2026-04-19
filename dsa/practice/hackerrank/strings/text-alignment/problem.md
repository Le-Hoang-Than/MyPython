# Text Alignment

Trong Python, một chuỗi văn bản có thể được căn lề **trái (left)**, **phải (right)** và **giữa (center)**.

**.ljust(width)**

Phương thức này trả về một chuỗi căn lề trái với độ dài bằng `width`.
```markdown
>>> width = 20
>>> print('HackerRank'.ljust(width,'-'))
HackerRank----------
```

**.center(width)**

Phương thức này trả về một chuỗi căn lề giữa với độ dài bằng width.

```markdown
>>> width = 20
>>> print('HackerRank'.center(width,'-'))
-----HackerRank-----
```

**.rjust(width)**

Phương thức này trả về một chuỗi căn lề phải với độ dài bằng width.

```markdown
>>> width = 20
>>> print('HackerRank'.rjust(width,'-'))
----------HackerRank
```

**Task**

Bạn được cung cấp một phần mã nguồn (partial code) dùng để tạo ra Logo HackerRank với độ dày (thickness) có thể thay đổi.

Nhiệm vụ của bạn là thay thế các khoảng trống (______) bằng các phương thức rjust, ljust hoặc center.

**Input Format**

Một dòng duy nhất chứa giá trị thickness (độ dày) của logo.

**Constraints**

- thickness phải là một số lẻ.
- $0 < \text{thickness} < 50$

**Output Format**

In ra logo theo mẫu yêu cầu.

**Sample Input**

```markdown
5
```

**Sample Output**

```markdown
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H
```