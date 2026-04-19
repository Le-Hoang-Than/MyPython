# String Validators

Python có sẵn các phương thức kiểm tra chuỗi (string validation) cho các dữ liệu cơ bản. Nó có thể kiểm tra xem một
chuỗi được cấu tạo từ các ký tự chữ cái, chữ số, hay ký tự đặc biệt, v.v.

**str.isalnum()**

Phương thức này kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ cái và chữ số hay không (a-z, A-Z và 0-9).

```markdown
> > > print 'ab123'.isalnum()
True
> > > print 'ab123#'.isalnum()
False
```

**str.isalpha()**

Phương thức này kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ cái hay không (a-z và A-Z).

```markdown
> > > print 'abcD'.isalpha()
True
> > > print 'abcd1'.isalpha()
False
```

**str.isdigit()**

Phương thức này kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ số hay không (0-9).

```markdown
> > > print '1234'.isdigit()
True
> > > print '123edsd'.isdigit()
False
```

**str.islower()**

Phương thức này kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ viết thường hay không (a-z).

```markdown
> > > print 'abcd123#'.islower()
True
> > > print 'Abcd123#'.islower()
False
```

**str.isupper()**

Phương thức này kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ viết hoa hay không (A-Z).

```markdown
> > > print 'ABCD123#'.isupper()
True
> > > print 'Abcd123#'.isupper()
False
```

**Task**

Bạn được cho một chuỗi $S$.

Nhiệm vụ của bạn là tìm xem trong chuỗi $S$ có chứa: ký tự chữ cái và số (alphanumeric), ký tự chữ cái (alphabetical),
chữ số (digits), chữ cái viết thường (lowercase) và chữ cái viết hoa (uppercase) hay không.

**Input Format**

Một dòng duy nhất chứa chuỗi $S$.

**Constraints**

$0 < \text{len}(S) < 1000$

**Output Format**


Dòng 1: In ra True nếu $S$ có bất kỳ ký tự chữ cái hoặc số nào. Ngược lại, in False.

Dòng 2: In ra True nếu $S$ có bất kỳ ký tự chữ cái nào. Ngược lại, in False.

Dòng 3: In ra True nếu $S$ có bất kỳ chữ số nào. Ngược lại, in False.

Dòng 4: In ra True nếu $S$ có bất kỳ ký tự viết thường nào. Ngược lại, in False.

Dòng 5: In ra True nếu $S$ có bất kỳ ký tự viết hoa nào. Ngược lại, in False.

**Sample Input**

```markdown
qA2
```

**Sample Output**

```markdown
True
True
True
True
True
```