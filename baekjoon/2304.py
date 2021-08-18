import sys

N = int(sys.stdin.readline())

sticks = {}
for _ in range(N):
    l, h = map(int, sys.stdin.readline().split())
    sticks[l] = h

l_sticks = list(sticks.keys())
l_sticks.sort()

h_sticks = []
for l in l_sticks:
    h_sticks.append(sticks[l])

max_idx = 0
for i in range(N):
    if h_sticks[i] >= h_sticks[max_idx]:
        max_idx = i

result = 0
point = 0
for i in range(max_idx+1):
    if h_sticks[point] <= h_sticks[i]:
        result += ((l_sticks[i] - l_sticks[point]) * h_sticks[point])
        point = i

point = N - 1
for i in range(N-1, max_idx-1, - 1):
    if h_sticks[point] <= h_sticks[i]:
        result += ((l_sticks[point] - l_sticks[i]) * h_sticks[point])
        point = i

result = result + h_sticks[max_idx]
print(result)