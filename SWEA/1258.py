T = int(input())

for tc in range(1, T+1):
    N = int(input())
    container = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(N):
            if container[i][j] != 0:
                y = 0
                dj = j
                while container[i][dj] != 0:
                    y += 1
                    dj += 1

                x = 0
                di = i
                while container[di][j] != 0:
                    x += 1
                    di += 1
                result.append([x, y])
                for h in range(i, i+x):
                    for w in range(j, j+y):
                        container[h][w] = 0

    for i in range(len(result)-1, 0, -1):
        for j in range(i):
            if result[j][0] * result[j][1] > result[j+1][0] * result[j+1][1]:
                result[j], result[j+1] = result[j+1], result[j]
            elif result[j][0] * result[j][1] == result[j+1][0] * result[j+1][1]:
                if result[j][0] > result[j+1][0]:
                    result[j], result[j+1] = result[j+1], result[j]

    print('#{0} {1}'.format(tc, len(result)), end=" ")
    temp = ''
    for i in range(len(result)):
        for j in result[i]:
            temp += str(j) + ' '
    print(temp)
