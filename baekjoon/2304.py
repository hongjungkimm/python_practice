import sys # 틀림

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

check_list = [1] + [0 for _ in range(N-2)] + [1]
max_h = h_sticks[0]
for i in range(1, N-1):
    if h_sticks[i] >= max_h:
        check_list[i] = 1
        max_h = h_sticks[i]

difference = 0
d = 0
for i in range(1, N):
    if check_list[i] == 1:
        if h_sticks[d] > h_sticks[i]:
            difference += ((l_sticks[i] - l_sticks[d]) * (max_h - h_sticks[i]))
            d = i
        else:
            difference += ((l_sticks[i] - l_sticks[d]) * (max_h - h_sticks[d]))
            d = i

print(((l_sticks[-1] - l_sticks[0] + 1) * max_h) - difference)