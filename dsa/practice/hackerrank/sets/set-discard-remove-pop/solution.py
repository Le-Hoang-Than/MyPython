def execute_command(set,cmd_list):
    for i in range(len(cmd_list)):
        cmd = cmd_list[i]
        match cmd[0]:
            case 'discard':
                set.discard(int(cmd[1]))
            case 'remove':
                set.remove(int(cmd[1]))
            case 'pop':
                set.pop()
    return sum(set)

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    cmd_list= [input().split() for _ in range(N)]
    print(execute_command(s,cmd_list))