T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 농장의 크기 N * N (N은 무조건 홀수)
    farm = [] # 농장을 리스트화 여기서 주의! 입력값에 공백이 없으므로 조심!
    for _ in range(N):
        tmp = []
        for i in input():
            tmp.append(int(i))
        farm.append(tmp)

    total = 0
    j = 0
    for i in range(N//2, -1, -1): # 가운데에서 위로
        total += sum(farm[i][j:N-j])
        j += 1

    j = 1
    for i in range(N//2+1, N): # 가운데의 하나 아래에서 끝으로
        total += sum(farm[i][j:N-j])
        j += 1

    print('#{0} {1}'.format(tc, total))