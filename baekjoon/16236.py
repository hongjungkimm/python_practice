import sys # 실패
from collections import deque

def bfs(ti, tj):
    queue = deque([[ti, tj]])
    di = [-1, 0, 0, 1]
    dj = [0, -1, 1, 0]
    cnt = 0
    n = 2
    n_cnt = 0
    while True:
        x, y = queue.popleft()
        space[x][y] = 0
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni <= N - 1 and 0 <= nj <= N - 1:
                if 1 <= space[ni][nj] < n:
                    queue.append([ni, nj])
                    cnt += 1
                    n_cnt += 1
                    if n == n_cnt:
                        n += 1
                        n_cnt = 0
                    break
                elif space[ni][nj] == 0 or space[ni][nj] == n:
                    queue.append([ni, nj])
                    cnt += 1
                    break

        tmp = 0
        flag = False
        for i in range(N):
            for j in range(N):
                if 1 <= space[i][j] < n:
                    tmp += 1
                    flag = True
                    break
            if flag:
                break
        if tmp == 0:
            return cnt

N = int(sys.stdin.readline())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

si = sj = 0
can_eat = 0
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            si, sj = i, j
        if 1 <= space[i][j] < 2:
            can_eat += 1

if can_eat:
    print(bfs(si, sj))
else:
    print(can_eat)
