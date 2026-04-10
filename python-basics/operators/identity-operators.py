"""
is 	    Returns True if both variables are the same object	        x is y
is not	Returns True if both variables are not the same object	x is not y
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# Các toán tử is trả về True nếu cả hai biến đều trỏ đến cùng một đối tượng:
print(x is z)
print(x is y)
print(x == y)

# Các toán tử is not trả về True nếu cả hai biến đều không trỏ đến cùng một đối tượng:
print(x is not y)
