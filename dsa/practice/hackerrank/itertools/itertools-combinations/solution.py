import itertools


def combinations(s, k):
    return list(itertools.combinations(s, k))


if __name__ == '__main__':
    s, k = input().split()
    for i in range(1, int(k) + 1):
        for combination in combinations(sorted(s), i):
            print(''.join(combination))
