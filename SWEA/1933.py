N = int(input())

for n in range(1, N+1):
    if N % n == 0:
        print(n, end=' ')