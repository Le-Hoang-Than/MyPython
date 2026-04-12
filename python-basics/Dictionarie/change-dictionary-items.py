"""
có thể thay đổi giá trị của một mục cụ thể bằng cách tham chiếu đến tên khóa của nó:
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
thisdict["year"] = 2018
print(thisdict)

"""
Phương thức này update()sẽ cập nhật từ điển với các mục từ đối số được cung cấp.

Tham số tham số phải là một từ điển hoặc một đối tượng có thể lặp lại với các cặp khóa:giá trị.
"""
# Cập nhật "năm sản xuất" của xe bằng phương update() pháp sau:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
