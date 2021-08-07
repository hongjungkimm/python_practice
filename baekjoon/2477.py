import sys

K = int(sys.stdin.readline())
width = []

for i in range(6):
    d, w = map(int, sys.stdin.readline().split())
    width.append(w)

area_list = [width[5]*width[0]]
for i in range(5):
    area_list.append(width[i] * width[i+1])

area_max = max(area_list)
result = K * (sum(area_list) - area_max * 2)

print(result)