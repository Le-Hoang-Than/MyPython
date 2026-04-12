"""
Trong Python, chuỗi ký tự được bao quanh bởi dấu ngoặc đơn hoặc dấu ngoặc kép.

'hello' cũng giống như "hello" .

Bạn có thể hiển thị một chuỗi ký tự bằng print()hàm:
"""
print("Hello")
print('Hello')
"""
Bạn có thể sử dụng dấu ngoặc kép bên trong chuỗi, miễn là chúng không trùng với dấu ngoặc kép bao quanh chuỗi đó:
"""
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

"""Việc gán một chuỗi cho một biến được thực hiện bằng cách sử dụng tên biến, theo sau là dấu bằng và chuỗi đó:
"""
a = "Hello"
print(a)

"""Bạn có thể gán một chuỗi nhiều dòng cho một biến bằng cách sử dụng ba dấu ngoặc kép:
"""
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

"""Hoặc ba dấu ngoặc kép đơn:"""
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

"""Lưu ý: trong kết quả, các dấu xuống dòng được chèn vào cùng vị trí như trong mã nguồn.
"""

"""
Giống như nhiều ngôn ngữ lập trình phổ biến khác, chuỗi trong Python là mảng các ký tự Unicode.

Tuy nhiên, Python không có kiểu dữ liệu ký tự, một ký tự đơn giản chỉ là một chuỗi có độ dài là 1.

Dấu ngoặc vuông có thể được sử dụng để truy cập các phần tử của chuỗi.
"""

# Lấy ký tự ở vị trí 1 (nhớ rằng ký tự đầu tiên có vị trí 0):

a = "Hello, World!"
print(a[1])

"""Vì chuỗi ký tự là mảng, chúng ta có thể lặp qua các ký tự trong chuỗi bằng forvòng lặp."""
for x in "banana":
  print(x)

# Hàm len()trả về độ dài của một chuỗi:

a = "Hello, World!"
print(len(a))

# Kiểm tra xem từ "free" có xuất hiện trong đoạn văn sau hay không:

txt = "The best things in life are free!"
print("free" in txt)

# Chỉ in nếu có tùy chọn "free":

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Để kiểm tra xem một cụm từ hoặc ký tự nhất định có xuất hiện trong một chuỗi hay không, ta có thể sử dụng từ khóa not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

# Chỉ in nếu không có từ "expensive":

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
