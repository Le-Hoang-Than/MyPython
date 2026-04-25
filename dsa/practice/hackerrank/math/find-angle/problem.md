# Find Angle MBC

![](https://s3.amazonaws.com/hr-challenge-images/9668/1440151155-10b2b748ee-rsz_1438840048-2cf71ed69d-findangle.png)

Cho tam giác $ABC$ là một tam giác vuông tại $B$.

Do đó, $\angle ABC = 90^\circ$.

Điểm $M$ là **trung điểm** của cạnh huyền $AC$.

Bạn được cho biết độ dài của hai cạnh $AB$ và $BC$.

Nhiệm vụ của bạn là tìm số đo của góc $\angle MBC$ (ký hiệu là $\theta$ trong hình) theo đơn vị độ.

**Input Format**

* Dòng đầu tiên chứa độ dài cạnh $AB$.
* Dòng thứ hai chứa độ dài cạnh $BC$.

**Constraints**

* $0 < AB \le 100$
* $0 < BC \le 100$
* Độ dài $AB$ và $BC$ là các số tự nhiên.

**Output Format**

In ra giá trị của $\angle MBC$ theo đơn vị độ.
**Lưu ý:** Làm tròn góc đến số nguyên gần nhất.

**Examples:**

* Nếu góc là $56.5000001^\circ$, in ra `57°`.
* Nếu góc là $56.5000000^\circ$, in ra `57°`.
* Nếu góc là $56.4999999^\circ$, in ra `56°`.

$0^\circ < \theta^\circ < 90^\circ$

**Sample Input**

```text
10
10
```

**Sample Output**

```text
45°
```