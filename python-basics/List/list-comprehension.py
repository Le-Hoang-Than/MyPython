"""
newlist = [expression for item in iterable if condition == True]

"""
# List comprehension cung cấp một cú pháp ngắn hơn khi muốn
# tạo một danh sách mới dựa trên các giá trị của một danh sách hiện có.
"""
Dựa trên list các loại trái cây, muốn có một danh sách mới,
chỉ chứa các loại trái cây với chữ "a" trong tên.

Nếu không  list comprehension, sẽ phải viết for với một bài kiểm tra
có điều kiện bên trong:
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

"""
Với  list comprehension có thể thực hiện tất cả những điều đó chỉ với một dòng mã:
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Các điều kiện giống như một bộ lọc chỉ chấp nhận các mục được đánh True.
"""
Điều kiện if x != "apple"  sẽ trả True đối với tất cả các yếu tố khác hơn "táo", làm cho danh sách mới chứa tất cả các loại trái cây ngoại trừ "táo".

Các điều kiện là tùy chọn và có thể bỏ qua:
"""
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# Các loop có thể là bất kỳ đối tượng có thể lặp lại nào, như list, tuple,set , v.v.
# Sử dụng range() tạo một iterable:
newlist = [x for x in range(10)]
print(newlist)

#Cùng một ví dụ, nhưng với một điều kiện là Chỉ chấp nhận các số thấp hơn 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

"""
Expression
"""
# Các Expression là mục hiện tại trong lần lặp, nhưng nó cũng là mục kết quả,
# mà có thể thao tác trước khi
# nó kết thúc giống như một mục danh sách trong danh sách mới:
# Đặt các giá trị trong danh sách mới thành chữ hoa:
newlist = [x.upper() for x in fruits]
print(newlist)
# Đặt tất cả các giá trị trong danh sách mới thành 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

# Các biểu hiện cũng có thể chứa các điều kiện,
# không giống như một bộ lọc, nhưng như một cách thao túng kết quả:
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)