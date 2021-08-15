T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cases = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stops = [int(input()) for _ in range(P)]
    stops_cnt = [0 for _ in range(P)]

    for i in range(len(cases)):
        for j in range(len(stops)):
            if cases[i][0] <= stops[j] <= cases[i][1]:
                stops_cnt[j] += 1

    print('#{0} {1}'.format(tc, ' '.join(list(map(str, stops_cnt)))))