T = int(input())

for tc in range(1, T+1):
    N, K  = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    
    cnt = 0 # 들어갈 수 있는 자리의 수
    for i in range(N): # 가로확인
        tmp = 0 # K개의 칸이 1인지 확인하는 임시 변수
        for j in range(N):
            if puzzle[i][j]: # 현재 칸이 1인이면 tmp에 한 칸 추가
                tmp += 1
            else:
                tmp = 0 # 그게 아니면 tmp를 초기화
            if tmp == K: # 만약 K번 1이 연속되는 칸이면
                if j + 1 == N: # 그리고 이 칸이 길이의 끝이면
                    if puzzle[i][j-K] == 0: # 이 연속되는 칸 앞의 숫자가 0이면
                        cnt += 1 # 최종 가능 자리 수에 1을 추가
                        break
                elif puzzle[i][j+1]: # 이 다음 칸이 1이면
                    tmp = 0 # tmp를 초기화
                else: # 이 다음칸이 0이면
                    if j - K < 0: # 0번째 칸부터 연속되는 칸일 때를 확인
                        cnt += 1 # 최종 가능 자리 수에 1을 추가
                        tmp = 0 # tmp 초기화
                    else:
                        if puzzle[i][j-K]: # 현재 칸에서 K를 뺀 칸이 1이면
                            tmp = 0 # tmp 초기화
                        else: # 그게 아니면
                            cnt += 1 # 최종 가능 자리 수에 1을 추가
                            tmp = 0 # tmp 초기화
    
    for j in range(N): # 세로확인
        tmp = 0
        for i in range(N):
            if puzzle[i][j]:
                tmp += 1
            else:
                tmp = 0
            if tmp == K:
                if i + 1 == N:
                    if puzzle[i-K][j] == 0:
                        cnt += 1
                        break
                elif puzzle[i+1][j]:
                    tmp = 0
                else:
                    if i - K < 0:
                        cnt += 1
                        tmp = 0
                    else:
                        if puzzle[i-K][j]:
                            tmp = 0
                        else:
                            cnt += 1
                            tmp = 0
    
    print('#{0} {1}'.format(tc, cnt))

    # cnt = 0
    # for i in range(N):
    #     j = 0
    #     tmp = 0
    #     while j < N:
    #         if puzzle[i][j]:
    #             tmp += 1
    #         else:
    #             tmp = 0
    #         if tmp == K:
    #             if j + 1 == N:
    #                 if puzzle[i][j-K] == 0:
    #                         cnt += 1
    #                         break
    #             elif puzzle[i][j+1] == 0:
    #                 if j - K < 0:
    #                     cnt += 1
    #                     tmp = 0
    #                 else:
    #                     if puzzle[i][j-K] == 0:
    #                         cnt += 1
    #                         tmp = 0
    #             else:
    #                 tmp = 0
    #         j += 1
    
    # for j in range(N):
    #     i = 0
    #     tmp = 0
    #     while i < N:
    #         if puzzle[i][j]:
    #             tmp += 1
    #         else:
    #             tmp = 0
    #         if tmp == K:
    #             if i + 1 == N:
    #                 if puzzle[i-K][j] == 0:
    #                         cnt += 1
    #                         break
    #             elif puzzle[i+1][j] == 0:
    #                 if i - K < 0:
    #                     cnt += 1
    #                     tmp = 0
    #                 else:
    #                     if puzzle[i-K][j] == 0:
    #                         cnt += 1
    #                         tmp = 0
    #             else:
    #                 tmp = 0
    #         i += 1
    
    # print('#{0} {1}'.format(tc, cnt))