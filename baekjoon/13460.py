import sys

N, M = map(int, sys.stdin.readline().split())

maze = []
for _ in range(N):
    line = sys.stdin.readline().rstrip()
    tmp = []
    for l in line:
        tmp.append(l)
    maze.append(tmp)

print(maze)