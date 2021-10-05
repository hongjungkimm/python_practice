from itertools import permutations

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    p_list = list(permutations(range(1, N), N-1))

    result = 0
    for i in range(len(p_list[0])-1):
        result += area[p_list[0][i]][p_list[0][i+1]]
    result += area[0][p_list[0][0]] + area[p_list[0][N-2]][0]

    for i in range(len(p_list)):
        temp = 0
        for j in range(len(p_list[i])-1):
            temp += area[p_list[i][j]][p_list[i][j+1]]
        temp += area[0][p_list[i][0]] + area[p_list[i][N-2]][0]
        if result > temp:
            result = temp

    print('#{0} {1}'.format(tc, result))