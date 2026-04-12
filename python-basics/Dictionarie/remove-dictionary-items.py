# Phương thức này pop()xóa mục có tên khóa được chỉ định:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

"""
Phương thức popitem()xóa mục được chèn cuối cùng (trong các phiên bản trước 3.7, một mục ngẫu nhiên sẽ bị xóa thay thế):
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# Từ khóa del xóa mục có tên khóa được chỉ định:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# Từ khóa del cũng có thể xóa hoàn toàn từ điển:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

# Phương thức này clear()xóa sạch từ điển:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
