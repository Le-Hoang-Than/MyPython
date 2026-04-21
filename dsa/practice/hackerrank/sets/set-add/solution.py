# Enter your code here. Read input from STDIN. Print output to STDOUT
def total_stamps(array):
    return len(array)

if __name__ == '__main__':
    n = int(input())
    s = {input() for _ in range(n)}
    print(total_stamps(s))