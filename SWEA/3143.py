T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    a = len(A)
    b = len(B)

    result = 0
    i = 0
    while i < a:
        if A[i:i+b] == B:
            result += 1
            i = i + b
        else:
            i += 1
            result += 1

    print('#{0} {1}'.format(tc, result))