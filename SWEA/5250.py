from collections import deque

def bfs(i, j):
    global result
    visited = [[float('inf')] * N for _ in range(N)]
    visited[0][0] = 0
    queue = deque([[0, 0]])

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ni = y + di[d]
            nj = x + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                plus = 1
                if area[ni][nj] > area[y][x]:
                    plus += area[ni][nj] - area[y][x]
                if visited[y][x] + plus < visited[ni][nj]:
                    visited[ni][nj] = visited[y][x] + plus
                    queue.append([ni, nj])
    return visited[N-1][N-1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    di = [1, 0, 0, -1]
    dj = [0, 1, -1, 0]
    result = bfs(0, 0)

    print('#{0} {1}'.format(tc, result))