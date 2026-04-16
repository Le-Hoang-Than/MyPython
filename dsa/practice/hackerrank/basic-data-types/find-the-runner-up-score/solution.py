def find_the_runner_up_score(lst):
    max_score = max(lst)
    second = float('-inf')
    for scr in lst:
        if scr != max_score and scr > second:
            second = scr

    return second


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(find_the_runner_up_score(list(arr)))
