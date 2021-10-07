def select(r, total, check):
    global result
    if total >= result:
        return
    if sum(check) == N:
        result = min(total, result)
        return

    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            select(r+1, total+cost[r][i], check)
            check[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    result = N * 99
    select(0, 0, check)

    print('#{0} {1}'.format(tc, result))