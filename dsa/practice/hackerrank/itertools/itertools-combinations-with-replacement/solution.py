import itertools

def combinations_with_replacement(s, k):
    return list(itertools.combinations_with_replacement(s,k))

if __name__ == '__main__':
    s, k = input().split()
    for i in combinations_with_replacement(sorted(s), int(k)):
        print(''.join(i))