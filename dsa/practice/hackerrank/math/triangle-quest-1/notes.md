# Notes

---

## Triangle Quest

**Mục tiêu bài toán:**

- Chỉ bằng cách sử dụng các phép toán số học
- in ra một tam giác số có chiều cao $N - 1$

**Ý tưởng:**

- Mỗi số  $i (1 ... N - 1)$ dòng tương ứng với một đơn vị:
    - hàng đơn vị: 1
    - hàng chục: 10
    - hàng trăm: 100
    - hàng nghìn: 1000
    - ....
- Mỗi dòng đều là bội số của chính dòng i đó. đặt i ra ngoài
    - 1 * 1
    - 2 * 11
    - 3 * 111
    - 4 * 1111

Cần tính một hằng số const sao cho i * const:

- Lấy hàng đơn vị của dòng đó bằng cách $10^i$:
    - 10
    - 100
    - 1000
    - 10000
    - ...

Nhưng đơn vị lớn hơn so với const cần tính, hạ xuống 1 đơn vị:

- 9
- 99
- 999
- 9999
- ...

Ước chung của const là 9, ta sẽ có được const cần tìm:
- 1 = 9 / 9
- 11 = 99 / 9
- 111 = 999 / 9
- 1111 = 9999 / 9
- ...

Vậy công thức của hằng số $const = \frac{(10^i - 1)}{9}$

Với $i$ là số dòng
