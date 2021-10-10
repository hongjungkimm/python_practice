import sys

def bfs(ti, tj):
    global check

    x, y = ti, tj
    while True:
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if rooms[ni][nj] - rooms[x][y] == 1:
                    x = ni
                    y = nj
                    check[rooms[ti][tj]] += 1
                    break
        else:
            return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    check = [1] * (N ** 2 + 1)
    for i in range(N):
        for j in range(N):
            bfs(i, j)

    for i in range(1, N ** 2 + 1):
        if check[i] == max(check):
            print('#{0} {1} {2}'.format(tc, i, max(check)))
            break