import sys

N, K = map(int,sys.stdin.readline().split())

stn_list = []
girl = []
boy = []

for i in range(N):
    student = list(map(int,sys.stdin.readline().split()))
    stn_list.append(student)

for i in range(2):
    for j in range(1, 7):
        temp = 0
        for stn in stn_list:
            if stn[0] == i and stn[1] == j:
                temp += 1
        if i == 0 and temp != 0:
            girl.append(temp)
        elif i == 1 and temp != 0:
            boy.append(temp)

cnt = 0
for i in girl:
    if i > K:
        cnt += (i // K + 1)
    else:
        cnt += 1

for i in boy:
    if i > K:
        cnt += (i // K + 1)
    else:
        cnt += 1

print(cnt)