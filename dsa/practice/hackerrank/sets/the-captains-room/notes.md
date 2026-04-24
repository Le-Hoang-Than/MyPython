# Note

---

## The Captain's Room

**Mục tiêu bài toán**

Tìm phòng của thuyền trưởng trong nhóm du khách, bao gồm:

- Một Thuyền trưởng (Captain).
    - Thuyền trưởng được xếp một phòng riêng.
- Một số lượng không xác định các nhóm gia đình, mỗi nhóm có $K$ thành viên ($K \neq 1$)
    - Mỗi nhóm gia đình được xếp chung vào một phòng (một phòng cho mỗi nhóm).

**Ý tưởng**

Ta có:

- K thành viên của mỗi nhóm.
    - Ví dụ: K = 5
- Một danh sách (list) L gồm các danh sách các số phòng của len(L) thành viên.
    - L = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 8]
    - 31 thành viên

Suy ra:

- Một tập hợp (set) S gồm danh sách số phòng.
    - S = {1, 2, 3, 4, 5, 6, 8}
    - 7 phòng

Giả sử:

Mỗi phòng có đủ K giường để chứa K thành viên:

- 7 x 5 = 35 (giường)
- L = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8]

Nhưng, thực tế số lượng thành viên là 31 trong đó có 1 thuyền trưởng:

- 31 // 5 = 6 (Nhóm)
- Có một phòng còn trống K - 1 giường
- L = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 8, _, _, _, _]

Mỗi giường đều được đánh nhãn số theo số phòng:

- Tổng nhãn các giường của phòng đó chia cho K giường sẽ có được số phòng (1)
- (4 + 4 + 4 + 4 + 4) \\ 5 = 4

Trường hợp lý tưởng mỗi phòng có đủ giường để chứa K thành viên, tổng nhãn các giường là:

- $K \times \sum S = 5 \times 29 = 145$

Nhưng trong thực tế:

- $\sum L = 113$

Sự chênh lệch giữa lý tưởng và thực tế chính là tổng giá trị nhãn của những chiếc giường trống trong phòng Thuyền
trưởng:

- $145 - 113 = 32$

Theo (1), ta có:
- 32 \\ (K - 1) = 32 \\ 4 = 8

**Cách giải**

$$\text{Số phòng Thuyền trưởng} = \frac{(K \times \sum S) - \sum L}{K - 1}$$