"""
không thể kết hợp chuỗi và số như thế này:
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)

Nhưng có thể kết hợp chuỗi và số bằng cách sử dụng f-string hoặc format() method này!
"""

"""
Để chỉ định một chuỗi là f-string, chỉ cần đặt một dấu f ngoặc nhọn phía trước chuỗi ký tự và thêm dấu ngoặc nhọn {} làm chỗ giữ chỗ cho các biến và các phép toán khác.
"""
# Tạo một f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Thêm một chỗ giữ chỗ cho biến price:

price = 59
txt = f"The price is {price} dollars"
print(txt)

"""
Một phần giữ chỗ có thể bao gồm một bộ điều chỉnh để định dạng giá trị.

Một ký tự bổ trợ được thêm vào bằng cách thêm dấu hai chấm :theo sau là kiểu định dạng hợp lệ, ví dụ như .2fcó nghĩa là số thập phân cố định với 2 chữ số sau dấu phẩy:
"""
# Hiển thị giá với 2 chữ số thập phân:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Thực hiện phép toán trong biến giữ chỗ và trả về kết quả:

txt = f"The price is {20 * 59} dollars"
print(txt)