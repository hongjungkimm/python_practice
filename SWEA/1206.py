for tc in range(1, 11):
    T = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(2, T-2):
        tmp = buildings[i-2:i] + buildings[i+1:i+3]
        for j in range(len(tmp)-1):
            if tmp[j] > tmp[j+1]:
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
        if buildings[i] > tmp[-1]:
            difference = (buildings[i] - tmp[-1])
            result += difference

    print('#{0} {1}'.format(tc, result))
