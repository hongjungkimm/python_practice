import sys

width, height = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

w_list = [0, width] # 10
h_list = [0, height] # 8
for _ in range(N):
    is_wh, line = map(int, sys.stdin.readline().split())
    if is_wh:
        w_list.append(line)
    else:
        h_list.append(line)

w_list.sort()
h_list.sort()

w_length = 0
for i in range(len(w_list)-1, 0, -1):
    if w_list[i] - w_list[i-1] > w_length:
        w_length = w_list[i] - w_list[i-1]

h_length = 0
for i in range(len(h_list)-1, 0, -1):
    if h_list[i] - h_list[i-1] > h_length:
        h_length = h_list[i] - h_list[i-1]

area = w_length * h_length
print(area)