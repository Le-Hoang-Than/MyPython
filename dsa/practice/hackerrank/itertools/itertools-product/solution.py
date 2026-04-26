from itertools import product


def cartesian(A, B):
    return product(A, B)


if __name__ == '__main__':
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    print(*list(product(A, B)))
