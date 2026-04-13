"""
Generator là các hàm có thể tạm dừng và tiếp tục thực thi.

Khi một hàm tạo được gọi, nó sẽ trả về một đối tượng tạo , đó là một trình lặp.

Mã bên trong hàm chưa được thực thi, nó chỉ được biên dịch. Hàm chỉ được thực thi khi bạn lặp qua trình tạo.
"""


# Một hàm tạo đơn giản:

def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)
"""
Generator cho phép lặp lại dữ liệu mà không cần lưu trữ toàn bộ tập dữ liệu trong bộ nhớ.
Thay vì sử dụng return, các trình tạo sử dụng yieldtừ khóa .
"""

"""
Từ khóa yield chính là yếu tố biến một hàm thành hàm tạo.

Khi yield gặp sự kiện này, trạng thái của hàm được lưu lại và giá trị được trả về. Lần tiếp theo khi trình tạo được gọi, nó sẽ tiếp tục từ vị trí đã dừng lại.
"""


# hàm tạo tạo ra các con số:

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


for num in count_up_to(5):
    print(num)

"""
Không giống như return, hàm này kết thúc hàm hiện tại, yieldnó tạm dừng hàm và có thể được gọi nhiều lần.
"""

"""
Generator tiết kiệm bộ nhớ vì chúng tạo ra các giá trị ngay lập tức thay vì lưu trữ mọi thứ trong bộ nhớ.

Đối với các tập dữ liệu lớn, trình tạo giúp tiết kiệm bộ nhớ:
"""


# Bộ tạo chuỗi lớn:
def large_sequence(n):
    for i in range(n):
        yield i


# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

"""Sử dụng next() với Generators"""


def simple_gen():
    yield "Emil"
    yield "Tobias"
    yield "Linus"


gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
"""Khi không còn giá trị nào để trả về nữa, trình tạo sẽ báo lỗi StopIteration:"""


def simple_gen():
    yield 1
    yield 2


gen = simple_gen()
print(next(gen))
print(next(gen))
# print(next(gen)) # This will raise StopIteration

"""
Tương tự như list comprehensions, có thể tạo generator bằng cách sử dụng generator expressions với dấu ngoặc đơn thay vì dấu ngoặc vuông:
"""

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# Sử dụng biểu thức tạo với tổng:
# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)

"""
Có thể sử dụng gen để tạo ra dãy Fibonacci.

Nó có thể tiếp tục tạo ra các giá trị vô thời hạn mà không lo hết bộ nhớ:
"""


# Tạo 100 số Fibonacci:

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
    print(next(gen))

"""
Phương thức send() cho phép bạn gửi một giá trị đến trình tạo:
"""


def echo_generator():
    while True:
        received = yield
        print("Received:", received)


gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")

"""
Phương thức close() dừng hàm tạo:
"""


def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")


gen = my_gen()
print(next(gen))
gen.close()
