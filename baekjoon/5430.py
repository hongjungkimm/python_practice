import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    P = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    tmp = sys.stdin.readline().rstrip()
    c = tmp[1:-1].split(',')
    numbers = deque(c)
    
    cnt = 0
    error = False
    for p in P:
        if p == 'R':
            if cnt:
                cnt = 0
            else:
                cnt = 1
        else:
            if n == 0:
                error = True
                break
            elif numbers:
                if cnt:
                    numbers.pop()
                else:
                    numbers.popleft()
            else:
                error = True
                break
    if error:
        print('error')
    else:
        if cnt:
            numbers.reverse()
            print('[' + ','.join(numbers) + ']')
        else:
            print('[' + ','.join(numbers) + ']')