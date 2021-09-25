# import sys

# def min_plane(n):
#     stack = [[n, 0]]

#     while stack:
#         num, time = stack.pop()
#         if sum(visited) == N:
#             return time
#         for i in schedule[num]:
#             if visited[i] == 0:
#                 visited[i] = 1
#                 stack.append([i, time+1])

# T = int(sys.stdin.readline())

# for _ in range(T):
#     N, M = map(int, sys.stdin.readline().split())
#     schedule = [[] * (N+1) for _ in range(N+1)]
    
#     for _ in range(M):
#         plane = list(map(int, sys.stdin.readline().split()))
#         schedule[plane[0]].append(plane[1])
#         schedule[plane[1]].append(plane[0])
    
#     visited = [0 for _ in range(N+1)]

#     print(min_plane(1))



import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    for j in range(M):
        a, b = map(int, sys.stdin.readline().split())
    print(N - 1)
