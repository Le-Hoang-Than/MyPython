# Python print() - Lý thuyết đầy đủ

## 1. Giới thiệu

`print()` là hàm dùng để xuất dữ liệu trong Python.

Nhiệm vụ chính:

- Chuyển dữ liệu thành chuỗi (`str`)
- Gửi dữ liệu đó tới một luồng output (mặc định là màn hình)

---

## 2. Cú pháp tổng quát

```python
print(*values, sep=' ', end='\n', file=None, flush=False)
```

## 3. Thành phần chi tiết

### 3.1 values

Là các giá trị cần in
Có thể là nhiều kiểu dữ liệu: int, float, str, bool, list,...

Python sẽ tự động chuyển sang chuỗi bằng str()

Ví dụ:

```python
print(10, 3.14, True)
```

### 3.2 sep (separator)

Là chuỗi phân cách giữa các giá trị
Mặc định: " " (dấu cách)

Cách hoạt động:

```python
value1 + sep + value2 + sep + value3
```

Ví dụ:

```python
print("A", "B", "C", sep="-")
```

Output:

```python
A - B - C
```

### 3.3 end (terminator)

Là chuỗi kết thúc sau khi in
Mặc định: "\n" (xuống dòng)

Cách hoạt động: `output = content + end`

Ví dụ:

```python
print("Hello", end=" ")
print("World")
```

Output:

```python
Hello
World
```

### 3.4 file (output stream)

Xác định nơi dữ liệu được gửi tới
Mặc định: sys.stdout (màn hình)

Có thể ghi ra file:

```python
with open("output.txt", "w") as f:
    print("Hello", file=f)
```

### 3.5 flush (buffer control)

Điều khiển việc xả bộ đệm (buffer)
Mặc định: False
Buffer là gì?

Python không in ngay lập tức mà:

Ghi vào bộ đệm
Khi đủ điều kiện → mới hiển thị
flush = True
In ngay lập tức
Dùng cho:
realtime output
debug
tool mạng

Ví dụ:

```python
print("Loading...", flush=True)
```

## 4. Luồng hoạt động của print()

`values → str() → nối bằng sep → thêm end → ghi vào file → flush?`

## 5. Ví dụ phân tích
```python
print("A", "B", sep="-", end="!", flush=True)
```

Quy trình:

1. "A" → "A"
2. "B" → "B"
3. Nối: "A-B"
4. Thêm end: "A-B!"
5. Ghi ra stdout
6. Flush ngay