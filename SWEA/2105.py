def dfs(i, j):
    stack = [[i, j, 0, 0, 1, 2, [cafe[i][j]]]]

    result = -1
    while stack:
        x, y, di_dir, dj_dir, di_cnt, dj_cnt, track = stack.pop()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if ni == i and nj == j:
                    if len(track) >= 4 and len(track) > result:
                        result = len(track)
                elif (di_dir == 0 and dj_dir == 0) and cafe[ni][nj] not in track:
                    stack.append([ni, nj, di[d], dj[d], di_cnt, dj_cnt, track + [cafe[ni][nj]]])
                else:
                    if cafe[ni][nj] not in track:
                        if di_dir == di[d]:
                            if dj_dir == dj[d]:
                                stack.append([ni, nj, di_dir, dj_dir, di_cnt, dj_cnt, track + [cafe[ni][nj]]])
                            else:
                                if dj_cnt >= 1:
                                    stack.append([ni, nj, di_dir, dj[d], di_cnt, dj_cnt - 1, track + [cafe[ni][nj]]])
                        else:
                            if di_cnt >= 1:
                                if dj_dir == dj[d]:
                                    stack.append([ni, nj, di[d], dj_dir, di_cnt - 1, dj_cnt, track + [cafe[ni][nj]]])
                                else:
                                    if dj_cnt >= 1:
                                        stack.append([ni, nj, di[d], dj[d], di_cnt - 1, dj_cnt - 1, track + [cafe[ni][nj]]])
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, -1, 1, 1]
    dj = [-1, 1, -1, 1]
    cnt = -1
    for i in range(N):
        for j in range(N):
            temp = dfs(i, j)
            if temp > cnt:
                cnt = temp

    print('#{0} {1}'.format(tc, cnt))
