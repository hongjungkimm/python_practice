def solution(n, results): 
    answer = 0
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))


# from collections import defaultdict

# def solution(n, results):

#     def dfs(i):
#         nonlocal n, results, results_dict, answer_list, check
        
#         stack = [[i, [i]]]
#         while stack:
#             a, trace = stack.pop()
#             check[a] += 1
#             if results_dict[a] == []:
#                 answer_list.append(trace)
#             else:
#                 for j in results_dict[a]:
#                     stack.append([j, trace + [j]])


#     results_dict = defaultdict(list)
#     for a, b in results:
#         results_dict[a].append(b)
    
#     check = [0] * (n + 1)
#     answer_list = []
#     for i in list(results_dict.keys()):
#         if results_dict[i] != []:
#             dfs(i)
            
#     answer = 0
#     length = len(answer_list)
#     for c in check:
#         if c == length:
#             answer += 1

#     return answer

# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))


# from collections import defaultdict

# def solution(n, results):

#     def dfs(i, trace):
#         nonlocal n, results, results_dict, answer_list, check

#         check[i] += 1
#         if results_dict[i] == []:
#             answer_list.append(trace)
#             return

#         for j in results_dict[i]:
#             dfs(j, trace + [j])


#     results_dict = defaultdict(list)
#     for a, b in results:
#         results_dict[a].append(b)

#     answer_list = []
#     check = [0] * (n + 1)
#     for i in range(1, n + 1):
#         if results_dict[i] == []:
#             continue
#         dfs(i, [i])
    
#     answer = 0
#     length = len(answer_list)
#     for c in check:
#         if c == length:
#             answer += 1
#     return answer

# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))