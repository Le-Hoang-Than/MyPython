import re

#
#\A    Trả về kết quả khớp nếu các ký tự được chỉ định nằm ở đầu chuỗi.
#

txt = "The rain in Spain"

# Kiểm tra xem chuỗi có bắt đầu bằng "The" hay không:

x = re.findall(r"\AThe", txt)

print(x)

if x:
    print("Có, tìm thấy kết quả khớp!")
else:
    print("Không tìm thấy")

#
#\b    Trả về kết quả khớp nếu các ký tự nằm ở đầu hoặc cuối của một từ.
#
txt = "The rain in Spain"

# Kiểm tra xem "ain" có xuất hiện ở ĐẦU một TỪ hay không:

x = re.findall(r"\bain", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#Ký tự "r" ở đầu đảm bảo chuỗi được xử lý như một 'raw string' (chuỗi thô)#
txt = "The rain in Spain"

# Kiểm tra xem "ain" có xuất hiện ở CUỐI một TỪ hay không:

x = re.findall(r"ain\b", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")
#
#\B    Trả về kết quả khớp nếu các ký tự có mặt, nhưng KHÔNG ở đầu hoặc cuối từ.
#

txt = "The rain in Spain"

# Kiểm tra xem "ain" có xuất hiện nhưng KHÔNG ở đầu của một từ:

x = re.findall(r"\Bain", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#Ký tự "r" ở đầu đảm bảo chuỗi được xử lý như một 'raw string'#
txt = "The rain in Spain"

# Kiểm tra xem "ain" có xuất hiện nhưng KHÔNG ở cuối của một từ:

x = re.findall(r"ain\B", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# \d   Trả về kết quả khớp khi chuỗi có chứa chữ số (0-9).
#
txt = "The rain in Spain"

# Kiểm tra xem chuỗi có chứa bất kỳ chữ số nào không (số từ 0-9):

x = re.findall(r"\d", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# \D   Trả về kết quả khớp khi chuỗi KHÔNG chứa chữ số.
#
txt = "The rain in Spain"

# Trả về kết quả khớp tại mọi ký tự KHÔNG phải là chữ số:

x = re.findall(r"\D", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# \s   Trả về kết quả khớp khi chuỗi có chứa ký tự khoảng trắng.
#
txt = "The rain in Spain"

# Trả về kết quả khớp tại mỗi ký tự khoảng trắng:

x = re.findall(r"\s", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# \S   Trả về kết quả khớp khi chuỗi KHÔNG chứa ký tự khoảng trắng.
#
txt = "The rain in Spain"

# Trả về kết quả khớp tại mỗi ký tự KHÔNG phải là khoảng trắng:

x = re.findall(r"\S", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# \w   Trả về kết quả khớp khi chuỗi chứa ký tự chữ, số hoặc gạch dưới.
#
txt = "The rain in Spain"

# Trả về kết quả khớp tại mỗi ký tự từ (các ký tự từ a đến Z, chữ số từ 0-9, và dấu gạch dưới _):

x = re.findall(r"\w", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# \W   Trả về kết quả khớp khi chuỗi KHÔNG chứa ký tự chữ, số, gạch dưới.
#
txt = "The rain in Spain"

# Trả về kết quả khớp tại mỗi ký tự KHÔNG phải là ký tự từ (các ký tự KHÔNG nằm trong khoảng a-Z, ví dụ: "!", "?" hay khoảng trắng...):

x = re.findall(r"\W", txt)

print(x)

if x:
    print("Có, tìm thấy ít nhất một kết quả khớp!")
else:
    print("Không tìm thấy")

#
# \Z   Trả về kết quả khớp nếu các ký tự được chỉ định nằm ở cuối chuỗi.
#
txt = "The rain in Spain"

# Kiểm tra xem chuỗi có kết thúc bằng "Spain" hay không:

x = re.findall(r"Spain\Z", txt)

print(x)

if x:
    print("Có, tìm thấy kết quả khớp!")
else:
    print("Không tìm thấy")