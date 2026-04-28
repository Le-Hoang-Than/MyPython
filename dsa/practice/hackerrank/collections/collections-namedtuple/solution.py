from collections import namedtuple

if __name__ == '__main__':
    N, students_list = int(input()), namedtuple('students_list', input().split())
    marks = [int(students_list(*list(input().split())).MARKS) for _ in range(N)]
    print(f'{sum(marks) / N:.2f}')
