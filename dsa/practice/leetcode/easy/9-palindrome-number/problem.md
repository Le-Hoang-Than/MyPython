# 9. Palindrome Number

`Easy` `Topics: Math`

Cho một số nguyên `x`, trả về `true` nếu `x` là số đối xứng (palindrome), và `false` nếu ngược lại.

**Example 1:**

> **Input:** x = 121
>
> **Output:** true
>
> **Explanation:** 121 đọc từ trái sang phải hay từ phải sang trái đều là 121.

**Example 2:**

> **Input:** x = -121
> 
> **Output:** false
> 
> **Explanation:** Từ trái sang phải, nó là -121. Từ phải sang trái, nó trở thành 121-. Vì vậy đây không phải là số đối xứng.

**Example 3:**

> **Input:** x = 10
> 
> **Output:** false
> 
> **Explanation:** Đọc từ phải sang trái là 01. Vì vậy đây không phải là số đối xứng.

**Constraints:**

>$-2^{31} \le x \le 2^{31} - 1$

**Follow up:** Bạn có thể giải bài toán này mà không cần chuyển đổi số nguyên thành chuỗi (string) không?
