N, M = map(int, input().split())
const = 2
for t in range(N):  # 0 1 2 3 4
    if t < (N // 2):
        print(('.|.' * (t * 2 + 1)).center(M, '-'), sep="")
    elif t == (N // 2):
        print(('WELCOME').center(M, '-'))  # 5
    elif t > N // 2:  # 6 - 2 = 4 , 7 - 4 = 3, 8 - 6 = 2, 9 - 8 = 1, 10 - 10 = 0
        print(('.|.' * ((t - const) * 2 + 1)).center(M, '-'), sep="")
        const = const + 2

# for t in range(N // 2):  # 0 1 2 3 4
#     print(('.|.' * (t * 2 + 1)).center(M, '-'), sep="")
#
# print(('WELCOME').center(M, '-'))  # 5
#
# for b in range(N // 2 - 1, -1, -1): # 4 3 2 1 0. 6 - 2, 7 - 4, 8 - 6, 9 - 8, 10 - 10 =>
#     print(('.|.' * (b * 2 + 1)).center(M, '-'), sep="")
