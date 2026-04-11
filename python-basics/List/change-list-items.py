# Để thay đổi giá trị của một mục cụ thể, cần số chỉ số:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "blackcurrant"
print(thislist)

# thay đổi giá trị của các mục trong một phạm vi cụ thể
# xác định danh sách với các giá trị mới và tham chiếu đến phạm vi số chỉ mục
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Nếu chèn nhiều hơn các mục hơn thay thế, các mục mới sẽ được chèn vào nơi bạn đã chỉ định,
# và các mục còn lại sẽ di chuyển tương ứng
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Nếu bạn chèn ít hơn các mục hơn bạn thay thế, các mục mới sẽ được chèn vào nơi bạn đã chỉ định,
# và các mục còn lại sẽ di chuyển tương ứng:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1:3] = ["watermelon"]
print(thislist)

# insert() method chèn một item tại index đã chỉ định:
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)
