import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

cnt = 0
i = 0
tmp = 1
while i < len(numbers) - 1:
    if numbers[i] <= numbers[i+1]:
        tmp += 1
        i += 1
    else:
        if tmp > cnt:
            cnt = tmp
            tmp = 1
            i += 1
        else:
            tmp = 1
            i += 1
    if tmp > cnt:
        cnt = tmp

i = 0
tmp = 1
while i < len(numbers) - 1:
    if numbers[i] >= numbers[i+1]:
        tmp += 1
        i += 1
    else:
        if tmp > cnt:
            cnt = tmp
            tmp = 1
            i += 1
        else:
            tmp = 1
            i += 1
    if tmp > cnt:
        cnt = tmp

if N == 1:
    print(1)
else:
    print(cnt)