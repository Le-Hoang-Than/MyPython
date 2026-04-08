# ==============================
# 1. IF - ELSE
# ==============================
age = 18

if age >= 18:
    print("Đủ tuổi")
else:
    print("Chưa đủ tuổi")

# ==	bằng
# !=	khác
# >	    lớn hơn
# <	    nhỏ hơn
# >=	lớn hơn hoặc bằng
# <=	nhỏ hơn hoặc bằng

# ==============================
# 2. IF - ELIF - ELSE
# ==============================

score = 8

if score >= 9:
    print("Giỏi")
elif score >= 7:
    print("Khá")
else:
    print("Trung bình")

# ==============================
# 3. NESTED IF
# ==============================

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Được vào")
    else:
        print("Thiếu giấy tờ")
else:
    print("Chưa đủ tuổi")

# ==============================
# 4. TOÁN TỬ LOGIC
# ==============================

# and	và
# or	hoặc
# not	phủ định

if age >= 18 and has_id:
    print("OK")

# ==============================
# 5. ternary operator - result = "Đúng" if condition else "Sai"
# ==============================
age = 18
msg = "Đủ tuổi" if age >= 18 else "Chưa đủ tuổi"
print(msg)

# ==============================
# 6. TRUE / FALSE
# ==============================

# Các giá trị được coi là False:
# 0
# ""
# None
# []
# {}

if "":
    print("True")
else:
    print("False")