import sys

N, M = map(int, sys.stdin.readline().split())

maze = []
for _ in range(N):
    line = sys.stdin.readline().rstrip()
    tmp = []
    for l in line:
        tmp.append(l)
    maze.append(tmp)

red = []
blue = []
hole = []
flag = False
for i in range(N):
    for j in range(M):
        if maze[i][j] == 'R':
            red = [i, j]
        elif maze[i][j] == 'B':
            blue = [i, j]
        elif maze[i][j] == 'O':
            hole = [i, j]
        if red and blue and hole:
            flag = True
            break
    if flag:
        break

answer = float('inf')
