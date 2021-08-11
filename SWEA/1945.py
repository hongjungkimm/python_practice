T  = int(input())

for tc in range(T):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    
    while True:
        if N % 2 == 0:
            N = N // 2
            a += 1
        elif N % 3 == 0:
            N = N // 3
            b += 1
        elif N % 5 == 0:
            N = N // 5
            c += 1
        elif N % 7 == 0:
            N = N // 7
            d += 1
        elif N % 11 == 0:
            N = N // 11
            e += 1
        elif N % 2 != 0 and N % 3 != 0 and N % 5 != 0 and N % 7 != 0 and N % 11 != 0:
            break
    
    print(f'#{tc+1} {a} {b} {c} {d} {e}')