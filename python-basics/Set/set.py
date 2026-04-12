"""
Set được sử dụng để lưu trữ nhiều mục trong một biến duy nhất.
Tập hợp là một tập hợp không có thứ tự , không thay đổi* và không được lập chỉ mục .
Các mục đã được thiết lập không thể thay đổi, nhưng có thể xóa các mục hiện có và thêm các mục mới.
"""
# Tạo một bộ:
thisset = {"apple", "banana", "cherry"}
print(thisset)

"""
Các mục trong tập hợp không được sắp xếp, không thể thay đổi và không cho phép giá trị trùng lặp.

Không có thứ tự" nghĩa là các mục trong một tập hợp không có thứ tự xác định.

Các mục trong tập hợp có thể xuất hiện theo thứ tự khác nhau mỗi khi sử dụng chúng, và không thể được tham chiếu bằng chỉ mục hoặc khóa.

Các mục trong tập hợp không thể thay đổi, nghĩa là chúng ta không thể thay đổi các mục sau khi tập hợp đã được tạo (có thể xóa các mục và thêm các mục mới).

Một tập hợp không thể có hai phần tử có cùng giá trị.
"""

# Các giá trị trùng lặp sẽ bị bỏ qua:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
"""
Các giá trị True và 1được coi là cùng một giá trị trong các tập hợp và được xử lý như các phần tử trùng lặp:
"""
# True và 1được coi là có cùng giá trị:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

"""
Các giá trị False và 0được coi là cùng một giá trị trong các tập hợp và được xử lý như các phần tử trùng lặp:
"""
# False và 0được coi là có cùng giá trị:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

# Tính số lượng phần tử trong một tập hợp:

thisset = {"apple", "banana", "cherry"}
print(thisset)

print(len(thisset))

# Các kiểu dữ liệu chuỗi, số nguyên và boolean:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# Một tập hợp chứa các chuỗi ký tự, số nguyên và giá trị boolean:

set4 = {"abc", 34, True, 40, "male"}

# Sử dụng hàm tạo set() để tạo một tập hợp:

thisset = set(("apple", "banana", "cherry"))
print(thisset)


