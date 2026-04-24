def happy_score(A, B, array):
    score = 0
    for i in range(len(array)):
        if array[i] in A:
            score += 1
        elif array[i] in B:
            score -= 1
    return score


if __name__ == '__main__':
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    print(happy_score(A, B, array))
