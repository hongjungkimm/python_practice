def solution(s):
    answer = []
    for i in s:
        if len(i) > 3:
            s_list = []
            for j in i:
                s_list.append(int(j))

                position = []
                for j in range(len(s_list) - 2):
                    if s_list[j] == 1 and s_list[j+1] == 1 and s_list[j+2] == 0:
                        position.append(j)

                tmp = []
                for j in position:
                    s_list_copy = s_list[:]
                    for _ in range(3):
                        s_list_copy.pop(j)
                    if s_list_copy[:3] == [1, 1, 1]:
                        tmp.append([1, 1., 0] + s_list_copy)
                    else:
                        cnt = 0
                        flag = False
                        for k in range(3, len(s_list_copy)):
                            if s_list_copy[k] == 1:
                                cnt += 1
                                if cnt >= 3:
                                    flag = True
                                    break

                        if cnt >= 3:
                            flag = True

                        if flag:
                            tmp.append(s_list_copy + [1, 1, 0])
                tmp.sort()
                if tmp:
                    answer.append(tmp[0])
                else:
                    answer.append(i)
                    break
        else:
            answer.append(i)
    return answer

print(solution(["1110","100111100","0111111010"]))