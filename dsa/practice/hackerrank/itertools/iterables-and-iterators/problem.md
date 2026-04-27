# Iterables and Iterators

Module itertools chuẩn hóa một bộ các công cụ cốt lõi có tốc độ nhanh và hiệu quả về bộ nhớ, hữu ích khi sử dụng riêng lẻ hoặc kết hợp với nhau. Cùng với nhau, chúng tạo thành một "đại số trình lặp" giúp việc xây dựng các công cụ chuyên biệt trở nên ngắn gọn và hiệu quả bằng ngôn ngữ Python thuần túy.

Để đọc thêm về các hàm trong module này, hãy xem tài liệu hướng dẫn của chúng tại đây.

Bạn được cho một danh sách gồm $N$ chữ cái tiếng Anh viết thường. Với một số nguyên $K$ cho trước, bạn có thể chọn ra $K$ chỉ số bất kỳ (giả sử chỉ số bắt đầu từ 1) với xác suất đồng đều từ danh sách.

Hãy tìm xác suất để ít nhất một trong $K$ chỉ số được chọn chứa chữ cái: 'a'.

**Input Format**

Đầu vào gồm ba dòng:
- Dòng đầu tiên chứa số nguyên $N$, biểu thị độ dài của danh sách.
- Dòng tiếp theo chứa $N$ chữ cái tiếng Anh viết thường cách nhau bởi dấu cách, biểu thị các phần tử của danh sách.
- Dòng thứ ba và cũng là dòng cuối cùng chứa số nguyên $K$, biểu thị số lượng chỉ số cần chọn.

**Output Format**

In ra một dòng duy nhất chứa xác suất để ít nhất một trong $K$ chỉ số được chọn chứa chữ cái: 'a'.

Lưu ý: Kết quả phải chính xác đến 3 chữ số thập phân.

**Constraints**

$1 \le N \le 10$

$1 \le K \le N$

Tất cả các chữ cái trong danh sách đều là chữ cái tiếng Anh viết thường.

**Sample Input**

```text
4 
a a c d
2
```

**Sample Output**

```text
0.8333
```

**Explanation**

Tất cả các bộ (tuples) không thứ tự có độ dài 2 gồm các chỉ số từ 1 đến 4 là:

$(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)$.

Trong số 6 tổ hợp này, có 5 tổ hợp chứa chỉ số 1 hoặc chỉ số 2 (là các chỉ số chứa chữ cái 'a').

Vì vậy, đáp án là $5/6 = 0.8333$.