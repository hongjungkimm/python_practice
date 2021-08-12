T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    mom = list(range(1, 13))
    n = len(mom)

    total = 0
    for i in range(1 << n):
        tmp = [] # 부분집합의 요소를 넣기 위한 임시 리스트
        tmp_total = 0 # 부분집합의 합을 구하기 위한 임시 변수
        for j in range(n):
            if i & (1 << j):
                tmp.append(mom[j])
        for t in tmp:
            tmp_total += t
        if len(tmp) == N and tmp_total == K: # 부분집합 안 요소의 개수가 N이고, 합이 K이면 전체 total 개수를 count
            total += 1

    print('#{0} {1}'.format(tc, total))
