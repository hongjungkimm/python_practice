T = int(input())

for tc in range(1, T+1):
    N, K  = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    
    cnt = 0
    for i in range(N):
        j = 0
        tmp = 0
        while j < N:
            if puzzle[i][j]:
                tmp += 1
            else:
                tmp = 0
            if tmp == K:
                if j + 1 == N:
                    if puzzle[i][j-K] == 0:
                            cnt += 1
                            break
                elif puzzle[i][j+1] == 0:
                    if j - K < 0:
                        cnt += 1
                        tmp = 0
                    else:
                        if puzzle[i][j-K] == 0:
                            cnt += 1
                            tmp = 0
                else:
                    tmp = 0
            j += 1
    
    for j in range(N):
        i = 0
        tmp = 0
        while i < N:
            if puzzle[i][j]:
                tmp += 1
            else:
                tmp = 0
            if tmp == K:
                if i + 1 == N:
                    if puzzle[i-K][j] == 0:
                            cnt += 1
                            break
                elif puzzle[i+1][j] == 0:
                    if i - K < 0:
                        cnt += 1
                        tmp = 0
                    else:
                        if puzzle[i-K][j] == 0:
                            cnt += 1
                            tmp = 0
                else:
                    tmp = 0
            i += 1
    
    print('#{0} {1}'.format(tc, cnt))