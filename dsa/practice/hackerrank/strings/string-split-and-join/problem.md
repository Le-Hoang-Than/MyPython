# String Split and Join

Trong Python, một chuỗi có thể được tách ra dựa trên một ký tự phân cách (delimiter).

**Example:**

```markdown
>>> a = "this is a string"
>>> a = a.split(" ") # 'a' được chuyển thành một danh sách các chuỗi con.
>>> print(a)
['this', 'is', 'a', 'string']
```

Việc nối các chuỗi lại cũng rất đơn giản:

```markdown
>>> a = "-".join(a)
>>> print(a)
this-is-a-string
```

**Task**

Bạn được cho một chuỗi ký tự. Hãy tách chuỗi đó dựa trên ký tự phân cách là khoảng trắng (" ") và nối lại bằng dấu gạch ngang ("-").

**Function Description**

Hãy hoàn thành hàm `split_and_join` trong trình soạn thảo.

Hàm `split_and_join` có tham số sau:
- string line: một chuỗi bao gồm các từ cách nhau bởi khoảng trắng.

**Returns**

- string: chuỗi kết quả sau khi đã được nối lại bằng dấu gạch ngang.

**Input Format**

Một dòng duy nhất chứa chuỗi các từ cách nhau bởi khoảng trắng.

**Sample Input**

```markdown
this is a string
```

**Sample Output**

```markdown
this-is-a-string
```