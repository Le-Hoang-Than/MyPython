"""
Biểu thức chính quy (RegEx) là một chuỗi ký tự tạo thành mẫu tìm kiếm.

Biểu thức chính quy (RegEx) có thể được sử dụng để kiểm tra xem một chuỗi có chứa mẫu tìm kiếm được chỉ định hay không.
"""

"""
Python có một gói tích hợp sẵn gọi là `<RegularExpression>` re, có thể được sử dụng để làm việc với Biểu thức chính quy.
"""
import re

# tìm trong chuỗi ký tự xem nó có bắt đầu bằng "The" và kết thúc bằng "Spain" hay không

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")


