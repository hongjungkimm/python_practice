def dfs(i, j, d):
    global result
    if i == N-1 and j == N-1:
        result.append(d)
        return
    else:
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if d+area[ni][nj] < min(result):
                    dfs(ni, nj, d+area[ni][nj])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1]
    dj = [1, 0]

    result = [(13+12)*10]
    dfs(0, 0, area[0][0])

    print('#{0} {1}'.format(tc, min(result)))