"""
Một Match Object là một đối tượng chứa thông tin về việc tìm kiếm và kết quả của việc tìm kiếm đó.
Lưu ý: Nếu không tìm thấy kết quả khớp nào, giá trị None sẽ được trả về thay vì Match Object.
Ví dụ: Thực hiện tìm kiếm để trả về một Match Object
"""
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) # Dòng này sẽ in ra một đối tượng (Match Object)

"""
Các Thuộc tính và Phương thức Match object có các thuộc tính và phương thức dùng để lấy thông tin về kết quả tìm kiếm:
.span()Trả về một tuple chứa vị trí bắt đầu và vị trí kết thúc của kết quả khớp.
.stringTrả về chuỗi đầu vào được truyền vào hàm.
.group()Trả về phần của chuỗi nơi tìm thấy kết quả khớp.
"""

# Sử dụng .span()In ra vị trí (bắt đầu và kết thúc) của lần xuất hiện khớp đầu tiên.
# Biểu thức chính quy tìm kiếm bất kỳ từ nào bắt đầu bằng chữ "S" viết hoa:


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) # Kết quả: (12, 17)
# Sử dụng .stringIn ra chuỗi gốc đã được truyền vào hàm:Pythonimport re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) # Kết quả: "The rain in Spain"
# Sử dụng .group()In ra phần của chuỗi nơi có kết quả khớp.
# Biểu thức chính quy tìm kiếm bất kỳ từ nào bắt đầu bằng chữ "S" viết hoa:Pythonimport re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) # Kết quả: "Spain"

"""Lưu ý quan trọngNếu không có kết quả khớp, biến x sẽ mang giá trị None. 
Khi đó, việc gọi các phương thức như .span() hay .group() sẽ gây ra lỗi AttributeError. 
Bạn nên kiểm tra trước khi sử dụng
"""

if x:
    print(x.group())
else:
    print("Không tìm thấy kết quả khớp")