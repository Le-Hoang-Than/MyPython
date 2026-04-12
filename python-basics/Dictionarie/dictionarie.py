"""
Dictionary được sử dụng để lưu trữ các giá trị dữ liệu dưới dạng cặp key:value.

Dictionarie là một tập hợp được sắp xếp*, có thể thay đổi và không cho phép trùng lặp.
"""
# Tạo và in từ điển:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

"""
Các mục trong dictionary được sắp xếp theo thứ tự, có thể thay đổi và không cho phép trùng lặp.

Các mục trong dictionary được trình bày dưới dạng cặp key:value và có thể được tham chiếu bằng cách sử dụng key name.
"""
# In ra giá trị "brand" của dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

"""
Khi nói rằng từ điển được sắp xếp, điều đó có nghĩa là các mục trong từ điển có một thứ tự xác định và thứ tự đó sẽ không thay đổi.

"Không có thứ tự" nghĩa là các mục không có thứ tự xác định, không thể tham chiếu đến một mục bằng cách sử dụng chỉ mục.

Từ điển có thể thay đổi được, nghĩa là có thể thay đổi, thêm hoặc xóa các mục sau khi từ điển đã được tạo.

Từ điển không thể có hai mục có cùng khóa:
"""

# Các giá trị trùng lặp sẽ ghi đè lên các giá trị hiện có:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# In ra số lượng mục trong từ điển:

print(len(thisdict))

# Các kiểu dữ liệu chuỗi, số nguyên, boolean và danh sách:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Sử dụng phương thức dict() để tạo một từ điển:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)