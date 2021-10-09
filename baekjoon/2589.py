import sys
from collections import deque

def bfs(ti, tj):
    queue = deque([[ti, tj]])
    visited = [[-1] * w for _ in range(h)]
    visited[ti][tj] = 0

    result = 0
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < h and 0 <= nj < w:
                if visited[ni][nj] == -1 and maze[ni][nj] == 'L':
                    queue.append([ni, nj])
                    visited[ni][nj] = visited[x][y] + 1
                    result = max(result, visited[ni][nj])
    
    return result

h, w = map(int, sys.stdin.readline().split())
maze = [[i for i in sys.stdin.readline().rstrip()] for _ in range(h)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
max_num = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == 'L':
            max_num = max(max_num, bfs(i, j))

print(max_num)