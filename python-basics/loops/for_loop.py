# ==============================
# 1. FOR
# ==============================
for i in range(5):
    print(i)

"""
range(start, stop, step)
-start: bắt đầu
-stop: kết thúc (không bao gồm)
-step: bước nhảy
"""

for i in range(1, 6):
    print(i, end=" ")

print()

for i in range(0, 10, 2):
    print(i, end=" ")

# lặp với list
numbers = [1, 2, 3]
for n in numbers:
    print(n)

print()

# lặp qua chuỗi
for ch in "LeHoangThan":
    print(ch)

# enumerate() lấy index
names = ["Trần", "Nguyễn", "Đinh", "Lê", "Lý"]
for i, name in enumerate(names):
    print(i, name, sep="-")

# break
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")

print()

# continue
for i in range(10):
    if i == 2:
        continue
    print(i, end=" ")

# else trong for
for i in range(3):
    print(i)
else:
    print("Hoàn Thành!")

# lồng vòng lặp
for i in range(3):
    for j in range(2):
        print(i, j)

# list comprehension
numbers = [i for i in range(5)]
print(numbers)