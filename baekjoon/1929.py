import sys

M, N = map(int, sys.stdin.readline().split())

check = [0 for _ in range(N+1)]

for i in range(2, N+1):
    j = 2
    while i * j <= N:
        check[i * j] = 1
        j += 1

if M == 1:
    M = 2
for i in range(M, N+1):
    if check[i] == 0:
        print(i)