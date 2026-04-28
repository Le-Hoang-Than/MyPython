# collections.Counter()

Một Counter là một vùng chứa (container) lưu trữ các phần tử dưới dạng các khóa (keys) của từ điển và số lần xuất hiện của chúng được lưu trữ dưới dạng các giá trị (values) của từ điển.

**Sample Code**

```text
>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
```

**Task**

Raghu là chủ một cửa hàng giày. Cửa hàng của anh ấy có $X$ số lượng giày.

Anh ấy có một danh sách chứa kích cỡ của từng đôi giày đang có trong cửa hàng.

Có $N$ khách hàng sẵn sàng trả một số tiền $x$ chỉ khi họ mua được đôi giày đúng kích cỡ mong muốn.

Nhiệm vụ của bạn là tính toán tổng số tiền mà Raghu đã kiếm được.

**Input Format**

Dòng đầu tiên chứa $X$, số lượng giày.

Dòng thứ hai chứa danh sách các kích cỡ giày hiện có trong cửa hàng, cách nhau bởi dấu cách.

Dòng thứ ba chứa $N$, số lượng khách hàng.

$N$ dòng tiếp theo, mỗi dòng chứa các giá trị cách nhau bởi dấu cách gồm: kích cỡ giày khách hàng muốn và giá tiền của đôi giày đó.

**Constraints**

$0 < X < 10^3$

$0 < N \le 10^3$

$20 < \text{giá tiền} < 100$

$2 < \text{kích cỡ giày} < 20$

**Output Format**

In ra tổng số tiền Raghu kiếm được.

**SAmple Input**

```text
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
```

**Sample Output**

```text
200
```

**Explanation**

Khách hàng 1: Mua giày cỡ 6 với giá $55.

Khách hàng 2: Mua giày cỡ 6 với giá $45.

Khách hàng 3: Cỡ 6 không còn hàng (đã bán hết cho 2 người trước), nên không mua được.

Khách hàng 4: Mua giày cỡ 4 với giá $40.

Khách hàng 5: Mua giày cỡ 18 với giá $60.

Khách hàng 6: Cỡ 10 không có sẵn trong kho, nên không mua được.

Tổng số tiền kiếm được = $55 + 45 + 40 + 60 = 200$.