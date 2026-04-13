"""
JSON là một cú pháp dùng để lưu trữ và trao đổi dữ liệu.

JSON là văn bản được viết bằng cú pháp đối tượng JavaScript.
"""

"""
Python có một gói tích hợp sẵn gọi là `<json>` json, có thể được sử dụng để làm việc với dữ liệu JSON.
"""
import json

"""
Nếu có một chuỗi JSON, bạn có thể phân tích cú pháp nó bằng cách sử dụng json.loads() method.
Kết quả sẽ là một dictionary
"""
# Chuyển đổi từ JSON sang Python:
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

"""
Nếu có một đối tượng Python, có thể chuyển đổi nó thành chuỗi JSON bằng cách sử dụng json.dumps() method.
"""
# Chuyển đổi từ Python sang JSON:
# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# Chuyển đổi các đối tượng Python thành chuỗi JSON và in ra các giá trị:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Chuyển đổi một đối tượng Python chứa tất cả các kiểu dữ liệu hợp lệ:
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

"""
Ví dụ trên in ra một chuỗi JSON, nhưng nó không dễ đọc vì không có thụt lề và xuống dòng.

Phương pháp này json.dumps()có các tham số để giúp việc đọc kết quả dễ dàng hơn:
"""
# Sử dụng tham số indent để xác định số lượng thụt lề:

print(json.dumps(x, indent=4))

"""
 có thể định nghĩa các dấu phân cách, giá trị mặc định là (", ", ": "), nghĩa là sử dụng dấu phẩy và dấu cách để phân tách từng đối tượng, và dấu hai chấm và dấu cách để phân tách khóa khỏi giá trị:
"""
# Sử dụng tham số separators này để thay đổi dấu phân cách mặc định:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Sử dụng tham số sort_keys này để chỉ định xem kết quả có nên được sắp xếp hay không:
print(json.dumps(x, indent=4, sort_keys=True))

