import sys
from collections import deque

def bfs(i, j, fi, fj):
    global area

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    visited = [[W * H] * (W) for _ in range(H)]
    queue = deque([[i, j, 0, 5, 0]])
    visited[i][j] = 0
    result = []
    while queue:
        x, y, path_cnt, recent_direction, change_cnt = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if ni == fi and nj == fj:
                if recent_direction == 5:
                    result.append([path_cnt, change_cnt])
                elif recent_direction == d:
                    result.append([path_cnt, change_cnt])
                else:
                    result.append([path_cnt, change_cnt + 1])
            elif 0 <= ni < H and 0 <= nj < W and area[ni][nj] == '.' and visited[x][y] + 1 <= visited[ni][nj]:
                visited[ni][nj] = visited[x][y] + 1
                if recent_direction == 5:
                    queue.append([ni, nj, path_cnt + 1, d, change_cnt])
                elif recent_direction == d:
                    queue.append([ni, nj, path_cnt + 1, d, change_cnt])
                else:
                    queue.append([ni, nj, path_cnt + 1, d, change_cnt + 1])

    result = sorted(result, key=lambda x: (x[0], x[1]))
    return result[0]


W, H = map(int, sys.stdin.readline().split())
area = []
for _ in range(H):
    temp = []
    line = sys.stdin.readline().rstrip()
    for l in line:
        temp.append(l)
    area.append(temp)

c_position = []
for i in range(H):
    for j in range(W):
        if area[i][j] == 'C':
            c_position.append([i, j])

answer = bfs(c_position[0][0], c_position[0][1], c_position[1][0], c_position[1][1])

print(answer[1])
