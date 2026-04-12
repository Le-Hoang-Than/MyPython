"""
Để xóa một mục trong một tập hợp, hãy sử dụng phương thức remove(), hoặc discard().
"""

# Loại bỏ "banana" bằng remove() method sau:

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print(thisset)
"""
Nếu mục cần xóa không tồn tại, remove()hệ thống sẽ báo lỗi.
"""

# Loại bỏ "chuối" bằng discard() method sau:
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.discard("banana")
print(thisset)
"""
Nếu mục cần xóa không tồn tại, discard()hệ thống sẽ KHÔNG báo lỗi.
"""

# Xóa ngẫu nhiên một mục bằng cách sử dụng pop() method sau:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
"""
Các tập hợp không được sắp xếp , vì vậy khi sử dụng pop()phương thức này, bạn không biết mục nào sẽ bị xóa.
"""

# Phương thức này clear() làm trống tập hợp:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Từ khóa này delsẽ xóa hoàn toàn tập hợp:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)