# The Minion Game

Kevin và Stuart muốn chơi một trò chơi có tên là **'The Minion Game'**.

**Game Rules**

Cả hai người chơi đều được cho cùng một chuỗi ký tự $S$.
Cả hai phải tạo ra các chuỗi con (substring) từ các chữ cái của chuỗi $S$ đó.

* **Stuart** phải tạo ra các từ bắt đầu bằng **phụ âm (consonants)**.
* **Kevin** phải tạo ra các từ bắt đầu bằng **nguyên âm (vowels)**.

Trò chơi kết thúc khi cả hai người chơi đã tạo ra tất cả các chuỗi con có thể có.

**Scoring**

Người chơi được cộng `+1` điểm cho mỗi lần chuỗi con đó xuất hiện trong chuỗi $S$.

**For Example:**

Chuỗi $S$ = `BANANA`
Từ bắt đầu bằng nguyên âm của Kevin = `ANA`

Ở đây, `ANA` xuất hiện **2 lần** trong `BANANA`. Vì vậy, Kevin sẽ được **2 điểm**.

Để hiểu rõ hơn, hãy xem hình ảnh bên dưới:

![The Minion Game](https://s3.amazonaws.com/hr-challenge-images/9693/1450330231-04db904008-banana.png)

**Task**

Xác định người thắng cuộc và số điểm của họ.

**Function Description**

Hãy hoàn thành hàm `minion_game` trong trình soạn thảo.

Hàm `minion_game` có tham số sau:

* **string string:** chuỗi ký tự cần phân tích.

**Prints**

* Tên người thắng cuộc và điểm số của họ, cách nhau bởi dấu cách trên một dòng.
* Hoặc in ra `Draw` nếu không có người thắng cuộc (hòa).


**Input Format**

Một dòng duy nhất chứa chuỗi $S$.

*Lưu ý: Chuỗi $S$ sẽ chỉ chứa các ký tự in hoa $[A-Z]$.*

**Constraints**

$0 < \text{len(S)} \le 10^6$

**Sample Input**

```markdown
BANANA
```

**Sample Output**

```markdown
Stuart 12
```

**Ghi chú:** Các nguyên âm chỉ bao gồm: A, E, I, O, U. Trong bài toán này, chữ Y không được coi là nguyên âm.