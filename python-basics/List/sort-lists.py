"""
Đối tượng list có method sort()
sẽ sắp xếp danh sách theo thứ tự chữ và số, tăng dần theo mặc định:
"""
# Sắp xếp danh sách theo thứ tự bảng chữ cái:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sắp xếp danh sách bằng số:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

"""
Để sắp xếp giảm dần, hãy sử dụng đối số từ khóa reverse = True:
"""
# Sắp xếp danh sách theo thứ tự bảng chữ cái:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# Sắp xếp danh sách bằng số:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

"""
Tùy chỉnh hàm sort
"""
# Sắp xếp danh sách dựa trên mức độ gần của số 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

"""
Trường hợp Insensitive Sort
"""
# Theo mặc định các phương pháp sort() là trường hợp nhạy cảm,
# dẫn đến tất cả các chữ in hoa được sắp xếp trước các chữ thường:
# Phân loại phân biệt trường hợp có thể cho kết quả không mong muốn:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Thực hiện một loại danh sách không phân biệt chữ hoa chữ thường:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Đảo ngược thứ tự của các mục trong danh sách:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)