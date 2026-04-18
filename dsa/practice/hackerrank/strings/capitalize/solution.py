def solve(s):
    l = s
    new_word = True
    result= ''
    for i in l:
        if new_word and i.isalpha():
            result= result+ i.upper()
            new_word = False
            continue
        elif i == ' ':
            new_word = True
        else:
            new_word = False
        result= result+ i
    return result

if __name__ == '__main__':
    print(solve(input()))
