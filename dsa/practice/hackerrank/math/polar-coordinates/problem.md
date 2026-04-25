# Polar Coordinates

Tọa độ cực là một cách thay thế để biểu diễn tọa độ Cartesian hoặc số phức.

Một số phức $z = x + iy$ được xác định hoàn toàn bởi phần thực $x$ và phần ảo $y$. Trong đó, $i$ là đơn vị ảo. Một tọa độ cực $(r, \varphi)$ được xác định hoàn toàn bởi mô-đun $r$ và góc pha $\varphi$.

![](https://s3.amazonaws.com/hr-challenge-images/9951/1440141121-5b051fd241-Capture.PNG)

Nếu chúng ta chuyển đổi số phức $z$ sang tọa độ cực, ta có:

- $r$: Khoảng cách từ $z$ đến gốc tọa độ, tức là $r = |z| = \sqrt{x^2 + y^2}$
- $\varphi$: Góc đo ngược chiều kim đồng hồ từ trục $x$ dương đến đoạn thẳng nối $z$ với gốc tọa độ.

Module cmath của Python cung cấp các hàm toán học cho số phức:

$cmath.phase$

Trả về pha của số phức $z$ (còn được gọi là đối số - argument của $z$).

```markdown
>>> phase(complex(-1.0, 0.0))
3.1415926535897931
```

$abs$

Trả về mô-đun (giá trị tuyệt đối) của số phức $z$.

```markdown
>>> abs(complex(-1.0, 0.0))
1.0
```

**Task**

Cho một số phức $z$. Nhiệm vụ của bạn là chuyển đổi nó sang tọa độ cực.

**Input Format**

Một dòng duy nhất chứa số phức $z$.

Lưu ý: Có thể sử dụng hàm complex() trong Python để chuyển đổi đầu vào thành một số phức.

**Constraints**

Số đã cho là một số phức hợp lệ.

**Output Format**

Xuất ra hai dòng:

Dòng đầu tiên chứa giá trị của $r$.

Dòng thứ hai chứa giá trị của $\varphi$.

**Sample Input**

```markdown
1+2j
```

**Sample Output**

```markdown
 2.23606797749979 
 1.1071487177940904
```

`Lưu ý: Kết quả đầu ra cần chính xác đến ít nhất 3 chữ số thập phân`