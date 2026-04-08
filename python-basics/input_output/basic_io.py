# ==============================
# 1. OUTPUT - print(values, sep, end, file, flush)
# ==============================
print("Hello World")
print(123)
print("Hello", 123)

# f-string (rất quan trọng)
name = "lEhOANGtHAN"
age = 22
print(f"Tôi là {name}, {age} tuổi")

# separator
print("A", "B", "C", sep="-")

# end
print("Hello", end=" ")
print("World")

# new line
print("Hello\nWorld")
print("Hello", end="\n")
print("World")

# .format()
print("Tên: {}, Tuổi: {}".format("lEhOANGtHAN", 22))

# % formating
print("Tên: %s, Tuổi: %d" % ("lEhOANGtHAN", 22))

# In danh sách / unpack
numbers = [1, 2, 3]
print(*numbers)

# file
with open("output.txt", "w") as f:
    print("Hello file", file=f)

# ==============================
# 2. INPUT cơ bản
# ==============================
name = input("Nhập tên của bạn: ")
print("Xin chào", name)

# input không có prompt
product = input()

# ép kiểu trực tiếp
seri = int(input("Nhập seri: "))
price = float(input("Nhập giá: "))

# nhập nhiều giá trị cùng lúc
a, b = input("nhập số a và b").split()
a, b = map(int, input().split())

# nhập list
number = list(map(int, input().split()))

# nhập từng ký tự
chars = list(input("nhập chuỗi: "))

# nhập nhiều dòng
for i in range(3):
    x = input(f"Lần {i}: ")
    print(x)

