def captains_room(rooms):
    return (K * sum(set(rooms)) - sum(rooms)) // (K - 1)


if __name__ == '__main__':
    K = int(input())
    rooms = list(map(int, input().split()))
    print(captains_room(rooms))