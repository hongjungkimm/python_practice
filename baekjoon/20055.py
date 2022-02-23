import sys

N, K = map(int, sys.stdin.readline().split())
belt = list(map(int, sys.stdin.readline().split()))
robot = [False] * N

cnt = 0
while True:
    for _ in range(N * 2):
        belt.insert(0, belt.pop())
    if robot.count(True):
        location = []
        for i in range(N):
            if robot[i] == True:
                location.append(i)
        for l in location:
            if l == N - 1:
                robot[l] = False
            else:
                if belt[l+1] and robot[l+1] == False:
                    belt[l+1] -= 1
                    robot[l+1] = True
                    robot[l] = False
    if belt[0]:
        robot[0] = True
        belt[0] -= 1
        cnt += 1
    if belt.count(0) >= K:
        break

print(cnt)