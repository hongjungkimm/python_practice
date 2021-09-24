def dfs(i, j, k, ans):
    global answer

    for d in range(4):
        x = i + di[d]
        y = j + dj[d]

        if 0 <= x < N and 0 <= y < N and not visited[x][y]:
            if mountain[i][j] > mountain[x][y]:
                visited[x][y] = True
                dfs(x, y, k, ans + 1)
                visited[x][y] = False
            elif k and mountain[i][j] > mountain[x][y] - k:
                restore = mountain[x][y]
                for cut in range(1, k+1):
                    mountain[x][y] = mountain[i][j] - cut
                    visited[x][y] = True
                    dfs(x, y, 0, ans + 1)
                    mountain[x][y] = restore
                    visited[x][y] = False

    if answer < ans:
        answer = ans


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    answer = 0

    max_high = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_high:
                max_high = mountain[i][j]

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_high:
                visited[i][j] = True
                dfs(i, j, K, 1)
                visited[i][j] = False

    print('#{} {}'.format(tc, answer))