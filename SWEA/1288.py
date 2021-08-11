T = int(input())

for tc in range(T):
    N = int(input())
    NN = N

    cnt = 0
    N_list = []
    while True:
        cnt += 1
        N = cnt * N
        N = str(N)
        for i in N:
            N_list.append(i)
        N_list = set(N_list)
        if len(N_list) == 10:
            break
        N_list = list(N_list)
        N = NN
    
    print(f'#{tc+1} {int(N)}')