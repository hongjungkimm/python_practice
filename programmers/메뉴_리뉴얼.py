from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for num in course:
        array = []
        for order in orders:
            order = sorted(order) 
            array.extend(list(combinations(order, num)))
        
        count = Counter(array)
        
        if count:
            if max(count.values()) >= 2:
                for key, value in count.items():
                    if value == max(count.values()):
                        answer.append("".join(key))
    
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))


# from collections import defaultdict
# from itertools import combinations

# def solution(orders, course):
#     alpha = []
#     for order in orders:
#         for o in order:
#             if o not in alpha:
#                 alpha.append(o)
    
#     alpha.sort()
#     answer = []
#     for c in course:
#         combi = combinations(alpha, c)
#         c_dict = defaultdict(list)
#         for com in combi:
#             tmp = ''.join(com)
#             cnt = 0
#             for order in orders:
#                 for i in tmp:
#                     if i not in order:
#                         break
#                 else:
#                     cnt += 1
#             if cnt >= 2:
#                 c_dict[cnt].append(tmp)
#         try:
#             max_cnt = max(list(c_dict.keys()))
#             for i in c_dict[max_cnt]:
#                 answer.append(i)
#         except:
#             pass
    
#     answer_sorted = []
#     for a in answer:
#         tmp = []
#         for i in a:
#             tmp.append(i)
#         tmp = ''.join(tmp)
#         answer_sorted.append(tmp)
    
#     answer_sorted.sort()
#     return answer_sorted