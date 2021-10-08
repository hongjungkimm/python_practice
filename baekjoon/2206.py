import sys
from collections import deque

def bfs(i, j):
    queue = deque([[i, j, 1]])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[i][j][1] = 1

    while queue:
        x, y, s = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][s]
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < M:
                if maze[ni][nj] == '1' and s == 1:
                    visited[ni][nj][0] = visited[x][y][1] + 1
                    queue.append([ni, nj, 0])
                elif maze[ni][nj] == '0' and visited[ni][nj][s] == 0:
                    visited[ni][nj][s] = visited[x][y][s] + 1
                    queue.append([ni, nj, s])
    return -1


N, M = map(int, sys.stdin.readline().split())
maze = [[i for i in sys.stdin.readline().rstrip()] for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

print(bfs(0, 0))