"""
()	                    :Parentheses
**	                    :Exponentiation
+x  -x  ~x	            :Unary plus, unary minus, and bitwise NOT
*  /  //  %	            :Multiplication, division, floor division, and modulus
+  -	                :Addition and subtraction
<<  >>	                :Bitwise left and right shifts
&	                    :Bitwise AND
^	                    :Bitwise XOR
|	                    :Bitwise OR
==  !=  >  >=  <  <=
is, is not, in, not in 	:Comparisons, identity, and membership operators
not	                    :Logical NOT
and	                    :AND
or	                    :OR
"""

# Cộng + và phép trừ - có cùng quyền ưu tiên,
# và do đó chúng ta đánh giá biểu thức từ trái sang phải:
print(5 + 4 - 7 + 3)
