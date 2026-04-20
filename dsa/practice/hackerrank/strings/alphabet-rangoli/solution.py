import string
from itertools import count


def print_rangoli(size):
    alphabet = list(string.ascii_lowercase[:n])
    alphabet.reverse()
    count = 0
    for c in range(n * 2):
        if c < n:
            left_row = [alphabet[i] for i in range(c + 1)]
            right_row = [alphabet[i] for i in range(c - 1, -1, -1)]
            row = '-'.join(left_row + right_row)
            print(row.center(n * 3 + (n - 3), '-'), sep='')
        elif c > n:
            count += 2
            left_row = [alphabet[b] for b in range(c - count - 1)]
            right_row = [alphabet[b] for b in range(c - 1 - count, -1, -1)]
            row = '-'.join(left_row + right_row)
            print(row.center(n * 3 + (n - 3), '-'), sep='')

if __name__ == '__main__':
    n = int(input())

    print_rangoli(n)
