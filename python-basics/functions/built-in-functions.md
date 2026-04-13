### Built-in Functions

| Hàm                | Mô tả                                                                                                     |
|:-------------------|:----------------------------------------------------------------------------------------------------------|
| **abs()**          | Trả về giá trị tuyệt đối của một số.                                                                      |
| **all()**          | Trả về True nếu tất cả các phần tử trong một đối tượng lặp (iterable) là đúng.                            |
| **any()**          | Trả về True nếu bất kỳ phần tử nào trong một đối tượng lặp là đúng.                                       |
| **ascii()**        | Trả về phiên bản có thể đọc được của một đối tượng. Thay thế các ký tự không phải ASCII bằng ký tự thoát. |
| **bin()**          | Trả về dạng nhị phân của một số.                                                                          |
| **bool()**         | Trả về giá trị Boolean của đối tượng được chỉ định.                                                       |
| **bytearray()**    | Trả về một mảng các byte.                                                                                 |
| **bytes()**        | Trả về một đối tượng bytes.                                                                               |
| **callable()**     | Trả về True nếu đối tượng có thể gọi được, ngược lại là False.                                            |
| **chr()**          | Trả về ký tự từ mã Unicode được chỉ định.                                                                 |
| **classmethod()**  | Chuyển đổi một phương thức thành phương thức lớp (class method).                                          |
| **compile()**      | Trả về nguồn được chỉ định dưới dạng một đối tượng, sẵn sàng để thực thi.                                 |
| **complex()**      | Trả về một số phức.                                                                                       |
| **delattr()**      | Xóa thuộc tính (đặc tính hoặc phương thức) khỏi đối tượng.                                                |
| **dict()**         | Trả về một từ điển (Dictionary).                                                                          |
| **dir()**          | Trả về danh sách các thuộc tính và phương thức của đối tượng.                                             |
| **divmod()**       | Trả về thương số và số dư của phép chia.                                                                  |
| **enumerate()**    | Trả về một đối tượng liệt kê (kèm chỉ số).                                                                |
| **eval()**         | Đánh giá và thực thi một biểu thức.                                                                       |
| **exec()**         | Thực thi mã (hoặc đối tượng) được chỉ định.                                                               |
| **filter()**       | Sử dụng hàm lọc để loại bỏ các phần tử trong đối tượng lặp.                                               |
| **float()**        | Trả về một số thực dấu phẩy động.                                                                         |
| **format()**       | Định dạng một giá trị cụ thể.                                                                             |
| **frozenset()**    | Trả về một đối tượng frozenset.                                                                           |
| **getattr()**      | Trả về giá trị của thuộc tính được chỉ định.                                                              |
| **globals()**      | Trả về bảng ký hiệu toàn cục hiện tại dưới dạng từ điển.                                                  |
| **hasattr()**      | Trả về True nếu đối tượng có thuộc tính được chỉ định.                                                    |
| **hash()**         | Trả về giá trị băm của đối tượng.                                                                         |
| **help()**         | Thực thi hệ thống trợ giúp tích hợp sẵn.                                                                  |
| **hex()**          | Chuyển đổi một số thành giá trị thập lục phân.                                                            |
| **id()**           | Trả về định danh (ID) của một đối tượng.                                                                  |
| **input()**        | Cho phép người dùng nhập dữ liệu.                                                                         |
| **int()**          | Trả về một số nguyên.                                                                                     |
| **isinstance()**   | Trả về True nếu đối tượng là một thực thể của lớp được chỉ định.                                          |
| **issubclass()**   | Trả về True nếu một lớp là lớp con của lớp khác.                                                          |
| **iter()**         | Trả về một đối tượng trình lặp (iterator).                                                                |
| **len()**          | Trả về độ dài (số lượng phần tử) của một đối tượng.                                                       |
| **list()**         | Trả về một danh sách (list).                                                                              |
| **locals()**       | Trả về bảng ký hiệu cục bộ hiện tại.                                                                      |
| **map()**          | Áp dụng một hàm cho tất cả phần tử trong trình lặp.                                                       |
| **max()**          | Trả về phần tử lớn nhất.                                                                                  |
| **memoryview()**   | Trả về một đối tượng xem bộ nhớ.                                                                          |
| **min()**          | Trả về phần tử nhỏ nhất.                                                                                  |
| **next()**         | Trả về phần tử tiếp theo trong trình lặp.                                                                 |
| **object()**       | Trả về một đối tượng mới cơ bản.                                                                          |
| **oct()**          | Chuyển đổi một số thành hệ bát phân.                                                                      |
| **open()**         | Mở một tệp và trả về đối tượng tệp.                                                                       |
| **ord()**          | Chuyển ký tự thành số nguyên đại diện cho mã Unicode.                                                     |
| **pow()**          | Trả về x lũy thừa y (x^y).                                                                                |
| **print()**        | In ra thiết bị đầu ra tiêu chuẩn.                                                                         |
| **property()**     | Lấy, thiết lập hoặc xóa một đặc tính.                                                                     |
| **range()**        | Tạo ra một dãy số.                                                                                        |
| **repr()**         | Trả về phiên bản có thể đọc được (dạng đại diện) của đối tượng.                                           |
| **reversed()**     | Trả về một trình lặp đã đảo ngược.                                                                        |
| **round()**        | Làm tròn một số.                                                                                          |
| **set()**          | Trả về một tập hợp (set) mới.                                                                             |
| **setattr()**      | Thiết lập giá trị cho thuộc tính của đối tượng.                                                           |
| **slice()**        | Trả về một đối tượng cắt (slice).                                                                         |
| **sorted()**       | Trả về một danh sách đã được sắp xếp.                                                                     |
| **staticmethod()** | Chuyển đổi một phương thức thành phương thức tĩnh.                                                        |
| **str()**          | Trả về một đối tượng chuỗi.                                                                               |
| **sum()**          | Tính tổng các phần tử của một trình lặp.                                                                  |
| **super()**        | Trả về một đối tượng đại diện cho lớp cha.                                                                |
| **tuple()**        | Trả về một bộ dữ liệu (tuple).                                                                            |
| **type()**         | Trả về kiểu dữ liệu của một đối tượng.                                                                    |
| **vars()**         | Trả về thuộc tính __dict__ của một đối tượng.                                                             |
| **zip()**          | Kết hợp các trình lặp lại với nhau.                                                                       |