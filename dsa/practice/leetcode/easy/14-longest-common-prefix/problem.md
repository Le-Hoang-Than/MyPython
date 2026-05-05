# 14. Longest Common Prefix

`Easy` `Array, String, Trie`

Viết một hàm để tìm chuỗi tiền tố chung dài nhất trong một mảng các chuỗi.

Nếu không có tiền tố chung, hãy trả về một chuỗi rỗng "".

**Example 1:**

> **Input:** strs = ["flower","flow","flight"]
> 
> **Output:** "fl"

**Example 2:**

> **Input:** strs = ["dog","racecar","car"]
>
> **Output:** ""
>
> **Explanation:** Không có tiền tố chung nào giữa các chuỗi đầu vào.

**Constraints:**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` chỉ bao gồm các chữ cái tiếng Anh viết thường nếu nó không rỗng.
