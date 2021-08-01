import sys

N = int(sys.stdin.readline())

list1 = []
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        list1.append(command[1])
    elif command[0] == 'pop':
        if list1:
            print(list1.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(list1))
    elif command[0] == 'empty':
        if list1:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if list1:
            print(list1[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if list1:
            print(list1[-1])
        else:
            print(-1)
