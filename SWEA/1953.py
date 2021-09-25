from collections import deque

def bfs(i, j):
    queue = deque([[i, j]])
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        flag = False
        for i in range(len(structure[tunnel[x][y]][0])):
            ni = x + structure[tunnel[x][y]][0][i]
            nj = y + structure[tunnel[x][y]][1][i]
            if 0 <= ni < N and 0 <= nj < M:
                if tunnel[ni][nj] != 0:
                    for j in range(len(structure[tunnel[ni][nj]][0])):
                        if structure[tunnel[x][y]][0][i] + structure[tunnel[ni][nj]][0][j] == 0 and structure[tunnel[x][y]][1][i] + structure[tunnel[ni][nj]][1][j] == 0:
                            if visited[ni][nj] == 0:
                                queue.append([ni, nj])
                                if visited[x][y] + 1 > L:
                                    flag = True
                                    break
                                visited[ni][nj] = visited[x][y] + 1
        if flag:
            break

    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                count += 1
    return count


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    structure = [
        [
            [0] # 0
        ],
        [
            [-1, 1, 0, 0], # 상 하 좌 우 1
            [0, 0, -1, 1]
        ],
        [
            [-1, 1], # 상 하 2
            [0, 0]
        ],
        [
            [0, 0], # 좌 우 3
            [-1, 1]
        ],
        [
            [-1, 0], # 상 우 4
            [0, 1]
        ],
        [
            [1, 0], # 하 우 5
            [0, 1]
        ],
        [
            [1, 0], # 하 좌 6
            [0, -1]
        ],
        [
            [-1, 0], # 상 좌 7
            [0, -1]
        ]
    ]

    print('#{0} {1}'.format(tc, bfs(R, C)))