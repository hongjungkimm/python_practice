import sys

def eat(si, sj, num):
    global fishes, arrows, visited, result

    if num > result:
        result = num
    
    
def move(si, sj, num):
    global fishes, arrows, visited, di, dj
    
    for n in range(1, 17):
        flag = False
        for i in range(4):
            for j in range(4):
                if visited[i][j] == False and fishes[i][j] == n:
                    flag = True
                    a = arrows[i][j]
                    cnt = 1
                    while cnt <= 8:
                        ni = i + di[a]
                        nj = j + dj[a]
                        if 0 <= ni < 4 and 0 <= nj < 4 and visited[ni][nj] == False:
                            break
                        else:
                            a = (a + 1) % 8
                        cnt += 1
                    if cnt <= 8:
                        fishes[i][j], fishes[ni][nj] = fishes[ni][nj], fishes[i][j]
                        arrows[i][j], arrows[ni][nj] = arrows[ni][nj], arrows[i][j]
                if flag:
                    break
            if flag:
                break


fishes = []
arrows = []

for _ in range(4):
    tmp = list(map(int, sys.stdin.readline().split()))
    fish = []
    arrow = []
    for i in range(0, len(tmp), 2):
        fish.append(tmp[i])
        arrow.append(tmp[i+1] - 1)
    fishes.append(fish)
    arrows.append(arrow)

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

visited = [[False] * 4 for _ in range(4)]
visited[0][0] = True
result = 0
move(0 ,0, fishes[0][0])
print(fishes)
print(arrows)
print(visited)