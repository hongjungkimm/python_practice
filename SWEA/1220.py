for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for j in range(100):
        tmp = []
        for i in range(100):
            tmp.append(table[i][j])
        if tmp.count(1) + tmp.count(2) >= 2:
            check_1 = False
            check_2 = False
            for k in range(100):
                if tmp[k] == 1:
                    if check_2:
                        check_2 = False
                    check_1 = True
                elif tmp[k] == 2:
                    check_2 = True
                if check_1 and check_2:
                    cnt += 1
                    check_1 = False
                    check_2 = False

    print('#{0} {1}'.format(tc, cnt))