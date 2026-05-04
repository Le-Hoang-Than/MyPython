# Notes

---

## 9. Palindrome Number

**Mục tiêu bài toán:**

- True: nếu x là số đối xứng
- False: nếu x là số bất đối xứng

**Ý tưởng:**

### Cách 1:

- Sử dụng phép chia lấy phần nguyên(//) và lấy phần dư mod(%)

Ví dụ: x = 12321

- Lần 1: x = 12321
    - Lấy số nguyên x chia 10 lấy phần dư: 12321 % 10 = 1
    - Lấy số nguyên x chia 10000 lấy phần nguyên: 12321 // 10000 = 1

- Bước chuyển:
    - Sau khi lấy được số đầu và số cuối cần loại bỏ 2 chữ số đó:
    - x = 12321
    - 12321 % 10000 = 2321
    - 2321 // 10 = 232

- Lần 2: x = 232
    - Lấy số nguyên x chia cho 10 lấy phần dư: 232 % 10 = 2
    - Lấy số nguyên x chia cho 100 lấy phần nguyên: 232 // 100 = 2

Cần thêm một lần nữa nếu trường hợp số nguyên x có độ dài các chữ số là chẵn

- Bước chuyển:
    - Sau khi lấy được số đầu và số cuối cần loại bỏ 2 chữ số đó:
    - x = 232
    - 232 % 100 = 32
    - 32 // 10 = 3

- Lần 3: x = 3
    - Lấy số nguyên x chia cho 10 lấy phần dư: 3 % 10 = 0
    - Lấy số nguyên x chia cho 100 lấy phần nguyên: 3 // 10 = 0

Cách 1 cần phải tìm được ước số để chia lấy dư

### Cách 2

- Ép số sang chuổi để so sánh
- So sánh chuỗi thận với chuỗi đảo được

**Cách giải**

### Cách 1: Cần phải có một hằng số

```text
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        const = 1
        while num // (const * 10) > 0:
            const *= 10

        while num > 0:
            fist = num // const
            last = num % 10
            if fist != last:
                return False
            num = (num % const) // 10
            const //= 100
        return True
```

### Cách 2: Sử dụng chuỗi

```text
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else str(x) == str(x)[::-1]
```

