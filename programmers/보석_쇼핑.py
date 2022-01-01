def solution(gems):
    gems_list = list(set(gems))
    length = len(gems_list)
    answer = []
    for i in range(len(gems) - length + 1):
        tmp = 0
        tmp_list = []
        for j in range(i, len(gems)):
            if answer:
                if answer[1] - answer[0] < j - i:
                    break
                elif answer[1] - answer[0] == j - i and answer[0] < i:
                    break

            if gems[j] not in tmp_list:
                tmp_list.append(gems[j])
                tmp += 1
                if tmp == length:
                    if answer:
                        if answer[1] - answer[0] > j - i:
                            answer = [i, j]
                        elif answer[1] - answer[0] == j - i and answer[0] > i:
                            answer = [i, j]
                    else:
                        answer = [i, j]
                    break
        else:
            break
    
    answer[0] += 1
    answer[1] += 1
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))