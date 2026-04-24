# The Captain's Room

Ông Anant Asankhya là quản lý tại khách sạn INFINITE. Khách sạn này có số lượng phòng vô hạn.

Vào một ngày đẹp trời, có một số lượng hữu hạn khách du lịch đến lưu trú.

Nhóm du khách bao gồm:

- Một Thuyền trưởng (Captain).
- Một số lượng không xác định các nhóm gia đình, mỗi nhóm có $K$ thành viên ($K \neq 1$)

Cách sắp xếp phòng:

- Thuyền trưởng được xếp một phòng riêng.
- Mỗi nhóm gia đình được xếp chung vào một phòng (một phòng cho mỗi nhóm).

Ông Anant có một danh sách không theo thứ tự các số phòng đã được ghi lại. Danh sách này chứa số phòng của tất cả du khách. Mỗi số phòng của các nhóm gia đình sẽ xuất hiện đúng $K$ lần trong danh sách, riêng số phòng của Thuyền trưởng chỉ xuất hiện duy nhất 1 lần.

Ông Anant cần bạn giúp tìm ra số phòng của Thuyền trưởng.

Bạn không biết tổng số khách hay tổng số nhóm gia đình. Bạn chỉ biết giá trị $K$ và danh sách số phòng.

**Input Format**

Dòng đầu tiên chứa số nguyên $K$ (kích thước của mỗi nhóm gia đình).

Dòng thứ hai chứa danh sách các số phòng (không theo thứ tự), cách nhau bởi dấu cách.

**Constraints**

$1 < K < 1000$

**Output Format**

In ra số phòng của Thuyền trưởng.

**Sample Input**

```markdown
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
```

**Sample Output**

```markdown
8
```

**Explanation**

Danh sách số phòng có tổng cộng 31 phần tử. Vì $K = 5$, nên phải có 6 nhóm gia đình ($6 \times 5 = 30$ người) và 1 Thuyền trưởng. Trong danh sách đã cho, tất cả các số phòng đều lặp lại đúng 5 lần, ngoại trừ số phòng 8.

Do đó, 8 là số phòng của Thuyền trưởng.