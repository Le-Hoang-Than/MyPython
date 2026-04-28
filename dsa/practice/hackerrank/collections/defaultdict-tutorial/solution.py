from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    A = defaultdict(list)
    for i in range(1, n + 1):
        A[input()].append(str(i))
    B = defaultdict(list)
    for _ in range(m):
        word = input()
        if word in A:
            print(' '.join(A[word]))
        else:
            print('-1')
