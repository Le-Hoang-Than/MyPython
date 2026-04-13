import re

#
# [arn] Trả về kết quả khớp nếu một trong các ký tự (a, r, hoặc n) xuất hiện.
#
txt = "The rain in Spain"

# Kiểm tra xem chuỗi có bất kỳ ký tự 'a', 'r', hoặc 'n' nào không:
x = re.findall("[arn]", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# [a-n] Khớp với bất kỳ ký tự thường nào từ a đến n.
#
txt = "The rain in Spain"

# Kiểm tra xem chuỗi có bất kỳ ký tự nào nằm giữa 'a' và 'n' không:
x = re.findall("[a-n]", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# [^arn] Khớp với bất kỳ ký tự nào NGOẠI TRỪ a, r, và n.
#
txt = "The rain in Spain"

# Kiểm tra xem chuỗi có các ký tự khác ngoài 'a', 'r', hoặc 'n' không:
x = re.findall("[^arn]", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# [0123] Khớp với bất kỳ chữ số nào trong bộ {0, 1, 2, 3}.
#
txt = "The rain in Spain"

# Kiểm tra xem chuỗi có bất kỳ chữ số 0, 1, 2, hoặc 3 nào không:
x = re.findall("[0123]", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# [0-9] Khớp với bất kỳ chữ số nào từ 0 đến 9.
#
txt = "8 times before 11:45 AM"

# Kiểm tra xem chuỗi có bất kỳ chữ số nào không:
x = re.findall("[0-9]", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# [0-5][0-9] Khớp với các số có hai chữ số từ 00 đến 59.
#
txt = "8 times before 11:45 AM"

# Kiểm tra xem chuỗi có bất kỳ số có hai chữ số nào từ 00 đến 59 không:
x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# [a-zA-Z] Khớp với bất kỳ chữ cái nào (không phân biệt hoa thường).
#
txt = "8 times before 11:45 AM"

# Kiểm tra xem chuỗi có ký tự nào từ a-z (viết thường) và A-Z (viết hoa) không:
x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# [+] Trong ngoặc vuông, các ký tự đặc biệt mất đi ý nghĩa của chúng. [+] chỉ đơn giản là tìm ký tự cộng.
#
txt = "8 times before 11:45 AM"

# Kiểm tra xem chuỗi có bất kỳ ký tự '+' nào không:
x = re.findall("[+]", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")
