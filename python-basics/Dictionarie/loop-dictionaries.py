"""
có thể duyệt qua một từ điển bằng cách sử dụng forvòng lặp.

Khi lặp qua một từ điển, giá trị trả về là các khóa của từ điển, nhưng cũng có các phương thức để trả về các giá trị .
"""

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}

# In ra tất cả các tên khóa trong từ điển, từng cái một:

for x in thisdict:
  print(x)

# có thể sử dụng keys()phương thức này để trả về các khóa của một từ điển:

for x in thisdict.keys():
  print(x)

# Lặp qua cả khóa và giá trị bằng cách sử dụng items()phương thức:

for x, y in thisdict.items():
  print(x, y)