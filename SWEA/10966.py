from collections import deque

def bfs(list1):
    queue = deque([list1])
    visited[list1[0]][list1[1]][list1[2]] = 0

    while queue:
        x, y, idx = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj][idx] == -1:
                    if ground[ni][nj] == 'L':
                        queue.appendleft([ni, nj, idx])
                        visited[ni][nj][idx] = visited[x][y][idx] + 1
                    else:
                        return visited[x][y][idx] + 1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ground = [[i for i in input()] for _ in range(N)]
    di = (-1, 1, 0, 0)
    dj = (0, 0, -1, 1)

    L_list = []
    cnt = -1
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 'L':
                cnt += 1
                L_list.append((i, j, cnt))

    visited = [[[-1] * (cnt + 1) for _ in range(M)] for _ in range(N)]

    result = 0
    for l in L_list:
        result += bfs(l)
        
    print('#{0} {1}'.format(tc, result))
