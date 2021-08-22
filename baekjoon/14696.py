import sys

N = int(sys.stdin.readline())

users = [list(map(int, sys.stdin.readline().split())) for _ in range(N*2)]
A = [users[i] for i in range(0, N*2, 2)]
B = [users[i] for i in range(1, N*2, 2)]

for i in range(N):
    result = ''
    A_cnt = [0 for _ in range(N)]
    B_cnt = [0 for _ in range(N)]
    for j in A[i][1:]:
        A_cnt[j] += 1
    for j in B[i][1:]:
        B_cnt[j] += 1
    for j in range(4, 0, -1):
        if A_cnt[j] > B_cnt[j]:
            result += 'A'
            break
        elif B_cnt[j] > A_cnt[j]:
            result += 'B'
            break
    if result == '':
        result = 'D'
    print(result)