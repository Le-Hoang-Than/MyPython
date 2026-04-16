def find_score_second(record):
    min_score = min(scr for _, scr in record)
    second = float('inf')
    for _, scr in record:
        if min_score < scr < second:
            second = scr
    names = [name for name, score in record if score == second]
    return sorted(names)

if __name__ == '__main__':
    rc = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        rc.append([name,score])
    for i in find_score_second(rc):
        print(i)