# List được sử dụng để lưu trữ nhiều mục trong một biến
# List được tạo bằng dấu ngoặc vuông

thislist = ["apple", "banana", "cherry"]
print(thislist)

# Các mục trong list được sắp xếp, có thể thay đổi, cho phép giá trị trùng lặp
# Các mục được lặp chỉ mục, mục đầu tiên có chỉ mục 0, mục thứ hai có index 1, v.v

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Để xác định danh sách có bao nhiêu mục, sử dụng len():
print(len(thislist))

# Các mục danh sách có thể thuộc bất kỳ kiểu dữ liệu nào:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# Một danh sách với các chuỗi, số nguyên và giá trị boolean:
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))

# hàm tạo constructor list()
thislist = list(("apple", "banana", "cherry"))
print(thislist)

