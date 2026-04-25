if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(pow(a, b), pow(a, b, mod=int(input())), sep='\n')
