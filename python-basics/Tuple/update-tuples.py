"""
Khi một tuple được tạo, bạn không thể thay đổi các giá trị của nó.
Bộ dữ liệu là không thay đổi, hoặc bất biến.

Nhưng có một cách giải quyết. Bạn có thể chuyển đổi bộ dữ liệu thành
list, thay đổi list và chuyển đổi list trở lại thành tuple.
"""

# Chuyển đổi bộ dữ liệu thành danh sách để có thể thay đổi nó:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

"""
Vì các bộ dữ liệu là bất biến nên chúng không có sẵn append() method, 
nhưng có nhiều cách khác để thêm các mục vào một bộ.

1. Chuyển đổi thành một list: Giống như cách giải quyết cho thay đổi 
một bộ, chuyển đổi nó thành một danh sách, thêm (các) mục và 
chuyển đổi nó trở lại thành tuple.
"""
# Chuyển đổi tuple thành list, thêm "cam" và chuyển đổi lại thành tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

"""
2. Thêm tuple vào một tuple. Được phép thêm tuple vào tuple, 
vì vậy nếu muốn thêm một mục, (hoặc nhiều), 
hãy tạo một bộ dữ liệu mới với item (s), và thêm nó vào tuple hiện có:
"""
# Tạo một tuple mới với giá trị "orange", và thêm tuple đó:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Chuyển đổi bộ dữ liệu thành danh sách, xóa "quả táo" và chuyển đổi lại thành bộ dữ liệu:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# Các del keyword có thể xóa tuple hoàn toàn:
thistuple = ("apple", "banana", "cherry")
del thistuple
