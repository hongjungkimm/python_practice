T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = list(filter(lambda x: x % 10 != 0, numbers))

    result_list = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            flag = True
            tmp = numbers[i] * numbers[j]
            tmp2 = str(tmp)
            for k in range(len(tmp2)-1):
                if int(tmp2[k+1]) >= int(tmp2[k]):
                    pass
                else:
                    flag = False
                    break
            if flag:
                result_list.append(tmp)

    if result_list:
        print('#{0} {1}'.format(tc, max(result_list)))
    else:
        print('#{0} -1'.format(tc))