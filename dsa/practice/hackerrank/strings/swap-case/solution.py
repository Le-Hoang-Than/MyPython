def swap_case(string):
    # rslt = ""
    # for i in string:
    #     if i.isupper():
    #         rslt += i.lower()
    #     elif i.islower():
    #         rslt += i.upper()
    #     else:
    #         rslt += i
    # return rslt
    return string.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
