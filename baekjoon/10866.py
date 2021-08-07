import sys
from collections import deque

N = int(sys.stdin.readline())

deque1 = deque()
for _ in range(N):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'push_front':
        deque1.appendleft(command[1])
    elif command[0] == 'push_back':
        deque1.append(command[1])
    elif command[0] == 'pop_front':
        if deque1:
            print(deque1[0])
            deque1.popleft()
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deque1:
            print(deque1[-1])
            deque1.pop()
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deque1))
    elif command[0] == 'empty':
        if deque1:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if deque1:
            print(deque1[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if deque1:
            print(deque1[-1])
        else:
            print(-1)