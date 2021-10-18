T = int(input()) # ~ing

for tc in range(1, T+1):
    N = int(input())
    maxinos = [list(map(int, input().split())) for _ in range(N)]

    cores = []
    for i in range(N):
        for j in range(N):
            if maxinos[i][j] == 1:
                cores.append([i, j])
    
