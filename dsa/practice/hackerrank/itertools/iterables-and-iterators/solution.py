import itertools


def probability(n, l, k):
    c = list(itertools.combinations(range(n), k))
    count = sum(any((l[j] == 'a' for j in i)) for i in c)
    return round(count / len(c), 4)


if __name__ == '__main__':
    n = int(input())
    l = list(map(str, input().split()))
    k = int(input())
    print(probability(n,l,k))