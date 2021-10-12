import sys
from itertools import combinations

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    combi = list(combinations(range(N), N//2))

    result = float('inf')
    for c in combi:
        temp_combi1 = list(combinations(c, 2))
        temp1 = 0
        for i, j in temp_combi1:
            temp1 += ingredients[i][j]
            temp1 += ingredients[j][i]

        temp_list = []
        for i in range(N):
            if i not in c:
                temp_list.append(i)
        temp_combi2 = list(combinations(temp_list, 2))
        temp2 = 0
        for i, j in temp_combi2:
            temp2 += ingredients[i][j]
            temp2 += ingredients[j][i]

        if abs(temp1 - temp2) < result:
            result = abs(temp1 - temp2)

    print('#{0} {1}'.format(tc, result))

