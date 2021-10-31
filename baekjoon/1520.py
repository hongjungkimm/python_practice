import sys
sys.setrecursionlimit(10000)

def dfs(i, j):
    global visited
    
    if visited[i][j] == -1:
        visited[i][j] = 0
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < M and 0 <= nj < N:
                if area[i][j] > area[ni][nj]:
                    visited[i][j] += dfs(ni, nj)

    return visited[i][j]
    

M, N = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

di = [1, 0, 0, -1]
dj = [0, 1, -1, 0]
visited = [[-1] * N for _ in range(M)]
visited[M-1][N-1] = 1

print(dfs(0, 0))