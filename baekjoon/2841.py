import sys

N, P = map(int, sys.stdin.readline().split())

melody = [[] for _ in range(7)]

cnt = 0
for _ in range(N):
    n, p = map(int, sys.stdin.readline().split())
    while True:
        if len(melody[n]) == 0 or melody[n][-1] < p:
            melody[n].append(p)
            cnt += 1
            break
        elif melody[n][-1] > p:
            melody[n].pop()
            cnt += 1
        elif melody[n][-1] == p:
            break

print(cnt)