import sys

N, M = map(int, sys.stdin.readline().split())

cant_hear = [sys.stdin.readline().rstrip() for _ in range(N)]
cant_see = [sys.stdin.readline().rstrip() for _ in range(M)]

s_cant_hear = set(cant_hear)
s_cant_see = set(cant_see)

remainder = set(s_cant_hear - s_cant_see)
result = list(s_cant_hear - remainder)

print(len(result))
result.sort()
for r in result:
    print(r)