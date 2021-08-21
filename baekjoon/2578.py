import sys

def check_bingo(list1):
    cnt = 0

    for line in list1:
        if sum(line) == 5:
            cnt += 1

    for i in range(5):
        tmp = 0
        for line in list1:
            tmp += line[i]
        if tmp == 5:
            cnt += 1

    tmp = 0
    for i in range(5):
        tmp += list1[i][i]
    if tmp == 5:
        cnt += 1

    tmp = 0
    for i in range(5):
        tmp += list1[i][4-i]
    if tmp == 5:
        cnt += 1

    return cnt

bingo = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
zero_bingo = [[0] * 5 for _ in range(5)]
numbers = [n for _ in range(5) for n in list(map(int, sys.stdin.readline().split()))]

num_count = 0
is_bingo = False
for n in numbers :
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == n:
                zero_bingo[i][j] = 1
                num_count += 1
                if check_bingo(zero_bingo) >= 3:
                    is_bingo = True
                    break
        if is_bingo:
            break
    if is_bingo:
        break

print(num_count)