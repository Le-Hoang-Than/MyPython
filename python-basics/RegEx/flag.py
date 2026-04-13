import re

"""
# re.ASCII  re.A   Chỉ trả về các kết quả khớp theo bảng mã ASCII.
#
"""
print("\n---")
txt = "Åland"

# Tìm tất cả các kết quả khớp ASCII:
print(re.findall(r"\w", txt, re.ASCII))

# Nếu không có flag này, ví dụ sẽ trả về tất cả các ký tự (bao gồm cả ký tự đặc biệt Å):
print(re.findall(r"\w", txt))

# Kết quả tương tự khi sử dụng flag viết tắt re.A:
print(re.findall(r"\w", txt, re.A))

"""
# re.DEBUG     Hiển thị thông tin gỡ lỗi (debug) về biểu thức đã biên dịch.
#
"""
print("\n---")
txt = "The rain in Spain"

# Sử dụng tìm kiếm không phân biệt hoa thường khi tìm kết quả khớp cho "Spain" trong văn bản:
# (Flag này sẽ in cấu trúc phân tích của biểu thức ra console)
print(re.findall("spain", txt, re.DEBUG))

"""
# re.DOTALL re.S   Cho phép ký tự . khớp với tất cả mọi ký tự (bao gồm cả ký tự xuống dòng \n).
#
"""
print("\n---")
txt = """Hi
my
name
is
Sally"""

# Tìm kiếm một chuỗi bắt đầu bằng "me", theo sau là một ký tự bất kỳ (kể cả ký tự xuống dòng), và tiếp tục với "is":
print(re.findall("me.is", txt, re.DOTALL))

# Ví dụ này sẽ không trả về kết quả nào nếu không có flag re.DOTALL:
print(re.findall("me.is", txt))

# Kết quả tương tự với flag viết tắt re.S:
print(re.findall("me.is", txt, re.S))

"""
# re.IGNORECASE re.I   Khớp kết quả không phân biệt chữ hoa và chữ thường.
#
"""
print("\n---")
txt = "The rain in Spain"

# Sử dụng tìm kiếm không phân biệt hoa thường khi tìm kiếm "spain" trong văn bản:
print(re.findall("spain", txt, re.IGNORECASE))

# Kết quả tương tự khi sử dụng flag viết tắt re.I:
print(re.findall("spain", txt, re.I))

"""
# re.MULTILINE  re.M   Chế độ đa dòng; giúp ^ và $ khớp tại điểm bắt đầu/kết thúc của MỖI DÒNG.
#
"""
print("\n---")
txt = """There
aint much
rain in 
Spain"""

# Tìm kiếm chuỗi "ain" ở vị trí đầu dòng:
print(re.findall("^ain", txt, re.MULTILINE))

# Ví dụ này sẽ không trả về kết quả nào nếu không có flag re.MULTILINE,
# vì ký tự ^ khi không có re.MULTILINE chỉ khớp tại điểm khởi đầu của toàn bộ văn bản:
print(re.findall("^ain", txt))

# Kết quả tương tự với flag viết tắt re.M:
print(re.findall("^ain", txt, re.M))

"""
# re.NOFLAG    Chỉ định rằng không có flag nào được thiết lập cho mẫu này.
#
"""
print("\n---")

"""
# re.UNICODE    re.U   Trả về các kết quả khớp theo chuẩn Unicode. (Mặc định từ Python 3).
#
"""
print("\n---")
txt = "Åland"

# Tìm tất cả các kết quả khớp UNICODE:
print(re.findall(r"\w", txt, re.UNICODE))

# Kết quả tương tự khi sử dụng flag viết tắt re.U:
print(re.findall(r"\w", txt, re.U))

"""
# re.VERBOSE    re.X   Cho phép thêm khoảng trắng và chú thích vào trong mẫu RegEx cho dễ đọc.
#
"""
print("\n---")
text = "The rain in Spain falls mainly on the plain"

# Tìm và trả về các từ có chứa cụm "ain":

pattern = """
[A-Za-z]* # bắt đầu với bất kỳ chữ cái nào
ain+      # chứa cụm 'ain'
[a-z]* # theo sau bởi bất kỳ chữ cái thường nào
"""

print(re.findall(pattern, text, re.VERBOSE))

# Ví dụ này sẽ không trả về gì nếu không có flag re.VERBOSE (vì nó sẽ coi khoảng trắng/chú thích là một phần của mẫu tìm kiếm)
print(re.findall(pattern, text))

# Kết quả tương tự với flag viết tắt re.X:
print(re.findall(pattern, text, re.X))
