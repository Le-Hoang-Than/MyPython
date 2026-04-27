import itertools


def compress_the_string(s):
    return [(len(list(g)), k) for k, g in itertools.groupby(s, None)]


if __name__ == '__main__':
    s = list(map(int, input()))
    print(*compress_the_string(s))
