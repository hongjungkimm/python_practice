import sys

def move(i, j, direction, cnt):
    global N, di, dj

    while cnt:
        cnt -= 1
        ni = i + di[direction-1]
        nj = j + dj[direction-1]
        if direction - 1 in [0, 2, 4, 6]:
            if ni == -1:
                ni = N - 1
            if ni == N:
                ni = 0
            if nj == -1:
                nj = N - 1
            if nj == N:
                nj = 0
            i = ni
            j = nj
        else:
            if ni == -1 or ni == N or nj == -1 or nj == N:
                ni -= di[direction-1]
                nj -= di[direction-1]
                i = nj
                j = ni
    
    result = [ni, nj]
    return result


N, M = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
point = [N-1, 0]

cloud = []
for i in range(M):
    if i == 0:
        direction, cnt = commands[0]
        point = move(point[0], point[1], direction, cnt)
        tmp = [point]
        if point[0] - 1 == 0 and point[1] + 1 == N:
            tmp.append([0, 0])
        else:
            tmp.append([point[0] - 1, point[1] + 1])
        if point[0] - 1 == 0:
            tmp.append([0, point[1]])
        else:
            tmp.append([point[0] - 1, point[1]])
        if point[1] + 1 == N:
            tmp.append([point[0], 0])
        else:
            tmp.append([point[0], point[1] + 1])
        for i, j in tmp:
            area[i][j] += 1
        for i, j in tmp:
            plus = 0
            for pi, pj in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
                ni = i + pi
                nj = j + pj
                if 0 <= ni < N and 0 <= nj < N and area[ni][nj]:
                    plus += 1
            area[i][j] += plus
        for i in range(N):
            for j in range(N):
                if [i, j] not in tmp and area[i][j] >= 2:
                    area[i][j] -= 2
                    cloud.append([i, j])
    else:
        direction, cnt = commands[i]
        print(cloud)
        for i in range(len(cloud)):
            location = move(cloud[i][0], cloud[i][1], direction, cnt)
            cloud[i] = location
            area[cloud[i][0]][cloud[i][1]] += 1
        print("-----")
        print(cloud)
        print("-------end")
        for i, j in cloud:
            plus = 0
            for pi, pj in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
                ni = i + pi
                nj = j + pj
                if 0 <= ni < N and 0 <= nj < N and area[ni][nj]:
                    plus += 1
            area[i][j] += plus
        
        tmp = []
        for i in range(N):
            for j in range(N):
                if [i, j] not in cloud and area[i][j] >= 2:
                    area[i][j] -= 2
                    tmp.append([i, j])
        cloud = tmp
    
print(area)