T = int(input())

for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]

    times = sorted(times, key=lambda x: x[1])
    idx = 0
    cnt = 1
    while True:
        for i in range(idx+1, N):
            if times[i][0] >= times[idx][1]:
                idx = i
                cnt += 1
        else:
            break

    print('#{0} {1}'.format(tc, cnt))
