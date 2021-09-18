import sys
from pprint import pprint # 메모리 초과

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

tiles = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

picture = [[0] * N for _ in range(N)]
# 빨, 파, 노 순서
if N % 2:
    c = 1
    k = 0
    for i in range(N//2+1):
        for j in range(i, N-k):
            if c % 3 == 1:
                picture[i][j] = 1
                picture[N-1-i][j] = 1
                picture[j][N-1-i] = 1
                picture[j][i] = 1
            elif c % 3 == 2:
                picture[i][j] = 2
                picture[N-1-i][j] = 2
                picture[j][N-1-i] = 2
                picture[j][i] = 2
            else:
                picture[i][j] = 3
                picture[N-1-i][j] = 3
                picture[j][N-1-i] = 3
                picture[j][i] = 3
        c += 1
        k += 1
else:
    c = 1
    k = 0
    for i in range(N//2):
        for j in range(i, N-k):
            if c % 3 == 1:
                picture[i][j] = 1
                picture[N-1-i][j] = 1
                picture[j][N-1-i] = 1
                picture[j][i] = 1
            elif c % 3 == 2:
                picture[i][j] = 2
                picture[N-1-i][j] = 2
                picture[j][N-1-i] = 2
                picture[j][i] = 2
            else:
                picture[i][j] = 3
                picture[N-1-i][j] = 3
                picture[j][N-1-i] = 3
                picture[j][i] = 3
        c += 1
        k += 1

pprint(picture)
for t in tiles:
    print(picture[t[0]-1][t[1]-1])