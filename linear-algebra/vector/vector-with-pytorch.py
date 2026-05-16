import torch

x = torch.tensor([1, 1.2, 1.5, 1.8, 2])

print(x)

# Độ dài
print("length of vector: ", x.size())  # or len(x)

# Định dạng của véc tơ
print("vector type: ", x.dtype)

# Tổng của các phần tử
print("sum of vector: ", x.sum())

# Trung bình các phần tử
print("mean of vector: ", x.mean())

# Giá trị nhỏ nhất
print("min of vector: ", x.min())

# Giá trị lớn nhất
print("max of vector: ", x.max())

x = torch.tensor([1, 2, 1.5, 1.8, 1.9])

y = torch.tensor([1.1, 2.2, 1.2, 1.6, 1.7])

print("x + y: ", x + y)

print("x - y: ", x - y)

print("x * y: ", x * y)

x = torch.tensor([1, 2, 1.5, 1.8, 1.9])

print("x + 5: ", x + 5)

print("x - 5: ", x - 5)

print("x * 5: ", x * 5)