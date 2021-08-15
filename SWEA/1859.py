T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))[::-1]

    result = 0
    max_idx = 0
    i = 1
    while i < N:
        if prices[max_idx] > prices[i]:
            result += (prices[max_idx] - prices[i])
            i += 1
        else:
            max_idx = i
            i += 1

    print('#{0} {1}'.format(tc, result))