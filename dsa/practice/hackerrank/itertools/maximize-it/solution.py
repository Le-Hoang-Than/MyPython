import itertools


def maximize(l, m):
    c = itertools.product(*l)
    results = [sum(x ** 2 for x in combo) % m for combo in c]
    return max(results)


if __name__ == '__main__':
    k, m = map(int, input().split())
    l = [list(map(int, input().split()))[1:] for _ in range(k)]
    print(maximize(l, m))
