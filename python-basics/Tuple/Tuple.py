"""
Bộ dữ liệu được sử dụng để lưu trữ nhiều mục trong một biến.
Tuple là một trong 4 kiểu dữ liệu tích hợp trong Python được sử dụng để lưu trữ các bộ sưu tập dữ liệu
Tuple là một collection được sắp xếp và không thay đổi.
Tuple được viết bằng dấu ngoặc tròn.
"""

# Tạo một bộ dữ liệu:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""
Các mục trong bộ dữ liệu được sắp xếp theo thứ tự, không thể thay đổi và cho phép các giá trị trùng lặp.
Tuple items được index, item đầu tiên có index [0], mục thứ hai có chỉ mục [1] v.v.
"""

"""
bộ dữ liệu được sắp xếp theo thứ tự, điều đó có nghĩa là các mục có 
thứ tự xác định và thứ tự đó sẽ không thay đổi.
"""

"""
không thể thay đổi, thêm hoặc xóa các mục sau khi bộ dữ liệu đã được tạo.
"""

# Vì các bộ dữ liệu được lập chỉ mục, chúng có thể có các mục có cùng giá tr:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# In số lượng mục trong bộ:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Để tạo một bộ dữ liệu chỉ có một mục, bạn phải thêm dấu phẩy sau mục đó,
# nếu không Python sẽ không nhận ra nó như là một tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Các kiểu dữ liệu chuỗi, int và boolean:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Một bộ dữ liệu có các chuỗi, số nguyên và giá trị boolean:
tuple1 = ("abc", 34, True, 40, "male")

# Sử dụng phương thức tuple() để làm một tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)