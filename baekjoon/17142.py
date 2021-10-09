import sys
from itertools import combinations
from collections import deque

def bfs(list1):
    queue = deque([])
    visited = [[-1] * N for _ in range(N)]
    for l in list1:
        queue.append(l)
        visited[l[0]][l[1]] = 0
    
    for w in wall:
        visited[w[0]][w[1]] = 0
    
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == -1:
                    if lab[ni][nj] == 0:
                        queue.append([ni, nj])
                        visited[ni][nj] = visited[x][y] + 1
                    elif lab[ni][nj] == 2:
                        for d in range(4):
                            ti = ni + di[d]
                            tj = nj + dj[d]
                            if 0 <= ti < N and 0 <= tj < N:
                                if visited[ti][tj] == -1:
                                    queue.append([ni, nj])
                                    visited[ni][nj] = visited[x][y] + 1
    num = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:
                if visited[i][j] == -1:
                    return float('inf')
                else:
                    if visited[i][j] > num:
                        num = visited[i][j]
    return num


N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append([i, j])

wall = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 1:
            wall.append([i, j])

powerset = list(combinations(virus, M))
min_time = float('inf')
for p in powerset:
    temp = bfs(p)
    if temp < min_time:
        min_time = temp

if min_time == float('inf'):
    print(-1)
else:
    print(min_time)