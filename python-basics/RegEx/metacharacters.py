"""
Metacharacters là những ký tự có ý nghĩa đặc biệt
"""
import re

# Một tập hợp các ký tự.
txt = "The rain in Spain"
# Tìm tất cả các ký tự viết thường nằm trong khoảng từ "a" đến "m":
x = re.findall("[a-m]", txt)
print(x)

# Báo hiệu một chuỗi đặc biệt (cũng dùng để "thoát" các ký tự đặc biệt).
txt = "That will be 59 dollars"
# Tìm tất cả các ký tự là chữ số:
x = re.findall(r"\d", txt)
print(x)

# Bất kỳ ký tự nào (ngoại trừ ký tự dòng mới).
txt = "hello planet"
# Tìm kiếm một chuỗi bắt đầu bằng "he", theo sau là hai ký tự (bất kỳ) và kết thúc bằng "o":
x = re.findall("he..o", txt)
print(x)

# Bắt đầu với...
txt = "hello planet"
# Kiểm tra xem chuỗi có bắt đầu bằng 'hello' hay không:
x = re.findall("^hello", txt)
if x:
    print("Có, chuỗi bắt đầu bằng 'hello'")
else:
    print("Không tìm thấy kết quả khớp")

# Kết thúc với...
txt = "hello planet"
# Kiểm tra xem chuỗi có kết thúc bằng 'planet' hay không:
x = re.findall("planet$", txt)
if x:
    print("Có, chuỗi kết thúc bằng 'planet'")
else:
    print("Không tìm thấy kết quả khớp")

# Xuất hiện 0 hoặc nhiều lần.
txt = "hello planet"
# Tìm kiếm một chuỗi bắt đầu bằng "he", theo sau là 0 hoặc nhiều ký tự (bất kỳ) và kết thúc bằng "o":
x = re.findall("he.*o", txt)
print(x)

# Xuất hiện 1 hoặc nhiều lần.
txt = "hello planet"
# Tìm kiếm một chuỗi bắt đầu bằng "he", theo sau là 1 hoặc nhiều ký tự (bất kỳ) và kết thúc bằng "o":
x = re.findall("he.+o", txt)
print(x)

# Xuất hiện 0 hoặc 1 lần.
txt = "hello planet"
# Tìm kiếm một chuỗi bắt đầu bằng "he", theo sau là 0 hoặc 1 ký tự (bất kỳ) và kết thúc bằng "o":
x = re.findall("he.?o", txt)
print(x)
# Lần này chúng ta không tìm thấy kết quả khớp, vì giữa "he" và "o" không phải là 0 hay 1 ký tự, mà là 2 ký tự.

# Xuất hiện chính xác số lần được chỉ định.
txt = "hello planet"
# Tìm kiếm một chuỗi bắt đầu bằng "he", theo sau chính xác 2 ký tự (bất kỳ) và kết thúc bằng "o":
x = re.findall("he.{2}o", txt)
print(x)

# Hoặc (Phép toán logic OR).
txt = "The rain in Spain falls mainly in the plain!"
# Kiểm tra xem chuỗi có chứa "falls" hoặc "stays" hay không:
x = re.findall("falls|stays", txt)
print(x)
if x:
    print("Có, ít nhất một kết quả khớp đã được tìm thấy!")
else:
    print("Không tìm thấy kết quả khớp")