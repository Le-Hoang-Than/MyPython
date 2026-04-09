# ==============================
# 1. FUNCTION
# ==============================
from os import name


def say_hello():
    print("hello")


say_hello()


# parameters
def greet(name):
    print("Hello", name)


greet("Lê Hoàng Thân")


def add(a, b):
    print(a + b)


add(3, 5)


# return
def add(a, b):
    return a + b


print(add(3, 5))


# default parameter
def greet(name="Guest"):
    print("Hello", name)


greet()
greet("lÊ hOÀNG tHÂN")


# keyword arguments
def info(name, age):
    print(name, age)


info(name="lê hoàng thân", age=22)


# *args
def total(*numbers):
    return sum(numbers)


print(total(1, 2, 3))


# **kwargs (dictionary)
def info(**data):
    print(data)


info(name="Than", age=22)


# hàm lồng nhau
def outner():
    def inner():
        print("Inside")

    inner()


outner()

# Lambda function
add = lambda a, b: a + b
print(add(2, 3))


# local variable
def local():
    x = 10
    print(x)
local()

# global variable
x = 101


def glbl():
    print(x)
glbl()