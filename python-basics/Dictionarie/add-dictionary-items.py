"""
Việc thêm một mục vào từ điển được thực hiện bằng cách sử dụng một khóa chỉ mục mới và gán giá trị cho nó:
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}
print(thisdict)

"""
Phương thức này update()sẽ cập nhật từ điển với các mục từ đối số được cung cấp. Nếu mục đó không tồn tại, mục đó sẽ được thêm vào.
"""
# Thêm mục màu vào từ điển bằng cách sử dụng update() phương thức:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})