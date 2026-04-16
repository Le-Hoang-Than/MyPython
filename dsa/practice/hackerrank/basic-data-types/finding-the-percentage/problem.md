# Finding the percentage

Đoạn mã mẫu được cung cấp sẽ đọc dữ liệu vào một Từ điển (Dictionary) chứa các cặp Khóa/Giá trị (Key/Value) theo định dạng name:[marks] của một nhóm sinh viên. Nhiệm vụ của bạn là in ra điểm trung bình của danh sách điểm tương ứng với tên sinh viên được yêu cầu, kết quả phải hiển thị đúng 2 chữ số sau dấu phẩy thập phân.

**Example**

Các cặp điểm key:value là:
- $'alpha'$: [20,30,40]
- $'beta'$: [30,50,70]

query_name = $'beta'$

Tên cần truy vấn (query_name) là 'beta'. Điểm trung bình của 'beta' là $(30 + 50 + 70) / 3 = 50.0$.

**Input Format**

- Dòng đầu tiên chứa số nguyên $n$, là số lượng hồ sơ sinh viên.
- $n$ dòng tiếp theo chứa tên và điểm số mà sinh viên đạt được, mỗi giá trị cách nhau bởi một khoảng trắng.
- Dòng cuối cùng chứa query_name, tên của sinh viên cần truy vấn.

**Constraints**

- $2 \le n \le 10$
- $0 \le \text{marks[i]} \le 100$
- Độ dài của mảng điểm = 3.

**Output Format**

In ra một dòng duy nhất: Điểm trung bình của sinh viên cụ thể đó, chính xác đến 2 chữ số thập phân.

**Sample Input 0**

```markdown
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

**Sample Output 0**

```markdown
56.00
```

**Explanation 0**

Điểm của Malika là {52, 56, 60}, với điểm trung bình là
$$\frac{52 + 56 + 60}{3} \Rightarrow 56$$ 

**Sample Input 1**

```markdown
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
```

**Sample Output 1**

```markdown
26.50
```