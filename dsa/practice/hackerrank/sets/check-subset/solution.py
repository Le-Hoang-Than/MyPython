def sub_set(A,B):
    return A.issubset(B)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        A = set(map(int, input().split()))
        m = int(input())
        B = set(map(int, input().split()))
        print(sub_set(A, B))