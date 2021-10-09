# import sys ~ing
# from itertools import combinations

# N = int(sys.stdin.readline())
# area_num = [0] + list(map(int, sys.stdin.readline().split()))
# population = {}
# for i in range(1, N+1):
#     population[i] = area_num[i]
# area = [[]]+[list(map(int, sys.stdin.readline().split()))[1:] for _ in range(N)]

# powerset = []
# for i in range(1, N//2+1):
#     for j in combinations(range(1, N+1), i):
#         powerset.append(j)

# print(powerset)
# print(area)