import sys # 시간초과

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

n = len(numbers)

cnt = 0
for i in range(1, 1 << n):
    tmp = []
    for j in range(n):
        if i & (1 << j):
            tmp.append(numbers[j])
    print(tmp)
    # if tmp == S:
    #     cnt += 1

# print(cnt)