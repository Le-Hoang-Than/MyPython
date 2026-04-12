"""có thể truy cập các mục trong từ điển bằng cách tham chiếu đến tên khóa của nó, nằm trong dấu ngoặc vuông:"""
# Lấy giá trị của khóa "model":

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# Ngoài ra còn có một phương pháp khác get()cũng cho kết quả tương tự:
x = thisdict.get("model")
print(x)

# Phương thức keys()sẽ trả về một danh sách tất cả các khóa trong từ điển.
x = thisdict.keys()
print(x)

"""
Danh sách các khóa là một dạng hiển thị của từ điển, có nghĩa là bất kỳ thay đổi nào được thực hiện đối với từ điển sẽ được phản ánh trong danh sách các khóa.
"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

# Phương thức values()sẽ trả về một danh sách tất cả các giá trị trong từ điển.
x = thisdict.values()
print(x)
"""
Danh sách các giá trị là một dạng hiển thị của từ điển, có nghĩa là bất kỳ thay đổi nào được thực hiện đối với từ điển sẽ được phản ánh trong danh sách các giá trị.
"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# Phương thức items()sẽ trả về từng mục trong từ điển dưới dạng các tuple trong một list.
x = thisdict.items()
print(x)

"""
Danh sách trả về là một dạng hiển thị các mục của từ điển, có nghĩa là bất kỳ thay đổi nào được thực hiện đối với từ điển sẽ được phản ánh trong danh sách các mục.
"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# Kiểm tra xem từ "model" có tồn tại trong từ điển hay không:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
