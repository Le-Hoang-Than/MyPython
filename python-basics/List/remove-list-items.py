# remove() method loại bỏ mục đã chỉ định.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.remove("banana")
print(thislist)

# Nếu có nhiều hơn một mục có giá trị được chỉ định,
# thì remove() method loại bỏ cái đầu tiên:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
thislist.remove("banana")
print(thislist)

# pop() phương thức loại bỏ theo index.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.pop(1)
print(thislist)

#Nếu bạn không chỉ định chỉ mục, pop() method loại bỏ mục cuối cùng.
thislist.pop()
print(thislist)

# del keyword cũng loại bỏ các chỉ định chỉ số:
thislist = ["apple", "banana", "cherry"]
print(thislist)
del thislist[0]
print(thislist)

# del keyword cũng có thể xóa hoàn toàn danh sách.
del thislist


# clear() method làm trống list.
# Danh sách vẫn còn, nhưng nó không có nội dung.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print(thislist)
