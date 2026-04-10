"""
Các toán tử bitwise được sử dụng để so sánh các số (nhị phân):

& 	AND
Sets each bit to 1 if both bits are 1
x & y

|	OR
Sets each bit to 1 if one of two bits is 1
x | y

^	XOR
Sets each bit to 1 if only one of two bits is 1
x ^ y

~	NOT
Inverts all the bits
~x

<<	Zero fill left shift
Shift left by pushing zeros in from the right and let the leftmost bits fall off
x << 2

>>	Signed right shift
Shift right by pushing copies of the leftmost bit in from the left,
and let the rightmost bits fall off
x >> 2
"""

# Toán tử & so sánh từng bit và đặt nó thành 1 nếu cả hai đều là 1, nếu không thì nó được đặt thành 0:

print(6 & 3)
# Biểu diễn nhị phân của 6 là 0110
# Biểu diễn nhị phân của 3 là 0011

# Sau đó, toán tử & so sánh các bit và trả về 0010, bằng 2 số thập phân.

# Toán tử | so sánh từng bit và đặt nó thành 1 nếu một hoặc cả hai đều là 1, nếu không thì nó được đặt thành 0:

print(6 | 3)
# Biểu diễn nhị phân của 6 là 0110
# Biểu diễn nhị phân của 3 là 0011

# Sau đó, toán tử | so sánh các bit và trả về 0111, bằng 7 số thập phân.

# Toán tử ^ so sánh mỗi bit và đặt nó thành 1 nếu chỉ có một là 1, nếu không (nếu cả hai đều là 1 hoặc cả hai đều là 0) thì nó được đặt thành 0:

print(6 ^ 3)
# Biểu diễn nhị phân của 6 là 0110
# Biểu diễn nhị phân của 3 là 0011

# Sau đó, toán tử ^ so sánh các bit và trả về 0101, là 5 trong số thập phân.