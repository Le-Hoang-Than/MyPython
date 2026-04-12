"""
Thay vì viết nhiều if..else câu, có thể sử dụng match.

Câu lệnh này matchchọn một trong nhiều khối mã để thực thi.

Cú pháp

match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
Cách thức hoạt động như sau:

Biểu thức match chỉ được đánh giá một lần.
Giá trị của biểu thức được so sánh với giá trị của từng biến case.
Nếu tìm thấy sự trùng khớp, khối mã tương ứng sẽ được thực thi.
"""

# sử dụng số thứ tự ngày trong tuần để in tên ngày trong tuần:
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

"""
Sử dụng ký tự gạch dưới _ làm giá trị trường hợp cuối cùng nếu bạn muốn khối mã được thực thi khi không có kết quả khớp nào khác:
"""
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
"""Giá trị _ sẽ luôn khớp, vì vậy điều quan trọng là phải đặt nó ở vị trí cuối cùng để nó hoạt động như một trường hợp mặc định ."""

"""
Sử dụng ký tự dấu gạch dọc | làm toán tử OR trong quá trình đánh giá trường hợp để kiểm tra xem có nhiều hơn một giá trị khớp trong cùng một trường hợp hay không :
"""
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

"""có thể thêm ifcác câu lệnh vào phần đánh giá trường hợp như một điều kiện kiểm tra bổ sung:"""
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")