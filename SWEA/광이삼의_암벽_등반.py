from collections import deque

def bfs(si, sj):
    global result

    visited = [[0] * N for _ in range(M)]
    visited[si][sj] = 9
    queue = deque()
    queue.append([si, sj, L, 9])
    while queue:
        ti, tj, remainder, cnt = queue.popleft()
        for d in range(4):
            ni = ti + di[d]
            nj = tj + dj[d]
            if 0 <= ni < M and 0 <= nj < N:
                if remainder and cnt > visited[ni][nj]:
                    if area[ni][nj] == 3:
                        if cnt > result:
                            result = cnt
                    elif area[ni][nj] == 1:
                        visited[ni][nj] = cnt - 1
                        queue.appendleft([ni, nj, L, cnt - 1])
                        queue.append([ni, nj, remainder - 1, cnt])
                    else:
                        visited[ni][nj] = cnt
                        queue.append([ni, nj, remainder - 1, cnt])
                
T = int(input())

for tc in range(1, T+1):
    M, N, L = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(M)]

    si = 0
    sj = 0
    ei = 0
    ej = 0
    for i in range(M):
        for j in range(N):
            if area[i][j] == 2:
                si = i
                sj = j
            if area[i][j] == 3:
                ei = i
                ej = j
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    result = -1
    bfs(si, sj)

    if result == -1:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {9 - result}')


# def bfs(ti, tj, remainder, cnt):
#     global result, visited

#     if ti == ei and tj == ej:
#         if cnt < result:
#             result = cnt
#         return

#     for d in range(4):
#         ni = ti + di[d]
#         nj = tj + dj[d]
#         if 0 <= ni < M and 0 <= nj < N:
#             if remainder and visited[ni][nj] == False:
#                 if area[ni][nj] == 0:
#                     visited[ni][nj] = True
#                     bfs(ni, nj, remainder - 1, cnt)
#                     visited[ni][nj] = False
#                 if area[ni][nj] == 1:
#                     visited[ni][nj] = True
#                     bfs(ni, nj, L, cnt + 1)
#                     bfs(ni, nj, remainder - 1, cnt)
#                     visited[ni][nj] = False
#                 if area[ni][nj] == 3:
#                     visited[ni][nj] = True
#                     bfs(ni, nj, remainder - 1, cnt)
#                     visited[ni][nj] = False
                
# T = int(input())

# for tc in range(1, T+1):
#     M, N, L = map(int, input().split())
#     area = [list(map(int, input().split())) for _ in range(M)]

#     si = 0
#     sj = 0
#     ei = 0
#     ej = 0
#     for i in range(M):
#         for j in range(N):
#             if area[i][j] == 2:
#                 si = i
#                 sj = j
#             if area[i][j] == 3:
#                 ei = i
#                 ej = j
    
#     di = [-1, 1, 0, 0]
#     dj = [0, 0, -1, 1]
#     result = float('inf')
#     visited = [[False] * N for _ in range(M)]
#     visited[si][sj] = True
#     bfs(si, sj, L, 0)

#     if result == float('inf'):
#         print(-1)
#     else:
#         print(result)