# 1. Two Sum
 
Cho một mảng các số nguyên `nums` và một số nguyên `target`, hãy trả về chỉ số của hai số đó sao cho tổng của chúng bằng `target`.

Bạn có thể giả định rằng mỗi đầu vào sẽ có đúng **một giải pháp duy nhất** và bạn không được sử dụng cùng một phần tử hai lần.

Bạn có thể trả về kết quả theo bất kỳ thứ tự nào.


**Example 1:**
```markdown
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Giải thích: Vì nums[0] + nums[1] == 9, chúng ta return [0, 1].
```

**Example 2:**
```markdown
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**

```markdown
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Ràng buộc:**

- 2 <= nums.length <= 10<sup>4</sup>

- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

- -10<sup>9</sup> <= target <= 10<sup>9</sup>

- **Chỉ tồn tại duy nhất một đáp án đúng.**

**Follow-up:** Bạn có thể tìm ra một thuật toán có độ phức tạp thời gian nhỏ hơn O(n<sup>2</sup>) không?