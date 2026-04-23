def symmetric_difference(s1,s2):
    return len(s1^s2)


if __name__ == '__main__':
    n = int(input())
    s1 = set(map(int, input().split()))
    m = int(input())
    s2 = set(map(int, input().split()))
    print(symmetric_difference(s1,s2))
