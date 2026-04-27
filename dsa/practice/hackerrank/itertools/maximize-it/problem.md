# Maximize It!

Cho hàm số $f(X) = X^2$. Bạn cũng được cho $K$ danh sách. Danh sách thứ $i$ bao gồm $N_i$ phần tử.

Bạn phải chọn chính xác một phần tử từ mỗi danh sách sao cho giá trị của phương trình dưới đây là lớn nhất:$$S = (f(X_1) + f(X_2) + \dots + f(X_k)) \text{%} M$$

Trong đó:

$X_i$ là phần tử được chọn từ danh sách thứ $i$.

$S_{max}$ là giá trị lớn nhất tìm được.

Ký hiệu $\%$ (hoặc $\pmod M$) biểu thị phép toán chia lấy dư.

Lưu ý: Bạn cần chọn đúng một phần tử từ mỗi danh sách, không nhất thiết phải là phần tử lớn nhất. Bạn cộng bình phương của các phần tử đã chọn và thực hiện phép chia lấy dư cho $M$. Giá trị lớn nhất có thể đạt được chính là đáp án của bài toán.

**Input Format**

Dòng đầu tiên chứa 2 số nguyên cách nhau bởi dấu cách: $K$ (số lượng danh sách) và $M$ (số chia dư).

$K$ dòng tiếp theo, mỗi dòng bắt đầu bằng một số nguyên $N_i$ (số lượng phần tử trong danh sách thứ $i$), theo sau là $N_i$ số nguyên là các phần tử của danh sách đó.

**Constraints**

$1 \le K \le 7$

$1 \le M \le 1000$

$1 \le N_{i} \le 7$

$1 \le \text{Giá trị tuyệt đối của các phần tử trong danh sách} \le 10^9$

**Output Format**

In ra một số nguyên duy nhất là giá trị $S_{max}$ thu được.

**Sample Input**

```text
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
```

**Sample Output**

```text
206
```

**Explanation**

Việc chọn 5 từ danh sách thứ nhất, 9 từ danh sách thứ hai và 10 từ danh sách thứ ba sẽ cho giá trị S tối đa bằng $(5^2 + 9^2 + 10^2) \% 1000 = 206$.