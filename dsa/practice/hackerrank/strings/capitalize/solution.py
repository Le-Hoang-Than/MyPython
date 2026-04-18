def solve(s):
    words_list = s.split()
    result = []
    for word in words_list:
        if str(word[0]).isalpha():
            result.append(str(word[0]).upper() + word[1:])
            print(result)
        else:
            result.append(word)
    return " ".join(result)


if __name__ == '__main__':
    print(solve(input()))
