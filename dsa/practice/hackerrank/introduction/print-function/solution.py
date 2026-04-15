def func(number):
    if 1<= number <= 150:
        func(number - 1)
        print(number, end="")
    return

if __name__ == '__main__':
    n = int(input())
    func(n)