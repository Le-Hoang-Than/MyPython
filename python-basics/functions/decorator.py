"""
Decorator cho phép bạn thêm hành vi bổ sung vào một hàm mà không cần thay đổi mã của hàm đó.

Decorator là một hàm nhận một hàm khác làm đầu vào và trả về một hàm mới.
"""


# Trước tiên định nghĩa decorator, sau đó áp dụng bằng @decorator_namehàm phía trên.

# Một decorator cơ bản dùng để viết hoa giá trị trả về của hàm được trang trí.
def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Hello Sally"


print(myfunction())

"""
Bằng cách đặt @changecasetrực tiếp phía trên định nghĩa hàm, hàm myfunction được "trang trí" bằng changecase chính hàm đó.

Hàm changecase là hàm trang trí.

Hàm myfunction là hàm được trang trí.
"""


# Các hàm có đối số cũng có thể được trang trí:
def changecase(func):
    def myinner(x):
        return func(x).upper()

    return myinner


@changecase
def myfunction(nam):
    return "Hello " + nam


print(myfunction("John"))

"""
Đôi khi hàm trang trí không kiểm soát được các đối số được truyền từ hàm được trang trí. Để giải quyết vấn đề này, hãy thêm vào hàm bao bọc, bằng cách này hàm bao bọc có thể chấp nhận bất kỳ số lượng và bất kỳ loại đối số nào, và truyền chúng cho hàm được trang trí.(*args, **kwargs)
"""


# Bảo mật hàm với các đối số *args và **kwargs:
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return myinner


@changecase
def myfunction(nam):
    return "Hello " + nam


print(myfunction("John"))

"""
Các decorator có thể chấp nhận các đối số của chính chúng bằng cách thêm một lớp bao bọc khác.
"""


# Một factory decorator nhận một tham số và biến đổi kiểu chữ dựa trên giá trị của tham số đó.
def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a

        return myinner

    return changecase


@changecase(1)
def myfunction():
    return "Hello Linus"


print(myfunction())

"""
có thể sử dụng nhiều decorator trên cùng một hàm.

Việc này được thực hiện bằng cách đặt các lệnh gọi decorator chồng lên nhau.

Các decorator được gọi theo thứ tự ngược lại, bắt đầu từ decorator gần hàm nhất.
"""


def changecase(func):
    def myinner():
        return func().upper()

    return myinner


def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"

    return myinner


@changecase
@addgreeting
def myfunction():
    return "Tobias"


print(myfunction())

"""
Các hàm trong Python có siêu dữ liệu có thể được truy cập bằng cách sử dụng các thuộc tính `<function>` __name__và `<function> __doc__`.
"""


# Thông thường, tên của một hàm có thể được trả về cùng với __name__thuộc tính:
def myfunction():
    return "Have a great day!"


print(myfunction.__name__)


# Tuy nhiên, khi một hàm được trang trí thêm, siêu dữ liệu của hàm gốc sẽ bị mất.
def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Have a great day!"


print(myfunction.__name__)

"""
Để khắc phục điều này, Python có một hàm tích hợp sẵn functools.wraps có thể được sử dụng để giữ nguyên tên và chuỗi tài liệu của hàm gốc.
"""
# Import functools.wraps để giữ nguyên tên hàm và chuỗi tài liệu gốc.
import functools


def changecase(func):
    @functools.wraps(func)
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Have a great day!"


print(myfunction.__name__)
