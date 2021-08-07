import sys
from collections import deque

N = int(sys.stdin.readline())

deque1 = deque(range(1, N+1))

while len(deque1) > 2:
    deque1.popleft()
    deque1.append(deque1[0])
    deque1.popleft()

if len(deque1) == 1:
    print(deque1[0])
else:
    deque1.popleft()
    print(deque1[0])