"""
=	    x = 5	        x = 5
+=	    x += 3	        x = x + 3
-=	    x -= 3	        x = x - 3
*=	    x *= 3	        x = x * 3
/=	    x /= 3	        x = x / 3
%=	    x %= 3	        x = x % 3
//=	    x //= 3	        x = x // 3
**=	    x **= 3	        x = x ** 3
&=	    x &= 3	        x = x & 3
|=	    x |= 3	        x = x | 3
^=	    x ^= 3	        x = x ^ 3
>>=	    x >>= 3	        x = x >> 3
<<=	    x <<= 3	        x = x << 3
:=	    print(x := 3)	x = 3
                        print(x)
"""
x = 5
print("x = 5 \t⇒\t", x)
x += 3
print("x += 3 \t⇒\t", x)
x -= 3
print("x -= 3 \t⇒\t", x)
x *= 3
print("x *= 3\t⇒\t", x)
x /= 3
print("x /= 3\t⇒\t", x)
x %= 3
print("x %= 3\t⇒\t", x)
x //= 3
print("x //= 3\t⇒\t", x)
x **= 3
print("x **= 3\t⇒\t", x)
x = 5
x &= 3
print("x &= 3\t⇒\t", x)
x |= 3
print("x |= 3\t⇒\t", x)
x = 5
x ^= 1
print("x ^= 3\t⇒\t", x)
x = 5
x >>= 1
print("x >>= 3\t⇒\t", x)
x = 5
x <<= 1
print("x <<= 3\t⇒\t", x)
x = 3
print("print(x := 3) ⇒", x)
