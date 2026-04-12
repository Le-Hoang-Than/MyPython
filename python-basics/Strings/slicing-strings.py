"""có thể trả về một phạm vi ký tự bằng cách sử dụng cú pháp slice.

Hãy chỉ định chỉ mục bắt đầu và chỉ mục kết thúc, được phân tách bằng dấu hai chấm, để trả về một phần của chuỗi."""

# Lấy các ký tự từ vị trí 2 đến vị trí 5 (không bao gồm):

b = "Hello, World!"
print(b[2:5])

# Đưa các nhân vật từ vị trí đầu tiên đến vị trí thứ 5 (không bao gồm):

b = "Hello, World!"
print(b[:5])

# Lấy các ký tự từ vị trí thứ 2 cho đến hết hàng:

b = "Hello, World!"
print(b[2:])
"""
Tìm các nhân vật:

Từ: "o" trong "World!" (vị trí -5)

Đến: nhưng không bao gồm: "d" trong "World!" (vị trí -2):
"""
b = "Hello, World!"
print(b[-5:-2])