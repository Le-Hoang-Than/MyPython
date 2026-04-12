"""
Sau khi tạo một bộ sưu tập, không thể thay đổi các thành phần trong đó, nhưng có thể thêm các thành phần mới.

Để thêm một mục vào một tập hợp, sử dụng phương thức add().
"""

# Thêm một mục vào một tập hợp bằng add() method:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

"""
Để thêm các mục từ một tập hợp khác vào tập hợp hiện tại, hãy sử dụng update() phương thức này.
"""
# Thêm các phần tử từ tropicalvào thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

"""
Đối tượng trong update() method không nhất thiết phải là một tập hợp, nó có thể là bất kỳ đối tượng có thể lặp nào (bộ dữ liệu, danh sách, từ điển, v.v.).
"""
# Thêm các phần tử của một danh sách vào một tập hợp:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
print(type(thisset))