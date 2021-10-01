T = int(input())

for tc in range(1, T+1):
    temp, cnt = input().split()
    number = [int(i) for i in temp]

    cnt = int(cnt)
    length = len(number)
    pointer = 0
    reverse = False
    while cnt > 0:
        if reverse:
            flag = False
            for i in range(length):
                for j in range(i+1, length):
                    if number[i] == number[j]:
                        flag = True
                        while cnt > 0:
                            cnt -= 1
                        break
                if flag:
                    break
            else:
                number[pointer], number[pointer-1] = number[pointer-1], number[pointer]
                cnt -= 1

            if pointer == 0:
                reverse = False
        else:
            max_rank = 0
            for i in range(pointer+1, length):
                if number[pointer] > number[i]:
                    max_rank += 1

            max_idx = pointer
            for i in range(length-1, pointer, -1):
                if number[i] > number[max_idx]:
                    max_idx = i

            equal_idx = 0
            equal_cnt = 0
            for i in range(length - 1, pointer, -1):
                if i != max_idx:
                    if number[i] == number[max_idx]:
                        equal_idx = i
                        equal_cnt += 1

            if max_idx != pointer:
                if max_rank and equal_cnt:
                    number[pointer], number[max_idx-max_rank] = number[max_idx-max_rank], number[pointer]
                    cnt -= 1
                else:
                    number[pointer], number[max_idx] = number[max_idx], number[pointer]
                    cnt -= 1
            elif equal_idx:
                number[pointer], number[equal_idx] = number[equal_idx], number[pointer]
                cnt -= 1



            pointer += 1
            if pointer == length - 1:
                reverse = True

    print('#{0} {1}'.format(tc, ''.join(list(map(str, number)))))