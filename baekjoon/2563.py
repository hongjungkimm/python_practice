import sys

N = int(sys.stdin.readline()) # 색종이의 개수

points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 각 사각형의 시작 좌표들

graph = [[0] * 101 for _ in range(101)]

for p in points: # 각 사각형의 시작 좌표를 기준으로 상, 우 +10을 해준 범위에 1을 찍어줌(각 사각형의 면적 표시, 점이 아니라 변을 기준으로)
    for i in range(p[0], p[0]+10):
        for j in range(p[1], p[1]+10):
            graph[i][j] += 1

cnt = 0
for i in range(101):
    for j in range(101):
        if graph[i][j] >= 1: # 1이상이 찍힌 면적을 확인
            cnt += 1

print(cnt)