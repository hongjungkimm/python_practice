# import sys 시간초과
# from collections import deque

# def bfs(i, j):
#     queue = deque([[i, j]])
#     visited = [[0] * M for _ in range(N)]
#     visited[i][j] = 1

#     while queue:
#         x, y = queue.popleft()
#         for d in range(4):
#             ni = x + di[d]
#             nj = y + dj[d]
#             if 0 <= ni < N and 0 <= nj < M:
#                 if visited[ni][nj] == 0 and maze[ni][nj] == '0':
#                     if ni == N - 1 and nj == M - 1:
#                         return visited[x][y] + 1
#                     visited[ni][nj] = visited[x][y] + 1
#                     queue.appendleft([ni, nj])
#     return -1

# N, M = map(int, sys.stdin.readline().split())
# maze = [[i for i in sys.stdin.readline().rstrip()] for _ in range(N)]
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]

# wall = []
# for i in range(N):
#     for j in range(M):
#         if maze[i][j] == '1':
#             wall.append([i, j])

# result = []
# for w in wall:
#     maze[w[0]][w[1]] = '0'
#     result.append(bfs(0, 0))
#     maze[w[0]][w[1]] = '1'

# final_result = 1000 * 1000
# for r in result:
#     if r != -1 and final_result > r:
#         final_result = r
# if final_result == 1000 * 1000:
#     final_result = -1

# print(final_result)