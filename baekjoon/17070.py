# import sys 재귀로 풀이

# def dfs(i, j, d):
#     # 0, 1, 2 == 가로, 세로, 대각 순서
#     global cnt

#     if i == N - 1 and j == N - 1:
#         cnt += 1
#         return

#     if i + 1 < N and j + 1 < N:
#         if house[i][j+1] == 0 and house[i+1][j+1] == 0 and house[i+1][j] == 0:
#             dfs(i + 1, j + 1, 2)

#     if d == 0 or d == 2:
#         if j + 1 < N:
#             if house[i][j+1] == 0:
#                 dfs(i, j + 1, 0)

#     if d == 1 or d == 2:
#         if i + 1 < N:
#             if house[i+1][j] == 0:
#                 dfs(i + 1, j, 1)

# N = int(sys.stdin.readline())
# house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# cnt = 0
# dfs(0, 1, 0)
# print(cnt)




import sys # 스택으로 풀이

def dfs(x, y, d):
    stack = [[x, y, d]]
 
    cnt = 0
    while stack:
        i, j, d = stack.pop()
        if i == N - 1 and j == N - 1:
            cnt += 1
            continue
        if i + 1 < N and j + 1 < N:
            if house[i][j+1] == 0 and house[i+1][j+1] == 0 and house[i+1][j] == 0:
                stack.append([i + 1, j + 1, 2])

        if d == 0 or d == 2:
            if j + 1 < N:
                if house[i][j+1] == 0:
                    stack.append([i, j + 1, 0])

        if d == 1 or d == 2:
            if i + 1 < N:
                if house[i+1][j] == 0:
                    stack.append([i + 1, j, 1])

    return cnt

N = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(dfs(0, 1, 0))