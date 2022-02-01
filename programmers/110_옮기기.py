def solution(s):
    answer = []
    for i in s:
        s_list = []
        for j in i:
            s_list.append(j)
        if len(i) <= 3:
            answer.append(i)
        else:
            while True:
                zero = 0
                cnt = 0
                for j in range(len(s_list)):
                    if s_list[j] == '1':
                        cnt += 1
                    else:
                        if cnt >= 3:
                            zero = j
                            s_list.pop(j)
                            break
                        cnt = 0
                if zero:
                    s_list.insert(j - 1, '0')
                else:
                    break
            s_str = ''
            for j in s_list:
                s_str += j
            answer.append(s_str)
    return answer

print(solution(["1110","100111100","0111111010", "11100"]))