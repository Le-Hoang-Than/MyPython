"""
Mô-đun re cung cấp một tập hợp các chức năng cho phép chúng ta tìm kiếm sự trùng khớp trong một chuỗi ký tự:
"""
import re

"""
Hàm findall() trả về một danh sách chứa tất cả các kết quả phù hợp.
"""
# In ra danh sách tất cả các kết quả phù hợp:

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# Nếu không tìm thấy kết quả phù hợp, một danh sách rỗng sẽ được trả về:
x = re.findall("Portugal", txt)
print(x)

"""
Hàm search() tìm kiếm sự trùng khớp trong chuỗi và trả về một đối tượng Match nếu tìm thấy sự trùng khớp.
Nếu có nhiều hơn một kết quả trùng khớp, chỉ kết quả trùng khớp đầu tiên sẽ được trả về
"""

# Tìm ký tự khoảng trắng đầu tiên trong chuỗi:
txt = "The rain in Spain"
x = re.search("\\s", txt)

print("The first white-space character is located in position:", x.start())

# Nếu không tìm thấy kết quả phù hợp, giá trị Nonesẽ được trả về:
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

"""
Hàm split() trả về một danh sách trong đó chuỗi đã được tách ra tại mỗi điểm khớp:
"""
# Tách chuỗi tại mỗi ký tự khoảng trắng:

txt = "The rain in Spain"
x = re.split("\\s", txt)
print(x)

"""
có thể kiểm soát số lần xuất hiện bằng cách chỉ định tham số maxsplit:
"""
# Chỉ tách chuỗi tại vị trí xuất hiện đầu tiên:

txt = "The rain in Spain"
x = re.split("\\s", txt, 1)
print(x)

"""
Hàm sub() sẽ thay thế các kết quả khớp bằng văn bản đã chọn:
"""
# Thay thế mọi ký tự khoảng trắng bằng số 9
txt = "The rain in Spain"
x = re.sub("\\s", "9", txt)
print(x)

"""
có thể kiểm soát số lần thay thế bằng cách chỉ định count tham số:
"""
# Thay thế 2 lần xuất hiện đầu tiên:
txt = "The rain in Spain"
x = re.sub("\\s", "9", txt, 2)
print(x)



