from collections import Counter


def total_moneys(list_sizes, N):
    money = 0
    for _ in range(N):
        size, x = map(int, input().split())
        if list_sizes[size] > 0:
            money += x
            list_sizes[size] -= 1
    return money


if __name__ == '__main__':
    X = int(input())
    list_sizes = Counter(list(map(int, input().split())))
    N = int(input())

    print(total_moneys(list_sizes, N))
