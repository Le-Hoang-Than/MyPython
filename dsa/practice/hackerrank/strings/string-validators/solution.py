def validate_string(s):
    print(any(str(char).isalnum() for char in s))
    print(any(str(char).isalpha() for char in s))
    print(any(str(char).isnumeric() for char in s))
    print(any(str(char).islower() for char in s))
    print(any(str(char).isupper() for char in s))

if __name__ == '__main__':
    s = input()
    validate_string(s)