import sys
from collections import deque

def bfs(i, j):
    di = [1, 0, 0, -1]
    dj = [0, 1, -1, 0]
    visited = [[-1] * M for _ in range(N)]
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 0
    result = []
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < M:
                if maze[ni][nj] == 1 and visited[ni][nj] == -1:
                    queue.append([ni, nj])
                    visited[ni][nj] = visited[x][y] + 1
                if ni == N - 1 and nj == M - 1:
                    result.append(visited[x][y] + 1)
    return min(result) + 1


N, M = map(int, sys.stdin.readline().split())

maze = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(N)]

print(bfs(0, 0))