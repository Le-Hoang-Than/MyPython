# Write a function

Một ngày dư được thêm vào lịch gần như bốn năm một lần vào ngày 29
tháng 2, và ngày đó được gọi là ngày nhuận. Việc này giúp điều chỉnh
lịch cho phù hợp với thực tế là hành tinh của chúng ta mất khoảng
365,25 ngày để quay quanh Mặt Trời. Một năm nhuận là năm có chứa
một ngày nhuận.

Trong lịch Gregorian (Dương lịch), ba điều kiện sau được sử dụng để
xác định năm nhuận:

- Năm đó chia hết cho 4 là năm nhuận, NGOẠI TRỪ:

    - Nếu năm đó chia hết cho 100, thì đó KHÔNG phải là năm nhuận, TRỪ KHI:

        - Năm đó cũng chia hết cho 400. Khi đó, nó lại là một năm nhuận.

Điều này có nghĩa là trong lịch Gregorian, các năm 2000 và 2400 là
năm nhuận, trong khi các năm 1800, 1900, 2100, 2200, 2300 và 2500
KHÔNG phải là năm nhuận.

**Task**

Cho một năm, hãy xác định xem đó có phải là năm nhuận hay không. 
Nếu là năm nhuận, trả về giá trị Boolean `True`, 
ngược lại trả về `False`.

Lưu ý rằng đoạn mã mẫu cung cấp sẵn việc đọc dữ liệu từ STDIN và 
truyền đối số vào hàm `is_leap`. Bạn chỉ cần hoàn thành nội dung 
bên trong hàm `is_leap`.

**Input Format**

Đọc vào giá trị year, là năm cần kiểm tra.

**Constraints**

$1900 \le \text{year} \le 10^5$

**Output Format**

Hàm phải trả về một giá trị Boolean (True hoặc False). 
Việc in kết quả ra màn hình do đoạn mã có sẵn xử lý.

**Sample Input 0**
```markdown
1990
```
**Sample Output 0**
```markdown
False
```
**Explanation 0**

1990 không phải là bội số của 4 nên không phải là năm nhuận.