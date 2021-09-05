import sys
from collections import deque

def bfs(ti, tj):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    queue = deque([[ti, tj]])
    space[ti][tj] = 0
    space_copy[ti][tj] = cnt
    tmp = 1
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < N and space[ni][nj] == 1:
                queue.append([ni, nj])
                space[ni][nj] = 0
                space_copy[ni][nj] = cnt
                tmp += 1

    return tmp

N = int(sys.stdin.readline())
space = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(N)]

space_copy = [[0] * N for _ in range(N)]
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if space[i][j] == 1:
            cnt += 1
            result.append(bfs(i, j))

print(cnt)
result.sort()
for r in result:
    print(r)
            