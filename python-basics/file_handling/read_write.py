# =========================================
# PYTHON FILE HANDLING
# =========================================

import os

# =========================================
# 1. TẠO & GHI FILE (write mode)
# =========================================
print("=== WRITE FILE ===")

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello Python\n")
    f.write("File Handling Demo\n")
    f.close()
print("Đã ghi file data.txt")

# =========================================
# 2. GHI THÊM FILE (append mode)
# =========================================
print("\n=== APPEND FILE ===")

with open("data.txt", "a", encoding="utf-8") as f:
    f.write("Dòng mới được thêm\n")
    f.close()
print("Đã append thêm nội dung")

# =========================================
# 3. ĐỌC TOÀN BỘ FILE
# =========================================
print("\n=== READ FILE ===")

with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    f.close()
print("Nội dung file:")
print(content)

# =========================================
# 4. ĐỌC TỪNG DÒNG
# =========================================
print("\n=== READ LINE BY LINE ===")

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
    f.close()
# =========================================
# 5. read(), readline(), readlines()
# =========================================
print("\n=== READ METHODS ===")

with open("data.txt", "r", encoding="utf-8") as f:
    print("read():")
    print(f.read())
    f.close()
with open("data.txt", "r", encoding="utf-8") as f:
    print("\nreadline():")
    print(f.readline())
    f.close()
with open("data.txt", "r", encoding="utf-8") as f:
    print("\nreadlines():")
    print(f.readlines())
    f.close()
# =========================================
# 6. WRITELINES()
# =========================================
print("\n=== WRITELINES ===")

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("list.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
    f.close()
print("Đã ghi list.txt")

# =========================================
# 7. KIỂM TRA FILE TỒN TẠI
# =========================================
print("\n=== CHECK FILE EXISTS ===")

if os.path.exists("data.txt"):
    print("data.txt tồn tại")
else:
    print("data.txt không tồn tại")

# =========================================
# 8. THÔNG TIN FILE
# =========================================
print("\n=== FILE INFO ===")

print("Thư mục hiện tại:", os.getcwd())
print("Danh sách file:", os.listdir())

# =========================================
# 9. FILE POINTER
# =========================================
print("\n=== FILE POINTER ===")

with open("data.txt", "r", encoding="utf-8") as f:
    print("Vị trí ban đầu:", f.tell())

    f.read(5)
    print("Sau khi đọc 5 ký tự:", f.tell())

    f.seek(0)
    print("Sau khi quay lại đầu:", f.tell())
    f.close()
# =========================================
# 10. COPY FILE
# =========================================
print("\n=== COPY FILE ===")

with open("data.txt", "r", encoding="utf-8") as f1, \
        open("copy.txt", "w", encoding="utf-8") as f2:
    f2.write(f1.read())
    f1.close()
    f2.close()
print("Đã copy sang copy.txt")

# =========================================
# 11. BINARY FILE (demo cơ bản)
# =========================================
print("\n=== BINARY FILE ===")

with open("binary.bin", "wb") as f:
    f.write(b"Hello Binary")
    f.close()
with open("binary.bin", "rb") as f:
    data = f.read()
    print("Binary data:", data)
    f.close()
# =========================================
# 12. XÓA FILE
# =========================================
print("\n=== DELETE FILE ===")

if os.path.exists("temp.txt"):
    os.remove("temp.txt")
    print("Đã xóa temp.txt")
else:
    print("temp.txt không tồn tại")
