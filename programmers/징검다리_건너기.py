def solution(stones, k):
    answer = 0
    length = len(stones)
    zero_stones = [0] * length
    while True:
        for i in range(length):
            if stones[i] > 0:
                stones[i] -= 1
            else:
                if zero_stones[i] == 0:
                    zero_stones[i] = 1
                for j in range(length - k + 1):
                    if sum(zero_stones[j:j+k]) == k:
                        return answer
        else:
            answer += 1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

# def solution(stones, k):
#     length = len(stones)
#     min_sum = float('inf')
#     for i in range(length - k + 1):
#         if sum(stones[i:i+k]) < min_sum:
#             min_sum = sum(stones[i:i+k])
    
#     answer = float('inf')
#     for i in range(length - k + 1):
#         if sum(stones[i:i+k]) == min_sum and max(stones[i:i+k]) < answer:
#             answer = max(stones[i:i+k])
            
#     return answer


# def solution(stones, k):
#     length = len(stones)
#     zero_stones = []
#     answer = 0
#     while True:
#         for i in range(length):
#             if stones[i] > 0:
#                 stones[i] -= 1
#                 if stones[i] == 0 and i < length - k:
#                     zero_stones.append(i)
#         answer += 1
#         for i in zero_stones:
#             if sum(stones[i:i+k]) == 0:
#                 return answer
#     return answer