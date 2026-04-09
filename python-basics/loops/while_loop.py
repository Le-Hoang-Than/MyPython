# ==============================
# 1. FOR
# ==============================
x=0
while x < 5:
    print(x)
    x += 1

# break
while True:
    x = input("Nhập 'exit' để thoát: ")
    if x == "exit":
        break

# continue
x = 0

while x < 5:
    x += 1
    if x == 3:
        continue
    print(x, end=" ")

# while - else
x = 0

while x < 3:
    print(x)
    x += 1
else:
    print("Hoàn thành")