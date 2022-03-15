def solution(info, query):
    info_list = []
    for i in info:
        info_list.append(i.split())
    
    query_list = []
    for q in query:
        tmp = q.split(" and ")
        end = tmp[-1].split()
        tmp.pop()
        tmp.append(end[0])
        tmp.append(end[1])
        query_list.append(tmp)

    answer = []
    for query in query_list:
        cnt = 0
        for info in info_list:
            if (query[0] == '-' or query[0] == info[0]) and (query[1] == '-' or query[1] == info[1]) and (query[2] == '-' or query[2] == info[2]) and (query[3] == '-' or query[3] == info[3]) and (query[4] == '-' or int(query[4]) <= int(info[4])):
                cnt += 1
        answer.append(cnt)

    return answer

# from collections import defaultdict

# def solution(info, query):
#     info_dict = defaultdict(list)
#     info_scores = []
#     for i in range(len(info)):
#         tmp = info[i].split()
#         for j in tmp[:-1]:
#             info_dict[j].append(i)
#         info_scores.append(int(tmp[-1]))

#     answer = []
#     for q in query:
#         tmp = q.split(" and ")
#         end = tmp[-1].split()
#         tmp.pop()
#         tmp.append(end[0])
#         tmp.append(end[1])
#         result = [1] * len(info)
#         nums = [0] * len(info)
#         for t in tmp:
#             if t == "-":
#                 pass
#             else:
#                 if t.isdigit():
#                     t = int(t)
#                     for i in range(len(info)):
#                         if info_scores[i] >= t:
#                             nums[i] = 1
#                 else:
#                     for i in range(len(info)):
#                         if result[i]:
#                             if i not in info_dict[t]:
#                                 result[i] = 0
#         cnt = 0
#         for i in range(len(info)):
#             if result[i] and nums[i]:
#                 cnt += 1
#         answer.append(cnt)

#     return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))