def change(idx, cnt):
    global result
    if idx >= N-1:
        result = cnt
        return
    for i in range(1, charge[idx]+1):
        if cnt+1 < result:
            change(idx+i, cnt+1)

T = int(input())

for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    charge = temp[1:] + [0]
    result = float('inf')
    change(0, -1)

    print('#{0} {1}'.format(tc, result))