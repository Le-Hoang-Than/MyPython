"""
không thể truy cập các mục trong một tập hợp bằng cách tham chiếu đến chỉ mục hoặc khóa.
Nhưng có thể lặp qua các mục trong tập hợp bằng vòng lặp for, hoặc kiểm tra xem một giá trị cụ thể có tồn tại trong tập hợp hay không bằng cách sử dụng từ khóa in.
"""

# Lặp qua tập hợp và in các giá trị:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Kiểm tra xem "banana" có xuất hiện trong tập hợp hay không:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

print("banana" not in thisset)
