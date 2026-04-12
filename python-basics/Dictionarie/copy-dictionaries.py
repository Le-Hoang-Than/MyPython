"""
không thể sao chép một từ điển chỉ bằng cách gõ dict2 = dict1, vì: dict2chỉ là một tham chiếu đến dict1, và những thay đổi được thực hiện trong dict1cũng sẽ tự động được thực hiện trong dict2.

Có nhiều cách để tạo bản sao, một trong số đó là sử dụng phương thức Từ điển tích hợp sẵn copy().
"""
# Sao chép một cuốn từ điển bằng phương thuc copy() sau:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Tạo bản sao của một từ điển bằng dict() hàm:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
