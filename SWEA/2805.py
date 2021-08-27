T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = []
    for _ in range(N):
        tmp = []
        for i in input():
            tmp.append(int(i))
        farm.append(tmp)

    total = 0
    j = 0
    for i in range(N//2, -1, -1):
        total += sum(farm[i][j:N-j])
        j += 1

    j = 1
    for i in range(N//2+1, N):
        total += sum(farm[i][j:N-j])
        j += 1

    print('#{0} {1}'.format(tc, total))