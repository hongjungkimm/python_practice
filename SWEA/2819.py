def bfs(ti, tj, string):
    global result
    global visited

    if len(string) == 7:
        result.append(string)
        return

    for d in range(4):
        ni = ti + di[d]
        nj = tj + dj[d]
        if 0 <= ni < 4 and 0 <= nj < 4:
            if string + grid[ni][nj] not in result:
                if len(string + grid[ni][nj]) <= 7:
                    visited[ni][nj] = True
                    bfs(ni, nj, string + grid[ni][nj])
                    visited[ni][nj] = False


T = int(input())

for tc in range(1, T+1):
    grid = [list(map(str, input().split())) for _ in range(4)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    visited = [[False] * 4 for _ in range(4)]
    result = []
    for i in range(4):
        for j in range(4):
            visited[i][j] = True
            bfs(i, j, grid[i][j])
            visited[i][j] = False

    print('#{0} {1}'.format(tc, len(result)))