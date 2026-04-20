import string
from itertools import count


def print_rangoli(size):
    # # Tạo danh sách chữ cái từ 'a' đến ký tự thứ 'size' và đảo ngược lại
    # alphabet = list(string.ascii_lowercase[:size])
    # alphabet.reverse()
    #
    # width = 4 * size - 3
    #
    # # Chạy từ 0 đến 2*size - 2 (tổng cộng 2*size - 1 dòng)
    # for c in range(2 * size - 1):
    #     if c < size:
    #         # Nửa trên và dòng giữa
    #         left_row = [alphabet[i] for i in range(c + 1)]
    #         right_row = [alphabet[i] for i in range(c - 1, -1, -1)]
    #     else:
    #         # Nửa dưới: lấy đối xứng của chỉ số
    #         # Khi c = size, nó sẽ giống dòng c = size - 2
    #         idx = 2 * size - 2 - c
    #         left_row = [alphabet[i] for i in range(idx + 1)]
    #         right_row = [alphabet[i] for i in range(idx - 1, -1, -1)]
    #
    #     row = '-'.join(left_row + right_row)
    #     print(row.center(width, '-'))
    # 1. Lấy danh sách chữ cái (a, b, c, ...)
    alphabet = string.ascii_lowercase

    # 2. Xác định các chữ cái sẽ dùng cho kích thước 'size'
    chars = alphabet[:size]

    lines = []

    # 3. Tạo nửa trên và dòng giữa (từ dòng 0 đến size-1)
    for i in range(size):
        # Lấy các chữ cái cho dòng hiện tại, đảo ngược chúng rồi ghép lại
        # Ví dụ dòng cuối (i=size-1): 'edcba' + 'bcde'
        left_side = chars[size - 1: i: -1]
        right_side = chars[i: size]
        row_chars = list(left_side + right_side)

        # Nối các chữ cái bằng dấu gạch ngang '-'
        row_string = "-".join(row_chars)

        # Căn giữa dòng với độ rộng là 4*size - 3
        width = 4 * size - 3
        lines.append(row_string.center(width, "-"))

    # 4. Tạo hình Rangoli hoàn chỉnh bằng cách ghép nửa trên và nửa dưới (đối xứng)
    # Nửa dưới là bản sao ngược của nửa trên (bỏ dòng cuối cùng vì nó là dòng giữa)
    final_rangoli = lines[::-1] + lines[1:]

    print('\n'.join(final_rangoli))


if __name__ == '__main__':
    n = int(input())

    print_rangoli(n)
