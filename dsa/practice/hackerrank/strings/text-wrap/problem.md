# Text Wrap

Bạn được cho một chuỗi ký tự $S$ và độ rộng $w$.

Nhiệm vụ của bạn là ngắt chuỗi đó thành một đoạn văn có độ rộng bằng $w$.

**Function Description**

Hãy hoàn thành hàm `wrap` trong trình soạn thảo dưới đây.

Hàm `wrap` có các tham số sau:

- string string: một chuỗi ký tự dài.
- int max_width: độ rộng tối đa để ngắt dòng.

**Returns**

- string: một chuỗi duy nhất chứa các ký tự xuống dòng (\n) tại những vị trí cần ngắt.

**Input Format**

Dòng thứ nhất chứa chuỗi ký tự $S$.

Dòng thứ hai chứa độ rộng $w$.

**Constraints**

- $0 < \text{len}(string) < 1000$
- $0 < \text{max width} < \text{len}(string)$

**Sample Input 0**

```markdown
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
```

**Sample Output 0**

```markdown
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
```