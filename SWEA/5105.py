T = int(input())

def search_maze(ti, tj, path): # path를 글로벌로 다시
    global result
    dij = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상 하 좌 우
    for di, dj in dij:
        ni = ti + di
        nj = tj + dj
        if 0 <= ni <= N - 1 and 0 <= nj <= N - 1:
            if maze[ni][nj] == 0:
                maze[ni][nj] = 4
                search_maze(ni, nj, path + [[ni, nj]])
            elif maze[ni][nj] == 3:
                result = path
                return result

for tc in range(1, T+1):
    N = int(input())
    maze = []
    for _ in range(N):
        tmp = []
        for i in input():
            tmp.append(int(i))
        maze.append(tmp)

    si = 0
    sj = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j

    result = []
    search_maze(si, sj, [[si, sj]])
    total_result = len(result) - 1
    if total_result < 0:
        total_result = 0
    print('#{0} {1}'.format(tc, total_result))