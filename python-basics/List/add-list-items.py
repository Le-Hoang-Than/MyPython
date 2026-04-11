# append item
# Để thêm một mục vào cuối danh sách, hãy sử dụng append()
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.append("orange")
print(thislist)

# Để chèn một mục danh sách tại một chỉ mục được chỉ định, sử dụng insert()
thislist.insert(1, "pineapple")
print(thislist)

# Để nối các phần tử từ danh sách khác vào danh sách hiện tại, sử dụng extend()
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Các extend() không phải nối thêm danh sách,
# có thể thêm bất kỳ đối tượng có thể lặp lại nào
# tuples, sets, dictionaries, v.v
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)