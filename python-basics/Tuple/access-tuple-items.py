# In mục thứ hai trong bộ dữ liệu:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# In mục cuối cùng của bộ dữ liệu:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Trả lại mục thứ ba, thứ tư và thứ năm:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Ví dụ này trả về các mục từ đầu nhưng KHÔNG bao gồm "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# Ví dụ này trả về các mục từ "cherry" và đến cuối:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Ví dụ này trả về các mục từ index -4 (included) đến index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Kiểm tra xem "apple" có trong bộ dữ liệu không:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")