""""
Có nhiều cách để kết hợp hai hoặc nhiều tập hợp trong Python.

Phương thức union()AND update()kết hợp tất cả các mục từ cả hai tập hợp.

Phương pháp này intersection()CHỈ giữ lại các bản sao trùng lặp.

Phương pháp này difference()giữ lại các mục từ tập hợp đầu tiên mà không có trong (các) tập hợp khác.

Phương pháp này symmetric_difference()giữ lại tất cả các mục NGOẠI TRỪ các mục trùng lặp.
"""

# Phương thức union() trả về một tập hợp mới chứa tất cả các mục từ cả hai tập hợp.
# Kết hợp tập hợp 1 và tập hợp 2 thành một tập hợp mới:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# sử dụng |toán tử thay vì union()phương thức, và sẽ nhận được kết quả tương tự.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# Kết hợp nhiều tập hợp bằng union():

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Dùng |để nối hai tập hợp:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

"""
Phương pháp này union() cho phép kết hợp một tập hợp với các kiểu dữ liệu khác, chẳng hạn như list hoặc tuple.

Kết quả sẽ là một tập hợp.
"""

# Kết hợp một set với một tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z, type(z))

"""
Toán tử này  | chỉ cho phép kết hợp các tập hợp với nhau, chứ không phải với các kiểu dữ liệu khác như làm với phương thưc union() khác.
"""

"""
Phương thức update() chèn tất cả các mục từ một tập hợp vào một tập hợp khác.

Thao tác update() thay đổi tập hợp ban đầu và không trả về một tập hợp mới.
"""
# Phương thức update() chèn các phần tử trong tập hợp 2 vào tập hợp 1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

"""
Cả hai union() phương thức update() đều sẽ loại bỏ các mục trùng lặp.
"""
set1 = {3, "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

"""
Chỉ tạo bản sao

Phương thức  intersection()sẽ trả về một tập hợp mới, chỉ chứa các mục có mặt trong cả hai tập hợp.
"""
# Kết hợp tập hợp 1 và tập hợp 2, nhưng chỉ giữ lại các phần tử trùng lặp:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# có thể sử dụng &toán tử thay vì phương thức, và bạn sẽ nhận được kết quả tương tự. intersection()
# Dùng &để nối hai tập hợp:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
"""
Toán tử này & chỉ cho phép kết hợp các tập hợp với nhau, chứ không phải với các kiểu dữ liệu khác như bạn có thể làm với intersection()phương thức khác.
"""

"""
Phương pháp này intersection_update()cũng CHỈ giữ lại các phần tử trùng lặp, nhưng nó sẽ thay đổi tập hợp ban đầu thay vì trả về một tập hợp mới.
"""
# Giữ lại các mục tồn tại trong cả hai tập tin set1và set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

"""
Các giá trị Truevà 1 được coi là có cùng giá trị. Điều tương tự cũng áp dụng cho Falsevà 0.
"""
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

"""
Phương thức này sẽ trả về một tập hợp mới chỉ chứa các mục từ tập hợp đầu tiên mà không có trong tập hợp kia.difference()
"""
# Giữ lại tất cả các mục từ tập hợp 1 mà không có trong tập hợp 2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# có thể sử dụng -toán tử thay vì phương thức, và bạn sẽ nhận được kết quả tương tự. difference()
# Dùng -để nối hai tập hợp:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
"""Toán tử này - chỉ cho phép bạn kết hợp các tập hợp với nhau, chứ không phải với các kiểu dữ liệu khác như làm với difference()phương thức khác."""

"""Phương pháp này difference_update()sẽ giữ lại các mục từ tập hợp đầu tiên mà không có trong tập hợp kia, nhưng nó sẽ thay đổi tập hợp ban đầu thay vì trả về một tập hợp mới."""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

"""
Phương thức symmetric_difference()sẽ chỉ giữ lại những phần tử KHÔNG có mặt trong cả hai tập hợp.
"""
# Giữ lại những vật phẩm không có trong cả hai bộ:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

"""có thể sử dụng ^toán tử thay vì phương thức, và sẽ nhận được kết quả tương tự. symmetric_difference()"""
# Dùng ^để nối hai tập hợp:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
"""Toán tử này ^ chỉ cho phép kết hợp các tập hợp với nhau, chứ không phải với các kiểu dữ liệu khác như làm với symmetric_difference()phương thức khác."""

"""
Phương pháp này symmetric_difference_update()cũng sẽ giữ lại tất cả các phần tử ngoại trừ các phần tử trùng lặp, nhưng nó sẽ thay đổi tập hợp ban đầu thay vì trả về một tập hợp mới.
"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)