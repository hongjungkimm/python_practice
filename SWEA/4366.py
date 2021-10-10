def change_decimal(num_list, n):
    if n == 2:
        result = 0
        for i in range(len(num_list)):
            result += (2 ** (len(num_list)-1-i)) * num_list[i]
        return result
    else:
        result = 0
        for i in range(len(num_list)):
            result += (3 ** (len(num_list)-1-i)) * num_list[i]
        return result

T = int(input())

for tc in range(1, T+1):
    two = [int(i) for i in input()]
    three = [int(i) for i in input()]

    flag = False
    final_result = 0
    for i in range(len(two)-1, 0, -1):
        temp1 = two[:]
        if two[i]:
            temp1[i] = 0
        else:
            temp1[i] = 1
        result1 = change_decimal(temp1, 2)
        for j in range(len(three)-1, -1, -1):
            if j > 0:
                for k in [0, 1, 2]:
                    if k != three[j]:
                        temp2 = three[:]
                        temp2[j] = k
                        result2 = change_decimal(temp2, 3)
                        if result1 == result2:
                            flag = True
                            break
            else:
                for k in [1, 2]:
                    if k != three[j]:
                        temp2 = three[:]
                        temp2[j] = k
                        result2 = change_decimal(temp2, 3)
                        if result1 == result2:
                            flag = True
                            break
        if flag:
            final_result = result1
            break

    print('#{0} {1}'.format(tc, final_result))