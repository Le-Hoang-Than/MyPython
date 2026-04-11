"""
Trong Python, "array" thường dùng bằng list.
"""
nums = [1, 2, 3]
print(nums)

# Thêm phần tử vào cuối list
nums.append(4)
print(nums)

# Tạo bản sao của list
new_nums = nums.copy()
print(new_nums)

# Xóa toàn bộ phần tử
nums.clear()
print(nums)

# Đếm số lần xuất hiện
nums = [1, 2, 2, 3]
print(nums)
print(nums.count(2))

# Lấy vị trí phần tử đầu tiên
print(nums.index(2))

# Chèn phần tử vào vị trí xác định
nums.insert(1, 99)
print(nums)

# Xóa phần tử theo vị trí
nums.pop(2)
nums.pop()  # xóa phần tử cuối
print(nums)

# Xóa phần tử theo giá trị
nums.remove(99)
print(nums)

# Thêm nhiều phần tử (từ iterable khác)
nums.extend(new_nums)
print(nums)

# Đảo ngược list
nums.reverse()
print(nums)

# Sắp xếp list
nums.sort()
print(nums)

#Sắp xếp giảm dần:
nums.sort(reverse=True)
print(nums)
