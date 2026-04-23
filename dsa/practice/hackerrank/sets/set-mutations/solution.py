def exc_cmd(A, N, cmd_lst):
    match cmd_lst[0]:
        case 'intersection_update':
            A.intersection_update(N)
        case 'symmetric_difference_update':
            A.symmetric_difference_update(N)
        case 'difference_update':
            A.difference_update(N)
        case 'update':
            A.update(N)


if __name__ == '__main__':
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        cmd_lst = input().split()
        N = set(map(int, input().split()))
        exc_cmd(A, N, cmd_lst)
    print(sum(A))