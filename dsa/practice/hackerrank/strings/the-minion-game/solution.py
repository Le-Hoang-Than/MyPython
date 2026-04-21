def minion_game(string):
    sub_string = {}
    # for i in range(len(string)):
    #     for j in range(i + 1, len(string) + 1):
    #         if string[i:j] not in sub_string and string[i:j].isupper():
    #             sub_string.append(string[i:j])

    # sub_string = {string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)}

    # for i in range(len(string)):
    #     for j in range(i + 1, len(string) + 1):
    #         sub = string[i:j]
    #         # Nếu đã thấy chuỗi này rồi, chỉ cần cộng thêm 1
    #         if sub in sub_string:
    #             sub_string[sub] += 1
    #         else:
    #             sub_string[sub] = 1

    kevins_score = 0
    stuarts_score = 0
    n = len(string)
    for i in range(n):
        if string[i] in 'AEIOU':
            kevins_score += (n - i)
        else:
            stuarts_score += (n - i)

    # for i in sub_string:
    #     count = 0
    #     start = 0
    #     while True:
    #         start = string.find(i, start)
    #         if start == -1:
    #             break
    #         count += 1
    #         start += 1
    #     if i[0] in ['A', 'E', 'I', 'O', 'U']:
    #         kevins_score += sub_string[i]
    #     else:
    #         stuarts_score += sub_string[i]

    if kevins_score > stuarts_score:
        print(f'Kevin {kevins_score}')
    elif stuarts_score > kevins_score:
        print(f'Stuart {stuarts_score}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
