# Lặp qua từng mục và in ra các giá trị:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# In tất cả các mục bằng cách tham chiếu đến số chỉ mục của chúng:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# In tất cả các mục, sử dụng while để duyệt qua tất cả các số chỉ mục:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

