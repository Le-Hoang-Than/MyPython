def merge_the_tools(string, k):
    n = len(string)
    if 1 <= n <= 1e4 and \
            1 <= k <= n and \
            n % k == 0:
        for i in range(0, n, k):
            result=[]
            t = string[i:i + k]
            u ={}
            for j in t:
                u |= {j:j}
            result.extend(iter(u.values()))
            print(*result, sep='')


# your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
