def captains_room(beds, K):
    return (K * sum(set(beds)) - sum(beds)) // (K - 1)


if __name__ == '__main__':
    K = int(input())
    beds = list(map(int, input().split()))
    print(beds)
    print(captains_room(beds, K))