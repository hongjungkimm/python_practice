import sys

height_list = [int(sys.stdin.readline()) for _ in range(9)]

search = False
for i in range(1 << 9):
    tmp = []
    for j in range(9):
        if i & (1 << j):
            tmp.append(height_list[j])
    if len(tmp) == 7 and sum(tmp) == 100:
        tmp.sort()
        for n in tmp:
            print(n)
        break