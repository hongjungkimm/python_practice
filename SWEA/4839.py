def binary_search(end, target):
    cnt = 0
    start = 1
    while start <= end:
        middle = int((start + end) / 2)
        if target == middle:
            return cnt
        elif target > middle:
            start = middle
            cnt += 1
        else:
            end = middle
            cnt += 1

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    cnt_A = binary_search(P, A)
    cnt_B = binary_search(P, B)

    if cnt_A == cnt_B:
        print('#{0} 0'.format(tc))
    elif cnt_A < cnt_B:
        print('#{0} A'.format(tc))
    else:
        print('#{0} B'.format(tc))