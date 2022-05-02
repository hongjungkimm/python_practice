def solution(distance, rocks, n):
    rocks.sort()
    answer = 0
    start = 0
    end = distance
    while start <= end:
        mid = (start + end) // 2
        del_rock = 0
        standard_rock = 0
        for rock in rocks:
            if rock - standard_rock < mid:
                del_rock += 1
            else:
                standard_rock = rock
            if del_rock > n:
                break
        if del_rock > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))


# from itertools import combinations

# def solution(distance, rocks, n):
#     rocks.sort()
#     length = len(rocks) - n
#     combi = list(combinations(rocks, length))
#     answer = -1
#     for c in combi:
#         temp = float('inf')
#         for i in range(len(c)):
#             if i == 0:
#                 diff = c[0]
#             elif i == len(c) - 1:
#                 diff = distance - c[i]
#             else:
#                 diff = c[i] - c[i-1]
#             if diff < temp:
#                 temp = diff
#         if temp > answer:
#             answer = temp
#     return answer

# print(solution(25, [2, 14, 11, 21, 17], 2))