import copy

for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start = []
    for i in range(100):
        if ladder[0][i] == 1:
            start.append(i)

    cnt_list = []
    for s in start:
        ladder_copy = copy.deepcopy(ladder)
        cnt = 0
        i = 0
        j = s
        while 99 > i:
            if 0 <= i <= 99 and 0 <= j + 1 <= 99 and ladder_copy[i][j+1]:
                    ladder_copy[i][j] = 0
                    j += 1
                    cnt += 1
            elif 0 <= i <= 99 and 0 <= j - 1 <= 99 and ladder_copy[i][j-1]:
                    ladder_copy[i][j] = 0
                    j -= 1
                    cnt += 1
            elif 0 <= i + 1 <= 99 and 0 <= j <= 99 and ladder_copy[i+1][j]:
                    ladder_copy[i][j] = 0
                    i += 1
                    cnt += 1
        cnt_list.append(cnt)

    min_idx = 0
    for i in range(len(cnt_list)):
        if cnt_list[min_idx] > cnt_list[i]:
            min_idx = i

    print('#{0} {1}'.format(tc, start[min_idx]))