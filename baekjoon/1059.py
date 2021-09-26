import sys

L = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())

S.sort()
r1 = 0
r2 = 0
for s in S:
    if n > s:
        r1 = s
for s in S:
    if s > r1:
        r2 = s
        break

result = list(range(r1+1, r2))
cnt = 0
for i in range(len(result)):
    for j in range(i+1, len(result)):
        if result[i] <= n <= result[j]:
            cnt += 1

print(cnt)