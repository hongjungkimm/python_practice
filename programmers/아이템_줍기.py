def solution(rectangle, characterX, characterY, itemX, itemY):
    
    graph = [[0] * 51 for _ in range(51)]
    for r in rectangle:
        for i in range(r[1], r[3] + 1):
            for j in range(r[0], r[2] + 1):
                graph[i][j] += 1

    di = [1, 0, 0, -1]
    dj = [0, 1, -1, 0]
    
    stack = [[characterY, characterX, 0]]
    visited = [[False] * 51 for _ in range(51)]
    
    while stack:
        y, x, distance = stack.pop()
        print(y, x, distance)
        if y == itemY and x == itemX:
            return distance

        if visited[y][x] == False:
            visited[y][x] = True
            for d in range(4):
                ni = y + di[d]
                nj = x + dj[d]
                if 0 <= ni < 51 and 0 <= nj < 51:
                    cnt = 0
                    for d in range(4):
                        tmp_i = ni + di[d]
                        tmp_j = nj + dj[d]
                        if 0 <= tmp_i < 51 and 0 <= tmp_j < 51 and graph[tmp_i][tmp_j] == 0:
                            cnt += 1
                    if cnt and visited[ni][nj] == False and graph[ni][nj]:
                        stack.append([ni, nj, distance + 1])




print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))