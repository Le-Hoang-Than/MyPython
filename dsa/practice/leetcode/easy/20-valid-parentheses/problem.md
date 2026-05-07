# 20. Valid Parentheses

`Easy` `Topics: String, Stack`

Cho một chuỗi schỉ chứa các ký tự '(', ')', '{', '}', '['và ']', hãy xác định xem chuỗi đầu vào có hợp lệ hay không.

Chuỗi đầu vào được coi là hợp lệ nếu:

1. Dấu ngoặc mở phải được đóng bằng cùng loại dấu ngoặc.
2. Các dấu ngoặc mở phải được đóng theo đúng thứ tự.
3. Mỗi dấu ngoặc đóng đều có một dấu ngoặc mở tương ứng cùng loại.

**Example 1:**

> **Input:** s = "()"
> 
> **Output:** true

**Example 2:**

> **Input:** s = "()[]{}"
> 
> **Output:** true

**Example 3:**

> **Input:** s = "(]"
> 
> **Output:** false

**Example 4:**

> **Input:** s = "([])"
> 
> **Output:** true

**Example 5:**

> **Input:** s = "([)]"
>
> **Output:** false

**Constraints:**

- $1 <= s.length <= 10^4$
- `s` Chỉ bao gồm dấu ngoặc đơn `'()[]{}'`.