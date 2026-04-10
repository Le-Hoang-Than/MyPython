"""
Bạn có thể lấy kiểu dữ liệu của bất kỳ đối tượng nào bằng cách sử dụng hàm type():
x = 5
print(type(x))
"""
# Text Type:	    str
x = "Hello World"
print(x)
print(type(x))

print()
# Numeric Types:	int, float, complex
x = 20
print(x)
print(type(x))

print()
x = 20.5
print(x)
print(type(x))

print()
x = 1j
print(x)
print(type(x))

print()
# Sequence Types:	list, tuple, range
x = ["apple", "banana", "cherry"]
print(x)
print(type(x))

x = ("apple", "banana", "cherry")
print(x)
print(type(x))

print()
x = range(10)
print(x)
# convert to list to display the content of x:
print(list(x))

print()
# Mapping Type:	    dict
x = {"name": "John", "age": 36}
print(x)
print(type(x))

print()
# Set Types:	    set, frozenset
x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

print()
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

print()
# Boolean Type:	    bool
x = True
print(x)
print(type(x))

print()
# Binary Types:	    bytes, bytearray, memoryview
x = b"Hello"
print(x)
print(type(x))

print()
x = bytearray(5)
print(x)
print(type(x))

print()
x = memoryview(bytes(5))
print(x)
print(type(x))

print()
# None Type:	    NoneType
x = None
print(x)
print(type(x))
print()
#=========================
# Chỉ định kiểu dữ liệu
#=========================
x = str("Hello World")
print(x)
print(type(x))
print()

x = int(20)
print(x)
print(type(x))
print()

x = float(20.5)
print(x)
print(type(x))
print()

x = complex(1j)
print(x)
print(type(x))
print()

x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))
print()

x = tuple(("apple", "banana", "cherry"))
print(x)
print(type(x))
print()

x = range(6)
print(x)
print(type(x))
print()

x = dict(name="John", age=36)
print(x)
print(type(x))
print()

x = set(("apple", "banana", "cherry"))
print(x)
print(type(x))
print()

x = frozenset(("apple", "banana", "cherry"))
print(x)
print(type(x))
print()

x = bool(5)
print(x)
print(type(x))
print()

x = bytes(5)
print(x)
print(type(x))
print()

x = bytearray(5)
print(x)
print(type(x))
print()

x = memoryview(bytes(5))