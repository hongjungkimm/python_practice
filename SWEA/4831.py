T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    charge_stop = [0] * (N + 1) # 충전소가 설치된 정류장 인덱스 표시 리스트
    for i in range(M):
        charge_stop[numbers[i]] += 1 # 0 1 0 1 0 0 0 1 0 1 0

    cnt = 0
    i = 0
    while i + K < N:
        tmp = 0
        for j in range(i+1, i+K+1): # i+1부터 i+K까지 충전소가 있는지 확인하고 가장 마지막 충전소를 stop 장소로 선정
            if charge_stop[j] == 1:
                tmp += 1
                i = j

        if tmp == 0: # 만약 구간 사이에 충전소가 없었다면 cnt를 0으로
            cnt = 0
            break
        if tmp >= 1:
            cnt += 1

    print('#{0} {1}'.format(tc, cnt))