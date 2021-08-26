T = int(input())

for tc in range(1, T+1):
    N, M  = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M):
        n = numbers.pop(0)
        numbers.append(n)

    print('#{0} {1}'.format(tc, numbers[0]))