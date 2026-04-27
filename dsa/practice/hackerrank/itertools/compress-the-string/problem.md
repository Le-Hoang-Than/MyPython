# Compress the String!

**Task**

Trong bài tập này, chúng tôi muốn bạn thấy được sự hữu ích của hàm groupby() trong thư viện itertools. Bạn có thể tìm hiểu thêm về hàm này tại tài liệu chính thức của Python.

Bạn được cho một chuỗi $S$. Giả sử một ký tự 'c' xuất hiện liên tiếp $n$ lần trong chuỗi. Hãy thay thế các lần xuất hiện liên tiếp này bằng cặp $(n, c)$ trong chuỗi kết quả.

Để hiểu rõ hơn về yêu cầu bài toán, hãy xem phần giải thích ví dụ bên dưới.

**Input Format**

Một dòng duy nhất chứa chuỗi $S$.

**Output Format**

Một dòng duy nhất chứa chuỗi đã được biến đổi (nén lại).

**Constraints**

Tất cả các ký tự trong $S$ đều là các chữ số nguyên nằm trong khoảng từ $0$ đến $9$.

**Sample Input**

```text
1222311
```

**Sample Output**

```text
(1, 1) (3, 2) (1, 3) (2, 1)
```

**Explanation**

Đầu tiên, ký tự 1 xuất hiện 1 lần. Nó được thay thế bằng (1, 1).

Tiếp theo, ký tự 2 xuất hiện 3 lần liên tiếp. Nó được thay thế bằng (3, 2).

Ký tự 3 xuất hiện 1 lần, thay bằng (1, 3).

Cuối cùng, ký tự 1 xuất hiện 2 lần liên tiếp, thay bằng (2, 1).

Lưu ý: Chú ý khoảng trắng đơn bên trong mỗi cặp ngoặc đơn và khoảng trắng giữa các cặp với nhau.
