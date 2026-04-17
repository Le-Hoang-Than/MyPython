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

# =====================================
# String format() Method
# =====================================

# Định nghĩa và cách sử dụng
'''
Phương thức format() định dạng giá trị được chỉ định và chèn chúng vào bên trong phần giữ chỗ của chuỗi.

Phần giữ chỗ được định nghĩa bằng dấu ngoặc nhọn: {}.

Phương thức format() trả về chuỗi đã được định dạng.
'''

# Cú pháp
'''string.format(value1, value2...)'''
'''
Bắt buộc. Một hoặc nhiều giá trị cần được định dạng và chèn vào chuỗi.

Các giá trị có thể là một danh sách các giá trị được phân tách bằng dấu phẩy, một danh sách cặp khóa-giá trị, hoặc sự kết hợp của cả hai.

Các giá trị có thể thuộc bất kỳ kiểu dữ liệu nào.
'''

# Các phần giữ chỗ
'''
Các phần giữ chỗ có thể được xác định bằng cách sử dụng chỉ mục được đặt tên {price}, chỉ mục được đánh số {0}hoặc thậm chí là các phần giữ chỗ trống {}.
'''

txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)

'''
# Căn lề (Alignment)	
'''
# :<	Căn lề trái kết quả (trong khoảng trống khả dụng).
# Để minh họa, chúng ta chèn số 8 để thiết lập không gian trống cho giá trị là 8 ký tự.
# Sử dụng "<" để căn chỉnh giá trị sang trái.
txt = "We have {:<8} chickens."
print(txt.format(49))

# :>	Căn lề phải kết quả (trong khoảng trống khả dụng).
# Để minh họa, chúng ta chèn số 8 để thiết lập không gian trống cho giá trị là 8 ký tự.
# Sử dụng ">" để căn chỉnh giá trị sang phải.
txt = "We have {:>8} chickens."
print(txt.format(49))

# :^	Căn giữa kết quả (trong khoảng trống khả dụng).
# Để minh họa, chúng ta chèn số 8 để thiết lập không gian trống cho giá trị là 8 ký tự.
# Sử dụng ký tự "^" để căn giữa giá trị.

txt = "We have {:^8} chickens."
print(txt.format(49))

'''
# Dấu (Signs)	
'''

# :=	Đặt dấu (âm/dương) ở vị trí ngoài cùng bên trái.
# Để minh họa, chúng ta chèn số 8 để chỉ định không gian trống dành cho giá trị.
# Sử dụng "=" để đặt dấu cộng/trừ ở vị trí ngoài cùng bên trái.
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

# :+	Sử dụng dấu cộng để hiển thị cả số dương và số âm.
# Sử dụng dấu "+" để luôn chỉ ra số đó là dương hay âm.
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

# :-	Chỉ sử dụng dấu trừ cho các giá trị âm (mặc định).
# Sử dụng dấu "-" để luôn chỉ ra nếu số đó là số âm (số dương được hiển thị mà không có dấu).
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

# :	Thêm một khoảng trắng trước số dương (và dấu trừ trước số âm).
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))

'''
# Dấu phân cách (Separators)	
'''

# :,	Sử dụng dấu phẩy làm dấu phân cách hàng nghìn.
txt = "The universe is {:,} years old."
print(txt.format(13800000000))

# :_	Sử dụng dấu gạch dưới làm dấu phân cách hàng nghìn.
txt = "The universe is {:_} years old."
print(txt.format(13800000000))

'''
# Hệ cơ số (Number Bases)	
'''

# :b	Định dạng hệ Nhị phân (Binary).
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

# :d	Định dạng hệ Thập phân (Decimal).
txt = "We have {:d} chickens."
print(txt.format(0b101))

# :o	Định dạng hệ Bát phân (Octal).
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))

# :x	Định dạng hệ Thập lục phân (Hex), viết thường.
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))

# :X	Định dạng hệ Thập lục phân (Hex), viết hoa.
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))

'''
# Số thực & Khoa học (Floating Point)	
'''
# :e	Định dạng Số mũ/Khoa học (chữ "e" thường).
txt = "We have {:e} chickens."
print(txt.format(5))

# :E	Định dạng Số mũ/Khoa học (chữ "E" hoa).
txt = "We have {:E} chickens."
print(txt.format(5))

# :f	Định dạng Số thực dấu phẩy tĩnh (Fix point).
# Sử dụng phím "f" để chuyển đổi một số thành số thập phân cố định, mặc định là 6 chữ số thập phân, nhưng hãy sử dụng dấu chấm theo sau là một số để chỉ định số chữ số thập phân
txt = "The price is {:.2f} dollars."
print(txt.format(45))
# Nếu không có ".2" bên trong phần giữ chỗ, số này sẽ được hiển thị như sau:
txt = "The price is {:f} dollars."
print(txt.format(45))

# :F	Định dạng Số thực dấu phẩy tĩnh (viết hoa INF và NAN).
# Sử dụng phím "F" để chuyển đổi một số thành số thập phân cố định, nhưng hiển thị inf và nan dưới dạng INF và NAN.
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))
# Ví dụ tương tự, nhưng với chữ f viết thường.
txt = "The price is {:f} dollars."
print(txt.format(x))

# :g	Định dạng chung (General format).

# :G	Định dạng chung (sử dụng E hoa cho ký hiệu khoa học).

'''
# Khác	
'''

# :c	Chuyển đổi giá trị thành ký tự Unicode tương ứng.

# :n	Định dạng số (tùy theo ngôn ngữ hệ thống).

# :%	Định dạng Phần trăm (Percentage).
txt = "You scored {:%}"
print(txt.format(0.25))
# Hoặc, không có số thập phân
txt = "You scored {:.0%}"
print(txt.format(0.25))