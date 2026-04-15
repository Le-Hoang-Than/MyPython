def exe_cmd(command_list):
    lst = []
    for prt in command_list:
        cmd = prt.split()
        match cmd[0]:
            case "insert":
                lst.insert(int(cmd[1]), int(cmd[2]))
            case "print":
                print(lst)
            case "remove":
                lst.remove(int(cmd[1]))
            case "append":
                lst.append(int(cmd[1]))
            case "sort":
                lst.sort()
            case "pop":
                lst.pop()
            case "reverse":
                lst.reverse()


if __name__ == '__main__':
    N = int(input())
    cmd_lst = [input() for _ in range(N)]
    exe_cmd(cmd_lst)