# import sys

# N, S = map(int, sys.stdin.readline().split())
# numbers = list(map(int, sys.stdin.readline().split()))

# cnt = 0
# for i in range(1, 1 << N):
#     tmp = []
#     for j in range(N):
#         if i & (1 << j):
#             tmp.append(numbers[j])
#     if sum(tmp) == S:
#         cnt += 1

# print(cnt)


# import sys
# from itertools import combinations

# N, S = map(int, sys.stdin.readline().split())
# numbers = list(map(int, sys.stdin.readline().split()))

# cnt = 0
# for i in range(N+1):
#     for j in combinations(numbers, i):
#         if j != () and sum(j) == S:
#             cnt += 1

# print(cnt)