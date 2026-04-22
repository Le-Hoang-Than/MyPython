def symmetric_difference(a, b):
    return sorted(a.symmetric_difference(b))


if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    c = symmetric_difference(a, b)
    print(*c,sep='\n')

