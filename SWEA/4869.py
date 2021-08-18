T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n = N //10

    result = 1
    if N == 10:
        pass
    else:
        i = 0
        while i < n - 1:
            if i % 2:
                result = result * 2 - 1
                i += 1
            else:
                result = result * 2 + 1
                i += 1
    
    print('#{0} {1}'.format(tc, result))