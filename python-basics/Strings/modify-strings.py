# Phương thức upper() trả về chuỗi ở dạng chữ hoa:

a = "Hello, World!"
print(a.upper())

# Phương thức lower()trả về chuỗi ở dạng chữ thường:

a = "Hello, World!"
print(a.lower())

# Phương pháp strip() loại bỏ mọi khoảng trắng ở đầu hoặc cuối chuỗi:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Phương thức này replace()thay thế một chuỗi ký tự bằng một chuỗi ký tự khác:

a = "Hello, World!"
print(a.replace("H", "J"))

# Phương pháp này split()sẽ chia chuỗi thành các chuỗi con nếu tìm thấy các trường hợp xuất hiện của ký tự phân cách:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']