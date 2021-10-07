def select(r, total, check):
    global result
    if total <= result:
        return
    if sum(check) == N:
        result = max(total, result)
        return

    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            select(r+1, (total*percent[r][i])/100, check)
            check[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    result = 0
    select(0, 1, check)
    result = result * 100
    print('#{} {:.6f}'.format(tc, result))