import itertools


def permutations(string, k):
    return list(itertools.permutations(string, k))


if __name__ == '__main__':
    string, k = input().split()
    for i in permutations(sorted(string), int(k)):
        print(''.join(i))
