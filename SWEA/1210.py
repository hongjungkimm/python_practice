for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    di = [-1, 0, 0] # 상 좌 우
    dj = [0, -1, 1]

    ni = 99
    nj = 0
    for i in range(100):
        if ladder[99][i] == 2:
            nj = i
    i = -1
    j = 0
    result = 0
    while True:
        ni = ni + i
        nj = nj + j
        if ni == 0:
            result = nj
            break
        if nj == 99:
            if ladder[ni][nj-1]:
                i = di[1]
                j = dj[1]
                ladder[ni][nj] = 0
            else:
                i = di[0]
                j = dj[0]
                ladder[ni][nj] = 0
        elif nj == 0:
            if ladder[ni][nj+1]:
                i = di[2]
                j = dj[2]
                ladder[ni][nj] = 0
            else:
                i = di[0]
                j = dj[0]
                ladder[ni][nj] = 0
        else:
            if ladder[ni][nj-1]:
                    i = di[1]
                    j = dj[1]
                    ladder[ni][nj] = 0
            elif ladder[ni][nj+1]:
                    i = di[2]
                    j = dj[2]
                    ladder[ni][nj] = 0
            else:
                i = di[0]
                j = dj[0]
                ladder[ni][nj] = 0

    print('#{0} {1}'.format(T, result))