"""
Khi tạo một tuple, thường gán giá trị cho nó. Quá trình này được gọi là "đóng gói" một tuple:
"""
# Đóng gói một tuple:
fruits = ("apple", "banana", "cherry")
print(fruits)

"""
Tuy nhiên, trong Python, chúng ta cũng được phép trích xuất các giá trị trở lại vào các biến. Quá trình này được gọi là "giải nén" (unpacking):
"""
# Giải nén một tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

"""
Nếu số lượng biến ít hơn số lượng giá trị, có thể thêm tham số *vào tên biến và các giá trị sẽ được gán cho biến đó dưới dạng một danh sách:
"""
# Gán các giá trị còn lại vào một danh sách có tên là "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

"""
Nếu dấu hoa thị được thêm vào tên của một biến khác với biến cuối cùng, Python sẽ gán giá trị cho biến đó cho đến khi số lượng giá trị còn lại bằng với số lượng biến còn lại.
"""
# Thêm danh sách các giá trị cho biến "tropic":
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)