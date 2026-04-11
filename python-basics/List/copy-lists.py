"""
không thể sao chép một danh sách chỉ bằng cách gõ list2 = list1,
bởi vì: list2 sẽ chỉ là một tham khảo đến list1,
và những thay đổi được thực hiện trong list1 cũng sẽ tự động
được thực hiện trong list2.
"""

# Tạo một bản sao của một danh sách với các copy() phương pháp:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Tạo một bản sao của một danh sách với các list() phương pháp:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Tạo một bản sao của một danh sách  bằng cách sử dụng : toán tử (slice)
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)