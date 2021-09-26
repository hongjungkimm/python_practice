import sys # 실패....
from itertools import combinations

N, L = map(int, sys.stdin.readline().split())

result = tuple()
flag = False
for i in range(L, 101):
    for j in combinations(list(range(0, N+1)), i):
        if sum(j) == N and len(j) >= 2 and 100 >= len(j):
            for k in range(len(j)-1):
                if j[k+1] - j[k] != 1:
                    break
            else:
                result = j
                flag = True
                break
    if flag:
        break

if result:
    print(*result)
else:
    print(-1)