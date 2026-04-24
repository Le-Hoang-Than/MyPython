def check_strict_superset(A, B):
    # return A | B == A and len(A - B) > 0
    return A > B and len(A.difference(B)) > 0

if __name__ == '__main__':
    A = set(map(int, input().split()))
    result = True
    for _ in range(int(input())):
        B = set(map(int, input().split()))
        if (check_strict_superset(A, B) == False):
            result = False
            break
    print(result)