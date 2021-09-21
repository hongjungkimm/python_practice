import sys

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

i = 0
while i < N:
    tmp = 0
    for j in range(N):
        if i != j:
            if numbers[i] % numbers[j] == 0:
                tmp += 1
    print(tmp)
    i += 1