# In tất cả các mục trong danh sách, từng mục một:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Sử dụng range() và len() để tạo ra một iterable phù hợp.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# lặp qua các mục trong danh sách bằng cách sử dụng while .
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
