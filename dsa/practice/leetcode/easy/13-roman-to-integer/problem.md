# 13. Roman to Integer

`Easy` `Topics: Hash Table, Math, String`

Số La Mã được đại diện bởi bảy ký hiệu khác nhau: I, V, X, L, C, D và M.

| Ký hiệu | 	Giá trị |
|---------|----------|
| I       | 	1       |
| V       | 	5       |
| X       | 	10      |
| L       | 	50      |
| C       | 	100     |
| D       | 	500     |
| M       | 	1000    |

Ví dụ, số $2$ được viết là II trong hệ La Mã, chỉ là hai số một cộng lại với nhau. Số $12$ được viết là XII, đơn giản là
X + II. Số $27$ được viết là XXVII, tức là XX + V + II.

Số La Mã thường được viết từ lớn nhất đến nhỏ nhất từ trái sang phải. Tuy nhiên, ký hiệu cho số bốn không phải là IIII.
Thay vào đó, số bốn được viết là IV. Bởi vì số một đứng trước số năm, chúng ta trừ nó đi để tạo thành bốn. Nguyên tắc
tương tự cũng áp dụng cho số chín, được viết là IX. Có sáu trường hợp phép trừ được sử dụng:

- I có thể được đặt trước V (5) và X (10) để tạo thành 4 và 9.
- X có thể được đặt trước L (50) và C (100) để tạo thành 40 và 90.
- C có thể được đặt trước D (500) và M (1000) để tạo thành 400 và 900.

Cho một chuỗi số La Mã, hãy chuyển đổi nó thành một số nguyên.

**Example 1:**

> **Input:** s = "III"
>
> **Output:** 3
> 
> **Explanation:** III = 3.

**Example 2:**

> **Input:** s = "LVIII"
> 
> **Output:** 58
> 
> **Explanation:** L = 50, V = 5, III = 3.

**Example 3:**

> **Input:** s = "MCMXCIV"
>
> **Output:** 1994
> 
> **Explanation:** M = 1000, CM = 900, XC = 90 và IV = 4.

**Constraints:**

- $1 \le s.length \le 15$
- s chỉ chứa các ký tự ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- Đảm bảo s là một số La Mã hợp lệ trong khoảng $[1, 3999]$.