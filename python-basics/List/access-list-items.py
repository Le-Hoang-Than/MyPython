# Các mục danh sách được lập chỉ mục và bạn có thể truy cập chúng bằng cách tham khảo số chỉ mục:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Chỉ mục tiêu cực có nghĩa là bắt đầu từ cuối
# -1 đề cập đến mục cuối cùng, -2 đề cập đến mục cuối cùng thứ hai, v.v.
print(thislist[-1])

# Bạn có thể chỉ định một phạm vi chỉ mục bằng cách chỉ định nơi bắt đầu và nơi đến kết thúc phạm vi.
# Khi chỉ định một phạm vi, giá trị trả về sẽ là một danh sách mới với các các mục được chỉ định.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

# Để xác định xem một mục được chỉ định có trong danh sách hay không, sử dụng in:
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")