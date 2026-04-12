"""
Khối lệnh try cho phép bạn kiểm tra lỗi trong một khối mã.

Khối lệnh except cho phép bạn xử lý lỗi.

Khối lệnh else cho phép bạn thực thi mã khi không có lỗi xảy ra.

Khối lệnh finally cho phép bạn thực thi mã, bất kể kết quả của các khối try và except.
"""

"""
Khi xảy ra lỗi, hay còn gọi là ngoại lệ, Python thường sẽ dừng lại và tạo ra thông báo lỗi.

Các trường hợp ngoại lệ này có thể được xử lý bằng trycâu lệnh:
"""

# Khối lệnh này trysẽ tạo ra một ngoại lệ vì xnó chưa được định nghĩa:

try:
  print(x)
except:
  print("An exception occurred")
"""Vì khối try gây ra lỗi, khối except sẽ được thực thi.

Nếu không có khối try, chương trình sẽ bị lỗi và báo lỗi
"""

"""có thể định nghĩa bao nhiêu khối xử lý ngoại lệ tùy thích, ví dụ: nếu bạn muốn thực thi một khối mã đặc biệt cho một loại lỗi đặc biệt:"""

# In ra một thông báo nếu khối try gây ra lỗi NameError và một thông báo khác cho các lỗi khác:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

"""
có thể sử dụng từ khóa else này để định nghĩa một khối mã sẽ được thực thi nếu không có lỗi nào xảy ra:
"""
# Trong ví dụ này, trykhối lệnh không tạo ra bất kỳ lỗi nào:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

"""
Nếu được chỉ định, khối lệnh finally sẽ được thực thi bất kể khối try có gây ra lỗi hay không.
"""
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

"""
có thể chọn ném ra một ngoại lệ nếu một điều kiện nào đó xảy ra.

Để ném (hoặc tạo ra) một ngoại lệ, hãy sử dụng từ khóaraise.
"""

# Báo lỗi và dừng chương trình nếu x nhỏ hơn 0:

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
"""
có thể xác định loại lỗi cần báo cáo và văn bản cần hiển thị cho người dùng.
"""
# Ném ngoại lệ TypeError nếu x không phải là số nguyên:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")