from collections import deque

def bfs(list1):
    queue = deque([list1])
    visited = [[-1] * M for _ in range(N)]
    visited[list1[0]][list1[1]] = 0

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == -1:
                    if ground[ni][nj] == 'L':
                        queue.appendleft([ni, nj])
                        visited[ni][nj] = visited[x][y] + 1
                    else:
                        return visited[x][y] + 1


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ground = [[i for i in input()] for _ in range(N)]

    L_list = []
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 'L':
                L_list.append([i, j])

    result = 0
    for l in L_list:
        result += bfs(l)

    print('#{0} {1}'.format(tc, result))