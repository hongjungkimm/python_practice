def search_end(i, j):
    global result
    maze[i][j] = 1 # 지나간 길 표시
    dij = [[1, 0], [0, 1], [0, -1], [-1, 0]] # 하 우 좌 상
    for di, dj in dij: # 이동위치 점 확인
        ni = i + di
        nj = j + dj
        if 0 < ni < 14 and 0 < nj < 14: # 미로의 범위 안이고
            if maze[ni][nj] == 0: # 갈 길이 있다면
                search_end(ni, nj) # 재귀로 반복
            elif maze[ni][nj] == 3: # 끝이 보였다면
                result = 1 # 도착여부 1로 반환
                return result

for _ in range(1, 11):
    tc = int(input())
    maze = []
    for _ in range(16):
        tmp = []
        for i in input():
            tmp.append(int(i))
        maze.append(tmp)

    result = 0 # 도착여부
    search_end(1, 1)
    print('#{0} {1}'.format(tc, result))