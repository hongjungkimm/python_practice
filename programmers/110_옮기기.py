def solution(s):
    answer = []
    for i in s:
        if len(i) <= 3:
            answer.append(i)
        else:
            stack = []
            cnt_110 = 0
            for j in i:
                if len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and j == '0':
                    for _ in range(2):
                        stack.pop()
                    cnt_110 += 1
                else:
                    stack.append(j)
            if cnt_110:
                cnt_1 = 0
                for s in stack[::-1]:
                    if s == '0':
                        break
                    else:
                        cnt_1 += 1
                answer.append(''.join(stack[:len(stack) - cnt_1]) + '110' * cnt_110 + '1' * cnt_1)
            else:
                answer.append(i)
    return answer

print(solution(["1110","100111100","0111111010", "11100", "101010110101010", "1000011110", "11110111101"]))