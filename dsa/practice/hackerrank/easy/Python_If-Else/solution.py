def check_weird(n):
    if 1 <= n <= 100:
        is_even = (n % 2 == 0)

        if (not is_even) or (is_even and 6 <= n <= 20):
            return "Weird"
        elif (is_even and 2 <= n <= 5) or (is_even and n > 20):
            return "Not Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(check_weird(n))
